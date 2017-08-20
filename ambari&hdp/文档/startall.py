import os
import sys


kafkapath='/home/app/kafka_2.11-0.9.0.0'

carpopath='/home/app/carpo-2.0-b40-2016-11-25'


def startMysql():
    os.system('service mysqld start')

def startCarpoAndKafka():
    if os.getcwd() !=kafkapath:
        os.chdir(kafkapath)
    os.system('bin/zookeeper-server-start.sh config/zookeeper.properties &')
    os.system('bin/kafka-server-start.sh config/server.properties &')

    if os.getcwd() !=carpopath:
        os.chdir(carpopath)
    os.system('bin/start-all.sh &')



if __name__=='__main__':
   startMysql()
   startCarpoAndKafka()


