import boto3
from botocore.client import Config

profiles = ['sandbox2']  # 
config = Config(region_name='us-east-1')

def volumedetails():
    for profile in profiles:
        print(profile)
        session = boto3.Session(profile_name=profile)
        ec2_resource = session.resource('ec2', config=config)
        for volume in ec2_resource.volumes.filter(Filters=[{'Name': 'encrypted', 'Values': ['false',]},
                                                           {'Name': 'status', 'Values': ['in-use',]}]):
            if volume.attachments[-1]['Device'] not in ['/dev/xvda', '/dev/sda1']:
                print(volume.volume_id, volume.attachments[-1]['Device'])


if __name__ == '__main__':
    volumedetails()
