import os
import sys

modFolder = os.path.join(os.path.expanduser("~"),'.config','virtbc')
modManager = os.path.join(modFolder, "virtbc_commands")

def setup_bashrc_mod():
    os.makedirs(modFolder, exist_ok=True)
    with open(modManager, 'a'):
        pass

def find_bashrc():
    # Default paths where .bashrc is commonly located
    possible_paths = [
        os.path.join(os.path.expanduser("~"),'.bashrc'),
    ]

    for path in possible_paths:
        if os.path.isfile(path):
            return path

    return None

def add_manager_to_bashrc():  
    setup_bashrc_mod()
    bashrc_path = find_bashrc()

    if bashrc_path:
        function_code = f'''
#virtbc implementation
source {modManager}
        '''

        try:
            with open(bashrc_path, 'a') as bashrc_file:
                bashrc_file.write(function_code)
        except Exception as e:
            print("Error:", e)
    else:
        print("Could not locate .bashrc file.")

def add_function(function_name):  
    currentMod = os.path.join(modFolder, function_name)
    bashrc_path = find_bashrc()

    if currentMod:
        vert_path = os.path.join(os.path.expanduser("~"),'.venvs','globalvenv','bin','activate')
        function_code = f'''
{function_name}() {{
    source {vert_path}
    local function_name="${{FUNCNAME[0]}}"
    local command_name="$(which "$function_name")"
    "$command_name" "$@"
    deactivate
}}
        '''

        try:
            with open(currentMod, 'a') as bash_mod:
                bash_mod.write(function_code)

            with open(modManager, 'a') as bashrc_file:
                bashrc_file.write(f'''
source {currentMod}
''')

            print("Function successfully added to .bashrc file:", currentMod)
            os.system("exec bash -l")
            print(".bashrc refreshed successfully.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: virtbc (command)")
    else:
        function_name = sys.argv[1]
        add_manager_to_bashrc()
        add_function(function_name)
