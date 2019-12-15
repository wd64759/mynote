# Docker is Back
## Command

* Basic
``` bash
docker images # 列出本地镜像
docker search ${key-word}  # 搜索服务器镜像
docker pull ubuntu:13.10 # 获取新镜像
docker rmi hello-world   # 删除镜像
docker rm pid 删除容器 # 需要先停止

docker logs -f pid
```

* Run image
``` bash
docker run image:tag # 启动并进入容器 
docker run -it image:tag /bin/bash # 以交互方式运行容器 -i, -t 为启动虚拟终端
docker run --name alpine-dev -p 1022:22 -v d:\tmp:/mnt/tmp -d alpine # -d 为后台运行
docker run -d -p 4200:4200 jared/webctx # 注意在window下的docker容器是跑着虚拟机上的，访问的IP地址需要使用虚拟机启动的ip

docker ps -a # 查看容器（包含停止状态的）

docker run -it -v /test:/soft centos /bin/bash #将宿主机/test目录挂载到/soft
```

* Container 管理
``` bash
docker container ls -a | awk '{print$1}' # 列出所有创建过的容器
docker rm $(docker container ls -qa)  # 删除所有容器
docker container prune # 删除所有容器
```


* Export/Input Images
``` bash
docker container ls
docker save -o abc.tar jarta/jre8:1.0      # 导出镜像到tar文件
docker import jarta_img.tar jarta/jre8:1.0 # 导入文件到镜像
```

* Advanced
``` bash
docker exec -it pid sh # 接入启动的容器

docker build -f /d/code100/js/Dockerfile -t jarta/jre8:1.0 . # 打镜像文件
docker inspect pid # 查看底层信息
docker restart t1  # 重启容器

docker commit afcaf46e8305 centos-vim      # 将容器（参数1为容器ID）打包成镜像centos-vim
docker commit -m="add home folder" -a="tester" 2ac230aabe14 ubuntu:v1 # 改变并提交镜像
```

## Dockerfile
``` docker file
# JDK relies on glibc
FROM docker.io/jeanblanchard/alpine-glibc
# author
LABEL maintainer="wei dong"
# A streamlined jre
ADD jre8.tar.gz /usr/java/jdk/
# set env
ENV JAVA_HOME /usr/java/jdk
ENV PATH ${PATH}:${JAVA_HOME}/bin
# run container with base path
WORKDIR /opt
```

# Alpine Linux
Alpine 中软件安装包的名字可能会与其他发行版有所不同，可以在 https://pkgs.alpinelinux.org/packages 网站搜索
``` bash
apk -h
```
