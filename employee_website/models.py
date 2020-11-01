from datetime import datetime 
from django.db import models
from django.conf import settings
from hrms_management.models import *
from hrms_employees.models import *
from knowleage_tranning.models import *

# Create your models here.
class EmployeeServicesRecruitementUpdateConsultantsDetails(models.Model):
    name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    constitution = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Constitution")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_services_recruitement_update_consultants_details"
#


AGENCY_TYPE = (
    ('Consultant', 'Consultant'),
    ('Hospital', ' Hospital'),
    ('Verification Agent', 'Verification Agent'),
    ('Field Agent', 'Field Agent'),
)

class EmployeeServicesRecruitementUpdateConsultants(models.Model):
    
    name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    contact_person_name=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    constitution = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Constitution")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    correspondance_address = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = " Address")
    building = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Building")
    block = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Block")
    sector = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Sector")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="City")
    district = models.CharField(max_length=200,default='', verbose_name="District")
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="State")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,  verbose_name="Country")
    zip_code = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pin code")
    cin_number = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "CIN Number")
    date_of_incorporation = models.DateField(blank = True, null = True, verbose_name = "Incorporation Date ")
    pan_card = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pan Card")
    tan_no = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "TAN Number")

    gst_registration = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "GST Registration")
    contact_person  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Person")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    designations = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Designation")
    mobile_number  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Mobile Number")
    mail_id  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Mail id")
    services_offered  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Services Offered")
    branches  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Branches")
    experience  = models.CharField(default='', blank=True, null=True, max_length=100,verbose_name = "Experience")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)
    agency_type = models.CharField(choices=AGENCY_TYPE,max_length=50,blank=True,null=True,verbose_name='Agency Type')
    employee_strength=models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Employee Strength')
    facilities_available=models.CharField(default='',blank=True,null=True,max_length=400,verbose_name='facilities Available')
    licence_no=models.CharField(default='',blank=True,null=True,max_length=400,verbose_name='Licence Number')
    date=models.DateField(blank = True, null = True, verbose_name = "date")
    class Meta:
        db_table = "employee_services_recruitement_update_consultants"


EMPLOYEE_VACANCIES_STATUS = (
    (1, 'Request Received'),
    (2, 'Recommended'),
    (3, 'Recommended By HR'),
    (4, 'Approved'),
)


EMPLOYEE_MODE_OF_PUBLISHING = (
    ('Consultant', 'Consultant'),
    ('On Website', 'On Website'),
    ('Social Media', 'Social Media'),
    ('Local News Paper', 'Local News Paper'),
    ('E News', 'E News'),
    ('Job Portals','Job Portals')
)


STATUS_CHOICE = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    ('Expired', 'Expired'),
    ('Withdraw','Withdraw'),
)

Urgency_CHOICE = (
    ('With in 15 days', 'With in 15 days'),
    ('With in 30 days', 'With in 30 days'),
    ('With in 3 month', 'With in 3 month'),
    ('With in 6 month', 'With in 6 month'),
)

PUBLISHING_CHOICE =(
    ('Consultant', 'Consultant'),
    ('On Website', 'On Website'),
    ('Social Media', 'Social Media'),
    ('Local News Paper', 'Local News Paper'),
    ('E News', 'E News'),
    ('Job Portals','Job Portals'),
 )
RESPONSE_CHOICE = (
     ('Online', 'Online'),
     ('Offline', 'Offline'),
     )
ACTION_STATUS = (
        ("Pending","Pending"),
        ("Recommended","Recommended"),
        ("Reviewed","Reviewed"),
        ("Approved", "Approved"),
        ("Put on hold","Put on hold"),
        ("Rejected", "Rejected"),
        
        
        
        

       
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)



class EmployeeServicesRecruitementCreateRequirement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment,blank=True, on_delete=models.CASCADE, null=True,verbose_name='Department')    
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    existing_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Existing Strength")
    new_requirement = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Requirement")
    total_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Total Strength")


    start_salary  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "salary Range")
    #salary_range  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    qualification  = models.ForeignKey(ManageQualification, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Qualification")
    experience  = models.ForeignKey(ManageExpereince, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Experience")
    language  = models.ForeignKey(ManageLanguage,  on_delete=models.SET_NULL,blank=True, null=True, max_length=200, verbose_name = "Language")
    time_frame_1 = models.CharField(choices= Urgency_CHOICE,default='With in 15 days', blank=True, null=True, max_length=200, verbose_name = "Time Frame")
    type_of_job   = models.ForeignKey(ManageUpdateEmploymentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of")
    job_description   = models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Job Description")
    valid_upto = models.DateField(blank = True, null = True, verbose_name = "Position Valid upto")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    position_available   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Available")
    position_publish   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Published")
    place_of_job_posting   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Place of Job Posting")
    response_mode   = models.CharField(choices=RESPONSE_CHOICE  ,default='', blank=True, null=True, max_length=200, verbose_name = "Response Mode")
    vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancies Approved")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    comment   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Comment")  
    job_link   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Name")
    status = models.CharField(choices= STATUS_CHOICE, max_length=60 , default='Open',  blank=True, null=True, verbose_name="STATUS")
    action_required = models.CharField(max_length=200,default='pending',choices=ACTION_STATUS, blank=True, null=True, verbose_name="Action Required")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(choices=GENDER,default='',blank=True,null=True,max_length=200,verbose_name="Gender")
    is_active = models.BooleanField(default=1)
    is_filled = models.BooleanField(default=0)


    class Meta:
        db_table = "employee_services_recruitement_create_requirement_model"

    #def __str__(self):
    #     return self.salary_range

RECOMMENDATION_STATUS=(
    ("Recommended","Recommended"),
    ("Rejected","Rejected"),
    ("Put on Hold","Put on Hold"),
)

HR_RECOMMENDED=(
    ("Recommended","Recommended"),
    ("Rejected","Rejected"),
    ("Put on Hold","Put on Hold"),
)

MODE_OF_RESPONSE=(
    ('online','online'),
    ('offline','offline'),
    ('both','both'),
)


MODE_OF_INTERVIEW=(
    ('Personal Meeting','Personal Meeting'),
    ('Telephonic','Telephonic'),
    ('Video Conferencing','Video Conferencing')
)
STATUS_OF_INTERVIEW =  (
    ('Attended', 'Attended'), 
    ('Rescheduled', 'Rescheduled'), 
    ('Absent', 'Absent'), 
    
)
IS_APPROVE=(
    ('Approve','Approve'),
    ('Rejected','Rejected'),
    ('Put on Hold','Put on Hold'),
)
SHORTLIST_RESUME=(
    ('Approve','Approve'),
    ('Rejected','Rejected'),
    ('Blacklist','Blacklist'),
)

ALLOW_PSYCO=(
    ('Allow','Allow'),
    ('Waive','Waive'),
)
OFFER_STATUS=(
    ('Approved','Approved'),
    ('Rejected','Recommended'),

)
NAME_SALUTE = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss'),
    ('Ms','Ms'),
    ('Dr','Dr'),
    ('CA','CA'),
    ('Er.','Er.'),
    ('Prof','Prof'),
)
MARITAL_STATUS = (
    ('Single','Single'),
    ('Married','Married'),
    ('Separated','Separated'),
   
)
APPROVAL_ACTION=(
    ("Approve","Approve"),
    ("Reject","Reject"),
    ("Put on Hold","Put on Hold"),
    ('Refered back','Refered back'),
)
CONSULTANT_MODE_RESPONSE=(
    ('online','online'),
    ('offline','offline'),
    ('both','both'),   
)
JOB_PORTAL_MODE_RESPONSE=(
    ('online','online'),
    ('offline','offline'),
    ('both','both'),   
)

