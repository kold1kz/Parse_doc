import httplib2 
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials	

CREDENTIALS_FILE = 'parsetable2-61d7c00cfd0d.json'  # Имя файла с закрытым ключом

# Читаем ключи из файла
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])

httpAuth = credentials.authorize(httplib2.Http()) # Авторизуемся в системе
service = apiclient.discovery.build('docs', 'v1', http = httpAuth)

def create_doc():
    newdocument = service.documents().create(body={'title': 'parse table'}).execute()
    newdocumentId = newdocument['documentId'] # сохраняем идентификатор файла
    print('https://docs.google.com/document/d/' + newdocumentId)


def give_access(mail, docId):
    driveService = apiclient.discovery.build('drive', 'v3', http = httpAuth) # Выбираем работу с Google Drive и 3 версию API
    try:
        access = driveService.permissions().create(
            fileId = docId,
            body = {'type': 'user', 'role': 'writer', 'emailAddress': mail},  # Открываем доступ на редактирование
            fields = 'id'
        ).execute()
        print(f'user {mail} access accept')
    except:
        print("error")
    



