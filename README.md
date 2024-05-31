# Virtual Bash Command // virtbc
This is designed to bypass venv global restrictions and allow users to run commands
Such as pip, mov-cli without being harassed by errors stating you cannot do thing outside of a venv
Don't get me wrong this still uses a venv however it's a cleaner safer method then removing the safety features.

# Recommended Installation
~~~
cd /tmp/
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz
pip install ./virtbc-main/scripts/. --break-system-packages
virtbc --setup
cd ~
~~~

# Alternative Installation
~~~
cd /tmp/
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz
cd virtbc-main
./install.sh
cd ~
~~~

# Uninstallation
~~~
cd /tmp/
mkdir virtbc-main
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz --wildcards '*uninstall.sh' -C virtbc-main
cd virtbc-main
pip uninstall virtbc -y --break-system-packages
./uninstall.sh
rm -rf ~/virtbc-main
cd ~
~~~
