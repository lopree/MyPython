import tensorflow as ten

tf = ten.constant('Hello,Work!')

sess = ten.Session()

print(sess.run(tf))