from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from pages.models import Properties, Agent, Transaction
from django.contrib import messages
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
import PyPDF2

# def render_to_pdf(template_src, context_dict={}):
# 	template = get_template(template_src)
# 	html  = template.render(context_dict)
# 	result = BytesIO()
# 	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
# 	if not pdf.err:
# 		return HttpResponse(result.getvalue(), content_type='application/pdf')
# 	return None


@login_required
def createinvoice(request):
			
	# if request.user.is_authenticated:
		if request.method == 'POST':
			context = None
			first= request.POST['first']
			last= request.POST['last']
			address= request.POST['address']
			service= request.POST['service']
			cost= request.POST['cost']
			method= request.POST['method']
			charge= request.POST['charge']
			contact= request.POST['contact']
			charged= (int(request.POST['charge'])/100)* int(request.POST['cost'])
			date= request.POST['date']
			agent= request.POST['agent']
			description= request.POST['description']
			p = Transaction(first=first, last=last, address=address, service=service, sales_price=cost, percent_charged = charge, payment_method =method, agent=agent, date=date)
			p.save()
			data  = {
			'first': request.POST['first'],
			'last': request.POST['last'],
			'address': request.POST['address'],
			'service': request.POST['service'],
			'cost': request.POST['cost'],
			'method': request.POST['method'],
			'charge': request.POST['charge'],
			'contact': request.POST['contact'],
			'charged': (int(request.POST['charge'])/100)* int(request.POST['cost']),
			'date': request.POST['date'],
			'description': "service charge sales of a plot of land",
			"company": "Ahodwoproperties",
			"phone": "055 3246 573 / 050 461 3609",
			"email": "info@ahodwoproperties.com",
			"website": "Ahodwoproperties.com",
			}
			
			
		
		
			return render(request, 'pages/pdf_template.html', {'data': data})
		return render(request, 'pages/index.html')
	# return redirect('login')

#Opens up page as PDF
# class ViewPDF(View):
	
# 	def get(self, request, *args, **kwargs):
# 		print(request.POST)

# 		pdf = render_to_pdf('pages/pdf_template.html', data)
# 		return HttpResponse(pdf, content_type='application/pdf')


#Automaticly downloads to PDF file
# class DownloadPDF(View):
# 	def get(self, request, *args, **kwargs):
		
# 		pdf = render_to_pdf('pages/pdf_template.html', data)

# 		response = HttpResponse(pdf, content_type='application/pdf')
# 		filename = "Invoice_%s.pdf" %("12341231")
# 		content = "attachment; filename='%s'" %(filename)
# 		response['Content-Disposition'] = content
# 		return response



@login_required
def properties(request):
	if request.method == 'POST':
		location = request.POST['location']
		description = request.POST['description']
		owner = request.POST['owner']
		contact = request.POST['contact']
		price = request.POST['price']
		image = request.POST['image']
		property_id = request.POST['id']
		p = Properties(location=location, description=location, owner=owner, owner_contact=contact, price=price, image=image, property_id=property_id)
		p.save()
	return render(request, 'pages/properties.html')



@login_required
def agent(request):
	if request.method == 'POST':
		first = request.POST['first']
		last = request.POST['last']
		address = request.POST['address']
		contact = request.POST['contact']
		position = request.POST['position']
		agent_id = request.POST['id']
		p = Agent(first=first, last=last, address=address, contact=contact, position=position, agent_id =agent_id)
		p.save()
	return render(request, 'pages/agent.html')


@login_required
def index(request):
	p= Agent.objects.all()
	return render(request, 'pages/index.html', {'agent':p})

	