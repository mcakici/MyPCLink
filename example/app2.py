def main():
    asd = 45
    print(id(asd))
    print(id(45))

    asd = 10
    print(id(asd))


    asd = [1,2,3,4,5]
    print(id(asd))

    asd.append(10)
    print(id(asd))




if __name__ == '__main__':
    main()