from kafka import KafkaProducer
from os import getenv

bootstrap_server_host = getenv('KAFKA_BOOTSTRAP_HOST', 'localhost')
bootstrap_server_port = getenv('KAFKA_BOOTSTRAP_PORT', '9092')
topic_name = getenv('TOPIC_NAME', 'my-topic')
times = int(getenv('TIMES', 1))
uri = f'{bootstrap_server_host}:{bootstrap_server_port}'

try:
    producer = KafkaProducer(bootstrap_servers=uri, acks=0, retries=5, batch_size=1)
    for i in range(times):
        message = f'{{ "message": "Sending Message: {i}" }}'
        producer.send(topic_name, message.encode())
    print(f'Kafka Bootstrap Server: {uri}')
    print(f'Topic: {topic_name}')
    print(f'Sent {times} messages')
finally:
    if producer is not None:
        producer.flush()
        producer.close()
