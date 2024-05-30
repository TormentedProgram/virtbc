# Virtual Bash Command // virtbc
This is designed to bypass venv global restrictions and allow users to run commands
Such as pip, mov-cli without being harassed by errors stating you cannot do thing outside of a venv
Don't get me wrong this still uses a venv however it's a cleaner safer method then removing the safety features.

# Installation Method 1
~~~
cd ~
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz
cd virtbc-main/scripts
pip install . --break-system-packages
cd ~
~~~

# Uninstallation Method 1
~~~
pip remove virtbc --break-system-packages
~~~

# Installation Method 2
~~~
cd ~
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz
cd virtbc-main
./install.sh
cd ~
~~~

# Uninstallation Method 2
~~~
cd ~
mkdir virtbc-main
curl -L https://github.com/TormentedProgram/virtbc/archive/master.tar.gz | tar xz --wildcards '*uninstall.sh' -C virtbc-main
cd virtbc-main
./uninstall.sh
rm -rf ~/virtbc-main
cd ~
~~~
