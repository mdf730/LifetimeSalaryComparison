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
	form.Textbox("Salary 2",
		form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="$35,000"), 
    form.Textbox("Annual Raise 2", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3.5%"),
    form.Textbox("401K Contribution 2", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="6%"),
    form.Textbox("401K Match 2", 
        form.notnull,
        form.regexp('\d+', 'Must be a digit'),
        placeholder="3%"))

details = form.Form(
	form.Textbox("Age",
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
    	elif not offer2.validates():
    		return render.formtest(form1, form2, form3)
    	elif not details.validates():
    		return render.formtest(form1, form2, form3)
    	else:
    		salary1 = offer1["Salary"].value
    		salary2 = offer2["Salary 2"].value
    		currentAge = details["Age"].value
    		raise1 = offer1["Annual Raise"].value
    		raise2 = offer2["Annual Raise 2"].value
    		contribution1 = offer1["401K Contribution"].value
    		contribution2 = offer2["401K Contribution 2"].value
    		match1 = offer1["401K Match"].value
    		match2 = offer2["401K Match 2"].value
    		market = details["Market growth"].value

    		career = 66 - int(currentAge)

    		totalLow = 0
    		totalHigh = 0

    		totalRetireLow = 0
    		totalRetireHigh = 0
    		
    		lowYear = float(salary2)
    		highYear = float(salary1)

    		retireLowYear = float(salary2)*(float(contribution2)+float(match2))/100
    		retireHighYear = float(salary1)*(float(contribution1)+float(match1))/100
    		
    		for year in range(career):
    			# FORM 1
    			totalHigh = totalHigh + highYear*(100 - float(contribution1))/100
    			highYear = (highYear * (100 + float(raise1)))/100
    			totalRetireHigh = totalRetireHigh*(100 + float(market))/100 + retireHighYear
    			retireHighYear = highYear * (float(contribution1)+float(match1))/100
    			
    			# FORM 2
    			totalLow = totalLow + lowYear*(100 - float(contribution2))/100
    			lowYear = (lowYear * (100 + float(raise2)))/100
    			totalRetireLow = totalRetireLow*(100 + float(market))/100 + retireLowYear
    			retireLowYear = lowYear * (float(contribution2)+float(match2))/100

    			print totalHigh,
    			print totalLow,
    			print totalRetireHigh,
    			print totalRetireLow

    		difference = totalHigh + totalRetireHigh - totalLow - totalRetireLow
    		return render.formresults(difference)

if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