class EmployeeServicesRecruitementRecommended(models.Model):
    webiste_action=models.BooleanField(blank=True,null=True)
    webiste_status=models.CharField(blank=True,null=True,max_length=100)
    mode_of_response_job_portal=models.CharField(blank=True,null=True,max_length=100,choices=JOB_PORTAL_MODE_RESPONSE,verbose_name='Mode of Response')
    portal_name=models.CharField(blank=True,null=True,max_length=100,verbose_name='Postal Name')
    job_portal_status=models.CharField(blank=True,null=True,max_length=100)
    jon_portal_action=models.BooleanField(default=0)
    url_job_portal=models.CharField(blank=True,null=True,max_length=100,verbose_name='Job Portal')
    valid_upto_job_portal=models.CharField(blank=True,null=True,max_length=100,verbose_name='Valid Upto')
    job_portal_status=models.CharField(blank=True,null=True,max_length=100)
    job_portal_action=models.BooleanField(default=0)
    mode_of_response_consultant=models.CharField(blank=True,null=True,max_length=100,choices=CONSULTANT_MODE_RESPONSE,verbose_name='Mode of Response')
    valid_upto_consultant=models.CharField(blank=True,null=True,max_length=100,verbose_name='Valid Upto')
    internal_source_action=models.CharField(blank=True,null=True,max_length=100)
    internal_source_status=models.BooleanField(default=0)
    consultant_source_status=models.CharField(blank=True,null=True,max_length=100)
    consultant_source_action=models.BooleanField(default=0)
    approval_status=models.BooleanField(default=0)
    approval_action=models.CharField(blank=True,null=True,max_length=100,choices=APPROVAL_ACTION)
    hr_status=models.BooleanField(default=0)
    grade_1 = models.ForeignKey(ManageGrade,blank=True, on_delete=models.CASCADE, null=True,verbose_name='Grade')    
    hr_action=models.CharField(max_length=100,default='pending',blank=True,null=True,choices=HR_RECOMMENDED,verbose_name='Action')
    tinme_frame=models.DateField(blank=True,null=True,verbose_name='Tentative closing date')
    caste   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Caste")
    religion    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Religion ")
    marital_status     = models.CharField(choices=MARITAL_STATUS,default='', blank=True, null=True, max_length=200, verbose_name = "Marital Status")
    middle_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Middle Name")
    last_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Last Name")
    name_salute   = models.CharField(choices=NAME_SALUTE,default='', blank=True, null=True, max_length=200, verbose_name = "Salute")
    landline_number = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Landline Number")
    emergency_number = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Emergency Number")
    name  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    relationship    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Language Known")
    pan_card   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pan Card")
    adhar_card   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Adhar Card")
    passport_no   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Passport Number")
    voter_id   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Voter Id")

    driving_license    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Driving License")
    date_of_anniversary    = models.DateField(blank = True, null = True, verbose_name = "Date of Anniversary")
    employee_id  = models.CharField(max_length=200, blank=True, null=True, verbose_name="Employee Id")
    mode_of_sourcing  = models.CharField(choices=PUBLISHING_CHOICE,default='', blank=True, null=True, max_length=200, verbose_name = "Mode of Sourcing")
    photo = models.FileField(upload_to='upload_report/%Y/%m/%d/', blank=True, null=True, verbose_name="Photo")
    first_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "First Name")


    publish_job_comment=models.TextField(max_length=600,blank=True,null=True,verbose_name='Comment')
    approve_comment= models.TextField( max_length=600,blank=True, null=True,verbose_name="Comment")  
    document_receivied=models.CharField(default='pending',max_length=100,blank=True,null=True)
    shortlist_resume_status=models.BooleanField(default=0)
    is_publish=models.BooleanField(default=0)
    approve_status=models.BooleanField(default=0)
    offer_formalities_status=models.CharField(choices=OFFER_STATUS,default='',max_length=200,blank=True,null=True)
    created_user=models.CharField(default='',max_length=200,blank=True,null=True)
    is_hrrecommend=models.BooleanField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    location = models.ForeignKey(ManageBranch,default='' ,on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment,blank=True, on_delete=models.CASCADE, null=True,verbose_name='Department')    
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    existing_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Existing Strength")
    new_requirement = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Requirement")
    total_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Total Strength")
    recommendation = models.CharField(max_length=200,default='pending',choices=RECOMMENDATION_STATUS, blank=True, null=True, verbose_name="Recommendation")
    start_salary  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    qualification  = models.ForeignKey(ManageQualification, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Qualification")
    experience  = models.ForeignKey(ManageExpereince, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Experience")
    language  = models.ForeignKey(ManageLanguage,  on_delete=models.SET_NULL,blank=True, null=True, max_length=200, verbose_name = "Language")
    time_frame_1 = models.CharField(choices= Urgency_CHOICE,default='With in 15 days', blank=True, null=True, max_length=200, verbose_name = "Time Frame")
    type_of_job   = models.ForeignKey(ManageUpdateEmploymentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of")
    job_description   = models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Job Description")
    valid_upto = models.DateField(blank = True, null = True, verbose_name = "Valid upto")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    position_available   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Available")
    position_publish   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Published")
    response_mode   = models.CharField(choices=RESPONSE_CHOICE  ,default='', blank=True, null=True, max_length=200, verbose_name = "Response Mode")
    vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancies Available")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    comment   = models.TextField( max_length=600,blank=True, null=True,verbose_name="Comment")  
    job_link   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Name")
    status = models.CharField(choices= STATUS_CHOICE, max_length=60 , default='Open',  blank=True, null=True, verbose_name="STATUS")
    action_required = models.CharField(max_length=200,default='pending',choices=ACTION_STATUS, blank=True, null=True, verbose_name="Action Required")
    publish_status= models.CharField(max_length=200,default='pending', blank=True, null=True, verbose_name="publish status")
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(choices=GENDER,default='',blank=True,null=True,max_length=200,verbose_name="Gender")
    is_active = models.BooleanField(default=1)
    is_recommended=models.BooleanField(default=0)
    hr_recommended= models.CharField(max_length=200,choices=HR_RECOMMENDED,default='pending', blank=True, null=True, verbose_name="Hr_recommended")
    is_approve= models.CharField(choices=IS_APPROVE,max_length=200,default='pending', blank=True, null=True, verbose_name="is_approve")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
   # vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancy Available")
    vacancy_posted = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancy Posted")
    is_filled = models.BooleanField(default=0)
    resume_received_doc  = models.FileField(upload_to='candidates_resume/%Y/%m/%d/', blank=True, null=True, verbose_name="Resume")
    name_of_candidate  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name of Candidate")
    phone_no = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Phone Number")
    email_id = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email Id")
    mode_of_response = models.CharField(choices=MODE_OF_RESPONSE, default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    updated_resume=models.BooleanField(default=0)
    shortlist_resume=models.CharField(choices=SHORTLIST_RESUME,default='pending',blank=True,null=True,max_length=200,verbose_name='Shortlist Resume')
    allow_psyco=models.CharField(choices=ALLOW_PSYCO,default='pending',blank=True,null=True,max_length=200,verbose_name='Allow Psyco')
    psyco_test=models.BooleanField(default=0)
    test_date=models.DateField(blank=True,null=True,verbose_name='Test Date')
    test_type=models.CharField(default='',max_length=200,blank = True, null = True, verbose_name = "Test Type")
    test_score_awarded=models.CharField(default='',blank=True,max_length=200,verbose_name='Test Score Awarded')
    test_analysis=models.CharField(default='',blank=True,max_length=200,verbose_name='Test Analysis')
    update_test=models.BooleanField(default=0)
    place_of_interview  = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = " Place Of Interview")
    timing_of_interview = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = " Timing Of Interview")
    date_interview  = models.DateField(blank=True, null=True, verbose_name = "Date Of Interview")
    contact_person = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = "Contact Person ")
    mode_of_interview=models.CharField(default='',blank=True,null=True,max_length=200,choices=MODE_OF_INTERVIEW ,verbose_name='Mode Of Interview')
    special_instruction=models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Special Instruction")
    schedule_status=models.BooleanField(default=0)
    person_name=models.CharField(default='',max_length=200,null=True,blank=True,verbose_name='Contact Person Name')
    person_emailid=models.CharField(default='',max_length=200,null=True,blank=True,verbose_name='Contact Person Email')
    person_phoneno=models.CharField(default='',max_length=200,null=True,blank=True,verbose_name='Contact Phone No')
    interview_score=models.CharField(default='',max_length=100,null=True,blank=True,verbose_name='Interview Score')
    individual_score=models.CharField(default='',max_length=200,null=True,blank=True,verbose_name='Individual Score')  
    reasone_for_rescheduling=models.CharField(default='',max_length=200,blank=True,verbose_name='Reason For Rescheduling')
    interview_of_status = models.CharField(choices= STATUS_OF_INTERVIEW, max_length=200 ,default='pending',  blank=True, null=True, verbose_name="Status of Interview")
    interview_result_status=models.CharField(default='pending',max_length=200,blank=True,verbose_name='Interview Result')
    interview_approvel=models.BooleanField(default=0)
    document_type_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Document Type')
    document_name_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Document Name')
    type_of_verification_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Type of Verification')
    verification_template_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Verification Template')
    required_by_1=models.DateField(blank = True, null = True, verbose_name = "Required by")
    document_status=models.BooleanField(default=0)
    document_submission   = models.FileField(upload_to='candidates_upload_document/%Y/%m/%d/', verbose_name="Document", blank=True, null=True)
    upload_document_status=models.BooleanField(default=0)
    referencename_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    referencerelationship_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Relationship")
    referencecontact_number_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    referenceemail_id_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email id")
    referenceaddress_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Address")
    referenceknown_since_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Known since")
    employer_name=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Employer Name")
    employercontact_person=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Person")
    employer_emailid=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email Id")
    employeer_phno=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Phone Number")
    address=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Address")
    type_of_address=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Type of Address")
    staying_since=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Staying Since")
    proof_attach=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Proof Attached")
    test_name=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Test Name")
    referred_to_hospital=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Reffered to Hospital")
    occupation   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    offer_formalities_action=models.BooleanField(default=0)
    grade=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Grade')
    
    offer_contact_person=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Contact Person')
    date_of_joining  = models.DateField(blank = True, null = True,  verbose_name = "Date of Joining")
    #location_of_joining  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Joining Location")
    gross_salary=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Gross Salary')
    salary_structut_salary_code_1  = models.ForeignKey(ManageSalary, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Salary Code")
    salary_structut_salary_name_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Salary Name")
    salary_structut_amount_offered_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Amount offered")
    salary_structut_taxability_1      = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Taxability")
    salary_structut_salary_frequency_1  = models.IntegerField(default=1, blank=True, null=True, verbose_name = "Frequency")
    perquisitec_name_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Perquisite Name")
    perquisite_frequency_1 = models.IntegerField(default=0, blank=True, null=True, verbose_name = "Frequency")
    perquisite_amount_1 = models.IntegerField(default=0, blank=True, null=True,  verbose_name = "Amount")
    deduction_name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    deduction_frequancy = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Frequancy")
    deduction_ammount = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Ammount")
    perquisite_taxability= models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Taxability")
    perquisite_CTC=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Part of CTC')
    deduction_CTC=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Part of CTC')
    deduction_type = models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Deduction Type')
    perquisite_type=models.CharField(default='',max_length=200,null=True,blank=True,verbose_name='Perquisite Type')
    issue_offer_action=models.CharField(default='pending',max_length=100,null=True,blank=True)
    issue_offer_status=models.BooleanField(default=0)
    offer_approval=models.BooleanField(default=0)
    acceptance_status=models.CharField(default='Pending for Acceptance',max_length=200,blank=True,null=True,verbose_name='Acceptance Status')
    offer_current_status=models.CharField(default='Pending for joining',max_length=200,blank=True,null=True,verbose_name='Offer Current Status')

    class Meta:
        db_table = "employee_services_recruitement_recommended"



###############################################################

#################################################################
class EmployeeServicesRecruitementDocumentUploads(models.Model):
    ref_id=models.ForeignKey(EmployeeServicesRecruitementRecommended, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    location_id=models.ForeignKey(ManageBranch,default='' ,on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    email_id=models.ForeignKey(EmployeeServicesRecruitementRecommended,on_delete=models.CASCADE,blank=True,null=True,verbose_name='Email',related_name='email_1')
    document_type_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Document Type')
    document_name_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Document Name')
    required_by_1=models.DateField(blank=True,null=True,verbose_name='Required by')
    verification_template_1=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Verification Template')
    type_of_verification_1=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Type Of Verification')
    verification_template_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Verification Template')
    type_of_verification_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Type Of Verification')
   
    document_status=models.BooleanField(default=0)
    class Meta:
        db_table='employee_services_recruitement_document_upload'

class EmployeeServicesRecruitementverificationtemplateUploads(models.Model):
    ref_id=models.ForeignKey(EmployeeServicesRecruitementRecommended, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    verification_template_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Verification Template')
    type_of_verification_1=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Type Of Verification')
    document_status=models.BooleanField(default=0)

    class Meta:
        db_table='employee_services_recruitement_verification_upload'


    
    class Meta:
        db_table='employee_services_recruitement_verification_upload'
############Hr Review################################3
class EmployeeServicesRecruitementHrReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment,blank=True, on_delete=models.CASCADE, null=True,verbose_name='Department')    
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    existing_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Existing Strength")
    new_requirement = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Requirement")
    total_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Total Strength")
    recommendation = models.CharField(max_length=200,default='',choices=RECOMMENDATION_STATUS, blank=True, null=True, verbose_name="Recommendation")
    start_salary  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    # salary_range  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    qualification  = models.ForeignKey(ManageQualification, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Qualification")
    experience  = models.ForeignKey(ManageExpereince, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Experience")
    language  = models.ForeignKey(ManageLanguage,  on_delete=models.SET_NULL,blank=True, null=True, max_length=200, verbose_name = "Language")
    time_frame_1 = models.CharField(choices= Urgency_CHOICE,default='With in 15 days', blank=True, null=True, max_length=200, verbose_name = "Time Frame")
    type_of_job   = models.ForeignKey(ManageUpdateEmploymentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of")
    job_description   = models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Job Description")
    valid_upto = models.DateField(blank = True, null = True, verbose_name = "Position Valid upto")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    position_available   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Available")
    position_publish   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Published")
    place_of_job_posting   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Place of Job Posting")
    response_mode   = models.CharField(choices=RESPONSE_CHOICE  ,default='', blank=True, null=True, max_length=200, verbose_name = "Response Mode")
    vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancies Approved")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    comment   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Comment")  
    job_link   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Name")
    status = models.CharField(choices= STATUS_CHOICE, max_length=60 , default='Open',  blank=True, null=True, verbose_name="STATUS")
    action_required = models.CharField(max_length=200,default='pending',choices=ACTION_STATUS, blank=True, null=True, verbose_name="Action Required")
    added = models.DateTimeField(auto_now=True)
    #updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(choices=GENDER,default='',blank=True,null=True,max_length=200,verbose_name="Gender")
    is_active = models.BooleanField(default=1)
    is_recommended=models.BooleanField(default=0)
    hr_recommended= models.CharField(max_length=200,default='pending', blank=True, null=True, verbose_name="Hr_recommended")
    #copy =models.OneToOneField(EmployeeServicesRecruitementRecommended,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = "employee_services_recruitement_hr_review_requirement"



EMPLOYEE_CANDIDATE_RESUME_STATUS = (
    (1, 'Resume Received'),
    (2, 'Resume Shortlisted'),
    (3, 'Candidates Shortlisted'),
    (4, 'Candidates Joined'),
    (5, 'Rejected'),
)


INTERVIEW_STATUS = (
    (1, 'Accept'),
    (2, 'Rejected'),
     (3, 'Hold'),
      (4, 'Delete'),
)
RESUME_STATUS_1 = (
    ('Accept', 'Accept'),
    ('Rejected', 'Rejected'),
     ('Hold', 'Hold'),
      ('Delete', 'Delete'),
)


OFFER_LETTER_STATUS = (
    (1, 'Pending'),
    (2, 'Inprogress'),
    (3, 'Completed'),
)
INTERVIEW_DETAILS = (
    ('Place of Interview', 'Place of Interview'),
    ('Timing of Interview', 'Timing of Interview'),
    ('Date of Interview', 'Date of Interview'),
    ('Contact Person', 'Contact Person'),
    
)
RECOMMENDATION_STATUS_1 =  (
    ('Interview Held', 'Interview Held'), 
    ('Postpone', 'Postpone'),
     ('Hold', 'Hold'),
     ('Cancelled', 'Cancelled'),
)
RECOMMENDATION_STATUS_1 =  (
    ('Interview Held', 'Interview Held'), 
    ('Postpone', 'Postpone'),
     ('Hold', 'Hold'),
     ('Cancelled', 'Cancelled'),
)
DOCUMNET_NAME  = (
    ('10th Certificate ', '10th Certificate '), 
    (' Graduation Certificate ', ' Graduation Certificate'), 
    ('Post Graduation Certificate', 'Post Graduation Certificate'), 
    ('Experience Certificate ', 'Experience Certificate'), 
    ('Relieving Letter ', ' Relieving Letter'), 
    ('Pan Card ', 'Pan Card '), 
    ('Aadhar Card ', 'Aadhar Card'), 
    (' Photo', 'Photo '), 
    (' Bank Statement', 'Bank Statement '), 
    (' Salary Slip', 'Salary Slip '), 
    
    )

CANDIDATE_SHORTLIST_STATUS =  (
    ('Offer Issues', 'Offer Issues'), 
    ('Expired', 'Expired'),
     ('Withdraw', 'Withdraw'),
     ('Join', 'Join'),
)

INTERVIEW_SCHEDULED_STATUS=  (
    (' Interview Scheduled', 'Interview Scheduled '),    
)
INTERVIEW_RESULT=  (
    (' Qualified ', ' Qualified '), 
    (' Rejected ', ' Rejected '), 
    (' Hold ', ' Hold '), 
    
)



class EmployeeServicesRecruitementInviteResume(models.Model):
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    received_from = models.ForeignKey(RecruitmentManagementCandidateSourcingManageReceiptofResume, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Received from")
    job_link = models.ForeignKey(EmployeeServicesRecruitementCreateRequirement , on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Received from")
    name_of_candidate  = models.ForeignKey(EmployeeServicesRecruitementRecommended,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Name of Candidate")
    phone_no = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Phone Number")
    email_id = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email Id")
    profile_summary  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Profile Summary")
    resume_received_doc  = models.FileField(upload_to='candidates_resume/%Y/%m/%d/', blank=True, null=True, verbose_name="Resume")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    interview_result_1 = models.CharField(choices=INTERVIEW_RESULT  ,default='', max_length=200, blank=True, null=True, verbose_name="Interview Result")
    interview_date  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Interview Date")
    interview_time  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Interview Time")
    overall_rating  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Overall Rating")
    formalities_completed_on  = models.DateField(blank = True, null = True,  verbose_name = "Formalities Completed on")
    status = models.IntegerField(choices= EMPLOYEE_CANDIDATE_RESUME_STATUS, default=1,  blank=True, null=True, verbose_name="Decision")
    interview_status = models.IntegerField(choices= INTERVIEW_STATUS, default=0,  blank=True, null=True, verbose_name="Resume Status")
    resume_status = models.CharField(choices= RESUME_STATUS_1, default='', max_length=200, blank=True, null=True, verbose_name="Resume Status")
    
    
    interview_committee = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Interview Committee")
    date_of_interview = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = " Date of Interview")
    details_of_interview = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Details of Interview")
    recommendation = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Recommendation")
    
    recommendation_1 = models.CharField(choices=RECOMMENDATION_STATUS_1, default='', blank=True, null=True, max_length=200, verbose_name = "Recommendation")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation offered")
    salary_offered  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Salary offered")
    offer_date  = models.DateField(blank = True, null = True,  verbose_name = "Offer Date")
    document_submission   = models.FileField(upload_to='candidates_upload_document/%Y/%m/%d/', verbose_name="Document", blank=True, null=True)
    date_joining_candition  = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = "Date Joining Condition")
    date_of_joining  = models.DateField(blank = True, null = True,  verbose_name = "Date of Joining")
    joining_location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Joining Location", related_name = "joining_location")
    reporting_officer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Reporting Officer")
    offer_letter_date  = models.DateField(blank = True, null = True,  verbose_name = "Offer Letter  Date")
    offer_letter_status = models.IntegerField(choices= OFFER_LETTER_STATUS, default=0,  blank=True, null=True, verbose_name="Interview Status")
    interview_details_status = models.CharField(choices= INTERVIEW_DETAILS, max_length=200 ,default='',  blank=True, null=True, verbose_name="Interview Status")
    interview_of_status = models.CharField(choices= STATUS_OF_INTERVIEW, max_length=200 ,default='Attended',  blank=True, null=True, verbose_name="Interview Status")
    
    place_of_interview  = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = " Place Of Interview")
    timing_of_interview = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = " Timing Of Interview")
    date_of_interview  = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = "Date Of Interview ")
    contact_person = models.CharField(default='', blank=True, null=True, max_length=200,  verbose_name = "Contact Person ")
    comment =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "Comment ")
    document_name = models.CharField(choices= DOCUMNET_NAME, max_length=200 ,default='',  blank=True, null=True, verbose_name=" Document Required")
    
    interview_held =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "Interview Held ")
    cancelled =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "Cancelled ")
    proposed =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "Proposed ")
    new_date =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "New Date ")
    new_time =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "New Time ")
    new_place_of_interview=  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "New Place ")
    new_contact_person =  models.CharField(default='', blank=True, null=True, max_length=800,  verbose_name = "New Contact Person ")
    candidate_shortlist_status = models.CharField(choices= CANDIDATE_SHORTLIST_STATUS, max_length=200 ,default='',  blank=True, null=True, verbose_name=" Status")
    interview_scheduled = models.CharField(choices= INTERVIEW_SCHEDULED_STATUS, max_length=200 ,default='Interview Scheduled',  blank=True, null=True, verbose_name=" Interview Scheduled")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)
    updated_resume=models.BooleanField(default=0)

    class Meta:
        db_table = "employee_services_recruitement_invite_resume"



