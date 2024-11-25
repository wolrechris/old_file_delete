# Old File Delete

Old File Delete is a simple program / script that allows you to delete files that are older than a specific age (configurable in seconds). It also lets you automatically delete empty folders.

This script is meant to be used within a docker container. Because of this, all paths that are to be deleted are expected to be found within `/delete`. Further configuration can be done by setting environment variables:

```
DELETE_FOLDERS = False # Delete empty folders
DELETION_AGE = 172800 # Age of files in seconds that will be deleted (default: 172800s = 48h)
```

## Build instructions:

```
git clone https://github.com/wolrechris/old_file_delete.git && cd old_file_delete
sudo docker build -t old-file-delete:v0.3 .
```