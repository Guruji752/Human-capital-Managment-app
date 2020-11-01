from __future__ import unicode_literals
import csv
import json
import os
from PIL import Image
from django.conf import settings
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.core import serializers
from django.shortcuts import render
#from django.shortcuts import render_to_response
from django.template import Template
from django.template.loader import get_template
from django.db.models import Q
from django.contrib.auth import update_session_auth_hash
from django.template.loader import render_to_string
from django.views import View
from django.views.decorators.cache import cache_control
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.utils.encoding import smart_str
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from aditshsoft.common import CommonPagination, SaveCsvSheet
from aditshsoft.common import Getmonthlist, SiteUrl, SendSmsEmailAndNotification
from aditshsoft.common import Getyearlist, time_slots, Getyearlist1, GetAndManageHierarchyOfEmployee
from employee_website.models import *
from admin_main.models import *
from hrms_employees.models import *
from employee_website.forms import *
from knowleage_tranning.forms import *
from datetime import date, datetime
from django.db.models import Q


class EmployeeServicesRecruitementUpdateConsultantsList(View):
	#import pdb
	#pdb.set_trace()
	template = 'employee_website/employee_services/recruitement/update_consultants_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report_p = EmployeeServicesRecruitementUpdateConsultantsDetails.objects.all().order_by('-id')
		get_report = EmployeeServicesRecruitementUpdateConsultants.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			# 'get_report_p':get_report_p,
		}
		return render(request, self.template, context)

##123
class AddEditCrmEmployeeServicesRecruitementUpdateConsultants(View):
	template = 'employee_website/employee_services/recruitement/add_edit_update_consultants.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id=None):
		if not request.user.is_authenticated:
			return redirect('index')

		# form1 = EmployeeServicesRecruitementUpdateConsultantsmodelForm()
		form_address = EmployeeServicesRecruitementUpdateConsultantsAddressForm()
		location_list=  ManageBranch.objects.all()
		
		context = {
			# "form":form1 ,
			"form_address":form_address,
			'location_list':location_list,
		}
		return render(request, self.template, context)

	def post(self,request,id=None):
		# import pdb
		# pdb.set_trace()
	
		try:
			if not request.user.is_authenticated:
				return redirect('index')
			if request.method=="POST":
				# import pdb
				# pdb.set_trace()
				form = EmployeeServicesRecruitementUpdateConsultantsAddressForm(request.POST)
				if form.is_valid():
					form.save()
					messages.add_message(request, messages.SUCCESS, "Data is Save SuccessFully.")
					return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')
				else:
					messages.add_message(request, messages.ERROR, "Something went wrong.")
					return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')

				# try:	
				# 	form1 = EmployeeServicesRecruitementUpdateConsultantsAddressForm(request.POST)
					
				# 	if form1.is_valid():
				# 		form1.save()
				# 	messages.add_message(request, messages.SUCCESS, "Data is Save SuccessFully.")
				# 	return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')
				# except Exception as ee:
				# 	messages.add_message(request, messages.ERROR, "pan card already registered.")
				# 	return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')

		except Exception as ee:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
			return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')