############################Publish Jobs######################3



class EmployeeServicesRecruitementPublishJobs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True)
    location = models.ForeignKey(ManageBranch,default='' ,on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    #place_of_job_posting = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Place of job Posting")

    department = models.ForeignKey(ManageDepartment,blank=True, on_delete=models.CASCADE, null=True,verbose_name='Department')    
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    existing_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Existing Strength")
    new_requirement = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Requirement")
    total_strength = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Total Strength")
    recommendation = models.CharField(max_length=200,default='',choices=RECOMMENDATION_STATUS, blank=True, null=True, verbose_name="Recommendation")

    start_salary  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    # salary_range  = models.ForeignKey(ManageSalaryRange,on_delete=models.SET_NULL, blank=True, null=True, max_length=200, verbose_name = "Salary Range")
    qualification  = models.ForeignKey(ManageQualification, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Qualification")
    experience  = models.ForeignKey(ManageExpereince, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Experience")
    language  = models.ForeignKey(ManageLanguage,  on_delete=models.SET_NULL,blank=True, null=True, max_length=200, verbose_name = "Language")
    time_frame_1 = models.CharField(choices= Urgency_CHOICE,default='With in 15 days', blank=True, null=True, max_length=200, verbose_name = "Time Frame")
    type_of_job   = models.ForeignKey(ManageUpdateEmploymentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of")
    job_description   = models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Job Description")
    valid_upto = models.DateField(blank = True, null = True, verbose_name = "Valid upto")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    position_available   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Available")
    position_publish   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Position Published")
    #place_of_job_posting   = models.CharField(ManagerBranch ,default='', blank=True, null=True, max_length=200, verbose_name = "Place of Job Posting")
    response_mode   = models.CharField(choices=RESPONSE_CHOICE  ,default='', blank=True, null=True, max_length=200, verbose_name = "Response Mode")
    vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancies Available")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    comment   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Comment")  
    job_link   = models.CharField( max_length=600,blank=True, null=True,verbose_name="Name")
    status = models.CharField(choices= STATUS_CHOICE, max_length=60 , default='Open',  blank=True, null=True, verbose_name="STATUS")
    action_required = models.CharField(max_length=200,default='pending',choices=ACTION_STATUS, blank=True, null=True, verbose_name="Action Required")
    #added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    gender = models.CharField(choices=GENDER,default='',blank=True,null=True,max_length=200,verbose_name="Gender")
    is_active = models.BooleanField(default=1)
    is_recommended=models.BooleanField(default=0)
    hr_recommended= models.CharField(max_length=200,default='pending', blank=True, null=True, verbose_name="Hr_recommended")
    is_approve= models.CharField(max_length=200,default='pending', blank=True, null=True, verbose_name="is_approved")
    mode_of_publishing = models.CharField(choices=PUBLISHING_CHOICE  ,default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    #place_of_job_posting   = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Place Of Job Posting")
   # vacancy_approved   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancy Available")
    vacancy_posted = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Vacancy Posted")
    #valid_upto = models.DateField(blank = True, null = True, verbose_name = "Valid upto")

    mode_of_response = models.CharField(choices=MODE_OF_RESPONSE, default='', max_length=200, blank=True, null=True, verbose_name="Mode of Publishment")
    
    class Meta:
        db_table="employee_services_recruitement_publish_jobs"





              
###############EmployeeServicesRecruitementPsychometricTest
class EmployeeServicesRecruitementPsychometricTest(models.Model):
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    name_of_candidate  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name of Candidate")
    status = models.IntegerField(choices= EMPLOYEE_CANDIDATE_RESUME_STATUS, default=1,  blank=True, null=True, verbose_name="Mode of Publishing")
    email     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email Id")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)
    class Meta:
        db_table = "employee_services_recruitement_psychometrictest"
###############

# ************************ Employee Registration 
NAME_SALUTE = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss'),
    ('Ms','Ms'),
    ('Dr','Dr'),
    ('CA','CA'),
    ('Er.','Er.'),
    ('Prof','Prof'),
)

MARITAL_STATUS = (
    ('Single','Single'),
    ('Married','Married'),
    ('Separated','Separated'),
   
)
class EmployeeRegistrationUpdateRegistrationPersonalDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    employee_created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank= False, null=True, related_name = "employee_created_by")
    employee_id  = models.CharField(max_length=200, blank=True, null=True, verbose_name="Employee Id")
    mode_of_sourcing  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Mode of Sourcing")
    
    mode_of_sourcing_1  = models.CharField(choices=PUBLISHING_CHOICE,default='', blank=True, null=True, max_length=200, verbose_name = "Mode of Sourcing")
    photo = models.FileField(upload_to='upload_report/%Y/%m/%d/', blank=True, null=True, verbose_name="Photo")
    type_of_job   = models.ForeignKey(ManagementEmployeeTypeofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of")
    name_salute   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name Salute")
    name_salute_1   = models.CharField( choices=NAME_SALUTE ,default='', blank=True, null=True, max_length=200, verbose_name = "Salute")
    first_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Employee Name")
    middle_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Middle Name")
    last_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Last Name")
    date_of_birth   =models.DateField(blank = True, null = True, verbose_name = "Date of Birth")
    caste   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Caste")
    religion    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Religion ")
    marital_status     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Marital Status")
    marital_status_1     = models.CharField(choices=MARITAL_STATUS ,default='', blank=True, null=True, max_length=200, verbose_name = "Marital Status")
    mobile_no     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Mobile Number")
    email     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email Id")
    landline_number      = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Landline Number")
    emergency_number       = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Emergency Number")
    name  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    relationship    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Language Known")
    pan_card   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pan Card")
    adhar_card   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Adhar Card")
    driving_license    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Driving License")
    language_known    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Language Known")
    language  = models.ForeignKey(ManageLanguage,  on_delete=models.SET_NULL,blank=True, null=True, max_length=200, verbose_name = "Language")
    date_of_anniversary    = models.DateField(blank = True, null = True, verbose_name = "Date of Anniversary")
    passport_no = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Passport Number")
    voter_id = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Voter ID")

    #added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return str(self.user_id)

    class Meta:
        db_table = "employee_registration_update_registration_personal_details"

class EmployeeRegistrationUpdateRegistrationFamilityDetails(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    mother_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    mother_dob   = models.DateField(blank = True, null = True, verbose_name = "DOB")
    mother_occupation   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    mother_contact_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    father_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    father_dob   = models.DateField(blank = True, null = True, verbose_name = "DOB")
    father_occupation   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    father_contact_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    spouse_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    spouse_dob   = models.DateField(blank = True, null = True, verbose_name = "DOB")
    spouse_occupation   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    spouse_contact_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_family_details"


class EmployeeRegistrationUpdateRegistrationFamilityChildren(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    relationship_1= models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Relationship")
    name_1=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Name') 
    date_of_birth_1=models.CharField(default='',blank=True,max_length=200,verbose_name='Date Of Birth')
    occupation_1=models.CharField(default='',blank=True,max_length=200,verbose_name='Occuption')
    contact_number_1=models.CharField(default='',blank=True,max_length=200,verbose_name='Contact Number')  
    children_name_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    children_dob_1   = models.DateField(blank = True, null = True, verbose_name = "DOB")
    children_occupation_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    children_contact_number_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_family_children"
OTHER_RELATIONSHIP = (
    ('Brother', 'Brother'),
    ('Sister', 'Sister'),
    ('Father', 'Father'),
    ('Mother', 'Mother'),
    ('Spouse', 'Spouse'),
    ('Daughter', 'Daughter'),
    ('son', 'son'),
    ('Uncle', 'Uncle'),
    ('Friend', 'Friend'),

)

class EmployeeRegistrationUpdateRegistrationFamiliyOtherDetails(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    other_name_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    other_dob_1   = models.DateField(blank = True, null = True, verbose_name = "Date of Birth")
    other_occupation_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Occupation")
    other_relationship_1   = models.CharField( default='', blank=True, null=True, max_length=200, verbose_name = "Relationship")
    other_contact_number_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    #added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_family_other_details"


class EmployeeRegistrationUpdateRegistrationMedicalHistory(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    name_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    blood_group_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Blood Group")
    type_of_illness_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Type of Illness")
    result_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Result")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_medical_history"

OWNERSHIP_STATUS = (
    ('Self on','Self on'),
    ('Rented','Rented'),
    ('Family On','Self On'),
)
class EmployeeRegistrationCorrespondenceAddress(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    landmark=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Land Mark")
    building   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "House Number")
    block   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Block")
    sector    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Sector")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="City")
    district   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "District")
    state = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="State")
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,  verbose_name="Country")
    zip_code     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pin Code")
    staying_since = models.DateField(blank = True, null = True, verbose_name = "Staying since")
    ownership     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Ownership")
    ownership_1     = models.CharField(choices=OWNERSHIP_STATUS ,default='', blank=True, null=True, max_length=200, verbose_name = "Ownership")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_correspondance"


class EmployeeRegistrationPermanentAddress(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    landmark_1=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Land Mark')
    building_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "House Number")
    block_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Block")
    sector_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Sector")
    city_1 = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="City")
    district_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "District")
    state_1 = models.ForeignKey(State, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="State")
    country_1 = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True,  verbose_name="Country")
    zip_code_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Pin Code")
    staying_since_1 = models.DateField(blank = True, null = True, verbose_name = "Staying since")
    ownership_1     = models.CharField(choices=OWNERSHIP_STATUS,default='', blank=True, null=True, max_length=200, verbose_name = "Ownership")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_parmanent_address"


class EmployeeRegistrationUpdateRegistrationJoiningDetails(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    joining_location   = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    joining_date_of_joining    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Date of Joining")
    joining_time     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Joining Time")
    joining_grade_offered     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Grade offered")
    joining_next_date_of_increment    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Next Date of Increment")
    joining_department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, null=True, verbose_name="Department")
    joining_designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, null=True, verbose_name="Designation")
    joining_responsibilities = models.ForeignKey(ManageResponsibility, on_delete=models.SET_NULL, null=True, verbose_name="Responsibility")
    joining_role = models.ForeignKey(RoleMangement, on_delete=models.SET_NULL, null=True, verbose_name="Role")
    joining_reporting_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Reporting To")
    joining_probation_period  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Probation Period")
    contract_valid_up_to  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Contract Valid Up To")
    mode_of_sourcing_1  = models.CharField(choices=PUBLISHING_CHOICE,default='', blank=True, null=True, max_length=200, verbose_name = "Mode of Sourcing")
    type_of_job   = models.ForeignKey(ManageUpdateEmploymentType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Type of Job")
    pay_roll_job   = models.ForeignKey(ManagementEmployeePayrollofJob, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Payroll of") 
    effective_date= models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Effective Date")
    
    status = models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='status')
    income_type = models.CharField(default='',max_length=100,null=True,blank=True,verbose_name='Income Type')
    gross_total_income=models.CharField(default='',max_length=100,null=True,blank=True,verbose_name='Gross Total Income')
    deduction=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Deduction')
    net_taxable_income=models.CharField(default='',max_length=100,null=True,blank=True,verbose_name='Net Taxable Income')
    upload_document = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True, verbose_name="Upload Documents")
    tax_declaration_type = models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Tax Declaration Type')
    exemption_type=models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Exemption Type')
    tax_rule=models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Tax Rule')
    exemption_amount=models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Exemption Amount')
    maxmimum_limit=models.CharField(max_length=100,default='',blank=True,null=True,verbose_name='Maximum Limit')
    upload_document_1 = models.FileField(upload_to='documents/%Y/%m/%d/', blank=True, null=True, verbose_name="Upload Documents")
    submission_date=models.DateField(blank=True,null=True,verbose_name='Submission date')
    tax_declaration_status=models.BooleanField(default=0)
    approve_date=models.DateField(blank=True,null=True,verbose_name='Approve Date')





    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_registration_joining_detail"

