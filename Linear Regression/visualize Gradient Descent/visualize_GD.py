import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


X = pd.read_csv("./Training Data/Linear_X_Train.csv").values
Y = pd.read_csv("./Training Data/Linear_Y_Train.csv").values


x = np.linspace(-5, 5, 10)


m = np.array([1.4 , 30.58600281, 48.99352692, 60.60890707, 67.94198628,
       72.57380595, 75.50083124, 77.35141162, 78.52196983, 79.2627314 ,
       79.7317185 , 80.02877353, 80.21700962, 80.33634116, 80.41202272,
       80.46004069, 80.49051909, 80.50987223, 80.5221658 , 80.52997788,
       80.53494398, 80.53810202, 80.54011098, 80.54138939, 80.54220319,
       80.54272139, 80.54305146, 80.54326177, 80.54339581, 80.54348126,
       80.54353576, 80.54357051, 80.54359269, 80.54360685, 80.54361588,
       80.54362165, 80.54362533, 80.54362769, 80.54362919, 80.54363015,
       80.54363077, 80.54363116, 80.54363141, 80.54363157, 80.54363167,
       80.54363174, 80.54363178, 80.54363181, 80.54363182, 80.54363184])

c = np.array([-1. , -0.34870694,  0.47200439,  1.24583877,  1.89411002,
        2.40321127,  2.78704632,  3.06842795,  3.27051975,  3.41341744,
        3.5132273 ,  3.58225543,  3.62960816,  3.66187149,  3.68372736,
        3.69845991,  3.70834831,  3.71496053,  3.71936747,  3.72229603,
        3.72423711,  3.72552067,  3.72636765,  3.72692549,  3.72729225,
        3.72753302,  3.72769084,  3.72779415,  3.72786171,  3.72790583,
        3.72793462,  3.72795338,  3.7279656 ,  3.72797355,  3.72797872,
        3.72798208,  3.72798426,  3.72798568,  3.7279866 ,  3.72798719,
        3.72798758,  3.72798783,  3.72798799,  3.72798809,  3.72798816,
        3.7279882 ,  3.72798823,  3.72798825,  3.72798826,  3.72798827])



plt.ion()
for i in range(10):
    y = m[i]*x + c[i]
    plt.scatter(X,Y)
    plt.plot(x,y, 'red')
    plt.draw()
    plt.pause(1)
    plt.clf()

   