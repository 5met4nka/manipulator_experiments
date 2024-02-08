# moveit_experiments

## Инструкция по работе с контейнером

* сборка изображения

```bash
docker image build -t lsd-maddrive-ros:noetic-desktop-full .
```

* запуск контейнера в хост-системе Linux

```bash
docker container run -it \
    --name=moveit_experiments \
    --network=host \
    --ipc=host \
    --volume=$HOME/moveit_ws/src:/root/moveit_ws/src \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
    --env=DISPLAY \
    lsd-maddrive-ros:noetic-desktop-full
```

* запуск контейнера в хост-системе Windows
```shell
docker container run -it `
    --name=moveit_experiments `
    --network=host `
    --ipc=host `
    --volume=C:\Users\$env:USERPROFILE\Documents\moveit_ws\src:/root/moveit_ws/src `
    -e DISPLAY=host.docker.internal:0.0 `
    lsd-maddrive-ros:noetic-desktop-full
```

* расширяем конфигурацию catkin параметрами из `/opt/ros/noetic`

```bash
catkin config --extend /opt/ros/noetic
```

* устанавливаем все зависимости

```bash
rosdep install -y -r \
    --from-paths src/ \
    --ignore-src \
    --rosdistro noetic
```
