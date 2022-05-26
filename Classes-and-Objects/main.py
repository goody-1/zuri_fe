class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        if type(name) != str:
            raise TypeError("'name' must be string!")

        if type(age) != int:
            raise TypeError("'age' must be int!")

        if type(tracks) != list:
            raise TypeError("'tracks' must be a list!")

        if type(score) != float and type(score) != int:
            raise TypeError("'score' must be a float or an int!")


        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def change_name(self, new_name):
        self.name = new_name

    def change_age(self, new_age):
        self.age = new_age

    def add_track(self, new_track):
        self.tracks.append(new_track)

    def get_score(self):
        return self.score



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
