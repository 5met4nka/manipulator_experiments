# manipulator_experiments

## Инструкция по работе с контейнером

* сборка изображения

```bash
docker image build -t lsd-maddrive-ros:noetic-desktop-full .
```

* запуск контейнера в хост-системе Linux

```bash
docker container run -it \
    --name=<TYPE_PROJECT_NAME> \
    --user=user1122 \
    --network=host \
    --ipc=host \
    --volume=$HOME/moveit_ws/src:/home/user1122/moveit_ws/src \
    --volume=/tmp/.X11-unix:/tmp/.X11-unix:rw \
    --env=DISPLAY \
    lsd-maddrive-ros:noetic-desktop-full
```

* запуск контейнера в хост-системе Windows
```shell
docker container run -it `
    --name=<TYPE_PROJECT_NAME> `
    --user=user1122 `
    --network=host `
    --ipc=host `
    --volume=C:\Users\Nikita\Documents\moveit_ws\src:/home/user1122/moveit_ws/src `
    -e DISPLAY=host.docker.internal:0.0 `
    lsd-maddrive-ros:noetic-desktop-full
```

* расширяем конфигурацию catkin параметрами из `/opt/ros/noetic`

```bash
sudo catkin config --extend /opt/ros/noetic
```

* устанавливаем все зависимости

rosdep install -y . \
    --from-paths src \
    --ignore-src \
    --rosdistro noetic
