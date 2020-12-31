# Kafka Python Spammer

A very simple app that allows you to send messages to a Kafka Topic.  Inpired from [kafka-spammer](https://github.com/redhat-developer-demos/kafka-spammer) which is originally written in Quarkus.

## Usage

To run it in your OpenShift cluster, just `oc run`, making sure to pass in a few environment arguments so that the messages can get to the right place.

1. KAFKA_BOOTSTRAP_HOST - Kafka bootstrap host
2. KAFKA_BOOTSTRAP_PORT - Kafka bootstrap port, defaults to 9092
3. TOPIC_NAME - Kafka topic name
4. TIMES - Number of messages you want to send

```
oc run kafka-spammer-$USER_NUMBER -it --image=jonnyman9/kafka-python-spammer:latest --rm=true --restart=Never --env KAFKA_BOOTSTRAP_HOST=my-cluster-kafka-bootstrap.kafka --env TOPIC_NAME=my-topic-$USER_NUMBER --env TIMES=20
```
