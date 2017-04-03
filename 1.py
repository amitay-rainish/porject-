# -*- coding: utf-8 -*-
import pygame
import time
import sys
import socket
import select

MAX_LETTERS = 20
WDADTH = 1200
HIGHTH = 700
COLOR = (200,135,7)
COLOR2 = (24,85,89)
COLOR3 = (130, 90, 20)
WRITE_BOX_LOACTION = (78,90,043), ((WDADTH / 2)-100, (HIGHTH / 2) - 15, 280, 80)
IMAGE = "C:/python in pc/pygame/download.jpg"
d = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
class Client(object):
    def __init__(self, name, text_box, screen):
        self.__name = name
        self.__my_socket = Socket1(name)
        self.__my_text_box = text_box
        self.__screen = screen

    def write_and_send(self, data):
        """
        writting and sending to the server
        """
        self.__my_socket.send_(data)
        self.recev()

    def recev(self):
        """
        rececve from the server information
        """
        read, w, x = select.select([self.__my_socket.return_the_socket()], [], [], 0)
        for r in read:
            if r == self.__my_socket.return_the_socket():
                messege = self.__my_socket.return_the_socket().recv(4096)
                self.__my_text_box.display_box(self.__screen, messege)


class Socket1(object):
    """
    the socket class of the client handel socket staff that the client need
    """
    def __init__(self, name):
        self.__name = name
        self.__my_sokcet = self.conect(name)

    def conect(self, name):
        """
        conect withe the server
        """
        my_socet = socket.socket()
        my_socet.connect(("127.0.0.1", 44))
        my_socet.send("name:" + name)
        return my_socet

    def send_(self, data):
        """
        sending the massage by the parameter that givven
        """
        time_ = time.strftime("%H:%M")
        name = self.__name
        self.__my_sokcet.send(time_ + " " + name + " " + data)

    def return_the_socket(self):
        return self.__my_sokcet


class write_box():
    def __init__(self, hiehts_loactin, width_loction, size_high, size_width):
        self.__loction_high = hiehts_loactin
        self.__loction_width = width_loction
        self.__size_high = size_high
        self.__size_width = size_width
        self.__massage = ""
        self.__massage_helper = []
        self.__color = COLOR3
        self.__i = 10
    def display_box(self, screen, message, color=(255, 5, 5)):
        if self.__i == 10:
            pygame.draw.rect(screen, self.__color,  (self.__loction_width, self.__loction_high, self.__loction_width, self.__loction_high ))
        if message == 13:
            #2fself.__i += 5
            ret = self.__massage
            self.__massage = ""
            message = ""
            return ret
        if len(message) > 1:
            self.__i += 10
        #     self.__massage_helper.append(message)
        #     self.__i = 10
        #     for mas in self.__massage_helper:
        #         print mas
        #         self.write(mas)
        #         self.__i += 5
            # self.__massage = message
        else:
            self.__massage += message
            message = self.__massage
        if len(message) > MAX_LETTERS:
            return ""
        self.write(message, color)
        return ""

    def write(self, message, color):
        myfont = pygame.font.SysFont("ariel", 20) #if border add 1 for transp
        if len(message) != 0:
            screen.blit(myfont.render(message, 1 , color),
            (self.__loction_width, self.__loction_high + self.__i))
        pygame.display.update()

def main():
    """
    Add Documentation here
    """
    pass  # Replace Pass with Your Code
# f ={}
# for p in d:
#     f["pygame.K_%s" % (p)] = p
# dic = {}
# for item in f.items():
#     k, v = item
#     dic[eval(k)] = v
pygame.init()
size = (WDADTH, HIGHTH)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("hello")
screen.fill(COLOR)
image = pygame.image.load(IMAGE)
screen.blit(image, (0,0))
pygame.display.flip()
sys.stdout.flush()
screen.fill(COLOR)
finish = False
i = 100
b = 100
l = write_box(100, 300, 80, 600)
p = write_box(90, 80, 76, 444)
sokcet_ = Client("namee", p, screen)

while not finish:
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
           finish = True
       elif event.type == pygame.KEYDOWN:
                i += 8
                if event.key == 13:
                    txt = 13
                else:
                    txt = unichr(event.key)
                b += 10
                i = 100
                # myfont = pygame.font.SysFont("ariel", 20)
                # label = myfont.render(txt, 34, (40, 40, 200))
                # screen.blit(label, (i, b))
                txt2 = l.display_box(screen, txt)
                if txt2 != "":
                    sokcet_.write_and_send(txt2)
                p.display_box(screen, txt2)
                # pygame.display.flip()
       else:
           massage_in = sokcet_.recev()
           if massage_in != None:
               p.display_box(screen, massage_in, (90, 80, 70))


pygame.quit()
if __name__ == '__main__':
    main()