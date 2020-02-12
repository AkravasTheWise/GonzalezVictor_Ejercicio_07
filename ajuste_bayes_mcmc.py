#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import matplotlib.pyplot as plt


# In[71]:


data=np.loadtxt('notas_andes.dat')
x=data[:,:4]
y=data[:,4]


# In[72]:


def modelo_lineal(beta_0,betas,x):
    return beta_0+betas*x    

def likelihood(x,y,beta_0,betas):
    sigma=0.1
    L = 1
    L *= (1.0/np.sqrt(2.0*np.pi*sigma**2))*np.exp(-0.5*(y-modelo_lineal(beta_0,betas,x[i,:3]))**2/(sigma**2))
    return L

def post(beta_0,betas,x,y):
    
    post=likelihood(x,y,beta_0,betas)
    #evidencia=np.trapz(post,)
    post=post/evidencia
    return post


# In[73]:


n_iterations = 200000 #this is the number of iterations I want to make
b_walk = np.empty((0)) #this is an empty list to keep all the steps
b_0 = np.random.rand(1,5) #this is the initialization
b_walk = np.append(b_walk,b_0)
b_walk = np.vstack((b_walk,b_0))

for i in range(n_iterations):
    b_prime = np.random.normal(b_walk[i], 0.1) #0.1 is the sigma (std. dev) in the normal distribution
    alpha = post(b_prime[0],b_prime[1:],x,y)/post(b_walk[i,0],b_walk[i,1:],x[i],y[i])
    if(alpha>=1.0):
        b_walk  = np.append(b_walk,b_prime)
    else:
        beta = random.random()
        if(beta<=alpha):
            b_walk = np.append(b_walk,b_prime)
        else:
            b_walk = np.append(b_walk,b_walk[i])


# In[ ]:





# In[ ]:




