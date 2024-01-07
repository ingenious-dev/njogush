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
        self.command_thread = None
        self.command_process = None

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

    def run_command_non_blocking(self, step, index):
        args = shlex.split(step.command)
        # with subprocess.Popen(args, stdout=subprocess.PIPE, shell=True) as proc:
            # log.write(proc.stdout.read())
        """
        ... Additionally, stderr can be STDOUT, which indicates that the stderr data from the applications should be captured into the same file handle as for stdout.
        """
        self.command_process = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        self.send(text_data=json.dumps({"logs": self.command_process.stdout.read().decode()}))
        # self.send(text_data=json.dumps({"logs": self.command_process.stderr.read().decode()}))

        report_data = {
            'step': StepSerializer(step).data,
            'status': 'success'
        }
        self.send(text_data=json.dumps({"report": report_data}))

        if index == self.command_count:
            self.send(text_data=json.dumps({"signal": 'finish'}))

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
                self.command_thread = None
                self.command_process.terminate()
                self.command_process = None
                return

        project = self.build_session.project
        steps = self.build_session.project.steps.all().order_by('rank')

        self.send(text_data=json.dumps({"signal": 'start'}))

        can_run = False
        for step in steps:
            # if current_step is set, start from it otherwise skip all
            # steps before it. Run all steps from the current_step onwords
            if self.build_session.current_step and not can_run:
                if step == self.build_session.current_step or step.rank >= self.build_session.current_step.rank:
                    can_run = True

                if not can_run:
                    continue
            
            self.build_session.current_step = step
            self.build_session.save()

            report_data = {
                'step': StepSerializer(step).data
            }

            report_data['status'] = 'loading'
            self.send(text_data=json.dumps({"report": report_data}))

            stdout = ''
            stderr = ''
            if step.category == 'folder':
                if platform == "linux" or platform == "linux2":
                    # linux
                    completed = subprocess.run(f'mkdir -p "{step.folder}"', capture_output=True, text=True, shell=True)
                elif platform == "darwin":
                    # OS X
                    completed = subprocess.run(f'mkdir -p "{step.folder}"', capture_output=True, text=True, shell=True)
                elif platform == "win32":
                    # completed = subprocess.run(f"mkdir {step.folder}", capture_output=True, text=True, shell=True)
                    # TODO https://stackoverflow.com/questions/4165387/create-folder-with-batch-but-only-if-it-doesnt-already-exist/20688004#20688004
                    completed = subprocess.run(f'if not exist "{step.folder}\" mkdir "{step.folder}"', capture_output=True, text=True, shell=True)
                    # Windows...
                
                stdout += completed.stdout
                stderr += completed.stderr

                if not stdout and not stderr:
                    stdout += f'STEP #{step.id}: FOLDER {step.folder} CREATED\n\n'
                
            if step.category == 'file':
                dirname = os.path.dirname(step.file_path)

                if platform == "linux" or platform == "linux2":
                    # linux
                    completed = subprocess.run(f'mkdir -p "{dirname}"', capture_output=True, text=True, shell=True)
                elif platform == "darwin":
                    # OS X
                    completed = subprocess.run(f'mkdir -p "{dirname}"', capture_output=True, text=True, shell=True)
                elif platform == "win32":
                    # completed = subprocess.run(f"" f"mkdir {dirname}", capture_output=True, text=True, shell=True)
                    # TODO https://stackoverflow.com/questions/4165387/create-folder-with-batch-but-only-if-it-doesnt-already-exist/20688004#20688004
                    completed = subprocess.run(f'if not exist "{dirname}\" mkdir "{dirname}"', capture_output=True, text=True, shell=True)

                stdout += completed.stdout
                stderr += completed.stderr

                if platform == "linux" or platform == "linux2":
                    # linux
                    completed = subprocess.run(f"cp {step.asset.file.path} {step.file_path}", capture_output=True, text=True, shell=True)
                elif platform == "darwin":
                    # OS X
                    completed = subprocess.run(f"cp {step.asset.file.path} {step.file_path}", capture_output=True, text=True, shell=True)
                elif platform == "win32":
                    completed = subprocess.run(f"copy {step.asset.file.path} {step.file_path}", capture_output=True, text=True, shell=True)

                stdout += completed.stdout
                stderr += completed.stderr

                if not stdout and not stderr:
                    stdout += f'STEP #{step.id}: FILE {step.file_path} CREATED\n\n'

            if step.category == 'excerpt':
                # TODO https://stackoverflow.com/questions/31261123/insert-text-in-between-file-lines-in-python/31261196#31261196
                
                filename = step.file_path
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
                        completed = subprocess.run(f"cp {new_filename} {filename}", capture_output=True, text=True, shell=True)
                    elif platform == "darwin":
                        # OS X
                        completed = subprocess.run(f"cp {new_filename} {filename}", capture_output=True, text=True, shell=True)
                    elif platform == "win32":
                        completed = subprocess.run(f"copy {new_filename} {filename}", capture_output=True, text=True, shell=True)

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
                        completed = subprocess.run(f"rm {new_filename}", capture_output=True, text=True, shell=True)
                    elif platform == "darwin":
                        # OS X
                        completed = subprocess.run(f"rm {new_filename}", capture_output=True, text=True, shell=True)
                    elif platform == "win32":
                        completed = subprocess.run(f"del {new_filename}", capture_output=True, text=True, shell=True)
                    
                    stdout += completed.stdout
                    stderr += completed.stderr

                except Exception as e:
                    stderr += f'{str(e)}\n\n'
                    self.send(text_data=json.dumps({"logs": stderr}))

                    report_data['status'] = 'failure'
                    self.send(text_data=json.dumps({"report": report_data}))
                    break

                if not stdout and not stderr:
                    stdout += f'STEP #{step.id}: EXCERPT\n {step.excerpt}\n ADDED\n\n'

            if step.category == 'command':
                # OPTION 1 - not ideal for long running process (see OPTION 2)
                # stdout, stderr = self.run_command_blocking(step)

                # OPTION 2
                self.command_count+=1
                self.command_thread = threading.Thread(target=self.run_command_non_blocking, args=(step, self.command_count))
                self.command_thread.start()
                
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
                break
        
        if not self.command_thread:
            self.send(text_data=json.dumps({"signal": 'finish'}))