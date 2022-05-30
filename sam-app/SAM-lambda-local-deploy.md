### Install sam cli ###

```
wget https://github.com/aws/aws-sam-cli/releases/download/v1.50.0/aws-sam-cli-linux-x86_64.zip

unzip aws-sam-cli-linux-x86_64.zip -d sam-installation

sudo ./sam-installation/install
sam --version

```

<i>optional - upgrade to python3.9</i>
```
sudo apt update
sudo apt install python3.9

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.[old-version] 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

sudo update-alternatives --config python3

sudo rm /usr/bin/python3
sudo ln -s python3.9 /usr/bin/python3
python3 --version

sudo apt-get install python3-pip

# step to fix the below sudo apt-get update issue for broken python3 createdb error

cd /usr/lib/python3/dist-packages
ls -la /usr/lib/python3/dist-packages
sudo cp apt_pkg.cpython-36m-x86_64-linux-gnu.so apt_pkg.so

```

<u>error details</u>
```
Traceback (most recent call last):
  File "/usr/lib/cnf-update-db", line 8, in <module>
    from CommandNotFound.db.creator import DbCreator
  File "/usr/lib/python3/dist-packages/CommandNotFound/db/creator.py", line 11, in <module>
    import apt_pkg
ModuleNotFoundError: No module named 'apt_pkg'
Reading package lists... Done
E: Problem executing scripts APT::Update::Post-Invoke-Success 'if /usr/bin/test -w /var/lib/command-not-found/ -a -e /usr/lib/cnf-update-db; then /usr/lib/cnf-update-db > /dev/null; fi'
E: Sub-process returned an error code
```

### Install Docker for loacl lambda test ###

```
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

sudo mkdir -p /etc/apt/keyrings

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

 echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

```