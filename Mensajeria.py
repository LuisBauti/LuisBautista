# -*- coding: utf-8 -*-
# programa: sistema de mensajeria movil
# Objetivo: poder ver y modificar los mensajes disponibles en la
#           bandeja de entrada y salida
#Autor: Luis Enrique Consuegra Bautista
# fecha: 29/02/2020
import sys
import os
import platform

class ShortMessageService:

    def __init__(self):
        self.MessageService = list()
        self.options = {"1": self.view_Entrada,
                        "2": self.view_Salida,
                        "3": self.add_Message,
                        "4": self.close}

    def menu(self):
        self.clear_screen()
        print("""
                Mensajeria
                1. Bandeja de entrada
                2. Mensajes enviados
                3. Enviar mensaje
                4.Salir
                """)

    def clear_screen(self):
        if platform.system() == "Winndows":
            os.system("cls")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("clear")
        else:
            print("Plataforma no soportada")
