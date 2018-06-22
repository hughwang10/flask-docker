#--no-cache
repo='hugh/lifegame'
docker image build --no-cache -t $repo .
docker rmi $(docker images -q --filter "dangling=true")
docker images | grep $repo