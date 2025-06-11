import subprocess
import boto3

def check_s3(bucket):
    s3 = boto3.client('s3')
    res = s3.get_bucket_versioning(Bucket=bucket)
    if res.get('Status') != 'Enabled':
        raise Exception("S3 Versioning NOT enabled!")
    print("[✔] S3 Versioning OK")

def check_dynamodb(table):
    dynamodb = boto3.client('dynamodb')
    tables = dynamodb.list_tables()['TableNames']
    if table not in tables:
        raise Exception("DynamoDB Lock Table NOT found!")
    print("[✔] DynamoDB Table OK")

def terraform(action):
    cmds = {'init': ["terraform", "init"],
            'plan': ["terraform", "plan"],
            'apply': ["terraform", "apply", "-auto-approve"]}
    subprocess.run(cmds[action], check=True)

if __name__ == "__main__":
    check_s3('tf-state-bucket-123')
    check_dynamodb('terraform-locks')
    terraform('init')
    terraform('plan')
    terraform('apply')
    print("✅ Terraform Infrastructure Provisioned Successfully.")
