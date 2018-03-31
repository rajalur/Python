class RoshunClass:
    dogs = []
    cats = []

    def __init__(self, d, c):
        self.dogs.append(d)
        self.cats.append(c)

    def __repr__(self):
        str = 'Dogs: '
        for dog in self.dogs:
            str += dog + ' '
        str += ', Cats: '
        for cat in self.cats:
            str += cat + ' '
        return str

    def add_a_dog(self, newdog):
        if newdog not in self.dogs:
            self.dogs.append(newdog)
            print 'Added a dog %s' % newdog
            #print self
        else:
            print 'Dog %s already exists!' % newdog

    def remove_a_dog(self, dog):
        if dog in self.dogs:
            self.dogs.remove(dog)
            print 'Removed dog %s' % dog
            #print self
        else:
            print 'ERROR: dog %s not found!' % dog

    def add_a_cat(self, cat):
        if cat not in self.cats:
            self.cats.append(cat)
            print 'Added a cat %s' % cat
        else:
            print 'Cat %s already exists!' % cat

def main():
    r = RoshunClass('Sophie', 'Billy')
    print r
    dogs_to_add = ['Rani', 'Jojo', 'Luca', 'Simba', 'Sasha']
    for dog in dogs_to_add:
        r.add_a_dog(dog)
    r.add_a_dog('Jojo')
    r.remove_a_dog('Luca')
    r.remove_a_dog('Peter')
    r.add_a_cat('Kitty')
    print r

if __name__ == '__main__':
    main()
