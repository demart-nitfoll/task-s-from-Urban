from time import sleep
class User:
    def __init__(self, name: str, password, age: int):
        self.nickname = name
        self.password = hash(password)
        self.age = age
    def __repr__(self):
        return self.nickname
class Video:
    def __init__(self, title: str, duration: int, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
    def __str__(self):
        return self.title
class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f"Пользователь {nickname} успешно зарегистрирован и вошел в систему.")
    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print(f"Пользователь {nickname} вошел в систему.")
                return
        print("Неверный логин или пароль.")
    def log_out(self):
        self.current_user = None
    def add(self, *args: Video):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)
                print(f"Видео {i.title} добавлено.")
            else:
                print(f"Видео с названием {i.title} уже существует.")
    def get_videos(self, search_word: str):
        s = []
        for i in self.videos:
            c = i.title
            if search_word.lower() in c.lower():
                s.append(i.title)
        return s
    def watch_video(self, search_video: str):
        if self.current_user != None:
            for i in self.videos:
                if search_video == i.title:
                    if self.current_user.age >= 18:
                        print(f"Начинаем просмотр видео: {i.title}")
                        for s in range(1, i.duration + 1):
                            print(s,end=" ")
                            sleep(1)
                        print('Конец видео')
                        return
                    else:
                        print("Вам нет 18 лет, пожалуйста покиньте страницу")
                        return
            print("Видео не найдено.")
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")

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