import sqlite3

def fetch_rfid_data():
    conn = sqlite3.connect('rfid_data.db')  
    cursor = conn.cursor()
    
    query = """
    SELECT id, tag_id, localizacao, timestamp
    FROM localizacao_rfid
    ORDER BY timestamp DESC
    LIMIT 10;  # Ajuste o limite conforme necessário para buscar mais registros
    """
    
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        
        print("Últimos registros de localização RFID:")
        for row in records:
            print(f"ID: {row[0]}, Tag ID: {row[1]}, Localização: {row[2]}, Timestamp: {row[3]}")
            
    except sqlite3.Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
    finally:
        conn.close()


fetch_rfid_data()
