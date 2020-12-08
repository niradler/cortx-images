# Cortx images

2020 cortx hackathon.

cortx is an open source s3 compatible storage server.

for more info on cortx visit https://github.com/Seagate/cortx-s3server.

## Intro

The idea is to create an alternative to platforms like cloudinary, and provide open source solution for the community to use.

### Usage

GET /images/{filename} // return original image

GET /images/120x120/{filename} // return resized image, with=120, height=120

* resized images will be stored for future use.
