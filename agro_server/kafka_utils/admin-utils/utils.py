from confluent_kafka.admin import AdminClient,NewTopic,ConfigResource



def create_base_input_topic(kafka_admin_client:AdminClient, topic_name:str, partitions:int, replication_factor:int=1, retention_ms:int=6000000):
    topic_metadata = kafka_admin_client.list_topics(topic=topic_name, timeout=-1)
    if topic_metadata is None:  
        kafka_admin_client.create_topics([NewTopic(topic_name, partitions, replication_factor)])
    alter_topics_properties(kafka_admin_client, topic_name, **{'retention.ms':retention_ms})

def alter_topics_properties(kafka_admin_client:AdminClient, *topics,**base_properties):
    alter_config_list=[]
    for topic in topics:
        alter_config_list.append(ConfigResource(restype='TOPIC', name=topic, set_config=base_properties, described_configs=None, error=None))
    kafka_admin_client.alter_configs(resources=alter_config_list, validate_only=False)

# TODO: check consumers and partitions number equality
# TODO: check retention policy effectivity 
# TODO: alter partition number in input topic
# TODO: think about anything else   
    