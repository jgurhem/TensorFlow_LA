import tensorflow as tf

def outData(sess, filename, data, rowDim, colDim, rowPos, colPos):
    #print tf.keras.backend.eval(data), rowDim, colDim
    arr = sess.run(data)
    f=open(filename, 'a')

    for i in range(rowDim):
        for j in range(colDim):
            print(rowPos * rowDim + i, colPos * colDim + j, arr[i, j], file=f)

    f.close()



def init(filename):
    f=open(filename, 'w')
    f.close()
