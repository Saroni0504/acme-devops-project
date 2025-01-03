import boto3
from concurrent.futures import ThreadPoolExecutor, as_completed
from logger import logger
from typing import List, Dict, Any


def list_regions() -> List[str]:
    """
    Retrieves a list of all available AWS regions.

    """
    ec2_client = boto3.client(service_name="ec2")
    try:
        response = ec2_client.describe_regions()
        return [region["RegionName"] for region in response["Regions"]]
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        return []


def describe_ec2_instances(region: str) -> List[Dict[str, Any]]:
    """
    Describes EC2 instances in a specified AWS region.
    Reservations contain a list of instances. Each instance has an instance ID.

    """
    ec2_client = boto3.client(service_name="ec2", region_name=region)
    try:
        response = ec2_client.describe_instances()
        return response["Reservations"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_rds_instances(region: str) -> List[Dict[str, Any]]:
    """
    Describes RDS instances in a specified AWS region.

    """
    rds_client = boto3.client(service_name="rds", region_name=region)
    try:
        response = rds_client.describe_db_instances()
        return response["DBInstances"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_s3_instances(region: str) -> List[Dict[str, Any]]:
    """
    Lists all S3 buckets available in the specified AWS region.

    """
    s3_client = boto3.client(service_name="s3", region_name=region)
    try:
        response = s3_client.list_buckets()
        return response["Buckets"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def describe_elb_instances(region: str) -> List[Dict[str, Any]]:
    """
    Describes ELB instances in a specified AWS region.

    """
    elb_client = boto3.client(service_name="elb", region_name=region)
    try:
        response = elb_client.describe_load_balancers()
        return response["LoadBalancerDescriptions"]
    except Exception as e:
        logger.error(f"An error occurred in {region}: {e}")
        return []


def fetch_region_services(region: str) -> Dict[str, Any]:
    """
    Fetches all services (EC2, RDS, S3, ELB) for a given region.

    """
    ec2_instances = {}
    for reservation in describe_ec2_instances(region=region):
        ec2_instances[reservation] = [
            instance["InstanceId"] for instance in reservation["Instances"]
        ]

    rds_instances = [
        instance["DBInstanceIdentifier"]
        for instance in describe_rds_instances(region=region)
    ]

    s3_buckets = [
        bucket["Name"] for bucket in describe_s3_instances(region=region)
    ]

    elb_instances = [
        elb["LoadBalancerName"] for elb in describe_elb_instances(region=region)
    ]

    return {
        "region": region,
        "services": {
            "ec2": ec2_instances,
            "rds": rds_instances,
            "s3": s3_buckets,
            "elb": elb_instances,
        },
    }


def list_services_by_region() -> Dict[str, Any]:
    """
    Lists all services for each AWS region by fetching data in parallel.

    """
    regions = list_regions()
    results = {}
    with ThreadPoolExecutor() as executor:
        future_to_region = {
            executor.submit(fetch_region_services, region): region for region in regions
        }
        for future in as_completed(future_to_region):
            region = future_to_region[future]
            try:
                result = future.result()
                results[result["region"]] = result["services"]
            except Exception as e:
                logger.error(f"An error occurred processing {region}: {e}")
    return results


if __name__ == "__main__":
    results = list_services_by_region()
    logger.info(results)
    logger.info(results["us-east-1"])
    logger.info("SUCCESS")
