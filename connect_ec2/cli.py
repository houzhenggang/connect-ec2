import click
import boto3
import json

@click.command()
@click.argument('name', default='', required=False)
def main(name):
    """ISSH/RDP command line tool for EC2"""
    click.echo('Connecting to {0}.'.format(name))

    #Initiate Ec2 client
    botoSession = boto3.Session()
    ec2 = botoSession.resource('ec2')
    ec2Client = boto3.client('ec2')
    instanceFilter = [
    				{
    				  "Name": "tag:Name",
    				  "Values" : [
    				  		name,
    				  ]
    				},
    			]
    response = ec2Client.describe_instances(
    			Filters=instanceFilter)

    instances = ec2.instances.filter(Filters = instanceFilter)
    if instances.Size > 1:
    	for instance in instances:
    		for tag in instance.tags:
    			print(tag.key)
    			print(tag.value)


 #   click.echo(response)
    for instance in instances:
        print(name)
        print(instance.private_ip_address)
        print(instance.public_ip_address)

    print(locals())


