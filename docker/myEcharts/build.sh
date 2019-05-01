cd /Users/zhu/bob/zboDoDataBus/docker/myEcharts/dockerFile &&
docker build -t myecharts .
docker run -d --name my_echarts -v /Users/zhu/bob/zboDoDataBus/docker/myEcharts/volumn:/bob/ --network=net_d myecharts

