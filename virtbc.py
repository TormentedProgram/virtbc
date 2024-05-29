import os
import sys

def find_bashrc():
    # Default paths where .bashrc is commonly located
    possible_paths = [
        os.path.join(os.path.expanduser("~"),'.bashrc'),
    ]

    for path in possible_paths:
        if os.path.isfile(path):
            return path

    return None

def add_function_to_bashrc(function_name):  
    bashrc_path = find_bashrc()

    if bashrc_path:
        
        function_code = """
{}() {{
    source /home/tormented/.venvs/globalvenv/bin/activate
    local function_name="${{FUNCNAME[0]}}"
    local command_name="$(which "$function_name")"
    if [ -z "$command_name" ]; then
        echo "Command not found!"
        return 1
    fi
    "$command_name" "$@"
    deactivate
}}
        """.format(function_name)

        try:
            with open(bashrc_path, 'a') as bashrc_file:
                bashrc_file.write(function_code)
            print("Function successfully added to .bashrc file:", bashrc_path)
            os.system("exec bash -l")
            print(".bashrc refreshed successfully.")
        except Exception as e:
            print("Error:", e)
    else:
        print("Could not locate .bashrc file.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: virtc function_name")
    else:
        function_name = sys.argv[1]
        add_function_to_bashrc(function_name)
