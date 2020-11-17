import cv2
import numpy as np
import face_recognition
import os

path = 'Images' #Colocar o caminho do computador do usuario para as imagems na qual as fotos estão
images = []
classNomes = []
minhasLista = os.listdir(path); #Função que ira ler todas os arquivos dentro de um diretorio


# Funcão que ira procurar e tranformar em ecoding todas as imagem colocadas como parametros
def procuraEcoding(images):
    listaDeEncods = []
    for img in images: #Ira fazer um loop dentro da pasta de imagems para realizar todas as ações abaixo para todas as imagems.
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converte todas as imagems para RGB
        encode = face_recognition.face_encodings(img)[0] #Ira retornar uma codificação/encoding 128-dimensões para cada imagem passada.
        listaDeEncods.append(encode) #Ira colocar o encode de uma imagem em uma lista
    return listaDeEncods #ira retornar a lista com todos os encodes da pasta imagems


for cls in minhasLista:
    curImg = cv2.imread(f'{path}/{cls}') #Um loop que ira ler todas as imagems
    images.append(curImg)
    classNomes.append(os.path.splitext(cls)[0]) # Divide o path que é passando como parametro como (path/file, ext/the type of the file )
print(classNomes)

# Tranforma todas as imagems na pasta de imagems em encodes.
listaDeEncodesConhecidas = procuraEcoding(images)
print('Encoding Complete')

class VerificarRosto:
    def leituraDORosto(self):
        # Acessa a web-cam
        cap = cv2.VideoCapture(0)
        # ira pegar cada frame da imagem
        while True:
            success, img = cap.read()
            imgs = cv2.resize(img, (0, 0), None, 0.25,0.25)  # tranforma o tamanho da imagem para 4x menor que a original
            imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)  # transforma a imagem para deixar de ser um jpg ou qualquer outro formato de imagem para virar RGB

            facesCurFrame = face_recognition.face_locations(imgs)  # detecta o rosto de alguem baseado em posiçoes que ja foram pré-colocadas e procura o rosto de qualquer imagem de pessoa passado como parametro sendo as localizacões (top, right,bottom ,left )
            encodeCurFrame = face_recognition.face_encodings(imgs, facesCurFrame)  # tranforma localização, cada ponto e gera 128 contagem que seria equivalente a marcas e localizaçoes do rosto de uma pessoa oque torna possivel de compara com as localizações de outras pessoa.

            for encodeFaces, faceLoc in zip(encodeCurFrame,facesCurFrame):  # esse for ira pegar o rosto do FacesCurFrame que é o rosto aparencendo na web-cam, detectar os rostos aparecendo e ira pegar os encodes da variavel encodesCurFrame e colocar no encodeFaces
                parecidos = face_recognition.compare_faces(listaDeEncodesConhecidas,encodeFaces)  # compara o rosto pego pela web-cam (encodeFaces) com todos os rostos em uma lista que nesse caso é o ListaDeEncodesConhecidas e compara-los.
                faceDis = face_recognition.face_distance(listaDeEncodesConhecidas,encodeFaces)  # é utlizado para encontrar a distancia de cada rosto nas lista de encodes conhecidos com a imagem aparecendo na web-cam sendo o menor valor que aparecer o que mais se parece.
                indexDosParecidos = np.argmin(faceDis)  # ira pegar o index da distancia com menor valor.

                if parecidos[indexDosParecidos]:
                    name = classNomes[indexDosParecidos]  # ira escrever o nome de qual rosto a imagem mostrada na web-cam é mais proximo.
                    return name #Retorna o nome do usuario pelo rosto colocado na frente da web-can
                else:
                    name = "falso"
                    return name #ira retornar o nome falso pela função

    #Função que ira verifificar todos os nomes dos arquivos no ditetorio passado como parametro, ira separar o tipo de arquivo e guardar em uma lista que esta sendo retornado
    def VerifyNameUsers(minhasListas):
        for cls in minhasLista:
            curImg = cv2.imread(f'{path}/{cls}')
            images.append(curImg)
            classNomes.append(os.path.splitext(cls)[0])
        return classNomes









