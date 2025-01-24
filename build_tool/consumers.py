# build_tool/consumers.py

# TODO https://channels.readthedocs.io/en/stable/tutorial/part_2.html#write-your-first-consumer
import json
import shlex, subprocess
import os
import threading
from sys import platform

from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

from .models import BuildSession
from .serializers import StepSerializer


class BuildConsumer(WebsocketConsumer):
    # TODO https://www.w3schools.com/python/python_inheritance.asp
    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.command_count = 0
        self.command_threads = {}
        self.command_process = {}
        self.events = {}
        self.thread_outputs = {}
        self.thread_sequence = {}

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]

        self.build_session = BuildSession.objects.get(pk=self.room_name)

        self.accept()

    def disconnect(self, close_code):
        pass

    def run_command_blocking(self, step):
        # TODO https://stackoverflow.com/questions/24306205/file-not-found-error-when-launching-a-subprocess-containing-piped-commands/24306385#24306385

        # TODO https://docs.python.org/3/library/subprocess.html#popen-constructor
        """... If shell is True, it is recommended to pass args as a string rather than as a sequence."""
        completed = subprocess.run(step.command, shell=True, capture_output=True, text=True)

        """
        Note It may not be obvious how to break a shell command into a sequence of arguments, especially in complex cases.
        shlex.split() can illustrate how to determine the correct tokenization for args:
        """
        # args = shlex.split(step.command)
        # completed = subprocess.run(args, shell=True, capture_output=True, text=True)

        stdout = completed.stdout
        stderr = completed.stderr

        if not stdout and not stderr:
            stdout = f'STEP #{step.id}: COMMAND\n {step.command}\n EXECUTED\n\n'

        return stdout, stderr

    def run_steps_non_blocking(self):
        for x, y in self.thread_sequence.items():
            # print(x, y)
            self.build_session.current_step = y['step']
            self.build_session.save()

            try:
                # y['method'](y['step'])
                if y.get('command_arguments'):
                    y['method'](y['step'], y['command_arguments'])
                else:
                    y['method'](y['step'])
            except Exception as e:
                try:
                    stdout = None
                    stderr = str(e)
                    self.socket_send(y['step'], stdout, stderr)
                except:
                    break

        self.send(text_data=json.dumps({"signal": 'finish'}))
                    
    def run_folder_non_blocking(self, step):
        stdout = ''
        stderr = ''
        self.socket_send(step, stdout, stderr, 'loading')

        if platform == "linux" or platform == "linux2":
            # linux
            completed = subprocess.run(f'mkdir -p {step.folder}', capture_output=True, text=True, shell=True)
        elif platform == "darwin":
            # OS X
            completed = subprocess.run(f'mkdir -p {step.folder}', capture_output=True, text=True, shell=True)
        elif platform == "win32":
            # completed = subprocess.run(f'mkdir "{step.folder}"', capture_output=True, text=True, shell=True)
            # TODO https://stackoverflow.com/questions/4165387/create-folder-with-batch-but-only-if-it-doesnt-already-exist/20688004#20688004
            completed = subprocess.run(f'if not exist {step.folder} mkdir {step.folder}', capture_output=True, text=True, shell=True)
            # Windows...
        
        stdout += completed.stdout
        stderr += completed.stderr

        if not stdout and not stderr:
            stdout += f'STEP #{step.id}: FOLDER {step.folder} CREATED\n\n'

        self.socket_send(step, stdout, stderr)

    def run_file_non_blocking(self, step):
        stdout = ''
        stderr = ''
        self.socket_send(step, stdout, stderr, 'loading')

        # os.path.dirname() only removes the lagging quotation
        # we are deliberatly removing quotation and adding it later to avoid syntax error
        dirname = os.path.dirname(step.file_path.strip("\""))

        if platform == "linux" or platform == "linux2":
            # linux
            completed = subprocess.run(f'mkdir -p "{dirname}"', capture_output=True, text=True, shell=True)
        elif platform == "darwin":
            # OS X
            completed = subprocess.run(f'mkdir -p "{dirname}"', capture_output=True, text=True, shell=True)
        elif platform == "win32":
            # completed = subprocess.run(f'mkdir "{dirname}"', capture_output=True, text=True, shell=True)
            # TODO https://stackoverflow.com/questions/4165387/create-folder-with-batch-but-only-if-it-doesnt-already-exist/20688004#20688004
            completed = subprocess.run(f'if not exist "{dirname}" mkdir "{dirname}"', capture_output=True, text=True, shell=True)

        stdout += completed.stdout
        stderr += completed.stderr

        if platform == "linux" or platform == "linux2":
            # linux
            completed = subprocess.run(f'cp "{step.asset.file.path}" {step.file_path}', capture_output=True, text=True, shell=True)
        elif platform == "darwin":
            # OS X
            completed = subprocess.run(f'cp "{step.asset.file.path}" {step.file_path}', capture_output=True, text=True, shell=True)
        elif platform == "win32":
            completed = subprocess.run(f'copy "{step.asset.file.path}" {step.file_path}', capture_output=True, text=True, shell=True)

        stdout += completed.stdout
        stderr += completed.stderr

        if not stdout and not stderr:
            stdout += f'STEP #{step.id}: FILE {step.file_path} CREATED\n\n'

        self.socket_send(step, stdout, stderr)

    def run_excerpt_non_blocking(self, step):
        stdout = ''
        stderr = ''
        self.socket_send(step, stdout, stderr, 'loading')

        # TODO https://stackoverflow.com/questions/31261123/insert-text-in-between-file-lines-in-python/31261196#31261196
                
        filename = step.file_path.strip("\"")
        new_filename = f'{step.file_path}__new'

        try:
            # STEP 1: Duplicate & clear content between excerpt markers
            try:
                # TODO https://stackoverflow.com/questions/2769061/how-to-erase-the-file-contents-of-text-file-in-python/2769090#2769090
                open(new_filename, 'w').close()

                with open(filename, "r") as prev_file, open(new_filename, "w") as new_file:
                    prev_contents = prev_file.readlines()
                    #Now prev_contents is a list of strings and you may add the new line to this list at any position
                    found_start_marker = False
                    found_end_marker = False
                    # can_write = True // Using found_start_marker and found_end_marker instead
                    for line in prev_contents:
                        if line.find(step.excerpt_start) != -1:
                            found_start_marker = True

                            # can_write = False
                            new_file.write(line)
                            continue

                        if line.find(step.excerpt_end) != -1:
                            found_end_marker = True

                            # can_write = True
                            new_file.write('\n')

                        # if can_write:
                        if not found_start_marker or found_end_marker:
                            new_file.write(line)

                excerpt_error = ''
                if not found_start_marker:
                    excerpt_error += f'EXCERPT START MARKER ({step.excerpt_start}) NOT FOUND\n'

                if not found_end_marker:
                    excerpt_error += f'EXCERPT END MARKER ({step.excerpt_end}) NOT FOUND\n'

                if excerpt_error:
                    excerpt_error += f'FILE ({step.file_path})\n'
                    raise Exception(excerpt_error)
                
            except Exception as e:
                raise Exception(f'STEP #{step.id}: {str(e)}')
            

            # STEP 2: Overwrite the orginal & remove the duplicate
            if platform == "linux" or platform == "linux2":
                # linux
                completed = subprocess.run(f'cp "{new_filename}" "{filename}"', capture_output=True, text=True, shell=True)
            elif platform == "darwin":
                # OS X
                completed = subprocess.run(f'cp "{new_filename}" "{filename}"', capture_output=True, text=True, shell=True)
            elif platform == "win32":
                completed = subprocess.run(f'copy "{new_filename}" "{filename}"', capture_output=True, text=True, shell=True)

            stdout += completed.stdout
            stderr += completed.stderr

            # STEP 3: Insert Excerpt
            try:
                # TODO https://pynative.com/python-search-for-a-string-in-text-files/
                with open(filename, "w") as original, open(new_filename, "r") as duplicate:
                    # read all lines in a list
                    lines = duplicate.readlines()
                    for line in lines:
                        # check if string present on a current line
                        if line.find(step.excerpt_start) != -1:
                            line_to_add = lines.index(line) + 1
                            break

                    lines.insert(line_to_add, step.excerpt)
                    original.write("".join(lines))
                    
            except Exception as e:
                raise Exception(f'STEP #{step.id}: {str(e)}')

            # STEP 4: Delete the duplicate
            if platform == "linux" or platform == "linux2":
                # linux
                completed = subprocess.run(f'rm "{new_filename}"', capture_output=True, text=True, shell=True)
            elif platform == "darwin":
                # OS X
                completed = subprocess.run(f'rm "{new_filename}"', capture_output=True, text=True, shell=True)
            elif platform == "win32":
                completed = subprocess.run(f'del "{new_filename}"', capture_output=True, text=True, shell=True)
            
            stdout += completed.stdout
            stderr += completed.stderr

        except Exception as e:
            stderr += f'{str(e)}\n\n'
            self.socket_send(step, stdout, stderr, 'loading')

        if not stdout and not stderr:
            stdout += f'STEP #{step.id}: EXCERPT\n {step.excerpt}\n ADDED\n\n'

        self.socket_send(step, stdout, stderr)

    def run_command_non_blocking(self, step, command_arguments=None):
        stdout = ''
        stderr = ''
        self.socket_send(step, stdout, stderr, 'loading')

        # args = shlex.split(step.command)
        # with subprocess.Popen(args, stdout=subprocess.PIPE, shell=True) as proc:
            # log.write(proc.stdout.read())
        """
        ... Additionally, stderr can be STDOUT, which indicates that the stderr data from the applications should be captured into the same file handle as for stdout.
        """
        # self.command_process[f"{step.id}"] = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) # does not well for multiline commands
        # self.command_process[f"{step.id}"] = subprocess.Popen(step.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        if command_arguments:
            self.command_process[f"{step.id}"] = subprocess.Popen(f"{step.command} --command_arguments {command_arguments}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        else:
            self.command_process[f"{step.id}"] = subprocess.Popen(step.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            
        # <<<<<<<<<<>>>>>>>
        # OPTION 1 - not working
        # + https://docs.python.org/3/library/subprocess.html#subprocess.Popen.stderr
        """Warning Use communicate() rather than .stdin.write, .stdout.read or .stderr.read to avoid deadlocks due to any of the other OS pipe buffers filling up and blocking the child process."""
        # self.thread_outputs['stdout'] = self.command_process[f"{step.id}"].stdout.read().decode()
        # self.thread_outputs['stderr'] = self.command_process[f"{step.id}"].stderr.read().decode()
        # <<<<<<<<<<>>>>>>>
        # <<<<<<<<<<>>>>>>>
        # OPTION 2
        outs, errs = self.command_process[f"{step.id}"].communicate()
        self.thread_outputs['stdout'] = outs.decode()
        self.thread_outputs['stderr'] = errs.decode()
        # <<<<<<<<<<>>>>>>>
        
        stdout += self.thread_outputs['stdout']
        stderr += self.thread_outputs['stderr']
        self.socket_send(step, stdout, stderr, 'success')
            
    def socket_send(self, step, stdout, stderr, default_status=None):
        report_data = {
            'step': StepSerializer(step).data
        }
        
        try:
            # <<<<<>>>>
            if stdout:
                self.build_session.logs += stdout
                self.build_session.save()
                self.send(text_data=json.dumps({"logs": stdout}))

                report_data['status'] = 'success'
                self.send(text_data=json.dumps({"report": report_data}))

            if stderr:
                self.build_session.logs += stderr
                self.build_session.save()
                self.send(text_data=json.dumps({"logs": stderr}))

                report_data['status'] = 'failure'
                self.send(text_data=json.dumps({"report": report_data}))
                # break
                raise Exception
            
            if default_status:
                report_data['status'] = default_status
                self.send(text_data=json.dumps({"report": report_data}))
        except Exception as e:
            # The message "Attempt to send on a closed protocol"
            # was observed when using CI/CD callback function.
            # This was probably due to the connection being closed by
            # the webhook server after sending the data.
            # To keep the websocket event loop (since it serving as a task queue)
            # we check for that specific error.
            # + https://stackoverflow.com/questions/62847184/disconnect-method-of-django-channels-websocketconsumer-not-being-called
            if "closed protocol" in str(e):
                return
            
            raise e
    
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        # self.send(text_data=json.dumps({"message": message}))

        if message == 'rerun':
            self.build_session.logs = ''
            self.build_session.current_step = None
            self.build_session.save()

        if message == 'stop':
            self.send(text_data=json.dumps({"signal": 'stop'}))
            if self.command_process:
                self.command_threads = {}
                for x, y in self.command_process.items():
                    # print(x, y)
                    y.terminate()
                self.command_process = {}
                return

        project = self.build_session.project
        steps = self.build_session.project.steps.all().order_by('rank')

        self.send(text_data=json.dumps({"signal": 'start'}))

        can_run = False
        for step in steps:
            if step.is_suspended:
                continue
            
            # if current_step is set, start from it otherwise skip all
            # steps before it. Run all steps from the current_step onwords
            if self.build_session.current_step and not can_run:
                if step == self.build_session.current_step or step.rank >= self.build_session.current_step.rank:
                    can_run = True

                if not can_run:
                    continue
            
            stdout = ''
            stderr = ''
            try:
                self.socket_send(step, stdout, stderr, 'setup')
            except:
                break
            
            self.command_count+=1

            if step.category == 'folder':
                self.thread_sequence[f"{self.command_count}"] = {
                    'method': self.run_folder_non_blocking,
                    'step': step
                }
                
            if step.category == 'file':
                self.thread_sequence[f"{self.command_count}"] = {
                    'method': self.run_file_non_blocking,
                    'step': step
                }
                
            if step.category == 'excerpt':
                self.thread_sequence[f"{self.command_count}"] = {
                    'method': self.run_excerpt_non_blocking,
                    'step': step
                }
                
            if step.category == 'command':
                self.thread_sequence[f"{self.command_count}"] = {
                    'method': self.run_command_non_blocking,
                    'step': step,
                    'command_arguments': self.build_session.command_arguments
                }
                
        self.command_threads[f"1"] = threading.Thread(target=self.run_steps_non_blocking)
        # self.command_threads[f"1"] = threading.Thread(target=self.run_steps_non_blocking, daemon=True)
        self.command_threads[f"1"].start()
        
        if not self.command_threads:
            self.send(text_data=json.dumps({"signal": 'finish'}))