class EmployeeIncomeTaxCalculation(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")

    location   = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, null=True, verbose_name="Department")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, null=True, verbose_name="Designation")
    employee_name = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Employee Name')
    assessment_year=models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Assessment Year')
    annual_salary = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Annual Salary')
    other_income = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Other Income')
    total_income = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Total Income')
    exemption = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Exemption')
    deduction = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Deduction')
    taxable_income = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Taxable Income')
    income_tax = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Income Tax')
    professional_tax = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Professional Tax')
    entertainment_tax = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Entertainment Tax')
    total= models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Total')
    cess = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Cess')
    total_tax_liabilty = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Total Tax Liability')
    tax_already_deducted = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Tax Already deducted')
    deduction_for_the_month = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Deductoin for the month')
    balance_tax = models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Balance Tax')
    tax_approve_action=models.BooleanField(default=0)
    tax_approve_status=models.CharField(max_length=100,default='',blank=True,null=True)
    approved_date=models.DateField(blank=True,null=True)
    recovery_period=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Recovery Period')
    recovery_type=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Recovery Type')
    recovery_amount=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Recovery Amount')
    recovery_approval_action=models.BooleanField(default=0)
    recovery_approval_status=models.CharField(default='',max_length=100,blank=True,null=True)



    class Meta:
        db_table="employee_income_tax_calculation"





class EmployeeUpdateRegistrationTermination(models.Model):
    termination_date=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Termination Date")
    approve_by=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Approved By")
    reason_termination=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Reasons for Termination")
    termination_benifit=models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Termination Benefit")

    class Meta:
        db_table='employee_registration_termination'

