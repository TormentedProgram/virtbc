import os
import argparse
import textwrap
import sys
import subprocess as cmd

possible_paths = [
    os.path.join(os.path.expanduser("~"),'.bashrc'),
]

modFolder = os.path.join(os.path.expanduser("~"),'.config','virtbc')
modManager = os.path.join(modFolder, "virtbc_commands")

def setup_bashrc_mod():
    venv_path = os.path.join(os.path.expanduser("~"), '.venvs', "virtbc-venv")
    needs_setup = False

    if not os.path.exists(venv_path): # I had a or statement but both were printing and I'm lazy
        needs_setup = True
    if not os.path.exists(modFolder):
        needs_setup = True
    if not os.path.exists(modManager):
        needs_setup = True

    if needs_setup:
        print("Setting up files!")
        if not os.path.exists(venv_path):
            cmd.check_call([sys.executable, "-m", "venv", venv_path])
        if not os.path.exists(modFolder):
            os.makedirs(modFolder, exist_ok=True)
        if not os.path.exists(modManager):
            with open(modManager, 'a'):
                pass
    else:
        print("Files do not need setup!")

def find_bashrc():
    for path in possible_paths:
        if os.path.isfile(path):
            return path
    return None

def remove_command(command):
    currentMod = os.path.join(modFolder, command)
    if os.path.exists(currentMod):
        os.remove(currentMod)
        with open(modManager, 'r') as file:
            lines = file.readlines()
            lines = [line for line in lines if command not in line]
            with open(modManager, 'w') as file:
                file.writelines(lines)
        print(f'Command: "{command}"" removed from VirtualENV successfully!')
    else:
        print("Command not found in database.")

def add_manager_to_bashrc():  
    bashrc_path = find_bashrc()

    with open(bashrc_path, 'r') as file:
        bashrc_file = file.read()
        if "virtbc" in bashrc_file:
            return

    if bashrc_path:
        try:
            with open(bashrc_path, 'a') as bashrc_file:
                bashrc_file.write("\n" + f'#virtbc implementation\nsource {modManager}'.strip())
        except Exception as e:
            print("Error:", e)
    else:
        print("Could not locate .bashrc file.")

def add_function(function_name):  
    currentMod = os.path.join(modFolder, function_name)

    if currentMod:
        venv_path = os.path.join(os.path.expanduser("~"),'.venvs','globalvenv','bin','activate')
        try:
            with open(currentMod, 'a') as bash_mod:
                content = textwrap.dedent(
                    f'''
                    {function_name}() {{
                        source {venv_path}
                        local function_name="${{FUNCNAME[0]}}"
                        local command_name="$(which "$function_name")"
                        "$command_name" "$@"
                        deactivate
                    }}
                ''' + "\n")
                lines = content.split('\n')
                content = '\n'.join(lines[1:])
                bash_mod.write(content)

            with open(modManager, 'a') as bashrc_file: #formats good
                bashrc_file.write(
                    textwrap.dedent(f'''
                    source {currentMod}
                    '''
            .strip() + "\n"))

            print("Function successfully added to .bashrc file:", currentMod)
            os.system("exec bash -l")
            print(".bashrc refreshed successfully.")
        except Exception as e:
            print("Error:", e)

def main():
    parser = argparse.ArgumentParser(description="Allows commands to run inside a VirtualENV without requiring the VENV path.")
    parser.add_argument("command", nargs='?', const='arg_was_not_given', help="Command to add only into VirtualENV.")
    parser.add_argument("--setup", "-s", action="store_true", help="Creates and sets up directories")
    parser.add_argument("--remove", "-r", action="store_true", help="Removes Command from VirtualENV.")
    args = parser.parse_args()

    if args.setup:
        setup_bashrc_mod()
        add_manager_to_bashrc()
    elif args.remove and args.command:
        remove_command(args.command)
    elif args.command:
        function_name = args.command
        add_manager_to_bashrc()
        add_function(function_name)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()