# ������ۺ���
from pandas import np


def computerCost(X,y,theta):
    m = len(y)
    J = 0
    J = (np.transpose(X*theta-y))*(X*theta-y)/(2*m) #�������J
    return J

# �ݶ��½��㷨
def gradientDescent(X,y,theta,alpha,num_iters):
    m = len(y)
    n = len(theta)
    temp = np.matrix(np.zeros((n,num_iters)))   # �ݴ�ÿ�ε��������theta��ת��Ϊ������ʽ
    J_history = np.zeros((num_iters,1)) #��¼ÿ�ε�������Ĵ���ֵ

    for i in range(num_iters):  # ������������
        h = np.dot(X,theta)     # �����ڻ���matrix����ֱ�ӳ�
        temp[:,i] = theta - ((alpha/m)*(np.dot(np.transpose(X),h-y)))   #�ݶȵļ���
        theta = temp[:,i]
        J_history[i] = computerCost(X,y,theta)      #���ü�����ۺ���
    return theta,J_history

# ��һ��feature
def featureNormaliza(X):
    X_norm = np.array(X)            #��Xת��Ϊnumpy������󣬲ſ��Խ��о��������
    #�����������
    mu = np.zeros((1,X.shape[1]))
    sigma = np.zeros((1,X.shape[1]))

    mu = np.mean(X_norm,0)          # ��ÿһ�е�ƽ��ֵ��0ָ��Ϊ�У�1�����У�
    sigma = np.std(X_norm,0)        # ��ÿһ�еı�׼��
    for i in range(X.shape[1]):     # ������
        X_norm[:,i] = (X_norm[:,i]-mu[i])/sigma[i]  # ��һ��

    return X_norm,mu,sigma


