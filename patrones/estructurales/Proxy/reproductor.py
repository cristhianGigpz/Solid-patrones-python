class Video:
    def reproducir(self):
        print("Reproduciendo video")


class VideoProxy:
    def __init__(self, video, premium=False):
        self.video = video
        self.premium = premium

    def reproducir(self):
        if not self.premium:
            print("Acceso denegado. Suscríbete para ver este video.")
            return

        self.video.reproducir()


video = Video()
proxy = VideoProxy(video, premium=False)
proxy.reproducir()

proxy = VideoProxy(video, premium=True)
proxy.reproducir()
