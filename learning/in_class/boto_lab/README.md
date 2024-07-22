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

## upload_file
Purpose:
Uploads a file to an S3 bucket.

Best Use Cases:

When you need to upload a file from your local filesystem to S3.
Suitable for large files because it handles multipart uploads automatically.
Pros:

Handles multipart uploads, making it suitable for large files.
Provides a simple and straightforward interface.
Cons:

Limited control over the upload process compared to put_object.
Only works with local files.

## upload_fileobj
Purpose:
Uploads a file-like object to an S3 bucket.

Best Use Cases:

When you need to upload data that is already in memory, like a BytesIO object.
Useful for data that isn't saved to disk.
Pros:

Allows uploading data directly from a file-like object.
Handles multipart uploads automatically.
Cons:

Limited control over the upload process compared to put_object.
May require more memory if the entire file-like object is held in memory.

## put_object
Purpose:
Uploads data to an S3 bucket.

Best Use Cases:

When you need to upload data directly from a string or bytes.
Useful for small objects or when you need more control over the upload.
Pros:

More control over the upload process.
Can specify additional parameters like metadata, ACLs, etc.
Cons:

Does not handle multipart uploads automatically.
Not as straightforward for uploading large files.

## download_file
Purpose:
Downloads a file from an S3 bucket to the local filesystem.

Best Use Cases:

When you need to download a file from S3 to your local filesystem.
Suitable for large files because it handles multipart downloads automatically.
Pros:

Handles multipart downloads, making it suitable for large files.
Provides a simple and straightforward interface.
Cons:

Limited control over the download process compared to get_object.
Only works with local files.

## download_fileobj
Purpose:
Downloads a file from an S3 bucket to a file-like object.

Best Use Cases:

When you need to download data directly into a file-like object.
Useful for data that you want to process in memory.
Pros:

Allows downloading data directly into a file-like object.
Handles multipart downloads automatically.
Cons:

Limited control over the download process compared to get_object.
May require more memory if the entire file-like object is held in memory.

## get_object
Purpose:
Retrieves an object from an S3 bucket.

Best Use Cases:

When you need to download an object and process it directly in your code.
Useful for streaming data or handling metadata.
Pros:

Provides a response with the object data and metadata.
Allows for streaming data without holding the entire object in memory.
Cons:

Does not handle multipart downloads automatically.
Requires more complex handling compared to download_file.
