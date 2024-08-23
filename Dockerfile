FROM ubuntu:22.04
WORKDIR /app

# 使用 & 来连接命令可能不会按预期工作，因为它们是在同一个RUN指令中执行的。
# 建议将每个命令放在单独的RUN指令中，以确保正确执行和层的缓存。

# 安装构建工具和依赖项
RUN apt-get update && \
    apt-get remove -y openjdk-11-jdk && \
    apt-get install -y openjdk-17-jdk && \
    apt-get install -y build-essential && \
    apt-get install -y cmake && \
    apt-get install -y wget && \
    apt-get install -y unzip && \
    apt-get install -y htop && \
    apt-get install -y git && \
    apt-get install -y python3-pip && \
    apt-get install -y tmux
RUN wget https://www.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz && \
    tar -xzvf apache-maven-3.9.9-bin.tar.gz -C /opt && \
    ln -s /opt/apache-maven-3.9.9/bin/mvn /usr/bin/mvn
RUN pip install ftfy