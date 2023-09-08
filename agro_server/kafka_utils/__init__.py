from settings.read_config import bootstrap_server
from confluent_kafka.admin import AdminClient

admin_client = AdminClient({
    "bootstrap.servers": bootstrap_server
})