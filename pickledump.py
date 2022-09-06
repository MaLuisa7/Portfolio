import pickle
import pickle_example

f = open('student.dat', 'wb')
s = pickle_example.Student(282060, 'Maria', 10)

pickle.dump(s, f)

f.close()

