import numpy as np

def calculate(list):
    if(len(list) != 9):
        return "The list should be 9 elements"
    else:
        matrice = np.array(list).reshape(3,3)
        dict = {
            "Mean" :
                [
                    matrice.mean(axis=0).tolist() ,
                    matrice.mean(axis= 1).tolist() ,
                    matrice.mean().tolist()
            ],
            "Variance" :
                [
                    matrice.var(axis=0).tolist() ,
                    matrice.var(axis= 1).tolist() ,
                    matrice.var().tolist()],
            "Standard Deviation" :
                [
                    matrice.std(axis=0).tolist() ,
                    matrice.std(axis= 1).tolist() ,
                    matrice.std().tolist()
                ],
            "Max" :
                [
                    matrice.max(axis=0).tolist() ,
                    matrice.max(axis= 1).tolist() ,
                    matrice.max().tolist()
                ],
            "Min" :
                [
                    matrice.min(axis=0).tolist() ,
                    matrice.min(axis= 1).tolist() ,
                    matrice.min().tolist()
                ],
            "Sum" :
                [matrice.sum(axis=0).tolist(),
                 matrice.sum(axis= 1).tolist() ,
                 matrice.sum().tolist()
                 ]
        }
        return dict