def EditCrmEmployeeServicesRecruitementUpdateConsultants(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementUpdateConsultants, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementUpdateConsultantsAddressForm(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')
    else:
        form = EmployeeServicesRecruitementUpdateConsultantsAddressForm(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_update_consultants.html', {'form': form})


			

	


class EmployeeServicesRecruitementUpdateConsultantsDelete(View):
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementUpdateConsultants.objects.filter(id = id).delete()
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_updateconsultants_list')


# 2
class EmployeeServicesRecruitementCreateRequirementList(View):
	template = 'employee_website/employee_services/recruitement/create_requirement_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class AddEditCrmEmployeeServicesRecruitementCreateRequirement(View):
	template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')

		if id is None:
			form = EmployeeServicesRecruitementCreateRequirementmodelForm1()
		else:
			data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
			form = EmployeeServicesRecruitementCreateRequirementmodelForm1(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if id is None:
			
			form = EmployeeServicesRecruitementCreateRequirementmodelForm1(request.POST)
			if form.is_valid():
				data = form.save()
				data.user_id = request.user.id
			
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		else:
			data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
			form = EmployeeServicesRecruitementCreateRequirementmodelForm1(request.POST, instance = data)
			if form.is_valid():
				data = form.save()
				data.user_id = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_createrequirement_list')


class EmployeeServicesRecruitementCreateRequirementDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id = id).delete()
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_createrequirement_list')


# 3
'''class EmployeeServicesRecruitementApproveVacanciesList(View):
	template = 'employee_website/employee_services/recruitement/approved_vacancies_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)
#
#'''
#EmployeeServicesRecruitementCreateRequirementmodelUpdateForm

class AddEditCrmEmployeeServicesRecruitementApproveVacancies(View):
	template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		# form = EmployeeServicesRecruitementApproveVacanciesUpdateForm(instance=data)
		form =EmployeeServicesRecruitementCreateRequirementmodelForm3(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		# form = EmployeeServicesRecruitementApproveVacanciesUpdateForm(request.POST, instance = data)
		form = EmployeeServicesRecruitementCreateRequirementmodelForm3(request.POST, instance = data)
		if form.is_valid():
			data = form.save()		# form = EmployeeServicesRecruitementApproveVacanciesUpdateForm(request.POST, instance = data)

			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_approvevacancies_list')







#########################Show Requirement###################################################################
class EmployeeServicesRecruitementApproveVacanciesList(View):
	template = 'employee_website/employee_services/recruitement/approved_vacancies_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(is_filled=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)




class EmployeeServicesShowRequirement(View):
	template = 'employee_website/employee_services/recruitement/approved_vacancies_list_2.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(is_filled=0).order_by('-id')
		#EmployeeServicesRecruitementCreateRequirement.objects.update(is_filled=1)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


def EditEmployeeServicesShowRerquirement(request, id):

	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.department_id=data[0].department
		form.designation_id=data[0].designation
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.job_description=data[0].job_description
		form.qualification_id=data[0].designation
		form.experience_id=data[0].experience
		form.language=data[0].language
		form.time_frame_1=data[0].time_frame_1
		form.type_of_job_id=data[0].type_of_job
		form.pay_roll_job_id=data[0].pay_roll_job
		form.gender=data[0].gender
		form.recommendation=request.POST.get('recommendation')
		form.job_description=data[0].job_description
		form.comment=request.POST.get('comment')
		if(form.recommendation=='Recommended'):
			form.is_recommended=1
		form.is_filled=1		
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_filled=1)
		return redirect('crm_website_employeeservices_recruitement_approvevacancies_list')

	else:
		form = EmployeeServicesRecruitementCreateRequirementmodelForm3(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/recruitement/recommend_add.html', context)






class EmployeeServicesRecruitementShowRequirementDelete(View):
	def get(self, request, id):
		#import pdb
		#pdb.set_trace()
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_filled=0)

		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_show_requirement_list')




def EditEmployeeServicesRecruitementRecommendedRequirement(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementCreateRequirementmodelForm3(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_approvevacancies_list')
    else:
        form = EmployeeServicesRecruitementCreateRequirementmodelForm3(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_recommended_requirement.html', {'form': form})




        

class RecommendedView(View):
	template = 'employee_website/employee_services/recruitement/recommended_view.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request,id):
		services = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, services, self.pagesize)

		return render(request, self.template, {'responselistquery': report_paginate,})


#list wala html bna

############################################# Show Requirement end Here ###########################################################3












##################################### HR Review of Requirement ##############################################################################3
class EmployeeServicesRecruitementHrReviewApproveList(View):
	
	template = 'employee_website/employee_services/recruitement/hr_review_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(hr_status=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

def EditEmployeeServicesRecruitementHrReview(request, id):

	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.department_id=data[0].department
		form.designation_id=data[0].designation
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.job_description=data[0].job_description
		form.qualification_id=data[0].designation
		form.experience_id=data[0].experience
		form.language=data[0].language
		form.time_frame_1=data[0].time_frame_1
		form.type_of_job_id=data[0].type_of_job
		form.pay_roll_job_id=data[0].pay_roll_job
		form.gender=data[0].gender
		form.hr_action=request.POST.get('hr_action')
		form.job_description=data[0].job_description
		form.comment=data[0].comment
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_status=1)
		return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')

	else:
		form = EmployeeServicesHrReviewActionForm(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/recruitement/hr_review_action.html', context)




class EmployeeServicesRecruitementHrReviewList(View):
	#import pdb
	#pdb.set_trace()
	template = 'employee_website/employee_services/recruitement/hr_review_show_requirement.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(hr_status=0).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

	



class EmployeeServicesRecruitementHrReviewedList(View):
	
	template = 'employee_website/employee_services/recruitement/hr_review_action.html'
	pagesize = 10
	#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id):
		
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_recommended = 'Recommended',is_hrrecommend=1)
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(hr_recommended = 'Recommended' ).order_by('-id')
		return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')
	





class EmployeeServicesRecruitementRejected(View):
	template = 'employee_website/employee_services/recruitement/menus_comments.html'
	pagesize = 10
	#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_recommended='Rejected',is_hrrecommend=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=Employeeserviceshrreviewcomment(instance=data)
		context = {
			'responselistquery': report_paginate,
			'form': form
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = Employeeserviceshrreviewcomment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')



class EmployeeServicesRecruitementPutOnHold(View):
	template = 'employee_website/employee_services/recruitement/menus_comments.html'
	pagesize = 10
	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_recommended='Put on hold',is_hrrecommend=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=Employeeserviceshrreviewcomment(instance=data)
		context = {
			'responselistquery': report_paginate,
			'form':form
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = Employeeserviceshrreviewcomment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')



def EditEmployeeServiceRecruitementHrReview(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
	
	if request.method == "POST":
		
		#EmployeeServicesRecruitementCreateRequirement.objects.filter(id=id).delete()
		form=EmployeeServicesRecruitementRecommended()
		form.location_id=request.POST.get('location')
		form.department_id=request.POST.get('department')
		form.designation_id=request.POST.get('designation')
		form.existing_strength=request.POST.get('existing_strength')
		form.new_requirement=request.POST.get('new_requirement')
		form.total_strength = request.POST.get('total_strength')
		form.salary_range_id=request.POST.get('salary_range')
		form.qualification_id=request.POST.get('qualification')
		form.experience_id=request.POST.get('experience')
		form.language_id=request.POST.get('language')
		form.time_frame_1=request.POST.get('time_frame_1')
		form.type_of_job_id=request.POST.get('type_of_job')
		form.pay_roll_job_id=request.POST.get('pay_roll_job')
		form.gender=request.POST.get('gender')
		form.recommendation=request.POST.get('recommendation')
		form.job_description=request.POST.get('job_description')
		form.comment=request.POST.get('comment')
		form.save()
		return redirect('crm_website_employeeservices_recruitement_hr_review_requirement_list')
	else:
		form = EmployeeServicesRecruitementCreateRequirementmodelForm3(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/recruitement/add_edit_update_hr_review_requirement.html', context)




class AddEditCrmEmployeeServicesRecruitementHrReview(View):
	template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		#form = EmployeeServicesRecruitementApproveVacanciesUpdateForm(instance=data)
		form =EmployeeServicesRecruitementHrReviewEditform(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementHrReviewDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_status=0,hr_recommended='pending',is_recommended=0,is_filled=0)
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_hr_review_requirement_list')


class EmployeeServicesRecruitementHrReviewDelete2(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(hr_status=0,hr_recommended='pending',is_recommended=1)
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_hr_review_requirement_list')



class EmployeeServiceRecruitemtnHrReviewView(View):
	template='employee_website/employee_services/recruitement/modify_hr_requirement.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request,id):
		if not request.user.is_authenticated:
			return redirect('index')
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicesRecruitementCreateRequirementmodelUpdateForm(instance=data)
		context	={
		'form':form
		}
		return render(request,self.template,context)

def EditEmployeeServicesRecruitementHRRequirement(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementHrReviewEditform(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')
    else:
        form = EmployeeServicesRecruitementHrReviewEditform(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/modify_hr_requirement.html', {'form': form})




############################### APPROVED REQUIREMENT ##############################################################################33

class EmployeeServicesRecruitementReviewedRequirementList(View):
	template = 'employee_website/employee_services/recruitement/approved_requirement_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(approval_status=1)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)



class EmployeeServicesRecruitementAllRequirementList(View):
	template = 'employee_website/employee_services/recruitement/approved_requirement.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(hr_action='Recommended',approval_status=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)
#

def EditEmployeeServiceRecruitementApprovalRequirementAction(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
	
	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.department_id=data[0].department
		form.designation_id=data[0].designation
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.job_description=data[0].job_description
		form.qualification_id=data[0].designation
		form.experience_id=data[0].experience
		form.language=data[0].language
		form.time_frame_1=data[0].time_frame_1
		form.type_of_job_id=data[0].type_of_job
		form.pay_roll_job_id=data[0].pay_roll_job
		form.gender=data[0].gender
		form.approval_action=request.POST.get('approval_action')
		form.job_description=data[0].job_description
		form.comment=data[0].comment
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(approval_status=1)
		return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')

	else:
		form = EmployeeServicesApprovalActionForm(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/recruitement/approval_action.html', context)








class EmployeeServicesRecruitementApprovedRecommendedRequirementsList(View):
	template = 'employee_website/employee_services/recruitement/approved_requirement_list.html'
	pagesize = 10
	def get(self, request,id):
		
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_approve= 'Approve',approve_status=1)
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(is_approve = 'Approve' )
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')



class EmployeeServicesRecruitementReferedBack(View):
	pagesize=10
	template = 'employee_website/employee_services/recruitement/menus_comments.html'

	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_approve='pending',approve_status=0,hr_recommended='Refered back')
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicesApproveRequirementcomment(instance=data)
		context = {
			'form':form,
			'responselistquery':report_paginate
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = EmployeeServicesApproveRequirementcomment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_hr_review_approve_requirement_list')

class EmployeeServicesRecruitementrejected(View):
	template = 'employee_website/employee_services/recruitement/menus_comments.html'
	pagesize = 10
	#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_approve='Rejected',approve_status=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicesApproveRequirementcomment(instance=data)
		context = {
			'form':form,
			'responselistquery':report_paginate
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = EmployeeServicesApproveRequirementcomment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')


class EmployeeServicesRecruitementputonhold(View):
	
	template = 'employee_website/employee_services/recruitement/menus_comments.html'
	pagesize = 10
	#@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_approve='Put on hold',approve_status=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicesApproveRequirementcomment(instance=data)
		context = {
			'form':form,
			'responselistquery':report_paginate
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = EmployeeServicesApproveRequirementcomment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')

#EmployeeServicesRecruitementCreateRequirementmodelUpdateForm

class AddEditCrmEmployeeServicesCreatedApproveRequirementView(View):
	template = 'employee_website/employee_services/recruitement/modify_hr_requirement.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		# form = EmployeeServicesRecruitementApproveVacanciesUpdateForm(instance=data)
		form =EmployeeServicesRecruitementCreateRequirementmodelUpdateForm(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	

class EmployeeServicesRecruitementReviewedRequirementDelete(View):
	
	def get(self,request,id):

		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(approval_status=0,approval_action='pending')

		return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')





def EditEmployeeServicesRecruitementApproveRequirementEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementApproveRequirementEditform(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_approve_reviewed_list')
    else:
        form = EmployeeServicesRecruitementApproveRequirementEditform(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/modify_hr_requirement.html', {'form': form})





			#########################Publish jobs################################



class EmployeeServicesRecruitementPublishVacanciesList(View):
	template = 'employee_website/employee_services/recruitement/publish_jobs.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(internal_source_status=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeServicesRecruitementAllPublishVacanciesList(View):
	template = 'employee_website/employee_services/recruitement/publish_jobs_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(approval_action='Approve',internal_source_status=0)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)




def EmployeeservicesRecruitementPublishVacancies(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.department_id=data[0].department
		form.job_description=data[0].job_description
		form.designation_id=data[0].designation
		form.mode_of_publishing=request.POST.get('mode_of_publishing')
		form.vacancy_posted=request.POST.get('vacancy_posted')
		form.mode_of_response=request.POST.get('mode_of_response')
		form.name=request.POST.get('name')
		form.valid_upto=request.POST.get('valid_upto')
		form.approval_action='Approve'
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(internal_source_status=1,internal_source_action='Published')
		
		return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')
	else:
		form = EmployeeServicesRecruitementPublishVacanciesForm(instance=company)
		#form.save()
		context= {
            'form': form
        }

		return render(request,'employee_website/employee_services/recruitement/Publish_vacancies.html',context)


class EmployeeServicesRecruitementPublishVacanicesRejected(View):
	pagesize=10
	template = 'employee_website/employee_services/recruitement/menus_comments.html'

	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(publish_status='Rejected',is_publish=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicePublishJobComment(instance=data)
		context = {
			'form':form,
			'responselistquery': report_paginate
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = EmployeeServicePublishJobComment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')


class EmployeeServicesRecruitementPublishVacanciesPutOnHold(View):
	pagesize=10
	template = 'employee_website/employee_services/recruitement/menus_comments.html'

	def get(self, request,id):
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(publish_status='Put on hold',is_publish=1)
		data=get_object_or_404(EmployeeServicesRecruitementRecommended,pk=id)
		form=EmployeeServicePublishJobComment(instance=data)
		context = {
			'form':form,
			'responselistquery': report_paginate
		}
		return render(request,self.template,context)
	def post(self, request, id):
		data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
		form = EmployeeServicePublishJobComment(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')




class EmployeeServicesRecruitementPublishVacanicesDelete(View):
	def get(request,self,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(internal_source_status=0)
		return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')






class AddEditCrmEmployeeServicesRecruitementPublishVacancies(View):
	template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementPublishJobs, pk=id)
		form = EmployeeServicesRecruitementPublishVacanciesForm(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		data = get_object_or_404(EmployeeServicesRecruitementPublishJobs, pk=id)
		form = EmployeeServicesRecruitementPublishVacanciesForm(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')



def EditEmployeeServicesRecruitementPublishJobsEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementPublishVacanciesForm(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_publishvacancies_list')
    else:
        form = EmployeeServicesRecruitementPublishVacanciesForm(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_publish_job.html', {'form': form})


################################################# Publish job consultant #####################################

class EmployeeServicesRecruitementPublishJobConsultant(View):
	template = 'employee_website/employee_services/recruitement/publish_job_conultant_display.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(consultant_source_action=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementPublishJobConsultantAll(View):
	template = 'employee_website/employee_services/recruitement/publish_job_consultant_all.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(approval_action='Approve',consultant_source_action=0)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


def EmployeeservicesRecruitementPublishVacanciesConsultant(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.department_id=data[0].department
		form.job_description=data[0].job_description
		form.designation_id=data[0].designation
		form.mode_of_publishing=request.POST.get('mode_of_publishing')
		form.vacancy_posted=request.POST.get('vacancy_posted')
		form.mode_of_response_consultant=request.POST.get('mode_of_response_consultant')
		form.name=request.POST.get('name')
		form.valid_upto_consultant=request.POST.get('valid_upto_consultant')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(consultant_source_status='Published',consultant_source_action=1)
		return redirect('publish_jobs_consultant')
	else:
		form = EmployeeServicesRecruitementPublishVacanciesConsultantForm(instance=company)
		#form.save()
		context= {
            'form': form
        }

		return render(request,'employee_website/employee_services/recruitement/publish_vacancies_consultant_edit.html',context)

class EmployeeServicesRecruitementPublishVacanciesConsultant(View):
	def get(request,self,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(consultant_source_action=0)
		return redirect('publish_jobs_consultant_all')

########################################### Publish Job Portal ###############################

class EmployeeServicesRecruitementPublishJobPortal(View):
	template = 'employee_website/employee_services/recruitement/publish_job_portal_display.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(jon_portal_action=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementPublishJobPortalAll(View):
	template = 'employee_website/employee_services/recruitement/publish_job_portal_all.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(jon_portal_action=0,approval_action='Approve')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

def EmployeeservicesRecruitementPublishVacanciesJobPortal(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.department_id=data[0].department
		form.job_description=data[0].job_description
		form.designation_id=data[0].designation
		form.valid_upto_job_portal=request.POST.get('valid_upto_job_portal')
		form.mode_of_response_job_portal=request.POST.get('mode_of_response_job_portal')
		form.portal_name=request.POST.get('portal_name')
		form.url_job_portal=request.POST.get('url_job_portal')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(job_portal_status='Published',jon_portal_action=1)
		return redirect('publish_job_portal')
	else:
		form = EmployeeServicesRecruitementPublishVacanciesJobPortalForm(instance=company)
		#form.save()
		context= {
            'form': form
        }

		return render(request,'employee_website/employee_services/recruitement/publish_vacancies_job_portal_edit.html',context)

class EmployeeServicesRecruitementPublishVacanciesJobPortal(View):
	def get(request,self,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(jon_portal_action=0)
		return redirect('publish_jobs_portal_all')



################################################################################################
#################################### Publish job Webiste #########################################

class EmployeeServicesRecruitementPublishJobWebiste(View):
	template = 'employee_website/employee_services/recruitement/webiste_display.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(jon_portal_action=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementPublishJobWebisteAll(View):
	template = 'employee_website/employee_services/recruitement/webiste_all_publish_jobs.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(jon_portal_action=0,approval_action='Approve')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

def EmployeeservicesRecruitementPublishVacanciesWebsiteEdit(request, id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	

	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended(id=id)
		form.location_id=data[0].location
		form.total_strength=data[0].total_strength
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.department_id=data[0].department
		form.job_description=data[0].job_description
		form.designation_id=data[0].designation
		form.valid_upto_job_portal=request.POST.get('valid_upto_job_portal')
		form.mode_of_response_job_portal=request.POST.get('mode_of_response_job_portal')
		form.portal_name=request.POST.get('portal_name')
		form.url_job_portal=request.POST.get('url_job_portal')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(job_portal_status='Published',jon_portal_action=1)
		return redirect('publish_job_portal')
	else:
		form = EmployeeServicesRecruitementPublishVacanciesJobPortalForm(instance=company)
		#form.save()
		context= {
            'form': form
        }

		return render(request,'employee_website/employee_services/recruitement/publish_vacancies_job_portal_edit.html',context)

class EmployeeServicesRecruitementPublishVacanciesWebisteDelete(View):
	def get(request,self,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(jon_portal_action=0)
		return redirect('publish_jobs_portal_all')


##################################################################################################


##################################################  Resume Recipet #############################################################

class EmployeeServicesRecruitementInviteResumeList(View):
	template = 'employee_website/employee_services/recruitement/invite_resume_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(updated_resume=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)
########################## Resume Bank ##############

class EmployeeServicesRecruitementResumeBankList(View):
	template = 'employee_website/employee_services/recruitement/resume_bank.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(updated_resume=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)





class AddEmployeeServicesRecruitementResume(View):
	template = 'employee_website/employee_services/recruitement/add_invite_resume.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(publish_status='Publish',updated_resume=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)



def AddEditCrmEmployeeServicesRecruitementResume2(request, id):

                	
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.mode_of_publishing=data[0].mode_of_publishing
		form.name=data[0].name
		form.location_id=data[0].location_id
		form.new_requirement=data[0].new_requirement
		form.existing_strength=data[0].existing_strength
		form.total_strength=data[0].total_strength
		form.vacancy_posted=data[0].vacancy_posted
		form.mode_of_response=data[0].mode_of_response
		form.valid_upto=data[0].valid_upto
		form.department_id=data[0].department_id
		form.job_description=data[0].job_description
		form.designation_id=data[0].designation_id
		form.name_of_candidate = request.POST.get('name_of_candidate')
		form.email_id=request.POST.get('email_id')
		form.resume_received_doc=request.FILES['resume_received_doc']
		form.phone_no=request.POST.get('phone_no')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_publish=1,approve_status=1,is_filled=1,is_recommended=True,updated_resume=1)

		return redirect('crm_website_employeeservices_recruitement_inviteresume_list')
	else:
		form = EmployeeServicesRecruitementesumeAddForm1(instance=company)
	#form.save()
		context= {
        		'form': form
    			}

	return render(request,'employee_website/employee_services/recruitement/add_edit_invite_resume.html',context)

def EditEmployeeServicesRecruitementresumerecipetEdit(request, id):

    company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
    if request.method == "POST":
    	data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
    	if data.exists():
    		form = EmployeeServicesRecruitementRecommended.objects.get(id=id)
    	else:
    		form=EmployeeServicesRecruitementRecommended()
    	form.mode_of_publishing=data[0].mode_of_publishing
    	form.name=data[0].name
    	form.location_id=data[0].location_id
    	form.new_requirement=data[0].new_requirement
    	form.existing_strength=data[0].existing_strength
    	form.total_strength=data[0].total_strength
    	form.vacancy_posted=data[0].vacancy_posted
    	form.mode_of_response=data[0].mode_of_response
    	form.valid_upto=data[0].valid_upto
    	form.department_id=data[0].department_id
    	form.job_description=data[0].job_description
    	form.designation_id=data[0].designation_id
    	form.name_of_candidate = request.POST.get('name_of_candidate')
    	form.email_id=request.POST.get('email_id')
    	form.resume_received_doc=request.FILES['resume_received_doc']
    	form.phone_no=request.POST.get('phone_no')
    	form.save()
    	EmployeeServicesRecruitementRecommended.objects.filter(id=id)
    	return redirect('crm_website_employeeservices_recruitement_inviteresume_list')
    else:
    	form  =  EmployeeServicesRecruitementesumeAddForm1(instance=company)
    	context= {
				'form': form
    			}
    return render(request, 'employee_website/employee_services/recruitement/edit_resume_recipet.html', {'form': form})








class AddEditCrmEmployeeServicesRecruitementInviteResume(View):
	template = 'employee_website/employee_services/recruitement/add_edit_invite_resume.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
	
		if id is None:
			form = EmployeeServicesRecruitementInviteResumeAddForm()
		else:
			data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
			form = EmployeeServicesRecruitementInviteResumeUpdateForm(instance=data)
		context = {
			'form': form,
			
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		if id is None:
			form = EmployeeServicesRecruitementInviteResumeAddForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
				return redirect('crm_website_employeeservices_recruitement_inviteresume_add1')
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
				return redirect('crm_website_employeeservices_recruitement_inviteresume_add1')
		else:
			data = get_object_or_404(EmployeeServicesRecruitementInviteResume,  pk=id)
			form = EmployeeServicesRecruitementInviteResumeUpdateForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_inviteresume_list')

###
def AddUpdateEmployeeServicesRecruitementResumeView(request,id=None):
	form =AddUpdateEmployeeServicesRecruitementResume()
	if request.method=="POST":
		form = AddUpdateEmployeeServicesRecruitementResume(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			return redirect('crm_website_employeeservices_recruitement_inviteresume_list')
	return render(request,'employee_website/employee_services/recruitement/add_edit_invite_resume.html',{'form':form})

###############

class AddEditCrmEmployeeServicesRecruitementResume(View):
	template = 'employee_website/employee_services/recruitement/add_edit_invite_resume.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		#import pdb
		#pdb.set_trace()
		if not request.user.is_authenticated:
			return redirect('index')

		if id is None:
			form = EmployeeServicesRecruitementesumeAddForm1()
		else:
			data = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
			form = EmployeeServicesRecruitementInviteResumeUpdateForm(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		#import pdb
		#pdb.set_trace()
		
		if id is None:
			form = EmployeeServicesRecruitementesumeAddForm1(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				EmployeeServicesRecruitementRecommended.objects.update(updated_resume=1)
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
				return redirect('crm_website_employeeservices_recruitement_inviteresume_list')

			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")

		else:
			data = get_object_or_404(EmployeeServicesRecruitementInviteResume,  pk=id)
			form = EmployeeServicesRecruitementInviteResumeUpdateForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")


################

class EmployeeServicesRecruitementInviteResumeDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id = id).update(updated_resume=0,publish_status='Publish')
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_inviteresume_list')






				#################################psychometrictest###############################################

class EmployeeServicesRecruitementPsychometricTestList(View):
	template = 'employee_website/employee_services/recruitement/psychometrictest_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 1).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(psyco_test=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class AddEditCrmEmployeeServicesRecruitementPsychometricTest(View):
	template = 'employee_website/employee_services/recruitement/add_edit_psychometrictest.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(shortlist_resume='Accepted',allow_psyco='pending',psyco_test=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)













class EmployeeServicesRecruitementAllowedPsychometricTest(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(allow_psyco='Allow',psyco_test=1)

		return redirect('crm_website_employeeservices_recruitement_psychometrictest_list')



class EmployeeServicesRecruitementWaivePsychometricTest(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(update_test=1,psyco_test=1,allow_psyco='Waive')

		return redirect('crm_website_employeeservices_recruitement_psychometrictest_list')



class EmployeeServicesRecruitementPsychometricTestDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id = id).update(psyco_test=0,allow_psyco='pending')
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_psychometrictest_list')



def EditEmployeeServicesRecruitementPsycometricEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementPsychometricTestEdit(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_psychometrictest_list')
    else:
        form = EmployeeServicesRecruitementPsychometricTestEdit(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/modify_hr_requirement.html', {'form': form})



######################################## UPDATE TEST RESULT #######################################################

class EmployeeServicesRecruitementUpdateTestResultList(View):
	template = 'employee_website/employee_services/recruitement/update_result_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 1).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(update_test=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class AddEditCrmEmployeeServicesRecruitementUpdateTestResult(View):
	template = 'employee_website/employee_services/recruitement/update_result.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(allow_psyco='Allow',update_test=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

	
	



def EmployeeServicesRecruitementUpdateTestResult(request, id):


                	
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate = data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.test_score_awarded=request.POST.get('test_score_awarded')
		form.test_analysis=request.POST.get('test_analysis')
		form.test_date=request.POST.get('test_date')
		form.test_type=request.POST.get('test_type')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(publish_status='Approved',is_approve='Yes',is_filled=1,is_recommended=True,updated_resume=1,update_test=1)

		return redirect('crm_website_employeeservices_recruitement_update_test_result_list')
	else:
		form = EmployeeServicesRecruitementInviteResumeUpdateForm1(instance=company)
	#form.save()
		context= {
        		'form': form
    			}

	return render(request,'employee_website/employee_services/recruitement/add_edit_update_result.html',context)









class EmployeeServicesRecruitementUpdateTestResultDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id = id).update(update_test=0)
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_update_test_result_list')

def EditEmployeeServicesRecruitementUpdateTestResultEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementInviteResumeUpdateForm1(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_update_test_result_list')
    else:
        form = EmployeeServicesRecruitementInviteResumeUpdateForm1(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_update_test_result.html', {'form': form})


##################################################################################################################

################################### Schedule Interview ################################################################
class EmployeeServicesRecruitementScheduleInterviewList(View):
	template = 'employee_website/employee_services/recruitement/schedule_interview_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 1).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(schedule_status=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)
class AddEditCrmEmployeeServicesRecruitementScheduleInterview(View):
	template = 'employee_website/employee_services/recruitement/schedule_interview.html'
	pagesize=10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(update_test=1,schedule_status=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

	


def EmployeeServicesRecruitementScheduleInterviewUpdate(request,id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate = data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.person_phoneno=request.POST.get('person_phoneno')
		form.person_emailid=request.POST.get('person_emailid')
		form.person_name=request.POST.get('person_name')
		form.mode_of_interview=request.POST.get('mode_of_interview')
		form.place_of_interview=request.POST.get('place_of_interview')
		form.date_interview=request.POST.get('date_interview')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(publish_status='Approved',is_approve='Yes',is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1)

		return redirect('crm_website_employeeservices_recruitement_schedule_interview_list')
	else:
		form = EmployeeServicesRecruitementCandidatesShortlistedUpdateForm(instance=company)
	#form.save()
		context= {
        		'form': form
    			}

	return render(request,'employee_website/employee_services/recruitement/add_edit_schedule_interview.html',context)





class EmployeeServicesRecruitementScheduleInterviewDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(id = id).update(schedule_status=0)
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_schedule_interview_list')


def EditEmployeeServicesRecruitementScheduleInterviewEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementCandidatesShortlistedUpdateForm(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_schedule_interview_list')
    else:
        form = EmployeeServicesRecruitementCandidatesShortlistedUpdateForm(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/schedule_interview_edit.html', {'form': form})




#			#########################Shortlist Resume ################################
# 6
class EmployeeServicesRecruitementResumeShortlistedList(View):
	template = 'employee_website/employee_services/recruitement/resume_shortlisted_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(shortlist_resume_status=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeServicesRecruitementAllShortlistedResumeList(View):
	template = 'employee_website/employee_services/recruitement/resume_shortlist.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(updated_resume=1,shortlist_resume='pending',shortlist_resume_status=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementAcceptedResume(View):

	def get(self,request,id):

		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(shortlist_resume='Accepted',shortlist_resume_status=1)

		return redirect('crm_website_employeeservices_recruitement_shortlistedresume_list')


class EployeeServiceRecruitementRejectedResume(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(shortlist_resume='Rejected',shortlist_resume_status=1)
		return redirect('crm_website_employeeservices_recruitement_shortlistedresume_list')

class EmployeeServiceRecruitementRejectedBlackList(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(shortlist_resume='Blacklisted',shortlist_resume_status=1)
		return redirect('crm_website_employeeservices_recruitement_shortlistedresume_list')



class EmployeeServicesRecruitementRecipetResumeDelete(View):
	def get(request,self,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(shortlist_resume_status=0,updated_resume=1,shortlist_resume='pending')
		#messages.add_message(request, messages.ERROR, "Data deleted Successfully.")
		return redirect("crm_website_employeeservices_recruitement_shortlistedresume_list")



def EditEmployeeServicesRecruitementShortlistresumeEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementShortlistResumeModify(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_shortlistedresume_list')
    else:
        form = EmployeeServicesRecruitementShortlistResumeModify(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/modify_hr_requirement.html', {'form': form})










class AddEditCrmEmployeeServicesRecruitementCandidatesShortlisted(View):
	template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementCandidatesShortlistedUpdateForm(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementCandidatesShortlistedUpdateForm(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_candidateshortlisted_list')





####################################### offer formalities #################################################
class EmployeeServicesRecruitementOfferStatusList(View):
	template = 'employee_website/employee_services/recruitement/offer_status_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(offer_formalities_action=1).order_by('-id')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementAllOfferStatusList(View):
	template = 'employee_website/employee_services/recruitement/edit_offer_formalities.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(upload_document_status=1,offer_formalities_action=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


def employeservicesrecruitementeditoffterformalities(request,id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate=data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.document_type_1=data[0].document_type_1
		form.document_name_1=data[0].document_name_1
		form.document_submission=data[0].document_submission
		form.type_of_verification_1=data[0].type_of_verification_1
		form.verification_template_1=data[0].verification_template_1
		form.referencename_1=request.POST.get('referencename_1')
		form.referencerelationship_1=request.POST.get('referencerelationship_1')
		form.referencecontact_number_1=request.POST.get('referencecontact_number_1')
		form.referenceemail_id_1=request.POST.get('referenceemail_id_1')
		form.occupation=request.POST.get('occupation')
		form.employer_name=request.POST.get('employer_name')
		form.employercontact_person=request.POST.get('employercontact_person')
		form.employer_emailid=request.POST.get('employer_emailid')
		form.employeer_phno=request.POST.get('employeer_phno')
		form.address=request.POST.get('address')
		form.type_of_address=request.POST.get('type_of_address')
		form.staying_since=request.POST.get('staying_since')
		form.proof_attach=request.POST.get('proof_attach')
		form.test_name=request.POST.get('test_name')
		form.referred_to_hospital=request.POST.get('referred_to_hospital')
		form.save()
		#EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(publish_status='Approved',is_approve='Yes',is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1)
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(offer_formalities_action=1)
		return redirect('crm_website_employeeservices_recruitement_offer_list')
	else:
		form = EmployeeservicesRecruitementofferstatus(instance=company)
	#form.save()
		context= {
        		'form': form
    			}

	return render(request,'employee_website/employee_services/recruitement/add_edit_offer_formalities.html',context)


class EmployeeServicesrecuitementOfferDelete(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(upload_document_status=0)
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_recruitement_offer_list')

class EmployeeServicesrecuitementOfferformalitiesReject(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(upload_document_status=0)
		return redirect('crm_website_employeeservices_recruitement_offer_edit')


def EditEmployeeServicesRecruitementOfferFormalitiesEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesRecruitementofferformalitiesedit(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_offer_list')
    else:
        form = EmployeeServicesRecruitementofferformalitiesedit(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/modify_hr_requirement.html', {'form': form})


############################################ issue offer letter ##########################################################33
class EmployeeServicesRecruitementOfIssueOfferLetterList(View):
	template = 'employee_website/employee_services/recruitement/issue_offer_letter.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(issue_offer_status=1).order_by('-id')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitementOfIssueOfferLetterListedit(View):
	template = 'employee_website/employee_services/recruitement/offer_letter.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')      
		# get_report = EmployeeServicesRecruitementInviteResume.objects.filter(status = 2).order_by('-id')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(offer_formalities_action=1,issue_offer_status=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)



def employeeservicesissueofferleteredit(request,id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate=data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.grade=request.POST.get('grade')
		form.offer_contact_person=request.POST.get('offer_contact')
		form.valid_upto=request.POST.get('valid_upto')
		form.gross_salary=request.POST.get('gross_salary')
		form.salary_structut_salary_code_1_id=request.POST.get('salary_structut_salary_code_1')
		form.salary_structut_salary_name_1=request.POST.get('salary_structut_salary_name_1')
		form.salary_structut_amount_offered_1=request.POST.get('salary_structut_amount_offered_1')
		form.salary_structut_taxability_1=request.POST.get('salary_structut_taxability_1')
		form.salary_structut_salary_frequency_1=request.POST.get('salary_structut_salary_frequency_1')
		form.perquisitec_name_1=request.POST.get('perquisitec_name_1')
		form.perquisite_frequency_1=request.POST.get('perquisite_frequency_1')
		form.perquisite_amount_1=request.POST.get('perquisite_amount_1')
		form.deduction_name=request.POST.get('deduction_name')
		form.deduction_frequancy=request.POST.get('deduction_frequancy')
		form.deduction_ammount=request.POST.get('deduction_ammount')
		form.perquisite_taxability=request.POST.get('perquisite_taxability')
		form.perquisite_CTC=request.POST.get('perquisite_CTC')
		form.deduction_CTC=request.POST.get('deduction_CTC')
		form.perquisite_type=request.POST.get('perquisite_type')
		form.deduction_type=request.POST.get('deduction_type')
		form.save()

		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(issue_offer_status=1)

		return redirect('crm_website_employeeservices_recruitement_issue_offer_letter_list')

	else:
		form=EmployeeservicesRecruitementissueofferletter(instance=company)
		context={
		'form':form
		}
		return render (request,'employee_website/employee_services/recruitement/offer_letter_form.html',context)

class EmployeeServicesissueofferletterdelete(View):
	def get(request,self, id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(issue_offer_status=0)
		return redirect('crm_website_employeeservices_recruitement_issue_offer_letter_list')


def EditEmployeeServicesRecruitementissueOfferFormalitiesEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeservicesRecruitementissueofferletter(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_issue_offer_letter_list')
    else:
        form = EmployeeservicesRecruitementissueofferletter(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_offer_letter.html', {'form': form})




############################################## offer Approval ###################################################
class EmployeeServicesRecruitementOfOfferApprovalList(View):
	template = 'employee_website/employee_services/recruitement/offer_approval.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(offer_approval=1).order_by('-id')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeServiceRecruitementAllOfferApprovalList(View):
	template = 'employee_website/employee_services/recruitement/offer_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(issue_offer_status=1,offer_approval=0).order_by('-id')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)



class EmployeeServicesRecruitementApproveofferletter(View):
	pagesize = 10
	def get(self, request,id):
		
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(issue_offer_action='Approved',offer_approval=1)
		# report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		# context = {
		# 	'responselistquery': report_paginate
		# }
		return redirect('crm_website_employeeservices_recruitement_offer_approval_list')


class EmployeeServicesRecruitementRejectofferletter(View):
	pagesize = 10
	def get(self, request,id):
		
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(issue_offer_action='Rejected',offer_approval=0,issue_offer_status=0,status='Rejected')
		# report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		# context = {
		# 	'responselistquery': report_paginate
		# }
		return redirect('crm_website_employeeservices_recruitement_offer_approval_list')

class EmployeeServicesRecruitementPutonHoldofferletter(View):
	pagesize = 10
	def get(self, request,id):
		
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(issue_offer_action='Put On Hold',offer_approval=0,issue_offer_status=0,status='Put on Hold')
		# report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		# context = {
		# 	'responselistquery': report_paginate
		# }
		return redirect('crm_website_employeeservices_recruitement_offer_approval_list')



class EmployeeServicesRecruitementDeleteofferletter(View):
	pagesize=10
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(offer_approval=0)
		return redirect('crm_website_employeeservices_recruitement_offer_approval_list')



#################################################################################################################


	########################################### Offer Status ##################################################################################

class EmployeeServicesRecruitementOfferStatus2(View):
	template = 'employee_website/employee_services/recruitement/offer_status.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(offer_approval=1).order_by('-id')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class EmployeeServicesRecruitmentApproveStatus(View):
	pagesize=10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(acceptance_status='Accepted',offer_current_status='Joined')

		get_report = EmployeeServicesRecruitementRecommended.objects.filter(issue_offer_action='Approve')
		
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return redirect('crm_website_employeeservices_recruitement_offer_status')





###


	


####
		####################################Document Request ##############################################


class EmployeeServicesRecruitementDocumentRequestList(View):
	template = 'employee_website/employee_services/recruitement/document_request_list.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		# import pdb
		# pdb.set_trace()
		# import pdb
		# pdb.set_trace()
		if not request.user.is_authenticated:
			return redirect('index')

		get_report = EmployeeServicesRecruitementRecommended.objects.filter(document_status=1)
		# get_report1=EmployeeServicesRecruitementverificationtemplateUploads.objects.filter(document_status=1)
		context = {
			'responselistquery': get_report,
			'responselistquery1':get_report,
			# 'responselistquery1':get_report1
		}
		return render(request, self.template, context)

		
class EmployeeServicesRecruitementDocumentRequestadd(View):
	template = 'employee_website/employee_services/recruitement/document_add_edit.html'
	pagesize=10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):

		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(interview_result_status='Recommended',document_status=0)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)

		context = {
			'responselistquery': report_paginate,
			'get_id':id
		}
		return render(request, self.template, context)

# class EmployeeServiceRecruitemetCandidatedocumentrequest(View):
# 	template = 'employee_website/employee_services/recruitement/document_list.html'
	
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id=id):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		context = {
# 			'form1': EmployeeservicesRecruitementDocumentRequestform(),
# 			# 'form2':Employeeservicesrecruitemetnverificationform(),
# 			# 'id':id
# 		}
# 		return render(request, self.template, context)

# 	def post(self, request, id=id ):
# 		import pdb
# 		pdb.set_trace()
# 		#data = get_object_or_404(EmployeeServicesRecruitementDocumentUploads, pk=id)
# 		form = EmployeeservicesRecruitementDocumentRequestform(request.POST, request.FILES)
# 		EmployeeServicesRecruitementDocumentUploads.objects.filter(id=id).update(document_status=1)

# 		if form.is_valid():
# 			data = form.save()
# 			data.user_id = request.user.id

# 			data.save()
# 			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
# 		return redirect('crm_website_employeeservices_document_request_list')
# 		# import pdb
# 		# pdb.set_trace()
# 		# kra_update_id = [int(p.split('_')[2]) for p in request.POST if 'document_type_' in p]
# 		# kra_update_id.sort()
# 		# for cer in kra_update_id:
# 		# 	kra_struct = EmployeeServicesRecruitementDocumentUploads()
# 		# 	kra_struct.document_type_1= request.POST.get('document_type_' + str(cer)).strip()
# 		# 	kra_struct.document_name_1 = request.POST.get('document_name_' + str(cer)).strip()
# 		# 	kra_struct.required_by_1 = request.POST.get('required_by_'+ str(cer)).strip()
# 		# 	# kra_struct.verification_template_1= request.POST.get('verification_template_' + str(cer)).strip()
# 		# 	# kra_struct.type_of_verification_1 = request.POST.get('type_of_verification_' + str(cer)).strip()
# 		# 	kra_struct.ref_id_id=id
# 		# 	kra_struct.save()

# 		# EmployeeServicesRecruitementDocumentUploads.objects.filter(ref_id_id=id).update(document_status=1)

# 		# verification_id = [int(p.split('_')[2]) for p in request.POST if 'verification_template_' in p]
# 		# verification_id.sort()
# 		# for cer in verification_id:
# 		# 	verf_struct = EmployeeServicesRecruitementDocumentUploads()
# 		# 	verf_struct.verification_template_1= request.POST.get('verification_template_' + str(cer)).strip()
# 		# 	verf_struct.type_of_verification_1 = request.POST.get('type_of_verification_' + str(cer)).strip()
# 		# 	verf_struct.ref_id_id=id
# 		# 	verf_struct.save()
# 		# EmployeeServicesRecruitementDocumentUploads.objects.update(document_status=1)
# 		# messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
# 		# return redirect('crm_website_employeeservices_document_request_list')





def EmployeeServiceRecruitemetCandidatedocumentrequest(request,id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate=data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.document_type_1=request.POST.get('document_type_1')
		form.document_name_1=request.POST.get('document_name_1')
		form.required_by_1=request.POST.get('required_by_1')
		form.type_of_verification_1=request.POST.get('type_of_verification_1')
		form.verification_template_1=request.POST.get('verification_template_1')
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(document_status=1,interview_approvel='True')
		return redirect('crm_website_employeeservices_document_request_list')
	else:
	#form.save()
		context= {
        		'form1': EmployeeservicesRecruitementDocumentRequestform(instance=company),
        		'form2':Employeeservicesrecruitemetnverificationform(instance=company),
    			}

	return render(request,'employee_website/employee_services/recruitement/document_list.html',context)


# AJAX for documents save

class Document_Upload(View):
    def post(self, request):

        print("--------SELF--PAN-------",request.POST)
        getinputid = [str(p.split('_')[2]) for p in request.POST if 'document_type_' in p]
        getinputid.sort()


        ServicesHtml = ''
        if request.is_ajax:
            for cer in getinputid:
                # import pdb
                # pdb.set_trace()

                save_data = EmployeeServicesRecruitementDocumentUploads()

                save_data.document_type_1 = request.POST.get('document_type_' + str(cer))
                save_data.document_name_1 = request.POST.get('document_name_' + str(cer))
                save_data.required_by_1 =request.POST.get('required_by_' +str(cer))
                save_data.ref_id_id = request.POST.get('main_app_name')

                save_data.save()
        return JsonResponse({'data':1})

class Verification_upload(View):
	def post(self,request):

		print("------verification-----",request.POST)
		getinputid = [str(p.split('_')[2]) for p in request.POST if 'verification_template_' in p]
		getinputid.sort()


		ServicesHtml = ''
		if request.is_ajax:

			for cer in getinputid:
				save_data = EmployeeServicesRecruitementRecommended()
				
				save_data.verification_template_1=request.POST.get('verification_template_'+str(cer))
				save_data.type_of_verification_1=request.POST.get('type_of_verification_1'+str(cer))
        		
				save_data.save()
		return JsonResponse({'data':1})


class EmployeeServicesrecruitementDocumentRequestDelete(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(document_status=0)
		return redirect('crm_website_employeeservices_document_request_list')



def EditEmployeeServicesRecruitementDocumentRequestEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeservicesRecruitementDocumentRequestform(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_shortlistedresume_list')
    else:
        form = EmployeeservicesRecruitementDocumentRequestform(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/edit_document_request.html', {'form': form})


############################################################################

######################################### Update Documents ################################################################################
class EmployeeServicesRecruitementUpdateDocumentsList(View):
	template = 'employee_website/employee_services/recruitement/update_document_list.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(upload_document_status=1).order_by('-id')
		context = {
			'responselistquery': get_report,
		}
		return render(request, self.template, context)
class EmployeeServicesRecruitementUpdateDocumentsadd(View):
	pagesize=10
	template = 'employee_website/employee_services/recruitement/edit_update_document.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(document_status=1,upload_document_status=0)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)

		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

def employeeservicedocumentrequest(request,id):
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.name_of_candidate=data[0].name_of_candidate
		form.email_id=data[0].email_id
		form.phone_no=data[0].phone_no
		form.document_type_1=data[0].document_type_1
		form.document_name_1=data[0].document_name_1
		form.required_by_1=data[0].required_by_1
		form.type_of_verification_1=data[0].type_of_verification_1
		form.verification_template_1=data[0].verification_template_1
		form.document_submission=request.FILES['document_submission']
		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(upload_document_status=1,document_receivied='Received')

		return redirect('crm_website_employeeservices_update_documents_list')
	else:
		form = EmployeeeservicesRecruitementdocumentupload(instance=company)
		context={
		'form':form
		}
		return render(request,'employee_website/employee_services/recruitement/upload_document.html',context)


class EmployeeServicesdocumentrequestdelete(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(upload_document_status=0,document_receivied='pending')
		messages.add_message(request,messages.SUCCESS,'Data Deleted Successfully.')
		return redirect('crm_website_employeeservices_update_documents_list')

def EditEmployeeServicesRecruitementUpdateDocumentEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeeservicesRecruitementdocumentupload(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_update_documents_list')
    else:
        form = EmployeeeservicesRecruitementdocumentupload(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/upload_document.html', {'form': form})



###########################################################################################################################################

class AddEditCrmEmployeeServicesRecruitementCandidatesOfferStatus(View):
	template = 'employee_website/employee_services/recruitement/update_candidates_joined.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementInterViewStatusShortlistedCandidateForm1(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementInterViewStatusShortlistedCandidateForm1(request.POST, request.FILES, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_offer_status_list')


class AddEditCrmEmployeeServicesRecruitementCandidatesOfferUpdateStatus(View):
	template = 'employee_website/employee_services/recruitement/update_candidates_joined.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementOfferStatusUpdateForm(instance=data)
		context = {
			'form': form,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		form = EmployeeServicesRecruitementOfferStatusUpdateForm(request.POST, request.FILES, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_offer_status_list')


			######################### Vacancy Status ###############################3


class EmployeeServicesRecruitementVacancyStatusList(View):
	template = 'employee_website/employee_services/recruitement/vacancy_status_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.all().order_by('-id')
	
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

def EditEmployeeServicesRecruitementVacancyStatusEdit(request, id):

    manageproduct = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)
    if request.method == "POST":
        form =EmployeeServicesVacancyStatusedit(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_website_employeeservices_recruitement_vacancystatus_list')
    else:
        form = EmployeeServicesVacancyStatusedit(instance=manageproduct)
    return render(request, 'employee_website/employee_services/recruitement/vacancy_edit.html', {'form': form})


				################ Interview Result #################


class EmployeeServicesRecruitementCandidatesInterViewStatusList(View):
	template = 'employee_website/employee_services/recruitement/interview_status.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(interview_approvel=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class AddEditCrmEmployeeServicesInterViewStatus(View):
	template = 'employee_website/employee_services/recruitement/add_edit_interview_status.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		# form = EmployeeServicesRecruitementInterViewStatusForm(instance=data)
		short_listed_candidated = EmployeeServicesRecruitementInterViewStatusShortlistedCandidateForm(instance=data)
		context = {
			# 'form': form,
			'short_listed_candidated': short_listed_candidated,
			'data': data
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		data = get_object_or_404(EmployeeServicesRecruitementInviteResume, pk=id)
		# form = EmployeeServicesRecruitementInterViewStatusForm(request.POST, instance = data)
		form = EmployeeServicesRecruitementInterViewStatusShortlistedCandidateForm(request.POST, instance = data)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			# if request.POST['status'] == '3':
			# 	if form1.is_valid():
			# 		form1.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')


class EmployeeServicesRecruitementCandidateShortlistedList(View):

	template = 'employee_website/employee_services/recruitement/candidate_short_list.html'
	pagesize = 15
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(schedule_status=1,interview_approvel=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


def EmployeeServiceRecruitemetCandidateUpdate(request,id):
	# import pdb
	# pdb.set_trace()
	pagesize=20
	company = get_object_or_404(EmployeeServicesRecruitementRecommended, pk=id)	
	if request.method == "POST":
		

		data = EmployeeServicesRecruitementRecommended.objects.filter(id=id)
		if data.exists():
			form = EmployeeServicesRecruitementRecommended.objects.get(id=id)

		else:
			form=EmployeeServicesRecruitementRecommended()
		form.location_id=data[0].location_id
		form.department_id=data[0].department_id
		form.designation_id=data[0].designation_id
		form.mode_of_interview=request.POST.get('mode_of_interview')
		form.place_of_interview=request.POST.get('place_of_interview')
		form.date_interview=request.POST.get('date_interview')
		form.individual_score=request.POST.get('individual_score')
		form.interview_score=request.POST.get('interview_score')
		form.comment=request.POST.get('comment')
		form.contact_person=request.POST.get('contact_person')
		form.reason_for_rescheduling=request.POST.get('reason_for_rescheduling')
		form.timing_of_interview=request.POST.get('timing_of_interview')
		form.interview_of_status=request.POST.get('interview_of_status')
		form.interview_result_status=request.POST.get('interview_result_status')
		# form.interview_approvel=request.POST.get('interview_approvel')

		form.save()
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(is_publish=1,approve_status=1,is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1,interview_approvel=1)

		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')
	else:
		form = EmployeeServicesRecruitementInterViewStatusForm(instance=company)
	#form.save()
		context= {
        		'form': form
    			}

	return render(request,'employee_website/employee_services/recruitement/add_edit_interview_update.html',context)


class EmployeeServiceRecruitemetCandidateDelete(View):
	def get(self,request,id):
		EmployeeServicesRecruitementRecommended.objects.filter(id=id).update(interview_approvel=0)
		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')






# class EmployeeServicesRecruitementInterviewResultRecommended(View):
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
# 		get_report = EmployeeServicesRecruitementRecommended.objects.update(is_publish=1,approve_status=1,is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1,interview_result_status='Recommended',interview_approvel=1,interview_of_status='Attended')
# 		#EmployeeServicesRecruitementCreateRequirement.objects.update(is_filled=1)
		
# 		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')


# class EmployeeServicesRecruitementInterviewResultRejected(View):
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
		
# 		get_report = EmployeeServicesRecruitementRecommended.objects.update(is_publish=1,approve_status=1,is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1,interview_result_status='Rejected',interview_approvel=1,interview_of_status='Attended')
		
# 		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')


# class EmployeeServicesRecruitementInterviewResultputonhold(View):
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		# get_report = EmployeeServicesRecruitementCreateRequirement.objects.filter(~Q(approval_level_id = 5)).order_by('-id')
		
# 		get_report = EmployeeServicesRecruitementRecommended.objects.update(is_publish=1,approve_status=1,is_filled=1,is_recommended=True,updated_resume=1,update_test=1,schedule_status=1,interview_result_status='Put On Hold',interview_approvel=1,interview_of_status='Attended')
# 		#EmployeeServicesRecruitementCreateRequirement.objects.update(is_filled=1)
		
# 		return redirect('crm_website_employeeservices_recruitement_interviewstatus_list')



# 7
class EmployeeServicesEmployeeRegistrationUpdateRegistrationsList(View):
	template = 'employee_website/employee_services/employee_registration/update_registrations_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
			#
			####
		get_report = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

##1
##2

class EmployeeServicesEmployeeOfferLatter(View):
	template = 'employee_website/employee_services/employee_registration/employee_offer_latter_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
			#
			####
		get_report = EmployeeServicesRecruitementRecommended.objects.filter(acceptance_status='Accepted').order_by('-id')
	
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class AddEmployeeServicesEmployeeRegistrationUpdateRegistrations(View):
	template = 'employee_website/employee_services/employee_registration/add_edit_update_registrations.html'
	template1 = 'employee_website/employee_services/employee_registration/employee_registertion_verification_report.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'personal_details': EmployeeEmployeeRegistrationUpdateRegistrationPersonalDetailsmodelForm,
			'emergency_contact_details':EmployeeServicesREgistrationEmergencyContactDetailsmodelform,			
			# 'family_detail_mother': EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetailsmodelMotherForm,
			# 'family_detail_father': EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetailsmodelFatherForm,
			# 'family_detail_spouse': EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetailsmodelSpouseForm,
			# 'family_detail_children': EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetailsmodelChildrenForm,
			'other_family_relationship': EmployeeEmployeeRegistrationUpdateRegistrationFamilityOtherRelationshipForm,
			'medical_history': EmployeeEmployeeRegistrationUpdateRegistrationMedicalHistorymodelForm,
			'correspondence_address': EmployeeEmployeeRegistrationCorrespondenceAddressForm,
			'permanent_address': EmployeeEmployeeRegistrationPermanentAddressForm,
			'joining_detail': EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetailsmodelForm,
			'qualification': EmployeeEmployeeRegistrationUpdateEducationalQualificationmodelForm,
			'professional_journey': EmployeeEmployeeRegistrationUpdateProfessionalJourneymodelForm,
			'salary_structutre': EmployeeEmployeeRegistrationUpdateSalaryStructutremodelForm,
			'bank_detail': EmployeeEmployeeRegistrationUpdateBankDetailsmodelForm,
			'verification_report': EmployeeEmployeeRegistrationVerificationReportmodelForm,
			'deduction_perquisites': EmployeeEmployeeRegistrationDeductionAndPerquisitesForm,
			'deduction': EmployeeEmployeeRegistrationDeductionForm,
			'asset_allocated': EmployeeEmployeeAssetAllocatedForm,
			'access_control': EmployeeEmployeeAccessControlsForm,
			'references': EmployeeEmployeeRegistrationReferencesmodelForm,
			'documents': CrmEmployeeEmployeeRegistrationDocumentsmodelForm
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		if request.POST['one_form'] == "one_form":
			if User.objects.filter(email = request.POST['email']):
				messages.add_message(request, messages.WARNING, "Email already exists.")
				return redirect('crm_website_employeeservices_employeeregistration_updateregistrations_add')
			
			save_user = User()
			save_user.email = request.POST['email']
			save_user.username = request.POST['email']
			save_user.mobile_no = request.POST['mobile_no']
			save_user.name = request.POST['first_name']
			save_user.department_id = request.POST['joining_department']
			save_user.designation_id = request.POST['joining_designation']
			save_user.responsibilities_id = request.POST['joining_responsibilities']
			save_user.user_role_id = request.POST['joining_role']
			save_user.reporting_to_id = request.POST['joining_reporting_to']
			save_user.is_sub_staff = True
			save_user.is_staff = False
			save_user.save()

			# data1 = EmployeeRegistrationUpdateRegistrationPersonalDetails()
			# data = request.user.head_office.hod_id
			# data1.employee_id = str(data)  + str(get_id).zfill(6)
			# data1.save()

			form = EmployeeEmployeeRegistrationUpdateRegistrationPersonalDetailsmodelForm(request.POST)
			if form.is_valid():
				import pdb
				pdb.set_trace()
				data = form.save()
				data.user_id = save_user.id
				get_id=data.id
				data.employee_created_by_id = request.user.id
				req=request.user.head_office.hod_id
				data.employee_id=str(req)+str(get_id).zfill(6)
				data.save()

			#company = get_object_or_404(EmployeeRegistrationCorrespondenceAddress, pk=id)	

			form2 = EmployeeEmployeeRegistrationCorrespondenceAddressForm(request.POST)
			if form2.is_valid():
				data = form2.save()
				data.user_id=save_user.id
				data.user_employee_id = get_id
				data.employee_created_by_id=request.user.id
				data.save()

			form3 = EmployeeEmployeeRegistrationPermanentAddressForm(request.POST)
			if form3.is_valid():
				data = form3.save()
				data.user_id=save_user.id
				data.user_employee_id = get_id
				data.employee_created_by_id=request.user.id
				data.save()
			form=EmployeeServicesREgistrationEmergencyContactDetailsmodelform(request.POST)
			if form.is_valid():
				data=form.save()
				data.user_id=save_user.id
				data.user_employee_id=get_id
				data.employee_created_by_id=request.user.id
				data.save()
				#get_id=data.id
			# save_obj = EmployeeRegistrationUpdateRegistrationFamilityDetails()
			# if str(request.POST.get('mother_name'))  and str(request.POST.get('mother_dob')) and str(request.POST.get('mother_occupation')):
			# 	save_obj.mother_name = str(request.POST.get('mother_name'))
			# 	save_obj.mother_dob = str(request.POST.get('mother_dob'))
			# 	save_obj.mother_occupation = str(request.POST.get('mother_occupation'))
			# 	save_obj.mother_contact_number = str(request.POST.get('mother_contact_number'))
			# 	save_obj.user_employee_id= get_id
			# 	save_obj.save()
			# if str(request.POST.get('father_name'))  and str(request.POST.get('father_dob')) and str(request.POST.get('father_occupation')):
			# 	save_obj.father_name = str(request.POST.get('father_name'))
			# 	save_obj.father_dob = str(request.POST.get('father_dob'))
			# 	save_obj.father_occupation = str(request.POST.get('father_occupation'))
			# 	save_obj.father_contact_number = str(request.POST.get('father_contact_number'))
			# 	save_obj.user_employee_id= get_id
			# 	save_obj.save()
			# if str(request.POST.get('spouse_name'))  and str(request.POST.get('spouse_dob')) and str(request.POST.get('spouse_occupation')):
			# 	save_obj.spouse_name = str(request.POST.get('spouse_name'))
			# 	save_obj.spouse_dob = str(request.POST.get('spouse_dob'))
			# 	save_obj.spouse_occupation = str(request.POST.get('spouse_occupation'))
			# 	save_obj.spouse_contact_number = str(request.POST.get('spouse_contact_number'))
			# 	save_obj.user_employee_id= get_id
			# 	save_obj.save()
			# children_data = [int(p.split('_')[2]) for p in request.POST if 'children_name_' in p]
			# children_data.sort()
			# for cer in children_data:
			# 	children = EmployeeRegistrationUpdateRegistrationFamilityChildren()
			# 	children.children_name_1 = request.POST.get('children_name_' + str(cer)).strip()
			# 	children.children_dob_1 = request.POST.get('children_dob_' + str(cer)).strip()
			# 	children.children_occupation_1 = request.POST.get('children_occupation_' + str(cer)).strip()
			# 	children.children_contact_number_1 = request.POST.get('children_contact_number_' + str(cer)).strip()
			# 	children.user_employee_id = get_id
			# 	children.save()

			other_relation = [int(p.split('_')[2]) for p in request.POST if 'other_name_' in p]
			other_relation.sort()
			for cer in other_relation:
				other_rela = EmployeeRegistrationUpdateRegistrationFamiliyOtherDetails()
				other_rela.other_name_1 = request.POST.get('other_name_' + str(cer)).strip()
				other_rela.other_dob_1 = request.POST.get('other_dob_' + str(cer)).strip()
				other_rela.other_occupation_1 = request.POST.get('other_occupation_' + str(cer)).strip()
				other_rela.other_contact_number_1 = request.POST.get('other_contact_number_' + str(cer)).strip()
				other_rela.other_relationship_1 = request.POST.get('other_relationship_' + str(cer)).strip()
				other_rela.user_employee_id = get_id
				other_rela.save()


			#Save Medical History
			medical_history_id = [int(p.split('_')[2]) for p in request.POST if 'blood_group_' in p]
			medical_history_id.sort()
			for cer in medical_history_id:
				medical_history = EmployeeRegistrationUpdateRegistrationMedicalHistory()
				medical_history.blood_group_1 = request.POST.get('blood_group_' + str(cer)).strip()
				medical_history.type_of_illness_1 = request.POST.get('type_of_illness_' + str(cer)).strip()
				medical_history.result_1 = request.POST.get('result_' + str(cer)).strip()
				medical_history.user_employee_id = get_id
				medical_history.save()

			

			

			form4 = EmployeeEmployeeRegistrationDeductionForm(request.POST)
			if form4.is_valid():
				data = form4.save()
				data.user_employee_id = get_id
				data.save()

			joining_detail = EmployeeRegistrationUpdateRegistrationJoiningDetails()
			joining_detail.mode_of_sourcing_1=request.POST.get('mode_of_sourcing_1')
			joining_detail.type_of_job_id=request.POST.get('type_of_job')
			joining_detail.pay_roll_job_id=request.POST.get('pay_roll_job')
			joining_detail.joining_location_id= request.POST.get('joining_location')
			joining_detail.joining_date_of_joining = request.POST.get('joining_date_of_joining')
			joining_detail.joining_time= request.POST.get('joining_time')
			joining_detail.joining_grade_offered= request.POST.get('joining_grade_offered')
			joining_detail.joining_next_date_of_increment= request.POST.get('joining_next_date_of_increment')
			joining_detail.joining_department_id= request.POST.get('joining_department')
			joining_detail.joining_designation_id= request.POST.get('joining_designation')
			joining_detail.joining_responsibilities_id = request.POST.get('joining_responsibilities')
			joining_detail.joining_role_id = request.POST.get('joining_role')
			joining_detail.joining_reporting_to_id = request.POST.get('joining_reporting_to')
			joining_detail.joining_probation_period = request.POST.get('joining_probation_period')
			joining_detail.contract_valid_up_to = request.POST.get('contract_valid_up_to')
			joining_detail.user_employee_id = get_id
			joining_detail.save()

			# # Save Joining Detail History
			# joining_history = EmployeeRegistrationUpdateRegistrationJoiningDetailsHistory()
			# joining_history.new_designation_id = request.POST.get('joining_designation')
			# joining_history.new_department_id = request.POST.get('joining_department')
			# joining_history.new_reporting_id = request.POST.get('joining_reporting_to')
			# joining_history.new_responsibilities_id = request.POST.get('joining_responsibilities')
			# joining_history.new_location_id =  request.POST.get('joining_location')
			# joining_history.joining_role_id = request.POST.get('joining_role')
			# joining_history.user_employee_id = get_id
			# joining_history.save()

			qualification_id = [int(p.split('_')[3]) for p in request.POST if 'educational_qualificationcourse_name_' in p]
			qualification_id.sort()
			for cer in qualification_id:
				qualification = EmployeeRegistrationUpdateEducationalQualification()
				qualification.educational_qualificationcourse_name_1= request.POST.get('educational_qualificationcourse_name_' + str(cer)).strip()
				qualification.educational_qualificationstart_date_1 = request.POST.get('educational_qualificationstart_date_' + str(cer)).strip()
				#qualification.educational_qualificationend_date_1 = request.POST.get('educational_qualificationend_date_' + str(cer)).strip()
				qualification.educational_qualificationmarks_division_1 = request.POST.get('educational_qualificationmarks_division_' + str(cer)).strip()
				#qualification.educational_qualificationroll_number_1= request.POST.get('educational_qualificationroll_number_' + str(cer)).strip()
				qualification.educational_qualificationuniversity_institution_1= request.POST.get('educational_qualificationuniversity_institution_' + str(cer)).strip()
				qualification.user_employee_id = get_id
				qualification.save()

			professional_journey_id = [int(p.split('_')[2]) for p in request.POST if 'professional_journeycompany_' in p]
			professional_journey_id.sort()
			for cer in professional_journey_id:
				professional_journey = EmployeeRegistrationUpdateProfessionalJourney()
				professional_journey.professional_journeycompany_1= request.POST.get('professional_journeycompany_' + str(cer)).strip()
				professional_journey.professional_journeystart_date_1 = request.POST.get('professional_journeystart_date_' + str(cer)).strip()
				#professional_journey.professional_journeyend_date_1 = request.POST.get('professional_journeyend_date_' + str(cer)).strip()
				professional_journey.professional_journeylast_desgination_1_id = request.POST.get('professional_journeylast_desgination_' + str(cer)).strip()
				professional_journey.professional_journeynature_of_duties_1 = request.POST.get('professional_journeynature_of_duties_' + str(cer)).strip()
				professional_journey.professional_journeylast_drawn_dalary_1 = request.POST.get('professional_journeylast_drawn_dalary_' + str(cer)).strip()
				professional_journey.reason_for_leaving_1 = request.POST.get('reason_for_leaving_' + str(cer)).strip()
				professional_journey.user_employee_id = get_id
				professional_journey.save()


			salary_struct_id = [int(p.split('_')[4]) for p in request.POST if 'salary_structut_salary_code_' in p]
			salary_struct_id.sort()
			for cer in salary_struct_id:
				salary_struct = EmployeeRegistrationUpdateSalaryStructutre()
				salary_struct.salary_structut_salary_code_1_id = request.POST.get('salary_structut_salary_code_' + str(cer)).strip()
				salary_struct.salary_structut_salary_name_1 = request.POST.get('salary_structut_salary_name_' + str(cer)).strip()
				salary_struct.salary_structut_salary_frequency_1 = request.POST.get('salary_structut_salary_frequency_' + str(cer)).strip()
				salary_struct.salary_structut_amount_offered_1= request.POST.get('salary_structut_amount_offered_' + str(cer)).strip()
				salary_struct.salary_structut_percentage_value_flag_1= request.POST.get('salary_structut_percentage_value_flag_' + str(cer)).strip()
				salary_struct.salary_structut_taxability_1 = request.POST.get('salary_structut_taxability_' + str(cer))
				salary_struct.user_employee_id = get_id
				salary_struct.save()

			deduc = [int(p.split('_')[1]) for p in request.POST if 'appicablitity_' in p]
			deduc.sort()
			for cer in deduc:
				salary_struct = EmployeeRegistrationDeductionAndPerquisites()
				if str(request.POST.get('appicablitity_'+str(cer))) == "2":
					salary_struct.appicablitity_1  = str(request.POST.get('appicablitity_'+str(cer)))
					salary_struct.save()
				else:
					salary_struct.appicablitity_1  = str(request.POST.get('appicablitity_'+str(cer)))
					salary_struct.perquisitec_category_1  = str(request.POST.get('perquisitec_category_'+str(cer)))
					salary_struct.perquisitec_name_1  = str(request.POST.get('perquisitec_name_'+str(cer)))
					salary_struct.perquisite_frequency_1  = str(request.POST.get('perquisite_frequency_'+str(cer)))
					salary_struct.percentage_value_flag_1  = str(request.POST.get('percentage_value_flag_'+str(cer)))
					salary_struct.perquisite_amount_1  = str(request.POST.get('perquisite_amount_'+str(cer)))
					salary_struct.save()

			save_bank_detail = EmployeeRegistrationUpdateBankDetails()
			save_bank_detail.account_type = request.POST.get('account_type')
			save_bank_detail.bank_account_number = request.POST.get('bank_account_number')
			save_bank_detail.bank_name = request.POST.get('bank_name')
			save_bank_detail.branch = request.POST.get('branch')
			save_bank_detail.ifscc_code = request.POST.get('ifscc_code')
			save_bank_detail.micr = request.POST.get('micr')
			save_bank_detail.user_employee_id = get_id 
			save_bank_detail.save()

			reference_id = [int(p.split('_')[1]) for p in request.POST if 'referencename_' in p]
			reference_id.sort()
			for cer in reference_id:
				reference = EmployeeRegistrationReferences()
				reference.referencename_1= request.POST.get('referencename_' + str(cer)).strip()
				reference.referencerelationship_1 = request.POST.get('referencerelationship_' + str(cer)).strip()
				reference.referencecontact_number_1 = request.POST.get('referencecontact_number_' + str(cer)).strip()
				reference.referenceemail_id_1 = request.POST.get('referenceemail_id_' + str(cer)).strip()
				reference.referenceaddress_1= request.POST.get('referenceaddress_' + str(cer)).strip()
				reference.referenceknown_since_1= request.POST.get('referenceknown_since_' + str(cer)).strip()
				reference.user_employee_id = get_id
				reference.save()

			asset_allocated = [int(p.split('_')[2]) for p in request.POST if 'asset_code_' in p]
			asset_allocated.sort()
			for cer in asset_allocated:
				asset_alloca= EmployeeAssetAllocated()
				asset_alloca.asset_code_1= request.POST.get('asset_code_' + str(cer)).strip()
				asset_alloca.asset_serial_number_1 = request.POST.get('asset_serial_number_' + str(cer)).strip()
				asset_alloca.asset_name_1 = request.POST.get('asset_name_' + str(cer)).strip()
				asset_alloca.asset_condition_1 = request.POST.get('asset_condition_' + str(cer)).strip()
				asset_alloca.asset_location_1= request.POST.get('asset_location_' + str(cer)).strip()
				asset_alloca.user_employee_id = get_id
				asset_alloca.save()

			verification_report = [int(p.split('_')[2]) for p in request.POST if 'verification_agency_' in p]
			verification_report.sort()
			for cer in verification_report:
				verificationreport = EmployeeRegistrationVerificationReport()
				verificationreport.verification_agency = request.POST.get('verification_agency_' + str(cer))
				verificationreport.finding = request.POST.get('finding_' + str(cer))
				verificationreport.upload_report = request.FILES.get('upload_report_' + str(cer))
				verificationreport.user_employee_id = get_id
				verificationreport.save()
			document_id = [int(p.split('_')[3]) for p in request.POST if 'name_of_documents_' in p]
			document_id.sort()
			for cer in document_id:
				document = EmployeeRegistrationDocuments()
				document.name_of_documents_1 = request.POST.get('name_of_documents_' + str(cer)).strip()
				document.upload_1 = request.FILES.get('upload_' + str(cer))
				document.document_type_1=request.POST.get('document_type_' +str(cer)).strip()
				document.user_employee_id = get_id
				document.save()

			form4 = EmployeeEmployeeAccessControlsForm(request.POST)
			if form4.is_valid():
				data = form4.save()
				data.user_employee_id = get_id
				data.save()
				# import pdb
				# pdb.set_trace()
				# data1 = EmployeeRegistrationUpdateRegistrationPersonalDetails()
				# data = request.user.head_office.hod_id

				# data1.employee_id = str(data)  + str(get_id).zfill(6)
				# data1.save()
			messages.add_message(request, messages.SUCCESS, "Employee Created successfully.")
			return redirect('crm_website_employeeservices_offer_latter_list')


class AddEmployeeServicesEmployeeRegistrationVerficationReport(View):
	template = 'employee_website/employee_services/employee_registration/employee_registertion_verification_report.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'verification_report': EmployeeEmployeeRegistrationVerificationReportmodelForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return render(request, self.template1, context)
		verification_report = [int(p.split('_')[2]) for p in request.POST if 'verification_agency_' in p]
		verification_report.sort()
		for cer in verification_report:
			verificationreport = EmployeeRegistrationVerificationReport()
			verificationreport.verification_agency = request.POST.get('verification_agency_' + str(cer))
			verificationreport.finding = request.POST.get('finding_' + str(cer))
			verificationreport.upload_report = request.FILES.get('upload_report_' + str(cer))
			verificationreport.user_employee_id = id
			verificationreport.save()
		return redirect('crm_website_employeeservices_employeeregistration_document_add', id = id)


class AddEmployeeServicesEmployeeRegistrationDocument(View):
	template = 'employee_website/employee_services/employee_registration/employee_registered_document.html'
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'documents': CrmEmployeeEmployeeRegistrationDocumentsmodelForm
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return render(request, self.template1, context)
		document_id = [int(p.split('_')[3]) for p in request.POST if 'name_of_documents_' in p]
		document_id.sort()
		for cer in document_id:
			document = EmployeeRegistrationDocuments()
			document.name_of_documents_1 = request.POST.get('name_of_documents_' + str(cer)).strip()
			document.upload_1 = request.FILES.get('upload_' + str(cer))
			document.user_employee_id = id
			document.save()
		messages.add_message(request, messages.SUCCESS, "Employee Registeration Successfully.")
		return redirect('crm_website_employeeservices_employeeregistration_employee_list')


class EditEmployeeServicesEmployeeRegistrationUpdateRegistrations(View):
	template = 'employee_website/employee_services/employee_registration/edit_employee.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.get(id = id)
		context = {
			'personal_details': EmployeeRegistrationUpdateRegistrationPersonalDetailsmodelForm(instance=data),
			'family_detail_mother': EmployeeRegistrationUpdateRegistrationFamilityDetailsmodelMotherForm(instance = EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetails.objects.get(user_employee_id = data.id)),
			'family_detail_father': EmployeeRegistrationUpdateRegistrationFamilityDetailsmodelFatherForm(instance = EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetails.objects.get(user_employee_id = data.id)),
			'family_detail_spouse': EmployeeRegistrationUpdateRegistrationFamilityDetailsmodelSpouseForm(instance = EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetails.objects.get(user_employee_id = data.id)),
			'family_detail_children': EmployeeRegistrationUpdateRegistrationFamilityDetailsmodelChildrenForm(instance = EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetails.objects.get(user_employee_id = data.id)),
			'medical_history': EmployeeEmployeeRegistrationUpdateRegistrationMedicalHistory.objects.filter(user_employee_id = data.id),
			'joining_detail': EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetailsmodelForm(instance = EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(user_employee_id = data.id)),
			'qualification': EmployeeEmployeeRegistrationUpdateEducationalQualification.objects.filter(user_employee_id = data.id),
			'professional_journey': EmployeeEmployeeRegistrationUpdateProfessionalJourney.objects.filter(user_employee_id = data.id),
			'salary_structutre': EmployeeEmployeeRegistrationUpdateSalaryStructutre.objects.filter(user_employee_id = data.id),
			'bank_detail': EmployeeEmployeeRegistrationUpdateBankDetailsmodelForm(instance = EmployeeEmployeeRegistrationUpdateBankDetails.objects.get(user_employee_id = data.id)),
			'verification_report': EmployeeEmployeeRegistrationVerificationReportmodelForm(instance = EmployeeEmployeeRegistrationVerificationReport.objects.get(user_employee_id = data.id)),
			'references': EmployeeEmployeeRegistrationReferences.objects.filter(user_employee_id = data.id),
			'documents': EmployeeEmployeeRegistrationDocuments.objects.filter(user_employee_id = data.id),
			'deduction_perquisites': EmployeeEmployeeRegistrationDeductionAndPerquisitesForm(instance=EmployeeEmployeeRegistrationDeductionAndPerquisites.objects.get(user_employee_id = data.id)),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')

		EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.get(id = id).delete()
		personal_details = EmployeeRegistrationUpdateRegistrationPersonalDetailssmodel()
		personal_details.employee_id_id = request.POST.get('employee_id')
		personal_details.user_id = request.POST.get('user')
		personal_details.salute= request.POST.get('salute')
		personal_details.first_name= request.POST.get('first_name')
		personal_details.middle_name= request.POST.get('middle_name')
		personal_details.last_name= request.POST.get('last_name')
		personal_details.date_of_birth= request.POST.get('date_of_birth')
		personal_details.caste= request.POST.get('caste')
		personal_details.religion= request.POST.get('religion')
		personal_details.marital_status= request.POST.get('marital_status')
		personal_details.mobile_number= request.POST.get('mobile_number')
		personal_details.email_id= request.POST.get('email_id')
		personal_details.landline_number= request.POST.get('landline_number')
		personal_details.emergency_number= request.POST.get('emergency_number')
		personal_details.name= request.POST.get('name')
		personal_details.pan_card= request.POST.get('pan_card')
		personal_details.adhar_card= request.POST.get('adhar_card')
		personal_details.driving_license= request.POST.get('driving_license')
		personal_details.language_known= request.POST.get('language_known')
		personal_details.relationship= request.POST.get('relationship')
		personal_details.photo = request.FILES.get('photo')
		personal_details.user_id = request.user.id
		get_id = personal_details.save()
		save_obj = EmployeeEmployeeRegistrationUpdateRegistrationFamilityDetails()
		if str(request.POST.get('mother_name'))  and str(request.POST.get('mother_dob')) and str(request.POST.get('mother_occupation')):
			save_obj.mother_name = str(request.POST.get('mother_name'))
			save_obj.mother_dob = str(request.POST.get('mother_dob'))
			save_obj.mother_occupation = str(request.POST.get('mother_occupation'))
			save_obj.user_employee_id= personal_details.id
			save_obj.save()
		if str(request.POST.get('father_name'))  and str(request.POST.get('father_dob')) and str(request.POST.get('father_occupation')):
			save_obj.father_name = str(request.POST.get('father_name'))
			save_obj.father_dob = str(request.POST.get('father_dob'))
			save_obj.father_occupation = str(request.POST.get('father_occupation'))
			save_obj.user_employee_id= personal_details.id
			save_obj.save()
		if str(request.POST.get('spouse_name'))  and str(request.POST.get('spouse_dob')) and str(request.POST.get('spouse_occupation')):
			save_obj.spouse_name = str(request.POST.get('spouse_name'))
			save_obj.spouse_dob = str(request.POST.get('spouse_dob'))
			save_obj.spouse_occupation = str(request.POST.get('spouse_occupation'))
			save_obj.user_employee_id= personal_details.id
			save_obj.save()
		if str(request.POST.get('children_name'))  and str(request.POST.get('children_dob')) and str(request.POST.get('children_occupation')):
			save_obj.children_name = str(request.POST.get('children_name'))
			save_obj.children_dob = str(request.POST.get('children_dob'))
			save_obj.children_occupation = str(request.POST.get('children_occupation'))
			save_obj.user_employee_id= personal_details.id
			save_obj.save()

		joining_detail = EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetails()
		joining_detail.joining_location= request.POST.get('joining_location')
		joining_detail.joining_date_of_joining = request.POST.get('joining_date_of_joining')
		joining_detail.joining_time= request.POST.get('joining_time')
		joining_detail.joining_grade_offered= request.POST.get('joining_grade_offered')
		joining_detail.joining_next_date_of_increment= request.POST.get('joining_next_date_of_increment')
		joining_detail.joining_department_id= request.POST.get('joining_department')
		joining_detail.joining_designation_id= request.POST.get('joining_designation')
		joining_detail.joining_responsibilities_id = request.POST.get('joining_responsibilities')
		joining_detail.joining_reporting_to_id = request.POST.get('joining_reporting_to')
		joining_detail.joining_probation_period = request.POST.get('joining_probation_period')
		joining_detail.user_employee_id = personal_details.id
		joining_detail.save()

		# Save Medical History
		medical_history_id = [int(p.split('_')[2]) for p in request.POST if 'blood_group_' in p]
		medical_history_id.sort()
		for cer in medical_history_id:
			medical_history = EmployeeEmployeeRegistrationUpdateRegistrationMedicalHistory()
			medical_history.blood_group_1 = request.POST.get('blood_group_' + str(cer)).strip()
			medical_history.type_of_illness_1 = request.POST.get('type_of_illness_' + str(cer)).strip()
			medical_history.result_1 = request.POST.get('result_' + str(cer)).strip()
			medical_history.user_employee_id = personal_details.id
			medical_history.save()

		qualification_id = [int(p.split('_')[3]) for p in request.POST if 'educational_qualificationcourse_name_' in p]
		qualification_id.sort()
		for cer in qualification_id:
			qualification = EmployeeEmployeeRegistrationUpdateEducationalQualification()
			qualification.educational_qualificationcourse_name_1= request.POST.get('educational_qualificationcourse_name_' + str(cer)).strip()
			qualification.educational_qualificationstart_date_1 = request.POST.get('educational_qualificationstart_date_' + str(cer)).strip()
			qualification.educational_qualificationend_date_1 = request.POST.get('educational_qualificationend_date_' + str(cer)).strip()
			qualification.educational_qualificationmarks_division_1 = request.POST.get('educational_qualificationmarks_division_' + str(cer)).strip()
			qualification.educational_qualificationroll_number_1= request.POST.get('educational_qualificationroll_number_' + str(cer)).strip()
			qualification.educational_qualificationuniversity_institution_1= request.POST.get('educational_qualificationuniversity_institution_' + str(cer)).strip()
			qualification.user_employee_id = personal_details.id
			qualification.save()

		professional_journey_id = [int(p.split('_')[2]) for p in request.POST if 'professional_journeycompany_' in p]
		professional_journey_id.sort()
		for cer in professional_journey_id:
			professional_journey = EmployeeEmployeeRegistrationUpdateProfessionalJourney()
			professional_journey.professional_journeycompany_1= request.POST.get('professional_journeycompany_' + str(cer)).strip()
			professional_journey.professional_journeystart_date_1 = request.POST.get('professional_journeystart_date_' + str(cer)).strip()
			professional_journey.professional_journeyend_date_1 = request.POST.get('professional_journeyend_date_' + str(cer)).strip()
			professional_journey.professional_journeylast_desgination_1_id = request.POST.get('professional_journeylast_desgination_' + str(cer)).strip()
			professional_journey.professional_journeynature_of_duties_1= request.POST.get('professional_journeynature_of_duties_' + str(cer)).strip()
			professional_journey.professional_journeylast_drawn_dalary_1= request.POST.get('professional_journeylast_drawn_dalary_' + str(cer)).strip()
			professional_journey.user_employee_id = personal_details.id
			professional_journey.save()

		salary_struct_id = [int(p.split('_')[4]) for p in request.POST if 'salary_structut_salary_code_' in p]
		salary_struct_id.sort()
		for cer in salary_struct_id:
			salary_struct = EmployeeEmployeeRegistrationUpdateSalaryStructutre()
			salary_struct.salary_structut_salary_code_1= request.POST.get('salary_structut_salary_code_' + str(cer)).strip()
			salary_struct.salary_structut_salary_name_1 = request.POST.get('salary_structut_salary_name_' + str(cer)).strip()
			salary_struct.professional_journeyend_date_1 = request.POST.get('professional_journeyend_date_' + str(cer)).strip()
			salary_struct.salary_structut_salary_frequency_1 = request.POST.get('salary_structut_salary_frequency_' + str(cer)).strip()
			salary_struct.salary_structut_amount_offered_1= request.POST.get('salary_structut_amount_offered_' + str(cer)).strip()
			salary_struct.salary_structut_percentage_value_flag_1= request.POST.get('salary_structut_percentage_value_flag_' + str(cer)).strip()
			salary_struct.salary_structut_taxability_1 = request.POST.get('salary_structut_taxability_' + str(cer)).strip()
			salary_struct.user_employee_id = personal_details.id
			salary_struct.save()

		save_bank_detail = EmployeeEmployeeRegistrationUpdateBankDetails()
		save_bank_detail.account_type = request.POST.get('account_type')
		save_bank_detail.bank_account_number = request.POST.get('bank_account_number')
		save_bank_detail.bank_name = request.POST.get('bank_name')
		save_bank_detail.branch = request.POST.get('branch')
		save_bank_detail.ifscc_code = request.POST.get('ifscc_code')
		save_bank_detail.micr = request.POST.get('micr')
		save_bank_detail.user_employee_id = personal_details.id
		save_bank_detail.save()

		reference_id = [int(p.split('_')[1]) for p in request.POST if 'referencename_' in p]
		reference_id.sort()
		for cer in reference_id:
			reference = EmployeeEmployeeRegistrationReferences()
			reference.referencename_1= request.POST.get('referencename_' + str(cer)).strip()
			reference.referencerelationship_1 = request.POST.get('referencerelationship_' + str(cer)).strip()
			reference.referencecontact_number_1 = request.POST.get('referencecontact_number_' + str(cer)).strip()
			reference.referenceemail_id_1 = request.POST.get('referenceemail_id_' + str(cer)).strip()
			reference.referenceaddress_1= request.POST.get('referenceaddress_' + str(cer)).strip()
			reference.referenceknown_since_1= request.POST.get('referenceknown_since_' + str(cer)).strip()
			reference.user_employee_id = personal_details.id
			reference.save()

		verificationreport = EmployeeEmployeeRegistrationVerificationReport()
		verificationreport.verification_agency = request.POST.get('verification_agency')
		verificationreport.finding = request.POST.get('finding')
		verificationreport.upload_report = request.FILES.get('upload_report')
		verificationreport.user_employee_id = personal_details.id
		verificationreport.save()

		verificationreport = EmployeeEmployeeRegistrationDeductionAndPerquisites()
		verificationreport.user_employee_id = personal_details.id
		verificationreport.perquisitec_category = request.POST.get('perquisitec_category')
		verificationreport.perquisitec_type = request.POST.get('perquisitec_type')
		verificationreport.perquisitec_name = request.POST.get('perquisitec_name')
		verificationreport.perquisite_frequency = request.POST.get('perquisite_frequency')
		verificationreport.perquisite_amount = request.POST.get('perquisite_amount')
		verificationreport.save()

		document_id = [int(p.split('_')[3]) for p in request.POST if 'name_of_documents_' in p]
		document_id.sort()
		for cer in document_id:
			document = EmployeeEmployeeRegistrationDocuments()
			document.name_of_documents_1 = request.POST.get('name_of_documents_' + str(cer)).strip()
			document.upload_1 = request.FILES.get('upload_' + str(cer))
			document.user_employee_id = personal_details.id
			document.save()
		messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		return redirect('crm_website_employeeservices_employeeregistration_updateregistrations_list')


class EmployeeServicesEmployeeRegistrationUpdateRegistrationsDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
		   return redirect('index')
		get_report = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.filter(id = id).delete()
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_employeeregistration_updateregistrations_list')


class AddEditCrmEmployeeEmployeeRegistrationUpdateDepartment(View):
	template = 'employee_website/employee_services/employee_registration/update_department.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeEmployeeRegistrationUpdateDepartmentForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		form = EmployeeEmployeeRegistrationUpdateDepartmentForm(request.POST)
		if form.is_valid():
			data = form.save()
			joining_detail = EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(user_employee_id = request.POST['employee_id'])
			joining_detail.joining_location= request.POST.get('new_location')
			joining_detail.joining_department_id= request.POST.get('new_department')
			joining_detail.joining_designation_id= request.POST.get('new_designation')
			joining_detail.joining_responsibilities_id = request.POST.get('new_responsibilities')
			joining_detail.joining_reporting_to_id = request.POST.get('new_reporting_to')
			joining_detail.save()
		messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		return redirect('crm_website_employeeservices_employeeregistration_updatedeaprtment_update')


class AddEditCrmEmployeeEmployeeRegistrationUpdateDepartmentJsonEmployee(View):
	def post(self, request, *args, **kwargs):
		ServicesHtml = ''
		if request.is_ajax:
			#get_info = EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(user_employee_id = request.POST['id'])
			# data = {
			# 	'employee_name':get_info.user_employee.first_name,
			# 	'department':get_info.joining_department.department,
			# 	'designation':get_info.joining_designation.designation,
			# 	'responsibilites':get_info.joining_responsibilities.responsibilities,
			# 	'reporting_to':get_info.joining_reporting_to.name,
			# 	'location':get_info.joining_location,
			# 	'current_sal':'n/a',
			# }
			# #get_info = EmployeeEmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(user_employee_id = request.POST['id'])
			data = {
				'employee_name':'yogesh',
				'department':'management',
				'designation':'manager',
				'responsibilites':'developer',
				'reporting_to':'yogesh',
				'location':'delhi',
				'current_sal':'n/a',
			}
			return JsonResponse({'data': data})


class EmployeeServicesEmployeeRegistrationEmployeeListList(View):
	template = 'employee_website/employee_services/employee_registration/update_registrations_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(user_employee__employee_created_by_id__in  = get_users).order_by('-id')
		get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeServicesEmployeeRegistrationEmployeeUpdate(View):
	template = 'employee_website/employee_services/employee_registration/update.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'new_details':EmployeeRegistrationUpdateRegistrationJoiningDetailsFormUpdate,
			'KRA_details': KeyResponsibilityUpdateKRAForm,
			'salary_structutre': EmployeeEmployeeRegistrationUpdateSalaryStructutremodelForm,
			'deduction_perquisites': EmployeeEmployeeRegistrationDeductionAndPerquisitesForm,
			'deduction': EmployeeEmployeeRegistrationDeductionForm,			
			
		}
		return render(request, self.template, context)


	def post(slef,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')

		salary_struct_id = [int(p.split('_')[4]) for p in request.POST if 'salary_structut_salary_code_' in p]
		salary_struct_id.sort()
		for cer in salary_struct_id:
			salary_struct = EmployeeRegistrationUpdateSalaryStructutre()
			salary_struct.salary_structut_salary_code_1_id = request.POST.get('salary_structut_salary_code_' + str(cer)).strip()
			salary_struct.salary_structut_salary_name_1 = request.POST.get('salary_structut_salary_name_' + str(cer)).strip()
			salary_struct.salary_structut_salary_frequency_1 = request.POST.get('salary_structut_salary_frequency_' + str(cer)).strip()
			salary_struct.salary_structut_amount_offered_1= request.POST.get('salary_structut_amount_offered_' + str(cer)).strip()
			salary_struct.salary_structut_percentage_value_flag_1= request.POST.get('salary_structut_percentage_value_flag_' + str(cer)).strip()
			salary_struct.salary_structut_taxability_1 = request.POST.get('salary_structut_taxability_' + str(cer))
			salary_struct.save()

		deduc = [int(p.split('_')[1]) for p in request.POST if 'appicablitity_' in p]
		deduc.sort()
		for cer in deduc:
			salary_struct = EmployeeRegistrationDeductionAndPerquisites()
			if str(request.POST.get('appicablitity_'+str(cer))) == "2":
				salary_struct.appicablitity_1  = str(request.POST.get('appicablitity_'+str(cer)))
				salary_struct.save()
			else:
				salary_struct.appicablitity_1  = str(request.POST.get('appicablitity_'+str(cer)))
				salary_struct.perquisitec_category_1  = str(request.POST.get('perquisitec_category_'+str(cer)))
				salary_struct.perquisitec_name_1  = str(request.POST.get('perquisitec_name_'+str(cer)))
				salary_struct.perquisite_frequency_1  = str(request.POST.get('perquisite_frequency_'+str(cer)))
				salary_struct.percentage_value_flag_1  = str(request.POST.get('percentage_value_flag_'+str(cer)))
				salary_struct.perquisite_amount_1  = str(request.POST.get('perquisite_amount_'+str(cer)))
				salary_struct.save()

		kra_update_id = [int(p.split('_')[2]) for p in request.POST if 'employee_id_' in p]
		kra_update_id.sort()
		for cer in kra_update_id:
			kra_struct = KeyResponsibilityUpdateKRA()
			kra_struct.employee_id_1_id= request.POST.get('employee_id_' + str(cer)).strip()
			kra_struct.employee_names_1 = request.POST.get('employee_names_' + str(cer)).strip()
			kra_struct.designation_1_id = request.POST.get('designation_' + str(cer)).strip()
			kra_struct.department_1_id = request.POST.get('department_' + str(cer))
			kra_struct.location_1_id= request.POST.get('location_' + str(cer)).strip()
			kra_struct.reporting_officer_1_id= request.POST.get('reporting_officer_' + str(cer)).strip()
			kra_struct.kra_period_1 = request.POST.get('kra_period_' + str(cer)).strip()
			kra_struct.month_and_year_1=request.POST.get('month_and_year_'+str(cer)).strip()
			kra_struct.kra_type_1=request.POST.get('kra_type_'+str(cer)).strip()
			kra_struct.kra_details_1=request.POST.get('kra_details'+str(cer))
			kra_struct.save()

		messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		return redirect('crm_website_employeeservices_employeeregistration_employee_list')


class EmployeeServiceEmployeeRegistrationTermination(View):
	template = 'employee_website/employee_services/employee_registration/termination.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		#instance = get_object_or_404(EmployeeUpdateRegistrationTermination, pk=id)

		context = {
 			'form':EmployeeRegistrationTermination,
 		}
		return render(request, self.template, context)
	def post(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		form=EmployeeUpdateRegistrationTermination()
		form.termination_date=request.POST.get('termination_date')
		form.approve_by=request.POST.get('approve_by')
		form.reason_termination=request.POST.get('reason_termination')
		form.termination_benifit=request.POST.get('termination_benifit')
		form.save()
		messages.add_message(request,messages.SUCCESS,"Data updated Successfully")
		return redirect('employee_services_termination')
	

#### update
# class EmployeeServicesEmployeeRegistrationEmployeeUpdate(View):
# 	template = 'employee_website/employee_services/employee_registration/update_registrations_update.html'
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		instance = get_object_or_404(EmployeeRegistrationUpdateRegistrationJoiningDetails, pk=id)
# 		context = {
# 			'form':EmployeeRegistrationUpdateRegistrationJoiningDetailsFormUpdate(instance = instance),
# 		}
# 		return render(request, self.template, context)

# 	def post(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		instance = get_object_or_404(EmployeeRegistrationUpdateRegistrationJoiningDetails, pk=id)
# 		form = EmployeeRegistrationUpdateRegistrationJoiningDetailsFormUpdate(request.POST,  instance = instance)
# 		if form.is_valid():
# 			form.save()
# 		messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
# 		return redirect('crm_website_employeeservices_employeeregistration_employee_list')

####
class LeavesUpdateLeaveQuotaOfEmployesListView(View):
	template = 'employee_website/employee_services/leaves/update_employees_leave_quota_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = LeaveandHolidaysManagementUpdateLeavesQuota.objects.filter(user_id__in = get_users).order_by('-id')
		get_report = LeaveandHolidaysManagementUpdateLeavesQuota.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class LeavesUpdateLeaveQuotaOfEmployesAddView(View):
	template = 'employee_website/employee_services/leaves/update_employees_leave_quota.html'


	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': LeaveandHolidaysManagementLeavesForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
		form = LeaveandHolidaysManagementLeavesForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('crm_website_employeeservices_employees_leavequota_list')


class LeavesUpdateLeaveQuotaOfEmployesUpdateView(View):
	template = 'employee_website/employee_services/leaves/update_employees_leave_quota.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = LeaveandHolidaysManagementUpdateLeavesQuota.objects.get(id = id )
		context = {
			'form': LeaveandHolidaysManagementLeavesForm(instance = data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
	
		data = LeaveandHolidaysManagementUpdateLeavesQuota.objects.get(id = id )
		form = LeaveandHolidaysManagementLeavesForm(request.POST, instance = data)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('crm_website_employeeservices_employees_leavequota_list')


class LeavesUpdateLeaveQuotaOfEmployesUpdateViewDelete(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = LeaveandHolidaysManagementUpdateLeavesQuota.objects.filter(id = id).delete()
		messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
		return redirect('crm_website_employeeservices_employees_leavequota_list')


class EmployeeLeavesLeaveRequestPostLeave(View):
	template = 'employee_website/employee_services/leaves/apply_leave.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeLeavesLeaveRequestForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		if not request.user.is_authenticated:
			return redirect('index')
		if request.method=='POST':
			form =EmployeeLeavesLeaveRequestForm(request.POST)
			if form.is_valid():
				form.save()
		# save_user = EmployeeLeavesLeaveRequest()
		# save_user.employee_id_id = request.user.id
		# save_user.type_of_leave_id = request.POST.get('type_of_leave')
		# save_user.leave_available = request.POST.get('leave_available')
		# save_user.start_date = request.POST.get('start_date')
		# save_user.end_date = request.POST.get('end_date')
		# save_user.total_leave = request.POST.get('total_leave')
		# save_user.explaination = request.POST.get('explaination')
		# save_user.save()
		messages.add_message(request, messages.SUCCESS, "Leave apply Successfully.")
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')


class LeavesUpdateLeaveQuotaOfEmployesUpdateViewCancel(View):
	
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeLeavesLeaveRequest.objects.filter(id = id)
		messages.add_message(request, messages.SUCCESS, "Leave cancel Successfully.")
		return redirect('crm_website_employeeservices_employees_leavequota_list')


class EmployeeLeavesLeaveRequestPendingforApprovalList(View):
	template = 'employee_website/employee_services/leaves/approve_leave.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.all()
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class allpendingleave(View):
	template = 'employee_website/employee_services/leaves/pending_for_approval_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.all()
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class ApproveLeave(View):
	def get(self,request,id):
		EmployeeLeavesLeaveRequest.objects.filter(id=id).update(status=1,leave_status='Approved')
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')

class RejectLeave(View):
	def get(self,request,id):
		EmployeeLeavesLeaveRequest.objects.filter(id=id).update(status=1,leave_status='Rejected')
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')

class putonholdLeave(View):
	def get(self,request,id):
		EmployeeLeavesLeaveRequest.objects.filter(id=id).update(status=1,leave_status='Put on hold')
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')


class DeleteLeave(View):
	def get(self,request,id):
		EmployeeLeavesLeaveRequest.objects.filter(id=id).update(status=0)
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')



def ModifyLeave(request, id):

	company = get_object_or_404(EmployeeLeavesLeaveRequest, pk=id)	

	if request.method == "POST":

		data = EmployeeLeavesLeaveRequest.objects.filter(id=id)
		if data.exists():
			form = EmployeeLeavesLeaveRequest.objects.get(id=id)

		else:
			form=EmployeeLeavesLeaveRequest(id=id)
		form.leave_status=request.POST.get('leave_status')
		form.save()
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')

	else:
		form = EmployeeLeavesModification(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/leaves/modify.html', context)





# class ModifyLeave(View):
# 	template = 'employee_website/employee_services/leaves/modify.html'

# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		context = {
# 			'form': EmployeeLeavesModification,
# 		}
# 		return render(request, self.template, context)

# 	def post(self, request, id=None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		if request.method=='POST':
# 			form =EmployeeLeavesModification(request.POST)
# 			if form.is_valid():
# 				form.save()
# 		messages.add_message(request, messages.SUCCESS, "Successfully Updated.")
# 		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')



class EmployeeLeavesLeaveRequestPostLeaveUpdate(View):
	template = 'employee_website/employee_services/leaves/update_status.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		instance = get_object_or_404(EmployeeLeavesLeaveRequest, pk=id)
		context = {
			'form': EmployeeLeavesLeaveRequestUpdateStatusForm(instance = instance),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		instance = get_object_or_404(EmployeeLeavesLeaveRequest, pk=id)
		form = EmployeeLeavesLeaveRequestUpdateStatusForm(request.POST,  instance = instance)
		if form.is_valid():
			form.save()
		messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		return redirect('crm_website_employeeservices_leave_pendingforapproval_list')


class EmployeeLeavesLeaveRequestPostLeaveJsonData(View):
	def post(self, request, *args, **kwargs):
		if request.is_ajax:
			get_info = LeaveandHolidaysManagementUpdateLeavesQuota.objects.filter(user_id = request.POST['user_id'] , leave_type_id = request.POST['id'])
			if get_info:
				data = {
					'employee_quota':get_info[0].leave_balance,
				}
			else:
				data = {
					'employee_quota': 0
				}
			return JsonResponse({'data': data})

class EmployeeLeavesLeaveRequestApprvedLeaveList2(View):
	template = 'employee_website/employee_services/leaves/approved_leave_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.filter(leave_status='Approved')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeLeavesLeaveRequestRejectedLeaveList2(View):
	template = 'employee_website/employee_services/leaves/rejected_leave_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.filter(leave_status='Rejected')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)







class EmployeeLeavesLeaveRequestApprovedLeaveList(View):
	template = 'employee_website/employee_services/leaves/approved_leave_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users, status = 2).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.filter(leave_status='Approved')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeLeavesLeaveRequestRejectedLeaveList(View):
	template = 'employee_website/employee_services/leaves/rejected_leave_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeLeavesLeaveRequest.objects.filter(employee_id_id__in = get_users, status = 3).order_by('-id')
		get_report = EmployeeLeavesLeaveRequest.objects.filter( status = 3).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeLeavesLeaveRequestMyBalanceLeaveList(View):
	template = 'employee_website/employee_services/leaves/my_balance_leave.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = LeaveandHolidaysManagementUpdateLeavesQuota.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


# Leaves
class EmployeeAttendanceUploadAttendanceUpdate(View):
	template = 'employee_website/employee_services/attendance/upload_attendance.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': UserAttendenceSerializersForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		# import pdb
		# pdb.set_trace()
		if not request.user.is_authenticated:
			return redirect('index')

		try:
			
			if 'upload_attendance' not in request.POST:
				today_date = date.today()
				# if CrmUserLoginApiLogs.objects.filter(added__date=today_date, login_true = True, user_id = request.user.id):
				# 	messages.add_message(request, messages.ERROR, "Login attendance already marked.")
				# 	return redirect('crm_website_employeeservices_leave_pendingforapproval_list')
				data  = UserLoginApiLogsAttendance()
				data.date_field=request.POST.get('date_field')
				data.date = request.POST.get('date')
				data.department_id=request.POST.get('department')
				data.designation_id=request.POST.get('designation')
				data.attendance_type =  request.POST.get('attendance_type')
				data.address =  request.POST.get('address')
				data.logout_address =  request.POST.get('logout_address')
				data.login_time =  str(request.POST['date_field'])+'-01'+' '+ request.POST['login_time']
				data.logout_time =  str(request.POST['date_field'])+'-01'+' '+ request.POST['logout_time']
				data.login_true =  True
				data.logout_true =  True
				data.employee_id_id =  request.POST.get('employee_id')
				data.employee_names=request.POST.get('employee_names')
				data.location_id=request.POST.get('location')
				data.attendance_mode=request.POST.get('attendance_mode')
				data.save()
				messages.add_message(request, messages.SUCCESS, "Attendance added Successfully.")
		
			else:
				excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
				SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
				with open(excel_name_sheet,'r')as f:
					data = csv.reader(f)
					count = 0
					for row in data:
						if count !=0:
							data  = UserLoginApiLogsAttendance()
							data.user_id = row[0]
							data.login_time =  str(row[1])+'-01'+' '+ str(row[3])
							data.attendance_type =  row[2]
							data.address =  row[4]
							data.logout_time =  str(row[1])+'-01'+' '+ str(row[5])
							data.logout_address =  row[6]
							data.login_true =  True
							data.logout_true =  True
							data.save()
						count += 1
				messages.add_message(request, messages.SUCCESS, "Attendance uploaded Successfully.")
			return redirect('crm_employee_services_attendance_update_list')
		except: 
			messages.add_message(request, messages.ERROR, "Timing format is invalid try again .")
			return redirect('crm_employee_services_attendance_update_list')






# class EmployeeAttendanceCorrection(View):
# 	template = 'employee_website/employee_services/attendance/attendance_correction.html'
# 	def get(self,request,id=None)




class EmployeeAttendanceUpdateAttendanceList(View):

    template = 'employee_website/employee_services/attendance/update_attendance.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')
        today = date.today()
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = UserLoginApiLogs.objects.filter(correction_status=1).order_by('-id')
        user_name = request.GET.get('user_name')
        search_date = request.GET.get('date')
        if  user_name != None and str(user_name) != "":
            get_data = get_data.filter(user__name__icontains=str(user_name).strip())
        if search_date != None and str(search_date) != "":
            get_data = get_data.filter(added__date =str(search_date).strip())
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)       
        context ={
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)

class EmployeeAttendanceUpdateAttendanceCorrection(View):

    template = 'employee_website/employee_services/attendance/attendance_correction.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')
        today = date.today()
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = UserLoginApiLogsAttendance.objects.filter( added__date = today).order_by('-id')
        user_name = request.GET.get('user_name')
        search_date = request.GET.get('date')
        if  user_name != None and str(user_name) != "":
            get_data = get_data.filter(user__name__icontains=str(user_name).strip())
        if search_date != None and str(search_date) != "":
            get_data = get_data.filter(added__date =str(search_date).strip())
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)       
        context ={
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)




class EmployeeAttendanceUpdateAttendanceUpdate(View):
	template = 'employee_website/employee_services/attendance/update_attendance_today.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(UserLoginApiLogs, pk = id)
		context = {
			'form': UserAttendenceSerializersUpdateForm(instance = data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		today_date = date.today()
		data = get_object_or_404(UserLoginApiLogs, pk = id)
		form = UserAttendenceSerializersUpdateForm(request.POST, instance = data)
		if form.is_valid():
			data  =form.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_employee_services_attendance_update_list')


class EmployeeAttendanceAttendanceStatusList(View):
    template = 'employee_website/employee_services/attendance/attendance_status.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')

        today = date.today()
        filter_type = request.GET.get('type')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = UserLoginApiLogsAttendance.objects.filter( added__date = today,approve_action=0).order_by('-id')
        if filter_type is not None:
        	if str(filter_type) == "1":
        		today = date.today()
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__date = today).order_by('-id')
        	elif str(filter_type) == "2":
        		current_month = datetime.now().month
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__month = current_month).order_by('-id')
        	elif str(filter_type) == "3":
        		previous_month = datetime.now().month - 1
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)       
        context ={
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)


class EmployeeAttendanceAttendanceStatusListDisplay(View):
    template = 'employee_website/employee_services/attendance/approved_attendance.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')

        today = date.today()
        filter_type = request.GET.get('type')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = UserLoginApiLogsAttendance.objects.filter(approve_action=1).order_by('-id')
        if filter_type is not None:
        	if str(filter_type) == "1":
        		today = date.today()
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__date = today).order_by('-id')
        	elif str(filter_type) == "2":
        		current_month = datetime.now().month
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__month = current_month).order_by('-id')
        	elif str(filter_type) == "3":
        		previous_month = datetime.now().month - 1
        		get_data = UserLoginApiLogsAttendance.objects.filter(added__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)       
        context ={
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)


class ApprovedAttendance(View):
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = UserLoginApiLogsAttendance.objects.filter(id = id).update(approve_action=1,approve_status='Approved',approval_date=date.today())
		return redirect('approved_attendance')


class RejectedAttendance(View):
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('index')

		get_report = UserLoginApiLogsAttendance.objects.filter(id = id).update(approve_action=1,approve_status='Rejected',approval_date=date.today())
		return redirect('approved_attendance')





###
class EmployeeAttendanceAttendanceStatusUpdate(View):
	template = 'employee_website/employee_services/attendance/update_attendance_today.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		data = get_object_or_404(UserLoginApiLogs, pk = id)
		context = {
			'form': UserLoginApiLogsForm(instance = data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
		today_date = date.today()
		data = get_object_or_404(UserLoginApiLogs, pk = id)
		form = UserLoginApiLogsForm(request.POST, instance = data)
		data.correction_status=1
		data.correction_date=date.today()
		print(form.errors)
		if form.is_valid():
			
			data  =form.save()
			messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_employee_services_attendance_status')




# HR Policies  > Update Policy
class EmployeeHRPoliciesUpdatePolicy(View):
	template = 'employee_website/employee_services/hr_policies/update_policies_upload.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		if id is None:
			context = {
				'form': EmployeeHRPoliciesUpdatePoliciesmodelForm,
			}
		else:
			data = get_object_or_404(EmployeeHRPoliciesUpdatePolicies,  pk=id)
			context = {
				'form': EmployeeHRPoliciesUpdatePoliciesmodelForm(instance = data),
			}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if id is None:
			form = EmployeeHRPoliciesUpdatePoliciesmodelForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				data.user_id  = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		else:
			data = get_object_or_404(EmployeeHRPoliciesUpdatePolicies,  pk=id)
			form = EmployeeHRPoliciesUpdatePoliciesmodelForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_employee_services_hrpolicies_upload_update_policies_list')	


class EmployeeHRPoliciesUpdateForms(View):
	template = 'employee_website/employee_services/hr_policies/update_forms_upload.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		if id is None:
			context = {
				'form': EmployeeHRPoliciesUpdateFormmodelForm,
			}
		else:
			data = get_object_or_404(EmployeeHRPoliciesUpdateForm,  pk=id)
			context = {
				'form': EmployeeHRPoliciesUpdateFormmodelForm(instance = data),
			}

		return render(request, self.template, context)

	def post(self, request, id = None):

		if id is None:
			form = EmployeeHRPoliciesUpdateFormmodelForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				data.user_id  = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		else:                                                                                        
			data = get_object_or_404(EmployeeHRPoliciesUpdateForm,  pk=id)
			form = EmployeeHRPoliciesUpdateFormmodelForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_employee_services_hrpolicies_upload_update_forms_list')


class EmployeeHRUpdateCircularsForms(View):
	template = 'employee_website/employee_services/hr_policies/update_circularal.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		if id is None:
			context = {
				'form': EmployeeHRPoliciesUpdateCircularsForm,
			}
		else:
			data = get_object_or_404(EmployeeHrPoliciesUpdateCirculars,  pk=id)
			context = {
				'form': EmployeeHRPoliciesUpdateCircularsForm(instance = data),
			}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if id is None:
			form = EmployeeHRPoliciesUpdateCircularsForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				data.user_id  = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		else:
			data = get_object_or_404(EmployeeHrPoliciesUpdateCirculars,  pk=id)
			form = EmployeeHRPoliciesUpdateCircularsForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_employee_services_hrpolicies_upload_update_circulars_list')


class EmployeeHRPoliciesUpdatePolicyList(View):
	template = 'employee_website/employee_services/hr_policies/update_policies_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeHRPoliciesUpdatePolicies.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)

		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeHRPoliciesUpdateFormmodelList(View):
	template = 'employee_website/employee_services/hr_policies/update_forms_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeHRPoliciesUpdateForm.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeHRPoliciesUpdateCircularsmodelList(View):
	template = 'employee_website/employee_services/hr_policies/update_circulars_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeHrPoliciesUpdateCirculars.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


# Claim and Reimbursement

class EmployeeClaimandReimbursementSubmitClaimsFormView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_claim.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitClaimsForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		if not request.user.is_authenticated:
			return render(request, self.template1, context)
		# import pdb
		# pdb.set_trace()
		claim_id = [int(p.split('_')[2]) for p in request.POST if 'claim_date_' in p]
		claim_id.sort()
		for cer in claim_id:
			claim = EmployeeClaimandReimbursementSubmitClaims()
			claim.claim_date_1 = request.POST.get('claim_date_' + str(cer)).strip()
			claim.location_1_id = request.POST.get('location_'+str(cer))
			claim.employee_id_1_id = request.POST.get('employee_id_' + str(cer)).strip()
			claim.employee_names_1=request.POST.get('employee_names_'+str(cer)).strip()
			claim.designation_1_id=request.POST.get('designation_'+str(cer)).strip()
			claim.department_1_id= request.POST.get('department_'+str(cer)).strip()
			claim.mode_of_travel_1=request.POST.get('mode_of_travel_'+str(cer)).strip()
			claim.no_days_1=request.POST.get('no_days_'+str(cer)).strip()
			claim.start_date_1= request.POST.get('start_date_'+str(cer)).strip()
			claim.end_date_1=request.POST.get('end_date_'+str(cer)).strip()
			claim.stay_arrangement_1=request.POST.get('stay_arrangement_'+str(cer)).strip()
			claim.ticket_expenses_1=request.POST.get('ticket_expenses_'+str(cer)).strip()
			claim.food_expenses_1=request.POST.get('food_expenses_'+str(cer)).strip()
			claim.stay_expenses_1=request.POST.get('stay_expenses_'+str(cer)).strip()
			claim.other_expenses_1=request.POST.get('other_expenses_'+str(cer)).strip()
			claim.total_expenses_1=request.POST.get('total_expenses_'+str(cer)).strip()
			claim.advance_taken_1=request.POST.get('advance_taken_'+str(cer)).strip()
			claim.balance_claim_1=request.POST.get('balance_claim_'+str(cer)).strip()

			claim.upload_1=request.POST.get('upload_'+str(cer))

			claim.save()
		messages.add_message(request, messages.SUCCESS, "Claim submited Successfully.")
		return redirect('crm_employee_services_claimandreimbursement_submitclaims')
		

class EmployeeClaimAndReimbursment(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/claim_reimbursment_request.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmpoloyeeClaimandReimbursementForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		if not request.user.is_authenticated:
			return render(request, self.template1, context)
		# import pdb
		# pdb.set_trace()
		claim_id = [int(p.split('_')[2]) for p in request.POST if 'claim_date_' in p]
		claim_id.sort()
		for cer in claim_id:
			claim = EmployeeClaimandReimbursement()
			claim.claim_date_1 = request.POST.get('claim_date_' + str(cer)).strip()
			claim.location_1_id = request.POST.get('location_'+str(cer))
			claim.employee_id_1_id = request.POST.get('employee_id_' + str(cer)).strip()
			claim.employee_names_1=request.POST.get('employee_names_'+str(cer)).strip()
			claim.designation_1_id=request.POST.get('designation_'+str(cer)).strip()
			claim.department_1_id= request.POST.get('department_'+str(cer)).strip()
			claim.date_of_processing_1=request.POST.get('date_of_processing_'+str(cer)).strip()
			claim.claim_type_1_id=request.POST.get('claim_type_'+str(cer)).strip()
			claim.claim_period_1= request.POST.get('claim_period_'+str(cer)).strip()
			claim.claim_amount_1=request.POST.get('claim_amount_'+str(cer)).strip()
			claim.claim_restriced_to_1=request.POST.get('claim_restriced_to_'+str(cer)).strip()
			claim.claim_details_1=request.POST.get('claim_details_'+str(cer)).strip()
			claim.comment_1=request.POST.get('comment_'+str(cer)).strip()
			claim.claim_upload_document=request.POST.get('claim_upload_document_'+str(cer))
			claim.save()
		messages.add_message(request, messages.SUCCESS, "Claim submited Successfully.")
		return redirect('crm_employee_services_claimandreimbursement_submitclaims')





# def EmployeeClaimAndReimbursment(request,id=id):
# 	import pdb
# 	pdb.set_trace()

# 	company = EmployeeClaimandReimbursementSubmitClaims.objects.filter(id=id)	
# 	if request.method == 'POST':
# 		# pdb.set_trace()
# 		claim_id = [int(p.split('_')[2]) for p in request.POST if 'claim_date_' in p]
# 		claim_id.sort()
# 		for cer in claim_id:
# 			claim = EmployeeClaimandReimbursementSubmitClaims()
# 			claim.claim_date_1 = request.POST.get('claim_date_' + str(cer)).strip()
# 			claim.location_1_id = request.POST.get('location_'+str(cer))
# 			claim.employee_id_1_id = request.POST.get('employee_id_' + str(cer)).strip()
# 			claim.employee_names_1=request.POST.get('employee_names_'+str(cer)).strip()
# 			claim.designation_1_id=request.POST.get('designation_'+str(cer)).strip()
# 			claim.department_1_id= request.POST.get('department_'+str(cer)).strip()
# 			#claim.date_of_processing_1=request.POST.get('date_of_processing_'+str(cer)).strip()
# 			claim.claim_type_1_id=request.POST.get('claim_type_'+str(cer)).strip()
# 			claim.claim_period_1= request.POST.get('claim_period_'+str(cer)).strip()
# 			claim.claim_amount_1=request.POST.get('claim_amount_'+str(cer)).strip()
# 			claim.claim_restriced_to_1=request.POST.get('claim_restriced_to_'+str(cer)).strip()
# 			claim.claim_details_1=request.POST.get('claim_details_'+str(cer)).strip()
# 			claim.comment_1=request.POST.get('comment_'+str(cer)).strip()
# 			claim.claim_upload_document=request.POST.get('claim_upload_document_'+str(cer))
# 			claim.save()
# 		messages.add_message(request, messages.SUCCESS, "Claim submited Successfully.")
# 		return redirect('claim_display')
# 	else:
# 		form = EmpoloyeeClaimandReimbursementForm()
# 		context={
# 			'form':form
# 		}
# 	return render(request,'employee_website/employee_services/claim_and_reimbursement/claim_reimbursment_request.html',context)



class EmployeeClaimandReimbursementSubmitClaimsApprovedView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_claim.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitClaimsApprovedForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		try:
			EmployeeClaimandReimbursementSubmitClaimsUpdateStatus.objects.get(user_id = request.user.id, submit_claim_id= id)
			messages.add_message(request, messages.WARNING, "Already submited.")
			return redirect('crm_employee_services_claimandreimbursement_submitclaims_list')
		except:
			save_data = EmployeeClaimandReimbursementSubmitClaimsUpdateStatus()
			save_data.user_id = request.user.id
			save_data.submit_claim_id = id
			save_data.approved_amount = request.POST.get('approved_amount_1')
			save_data.save()
			messages.add_message(request, messages.SUCCESS, "Amount offered Successfully.")
			return redirect('crm_employee_services_claimandreimbursement_submitclaims_list')


class EmployeeClaimandReimbursementSubmitClaimsListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/travel_calim_approval.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		# import pdb
		# pdb.set_trace()
		get_report = EmployeeClaimandReimbursementSubmitClaims.objects.filter(claim_action=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)






class EmployeeClaimandReimbursementSubmitClaimsListViewDisplay(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_claim_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeClaimandReimbursementSubmitClaims.objects.filter(claim_action=1)
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimReimbursementApproveAction(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursementSubmitClaims.objects.filter(id=id).update(claim_status='Approved',today_date=date.today(),claim_action=1)
		return redirect('travel_claim_display')

class EmployeeClaimReimbursementRejectedAction(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursementSubmitClaims.objects.filter(id=id).update(claim_status='Rejected',today_date=date.today(),claim_action=1)
		return redirect('travel_claim_display')


class EmployeeClaimReimbursementDeleteAction(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursementSubmitClaims.objects.filter(id=id).update(claim_status='pending',claim_action=0)
		return redirect('travel_claim_display')




class EmployeClaimdata(View):
	template='employee_website/employee_services/claim_and_reimbursement/claim_request.html'
	pagesize=10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeClaimandReimbursement.objects.filter(claim_action=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeClaimdatalist(View):
	template='employee_website/employee_services/claim_and_reimbursement/claim_request_display.html'
	pagesize=10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeClaimandReimbursement.objects.filter(claim_action=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursmentApprove(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursement.objects.filter(id=id).update(claim_action=1,claim_status='Approved',approved_date=date.today())
		return redirect('claim_data')

class EmployeeClaimandReimbursmentRejected(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursement.objects.filter(id=id).update(claim_action=1,claim_status='Rejected',approved_date=date.today())
		return redirect('claim_data')

class EmployeeClaimandReimbursmentDelete(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeClaimandReimbursement.objects.filter(id=id).update(claim_action=0)
		return redirect('claim_data')



class EmployeeClaimandReimbursementSubmitClaimsApprovedListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_claim_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_report = EmployeeClaimandReimbursementSubmitClaims.objects.filter(status = 'Approved').order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursementSubmitReimbursementFormView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitReimbursementForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		get_all_id = [int(p.split('_')[2]) for p in request.POST if 'reimbursement_month_' in p]
		get_all_id.sort()
		for data in get_all_id:
			save_submit_claim = EmployeeClaimandReimbursementSubmitReimbursement()
			save_submit_claim.user_id = request.user.id
			save_submit_claim.reimbursement_month_1 = request.POST.get('reimbursement_month_'+str(data))
			save_submit_claim.reimbursement_type_1_id = request.POST.get('reimbursement_type_'+str(data))
			save_submit_claim.reimbursement_period_1 = request.POST.get('reimbursement_period_'+str(data))
			save_submit_claim.details_1 = request.POST.get('details_'+str(data))
			save_submit_claim.amount_1 = request.POST.get('amount_'+str(data))
			save_submit_claim.maximum_limit_1 = request.POST.get('maximum_limit_'+str(data))
			save_submit_claim.comment_1 =  request.POST.get('comment_'+str(data))
			save_submit_claim.upload_1 = request.FILES.get('upload_'+str(data))
			save_submit_claim.save()
		messages.add_message(request, messages.SUCCESS, "Claim submited Successfully.")
		return redirect('crm_employee_services_claimandreimbursement_submitreimbursement')


class EmployeeClaimandReimbursementSubmitReimbursementApprovedView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitReimbursementFormApprovedForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		try:
			save_data = EmployeeClaimandReimbursementSubmitClaimsUpdateStatus.objects.get(user_id = request.user.id, submit_claim_id = id)
		except:
			save_data = EmployeeClaimandReimbursementSubmitClaimsUpdateStatus()
			save_data.user_id = request.user.id
			save_data.submit_claim_id = id
			save_data.approved_amount = request.POST['approved_amount_1']
			save_data.save()
		messages.add_message(request, messages.SUCCESS, "Amount offered Successfully.")
		return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_list')


class EmployeeClaimandReimbursementSubmitReimbursementApprovedListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_reimbursement_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeClaimandReimbursementSubmitReimbursement.objects.filter(status = 2).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


# Approved Claim To Process
class EmployeeClaimandReimbursementSubmitReimbursementApprovedClaimToProcessView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/claim_processing.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeClaimandReimbursementSubmitClaimsUpdateStatus.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursementApprovedDateOfProcessingView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitAmountApprovedProcessingForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(EmployeeClaimandReimbursementSubmitClaimsUpdateStatus, pk = id)
		instance = get_object_or_404(EmployeeClaimandReimbursementSubmitClaims, pk = get_data.submit_claim_id)
		form = EmployeeClaimandReimbursementSubmitAmountApprovedProcessingForm(request.POST, instance = instance)
		if form.is_valid():
			data = form.save()
			if request.POST.get('status') == "2":
				data.approved_by_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Amount offered Successfully.")
		else:
			messages.add_message(request, messages.ERROR, "Someting went Wrong.")
		return redirect('crm_employee_services_claimandreimbursement_claimprocessing_list')


class EmployeeClaimandReimbursementSubmitReimbursementApprovedClaimToProcessListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/reimbursement_processing.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeClaimandReimbursementSubmitReimbursement.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursementClaimClaimProcessedListView(View):
    template = 'employee_website/employee_services/claim_and_reimbursement/claim_processed_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
           return redirect('index')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        # get_data = EmployeeClaimandReimbursementSubmitClaims.objects.filter( status = 'Pending').order_by('-id')
        get_data = EmployeeClaimandReimbursementSubmitClaims.objects.all().order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(updated__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(date_of_processing__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(date_of_processing__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
            'responselistquery': report_paginate
        }
        return render(request, self.template, context)

#########
class EmployeeClaimandReimbursementClaimClaimProcessedUpdatesView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitClaimsUpdatesForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		manageproduct = get_object_or_404(EmployeeClaimandReimbursementSubmitClaims, pk=id)
		if request.method == "POST":
			form =EmployeeClaimandReimbursementSubmitClaimsUpdatesForm(request.POST, instance=manageproduct)
			if form.is_valid():
				form.save()
				return redirect('crm_employee_services_claimandreimbursement_claim_claimprocessed_list')
		else:
			form = EmployeeClaimandReimbursementSubmitClaimsUpdatesForm(instance=manageproduct)
		return redirect('crm_employee_services_claimandreimbursement_claim_claimprocessed_list')



class EmployeeClaimandReimbursementReimbursementRejectedListView(View):
    template = 'employee_website/employee_services/claim_and_reimbursement/submit_reimbursement_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
           return redirect('index')

       	get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = EmployeeClaimandReimbursementSubmitReimbursement.objects.all().order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(updated__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(date_of_processing__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(date_of_processing__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        
        context = {
           'responselistquery': report_paginate
        }
        return render(request, self.template, context)
###############
class EmployeeClaimandReimbursementReimbursementRejectedUpdateView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/submit_reimbursement_add.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitReimbursementSubmitUpdateForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		manageproduct = get_object_or_404(EmployeeClaimandReimbursementSubmitReimbursement, pk=id)
		if request.method == "POST":
			form =EmployeeClaimandReimbursementSubmitReimbursementSubmitUpdateForm(request.POST, instance=manageproduct)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, "Data Add Successfully.")
				return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_reimbursementprocessed_list')
		else:
			form = EmployeeClaimandReimbursementSubmitReimbursementSubmitUpdateForm(instance=manageproduct)
			messages.add_message(request, messages.SUCCESS, "Data Add Fail.")

		return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_reimbursementprocessed_list')




# All Claim and Reimbursement
class EmployeeClaimandReimbursementClaimStatusListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/claim_status_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = EmployeeClaimandReimbursementSubmitClaims.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursementSubmitReimbursementListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeClaimandReimbursementSubmitClaimsApprovedForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		manageproduct = get_object_or_404(EmployeeClaimandReimbursementSubmitReimbursement, pk=id)
		if request.method == "POST":
			form =EmployeeClaimandReimbursementSubmitClaimsApprovedForm(request.POST, instance=manageproduct)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, "Data Add Successfully.")
				return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_status_list')
		else:
			form = EmployeeClaimandReimbursementSubmitClaimsApprovedForm(instance=manageproduct)
			messages.add_message(request, messages.SUCCESS, "Data Add Fail.")

		return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_status_list')



		# try:
		# 	save_data = EmployeeClaimandReimbursementSubmitReimbursementUpdateStatus.objects.get(user_id = request.user.id, submit_claim_id = id)
		# except:
		# 	save_data = EmployeeClaimandReimbursementSubmitReimbursementUpdateStatus()
		# 	save_data.user_id = request.user.id
		# 	save_data.submit_claim_id = id
		# 	save_data.approved_amount = request.POST['approved_amount']
		# 	save_data.save()
		# messages.add_message(request, messages.SUCCESS, "Amount offered Successfully.")
		# return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_status_list')


class EmployeeClaimandReimbursementRembursementStatusListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/rembursement_status_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = EmployeeClaimandReimbursementSubmitReimbursement.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class EmployeeClaimandReimbursementSubmitReimbursementApprovedDateOfProcessingView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/approved_reimbursement.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeReimbursementSubmitAmountApprovedProcessingForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):


		manageproduct = get_object_or_404(EmployeeClaimandReimbursementSubmitReimbursement, pk=id)
		if request.method == "POST":
			form =EmployeeClaimandReimbursementSubmitAmountApprovedProcessingForm(request.POST, instance=manageproduct)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, "Data Add Successfully.")
				return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursementprocessing_list')
		else:
			form = EmployeeClaimandReimbursementSubmitAmountApprovedProcessingForm(instance=manageproduct)
			messages.add_message(request, messages.ERROR, "Someting went Wrong.")

		return redirect('crm_employee_services_claimandreimbursement_submitreimbursement_reimbursementprocessing_list')


class EmployeePayrollProcessingAcceptAttendanceListView(View):
	template = 'employee_website/employee_services/payroll/accept_attendance.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_current_month = date.today().month
		get_all_user_ids = UserLoginApiLogsAttendance.objects.all().order_by("-id")
		get_joining_details=EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.all()
		get_all_data  = ManageWorkingDays.objects.all().order_by('-id')
		get_financial_year = ManageHolidays.objects.all().order_by('-id')
	
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'get_all_data':get_all_data,
			'get_financial_year':get_financial_year,
			'stauts': ATTENDENCE_STATUS,
			'joining_detail': get_joining_details,
			# 'get_monthly_holidays_days':get_monthly_holidays_days,
		}
		return render(request, self.template, context)

	def post(self, request):
		get_current_month = date.today().month
		accept_reject = UserLoginApiLogs.objects.filter(user_id__in = [data  for data in request.POST['bul_data'].split(',')], added__month = get_current_month).update(attendance_status = request.POST['status'])
		messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		return redirect('crm_employee_services_payroll_accept_attendance_list')
#1
class UserAcceptAttendanceUpdateFormView(View):
	template = 'employee_website/employee_services/payroll/accept_attendance_update.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': UserAcceptAttendanceUpdateForm(),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		manageproduct = get_object_or_404(UserLoginApiLogs, pk=id)
		if request.method == "POST":
			form =UserAcceptAttendanceUpdateForm(request.POST, instance=manageproduct)
			if form.is_valid():
				form.save()
				return redirect('crm_employee_services_payroll_accept_attendance_list')
		else:
			form = UserAcceptAttendanceUpdateForm(instance=manageproduct)
		return redirect('crm_employee_services_payroll_accept_attendance_list')




class EmployeePayrollProcessingAcceptOverTimeListView(View):
	template = 'employee_website/employee_services/payroll/accept_overtime_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_current_month = date.today().month
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_all_user_ids =[p['user_id'] for p in OvertimeManagementUpdateOvertime.objects.values('user_id').filter(user_id__in = get_users, added__month = get_current_month, user_id = request.user.id).distinct()] 
		get_all_user_ids = OvertimeManagementUpdateOvertime.objects.all().order_by("-id")
		# get_report = User.objects.filter(id__in = get_all_user_ids)
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'stauts': ATTENDENCE_STATUS
		}
		return render(request, self.template, context)

	def post(self, request):
		get_current_month = date.today().month
		accept_reject = UserLoginApiLogs.objects.filter(user_id__in = [data  for data in request.POST['bul_data'].split(',')], added__month = get_current_month).update(attendance_status = request.POST['status'])
		messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		return redirect('crm_employee_services_payroll_accept_attendance_list')


class EmployeePayrollUpdateLeavesListView(View):
	template = 'employee_website/employee_services/payroll/update_leaves_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_current_month = date.today().month
		get_all_user_ids = EmployeeLeavesLeaveRequest.objects.filter(added__month = get_current_month).order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'leave_status':LEAVE_STATUS
		}
		return render(request, self.template, context)

	def post(self, request):
		data1 = [data  for data in request.POST['bul_data'].split(',')]
		accept_reject = EmployeeLeavesLeaveRequest.objects.filter(id__in = data1).update(status = request.POST['status'])
		messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		return redirect('crm_employee_services_payroll_update_leave_list')


class EmployeePayrollAcceptClaimsView(View):
	template = 'employee_website/employee_services/payroll/accept_claims_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_current_month = date.today().month
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_all_user_ids = EmployeeClaimandReimbursementSubmitClaims.objects.filter(user_id__in = get_users, added__month = get_current_month, user_id = request.user.id, status = 2)
		get_all_user_ids = EmployeeClaimandReimbursementSubmitClaims.objects.filter(claim_status='Approved').order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status':CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request):
		data1 = [data  for data in request.POST['bul_data'].split(',')]
		accept_reject = EmployeeClaimandReimbursementSubmitClaims.objects.filter(id__in = data1).update(status = request.POST['status'])
		messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		return redirect('crm_employee_services_payroll_claim_update_list')


class EmployeePayrollUpdateReimbursementView(View):
	template = 'employee_website/employee_services/payroll/update_reimbursement_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_current_month = date.today().month
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_all_user_ids = EmployeeClaimandReimbursement.objects.all()
		print(get_all_user_ids)
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status':CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request):
		data1 = [data  for data in request.POST['bul_data'].split(',')]
		accept_reject = EmployeeClaimandReimbursementSubmitReimbursement.objects.filter(id__in = data1).update(status = request.POST['status'])
		messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		return redirect('crm_employee_services_payroll_reimbursement_update_list')


class EmployeePayrollUpdateAdvancesView(View):
	template = 'employee_website/employee_services/payroll/update_advances_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_all_user_ids = EmployeeAdvancesSubmitAdvanceRequest.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		if 'upload_bulk_data' in request.FILES:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet,'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = EmployeePayrollProcessingUpdateAdvances()
							save_data.location = row[0]
							save_data.department = row[1]
							save_data.month_and_year = row[2]
							save_data.user_id = row[3]
							save_data.recovery_period = row[4]
							save_data.advance_amount = row[5]
							save_data.interest_rate = row[6]
							save_data.total_amount = row[7]
							save_data.recovery_amount = row[8]
							save_data.recovery_start_date = row[9]
							save_data.save()
						except EmployeePayrollProcessingUpdateAdvances.DoesNotExist:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_update_advances_list')

					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_update_advances_list')
		else:
			data1 = [data  for data in request.POST['bul_data'].split(',')]
			accept_reject = EmployeePayrollProcessingUpdateAdvances.objects.filter(id__in = data1).update(status = request.POST['status'])
			messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
			return redirect('crm_employee_services_payroll_update_advances_list')


class EmployeePayrollIncentivesView(View):
	template = 'employee_website/employee_services/payroll/update_incentives.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_current_month = date.today().month
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_all_user_ids = EmployeeAdvancesSubmitIncentiveBonus.objects.filter(user_id__in = get_users, added__month = get_current_month, user_id = request.user.id, status = 3)
		get_all_user_ids = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		if 'upload_bulk_data' in request.FILES:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet,'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = EmployeePayrollProcessingUpdateIncentives()
							save_data.location = row[0]
							save_data.department = row[1]
							save_data.month_and_year = row[2]
							save_data.user_id = row[3]
							save_data.incentive_type = row[4]
							save_data.incentive_period = row[5]
							save_data.incentive_amount = row[6]
							save_data.save()
						except:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_update_incentive_list')

					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_update_incentive_list')
		else:
			data1 = [data  for data in request.POST['bul_data'].split(',')]
			accept_reject = EmployeePayrollProcessingUpdateIncentives.objects.filter(id__in = data1).update(status = request.POST['status'])
			messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
			return redirect('crm_employee_services_payroll_update_incentive_list')



# class EmployeePayrollUpdateAdvance(View):
# 	template = 'employee_website/employee_services/employee_advance.html'
# 	pagesize = 10

# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		get_current_month = date.today().month
# 		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
# 		# get_all_user_ids = EmployeeAdvancesSubmitIncentiveBonus.objects.filter(user_id__in = get_users, added__month = get_current_month, user_id = request.user.id, status = 3)
# 		get_all_user_ids = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by("-id")
# 		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
# 		context = {
# 			'responselistquery': report_paginate,
# 			'status': CLAIM_STATUS
# 		}
# 		return render(request, self.template, context)











class EmployeeUpdateTaxDeclarationView(View):
	template = 'employee_website/employee_services/payroll/update_tax_declaration.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		form = EmployeePayrollProcessingUpdateTaxDeclarationForm()
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_all_user_ids = EmployeePayrollProcessingUpdateTaxDeclaration.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS,
			'form':form
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		                                             
		if 'upload_bulk_data' not in request.FILES:

			form = EmployeePayrollProcessingUpdateTaxDeclarationForm(request.POST)
			
			if form.is_valid():
				form.save()
			return redirect('crm_employee_services_payroll_tax_declaration_list')
			
		else:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet, 'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = EmployeePayrollProcessingUpdateTaxDeclaration()
							save_data.location = row[0]
							save_data.departments = row[1]
							save_data.assessment_year = row[2]
							save_data.employee_id = row[3]
							save_data.employee_names= row[4]
							save_data.tax_declaration_type = row[5]
							save_data.tax_rule = row[6]
							save_data.exemption_claimed = row[7]
							save_data.exemption_approved = row[8]
							save_data.maximum_limit = row[9]
							save_data.save()
							messages.add_message(request, messages.SUCCESS, "Data upload Sucessfully.")
							return redirect('crm_employee_services_payroll_tax_declaration_list')
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_tax_declaration_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_tax_declaration_list')
		
###

def EmployeeUpdateTaxDeclarationUpdateView(request, id = None):
	form = EmployeePayrollProcessingUpdateTaxDeclarationForm()
	manageproduct = get_object_or_404(EmployeePayrollProcessingUpdateTaxDeclaration, pk=id)
	if request.method == "POST":
		form =EmployeePayrollProcessingUpdateTaxDeclarationForm(request.POST, instance=manageproduct)
		if form.is_valid():
			form.save()
			return redirect('crm_employee_services_payroll_tax_declaration_list')
	else:
		form = EmployeePayrollProcessingUpdateTaxDeclarationForm(instance=manageproduct)
	return render(request,'employee_website/employee_services/payroll/update_tax_declaration_edit.html',{'form':form})
########

class EmployeeUpdateTaxRecoveryView(View):
	template = 'employee_website/employee_services/payroll/update_tax_recovery.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = EmployeePayrollProcessingUpdateTaxRecoveryForm()
		
		get_all_user_ids = EmployeePayrollProcessingUpdateTaxRecovery.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'form':form
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		if 'upload_bulk_data' not in request.FILES:
			form = EmployeePayrollProcessingUpdateTaxRecoveryForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect('crm_employee_services_payroll_tax_recovery_list')
			
		else:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet, 'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							
							save_data = EmployeePayrollProcessingUpdateTaxRecovery()
							save_data.location = row[0]
							save_data.departments = row[1]
							save_data.assessment_year = row[2]
							save_data.employee_id = row[3]
							save_data.employee_names= row[4]
							save_data.year_to_date_salary = row[5]
							save_data.annual_salary = row[6]
							save_data.total_tax_payable = row[7]
							save_data.tax_already_recovered = row[8]
							save_data.recovery_during_current_month = row[9]
							save_data.total_tax_recovered = row[10]
							save_data.balance_tax_payable = row[11]
							save_data.save()
							messages.add_message(request, messages.SUCCESS, "Data upload Sucessfully.")
							return redirect('crm_employee_services_payroll_tax_recovery_list')
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_tax_recovery_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_tax_recovery_list')
		
###

def EmployeeUpdateTaxRecoveryUpdateView(request, id = None):
	form = EmployeePayrollProcessingUpdateTaxRecoveryForm()
	manageproduct = get_object_or_404(EmployeePayrollProcessingUpdateTaxRecovery, pk=id)
	if request.method == "POST":
		form =EmployeePayrollProcessingUpdateTaxRecoveryForm(request.POST, instance=manageproduct)
		if form.is_valid():
			form.save()
			return redirect('crm_employee_services_payroll_tax_recovery_list')
	else:
		form = EmployeePayrollProcessingUpdateTaxRecoveryForm(instance=manageproduct)
	return render(request,'employee_website/employee_services/payroll/update_tax_recovery_edit.html',{'form':form})


#######end 

class EmployeeSalaryDeductionsListAddView(View):
	template = 'employee_website/employee_services/payroll/statutory_deductions_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = PayrollStatutoryDeductionsForm()
		get_all_user_ids = PayrollStatutoryDeductions.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS,
			'form':form,
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
	
		if 'upload_bulk_from_btn' not in request.FILES:
			
			if request.method=="POST":
				form = PayrollStatutoryDeductionsForm(request.POST)
				
				if form.is_valid():
					form.save()
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_crmemployee_manageemployee_statutorydeductions_list')

		else:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet, 'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = PayrollStatutoryDeductions()
							save_data.user_id = row[0]
							data_time = datetime.strptime(str(row[1]), "%d/%m/%Y") 
							save_data.month_and_year = data_time.strftime("%Y-%m-%d")
							save_data.deduction_type_id = row[2]
							save_data.employer_contribution = row[3]
							save_data.employee_contribution = row[4]
							save_data.others = row[5]
							save_data.total_deduction = row[6]
							save_data.save()
							messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
							return redirect('crm_crmemployee_manageemployee_statutorydeductions_list')
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_crmemployee_manageemployee_statutorydeductions_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_crmemployee_manageemployee_statutorydeductions_list')


def PayrollStatutoryDeductionsUpdateView(request, id = None):
	form = PayrollStatutoryDeductionsUpdateForm()
	manageproduct = get_object_or_404(PayrollStatutoryDeductions, pk=id)
	if request.method == "POST":
		form =PayrollStatutoryDeductionsUpdateForm(request.POST, instance=manageproduct)
		if form.is_valid():
			form.save()
			return redirect('crm_crmemployee_manageemployee_statutorydeductions_list')
	else:
		form = PayrollStatutoryDeductionsUpdateForm(instance=manageproduct)
	return render(request,'employee_website/employee_services/payroll/statutory_deductions_update.html',{'form':form})


class PayrollSalaryVoucherListAddView(View):
	template = 'employee_website/employee_services/payroll/payroll_salary_voucher_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = PayrollSalaryVoucherForm()
		get_all_user_ids = PayrollSalaryVoucher.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS,
			'form':form
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		
		if 'upload_bulk_data' not in request.FILES:
			if request.method =="POST":
				form =PayrollSalaryVoucherForm(request.POST)
				if form.is_valid():
					form.save()
					messages.add_message(request, messages.SUCCESS, 'Data Is Save SuceessFully.')
					return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
				messages.add_message(request, messages.SUCCESS, 'Invalid Data.')
				return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
		else:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet,'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = PayrollSalaryVoucher()
							save_data.month_and_year =row[0]
							save_data.gl_code = row[1]
							save_data.particulars = row[2]
							save_data.debit_amount = row[3]
							save_data.credit_amount = row[4]
							save_data.save()
							messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
							return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
		# else:
		# 	data1 = [data  for data in request.POST['bul_data'].split(',')]
		# 	accept_reject = PayrollSalaryVoucher.objects.filter(id__in = data1).update(status = request.POST['status'])
		# 	messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		# 	return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')

###


def PayrollSalaryVoucherListUpdateView(request, id = None):
	
	form = PayrollSalaryVoucherUpdateForm()
	manageproduct = get_object_or_404(PayrollSalaryVoucher, pk=id)
	if request.method == "POST":
		form =PayrollSalaryVoucherUpdateForm(request.POST, instance=manageproduct)
		if form.is_valid():
			form.save()
			return redirect('crm_crmemployee_manageemployee_salaryvoucher_list')
	else:
		form = PayrollSalaryVoucherUpdateForm(instance=manageproduct)
	return render(request,'employee_website/employee_services/payroll/payroll_salary_voucher_update.html',{'form':form})




class PayrollSalaryDisbursementListAddView(View):
	template = 'employee_website/employee_services/payroll/salary_disbursement_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_all_user_ids = PayrollSalaryDisbursement.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		
		excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
		SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
		with open(excel_name_sheet,'r')as f:
			data = csv.reader(f)
			count = 0
			for row in data:
				if count !=0:
					try:
						
						save_data = PayrollSalaryDisbursement()
						# data_time = datetime.strptime(str(row[0]), "%d/%m/%Y") 
						# save_data.month_and_year = data_time.strftime("%Y-%m-%d")
						save_data.month_and_year = row[0]
						save_data.employee_id = row[1]
						save_data.employee_names =row[2]
						save_data.bank_name = row[3]
						save_data.ifsc_code = row[4]
						save_data.account_number = row[5]
						save_data.amount = row[6]
						save_data.mode_of_payment = row[7]
						save_data.date_of_payment = row[8]
						# date_payment = datetime.strptime(str(row[8]), "%d/%m/%Y") 
						# save_data.date_of_payment = date_payment.strftime("%Y-%m-%d")
						save_data.save()
						messages.add_message(request, messages.SUCCESS, "Data Save SuccessFully.")
						return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
					except Exception as e:
						messages.add_message(request, messages.ERROR, "Something went wrong.")
						return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
				count += 1
			messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
####
### upload data to form 
def PayrollSalaryDisbursementListAddFormView(request):
	form = PayrollSalaryDisbursementAddForm()
	if request.method=="POST":
		form = PayrollSalaryDisbursementAddForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
	return render(request,'employee_website/employee_services/payroll/salary_disbursement_addedit.html',{'form':form})
		
####
def PayrollSalaryDisbursementListUpdate(request,id=None):
	manageEmp = get_object_or_404(PayrollSalaryDisbursement,pk=id)
	form = PayrollSalaryDisbursementAddForm(instance=manageEmp)
	
	if request.method=='POST':
		form = PayrollSalaryDisbursementAddForm(request.POST,instance=manageEmp)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
	return render(request,'employee_website/employee_services/payroll/salary_disbursement_addedit.html',{'form':form})



class EmployeePayrollProcessingTaxCalculationView(View):
	template = 'employee_website/employee_services/payroll/tax_calculation.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = EmployeePayrollProcessingTaxCalculationForm()
		get_all_user_ids = EmployeePayrollProcessingTaxCalculation.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS,
			'form':form
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		if 'upload_bulk_data' not in request.FILES:
		
			form = EmployeePayrollProcessingTaxCalculationForm(request.POST)
			if form.is_valid():
				form.save()
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_employee_services_payroll_tax_calculation_list')
		
		else:
			
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet,'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = EmployeePayrollProcessingTaxCalculation()
							save_data.location = row[0]
							save_data.departments = row[1]
							save_data.assessment_year = row[2]
							save_data.year_to_date_salary = row[3]
							save_data.annual_salary = row[4]
							save_data.other_income = row[5]
							save_data.total_income = row[6]
							save_data.exemption = row[7]
							save_data.deduction = row[9]
							save_data.taxable_income = row[10]
							save_data.tax = row[11]
							save_data.cess = row[12]
							save_data.total_tax_payable = row[13]
							save_data.tax_deducted = row[14]
							save_data.tax_paid = row[15]
							# save_data.balance_tax_payable = row[16]
							save_data.save()
					
							messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
							return redirect('crm_employee_services_payroll_tax_calculation_list')
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_tax_calculation_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_tax_calculation_list')
		# else:
		# 	data1 = [data  for data in request.POST['bul_data'].split(',')]
		# 	accept_reject = EmployeePayrollProcessingTaxCalculation.objects.filter(id__in = data1).update(status = request.POST['status'])
		# 	messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
		# 	return redirect('crm_employee_services_payroll_tax_calculation_list')

#########
def EmployeePayrollProcessingTaxCalculationUpdateView(request,id=None):
	manage_data = get_object_or_404(EmployeePayrollProcessingTaxCalculation,pk=id)
	form = EmployeePayrollProcessingTaxCalculationForm(instance=manage_data)
	if request.method=="POST":
		form = EmployeePayrollProcessingTaxCalculationForm(request.POST,instance=manage_data)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS, "Data Update Successfully.")
			return redirect('crm_employee_services_payroll_tax_calculation_list')
		else:
			messages.add_message(request,messages.ERROR, "Something went wrong.")
			return redirect('crm_employee_services_payroll_tax_calculation_list')
	return render(request, 'employee_website/employee_services/payroll/tax_calculation_update.html' ,{'form':form})

class EmployeePayrollProcessingUpdateRecoveriesView(View):
	template = 'employee_website/employee_services/payroll/update_recoveries_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_all_user_ids = EmployeePayrollProcessingUpdateRecoveries.objects.all().order_by("-id")
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'status': CLAIM_STATUS
		}
		return render(request, self.template, context)

	def post(self, request, *args, **kwargs):
		if not request.user.is_authenticated:
			return redirect('index')
		if 'upload_bulk_data' in request.FILES:
			excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
			SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
			with open(excel_name_sheet,'r')as f:
				data = csv.reader(f)
				count = 0
				for row in data:
					if count !=0:
						try:
							save_data = EmployeePayrollProcessingUpdateRecoveries()
							save_data.location = row[0]
							save_data.departments = row[1]
							save_data.month_and_year = row[2]
							save_data.employee_id = row[3]
							save_data.employee_names = row[4]
							save_data.recovery_period = row[5]
							save_data.recovery_type = row[6]
							save_data.recovery_amount = row[7]
							save_data.save()
						except Exception as e:
							messages.add_message(request, messages.ERROR, "Something went wrong.")
							return redirect('crm_employee_services_payroll_update_recovery_list')
					count += 1
				messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
				return redirect('crm_employee_services_payroll_update_recovery_list')
		else:
			data1 = [data  for data in request.POST['bul_data'].split(',')]
			accept_reject = EmployeePayrollProcessingUpdateRecoveries.objects.filter(id__in = data1).update(status = request.POST['status'])
			messages.add_message(request, messages.SUCCESS, "Status Change Successfully..")
			return redirect('crm_employee_services_payroll_update_recovery_list')


### upload data to form 
def EmployeePayrollProcessingUpdateRecoveriesAdd(request):
	form = EmployeePayrollProcessingUpdateRecoveriesAddForm()
	if request.method=="POST":
		form = EmployeePayrollProcessingUpdateRecoveriesAddForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_employee_services_payroll_update_recovery_list')
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
			return redirect('crm_employee_services_payroll_update_recovery_list')
	return render(request,'employee_website/employee_services/payroll/update_recoveries_editadd.html',{'form':form})
		
####
def EmployeePayrollProcessingUpdateRecoveriesUpdate(request,id=None):

	manageEmp = get_object_or_404(EmployeePayrollProcessingUpdateRecoveries,pk=id)
	form = EmployeePayrollProcessingUpdateRecoveriesAddForm(instance=manageEmp)
	
	if request.method=='POST':
		form = EmployeePayrollProcessingUpdateRecoveriesAddForm(request.POST,instance=manageEmp)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data uploaded Successfully.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
		else:
			messages.add_message(request, messages.ERROR, "Something went wrong.")
			return redirect('crm_crmemployee_manageemployee_salarydisbursement_list')
	return render(request,'employee_website/employee_services/payroll/update_recoveries_editadd.html',{'form':form})

	
	
#1
# Key Responsibility Areas & Targets
class AddEditKeyResponsibilityAreasUpdateTargetsKRATargetsView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_update_kra_targets.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityUpdateKRAForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		

		kra_update_id = [int(p.split('_')[2]) for p in request.POST if 'employee_id_' in p]
		kra_update_id.sort()
		for cer in kra_update_id:
			kra_struct = KeyResponsibilityUpdateKRA()
			kra_struct.employee_id_1_id= request.POST.get('employee_id_' + str(cer)).strip()
			kra_struct.employee_names_1 = request.POST.get('employee_names_' + str(cer)).strip()
			kra_struct.designation_1_id = request.POST.get('designation_' + str(cer)).strip()
			kra_struct.department_1_id = request.POST.get('department_' + str(cer)).strip()
			kra_struct.location_1_id= request.POST.get('location_' + str(cer)).strip()
			kra_struct.reporting_officer_1_id= request.POST.get('reporting_officer_' + str(cer)).strip()
			kra_struct.kra_period_1 = request.POST.get('kra_period_' + str(cer)).strip()
			kra_struct.month_and_year_1=request.POST.get('month_and_year_'+str(cer)).strip()
			kra_struct.kra_type_1=request.POST.get('kra_type_'+str(cer)).strip()
			kra_struct.kra_details_1=request.POST.get('kra_details'+str(cer))
			

			kra_struct.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")

				
		
		
		return redirect('crm_employee_services_payroll_keyresponsibilityareas_update_kra')


class AddEditKeyResponsibilityAreasUpdateTargetsView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_kra_target.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityAreasTargetsUpdateKRATargetsForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		
		update_target_id = [int(p.split('_')[2]) for p in request.POST if 'employee_id_' in p]
		update_target_id.sort()
		for cer in update_target_id:
			update_struct = KeyResponsibilityUpdateTargets()
			update_struct.employee_id_1_id= request.POST.get('employee_id_' + str(cer)).strip()
			update_struct.employee_names_1 = request.POST.get('employee_names_' + str(cer)).strip()
			update_struct.designation_1_id = request.POST.get('designation_' + str(cer)).strip()
			update_struct.department_1_id = request.POST.get('department_' + str(cer)).strip()
			update_struct.location_1_id= request.POST.get('location_' + str(cer)).strip()
			update_struct.reporting_officer_1_id= request.POST.get('reporting_officer_' + str(cer)).strip()
			update_struct.target_period_1 = request.POST.get('target_period_' + str(cer)).strip()
			update_struct.month_and_year_1=request.POST.get('month_and_year_'+str(cer)).strip()
			update_struct.target_type_1=request.POST.get('target_type_'+str(cer)).strip()
			update_struct.target_name_1=request.POST.get('target_name_'+str(cer))
			update_struct.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")		
		return redirect('KRA_update_targets')

class AddEditKeyResponsibilityAreasApproveKRAView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_approve_KRA.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityAreasApproveKRAForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = KeyResponsibilityAreasApproveKRAForm(request.POST)
		if form.is_valid():
			form = form.save()
			form.user_id = request.user.id
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('KRA_approve_KRA')


class AddEditKeyResponsibilityAreasApproveTargetView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_approve_KRA.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityAreasApproveTargetForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = KeyResponsibilityAreasApproveTargetForm(request.POST)
		if form.is_valid():
			form = form.save()
			form.user_id = request.user.id
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('KRA_approve_target')

		
class AddEditKeyResponsibilityKraPeformanceView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_kra_performance.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityKRAPerformanceForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = KeyResponsibilityKRAPerformanceForm(request.POST)
		if form.is_valid():
			form = form.save()
			form.user_id = request.user.id
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('KRA_approve_target')


class AddEditKeyResponsibilityKratargetperformanceachievementView(View):
	template = 'employee_website/employee_services/kra_responsibility_areas_target/kra_achievement_performance.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KeyResponsibilityAreasTargetAchievementForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = KeyResponsibilityAreasTargetAchievementForm(request.POST)
		if form.is_valid():
			form = form.save()
			form.user_id = request.user.id
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('KRA_approve_target')


# class KeyResponsibilityAreasTargetsKRATargetsPerformanceListView(View):
# 	template = 'employee_website/employee_services/kra_responsibility_areas_target/kra_targets_performance_list.html'
# 	pagesize = 10

# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
# 		# data_list = KeyResponsibilityAreasTargetsUpdateKRATargets.objects.filter(user_id__in = get_users)
	
		
# 		data_list = KeyResponsibilityAreasTargetsUpdateKRATargets.objects.all()

# 		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
# 		context = {
# 			'responselistquery': report_paginate,
# 		}
# 		return render(request, self.template, context)


# class KeyResponsibilityAreasTargetsKRATargetsPerformanceUpdateView(View):
# 	template = 'employee_website/employee_services/kra_responsibility_areas_target/add_edit_update_kra_targets.html'

# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		context = {
# 			'form': KeyResponsibilityAreasTargetsUpdateKRATargetsUpdateForm,
# 		}
# 		return render(request, self.template, context)

# 	def post(self, request, id = None):
# 		data = get_object_or_404(KeyResponsibilityAreasTargetsUpdateKRATargets, pk = id)
# 		data.status = request.POST.get('status')
# 		data.kra_fulfilment = request.POST.get('kra_fulfilment')
# 		data.save()
# 		messages.add_message(request, messages.SUCCESS, "Data added successfully.")
# 		return redirect('crm_employee_services_payroll_kra_target_performance_list')


# class KeyResponsibilityAreasTargetsKRATargetsReviewListView(View):
# 	template = 'employee_website/employee_services/kra_responsibility_areas_target/kra_target_review_list.html'
# 	pagesize = 10

# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
		
# 		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
# 		current_month = datetime.now().month
# 		# data_list = KeyResponsibilityAreasTargetsUpdateKRATargets.objects.filter(user_id__in = get_users)
# 		data_list = KeyResponsibilityAreasTargetsUpdateKRATargets.objects.all().order_by('-id')

# 		if str(request.GET.get('filter_type')) == "1":
# 			data_list = data_list.filter(month_and_year__month = current_month)
# 		elif str(request.GET.get('filter_type')) == "2":
# 			data_list = data_list.filter(month_and_year__month = current_month - 1)
	
# 		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
# 		context = {
# 			'responselistquery': report_paginate,
# 		}
# 		return render(request, self.template, context)


class EmployeeExitEmployeeResignationLetterView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeExitEmployeeResignationForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		# import pdb
		# pdb.set_trace()
		form = EmployeeExitEmployeeResignationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('employee_services_employee_resignation')


class EmployeeExitEmployeeRecommendationView(View):
	template = 'employee_website/employee_services/employee_exit/exit_employee_recommendation_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(user_id__in = get_users)
		
		
		data_list = EmployeeExitEmployeeResignation.objects.filter(exit_recommended=0)
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)

# class EmployeeExitrecommended(View):
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self, request, id = None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		EmployeeExitEmployeeResignation.objects.update(exit_recommended=1)
# 		# context = {
# 		# 	'form': EmployeeExitEmployeeResignationUpdateStatusForm(instance = get_data),
# 		# }
# 		return redirect('exit_employee_approval')



class EmployeeExitEmployeeResignationLetterResignationStatusView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		EmployeeExitEmployeeResignation.objects.update(exit_recommended=1)

		context = {
			'form': EmployeeExitEmployeeResignationUpdateStatusForm(instance = get_data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		form = EmployeeExitEmployeeResignationUpdateStatusForm(request.POST, instance = get_data)
		if form.is_valid():
			data = form.save()
			if request.POST['status'] == '2':
				data.approved_date = datetime.now()
				data.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('employee_exit_management_recommendation')


class EmployeeExitEmployeeApprovalView(View):
	template = 'employee_website/employee_services/employee_exit/exit_employee_approval_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(user_id__in = get_users)
		
		
		data_list = EmployeeExitEmployeeResignation.objects.filter(exit_recommended=1,approve=0)
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)


class EmployeeExitEmployeeApprove(View):
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		EmployeeExitEmployeeResignation.objects.update(approve=1)

		# context = {
		# 	'form': EmployeeExitEmployeeResignationUpdateStatusForm(instance = get_data),
		# }
		return redirect('employee_services_employee_relieving_list')

class EmployeeExitEmployeeEmployeeRelievingView(View):
	template = 'employee_website/employee_services/employee_exit/employee_relieving.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(user_id__in = get_users, status = 2)
		data_list = EmployeeExitEmployeeResignation.objects.filter(approve=1)

		

		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)


class EmployeeExitEmployeeFullandFinalSettlementListView(View):
	template = 'employee_website/employee_services/employee_exit/full_and_final_settlement_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(Q(status = 3) | Q(status = 5), user_id__in =get_users, )
		data_list = EmployeeExitEmployeeResignation.objects.filter(approve=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)


class EmployeeExitEmployeeResignationFandFView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)

		context = {
			'form': EmployeeExitFullandfinalForm(instance = get_data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		form = EmployeeExitFullandfinalForm(request.POST, instance = get_data)
		if form.is_valid():
			data = form.save()
			if request.POST:
				data.approved_date = datetime.now()
				data.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('employee_exit_management_recommendation')


class EmployeeExitEmployeeListView(View):
	template = 'employee_website/employee_services/employee_exit/employee_exit.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(Q(status = 3) | Q(status = 5), user_id__in =get_users, )
		data_list = EmployeeExitEmployeeResignation.objects.filter(approve=1).order_by('-id')

		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)






class EmployeeExitEmployeeResignationLetterListView(View):
	template = 'employee_website/employee_services/employee_exit/resignation_status_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# data_list = EmployeeExitEmployeeResignation.objects.filter(user_id__in = get_users)
		
		
		data_list = EmployeeExitEmployeeResignation.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)





class EmployeeExitEmployeeResignationRelievingStatusView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		context = {
			'form': EmployeeExitEmployeeRelievingUpdateStatusForm(instance = get_data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		form = EmployeeExitEmployeeRelievingUpdateStatusForm(request.POST, instance = get_data)
		if form.is_valid():
			data = form.save()
			if request.POST['status'] == '2':
				data.approved_date = datetime.now()
				data.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('employee_services_employee_relieving_list')	



class EmployeeExitEmployeeFullandFinalSettlementUpdateStatusView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		context = {
			'form': EmployeeExitEmployeeFullandFinalSettlementUpdateStatusseForm(instance = get_data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(EmployeeExitEmployeeResignation, pk = id)
		form = EmployeeExitEmployeeFullandFinalSettlementUpdateStatusseForm(request.POST, instance = get_data)
		if form.is_valid():
			data = form.save()
			data.approved_date = datetime.now()
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('employee_services_employee_fullandfinalsettlement_list')






class WebsiteHolidaysListView(View):
    template = 'employee_website/employee_services/leaves/manage_manage_holidays_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_financial_year = ManageHolidays.objects.all().order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_financial_year, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)


class WebsiteAddUpdateHoliDaysView(View):
    template = 'employee_website/employee_services/leaves/add_manage_holidays.html'

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, holidaysdaysid = None):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        if holidaysdaysid is None:
            data = ''
            holidaysdaysid = None
        else:
            data = get_object_or_404(ManageHolidays, pk=holidaysdaysid)
            holidaysdaysid = holidaysdaysid
        context = {
            'data': data, 
            'holidaysdaysid': holidaysdaysid,
            'impace_on_salary':YESNO,
            'parent_company': CompanySetup.objects.filter(is_active = True).order_by('-id'),
            'head_offce': ManageHeadOfficeSetup.objects.filter(is_active = True).order_by('-id'),
            'branches': ManageBranch.objects.filter(is_active = True).order_by('-id'),
            'month_list' : Getmonthlist.month_list(),
            'year_list':Getyearlist.year_list()
        }
        return render(request, self.template, context)

    def post(self, request, holidaysdaysid = None):
        if request.POST['holidaysdaysid'] is None or request.POST['holidaysdaysid'] == "None":
            save_fina_year = ManageHolidays()
            messages.add_message(request, messages.SUCCESS, "Holiday added Successfully.")
        else:
            holidaysdaysid = request.POST['holidaysdaysid']
            save_fina_year = get_object_or_404(ManageHolidays, pk=holidaysdaysid)
            messages.add_message(request, messages.SUCCESS, "Holiday updated Successfully.")
        save_fina_year.holidays_type =  request.POST['holidays_type']
        save_fina_year.year =  str(request.POST['holiday_year'])
        save_fina_year.month =  str(request.POST['holiday_month'])
        save_fina_year.company_id =  request.POST['parent_company']
        save_fina_year.head_office_id =  request.POST['head_offce']
        save_fina_year.date =  request.POST['holidays_date']
        save_fina_year.implact_on_salry =  request.POST['implact_on_salry']
        if 'is_active' in request.POST:
            save_fina_year.is_active =  True
        else:
            save_fina_year.is_active =  False
        save_fina_year.save()
        append_data = []
        if 'branches' in request.POST:
            for p in  dict(request.POST)['branches']:
            	if str(p) != "":
	                append_data.append(p)
	                try:
	                    saved_data = ManageHolidaysBranches.objects.get(holiday_id = save_fina_year.id, branch_id = p)
	                except ManageHolidaysBranches.DoesNotExist:
	                    saved_data = ManageHolidaysBranches()
	                    saved_data.holiday_id = save_fina_year.id
	                    saved_data.branch_id = p
	                    saved_data.save()
        ManageHolidaysBranches.objects.filter(~Q(branch_id__in = append_data), holiday_id = save_fina_year.id).delete()
        return redirect('website_list_holi_days_add')


class WebsiteHolidaysDeletView(View):
    def get(self, request, holidaysdaysid):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_report = ManageHolidays.objects.filter(id = holidaysdaysid).delete()
        messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
        return redirect('website_list_holi_days_add')


# Overtime
class OvertimeManagementUpdateOvertimeListView(View):
    template = 'employee_website/employee_services/over_time/update_over_time_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = OvertimeManagementUpdateOvertime.objects.filter( status = 1).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)

    def post(self, request):
        excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
        SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
        with open(excel_name_sheet,'r')as f:
            data = csv.reader(f)
            count = 0
            for row in data:
                if count !=0:
                    save_data = OvertimeManagementUpdateOvertime()
                    data_time = datetime.strptime(str(row[1]), "%d/%m/%y") 
                    save_data.user_id = row[0]
                    save_data.month_and_year_date = data_time.strftime("%Y-%m-%d")
                    save_data.overtime_start = row[2]
                    save_data.overtime_end = row[3]
                    save_data.total_hours = row[4]
                    save_data.reason = row[5]
                    save_data.save()
                count += 1
        messages.add_message(request, messages.SUCCESS, "Overtime uploaded successfully.")
        return redirect('website_edit_update_over_time_list')


###
class OvertimeManagementUpdateOvertimeAddView(View):
	template = 'employee_website/employee_services/over_time/update_over_time_add.html'
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = Overtimeupdateform()
		context={
			'form':form
		}
		return render(request,self.template,context)
	def post(self,request):
		import pdb
		pdb.set_trace()
		if not request.user.is_authenticated:
			return redirect('index')
		if request.method=="POST":
			form = Overtimeupdateform(request.POST)
			if form.is_valid():
				form.save()
				
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('website_edit_update_over_time_list')

		

class OvertimeManagementUpdateOvertimeDeletView(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_report = OvertimeManagementUpdateOvertime.objects.filter(id = id).update(action_status=0,overtime_status='pending')
        messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
        return redirect('website_edit_update_over_time_status_list')



class OvertimeManagementUpdateOvertimeStatusListViewDisplay(View):
    template = 'employee_website/employee_services/over_time/overtime_approval_display.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = OvertimeManagementUpdateOvertime.objects.filter(action_status=1).order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(month_and_year_date__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(month_and_year_date__month = previous_month).order_by('-id')
        
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)





class OvertimeManagementUpdateOvertimeStatusListView(View):
    template = 'employee_website/employee_services/over_time/update_over_time_status_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = OvertimeManagementUpdateOvertime.objects.filter(action_status=0).order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(month_and_year_date__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(month_and_year_date__month = previous_month).order_by('-id')
        
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)





class OvertimeApprove(View):
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('adminlogin')
		get_report = OvertimeManagementUpdateOvertime.objects.filter(id = id).update(action_status=1,overtime_status='Approve',approved_date=date.today())
		return redirect('overtime_approval_display')

class OvertimeRejected(View):
	def get(self, request, id):
		if not request.user.is_authenticated:
			return redirect('adminlogin')
		get_report = OvertimeManagementUpdateOvertime.objects.filter(id = id).update(action_status=1,overtime_status='Rejected',approved_date=date.today())
		return redirect('overtime_approval_display')




class OvertimeManagementUpdateOvertimeStatusListViewUpdateStatusView(View):
	template = 'employee_website/employee_services/employee_exit/add_employee_resignation.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_data = get_object_or_404(OvertimeManagementUpdateOvertime, pk = id)
		context = {
			'form': OvertimeManagementUpdateOvertimeStatusListViewUpdateStatusViewForm(instance = get_data),
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		get_data = get_object_or_404(OvertimeManagementUpdateOvertime, pk = id)
		form = OvertimeManagementUpdateOvertimeStatusListViewUpdateStatusViewForm(request.POST, instance = get_data)
		if form.is_valid():
			data = form.save()
			
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('website_edit_update_over_time_list')


class TravelClaimManagementTravelConveyanceTravelRequestListView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/travel_approved_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_data = TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(action=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class TravelClaimManagementTravelConveyanceAllTravelRequest(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/travel_request_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_data = TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(action=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class travelrequestapprove(View):
	def get(request,self,id):
		TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(id=id).update(action=1,status='Approved')
		return redirect('website_travel_request_list')

class travelrequestrejected(View):
	def get(request,self,id):
		TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(id=id).update(action=1,status='Rejected')
		return redirect('website_travel_request_list')

class travelrequestdelete(View):
	def get(request,self,id):
		TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(id=id).update(action=0,status='pending')
		messages.add_message(request,messages.SUCCESS,'Data Successfully Deleted')
		return redirect('website_travel_request_list')
		



class TravelClaimManagementTravelConveyanceTravelRequestAddView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/add_travel_request.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		form = TravelClaimManagementTravelConveyanceTravelRequestForm
		context = {
			'form': form
		}
		return render(request, self.template, context)

	def post(self, request):
		if request.method=="POST":
			other_relation = [int(p.split('_')[2]) for p in request.POST if 'other_name_' in p]
			other_relation.sort()
			for cer in other_relation:
				other_rela = TravelClaimManagementTravelConveyanceTravelRequest()
				other_rela.other_name_1 = request.POST.get('other_name_' + str(cer)).strip()
				other_rela.other_dob_1 = request.POST.get('other_dob_' + str(cer)).strip()
				other_rela.other_occupation_1 = request.POST.get('other_occupation_' + str(cer)).strip()
				other_rela.other_contact_number_1 = request.POST.get('other_contact_number_' + str(cer)).strip()
				other_rela.other_relationship_1 = request.POST.get('other_relationship_' + str(cer)).strip()
				other_rela.user_employee_id = get_id
				other_rela.save()
			form = TravelClaimManagementTravelConveyanceTravelRequestForm(request.POST)
			if form.is_valid():
				data = form.save()
				# data.user_id = request.user.id
				# data.save()
				messages.add_message(request, messages.SUCCESS, "Data added successfully.")
			else:
				messages.add_message(request, messages.WARNING, "Data already exists.")
			return redirect('website_travel_request_list')
###

###
class TravelClaimManagementTravelConveyanceTravelRequestStatusView(View):
    template = 'employee_website/employee_services/claim_and_reimbursement/travel_request_status_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(status='Pending').order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(added__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(added__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)
#1
###
class TravelClaimManagementTravelConveyanceTravelRequestStatusApprovedView(View):
    template = 'employee_website/employee_services/claim_and_reimbursement/travel_request_status_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(status='Approved').order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(added__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(added__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)

#11
###
class TravelClaimManagementTravelConveyanceTravelRequestStatusRejectedView(View):
    template = 'employee_website/employee_services/claim_and_reimbursement/travel_request_status_list.html'
    pagesize = 10
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('adminlogin')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = TravelClaimManagementTravelConveyanceTravelRequest.objects.filter(status='Rejected').order_by('-id')
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(added__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(added__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        	'responselistquery': report_paginate
    	}
        return render(request, self.template, context)








class TravelClaimManagementTravelConveyanceTravelRequestUpdateStatusView(View):
	template = 'employee_website/employee_services/claim_and_reimbursement/add_travel_request.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		instance = get_object_or_404(TravelClaimManagementTravelConveyanceTravelRequest, pk = id)
		form = TravelClaimManagementTravelConveyanceTravelRequestUpdateForm(instance = instance)
		context = {
			'form': form
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		instance = get_object_or_404(TravelClaimManagementTravelConveyanceTravelRequest, pk = id)
		form = TravelClaimManagementTravelConveyanceTravelRequestUpdateForm(request.POST, instance = instance)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
		return redirect('website_travel_request_list')


# Employee Advances 
class EmployeeAdvancesSubmitAdvanceRequestView(View):
	template = 'employee_website/employee_services/employee_advances/add_update_form.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': EmployeeAdvancesSubmitAdvanceRequestForm,
			'frm': True
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		# import pdb
		# pdb.set_trace()
		if request.method=='POST':
			form = EmployeeAdvancesSubmitAdvanceRequestForm(request.POST,request.FILES)
			if form.is_valid():
				form.save()
			messages.add_message(request, messages.SUCCESS, "Data added successfully.")
			return redirect('website_travel_advance_request_submit_request')
			
		else:
			messages.add_message(request, messages.WARNING, "Data already exists.")
			return redirect('website_travel_advance_request_submit_request')


		# ids = [int(p.split('_')[2]) for p in request.POST if 'advance_type_' in p]
		# ids.sort()
		# for data in ids:
		# 	save_data = EmployeeAdvancesSubmitAdvanceRequest()
		# 	save_data.advance_type_1_id = request.POST.get('advance_type_'+str(data))
		# 	save_data.advance_amount_1 = request.POST.get('advance_amount_'+str(data))
		# 	save_data.recovery_start_from_1 = request.POST.get('recovery_start_from_'+str(data))
		# 	save_data.justification_1 = request.POST.get('justification_'+str(data))
		# 	save_data.recovery_period_1 = request.POST.get('recovery_period_'+str(data))
		# 	save_data.advance_approved_1 = request.POST.get('advance_approved_'+str(data))
		# 	save_data.user_id = request.user.id
		# 	save_data.save()
		return redirect('website_travel_advance_request_submit_request')


class EmployeeAdvancesSubmitAdvanceRequestListView(View):
	template = 'employee_website/employee_services/employee_advances/list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		data_list = EmployeeAdvancesSubmitAdvanceRequest.objects.filter(action=1).order_by("-id")
		# data_list = EmployeeAdvancesSubmitAdvanceRequest.objects.filter(status='Processed').order_by("-id")
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)


# class EmployeePerquistesPerquisiteRequest(View):
# 	template = 'employee_website/employee_services/perquisite/perquisite_request.html'
# 	pagesize=10
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self,request,id=None):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		form = EmployeePerquistesRequestForm
# 		context={
# 			'form': form
# 		}
	
# 		return render(request,self.template,context)




class EmployeeAdvancesSubmitAdvanceRequestListApprovedAdvanceList(View):
	template = 'employee_website/employee_services/employee_advances/approved_advance.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		data_list = EmployeeAdvancesSubmitAdvanceRequest.objects.filter(action=0).order_by("-id")
		# data_list = EmployeeAdvancesSubmitAdvanceRequest.objects.filter(status='Processed').order_by("-id")
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)



class ApproveAdvance(View):
	def get(self,request,id=id):
		EmployeeAdvancesSubmitAdvanceRequest.objects.filter(id=id).update(action=1,action_status='Approved',today_date=date.today())
		return redirect('website_travel_advance_request_status_list')

class RejectAdvance(View):
	def get(self,request,id=id):
		EmployeeAdvancesSubmitAdvanceRequest.objects.filter(id=id).update(action=1,action_status='Rejected')
		return redirect('website_travel_advance_request_status_list')




class EmployeeAdvancesSubmitAdvanceRequestUpdateView(View):
	template = 'employee_website/employee_services/employee_advances/add_update_form.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
		form=EmployeeAdvancesSubmitAdvanceRequestUpdateStatusForm()
		return render(request, self.template, {"form":form})

	def post(self, request, id = None):
		
	
		if request.method=="POST":
			data = ''
			instance = get_object_or_404(EmployeeAdvancesSubmitAdvanceRequest, pk = id)
			form = EmployeeAdvancesSubmitAdvanceRequestUpdateStatusForm(request.POST, instance = instance)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data added successfully.")
			else:
				messages.add_message(request, messages.WARNING, "Data already exists.")
			if data.status == "Processing":
				return redirect('website_travel_advance_request_status_list')
			elif data.status == "Processed":
				return redirect('website_travel_advance_request_processed_list')
			else:
				return redirect('website_travel_advance_request_processing_list')


class EmployeeAdvancesSubmitAdvanceRequestProcessingListView(View):
	template = 'employee_website/employee_services/employee_advances/list_processing_list.html'
	pagesize = 10

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		data_list = EmployeeAdvancesSubmitAdvanceRequest.objects.filter( status ="Processing")
		report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
		context = {
			'responselistquery': report_paginate,
		}
		return render(request, self.template, context)


class EmployeeAdvancesSubmitAdvanceRequestProcessedListView(View):
    template = 'employee_website/employee_services/employee_advances/request_processed_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = EmployeeAdvancesSubmitAdvanceRequest.objects.filter( status ="Processed")
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(added__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(added__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(added__month = previous_month).order_by('-id')

        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        'responselistquery': report_paginate,
        }
        return render(request, self.template, context)

##11
# # Incentive &  Bonus
class IncentiveBonusUpdateIncentiveBonusAddView(View):
	template = 'employee_website/employee_services/incentive_bonus/update_incentive_bonus.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		form = EmployeeAdvanceSubmitIncentiveBonusForm()
		return render(request, self.template,{'form':form})
	def post(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		try:
			if 'upload_bulk_data' not in request.POST:
		
				form =EmployeeAdvanceSubmitIncentiveBonusForm(request.POST,request.FILES)
				if form.is_valid():
					form.save()
				messages.add_message(request, messages.SUCCESS, "Incentive bonus updated successfully.")
				return redirect('website_travel_incentive_bonus_add')
					
			else:
				excel_name_sheet = settings.MEDIA_URL+'upload_csv_file/'+ str(request.FILES['upload_bulk_data'])
				SaveCsvSheet.save_file(request, request.FILES['upload_bulk_data'], settings.MEDIA_URL + 'upload_csv_file')
				with open(excel_name_sexcel_name_sfilterheetfilterheet, 'r')as f:
					data = csv.reader(f)
					count = 0
					for row in data:
						if count !=0:
							try:
								save_data = EmployeeAdvancesSubmitIncentiveBonus()
								save_data.employee_id_id = row[0]
								save_data.incentive_type = row[1]
								save_data.incentive_period = row[2]
								save_data.incentive_amount = row[3]
								save_data.save()
							except:
								messages.add_message(request, messages.ERROR, "Something went wrong.")
								return redirect('crm_employee_services_payroll_update_advances_list')
						count +=1
			messages.add_message(request, messages.SUCCESS, "Incentive bonus updated successfully.")
			return redirect('website_travel_incentive_bonus_add')

		except:
			messages.add_message(request, messages.ERROR, " invalid data try again .")
			return redirect('website_travel_incentive_bonus_add')






class IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalListView(View):
    template = 'employee_website/employee_services/incentive_bonus/incentive_bonus_approval_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        data_list = EmployeeAdvancesSubmitIncentiveBonus.objects.filter(action=1).order_by("-id")
        report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
        context = {
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)


class TaxDeclarationUpdateTaxDeclaration(View):
	template = 'employee_website/employee_services/tax_declaration/update_tax_declaration.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(user_employee__employee_created_by_id__in  = get_users).order_by('-id')
		get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
		  'responselistquery': report_paginate
		}
		return render(request, self.template, context)

# class TaxDeclarationupdateotherincome(View):
# 	template = 'employee_website/employee_services/tax_declaration/update_income.html'
# 	pagesize=10
# 	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
# 	def get(self,request,id=id):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		form = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(id=id)
# 		context={
# 		'form':form
# 		}
# 		return redirect(request,self.template,context)

def TaxDeclarationupdateotherincome(request, id=id):

	company = get_object_or_404(EmployeeRegistrationUpdateRegistrationJoiningDetails, pk=id)	

	if request.method == "POST":

		data = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(id=id)
		if data.exists():
			form = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(id=id)

		else:
			form=EmployeeRegistrationUpdateRegistrationJoiningDetails(id=id)
		form.joining_location=data[0].joining_location
		form.income_type=request.POST.get('income_type')
		form.gross_total_income=request.POST.get('gross_total_income')
		form.deduction=request.POST.get('deduction')
		form.net_taxable_income=request.POST.get('net_taxable_income')
		form.upload_document=request.FILES['upload_document']
		form.save()
		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(id=id).update(submission_date=date.today())
		return redirect('hcm_update_tax_declaration')

	else:
		form = TaxDeclarationUpdateIncome(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/tax_declaration/update_income.html', context)


def TaxDeclarationExemption(request, id=id):

	company = get_object_or_404(EmployeeRegistrationUpdateRegistrationJoiningDetails, pk=id)	

	if request.method == "POST":

		data = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(id=id)
		if data.exists():
			form = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.get(id=id)

		else:
			form=EmployeeRegistrationUpdateRegistrationJoiningDetails(id=id)
		form.tax_declaration_type=request.POST.get('tax_declaration_type')
		form.exemption_type=request.POST.get('exemption_type')
		form.tax_rule=request.POST.get('tax_rule')
		form.maxmimum_limit=request.POST.get('maxmimum_limit')
		form.exemption_amount=request.POST.get('exemption_amount')
		form.upload_document_1=request.FILES['upload_document_1']
		form.save()
		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(id=id).update(submission_date=date.today())
		return redirect('hcm_update_tax_declaration')

	else:
		form = TaxDeclarationExemptionform(instance=company)
		context= {
            'form': form
        }
		return render(request, 'employee_website/employee_services/tax_declaration/update_income.html', context)


class TaxDeclarationApprovalAll(View):
	template = 'employee_website/employee_services/tax_declaration/tax_declaration_approval.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(user_employee__employee_created_by_id__in  = get_users).order_by('-id')
		get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(tax_declaration_status=0).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
		  'responselistquery': report_paginate
		}
		return render(request, self.template, context)



class TaxDeclarationApprovalDisplay(View):
	template = 'employee_website/employee_services/tax_declaration/tax_declaration_display.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(user_employee__employee_created_by_id__in  = get_users).order_by('-id')
		get_report = EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.filter(tax_declaration_status=1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
		  'responselistquery': report_paginate
		}
		return render(request, self.template, context)

class TaxDeclarationApprove(View):
	def get(self, request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.update(tax_declaration_status=1,status='Approved',approve_date=date.today())
		return redirect('tax_declaration_display')

# class TaxDeclarationApprove(View):
# 	def get(self, request,id=id):
# 		if not request.user.is_authenticated:
# 			return redirect('index')
# 		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.update(tax_declaration_status=1,status='Rejected')
# 		return redirect('tax_declaration_display')

class TaxDeclarationReject(View):
	def get(self, request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.update(tax_declaration_status=1,status='Rejected',approve_date=date.today())
		return redirect('tax_declaration_display')

class TaxDeclarationDelete(View):
	def get(self, request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeRegistrationUpdateRegistrationJoiningDetails.objects.update(tax_declaration_status=0)
		return redirect('tax_declaration_display')







class IncomeTaxCalculation(View):
	template='employee_website/employee_services/tax_declaration/tax_calculation.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)

	def get(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		form=IncomeTaxCalculationForm()
		context ={
			'form':form
		}

		return render(request,self.template,context)
	def post(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		form=IncomeTaxCalculationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
		return redirect('income_tax_calculation_display')


class IncomeTaxCalculationDisplay(View):
	template='employee_website/employee_services/tax_declaration/tax_calculation_display.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)

	def get(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.all().order_by('-id')
		context ={
			'responselistquery':responselistquery
		}

		return render(request,self.template,context)


class IncomeTaxApproval(View):
	template='employee_website/employee_services/tax_declaration/income_tax_approval.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.filter(tax_approve_action=1)
		context={
			'responselistquery':responselistquery
		}
		return render(request,self.template,context)
class IncomeTaxApprovalall(View):
	template='employee_website/employee_services/tax_declaration/income_tax_approval_all.html'
	def get(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.filter(tax_approve_action=0)
		context={
			'responselistquery':responselistquery
		}
		return render(request,self.template,context)


class IncomeTaxActionApprove(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(tax_approve_action=1,tax_approve_status='Approved',approved_date=date.today())
		return redirect('income_tax_approval')

class IncomeTaxActionRejected(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(tax_approve_action=1,tax_approve_status='Rejected',approved_date=date.today())
		return redirect('income_tax_approval')



class IncomeTaxDisplayActionDelete(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(tax_approve_action=0)
		return redirect('income_tax_approval')

class OtherrecoveryUpdateRecoverydisplay(View):
	template='employee_website/employee_services/tax_declaration/update_recovery_display.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.all()
		context={
			'responselistquery':responselistquery
		}
		return render(request,self.template,context)


class OtherrecoveryUpdateRecovery(View):
	template='employee_website/employee_services/tax_declaration/update_recovery.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		form=EmployeeOtherRecoveryUpdateRecoveryForm()
		context={
			'form':form
		}
		return render(request,self.template,context)
	def post(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		form=EmployeeOtherRecoveryUpdateRecoveryForm(request.POST)
		if form.is_valid():
			form.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
		return redirect('other_recovery_update_recovery')





class OtherrecoveryRecoveryApprovalDisplay(View):
	template='employee_website/employee_services/tax_declaration/other_recovery_approval_display.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.filter(recovery_approval_action=1)
		context={
			'responselistquery':responselistquery
		}
		return render(request,self.template,context)



class OtherrecoveryRecoveryApproval(View):
	template='employee_website/employee_services/tax_declaration/other_recovery_approval.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self,request):
		if not request.user.is_authenticated:
			return redirect('index')
		responselistquery=EmployeeIncomeTaxCalculation.objects.filter(recovery_approval_action=0)
		context={
			'responselistquery':responselistquery
		}
		return render(request,self.template,context)



class Otherrecoveryactionapproval(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(recovery_approval_action=1,recovery_approval_status='Accepted',approved_date=date.today())
		return redirect('other_recovery_recovey_approval_display')

class Otherrecoveryactionrejected(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(recovery_approval_action=1,recovery_approval_status='Rejected',approved_date=date.today())
		return redirect('other_recovery_recovey_approval_display')


class Otherrecoveryactiondelete(View):
	def get(self,request,id=id):
		if not request.user.is_authenticated:
			return redirect('index')
		EmployeeIncomeTaxCalculation.objects.filter(id=id).update(recovery_approval_action=0)
		return redirect('other_recovery_recovey_approval_display')



class IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalListApprovedIncentive(View):
    template = 'employee_website/employee_services/incentive_bonus/incentive_approved_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')
        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        data_list = EmployeeAdvancesSubmitIncentiveBonus.objects.filter(action=0).order_by("-id")
        report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
        context = {
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)

class IncentiveApproved(View):
	def get(self , request,id=id):
		EmployeeAdvancesSubmitIncentiveBonus.objects.filter(id=id).update(action=1,action_status='Approved',today_date=date.today())

		return redirect('website_incentive_bonus_status_processing_list')


class IncentiveRejected(View):
	def get(self , request,id=id):
		EmployeeAdvancesSubmitIncentiveBonus.objects.filter(id=id).update(action=1,action_status='Reject',today_date=date.today())

		return redirect('website_incentive_bonus_status_processing_list')


class IncentiveDelete(View):
	def get(self , request,id=id):
		EmployeeAdvancesSubmitIncentiveBonus.objects.filter(id=id).update(action=0)

		return redirect('website_incentive_bonus_status_processing_list')




#11
class IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalUpdateView(View):
	template = 'employee_website/employee_services/employee_advances/add_update_form.html'
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		instance = get_object_or_404(EmployeeAdvancesSubmitIncentiveBonus, pk = id)
		context = {
            'form': EmployeeAdvancesSubmitIncentiveBonusUpdateStatusForm(instance = instance),
        }
		return render(request, self.template, context)
	def post(self, request, id = None):
		data = ''
		
		instance =get_object_or_404(EmployeeAdvancesSubmitIncentiveBonus, pk=id)
		form = EmployeeAdvancesSubmitIncentiveBonusUpdateStatusForm(request.POST, instance = instance)
		if form.is_valid():
			form.save()
			messages.add_message(request,messages.SUCCESS,"Data added successfully")
			return redirect('website_travel_incentive_bonus_status_list')
		else:
			messages.add_message(request,messages.WARNING, "Data already exists")
		if data.status=="Pending":
			return redirect('website_travel_incentive_bonus_status_list')
		elif data.status=="Processing":
			return redirect('website_incentive_bonus_status_processing_list')
		elif data.status =="Processed":
			return redirect('website_incentive_bonus_status_processed_list')
		else:
			return redirect('website_travel_incentive_bonus_status_list')


	
   

class IncentiveBonusUpdateIncentiveBonusIncentiveBonusProcessingListView(View):
    template = 'employee_website/employee_services/incentive_bonus/incentive_bonus_processing_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        data_list = EmployeeAdvancesSubmitIncentiveBonus.objects.filter( status ="Processing").order_by("-id")
        report_paginate = CommonPagination.paginattion(request, data_list, self.pagesize)
        context = {
            'responselistquery': report_paginate,
        }
        return render(request, self.template, context)


class IncentiveBonusUpdateIncentiveBonusIncentiveBonusProcessedListView(View):
    template = 'employee_website/employee_services/incentive_bonus/incentive_bonus_processed_list.html'
    pagesize = 10

    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request, id = None):
        if not request.user.is_authenticated:
            return redirect('index')

        get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
        get_data = EmployeeAdvancesSubmitIncentiveBonus.objects.filter( status ="Processed").order_by("-id")
        filter_type = request.GET.get('filter')
        if str(filter_type) == "1":
            today = date.today()
            get_data = get_data.filter(updated__date = today).order_by('-id')
        elif str(filter_type) == "2":
            current_month = datetime.now().month
            get_data = get_data.filter(updated__month = current_month).order_by('-id')
        elif str(filter_type) == "3":
            previous_month = datetime.now().month - 1
            get_data = get_data.filter(updated__month = previous_month).order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
        context = {
        'responselistquery': report_paginate,
        }
        return render(request, self.template, context)


# WEBSITE >>>>>>>>>>>>>>>>> Knowledge and Training
class KnowledgeandTrainingUpdateDocumentsView(View):
	template = 'know_and_training/update_dcuments.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KnowledgeandTrainingUpdateDocumentsForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if id is None:
			form = KnowledgeandTrainingUpdateDocumentsForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				data.user_id = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		else:
			data = get_object_or_404(KnowledgeandTrainingUpdateDocuments,  pk=id)
			form = KnowledgeandTrainingUpdateDocumentsForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, "Something went wrong.")
		return redirect('crm_knowledgeandtraining_update_documents_view')


class KnowledgeandTrainingUpdateTrainingView(View):
	template = 'know_and_training/update_training.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': CrmManageProductTrainingModelForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = CrmManageProductTrainingModelForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
		else:
			messages.add_message(request, messages.ERROR, form.errors)
		return redirect('crm_knowledgeandtraining_update_training_view')


class KnowledgeandTrainingUpdatePromotionsView(View):
	template = 'know_and_training/update_pramotion.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': CrmManageProductPromotionsModelForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		form = CrmManageProductPromotionsModelForm(request.POST, request.FILES)
		if form.is_valid():
			data = form.save()
			data.user_id = request.user.id
			data.save()
			messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
		else:
			messages.add_message(request, messages.ERROR, form.errors)
		return redirect('crm_knowledgeandtraining_update_promotions_view')


class KnowledgeandTrainingKnowledgeSharingView(View):
	template = 'know_and_training/knowledge_sharing.html'

	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		context = {
			'form': KnowledgeandTrainingKnowledgeSharingForm,
		}
		return render(request, self.template, context)

	def post(self, request, id = None):
		if id is None:
			form = KnowledgeandTrainingKnowledgeSharingForm(request.POST, request.FILES)
			if form.is_valid():
				data = form.save()
				data.user_id = request.user.id
				data.save()
				messages.add_message(request, messages.SUCCESS, "Data added Successfully.")
			else:
				messages.add_message(request, messages.ERROR, form.errors)
		else:
			data = get_object_or_404(KnowledgeandTrainingKnowledgeSharing,  pk=id)
			form = KnowledgeandTrainingKnowledgeSharingForm(request.POST, request.FILES, instance = data)
			if form.is_valid():
				data = form.save()
				messages.add_message(request, messages.SUCCESS, "Data updated Successfully.")
			else:
				messages.add_message(request, messages.ERROR, form.errors)
		return redirect('crm_knowledgeandtraining_update_knowledge_sharing')


class KnowledgeandTrainingUpcomingTraningListView(View):
	template = 'know_and_training/up_coming_training_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = ManageKnowledgeProductTraining.objects.filter(user_id__in = get_users, is_active = True, start_date__gt = date.today()).order_by('-id')
		get_report = ManageKnowledgeProductTraining.objects.filter( is_active = True).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class KnowledgeandTrainingCurrentTraningListView(View):
	template = 'know_and_training/current_training_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = ManageKnowledgeProductTraining.objects.filter( is_active = True).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class KnowledgeandTrainingPastraningListView(View):
	template = 'know_and_training/past_traning_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = ManageKnowledgeProductTraining.objects.filter( is_active = True, training_calander = date.today()).order_by('-id')
		get_report = ManageKnowledgeProductTraining.objects.filter( is_active = True).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class KnowledgeandTrainingRequestReceivedForTrainignListView(View):
	template = 'know_and_training/request_received_for_traning_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_report = ManageProductTrainingSendWishToAttend.objects.filter(status = 1).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class KnowledgeandTrainingCurrentPromotionsListView(View):
	template = 'know_and_training/current_promotions_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		today_date =  date.today()
		get_report = ManageKnowledgeProductPromotions.objects.filter( is_active = True).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)
###update
class KnowledgeandTrainingCurrentPromotionsUpdateView(View):
	template= 'know_and_training/current_promotions_update.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store =True)
	def get(self,request,id=None):
		if not request.user.is_authenticated:
			return redirect('index')
		form = GetAndManageHierarchyOfEmployeeForm()
		context ={
			'form' :form
			
		}
		return render(request,self.template,context)
#!
#2
	def post(self,request, id):
		if not request.user.is_authenticated:
			return render('index')
		
		try:
			get_data = get_object_or_404(ManageKnowledgeProductPromotions, pk=id)
			form = GetAndManageHierarchyOfEmployeeForm(request.POST,instance= get_data)
			if form.is_valid():
				form.save()
				messages.add_message(request,messages.SUCCESS,"Data added successfully")
			else:
				messages.add_message(request,messages.WARNING,"Data already exists")
			return redirect('crm_knowledgeandtraining_update_current_promotions_list')
		
		except:
			messages.add_message(request,messages.WARNING,"Something went wrong.")
			return redirect('crm_knowledgeandtraining_update_current_promotions_list')



class KnowledgeandTrainingUpcomingPromotionsListView(View):
	template = 'know_and_training/up_coming_pramotions_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		today_date =  date.today()
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = ManageKnowledgeProductPromotions.objects.filter( is_active = True, start_date__gt = date.today()).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class KnowledgeandTrainingPastPromotionsListView(View):
	template = 'know_and_training/past_promotions_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		today_date =  date.today()
		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		# get_report = ManageKnowledgeProductPromotions.objects.filter(is_active = True, start_date__lt = date.today()).order_by('-id')
		get_report = ManageKnowledgeProductPromotions.objects.filter(is_active = True).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class TrainingAttendListView(View):
	template = 'know_and_training/traning_attend_list.html'
	pagesize = 10
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')

		get_users = GetAndManageHierarchyOfEmployee.Employee_list(request)
		get_report = ManageProductTrainingSendWishToAttend.objects.all().order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		context = {
			'responselistquery': report_paginate
		}
		return render(request, self.template, context)


class send_request_to_for_attend_traning(View):
    def post(self, request):
	    if not request.user.is_authenticated:
	        return redirect('index')
	    if request.is_ajax:
	        try:
	            get_report = ManageProductTrainingSendWishToAttend.objects.get(traning_id_id = request.POST['id'], user_id = request.user.id)
	            data = ''
	        except:
	            save_dat = ManageProductTrainingSendWishToAttend()
	            save_dat.traning_id_id = request.POST['id']
	            save_dat.user_id = request.user.id
	            save_dat.save()
	            data = '1'
	        return JsonResponse({'data': data})
	    else:
	        return redirect('index')


class ApprovalVacancies(View):
	
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id, stauts_id, menu_level):
		if not request.user.is_authenticated:
			return redirect('index')

		if int(menu_level) == 1:
			get_report = EmployeeServicesRecruitementCreateRequirement.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_website_employeeservices_recruitement_approvevacancies_list")
		elif int(menu_level) == 2:
			get_report = CrmUserLoginApiLogs.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_attendance_status")
		elif int(menu_level) == 3:
			get_report = OvertimeManagementUpdateOvertime.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("website_edit_update_over_time_status_list")
		elif int(menu_level) == 4:
			get_report = TravelClaimManagementTravelConveyanceTravelRequest.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
		elif int(menu_level) == 5:
			get_report = EmployeeClaimandReimbursementSubmitClaims.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_claimandreimbursement_claim_claimprocessed_list")
		elif int(menu_level) == 6:
			get_report = EmployeeClaimandReimbursementSubmitReimbursement.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_reimbursementprocessed_list")
		elif int(menu_level) == 7:
			get_report = EmployeeAdvancesSubmitAdvanceRequest.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("website_travel_advance_request_processed_list")
		elif int(menu_level) == 8:
			get_report = EmployeeAdvancesSubmitIncentiveBonus.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("website_incentive_bonus_status_processed_list")
		elif int(menu_level) == 9:
			get_report = EmployeeHRPoliciesUpdatePolicies.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_hrpolicies_upload_update_policies_list")
		elif int(menu_level) == 10:
			get_report = EmployeeHrPoliciesUpdateCirculars.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_hrpolicies_upload_update_circulars_list")
		elif int(menu_level) == 11:
			get_report = EmployeeHRPoliciesUpdateForm.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_hrpolicies_upload_update_forms_list")
		elif int(menu_level) == 12:
			get_report = CrmManageProductTraining.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_knowledgeandtraining_update_current_traning_list")
		elif int(menu_level) == 13:
			get_report = CrmManageProductPromotions.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_knowledgeandtraining_update_current_promotions_list")
		elif int(menu_level) == 14:
			get_report = PayrollStatutoryDeductions.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_crmemployee_manageemployee_statutorydeductions_list")
		elif int(menu_level) == 15:
			get_report = PayrollSalaryVoucher.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_crmemployee_manageemployee_salaryvoucher_list")
		elif int(menu_level) == 16:
			get_report = PayrollSalaryDisbursement.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_crmemployee_manageemployee_salarydisbursement_list")
		elif int(menu_level) == 17:
			get_report = EmployeePayrollProcessingUpdateRecoveries.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_payroll_update_recovery_list")
		elif int(menu_level) == 18:
			get_report = EmployeePayrollProcessingUpdateTaxDeclaration.objects.get(id = id)
			data_append = get_report.approval_level_all_status+','+stauts_id
			get_report.approval_level_all_status = data_append.lstrip(',')
			get_report.approval_level_id  = stauts_id
			get_report.save()
			return redirect("crm_employee_services_payroll_tax_declaration_list")


#######



class Datapost(View):
    template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'

    def get(self,request):
        form = EmployeeServicesRecruitementPublishVacanciesForm()
        context = {'form': form}
        return render(request, self.template, context)            


    def post(self, request):
        form = EmployeeServicesRecruitementPublishVacanciesForm(request.POST, request.FILES)
        if form.is_valid():             
            messages.add_message(request, messages.SUCCESS,('Successfully added!! ')) 
            form.save()   
        else:
            messages.add_message(request, messages.WARNING,('Data already exists!!'))
        return redirect('crm_website_employeeservices_recruitement_publishvacancies_update')

class Datapost1(View):
    template = 'employee_website/employee_services/recruitement/add_edit_create_requirement.html'

    def get(self,request):
        form = EmployeeServicesRecruitementInviteResumeAddForm1()
        context = {'form': form}
        return render(request, self.template, context)            


    def post(self, request):

        form = EmployeeServicesRecruitementInviteResumeAddForm1(request.POST, request.FILES)
		
        if form.is_valid(): 
			           
            messages.add_message(request, messages.SUCCESS,('Successfully added!! ')) 
            form.save()   
        else:
            messages.add_message(request, messages.WARNING,('Data already exists!!'))
        return redirect('crm_website_employeeservices_recruitement_publishvacancies_update')

###

##
class EmployeeHolidaysAndLeavesList(View):
    template = 'employee_website/employee_services/leaves/manage_manage_holidays_list.html'
    pagesize = 10
    
    @cache_control(no_cache=True, must_revalidate=True, no_store=True)
    def get(self, request):
        if not request.user.is_superuser:
            return redirect('adminlogin')
        get_report = ManageHolidays.objects.all().order_by('-id')
        report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
        return render(request, self.template,{'responselistquery': report_paginate})


class AddEmployeeHolidaysAndLeaves(View):
    template = 'employee_website/employee_services/leaves/add_manage_holidays_leaves.html'
    
    def get(self,request):
        form = ManageHolidaysForm()
        context = {'form': form}
        return render(request, self.template, context)            


    def post(self, request, branch_id = None):
        form = ManageHolidaysForm(request.POST, request.FILES)
        if form.is_valid():             
            messages.add_message(request, messages.SUCCESS,('Successfully added!! ')) 
            form.save()   
        else:
            messages.add_message(request, messages.WARNING,('Data already exists!!'))
        return redirect('EmployeeHolidaysAndLeaveslist')

def AddEditEmployeeHolidaysAndLeaves(request, id):

    manageproduct = get_object_or_404(ManageHolidays, pk=id)
    if request.method == "POST":
        form =ManageHolidaysForm(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('EmployeeHolidaysAndLeaveslist')
    else:
        form = ManageHolidaysForm(instance=manageproduct)
    return render(request,  'employee_website/employee_services/leaves/add_manage_holidays_leaves.html', {'form': form})


class EmployeeHolidaysAndLeavesDelete(View):
    def get(self, request, id):
        if not request.user.is_superuser:
            return redirect('adminlogin')
        get_report = ManageHolidays.objects.filter(id = id).delete()
        messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
        return redirect('EmployeeHolidaysAndLeaveslist')


# payroll_processed_list.html
       
def EmployeePayrollProcessedAddView(request):

	form = EmployeePayrollProcessedForm()
	if request.method=="POST":
		form = EmployeePayrollProcessedForm(request.POST)
		print(form.errors)
		if form.is_valid(): 
			form.save() 
			print(form)           
			messages.add_message(request, messages.SUCCESS,('Successfully added!! ')) 
			return redirect('crm_crmemployee_manageemployee_payrollprocessed_add')   
		else:
			messages.add_message(request, messages.WARNING,('Invalid Data !!'))
			return redirect('crm_crmemployee_manageemployee_payrollprocessed_add') 
	return render(request,'employee_website/employee_services/payroll/payroll_processed_add.html',{'form':form})

##
##
##
##

class EmployeePayrollProcessedListView(View):
	template = 'employee_website/employee_services/payroll/payroll_processed_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		# if not request.user.is_authenticated:
		# 	return redirect('index')

		
		# get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		# get_data = UserLoginApiLogs.objects.filter(status='Approved').order_by('-id')
		# filter_type = request.GET.get('filter')
		# if str(filter_type) == "1":
		# 	today = date.today()
		# 	get_data = get_data.filter(date_of_payment = today).order_by('-id')
		# elif str(filter_type) == "2":
		# 	current_month = datetime.now().month
		# 	get_data = get_data.filter(date_of_payment = current_month).order_by('-id')
		# elif str(filter_type) == "3":
		# 	previous_month = datetime.now().month - 1
		# 	get_data = get_data.filter(date_of_payment = previous_month).order_by('-id')
		# report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
		# context = {
        #     'responselistquery': report_paginate,
		# 	'get_bank':get_bank,
		# 	}
		# return render(request, self.template,context)
		get_all_user_ids = UserLoginApiLogs.objects.filter(attendance_status=2).order_by("-id")
		
		get_all_data  = ManageWorkingDays.objects.all().order_by('-id')  
		get_financial_year = ManageHolidays.objects.all().order_by('-id')
		get_leave_type = HolidaysandLeavesLeaveType.objects.all().order_by('-id')
		get_claim_type = ManageClaimType.objects.all().order_by('-id')
		get_reimbursement = ManageReimbursement.objects.all().order_by('-id')
		get_incentive = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by('-id')[:1]
		get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		get_pancard = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.all().order_by('-id')[:1]
		# get_processing = EmployeePayrollProcessed.objects.all().order_by('-id')[:1]
		

		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'get_all_data':get_all_data,
			'get_financial_year':get_financial_year,
			'stauts': ATTENDENCE_STATUS,
			'get_leave_type':get_leave_type,
			'get_claim_type':get_claim_type,
			'get_reimbursement':get_reimbursement,
			'get_incentive':get_incentive,
			'get_bank':get_bank,
			'get_pancard':get_pancard,
			# 'get_processing':get_processing,

			# 'get_monthly_holidays_days':get_monthly_holidays_days,
		
		}
		return render(request, self.template,context)



class EmployeePayrollProcessedPendingListView(View):
	template = 'employee_website/employee_services/payroll/payroll_processed_pending_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_data = EmployeePayrollProcessed.objects.all().order_by('-id')
		filter_type = request.GET.get('filter')
		if str(filter_type) == "1":
			today = date.today()
			get_data = get_data.filter(date_of_payment = today).order_by('-id')
		elif str(filter_type) == "2":
			current_month = datetime.now().month
			get_data = get_data.filter(date_of_payment = current_month).order_by('-id')
		elif str(filter_type) == "3":
			previous_month = datetime.now().month - 1
			get_data = get_data.filter(date_of_payment = previous_month).order_by('-id')
		report_paginate = CommonPagination.paginattion(request, get_data, self.pagesize)
		context = {
            'responselistquery': report_paginate
			}
		return render(request, self.template, context)


def EmployeePayrollProcessedListViewUpdate(request, id):

    manageproduct = get_object_or_404(EmployeePayrollProcessed, pk=id)
    if request.method == "POST":
        form =EmployeePayrollProcessedFormUpdate(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_crmemployee_manageemployee_payrollprocessed_list')
    else:
        form = EmployeePayrollProcessedFormUpdate(instance=manageproduct)
    return render(request,  'employee_website/employee_services/payroll/payroll_processed_update.html',{'form':form})


class EmployeePayrollProcessedListViewDelete(View):
    def get(self, request, id):
        if not request.user.is_superuser:
            return redirect('adminlogin')
        get_report = EmployeePayrollProcessed.objects.filter(id = id).delete()
        messages.add_message(request, messages.SUCCESS, "Data deleted Successfully.")
        return redirect('crm_crmemployee_manageemployee_payrollprocessed_list')
###
class EmployeePayrollstatusListView(View):
	template = 'employee_website/employee_services/payroll/payroll_status_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request):
		if not request.user.is_superuser:
			return redirect('adminlogin')
		# get_report = EmployeePayrollProcessed.objects.all().order_by('-id')
		
		# report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		# get_current_month = date.today().month
		# get_all_user_ids = UserLoginApiLogs.objects.filter(attendance_status=2).order_by("-id")
		
		# get_all_data  = ManageWorkingDays.objects.all().order_by('-id')  
		# get_financial_year = ManageHolidays.objects.all().order_by('-id')
		# get_leave_type = HolidaysandLeavesLeaveType.objects.all().order_by('-id')
		# get_claim_type = EmployeeClaimandReimbursementSubmitClaims.objects.all().order_by('-id')
		# get_reimbursement = ManageReimbursement.objects.all().order_by('-id')
		# get_incentive = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by('-id')[:1]
		# get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		
		
		
	
		# report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		# context = {
		# 	'responselistquery': report_paginate,
		# 	'get_all_data':get_all_data,
		# 	'get_financial_year':get_financial_year,
		# 	'stauts': ATTENDENCE_STATUS,
		# 	'get_leave_type':get_leave_type,
		# 	'get_claim_type':get_claim_type,
		# 	'get_reimbursement':get_reimbursement,
		# 	'get_incentive':get_incentive,
		# 	'get_bank':get_bank,
			
		# 	# 'get_monthly_holidays_days':get_monthly_holidays_days,
		# }
		# return render(request, self.template,context)
		get_all_user_ids = UserLoginApiLogs.objects.all().order_by("-id")
		
		get_all_data  = ManageWorkingDays.objects.all().order_by('-id')  
		get_financial_year = ManageHolidays.objects.all().order_by('-id')
		get_leave_type = HolidaysandLeavesLeaveType.objects.all().order_by('-id')
		get_claim_type = ManageClaimType.objects.all().order_by('-id')
		get_reimbursement = ManageReimbursement.objects.all().order_by('-id')
		get_incentive = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by('-id')[:1]
		get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		get_pancard = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.all().order_by('-id')[:1]
		# get_processing = EmployeePayrollProcessed.objects.all().order_by('-id')[:1]
		

		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'get_all_data':get_all_data,
			'get_financial_year':get_financial_year,
			'stauts': ATTENDENCE_STATUS,
			'get_leave_type':get_leave_type,
			'get_claim_type':get_claim_type,
			'get_reimbursement':get_reimbursement,
			'get_incentive':get_incentive,
			'get_bank':get_bank,
			'get_pancard':get_pancard,
			# 'get_processing':get_processing,

			# 'get_monthly_holidays_days':get_monthly_holidays_days,
		
		}
		return render(request, self.template,context)



class EmployeePayrollProcessingListView(View):
	template = 'employee_website/employee_services/payroll/payroll_processing_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request, id = None):
		if not request.user.is_authenticated:
			return redirect('index')
		
		get_all_user_ids = UserLoginApiLogs.objects.filter(attendance_status=2).order_by("-id")
		location = request.GET.get('location')
		month_and_year = request.GET.get('login_time')
		if  location != None and str(location) != "":
			get_all_user_ids = get_all_user_ids.filter(location=str(location).strip())
			
		if month_and_year != None and str(month_and_year) != "":
			get_all_user_ids = get_all_user_ids.filter(month_and_year =str(month_and_year).strip())
		
		
		get_all_user_ids = UserLoginApiLogs.objects.filter(attendance_status=2).order_by("-id")
		
		get_all_data  = ManageWorkingDays.objects.all().order_by('-id')  
		get_financial_year = ManageHolidays.objects.all().order_by('-id')
		get_leave_type = HolidaysandLeavesLeaveType.objects.all().order_by('-id')
		get_claim_type = ManageClaimType.objects.all().order_by('-id')
		get_reimbursement = ManageReimbursement.objects.all().order_by('-id')
		get_incentive = EmployeeAdvancesSubmitIncentiveBonus.objects.all().order_by('-id')[:1]
		get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		get_pancard = EmployeeRegistrationUpdateRegistrationPersonalDetails.objects.all().order_by('-id')[:1]
		
		get_amount_offer = EmployeeRegistrationUpdateSalaryStructutre.objects.all().order_by('-id')[:1]
		
		print(get_amount_offer)
		get_processing = EmployeePayrollProcessed.objects.all().order_by('-id')[:1]
		

		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'get_all_data':get_all_data,
			'get_financial_year':get_financial_year,
			'stauts': ATTENDENCE_STATUS,
			'get_leave_type':get_leave_type,
			'get_claim_type':get_claim_type,
			'get_reimbursement':get_reimbursement,
			# 'get_incentive':get_incentive,
			'get_bank':get_bank,
			# 'get_pancard':get_pancard,
			# 'get_amount_offer':get_amount_offer,

			'get_processing':get_processing,

			# 'get_monthly_holidays_days':get_monthly_holidays_days,
		
		}
		return render(request, self.template,context)





def EmployeePayrollStatusListViewUpdate(request, id):

    manageproduct = get_object_or_404(EmployeePayrollProcessed, pk=id)
    if request.method == "POST":
        form =EmployeePayrollProcessedFormUpdate(request.POST, instance=manageproduct)
        if form.is_valid():
            form.save()
            return redirect('crm_crmemployee_manageemployee_payrollprocessed_list')
    else:
        form = EmployeePayrollProcessedFormUpdate(instance=manageproduct)
    return render(request,  'employee_website/employee_services/payroll/payroll_processed_update.html',{'form':form})

def EmployeesalarySlipAddView(request):
	form = EmployeesalarySlipForm()
	if request.method=='POST':
		form = EmployeesalarySlipForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('EmployeePayrollSlipListView')
		 


class EmployeePayrollSlipListView(View):
	template = 'employee_website/employee_services/payroll/payroll_salary_slip_list.html'
	pagesize = 10
	@cache_control(no_cache=True, must_revalidate=True, no_store=True)
	def get(self, request,id=None):
		if not request.user.is_superuser:
			return redirect('adminlogin')
		# get_report = EmployeePayrollProcessed.objects.filter(id=id)
		# get_report2= CompanySetup.objects.all().order_by('-id')[:1]
		# get_report3= ManageSalary.objects.all().order_by('-id')[:1]
		
		# report_paginate = CommonPagination.paginattion(request, get_report, self.pagesize)
		# return render(request, self.template,{'responselistquery': report_paginate ,'get_report2':get_report2,'get_report3':get_report3})
		get_current_month = date.today().month
		get_all_user_ids = UserLoginApiLogs.objects.filter(attendance_status=2).order_by("-id")
		get_bank = EmployeeRegistrationUpdateBankDetails.objects.all().order_by('-id')[:1]
		get_report2= CompanySetup.objects.all().order_by('-id')[:1]
		get_report3= ManageSalary.objects.all().order_by('-id')[:1]
		get_all_data  = ManageWorkingDays.objects.all().order_by('-id')
		get_financial_year = ManageHolidays.objects.all().order_by('-id')
	
		report_paginate = CommonPagination.paginattion(request, get_all_user_ids, self.pagesize)
		context = {
			'responselistquery': report_paginate,
			'get_all_data':get_all_data,
			'get_financial_year':get_financial_year,
			'stauts': ATTENDENCE_STATUS,
			'get_report2':get_report2,			
			'get_report3':get_report3,
			'get_bank':get_bank,
			# 'get_monthly_holidays_days':get_monthly_holidays_days,
		}
		return render(request, self.template, context)