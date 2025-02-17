from models.logmaker import LogMaker
from models.rabbitmq import RabbitMQ


def publish_test_message():
    rabbitmq = RabbitMQ()
    log_maker = LogMaker()
    logs = log_maker.simulate_logs(num_entries=10)
    try:
        for entry in logs:
            rabbitmq.publish(queue_name='test_queue', message=str(entry))
            print("Test message published successfully.")
    except Exception as e:
        print(f"Failed to publish test message: {e}")
    finally:
        rabbitmq.close()


if __name__ == "__main__":
    publish_test_message()
