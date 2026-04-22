import numpy as np

# a=[1,2,4]
# print(type(a))
# b=np.array(a)
# print(type(b))

# c=np.array([[[1,2,3],[4,5,6],[7,9,8]]])
# print(c.ndim)
# print(c.size)
# print(c.dtype)
# print(c.shape)
# print(c.itemsize)
# print(c.nbytes)

# i=[[[[1,2,3]],[[1,2,3]]]]
# c=np.array(i)
# print(c.shape)
# print(c.ndim)
# print(c.size)
# print(c.dtype)
# print(c.itemsize)
# print(c.nbytes)

# i=(1,2,2)
# a=np.array(i)
# print(a)
# print(a.size)
# print(a.dtype)
# print(a.nbytes)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize)
# print("-"*5)

# i=((1,2,2),(4,6,7))
# a=np.array(i)
# print(a)
# print(a.size)
# print(a.dtype)
# print(a.nbytes)
# print(a.ndim)
# print(a.shape)
# print(a.itemsize)


# a=[4,5,6,]
# b=np.array(a)
# c=[9,5,6]
# d=np.array(c)
# print(a+c)
# print(a+b)
# print(b+c)
# print(b+d)
# print("-"*5)

# a=[4,5,6,]
# b=np.array(a)
# c=[9,5,6]
# d=np.array(c)
# # print(a*c)
# print(a*b)
# print(b*c)
# print(b*d)
# print("-"*5)

# a=[4,5,6,]
# b=np.array(a)
# c=[9,5,6]
# d=np.array(c)
# # print(a/c)
# print(a/b)
# print(b/c)
# print(a/d)



# arange
# a=np.arange(1,11,1)
# print(type(a))
# print(a)
# print("------")
# b=np.arange(1,10,3)
# print(b)
# print("---------")
# c=np.arange(12)
# print(c)
# print("--------")
# d=np.arange(11,25,1)
# e=np.array(d)
# print(type(e))
# print(e)

# linespace
# a=np.linspace(1,1)
# print(type(a))
# print(a)
# print("=====")
# b=np.linspace(1,2,4)
# print(b)
# print("------")
# c=np.linspace(10,1)
# print(c)
# print("===")
# d=np.linspace(1,10,10)
# print(d)
# e=np.arange(1,10,1)
# print(e)


# a=np.zeros([10,3,15])
# print(type(a))
# print(a.ndim)
# print(a)


# d=np.ones([2,5,2])
# print(d)

# a=np.eye(3)
# print(a)
# print("==")
# b=np.eye(7,3)
# print(b)

# a=np.arange(0,18).reshape(2,3,3)
# print(a)
# print(a.shape)

# a=np.array([1,2,3])
# a=np.tile(a,(3))
# print(a)

# a=np.array([1,2,3,4])
# print(a)
# print(a.dtype)
# print(a.astype(float))
# print(a.astype(str))

# a=np.random.rand(2,2,3)
# print(a)
# print(a.ndim)
# print(a[0])
# print(a[1])
# print("=====")

# a=np.random.randint(1,10,(2,3,5))
# print(a)
# print(a.ndim)
# print(a[1,2,-2])
# print("=====")

a=np.random.randn(4,2,5)
print(a)
print(a.ndim)
print(a[0,1])
print("======")

# a=np.array([1,10])
# b=np.random.choice(a,(5,2,3))
# print(b)
# print(a[0])


