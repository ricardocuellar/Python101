
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# 1 -> *, $ 

def show_draw():
    fill = '*'
    empty = '$'
    for line in picture:
        for pixel in line:
            if(pixel):
                print(fill, end='') #print
            else: 
                print(empty, end='')
        print('')
            
        

show_draw()

print(picture)

# que la vista sea igual a la del arreglo 
#   [0,0,0,1,0,0,0]
#   [0,0,1,1,1,0,0]
#   [0,1,1,1,1,1,0]
#   [1,1,1,1,1,1,1]
#   [0,0,0,1,0,0,0]
#   [0,0,0,1,0,0,0]

#Cambiar de 1 -> * y el 0-> $