# основной образ
FROM osrf/ros:noetic-desktop-full

# добавляем пользователя по умолчанию
ARG USERNAME=user1122
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && mkdir /home/$USERNAME/.config && chown $USER_UID:$USER_GID /home/$USERNAME/.config

RUN echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# необходимые apt-пакеты
RUN apt-get update && apt-get install -y \
    curl \
    zsh \
    git \
    sudo \
    dos2unix \
    python3-catkin-tools

RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# копируем .bashrc
COPY zshrc /home/${USERNAME}/.zshrc
RUN dos2unix /home/${USERNAME}/.zshrc