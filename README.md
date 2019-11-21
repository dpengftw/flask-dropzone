# flask-dropzone
Dropzone HTTP Uploader built on Flask

## Installation

Use Docker to run the HTTP uploader. Here the upload directory is mounted to the host /tmp dir. 
Files uploaded will be under /tmp.

```
docker run -itd --rm --name flask-dropzone -p 5000:5000 -v /tmp:/app/uploads flask-dropzone
```

## Screenshot

(images/Flask-Dropzone-Demo_-Parallel-Upload-Google-Chrome-2019-11-17-10-23-32.gif)

## Environment Variables

|Name              |Description              |
|------------------|-------------------------|
|GIT_NAME          |Name of the Git user     |
|GIT_REPO          |Git repo URL             |
|REMOVE_FILES      |Remove app root files    |
|GIT_BRANCH        |Git branch to pull       |
|SSH_KEY           |SSH key in base64 encoded|
|GIT_USERNAME      |Username of the Git user |
|GIT_PERSONAL_TOKEN|Git token to access repo |

## Custom Git Repo Deployment

```
docker run -itd --rm --name flask-dropzone -p 5000:5000 \
  -e GIT_NAME=<Full Name> \ 
  -e GIT_REPO=<Git URL> \
  -e GIT_USERNAME=<Username \
  -e GIT_PERSONAL_TOKEN=<Git token>
```

## Usage

Open http://docker IP:5000, and drag and drop any file onto the HTTP upload zone.  Files will be uploaded
and placed in /app/uploads.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
