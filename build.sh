#--no-cache
docker image build -t hugh/myflask01 .
docker rmi $(docker images -q --filter "dangling=true")
docker images