# build customized image

## command
``` bash
# start standard image
docker run --name redis-test -p 6379:6379 -d --restart=always redis:latest redis-server --appendonly yes --requirepass "your passwd" 

# connect it with redis client
docker exec -it $ID redis-cli -a 'your passwd'
```

