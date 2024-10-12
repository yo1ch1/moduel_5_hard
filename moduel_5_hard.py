from time import sleep


class User:

    def __init__(self, nickname, password, age):
        if isinstance(nickname, str) and isinstance(
                password, str) and isinstance(age, int):
            self.nickname = nickname
            self.password = hash(password)
            self.age = age

    def __str__(self):
        return f"Пользователь {self.nickname}"


class Video:

    def __init__(self, title, duration, adult_mode=False):
        if (isinstance(title, str) and isinstance(duration, int)
                and isinstance(adult_mode, bool)):
            self.title = title
            self.duration = duration
            self.time_now = 0
            self.adult_mode = adult_mode

    def __str__(self):
        return self.title


class UrTube:

    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        user = User(nickname, password, age)
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        user = User(nickname, password, age)
        self.users.append(user)
        self.current_user = user

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def log_out(self):
        self.current_user = None

    def add(self, *videos_1):
        for video in videos_1:
            is_exist = False
            for svid in self.videos:
                if svid.title == video.title:
                    is_exist = True
                    break
            if not is_exist:
                self.videos.append(video)

    def get_videos(self, title: str):
            for video in self.videos:
                if title.lower() in video.title.lower():
                    return video
            return None

    def watch_video(self, title):
        if self.current_user is None:
            return print("Войдите в аккаунт, чтобы смотреть видео")
        else:
            video = self.get_videos(title)

        if video is None:
            print('Такого видео не существует')
        elif self.current_user.age < 18 and video.adult_mode:
            print('Вам нет 18 лет, пожалуйста покиньте страницу')
        else:
                while video.time_now < video.duration:
                    for sec in range(video.time_now, video.duration + 1):
                        print(sec)
                        sleep(1)
                        video.time_now += 1

                        video.time_now = 0
                    break
                print('Конец видео')

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
