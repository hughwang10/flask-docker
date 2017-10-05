#--no-cache
repo='hugh/myflask01'
docker image build -t $repo .
docker rmi $(docker images -q --filter "dangling=true")
docker images | grep $repo