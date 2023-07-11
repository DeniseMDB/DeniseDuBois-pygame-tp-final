import sqlite3

def create_database_game():
    try:
        with sqlite3.connect("DB_bob.db") as conexion:
            ranking_score = ''' CREATE TABLE IF NOT EXISTS Ranking_Score
                    (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Player TEXT,
                            Score INTEGER,
                            Timer INTEGER
                    )
                    '''
            conexion.execute(ranking_score)

            saves = ''' create table if not exists Saves
                        (
                                Save text,
                                Name text,
                                Level integer,
                                Score integer,
                                Timer integer
                        )
                    '''
            conexion.execute(saves)               
        print("Se creó el archivo de base de datos")
    except sqlite3.OperationalError:
        print("No se pudo crear el archivo de base de datos")


def save_score(name, score, time):
    try:
        with sqlite3.connect("DB_bob.db") as conexion:
            conexion.execute("INSERT INTO Ranking_Score (Player, Score, Timer) VALUES (?, ?, ?)", (name, score, time))
        print("Puntuación guardada exitosamente")
    except sqlite3.Error as error:
        print("Error al guardar la puntuación:", error)


def save_game(save, level, score, timer):
    try:
        with sqlite3.connect("DB_bob.db") as conexion:
            sentencia = "UPDATE Saves SET score=?, timer=? WHERE save=? AND level=?"
            conexion.execute(sentencia, (score, timer, save, level))
        print("Partida guardada exitosamente")
    except sqlite3.Error as error:
        print("Error al guardar la partida:", error)


def get_scores():
    try:
        with sqlite3.connect("DB_bob.db") as conexion:
            cursor = conexion.execute("SELECT Player, Score, Timer FROM Ranking_Score ORDER BY Score DESC, Timer ASC LIMIT 5")
            return cursor.fetchall()
    except sqlite3.Error as error:
        print("Error al obtener las puntuaciones:", error)
        return []


def create_start(save, name, niveles):
    with sqlite3.connect("DB_bob.db") as conexion:
        try:
            sentencia = "INSERT INTO Saves (Save, Name, Level, Score, Timer) VALUES (?, ?, ?, ?, ?)"
            unlock = 1
            for nivel in range(1, niveles + 1):
                conexion.execute(sentencia, (save, name, nivel,0,0))
                unlock = 0
            print("Partida creada exitosamente")
        except sqlite3.Error as error:
            print("Error al crear la partida:", error)


def get_name_save(save):
    with sqlite3.connect("DB_bob.db") as conexion:
        try:
            cursor = conexion.execute("SELECT name FROM Saves WHERE save=?", (save,))
            nombre = cursor.fetchone()
            if nombre:
                return nombre[0]
            else:
                print("No se encontró el save:", save)
                return None
        except sqlite3.Error as error:
            print("Error al obtener el nombre del save:", error)
            return None


def get_data_level(save, nivel):
    with sqlite3.connect("DB_bob.db") as conexion:
        try:
            sentencia = "SELECT `score` FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia, (save, nivel))
            datos = cursor.fetchone()
            return datos if datos is not None else 0  # Retorna 0 si no se encuentra ningún dato
        except:
            print("Error al obtener los datos")
            return 0


def get_time_level(save, nivel):
    with sqlite3.connect("DB_bob.db") as conexion:
        try:
            sentencia = "SELECT timer FROM Saves WHERE save=? AND level=?"
            cursor = conexion.execute(sentencia, (save, nivel))
            datos = cursor.fetchone()
            if datos:
                return datos[0]
            else:
                print("No se encontró el timer del nivel")
                return 0
        except sqlite3.Error as error:
            print("Error al obtener el timer del nivel:", error)
            return 0