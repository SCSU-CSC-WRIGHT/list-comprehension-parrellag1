numbers = [1,7,11,13]
test = [1,2,4,7]

for num in numbers:
    if num in test:
        test.remove(num)
        return (numbers + test)