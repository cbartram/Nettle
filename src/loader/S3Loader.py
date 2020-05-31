import os
import chalk
import boto3
import io
from loader import Loader
from PIL import Image

class S3Loader(Loader.Loader):
	def __init__(self, config):
		super().__init__()
		self.config = config

	def load(self):
		print(chalk.blue(f'[INFO] Loading Image from S3: {self.config["DEFAULT"]["ImagePath"]}'))
		s3 = boto3.resource('s3', region_name='us-east-1')
		if (os.getenv("AWS_ACCESS_KEY_ID") == None or os.getenv("AWS_SECRET_ACCESS_KEY") == None):
			print(chalk.red(
				"[ERROR] Missing aws credentials. Ensure access key id and secret access key values are properly set."))
			os._exit(1)

		if not self.config["DEFAULT"]["ImagePath"].startswith("s3://"):
			print(chalk.red("[ERROR] S3 Image location configuration option must begin with the \"s3://\" prefix."))
			os._exit(1)

		# Parse bucket and path from given configuration
		idx = self.config["DEFAULT"]["ImagePath"][5:].index('/')
		bucketName = self.config["DEFAULT"]["ImagePath"][5:][:idx]
		path = self.config["DEFAULT"]["ImagePath"][5:][idx + 1:]

		bucket = s3.Bucket(bucketName)
		object = bucket.Object(path)

		file_stream = io.StringIO()
		object.download_fileobj(file_stream)
		image = Image.open(file_stream)
		return image