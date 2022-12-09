import random

def split_lines(input, seed, output1, output2):
  random.seed(seed)
  with open(file = input, mode='r') as file:
    with open(file = output1, mode='w+') as out1:
      with open(file = output2, mode='w+') as out2:
        for line in file.readlines():
          if random.random() <= 0.75:
            out1.write(line)
          else :
            out2.write(line)

if __name__ == "__main__":
    split_lines('cleaned_music.csv', 20, 'train.csv', 'test.csv')