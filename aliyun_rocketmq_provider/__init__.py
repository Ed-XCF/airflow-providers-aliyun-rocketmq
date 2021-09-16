with open("version", "r") as fh:
    version = fh.read()

def get_provider_info():
    return {
        "package-name": "apache-airflow-providers-aliyun-rocketmq",
        "name": "Aliyun RocketMQ Airflow Provider",
        "description": "Airflow provider for aliyun rocketmq",
        "hook-class-names": ["aliyun_rocketmq_provider.hooks.aliyun_rocketmq.AliyunRocketMQHook"],
        "versions": [version]
    }
