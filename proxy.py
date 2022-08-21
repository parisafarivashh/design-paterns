"""
The Proxy design pattern is a class functioning as an interface to
another class or object.

A Proxy could be for anything, such as a network connection,
an object in memory, a file, or anything else you need to provide an abstraction between.

It is also very similar to the Facade, except you can add extra responsibilities
just like the Decorator. The Decorator however can be used recursively.


Open/Closed Principle: Without changing the client code,
    we can easily introduce the new proxies in our application.
Smooth Service: The proxy that we creates works even when the service
   object is not ready or is not available at the current scenario.
Security: Proxy method also provides the security to the system.
Performance: It increases the performance of the application by avoiding
   the duplication of the objects which might be huge size and memory intensive.
"""


class Image:
    def __init__(self, filename):
        self._filename = filename

    def load_image_from_disk(self):
        print("loading " + self._filename)

    def display_image(self):
        print("display " + self._filename)


class Proxy:
    def __init__(self, subject):
        self._subject = subject
        self._proxystate = None


class ProxyImage(Proxy):
    def display_image(self):
        if self._proxystate == None:
            self._subject.load_image_from_disk()
            self._proxystate = 1
        print("display " + self._subject._filename)


if __name__ == '__main__':
    proxy_image1 = ProxyImage(Image("HiRes_10Mb_Photo1"))
    proxy_image2 = ProxyImage(Image("HiRes_10Mb_Photo2"))

    proxy_image1.display_image()  # loading necessary
    proxy_image1.display_image()  # loading unnecessary
    proxy_image2.display_image()  # loading necessary
    proxy_image2.display_image()  # loading unnecessary
    proxy_image1.display_image()  # loading unnecessary

