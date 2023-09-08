from settings.read_config import input_topic_name, default_partitions, default_consumer_group_name, historic_data_listener_group_name
from confluent_kafka.admin import AdminClient,NewTopic,ConfigResource
from kafka_utils.admin import check_consumers

def create_consumer(client:AdminClient,is_creation_allowed:bool,consumer_group:str,topic_name:str):
    if check_consumers(topic_name, default_partitions): 
        client.crea
    pass

def shoutdown_consumer(client:AdminClient,id):
    pass

def define_new_consumer_group(client:AdminClient, group_name):
    pass

def get_consumer_info(client:AdminClient, topic:str):
    pass
