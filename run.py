import web
from web import form

render = web.template.render('templates/')

urls = (
    '/', 'index'
)
app = web.application(urls, globals())

offer1 = form.Form(
	form.Textbox("Salary",
		form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="$35,000"), 
    form.Textbox("Annual Raise", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3.5%"),
    form.Textbox("401K Contribution", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="6%"),
    form.Textbox("401K Match", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3%"))

offer2 = form.Form(
	form.Textbox("Salary",
		form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="$35,000"), 
    form.Textbox("Annual Raise", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3.5%"),
    form.Textbox("401K Contribution", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="6%"),
    form.Textbox("401K Match", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3%"))

details = form.Form(
	form.Textbox("Current Age",
    	form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        form.Validator(' Must be less than 65', lambda x:int(x)<65)),
    form.Textbox("Market growth", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="6%"))


class index:        
    def GET(self):
    	form1 = offer1()
    	form2 = offer2()
    	form3 = details()
       	return render.formtest(form1, form2, form3)

    def POST(self):
    	form1 = offer1()
    	form2 = offer2()
    	form3 = details()
    	if not offer1.validates():
    		return render.formtest(form1, form2, form3)
    	else:
    		lowerSalary = form["Lower Salary"].value
    		higherSalary = form["Higher Salary"].value
    		currentAge = form["Current Age"].value
    		annualRaise = form["Annual Raise"].value

    		career = 66 - int(currentAge)
    		totalLow = 0
    		totalHigh = 0
    		lowYear = float(lowerSalary)
    		highYear = float(higherSalary)
    		for year in range(career):
    			totalLow = totalLow + lowYear
    			totalHigh = totalHigh + highYear
    			lowYear = (lowYear * (100 + float(annualRaise)))/100
    			highYear = (highYear * (100 + float(annualRaise)))/100

    		difference = totalHigh - totalLow
    		return '''
    		Lower: %s
    		Higher: %s
    		Age: %s
    		Raise: %s
    		Extra Earnings: %s
    		''' % (lowerSalary, higherSalary, currentAge, annualRaise, difference)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
