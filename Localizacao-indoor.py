dados_rfid = [
    {'tag_id': 'tag1', 'reader_id': 'reader1', 'timestamp': '2024-02-06 10:00:00'},
    {'tag_id': 'tag2', 'reader_id': 'reader2', 'timestamp': '2024-02-06 10:00:05'},
    
]


localizacao_leitores = {
    'reader1': 'Entrada Principal',
    'reader2': 'Sala de Reuniões',
    
}


ultima_localizacao = {}
for dado in dados_rfid:
    tag = dado['tag_id']
    reader = dado['reader_id']
    localizacao = localizacao_leitores.get(reader, 'Localização desconhecida')
    ultima_localizacao[tag] = localizacao


for tag, localizacao in ultima_localizacao.items():
    print(f"Tag {tag} foi vista pela última vez em {localizacao}.")

