import boto3

from logger import logger


def list_regions():
    ec2_client = boto3.client(service_name="ec2")
    try:
        response = ec2_client.describe_regions()
        return [region["RegionName"] for region in response["Regions"]]
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return []


def describe_ec2_instances(region):
    ec2_client = boto3.client(service_name="ec2", region_name=region)
    try:
        response = ec2_client.describe_instances()
        return response["Reservations"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_rds_instances(region):
    rds_client = boto3.client(service_name="rds", region_name=region)
    try:
        response = rds_client.describe_db_instances()
        return response["DBInstances"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_s3_instances(region):
    s3_client = boto3.client(service_name="s3", region_name=region)
    try:
        response = s3_client.list_buckets()
        return response["Buckets"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_elb_instances(region):
    elb_client = boto3.client(service_name="elb", region_name=region)
    try:
        response = elb_client.describe_load_balancers()
        return response["LoadBalancerDescriptions"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_route53_instances(region):
    route53_client = boto3.client(service_name="route53", region_name=region)
    try:
        response = route53_client.list_hosted_zones()
        return response["HostedZones"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def list_services_by_region():
    regions = list_regions()
    results = {}
    for region in regions:
        ec2_instances = {}
        for reservation in describe_ec2_instances(region=region):
            ec2_instances[reservation] = [
                instance["InstanceId"] for instance
                in reservation["Instances"]
            ]

        rds_instances = [
            instance["DBInstanceIdentifier"] for instance
            in describe_rds_instances(region=region)
        ]

        s3_buckets = [
            bucket["Name"] for bucket
            in describe_s3_instances(region=region)
        ]

        elb_instances = [
            elb["LoadBalancerName"] for elb
            in describe_elb_instances(region=region)
        ]

        route_53_instances = [
            hosted_zone["Name"] for hosted_zone
            in describe_route53_instances(region=region)
        ]

        results[region] = {
            "ec2": ec2_instances,
            "rds": rds_instances,
            "s3": s3_buckets,
            "elb": elb_instances,
            "route53": route_53_instances,
        }
    return results


if __name__ == "__main__":
    results = list_services_by_region()
    logger.info(results)
    logger.info(results["us-east-1"])
    logger.info("SUCCESS")
