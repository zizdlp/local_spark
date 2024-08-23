CURRENT_DIR := $(shell pwd)
run_base:
	docker run -itd -v  ${CURRENT_DIR}:/app --name ubuntu_base ubuntu:22.04
use_base:
	docker exec -it ubuntu_base bash
update_mvn:
	apt-get remove -y maven
	# Install Maven 3.9.9
	apt-get update
	apt-get install -y wget
	wget https://www.apache.org/dist/maven/maven-3/3.9.9/binaries/apache-maven-3.9.9-bin.tar.gz
	tar -xzvf apache-maven-3.9.9-bin.tar.gz -C /opt
	ln -s /opt/apache-maven-3.9.9/bin/mvn /usr/bin/mvn
set_env:
	export SPARK_HOME=/app/spark
	export PATH=$SPARK_HOME/bin:$PATH
local_test:
	spark-submit --master local[4] tests/base_test.py > logs/base_test.log 2>&1
	cat logs/base_test.log | grep "mydebug:"