class EmployeeRegisterationUpdateRegistrationEmergencyContactdetails(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")

    name=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Name')
    contact_number=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Contact Number')
    email=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='Email Id')
    relationship=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name ='Relationship')

    class Meta:
        db_table='employee_registration_emergency_details'

class EmployeeRegistrationUpdateRegistrationJoiningDetailsHistory(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Employee Id")
    current_designation = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Designation")
    new_designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, null=True, verbose_name="New Designation")
    current_department  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Department")
    new_department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, null=True, verbose_name="New Department")
    current_reporting = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Reporting To")
    new_reporting = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="New Reporting To")
    current_responsibilites = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Responsibilit")
    new_responsibilities = models.ForeignKey(ManageResponsibility, on_delete=models.SET_NULL, null=True, verbose_name="New Responsibility")
    current_location  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Current Location")
    new_location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "New Location")
    current_role  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Current Role")
    joining_role = models.ForeignKey(RoleMangement, on_delete=models.SET_NULL, null=True, verbose_name="New Role")
    current_salary  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Current Salary")
    new_salary  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="New Salary")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_joining_details_history"


class EmployeeRegistrationUpdateEducationalQualification(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    educational_qualificationcourse_name_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Course/Class")
    educational_qualificationstart_date_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Acedemic Year ")
    educational_qualificationend_date_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "End Date")
    educational_qualificationmarks_division_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Marks")
    educational_qualificationroll_number_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Roll Number")
    educational_qualificationuniversity_institution_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "University/Board")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_educational_qualification"


class EmployeeRegistrationUpdateProfessionalJourney(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    professional_journeycompany_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Employeer Name")
    professional_journeystart_date_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Period")
    professional_journeyend_date_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "End Date")
    professional_journeylast_desgination_1   = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, null=True, verbose_name="Last Designation")
    professional_journeynature_of_duties_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Main Responsibilites")
    professional_journeylast_drawn_dalary_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Last Drawn Salary")
    reason_for_leaving_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Reason for Leaving")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_professional_journey"
TAXABILITY_STATUS = (
    ('Yes','Yes'),
    ('No','No'),
)


class EmployeeRegistrationUpdateSalaryStructutre(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    salary_structut_salary_code_1  = models.ForeignKey(ManageSalary, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Salary Code")
    salary_structut_salary_name_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Salary Name")
    salary_structut_salary_frequency_1  = models.IntegerField(choices = FREQUENCY, default=1, blank=True, null=True, verbose_name = "Frequency")
    salary_structut_amount_offered_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Amount offered")
    salary_structut_percentage_value_flag_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Percentage/ Value Flag")
    salary_structut_taxability_1      = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Taxability")
    salary_structut_taxability_status      = models.CharField(choices=TAXABILITY_STATUS ,default='', blank=True, null=True, max_length=200, verbose_name = "Taxability")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_salary_structutre"


class EmployeeRegistrationDeductionAndPerquisites(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    appicablitity_1 = models.IntegerField(choices= YESNO, default=1,  blank=True, null=True, verbose_name="Applicablitity")
    perquisitec_category_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Perquisite Code")
    perquisitec_name_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Perquisite Name")
    perquisite_frequency_1 = models.IntegerField(choices = FREQUENCY, default=1, blank=True, null=True, verbose_name = "Perquisite Frequency")
    percentage_value_flag_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Part of CTC")
    perquisite_amount_1 = models.IntegerField(default=0, blank=True, null=True,  verbose_name = "Amount offered")
    perquisite_taxability_status_1 = models.CharField(choices=TAXABILITY_STATUS ,default='', blank=True, null=True, max_length=200, verbose_name = "Taxability")

    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_deduction_and_perquisites"
class EmployeeRegistrationDeduction(models.Model):
    applicated  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Applicated")
    deduction_code  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Deduction Code")
    deduction_name = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Deduction Name")
    deduction_frequancy = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Frequancy")
    deduction_ammount = models.IntegerField(default=0, blank=True, null=True, verbose_name = "Deduction Ammount")
    deduction_taxability_status_1 = models.CharField(choices=TAXABILITY_STATUS ,default='', blank=True, null=True, max_length=200, verbose_name = "Tax Impact")
    part_of_ctc_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Part of CTC")

    class Meta:
        db_table = "employee_registration_deduction"
class EmployeeRegistrationUpdateBankDetails(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    account_type   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Account Type")
    bank_account_number    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Bank Account Number")
    bank_name    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Bank Name")
    branch     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Branch")
    ifscc_code     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "IFSC Code")
    micr       = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "MICR ")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_registration_bank_details"


class EmployeeRegistrationReferences(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    referencename_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name")
    referencerelationship_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Relationship")
    referencecontact_number_1    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Contact Number")
    referenceemail_id_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Email id")
    referenceaddress_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Address")
    referenceknown_since_1     = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Known since")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_registration_references"

Verification_STATUS = (
    ('Accept', 'Accept'),
    ('Rejected', 'Rejected'),
)
  

class EmployeeRegistrationVerificationReport(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    verification_agency_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Verification Name")
    finding_1     = models.CharField( max_length=200, choices= Verification_STATUS, default='',  blank=True, null=True, verbose_name = "Status")
    upload_report_1   = models.FileField(upload_to='upload_report/%Y/%m/%d/', verbose_name="Report")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_verification_report"

          
class EmployeeRegistrationDocuments(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    document_type_1=models.CharField(default='',blank=True,null=True,max_length=200,verbose_name='Document Type')
    name_of_documents_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Name of Documents")
    upload_1   = models.FileField(upload_to='upload_report/%Y/%m/%d/', verbose_name="Upload")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_registration_documents"


class EmployeeAssetAllocated(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    asset_code_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Asset Code")
    asset_serial_number_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Asset Serial Number")
    asset_name_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Asset Name")
    asset_condition_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Asset Condition")
    asset_location_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Asset Location")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_asset_allocated"


class EmployeeAccessControls(models.Model):
    user_employee  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    official_email_id   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Official Email Id")
    official_contact_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Official Contact Number")
    id_card_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "ID Card number")
    system_access_id   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "System Access Id")
    attendance_card_number   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Attendance Card Number")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_access_controls"


class EmployeeRegistrationUpdateDepartment(models.Model):
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User Id")
    employee_name   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Employee Name")
    current_designation   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Designation")
    new_designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, null=True, verbose_name="New Designation")
    current_department    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Department")
    new_department  = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, null=True, verbose_name="New Department")
    current_reporting_to = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Current Reporting To")
    new_reporting_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="New Reporting To")
    current_responsibilites   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Responsibilites")
    new_responsibilities = models.ForeignKey(ManageResponsibility, on_delete=models.SET_NULL, null=True, verbose_name="New Responsibility")
    current_location   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Location")
    new_location   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Location")
    current_salary    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Current Salary")
    new_salary    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "New Salary")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_registration_update_department"


LEAVE_STATUS = (
    ('all','all'),
    ('Actioned', "Actioned"),
   
)

LEAVE=(
    ('Approved','Approved'),
    ('Rejected','Rejected'),
    ('Put on hold','Put on hold'),
)

# Leaves
class EmployeeLeavesLeaveRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    no_days=models.IntegerField(default=0,blank=True,null=True,verbose_name='Number of leaves')
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Employee Name")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    type_of_leave  = models.ForeignKey(HolidaysandLeavesLeaveType, on_delete=models.SET_NULL, blank= False, null=True, verbose_name = "Type of Leave")
    leave_available    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Leave Available")
    start_date    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Start Date")
    end_date    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "End Date")
    total_leave    = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Total Leave")
    explaination    = models.TextField(default='', blank=True, null=True, max_length=200, verbose_name = "Explaination")
    status = models.BooleanField(default=0)
    leave_status=models.CharField(choices=LEAVE,default='',blank=True,null=True,max_length=100,verbose_name='Leave Status')
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_leaves_leave_request"


