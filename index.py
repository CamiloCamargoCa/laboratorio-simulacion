from flask import Flask, render_template
from scipy.stats.distributions import chi2

app = Flask(__name__)


# http://127.0.0.1:8080/Xo/59/a/21/c/13"
# @app.route('/Xo/<int:XoIn>/a/<int:aIn>/c/<int:cIn>')
def home(XoIn1,aIn1,cIn1):
	# m = 101
	# Xo = 59
	# M = 100
	# a = 21
	# c = 13

	m = 100
	Xo = XoIn1
	M = 100
	a = aIn1
	c = cIn1

	aux = {0:Xo}
	aux1 = {0:Xo}
	u = {0:Xo}
	labels = [0]
	values = [Xo]
	# print(aux[0])

	for i in range(1,m):
		# print(i)
		aux[i] = (aux[i-1]*a+c)%M
		aux1[i] = (aux[i-1]*a+c)%M
		labels.append(i)
		values.append(aux[i])


	for j in aux:
		u[j]=aux[j]/M
	

	dataArray = {
        "data": 0,
        "labelsArray": {},
        "valuesArray": {}
    }


	dataArray['data']=u
	dataArray['labelsArray']=labels
	dataArray['valuesArray']=values
	dataArray['aux1']=aux1
	

	# print(u)
	# print(dataArray)
	# print(labels)
	# print(values)
	# return render_template("graph.html",labels=labels, values=values, puntos=u)
	return dataArray




@app.route('/Xo/<int:XoIn>/a/<int:aIn>/c/<int:cIn>')
def pruebaLaboratorio(XoIn,aIn,cIn):
	datatemp = home(XoIn,aIn,cIn)
	data = datatemp['data']
	aux1 = datatemp['aux1']
	cantidad = len(data)
	suma=0
	promedio=0
	sumaCuadrada=0
	vr=0
	
	# print(data)	
	# suma
	for num in range(0,100):
		suma = suma+data[num]
	

	# promedio
	promedio=(suma/cantidad)


	for num in range(0,100):
		# print("para numero: "+str(data[num])+" valor es: "+str(((data[num]-promedio)**2)))
		sumaCuadrada += ((data[num]-promedio)**2)


	vr = sumaCuadrada/(cantidad-1)
	a = 0.05
	n_1 = cantidad-1
	ali = a/2
	als = 1-(ali)
	divi = (12*n_1)
	lstemp = chi2.ppf(ali, n_1)
	litemp = chi2.ppf(als, n_1)
	li = chi2.ppf(als, n_1)/divi
	ls = chi2.ppf(ali, n_1)/divi
	labels = datatemp['labelsArray']
	values = datatemp['valuesArray']


	
	# print(aux1)
	# print(ls)
	# print(n_1)
	# print(divi)
	# print(ali)
	# print(als)
	# print(labels)
	# print(values)
	# print(data)
	return render_template("graph.html",labels=labels, values=values, puntos=data, a=a, n_1=n_1, ali=ali, als=als, li=li, ls=ls, vr=vr, litemp=litemp, lstemp=lstemp,cantidad=cantidad, divi=divi, aux1=aux1)
	# return render_template("graph.html",labels=labels, values=values)





# if __name__ == '__main__':
# 	# print(d)
# 	pruebaLaboratorio(59,21,13)
# 	# home(59,21,13)
# 	app.run(host='127.0.0.1', port=8080, debug=True)


# from flask import Flask

# app = Flask(__name__)


# @app.route('/')
# def hello():
#     return 'Hello, World!'

if __name__ == '__main__':
	# print(d)
	# pruebaLaboratorio(59,21,13)
	# home(59,21,13)
	# hello()
	app.run(host='127.0.0.1', port=8000, debug=True)