from pprint import pprint
import boto3
from botocore.exceptions import ClientError


def get_message(recipient, sender, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    table = dynamodb.Table('Messages')

    try:
        response = table.get_item(Key={'recipient': recipient, 'sender': sender})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


if __name__ == '__main__':
    message = get_message("Mauricio", "Adam")
    if message:
        print("Get message succeeded:")
        pprint(message, sort_dicts=False)