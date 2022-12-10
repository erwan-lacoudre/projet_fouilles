import random

def split_lines(input, seed, output1, output2):
  random.seed(seed)
  with open(file = input, mode='r') as file:
    with open(file = output1, mode='w+') as out1:
      with open(file = output2, mode='w+') as out2:
        names = file.readline()
        out1.write(names)
        out2.write(names)
        for line in file.readlines():
          if random.random() <= 0.75:
            out1.write(line)
          else :
            out2.write(line)

if __name__ == "__main__":
    split_lines('cleaned_data.csv', 20, 'train.csv', 'test.csv')
    