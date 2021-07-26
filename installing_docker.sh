sudo yum remove docker docker-client docker-client-latest docker-common docker-latest docker-latest-logrotate docker-logrotate docker-selinux docker-engine-selinux docker-engine
sudo yum install -y yum-utils
sudo yum install -y device-mapper-persistent-data
sudo yum install -y lvm2
sudo yum-config-manager \
--add-repo \
https://download.docker.com/linux/centos/docker-ce.repo
sudo yum install -y docker-ce
sudo yum install -y docker-ce-cli
sudo yum install -y containerd.io
sudo systemctl start docker
sudo docker run hello-world
