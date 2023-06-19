# RestApi_Kafka_Python
Get real data from API using Kafka and Streamlit python

To run Kafka install kafka and run following commands on windows environment 

zookeeper-server-start.bat ..\..\config\zookeeper.properties
kafka-server-start.bat ..\..\config\server.properties
kafka-topics.bat --create --topic my-topic1 --bootstrap-server localhost:9092 --replication-factor 1 --partitions 3
kafka-console-producer.bat --broker-list localhost:9092 --topic my-topic1
kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic my-topic1 --from-beginning

![Project_Sample](https://github.com/PrasannaYelsan/RestApi_Kafka_Python/assets/72689004/f69a2e4c-2297-41d6-b8e8-6491a888978c)
