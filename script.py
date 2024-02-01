import os
import time
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pytube import YouTube


def dowloadVid(link) :        
    yt = YouTube(link);    
    temp = yt.length;
    if temp < 360:
        video = yt.streams.get_highest_resolution();
        video.download(toSearch)

def main() :    
    navegador = webdriver.Chrome();
    navegador.get("https://www.youtube.com/");
    navegador.maximize_window();
    time.sleep(5);
    input = navegador.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input");
    if input :
        input.click();
        time.sleep(2);
        input.send_keys(toSearch);
        time.sleep(2);
        
        navegador.find_element(By.XPATH, "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button").send_keys(Keys.ENTER);
        time.sleep(2);           
        actions = ActionChains(navegador)
        actions.send_keys(Keys.END).perform()                           
        thumbs = navegador.find_elements(By.ID, "video-title");
        
        time.sleep(2);
        tamanhoL = [];        
        tamanhoT = [];    
        toSearch.capitalize;
        for thumb in  thumbs :            
            link = thumb.get_attribute('href');               
            capa = thumb.get_attribute('title');             
           
            if link != None and capa != None :  
               tamanhoL.append(link)
               tamanhoT.append(capa)   
                           
                
        for texto, thumb in zip(tamanhoL, tamanhoT) :    
            arquivo.write(f'"Link: "{texto} \n');
            dowloadVid(texto);                             

    else : 
        print("n achei")   

teste = None;

def onClick():
    label.config(text="Botão clicado!");
    global teste;
    teste = inputSearch.get();      
 
janela = tk.Tk();
janela.title("DOWLOADER-300Vortex");

label = tk.Label(janela, text="Olá, mundo!");
label.pack();

inputSearch = tk.Entry(janela);
inputSearch.pack();

botao = tk.Button(janela, text="Clique em mim", command=onClick);
botao.pack();

   
caminho_do_arquivo = "C:\\Users\\Latitude 3490\\Desktop\\python\\videos.txt";
arquivo = open(caminho_do_arquivo, "w");

janela.mainloop();
while True:       
    toSearch = teste;   
    toSearch.capitalize;
    if toSearch != None:
        try :
            os.mkdir(toSearch);
            main();
        except :  
            main();
        arquivo.close();   
    