class EmployeeHRPoliciesUpdatePolicies(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True)
    policy_type  = models.ForeignKey(HRPoliciesPolicyType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Policy Type")
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    upload   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    effect_date = models.DateTimeField(blank = True, null = True, verbose_name = "Effect Date(Format:2019-08-05)")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.policy_type

    class Meta:
        db_table = "employee_hr_policies_update_policies_model"


class EmployeeHRPoliciesUpdateForm(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True)
    form_type  = models.ForeignKey(PoliciesandFormsManagementHRPolicies, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Form Type")
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    upload   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    effect_date = models.DateTimeField(blank = True, null = True, verbose_name = "Effect Date")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.form_type

    class Meta:
        db_table = "employee_hr_policies_update_form_model"


class EmployeeHrPoliciesUpdateCirculars(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True)
    circular_type  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Circular Type")
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    upload   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    effect_date = models.DateTimeField(blank = True, null = True, verbose_name = "Effect Date")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    def __str__(self):
        return self.circular_type

    class Meta:
        db_table = "employee_hr_policies_update_circulars_model"


CLAIM_STATUS = (
    (1, "Pending"),
    (2, "Approved"),
    (3, "Rejected"),
)

CLAIM_Reimbursement_STATUS = (
        ("Pending", "Pending"),
        ( "Approved", "Approved"),
        ("Rejected", "Rejected"),
    )
MODE_OF_TRAVEL=(
    ('Air','Air'),
    ('Road','Road'),
    ('Train','Train'),
    ('Own Arrangement','Own Arrangement'),
)

STAY_ARRANGEMENT=(
    ('Own Arrangement','Own Arrangement'),
    ('Company Arrangement','Company Arrangement'),
)

# Claim and Reimbursement
class EmployeeClaimandReimbursementSubmitClaims(models.Model):
    today_date=models.DateField(blank=True,null=True)
    claim_action=models.BooleanField(default=0)
    claim_status=models.CharField(max_length=100,default='pending',blank=True,null=True)
    ticket_expenses_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Ticket Expenses')
    food_expenses_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Food Expenses')
    stay_expenses_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Stay Expenses')
    other_expenses_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Other Expenses')
    total_expenses_1=models.IntegerField(default=0,blank=True,null=True ,verbose_name='Total Expenses')
    no_days_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='No of days')
    advance_taken_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Advance Taken')
    balance_claim_1=models.IntegerField(default=0,blank=True,null=True,verbose_name='Balance Claim')
    purpose_of_travel_1=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Purpose of Travel')
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    mode_of_travel_1=models.CharField(max_length=100,default='',blank=True,null=True,choices=MODE_OF_TRAVEL,verbose_name='Mode of Travel')
    employee_names_1 =  models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Employee Name ")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    start_date_1=models.DateField(blank=True,null=True,verbose_name='Start Date')
    end_date_1=models.DateField(blank=True,null=True,verbose_name='End Date')
    stay_arrangement_1=models.CharField(max_length=100,default='',blank=True,null=True,choices=STAY_ARRANGEMENT,verbose_name='Stay arrangement')
    location_1  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    approved_by  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True, related_name = "claim_approved_by")
    claim_date_1 = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Month/Year")
    claim_type_1  = models.ForeignKey(ManageClaimType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Claim Type")
    claim_period_1  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Period")
    claim_details_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Details")
    claim_amount_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Amount")
    claim_restriced_to_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Limit")
    comment_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Comment")
    approved_amount_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")
    upload_1   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    date_of_processing_1 = models.DateTimeField(blank = True, null = True, verbose_name = "Date")
    status = models.CharField( max_length=200,choices=CLAIM_Reimbursement_STATUS, default="",  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    claim_upload_document = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_claimand_reimbursement_submit_claims"


class EmployeeClaimandReimbursement(models.Model):
    claim_action=models.BooleanField(default=0)
    claim_status=models.CharField(max_length=100,blank=True,null=True,default='Pending')
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    location_1  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1 =  models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Employee Name ")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    start_date_1=models.DateField(blank=True,null=True,verbose_name='Start Date')
    end_date_1=models.DateField(blank=True,null=True,verbose_name='End Date')
    approved_date=models.CharField(default='',blank=True,null=True,max_length=100)
    approved_by  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True, related_name = "claim_approved")
    claim_date_1 = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Month/Year")
    claim_type_1  = models.ForeignKey(ManageClaimType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Claim Type")
    claim_period_1  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Period")
    claim_details_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Details")
    claim_amount_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Amount")
    claim_restriced_to_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Claim Limit")
    comment_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Comment")
    approved_amount_1 = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")
    upload_1   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    date_of_processing_1 = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Date")
    claim_upload_document = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)




class EmployeeClaimandReimbursementSubmitClaimsUpdateStatus(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    submit_claim  = models.OneToOneField(EmployeeClaimandReimbursementSubmitClaims, on_delete=models.CASCADE, blank= False, null=True)
    approved_amount = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")

    class Meta:
        db_table = "employee_claimand_reimbursement_submit_claims_update_status"



class EmployeeClaimandReimbursementSubmitReimbursement(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    
    employee_names =  models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Employee Name ")
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    approved_by  = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True, related_name = "reimbursement_approved_by")
    reimbursement_month_1 = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    reimbursement_type_1 = models.ForeignKey(ManageReimbursement, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Reimbursement Type")
    reimbursement_period_1  = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Reimbursement Period")
    amount_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount")
    maximum_limit_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Maximum Limit")
    comment_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Comment")
    upload_1   = models.FileField(upload_to='upload_hr_policies/%Y/%m/%d/', verbose_name="Upload(PDF File Only)")
    status = models.CharField( max_length=200,choices=CLAIM_Reimbursement_STATUS, default='Pending',  blank=True, null=True, verbose_name="Status")
    approved_amount_1   = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")
    approved_amount = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")
    
    date_of_processing = models.DateTimeField(blank = True, null = True, verbose_name = "Date of Processing")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_claimand_reimbursement_submit_reimbursement"

class EmployeeClaimandReimbursementSubmitReimbursementUpdateStatus(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    submit_claim  = models.OneToOneField(EmployeeClaimandReimbursementSubmitReimbursement, on_delete=models.CASCADE, blank= False, null=True)
    approved_amount = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name="Amount Approved")

    class Meta:
        db_table = "employee_claimand_reimbursement_submit_reimbursement_update_status"






class EmployeePayrollProcessingUpdateAdvances(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    location = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    department = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    month_and_year = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    advance_type = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    recovery_period  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    advance_amount  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    interest_rate   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    total_amount    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    recovery_amount    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    recovery_start_date    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_payroll_processing_update_advances"


class EmployeePayrollProcessingUpdateIncentives(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    location = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    department = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    month_and_year = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    incentive_type  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    incentive_period  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    incentive_amount  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Reimbursement Month")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_payroll_processing_update_incentive"


class EmployeePayrollProcessingUpdateTaxDeclaration(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location")
    assessment_year = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Assessment Year")
    tax_declaration_type  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax Declaration Type")
    tax_rule  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax Rule")
    exemption_claimed  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Exemption Claimed")
    exemption_approved  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Exemption Approved")
    maximum_limit  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=False, verbose_name="Status")
    status1 = models.CharField(max_length=200, choices=CLAIM_Reimbursement_STATUS, default='Pending',  blank=True, null=False, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    submission_date=models.CharField(default='',blank=True,null=True,max_length=100,verbose_name='Submission Date')
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)


    class Meta:
        db_table = "employee_payroll_processing_tax_declaration"

######


######
class EmployeePayrollProcessingUpdateTaxRecovery(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location")
    departments = models.CharField(max_length=200, blank=True, null=True, verbose_name="Departments")
    assessment_year = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Assessment Year")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    
    employee_names  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    year_to_date_salary  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax Recovery Type")
    annual_salary  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Annual Salary")
    total_tax_payable  =  models.CharField(max_length=200, blank = True, null = True, verbose_name = "Total Tax Payable")
    tax_already_recovered =  models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax already Recovered")
    recovery_during_current_month =  models.CharField(max_length=200, blank = True, null = True, verbose_name = "Recovery During Current Month")
    total_tax_recovered =  models.CharField(max_length=200, blank = True, null = True, verbose_name = "Total Tax Recovered")
    balance_tax_payable =   models.CharField(max_length=200, blank = True, null = True, verbose_name = "Balance Tax Payable")
    status = models.CharField(max_length=200, choices=CLAIM_Reimbursement_STATUS, default='Pending',  blank=True, null=False, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)


    class Meta:
        db_table = "employee_payroll_processing_tax_recovery"




class EmployeePayrollProcessingTaxCalculation(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    departments = models.CharField(max_length=200, blank=True, null=True, verbose_name="Department")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location")
    assessment_year = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Departments")
    year_to_date_salary  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax Declaration Type")
    annual_salary  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Tax Rule")
    other_income  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Exemption Claimed")
    total_income  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Exemption Approved")
    exemption  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    deduction  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    taxable_income  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    tax  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    cess   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    total_tax_payable    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    tax_deducted    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    tax_paid    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    balance_tax_payable    = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Maximum Limit")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_payroll_processing_tax_calculation"


class EmployeePayrollProcessingUpdateRecoveries(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True)
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    
    employee_names  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    departments = models.CharField(max_length=200, blank=True, null=True, verbose_name="Department")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location")
    month_and_year = models.CharField(max_length=200, blank = True, null = True)
    recovery_period   = models.CharField(max_length=200, blank = True, null = True)
    recovery_type  = models.CharField(max_length=200, blank = True, null = True)
    recovery_amount  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Exemption Claimed")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_payroll_processing_update_recoveries"


# Key Responsibility Areas & Targets

class ABC(models.Model):
    name=models.CharField(default='',max_length=200,blank=True,null=True,verbose_name='name')

    class Meta:
        db_table='abc_1'


class KeyResponsibilityUpdateKRA(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation",related_name='designation_1')
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department",related_name='department_1')
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Month & Year ")
    kra_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Type")
    kra_frequency_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Frequency")
    kra_details_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Details")
    kra_fulfilment   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Fulfilment")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer", related_name = "reporting_officer")
    kra_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Period")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "key_responsibility_update_target"


class KeyResponsibilityUpdateTargets(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Target Month ")
    target_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Type")
    target_name_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Name")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer",related_name='reporting_officer_1')
    target_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Period")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table='key_responsibility_update_KRA'


class KeyResponsibilityApproveKRA(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Month & Year ")
    approve_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Type")
    approve_details_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Details")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer", related_name = "reporting_officer_2")
    approve_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Period")
    approval_status=models.CharField(max_length=200, blank = True, null = True, verbose_name = 'Approval Status')
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table='key_responsibility_approve_kra'



class KeyResponsibilityApproveTargets(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Target Month ")
    target_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Type")
    target_name_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Name")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer",related_name='reporting_officer_3')
    target_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Period")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Aproval Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table='key_responsibility_approve_targets'

class keyResponsibilityKRAPerformance(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Month & Year ")
    kra_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Type")
    kra_frequency_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Frequency")
    kra_details_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Details")
    kra_fulfilment   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Fulfilment")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer", related_name = "officer_reporting")
    kra_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "KRA Period")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table='key_responsibility_kra_performance'


class keyResponsibilityKRAPerformanceAchievement(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User Id")
    employee_id_1  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Employee Id")
    employee_names_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation_1 = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department_1 = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location_1 = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_1 = models.DateField(blank = True, null = True, verbose_name = "Target Month ")
    target_type_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Type")
    target_name_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Name")
    reporting_officer_1   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Reporting Officer",related_name='reporting_officer_6')
    target_period_1=models.CharField(max_length=200, blank = True, null = True, verbose_name = "Target Period")
    kra_fulfilment   = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Fulfilment")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table='key_responsibility_target_achievement'








RESIGNATION_STATUS = (
    (1, "Pending"),
    (2, "Approved"),
    (3, "Full and Final Settlement"),
    (4, "Rejected"),
    (5, "Release"),
)

COMMON_RESIGNATION_STATUS = (
    (1, "Pending"),
    (2, "Inprocess"),
    (3, "Complete"),
)
FINAL_SAL_STATUS = (
    ("Pending", "Pending"),
    
    ( "Setter", "Setter"),
)

class EmployeeExitEmployeeResignation(models.Model):
    exit_recommended=models.BooleanField(default=0)
    exit_reject=models.BooleanField(default=0)
    approve=models.BooleanField(default=0)
    current_status=models.CharField(default='pending',max_length=100,blank=True,null=True,verbose_name='Current Status')
    upload_FandF=models.FileField(upload_to='upload_report/%Y/%m/%d/', blank=True, null=True, verbose_name="Upload F&F statement")
    upload_resignation=models.FileField(upload_to='upload_report/%Y/%m/%d/', blank=True, null=True, verbose_name="Upload Resignation Letter")
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Employee Id")
    employee_id = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Employee Id")
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    reporting_officer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name = "Reporting Officer", related_name = "reporting_officers")
    resignation_date = models.DateField(blank = True, null = True, verbose_name = "Resignation Date")
    last_date = models.DateField(blank = True, null = True, verbose_name = "Last Date")

    reasons_for_resignation  = models.CharField(max_length=500, blank = True, null = True, verbose_name = "Reasons for Resignation")
    notice_period_applicability = models.IntegerField(choices=YESNO, default=1,  blank=True, null=True, verbose_name="Notice Period")
    notice_period_required  = models.IntegerField(choices=YESNO, default=0,  blank=True, null=True,  verbose_name = "Notice Period Required")
    notice_period_waived   = models.IntegerField(choices=YESNO, default=0,  blank=True, null=True,  verbose_name = " Notice Period Waived")
    notice_period_to_be_served   = models.IntegerField(default=0,  blank=True, null=True,  verbose_name = "Notice Period to be Served(In days)")
    status = models.IntegerField(choices=RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    notice_pay_deducted = models.IntegerField(choices=YESNO, default=0,  blank=True, null=True, verbose_name="Notice Pay Deducted")
    status_of_assets_allocated = models.IntegerField(choices=COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status of Assets Allocated")
    status_of_responsibility_handover = models.IntegerField(choices=COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status of Responsibility Handover")
    status_of_formalities_completed_status_of_exit_interview  = models.IntegerField(choices=COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status of Formalities completed  Status of Exit Interview")
    status_of_relieving_letters_status_of_full_and_final_settlement  = models.IntegerField(choices=COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status of Relieving Letters  Status of Full and Final Settlement")
    final_salary_status  = models.IntegerField(choices=COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Final Salary Status")
    
    final_sal_status  = models.CharField(max_length=200,choices=FINAL_SAL_STATUS, default='',  blank=True, null=True, verbose_name="Final Salary Status")
    net_salary = models.CharField(max_length=200, blank = True, null = True, verbose_name="Impact on Salary")

    approved_date = models.DateTimeField(blank = True, null = True)
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_exit_employee_resignation"
##
##
FREQUENCY_Leave=(

    ('Monthly','Monthly'),
    ('Half Yearly','Half Yearly'),
    ('Yearly','Yearly'),

)
class LeaveandHolidaysManagementUpdateLeavesQuota(models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Employee Id")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")

    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    first_name  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Name",related_name='first_names')
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    leave_type  = models.ForeignKey(HolidaysandLeavesLeaveType, on_delete=models.SET_NULL, blank= True, null=True, verbose_name = "Leave Type")
    financial_year = models.ForeignKey(ManageFinancialYear, on_delete=models.SET_NULL, blank= True, null=True, verbose_name="Financial Year")
    leave_balance = models.CharField(max_length=200, blank = True, null = True, verbose_name="Balance in Beginning ")
    leave_added = models.CharField(max_length=200, blank = True, null = True, verbose_name="Leave Added")
    frequency_of_leave = models.CharField(choices=FREQUENCY_Leave,max_length=200, blank = True, null = True, verbose_name="Frequency of Leave")
    impact_on_salary   = models.IntegerField(choices=YESNO, default=0,  blank=True, null=True,  verbose_name = "Impace on Salary")
    maximum_limit_carry_forward_allowed   = models.CharField(max_length=200, blank = True, null = True,  verbose_name = "Maximum Limit")
    total_leave=models.CharField(max_length=200, blank = True, null = True, verbose_name="Total Leave")
    encashment_allowed   = models.IntegerField(choices=YESNO, default=0,  blank=True, null=True,  verbose_name = "Encashment allowed")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "leave_and_holidays_management_leaves"
        unique_together = ('user', 'leave_type',)


OVERTIME_TYPE = (
    ('Office', 'Office'),
    ('Field', 'Field'),
    ('On Tour', 'On Tour'),
    ('On Duty', 'On Duty'),
)

ATTENDENCE_STATUS = (
    ('Pending', 'Pending'),
    ('Accept', 'Accept'),
    ('Reject', 'Reject'),
)

MODE_OF_ATTENDANCE=(
    ('Manual','Manual'),
    ('Online','Online'),
    ('Bio_Matrix','Bio Matrix'),
)





class OvertimeManagementUpdateOvertime(models.Model):
    action_status=models.BooleanField(default=0)
    overtime_status=models.CharField(max_length=100,default='pending',blank =True,null=True)
    approved_date=models.DateField(blank=True,null=True)
    date=models.DateField(blank=True,null=True,verbose_name='Date')
    user  = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "Employee Id")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    employee_names  = models.CharField(max_length=200, blank = True, null = True, verbose_name = "Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    month_and_year_date = models.DateField(blank = True, null = True, verbose_name = "Month/Year")
    overtime_start = models.CharField(max_length=200, blank = True, null = True, verbose_name="Login Time")
    overtime_end = models.CharField(max_length=200, blank = True, null = True, verbose_name="Logout Time")
    total_hours = models.IntegerField(default =0, blank = True, null = True, verbose_name="Total Hours")
    reason = models.TextField(blank = True, null = True, verbose_name="Reason")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    overtime_type = models.CharField(max_length=100,choices= OVERTIME_TYPE, default=0,  blank=True, null=True, verbose_name = "OvertimeType")
    mode_of_attendance = models.CharField(max_length=100,choices= MODE_OF_ATTENDANCE, default=0,  blank=True, null=True, verbose_name = "Mode of attendance")
    login_address = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Login Location")
    logout_address = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Logout Location")
    login_time = models.DateTimeField(blank = True, null = True, verbose_name = "Login  Time")
    logout_time = models.DateTimeField(blank = True, null = True, verbose_name = "Logout Time")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "over_time_management_update_over_time"

CLAIM_STATUS = (
    ("Pending", "Pending"),
    ( "Approved", "Approved"),
    ("Rejected", "Rejected"),
)

ARRANGEMENET=(
    ('Own Arrangement','Own Arrangement'),
    ('Company Arrangement','Company Arrangement'),
)
class TravelClaimManagementTravelConveyanceTravelRequest(models.Model):
    action=models.BooleanField(default=0)
    ticket_expenses=models.IntegerField(blank=True,null=True,verbose_name='Ticket Expenses')
    food_expenses=models.IntegerField(blank=True,null=True,verbose_name='Food Expenses')
    stay_expenses=models.IntegerField(blank=True,null=True,verbose_name='Stay Expenses')
    other_expenses=models.IntegerField(blank=True,null=True,verbose_name='Other Expenses')
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    mode_of_travel  = models.ForeignKey(TravelandClaimTravelManagementModeofTravel, on_delete=models.SET_NULL, blank= True, null=True, verbose_name = "Mode of Travel")
    no_of_days = models.CharField(max_length=200, blank = True, null = True, verbose_name="No of Days")
    travel_start_date =  models.DateField(blank = True, null = True, verbose_name="Start Date")
    travel_end_date =  models.DateField(blank = True, null = True, verbose_name="End Date")
    stay_arrangement = models.CharField(max_length=100,choices=ARRANGEMENET, default=0,  blank=True, null=True, verbose_name="Stay Arrangement")
    total_travel_cost = models.CharField(max_length=200, blank = True, null = True, verbose_name="Total Travel Cost")
    advance_required  = models.CharField(max_length=200, blank = True, null = True, verbose_name="Advance Required")
    reasons_for_travel   = models.CharField(max_length=200, blank = True, null = True, verbose_name="Purpose for Travel")
    status = models.CharField(max_length=200,choices=CLAIM_STATUS, default='Pending',  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "travel_claim_management_travel_conveyance_travel_requests"

REQUEST_STATUS = (
    (1, "Pending"),
    (2, "Processing"),
    (3, "Processed "),
)


REQUEST_EMP_STATUS = (
    ("Pending", "Pending"),
    ("Processing", "Processing"),
    ("Processed", "Processed "),
)

YES_NO =(
    ("YES","YES"),
    ("NO","NO")
)
# Employee Advances 
class EmployeeAdvancesSubmitAdvanceRequest(models.Model):
    today_date=models.DateField(blank=True,null=True,verbose_name='Approved Date')
    action_status=models.CharField(blank=True,null=True,max_length=100)
    action=models.BooleanField(default=0)
    request_date=models.DateField(blank=True,null=True,verbose_name='Request Date')
    month_and_year=models.DateField(blank=True,null=True,verbose_name='Month/Year')
    user   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    approved_by   = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True, related_name = "employee_advance_approved_by")
    advance_type_1   = models.ForeignKey(ManagePayRollDefineAdvances, on_delete=models.SET_NULL, blank= True, null=True, verbose_name = "Advance Type")
    advance_amount_1 = models.CharField(max_length=200, blank = True, null = True, verbose_name="Recovery Amount")
    recovery_start_from_1 = models.DateField(blank = True, null = True, verbose_name="Recovery Start Date")
    recovery_end_from_1 = models.DateField(blank = True, null = True, verbose_name="Recovery End Date")
    interest_rate=models.IntegerField(blank=True,null=True,verbose_name='Interest Charged')
    recovery_period_1 = models.CharField(max_length=200, blank = True, null = True, verbose_name="Period")
    justification_1 = models.CharField(max_length=200, blank = True, null = True, verbose_name="Purpose")
    status = models.CharField(max_length=200,choices=REQUEST_EMP_STATUS, default='Pending',  blank=True, null=True, verbose_name="Approval Status")
    advance_approved_1 = models.CharField(max_length=200,choices=YES_NO, default="NO",  blank=True, null=True, verbose_name="Advance Approved")
    payment_status  = models.CharField(max_length=200,choices=YES_NO, default="NO",  blank=True, null=True, verbose_name="Payment Status ")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_advances_submit_advance_request"

# class EmployeePerquisite(models.Model):
#     month_and_year=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Month/Year')
#     location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
#     employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
#     employee_name=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Employee name')
#     designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
#     department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
#     perquisite_type=models.
# Incentive &  Bonus 
class EmployeeAdvancesSubmitIncentiveBonus(models.Model):
    today_date=models.DateField(blank=True,null=True)
    action_status=models.CharField(max_length=100,default='pending',blank=True,null=True)
    action=models.BooleanField(default=0)
    maximum_limit=models.IntegerField(blank = True, null = True, verbose_name="Maximum Limit")
    period=models.DateField(blank=True,null=True,verbose_name='Period')
    user   = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, verbose_name = "User")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    date=models.CharField(default='',max_length=100,blank=True,null=True,verbose_name='Month/Year')
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    location = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    approved_by   = models.ForeignKey(User, on_delete=models.SET_NULL, blank= True, null=True, related_name = "employee_incentive_approved_by")
    incentive_type = models.CharField(max_length=200, blank = True, null = True, verbose_name="Incentive Type")
    incentive_period = models.CharField(max_length=200, blank = True, null = True, verbose_name="Incentive Period")
    incentive_amount = models.CharField(max_length=200, blank = True, null = True, verbose_name="Incentive Amount")
    status = models.CharField(max_length=200,choices=REQUEST_EMP_STATUS, default="Pending",  blank=True, null=True, verbose_name="Approval Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_advances_submit_incentive_bonus"



class ManageProductTrainingSendWishToAttend(models.Model):
    traning_id = models.ForeignKey(ManageKnowledgeProductTraining, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Training")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="User")
    status = models.IntegerField(choices= COMMON_RESIGNATION_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    is_active = models.BooleanField(default=1, verbose_name="Is Active")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "manage_product_training_send_wish_to_attend"


class PayrollStatutoryDeductions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    deduction_type = models.ForeignKey(ManagePayRollStatutoryDeductions, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Deduction Type")
    employer_contribution = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employer Contribution")
    employee_contribution = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Contribution")
    month_and_year= models.DateField(blank = True, null = True, verbose_name="Month and Year")
    others = models.CharField(max_length=200, blank = True, null = True, verbose_name="Others")
    total_deduction = models.CharField(max_length=200, blank = True, null = True, verbose_name="Total Deduction")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    is_active = models.BooleanField(default=1, verbose_name="Is Active")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "payroll_statuary_deduction"



class PayrollSalaryVoucher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    month_and_year= models.CharField(max_length=200, blank = True, null = True, verbose_name="Month and Year")
    gl_code = models.CharField(max_length=200, blank = True, null = True, verbose_name="GL Code")
    particulars = models.CharField(max_length=200, blank = True, null = True, verbose_name="Particulars")
    debit_amount = models.CharField(max_length=200, blank = True, null = True, verbose_name="Debit Amount")
    credit_amount = models.CharField(max_length=200, blank = True, null = True, verbose_name="Credit Amount")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    is_active = models.BooleanField(default=1, verbose_name="Is Active")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "payroll_salary_voucher_data"


class PayrollSalaryDisbursement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, verbose_name="User")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.SET_NULL, blank = True, null = True, verbose_name = "Employee Id")
    
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    month_and_year= models.CharField(max_length=200, blank = True, null = True, verbose_name="Month and Year")
    bank_name = models.CharField(max_length=200, blank = True, null = True, verbose_name="Bank Name")
    ifsc_code = models.CharField(max_length=200, blank = True, null = True, verbose_name="IFSC Code")
    account_number = models.CharField(max_length=200, blank = True, null = True, verbose_name="Account Number")
    amount = models.CharField(max_length=200, blank = True, null = True, verbose_name="Amount")
    mode_of_payment = models.CharField(max_length=200, blank = True, null = True, verbose_name="Mode of Payment")
    date_of_payment  =  models.CharField(max_length=200, blank = True, null = True, verbose_name="Date of Payment")
    status = models.IntegerField(choices=CLAIM_STATUS, default=1,  blank=True, null=True, verbose_name="Status")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    is_active = models.BooleanField(default=1, verbose_name="Is Active")
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = "payroll_salary_disbursement"


##
days_in_month = (
    (25,25),
    ( 24,24),
    (23,23),
    (22,22),
)
monthly_off = (
    (8,8),
    ( 6,6),
    (5,5),
    (4,4),
)
working_days = (
    (24,24),
    (23,23),
    (22,22),
    (21,21)
   
)
PAYROLL_STATUS = (
    ("Pending", "Pending"),
    ( "Approved", "Approved"),
    ("Rejected", "Rejected"),
)
class EmployeePayrollProcessed(models.Model):
    location  = models.ForeignKey(ManageBranch, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    
    month_and_year= models.ForeignKey(EmployeePayrollProcessingUpdateAdvances,on_delete=models.CASCADE, blank = True, null = True, verbose_name="Month and Year")
    employee_id  = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank = True, null = True, verbose_name = "Employee Id",related_name='employee_ids')
    first_name =  models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank = True, null = True, verbose_name = "Employee Name", related_name='employee_name')
    employee_names = models.CharField(max_length=200, blank = True, null = True, verbose_name="Employee Name")
    days_in_month = models.IntegerField(choices=days_in_month, default="",  blank=True, null=True, verbose_name="Days In Month")
    monthly_off = models.IntegerField(choices=monthly_off, default="",  blank=True, null=True, verbose_name="Month Off")
    working_days  = models.IntegerField(choices=working_days, default="",  blank=True, null=True, verbose_name="Working Days")
    holidays = models.CharField(max_length=200, blank = True, null = True, verbose_name="Holidays")
    leave_balance = models.ForeignKey(LeaveandHolidaysManagementUpdateLeavesQuota,on_delete=models.CASCADE, blank = True, null = True, verbose_name="Total Leave ")
    leave_type  = models.ForeignKey(HolidaysandLeavesLeaveType, on_delete=models.SET_NULL, blank= True, null=True, verbose_name = "Leaves Type")
    leave_without_pay = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Leave withOut Pay")
    joining_grade_offered = models.ForeignKey(EmployeeRegistrationUpdateRegistrationJoiningDetails,on_delete=models.SET_NULL, blank = True, null = True, verbose_name="Grad")
    pan_card   = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails,on_delete=models.CASCADE, blank=True, null=True, verbose_name = "Pan Card")
    pan_card_1   = models.CharField(max_length=200, blank=True, null=True, verbose_name = "Pan Card")
    
    basic_pay = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Basic Pay")
    hra_allowances = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="HRA Allowances")
    conveyance = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Conveyance")
    claim_type   = models.ForeignKey(ManageClaimType, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Claim ")
    reimbursement_type_1 = models.ForeignKey(ManageReimbursement, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Reimbursement Type")
    Incentive_1   = models.CharField(max_length=200, blank = True, null = True, verbose_name="Incentive Gross Salary")
    performance_bonus  = models.CharField(max_length=200, blank = True, null = True, verbose_name="Performance Bonus Gross Salary")
    basic_pay  = models.CharField(max_length=200, blank = True, null = True, verbose_name="Basic Pay")
    hra_allowances_1  = models.CharField(max_length=200, blank = True, null = True, verbose_name="HRA Allowances")
    conveyance_1 =  models.CharField(max_length=200, blank = True, null = True, verbose_name="Conveyance")
    claim_amount_1 = models.ForeignKey( EmployeeClaimandReimbursementSubmitClaims, on_delete=models.CASCADE ,blank = True, null = True, verbose_name="Conveyance")
    Reimbursement =	models.CharField(max_length=200, blank = True, null = True, verbose_name="Conveyance")
    incentive_2  =	 models.CharField(max_length=200, blank = True, null = True, verbose_name="Incentive Salary Earned")
    total  = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Total Gross Salary")
    performance_bonus	=	 models.CharField(max_length=200, blank = True, null = True, verbose_name="Performance Bonus Salary Earned")	 
    total_1	=	 models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Total Salary Earned")
    pf = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="PF Deduction Details")	
    esic = models.CharField(max_length=200, blank = True, null = True, verbose_name="ESIC Deduction Details")
    absent	 = models.CharField(max_length=200, blank = True, null = True, verbose_name="Absent Deduction Details")
    income  = models.CharField(max_length=200, blank = True, null = True, verbose_name="Income Deduction Details")
    tax	 = models.CharField(max_length=200 ,blank = True, null = True, verbose_name="TAX Deduction Details")
    loan_recovery	= models.CharField(max_length=200 ,blank = True, null = True, verbose_name="Loan Recovery Deduction Details")
    total_2	= models.CharField(max_length=200, blank = True, null = True, verbose_name="Total Deduction Details")
    net_salary_payable = models.CharField(max_length=200, blank = True, null = True, verbose_name="Total Salary Earned")
    bank_name = models.CharField(max_length=200, blank = True, null = True, verbose_name="Bank Name")
    ifsc_code = models.CharField(max_length=200, blank = True, null = True, verbose_name="IFSC Code")
    account_number = models.CharField(max_length=200,  blank = True, null = True, verbose_name="Account Number")
    amount = models.CharField(max_length=200  ,blank = True, null = True, verbose_name="Amount")
    mode_of_payment = models.CharField(max_length=200, blank = True, null = True, verbose_name="Mode of Payment")
    date_of_payment  =  models.CharField(max_length=200, blank = True, null = True, verbose_name="Date of Payment")
    status = models.CharField(max_length=200,choices=PAYROLL_STATUS, default="Pending",  blank=True, null=True, verbose_name="Status")
    date_of_processing = models.DateTimeField(blank = True, null = False, verbose_name = "Date of Processing")
    upload = models.FileField(upload_to='documents/%Y/%m/%d/',verbose_name="Template Upload")
    upload_1   = models.FileField(upload_to='upload_report/%Y/%m/%d/', verbose_name="Upload")
    
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)

    class Meta:
        db_table = "employee_payroll_processed"

   


class UserLoginApiLogsAttendance(models.Model):   
    approve_status=models.CharField(max_length=100,blank=True,null=True,default='')
    approve_action=models.BooleanField(default=0)
    correction_status=models.BooleanField(default=0)
    date=models.DateField(blank=True,null=True,verbose_name='Date')
    correction_date=models.DateField(blank=True,null=True)
    approval_date=models.DateField(blank=True,null=True)
    attendance_mode=models.CharField(default='',choices=MODE_OF_ATTENDANCE,max_length=100,blank=True,null=True,verbose_name='Mode of Attendance')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank= False, null=True, verbose_name = "Employee Id")
    employee_id = models.ForeignKey(EmployeeRegistrationUpdateRegistrationPersonalDetails, on_delete=models.CASCADE, blank = True, null = True, verbose_name = "Employee Id")
    employee_names = models.CharField(unique = True, default='',  blank=True, null=True, max_length = 250, verbose_name = "Employee Name")
    location  = models.ForeignKey(ManageBranch, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Location")
    department = models.ForeignKey(ManageDepartment, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Department")
    designation = models.ForeignKey(ManageDesignation, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Designation")
    responsibilities = models.ForeignKey(ManageResponsibility, on_delete=models.SET_NULL,  null=True, verbose_name="Responsibility")
    user_pics = models.ImageField(upload_to = 'user_attendence_pics/', default = '', blank= False, null=True, verbose_name = "Login User Pics")
    logout_user_pics = models.ImageField(upload_to = 'user_attendence_pics/', default = '', blank= False, null=True, verbose_name = "Logout User Pics")
    attendance_type = models.CharField(max_length=100,choices= ATTENDENCE_TYPE, default=0,  blank=True, null=True, verbose_name = "Attendance Type")
    logout_attendance_type = models.IntegerField(choices= ATTENDENCE_TYPE, default=0,  blank=True, null=True, verbose_name = "Logout Attendance Type")
    address = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Login Location")
    logout_address = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Logout Location")
    latitude = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    logout_latitude = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    longitude = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    logout_longitude = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    login_true = models.BooleanField(default=0)
    logout_true = models.BooleanField(default=0)
    logout_true1 = models.BooleanField(default=0)
    notification_send = models.BooleanField(default=0)
    added = models.DateTimeField(auto_now_add=True, verbose_name = "Login  Time")
    login_time = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Login  Time(10:53)")
    logout_time = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Logout Time(10:53)")
    month_year=models.DateField(blank=True,null=True,verbose_name='Month/Year')
    date_field = models.CharField(max_length=100,blank = True, null = True, verbose_name = "Month/Year")
    approval_level = models.ForeignKey(ApprovalMatrixiDefineApprovalLevel, blank=False, null=True, on_delete=models.SET_NULL, verbose_name="Approval Level")
    approval_level_all_status   = models.CharField(default='', blank=True, null=True, max_length=200)
    attendance_status = models.CharField(max_length=100,choices= ATTENDENCE_STATUS, default='',  blank=True, null=True, verbose_name = "Correction Status")
    attendance_correction = models.CharField(default='', blank=True, null=True, max_length=200, verbose_name = "Correction")
    is_active = models.BooleanField(default=1)


    class Meta:
        db_table = "user_login_api_logs_attendance"