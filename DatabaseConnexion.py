import psycopg2

class DatabaseConnexion:
    # mon constructeur fabrique l'objet et d'office lui affecte les éléments de connexion à la base de donnée ainsi que le curseur
    def __init__(self):
        try:
            self.conn = psycopg2.connect(host = 'localhost', user = 'rooot', password = 'mypass', database = 'azuredb')
            self.mycursor = self.conn.cursor()
            print("Connected", self.conn)
        except Exception as Error:
            print("Not connected due to: ", Error)
    
    def create_db(self):
        self.mycursor.execute("CREATE DATABASE IF NOT EXISTS azuredb;")
        print("database created")

    # suppression de table si elle existe
    def drop_table(self):
        self.mycursor.execute("DROP TABLE IF EXISTS list_mail;")
        self.commit = self.conn.commit()
        print("table dropped")

    # # création d'une table
    def create_table(self):
        self.mycursor = self.mycursor
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS list_mail (id SERIAL, name CHAR(255), mail CHAR(255));")
        self.commit = self.conn.commit()
        print("table created")

    # insertion de donnée dans la table
    def insert_data(self,name, mail):
        self.mycursor.execute("INSERT INTO list_mail (name, mail) VALUES (%s, %s)", (name, mail))
        print("data inserted")
    
    # récupérer donnée dans la table
    def get_data(self):
        self.mycursor.execute('''SELECT id, mail FROM list_mail ORDER BY id DESC LIMIT 5;''')
        result = self.mycursor.fetchall()

    # nettoye et ferme la connexion de la base de donnée
    def close(self):
        self.commit = self.conn.commit()
        self.cursors = self.mycursor.close()
        self.conn = self.conn.close()
        print("closed")
    
# if __name__ =='__main__':
#     db = DatabaseConnexion()
#     db.create_table()
