from create_doc import  service


docId='1C24LgWSvLzt3UEofn8jK6NTSgUIgpOW-lpgV_p-8f-U'


def deleate_table():
    document = service.documents().get(documentId=docId).execute()
    table = document['body']['content'][2]

    requests = [{
        'deleteContentRange': {
        'range': {
            'segmentId': '',
            'startIndex': table['startIndex'],
            'endIndex':   table['endIndex']
        }
        },
    }
    ]
    result = service.documents().batchUpdate(documentId=docId, body={'requests': requests}).execute()

def create_table(rows,columns):
    requests = [{
      'insertTable': {
          'rows': rows,
          'columns': columns,
          'endOfSegmentLocation': {
            'segmentId': ''
          }
      },
  }
  ]
    result = service.documents().batchUpdate(documentId=docId, body={'requests': requests}).execute()

def insert_txt(txt,rows,colu):
    document = service.documents().get(documentId=docId).execute()
    table = document['body']['content'][2]
    tableIndex=table['table']['tableRows'][rows]['tableCells'][colu]['content'][0]['startIndex']
    requests = [{
        'insertText': {
            'location': {
            'index': tableIndex
            },
            'text': txt
        }
    }]
    result=service.documents().batchUpdate(documentId=docId, body={'requests': requests}).execute()