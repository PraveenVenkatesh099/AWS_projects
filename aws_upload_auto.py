import boto3

# Replace these with your AWS credentials and S3 bucket name
ACCESS_KEY = 'FAKEACCESSKEY'
SECRET_KEY = 'FAKE_SECRET_KEY'
BUCKET_NAME = 'myfirstbucketlegoio'

# Initialize S3 client
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

# Upload a file
file_path = "C:\praveen\LegoIO\Weekly_status_report\Weekly_Status_Report_04_20_2025.docx"
file_name = 'weekly_status_report_04_20_2025.docx'  # Name for the file in S3 bucket

try:
    s3.upload_file(file_path, BUCKET_NAME, file_name)
    print(f"File uploaded successfully to {BUCKET_NAME}")
except Exception as e:
    print(f"Error uploading file: {e}")