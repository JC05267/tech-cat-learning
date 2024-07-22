# S3 Upload and Download Methods

S3 has several methods for uploading and downloading files with boto3.

They are: upload_file, upload_fileobj, put_object, download_file, download_fileobj, get_object

| Method | Purpose | Best Use Cases | Pros | Cons |
|-----------------|---------------------------------------------|-------------------------------------------------------|------------------------------------------------------------|--------------------------------------------------------|
| upload_file | Uploads a file to S3 | Uploading local files, suitable for large files | Handles multipart uploads, simple interface | Limited control, only works with local files |
| upload_fileobj| Uploads a file-like object to S3 | Uploading in-memory data | Allows direct upload from file-like object, multipart support | Limited control, may require more memory |
| put_object | Uploads data to S3 | Uploading strings or bytes, needing more control | More control, can specify additional parameters | No automatic multipart support, complex for large files|
| download_file | Downloads a file from S3 to local filesystem| Downloading local files, suitable for large files | Handles multipart downloads, simple interface | Limited control, only works with local files |
| download_fileobj| Downloads a file to a file-like object | Downloading data into memory | Allows direct download to file-like object, multipart support | Limited control, may require more memory |
| get_object | Retrieves an object from S3 | Streaming data, handling metadata | Provides object data and metadata, supports streaming | No automatic multipart support, complex handling |
