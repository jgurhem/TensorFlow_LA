import tensorflow as tf

def outData(filename, data, rowDim, colDim, rowPos, colPos):
    #print tf.keras.backend.eval(data), rowDim, colDim
    arr = tf.keras.backend.eval(data)
    f=open(filename, 'a')

    for i in range(rowDim):
        for j in range(colDim):
            print >>f, rowPos * rowDim + i, colPos * colDim + j, arr[i, j]

    f.close()



def init(filename):
    f=open(filename, 'w')
    f.close()
