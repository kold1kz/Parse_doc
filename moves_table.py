"""moves with tables"""
from create_doc import  service


DOC_ID='1C24LgWSvLzt3UEofn8jK6NTSgUIgpOW-lpgV_p-8f-U'


def deleate_table():
    """deleate_teble 1"""
    document = service.documents().get(documentId=DOC_ID).execute()
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
    service.documents().batchUpdate(documentId=DOC_ID, body={'requests': requests}).execute()

def create_table(rows,columns):
    """create tables"""
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
    service.documents().batchUpdate(documentId=DOC_ID, body={'requests': requests}).execute()

def insert_txt(txt,rows,colu):
    """input text"""
    document = service.documents().get(documentId=DOC_ID).execute()
    table = document['body']['content'][2]
    tableindex=table['table']['tableRows'][rows]['tableCells'][colu]['content'][0]['startIndex']
    requests = [{
        'insertText': {
            'location': {
            'index': tableindex
            },
            'text': txt
        }
    }]
    service.documents().batchUpdate(documentId=DOC_ID, body={'requests': requests}).execute()
