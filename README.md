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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)