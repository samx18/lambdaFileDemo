import boto3

#Create a S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Create a file uunder /tmp

	file = open("/tmp/demo.txt", "w")
    file.write("Hello World")
    file.close()
    
	s3.upload_file("/tmp/demo.txt", "ctrbot", "demo.txt")
    return 'file created & uploaded to S3'
