# File: awsec2_consts.py
# Copyright (c) 2019 Splunk Inc.
#
# SPLUNK CONFIDENTIAL - Use or disclosure of this material in whole or in part
# without a valid written license from Splunk Inc. is PROHIBITED.
# Define your constants here

EC2_JSON_ACCESS_KEY = "access_key"
EC2_JSON_SECRET_KEY = "secret_key"
EC2_JSON_REGION = "region"
EC2_MAX_RESULTS_LIMIT = 1000

EC2_REGION_DICT = {
        "US East (Ohio)": "us-east-2",
        "US East (N. Virginia)": "us-east-1",
        "US West (N. California)": "us-west-1",
        "US West (Oregon)": "us-west-2",
        "Asia Pacific (Mumbai)": "ap-south-1",
        "Asia Pacific (Osaka-Local)": "ap-northeast-3",
        "Asia Pacific (Seoul)": "ap-northeast-2",
        "Asia Pacific (Singapore)": "ap-southeast-1",
        "Asia Pacific (Sydney)": "ap-southeast-2",
        "Asia Pacific (Tokyo)": "ap-northeast-1",
        "Canada (Central)": "ca-central-1",
        "China (Beijing)": "cn-north-1",
        "China (Ningxia)": "cn-northwest-1",
        "EU (Frankfurt)": "eu-central-1",
        "EU (Ireland)": "eu-west-1",
        "EU (London)": "eu-west-2",
        "EU (Paris)": "	eu-west-3",
        "EU (Stockholm)": "eu-north-1",
        "South America (Sao Paulo)": "sa-east-1",
        "AWS GovCloud (US-East)": "us-gov-east-1",
        "AWS GovCloud (US)": "us-gov-west-1"
    }

EC2_INVALID_LIMIT_MSG = 'Please provide non-zero positive integer in {param_name}'
