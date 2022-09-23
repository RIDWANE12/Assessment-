from pykalman import KalmanFilter
import itertools 
df=pd.read_csv('/content/ingredient.csv')

def KFSM(input):
    X=input.transpose().values.tolist()
    kf=lambda signal: KalmanFilter().em(signal, n_iter=7).filter(signal)[0].tolist()
    array=np.array([list(itertools.chain(*kf(signal))) for signal in X])
    return array 

KFSM(df).shape

df1=pd.DataFrame(KFSM(df).transpose())
df1.columns=df.columns
df1.to_excel('ingredient_KF-denoised.xlsx',index=False)


