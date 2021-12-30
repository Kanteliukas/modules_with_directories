from modules.python_kursas import PythonKursas
from modules.kursas import Kursas

def main():
    new_lecture = Kursas("JavaScript", "Mantvydas", "1 valanda")
    python_lecture = PythonKursas("Python", "Jomantas", "4 valandos")
    new_lecture.destyti()
    python_lecture.destyti()

if __name__ == '__main__':
    main()


