from employee_website.views import *
from django.conf.urls import include
from django.conf.urls import url

# Knowledge and Training
urlpatterns = [
    url(r'^hrms/employeeservices/recruitement/updateconsultants/list/$', EmployeeServicesRecruitementUpdateConsultantsList.as_view(), name='crm_website_employeeservices_recruitement_updateconsultants_list'),

    url(r'^hrms/employeeservices/recruitement/updateconsultants/add/$', AddEditCrmEmployeeServicesRecruitementUpdateConsultants.as_view(), name='crm_website_employeeservices_recruitement_updateconsultants_add'),

    url(r'^hrms/employeeservices/recruitement/updateconsultants/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EditCrmEmployeeServicesRecruitementUpdateConsultants, name="crm_website_employeeservices_recruitement_updateconsultants_edit"),
    url(r'^hrms/employeeservices/recruitement/updateconsultants/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementUpdateConsultantsDelete.as_view(), name='crm_website_employeeservices_recruitement_updateconsultants_delete'),

    url(r'^hrms/employeeservices/recruitement/createrequirement/list/$', EmployeeServicesRecruitementCreateRequirementList.as_view(), name='crm_website_employeeservices_recruitement_createrequirement_list'),
   

    url(r'^hrms/employeeservices/recruitement/createrequirement/add/$', AddEditCrmEmployeeServicesRecruitementCreateRequirement.as_view(), name='crm_website_employeeservices_recruitement_createrequirement_add'),

    url(r'^hrms/employeeservices/recruitement/createrequirement/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementCreateRequirement.as_view(), name="crm_website_employeeservices_recruitement_createrequirement_edit"),
    url(r'^hrms/employeeservices/recruitement/createrequirement/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementCreateRequirementDelete.as_view(), name='crm_website_employeeservices_recruitement_createrequirement_delete'),
    url(r'^hrms/employeeservices/approval/vacancy/(?P<id>[0-9,a-z,A-Z]+)/$', ApprovalVacancies.as_view(), name='approval_vacancy_update_status'),
                                      
                                      
                                      
                                        ############################### Approve Vacancies#########################
    url(r'^hrms/employeeservices/recruitement/approvevacancies/reviewed/list/$', EmployeeServicesRecruitementReviewedRequirementList.as_view(), name='crm_website_employeeservices_recruitement_approve_reviewed_list'),
    url(r'^hrms/employeeservices/recruitement/approve/requirement/list/$',EmployeeServicesRecruitementApproveVacanciesList.as_view(), name='crm_website_employeeservices_recruitement_approve_vacancies_list'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesCreatedApproveRequirementView.as_view(), name='crm_website_employeeservices_recruitement_approve_requirement_update'),
    #url(r'^hrms/employeeservices/recruitement/approvevacancies/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementApproveVacancies.as_view(), name='crm_website_employeeservices_recruitement_approvevacancies_update'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementReviewedRequirementDelete.as_view(), name='crm_website_employeeservices_recruitement_approve_requirement_delete'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/referedback/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementReferedBack.as_view(),name='employeeservices_recruitement_refered_back'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementrejected.as_view(),name='employeeservices_recruitement_hr_recommended_rejected'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/putonhold/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementputonhold.as_view(),name='employeeservices_recruitement_hr_recommended_putonhold'),
    url(r'^hrms/employeeservices/recruitement/approverequirement/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementApproveRequirementEdit,name='employeeservices_recruitement_approve_requirement_modify'),

    url(r'^hrms/employeeservices/recruitement/approvevacancies/hr/recommended/list/$', EmployeeServicesRecruitementAllRequirementList.as_view(), name='crm_website_employeeservices_recruitement_approve_hr_recommended'),
    url(r'^hcm/employeeservicers/approval/action/(?P<id>[0-9,a-z,A-Z]+)/$', EditEmployeeServiceRecruitementApprovalRequirementAction, name='hcm_approval_action'),
 


    url(r'^hrms/employeeservices/recruitement/approvevacancies/recommended/list/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementApprovedRecommendedRequirementsList.as_view(), name='crm_website_employeeservices_recruitement_approved_recommended'),
               
                           
                           
                           
                            ######################################### Show Requirement ###########################################################################33
    
    url(r'^hrms/employeeservices/recruitement/approvevacancies/list/$', EmployeeServicesRecruitementApproveVacanciesList.as_view(), name='crm_website_employeeservices_recruitement_approvevacancies_list'),

    url(r'^hrms/employeeservices/recruitement/ShowRequirement/list/$', EmployeeServicesShowRequirement.as_view(), name='crm_website_employeeservices_show_requirement_list'),
    #url(r'^hrms/employeeservices/recruitement/ShowRequirement/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesShowRequirement.as_view(), name='crm_website_employeeservices_show_requirement_update'),    

    url(r'^hrms/employeeservices/recruitement/ShowRequirement/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EditEmployeeServicesShowRerquirement, name='crm_website_employeeservices_show_requirement_update_edit'),

    url(r'^hrms/employeeservices/recruitement/Showrequirement/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementShowRequirementDelete.as_view(),name='employeeservices_show_requirement_delete'),

    url(r'^hrms/employeeservices/recruitement/Showrequirement/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementRecommendedRequirement,name='employeeservices_recommended_requirement_modify'),
    url(r'^hrms/employeeservices/recruitement/Showrequirement/view/(?P<id>[0-9,a-z,A-Z]+)/$',RecommendedView.as_view(),name='recommended_view'),
    ##################################################################################################################################
                   

                     ####################################### Document Request ############################################
    url(r'^hrms/employeeservices/recruitement/document/request/list/$', EmployeeServicesRecruitementDocumentRequestList.as_view(), name='crm_website_employeeservices_document_request_list'),

    url(r'^hrms/employeeservices/recruitement/document/request/list/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementDocumentRequestList.as_view(), name='crm_website_employeeservices_document_request_list'),

    url(r'^hrms/employeeservices/recruitement/document/request/update/$', EmployeeServicesRecruitementDocumentRequestadd.as_view(), name='crm_website_employeeservices_document_request_add'),

    url(r'^hrms/employeeservices/recruitement/document/request/create/list/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServiceRecruitemetCandidatedocumentrequest, name='crm_website_employeeservices_create_document_list'),
    
    url(r'^hrms/employeeservices/recruitement/document/request/create/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesrecruitementDocumentRequestDelete.as_view(), name='crm_website_employeeservices_create_document_delete'),
    url(r'^hrms/employeeservices/recruitement/document/request/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementDocumentRequestEdit,name='document_request_modify'),


                    ########################################################################################################
    url(r'^hrms/employeeservices/document_uploa/$', Document_Upload.as_view(), name='document_upload_req'),
    url(r'^hrms/employeeservices/document_verification/$',Verification_upload.as_view(),name='document_verification_req'),
                    ####################################### Update Documents ###################################################################
    url(r'^hrms/employeeservices/recruitement/documentupdates/list/$', EmployeeServicesRecruitementUpdateDocumentsList.as_view(), name='crm_website_employeeservices_update_documents_list'),
    url(r'^hrms/employeeservices/recruitement/documentupdates/update/$', EmployeeServicesRecruitementUpdateDocumentsadd.as_view(), name='crm_website_employeeservices_update_documents_add'),
    url(r'^hrms/employeeservices/recruitement/documentupdates/upload/(?P<id>[0-9,a-z,A-Z]+)/$',employeeservicedocumentrequest,name='crm_website_employeeservices_upload_document'),
    url(r'^hrms/employeeservices/recruitement/document/updates/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesdocumentrequestdelete.as_view(),name='crm_website_employeeservices_upload_document_delete'),
    url(r'^hrms/employeeservices/recruitement/document/updates/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementUpdateDocumentEdit,name='update_dcoument_modify'),
    ############################################# HR review ########################################################################

    url(r'^hrms/employeeservices/recruitement/Approve/HRrequirement/list/$', EmployeeServicesRecruitementHrReviewApproveList.as_view(), name='crm_website_employeeservices_recruitement_hr_review_approve_requirement_list'),

    url(r'^hrms/employeeservices/recruitement/HRreview/Showrequirement/list/$', EmployeeServicesRecruitementHrReviewList.as_view(), name='crm_website_employeeservices_recruitement_hr_review_requirement_list'),

    url(r'^hrms/employeeservices/recruitement/HRreview/action/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementHrReview,name='edit_employee_recruitement'),

    url(r'^hrms/employeeservices/recruitement/HRrequirement/recommended/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementHrReviewedList.as_view(), name='crm_website_employeeservices_recommended_by_Hr'),

    url(r'^hrms/employeeservices/recruitement/HRrequirement/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementRejected.as_view(), name='crm_website_employeeservices_not_recommended_by_Hr'),
    url(r'^hrms/employeeservices/recruitement/HRrequirement/putonhold/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPutOnHold.as_view(), name='crm_website_employeeservices_rejected'),
    url(r'^hrms/employeeservices/recruitement/HRrequirement/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementHRRequirement,name='employeeservices_hr_review_modify'),

    url(r'^hrms/employeeservices/recruitement/HRreview/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementHrReview.as_view(), name='crm_website_employeeservices_recruitement_hr_review_of_requirement_update'),
    url(r'^hrms/employeeservices/recruitement/HRreview/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EditEmployeeServiceRecruitementHrReview, name='crm_website_employeeservices_hr_review_of_requirement_update_edit'),
    url(r'^hrms/employeeservices/recruitement/HRreview/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementHrReviewDelete.as_view(), name='crm_website_employeeservices_hr_review_of_requirement_delete'),
    url(r'^hrms/employeeservices/recruitement/HRreview/requirement/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementHrReviewDelete2.as_view(),name='crm_website_hr_recommended_delete'),
    url(r'^hrms/employeeservices/recruitement/HRreview/modify/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementHrReview.as_view(), name='crm_website_employeeservices_hr_review_of_requirement_modify'),

                            
                            
                            
                                        
                                        #####################################Publish Jobs ########################################################

    url(r'^hrms/employeeservices/recruitement/publishvacancies/list/$', EmployeeServicesRecruitementPublishVacanciesList.as_view(), name='crm_website_employeeservices_recruitement_publishvacancies_list'),
    url(r'^hrms/employeeservices/recruitement/publishvacancies/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementPublishVacancies.as_view(), name='crm_website_employeeservices_recruitement_publishvacancies_update'),
    url(r'^hrms/employeeservices/recruitement/inviteresume/add/$', AddEditCrmEmployeeServicesRecruitementInviteResume.as_view(), name='crm_website_employeeservices_recruitement_inviteresume_add'),
    url(r'^hrms/employeeservices/recruitement/publishvacancies/recommended/list/$', EmployeeServicesRecruitementAllPublishVacanciesList.as_view(), name='crm_website_employeeservices_recruitement_recommended_publishvacancies_list'),
    url(r'^hrms/employeeservices/recruitement/publish/vacancies/form/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeservicesRecruitementPublishVacancies, name='crm_website_employeeservices_recruitement_recommended_publish_vacancies'),
    url(r'^hrms/enmployeeservices/recruitement/publish/vacancies/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanicesRejected.as_view(),name='employeeservices_recommended_publish_vacancies_rejected'),
    url(r'^hrms/enmployeeservices/recruitement/publish/vacancies/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanicesDelete.as_view(),name='crm_website_employeeservices_recruitement_publish_jobs_delete'),
    url(r'^hrms/enmployeeservices/recruitement/publish/vacancies/putonhold/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanciesPutOnHold.as_view(),name='crm_website_employeeservices_recruitement_publish_jobs_put_on_hold'),
    url(r'^hrms/enmployeeservices/recruitement/publish/vacancies/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementPublishJobsEdit,name='crm_website_employeeservices_recruitement_publish_jobs_modify'),
    url(r'^hrms/employeeservices/recruitement/resume/add/$', AddUpdateEmployeeServicesRecruitementResumeView, name='crm_website_employeeservices_recruitement_list'),
                ##########################################################################################################################################################


                ###########################################################################Publish Jobs Consultant#####################################################3
    url(r'^hcm/employeeservices/recruitement/publish/jobs/consultant/$', EmployeeServicesRecruitementPublishJobConsultant.as_view(), name='publish_jobs_consultant'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/consultant/all/$', EmployeeServicesRecruitementPublishJobConsultantAll.as_view(), name='publish_jobs_consultant_all'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/consultant/edit/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeservicesRecruitementPublishVacanciesConsultant ,name='publish_jobs_consultant_edit'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/consultant/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanciesConsultant.as_view(),name='publish_consultant_delete'),
                                                        ################################################################################


                 ###########################################################################Publish Jobs portal#####################################################3
    url(r'^hcm/employeeservices/recruitement/publish/jobs/portal/$', EmployeeServicesRecruitementPublishJobPortal.as_view(), name='publish_job_portal'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/portal/all/$', EmployeeServicesRecruitementPublishJobPortalAll.as_view(), name='publish_jobs_portal_all'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/portal/edit/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeservicesRecruitementPublishVacanciesJobPortal ,name='publish_jobs_portal_edit'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/portal/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanciesJobPortal.as_view(),name='publish_job_portal_delete'),
                                                        ################################################################################

              ###########################################################################Publish Website #####################################################3
    url(r'^hcm/employeeservices/recruitement/publish/jobs/Webiste/$', EmployeeServicesRecruitementPublishJobWebiste.as_view(), name='publish_webiste'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/Webiste/all/$', EmployeeServicesRecruitementPublishJobWebisteAll.as_view(), name='publish_website_all'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/Webiste/edit/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeservicesRecruitementPublishVacanciesWebsiteEdit ,name='publish_webiste_edit'),
    url(r'^hcm/employeeservices/recruitement/publish/jobs/Webiste/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementPublishVacanciesWebisteDelete.as_view(),name='publish_webiste_delete'),
                                                        ################################################################################




                                        ############################### Resume Recipet ##############################################################


    url(r'^hrms/employeeservices/recruitement/inviteresume/list/$', EmployeeServicesRecruitementInviteResumeList.as_view(), name='crm_website_employeeservices_recruitement_inviteresume_list'),

    url(r'^hrms/employeeservices/recruitement/resume/$', AddEmployeeServicesRecruitementResume.as_view(), name='crm_website_employeeservices_recruitement_list1'),
    url(r'^hrms/employeeservices/recruitement/resume/approved/form/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementResume2, name='crm_website_employeeservices_recruitement_inviteresume'),
    url(r'^hrms/employeeservices/recruitement/exit/interview/$',EmployeeExitEmployeeListView.as_view(),name='exit_employee'),
   
   # url(r'^hrms/employeeservices/recruitement/resumes/add/form/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementResume2 , name='crm_website_employeeservices_recruitement_inviteresume_add1'),
    url(r'^hrms/employeeservices/recruitement/inviteresume/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementInviteResume.as_view(), name="crm_website_employeeservices_recruitement_inviteresume_edit"),
    url(r'^hrms/employeeservices/recruitement/inviteresume/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementInviteResumeDelete.as_view(), name='crm_website_employeeservices_recruitement_inviteresume_delete'),

    url(r'^hrms/employeeservices/recruitement/inviteresume/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementresumerecipetEdit,name='empolyeeservices_recruitemtent_invite_resume_modify'),


                                                        #################  PsychometricTest #################################
    url(r'^hrms/employeeservices/recruitement/psychometric/test/list/$', EmployeeServicesRecruitementPsychometricTestList.as_view(), name='crm_website_employeeservices_recruitement_psychometrictest_list'),
    url(r'^hrms/employeeservices/recruitement/psychometric/test/add/$', AddEditCrmEmployeeServicesRecruitementPsychometricTest.as_view(), name='crm_website_employeeservices_recruitement_psychometrictest_add'),
    url(r'^hrms/employeeservices/recruitement/psychometric/test/allowed/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementAllowedPsychometricTest.as_view(), name='crm_website_employeeservices_recruitement_allowed_psyco_test'),
    url(r'^hrms/employeeservices/recruitement/psychometric/test/waived/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementWaivePsychometricTest.as_view(), name='crm_website_employeeservices_recruitement_waive_psyco_test'),

    url(r'^hrms/employeeservices/recruitement/psychometric/test/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementPsychometricTest.as_view(), name="crm_website_employeeservices_recruitement_psychometrictest_edit"),
    url(r'^hrms/employeeservices/recruitement/psychometric/test/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementPsychometricTestDelete.as_view(), name='crm_website_employeeservices_recruitement_psychometrictest_delete'),
    url(r'^hrms/employeeservices/recruitement/psychometric/test/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementPsycometricEdit,name='crm_website_employeeservices_recruitement_psychometrictest_modify'),
    
                                                            ################# update test result #############################################3333
    url(r'^hrms/employeeservices/recruitement/updatetestresult/test/list/$', EmployeeServicesRecruitementUpdateTestResultList.as_view(), name='crm_website_employeeservices_recruitement_update_test_result_list'),
    url(r'^hrms/employeeservices/recruitement/updatetestresult/test/add/$', AddEditCrmEmployeeServicesRecruitementUpdateTestResult.as_view(), name='crm_website_employeeservices_recruitement_update_test_result_add'),
    url(r'^hrms/employeeservices/recruitement/updatetestresult/test/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementUpdateTestResult.as_view(), name="crm_website_employeeservices_recruitement_update_test_result_edit"),
    url(r'^hrms/employeeservices/recruitement/updatetestresult/test/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementUpdateTestResultDelete.as_view(), name='crm_website_employeeservices_recruitement_update_test_result_delete'),
    url(r'^hrms/employeeservices/recruitement/updatetestresult/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementUpdateTestResult, name='crm_website_employeeservices_recruitement_update_result'),
    url(r'^hrms/employeeservices/recruitement/updatetestresult/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementUpdateTestResultEdit,name='employeeservice_recruitement_updateresult_modify'),


                                                            ###################################################################################################################
########################################### Schedule Interview ########################################################3
    url(r'^hrms/employeeservices/recruitement/schedule/interview/list/$', EmployeeServicesRecruitementScheduleInterviewList.as_view(), name='crm_website_employeeservices_recruitement_schedule_interview_list'),
    url(r'^hrms/employeeservices/recruitement/schedule/interview/add/$', AddEditCrmEmployeeServicesRecruitementScheduleInterview.as_view(), name='crm_website_employeeservices_recruitement_schedule_interview_add'),
    url(r'^hrms/employeeservices/recruitement/schedule/interview/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementScheduleInterviewUpdate, name='crm_website_employeeservices_recruitement_schedule_interview_update'),
    url(r'^hrms/employeeservices/recruitement/schedule/interview/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementScheduleInterviewEdit,name='employeeservie_requirtement_schedule_interview_modify'),

    #url(r'^hrms/employeeservices/recruitement/schedule/interview/edit/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementScheduleInterview.as_view(), name="crm_website_employeeservices_recruitement_schedule_interview_edit"),
    url(r'^hrms/employeeservices/recruitement/schedule/interview/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementScheduleInterviewDelete.as_view(), name='crm_website_employeeservices_recruitement_schedule_interview_delete'),
############################################################## issue offer letter #######################################################################
    url(r'^hrms/employeeservices/recruitement/issueofferletter/list/$', EmployeeServicesRecruitementOfIssueOfferLetterList.as_view(), name='crm_website_employeeservices_recruitement_issue_offer_letter_list'),
    url(r'^hrms/employeeservices/recruitement/issueofferletter/edit/$', EmployeeServicesRecruitementOfIssueOfferLetterListedit.as_view(), name='crm_website_employeeservices_recruitement_issue_offer_letter_edit'),
    url(r'^hrms/employeeservices/recruitement/issueofferletter/form/(?P<id>[0-9,a-z,A-Z]+)$', employeeservicesissueofferleteredit, name='crm_website_employeeservices_recruitement_issue_offer_form'),
    url(r'^hrms/employeeservices/recruitement/issueofferletter/delete/(?P<id>[0-9,a-z,A-Z]+)$', EmployeeServicesissueofferletterdelete.as_view(), name='crm_website_employeeservices_recruitement_issue_offer_delete'),
    url(r'^hrms/employeeservices/recruitement/issueofferletter/modify/(?P<id>[0-9,a-z,A-Z]+)$',EditEmployeeServicesRecruitementissueOfferFormalitiesEdit,name='issue_offer_letter_modify'),

#####################################################################################################################################################################
############################################ Offer Approval#######################################################################################
    url(r'^hrms/employeeservices/recruitement/OfferApproval/list/$', EmployeeServicesRecruitementOfOfferApprovalList.as_view(), name='crm_website_employeeservices_recruitement_offer_approval_list'),
    url(r'^hrms/employeeservices/recruitement/OfferApproval/list/edit/$', EmployeeServiceRecruitementAllOfferApprovalList.as_view(), name='crm_website_employeeservices_recruitement_offer_approval_edit'),
    url(r'^hrms/employeeservices/recruitement/OfferApproval/approved/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementApproveofferletter.as_view(), name='crm_website_employeeservices_recruitement_offer_approve'),
    url(r'^hrms/employeeservices/recruitement/OfferApproval/rejected/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementRejectofferletter.as_view(), name='crm_website_employeeservices_recruitement_offer_rejected'),
    url(r'^hrms/employeeservices/recruitement/OfferApproval/putonhold/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementPutonHoldofferletter.as_view(), name='crm_website_employeeservices_recruitement_offer_putonhold'),
    url(r'^hrms/employeeservices/recruitement/OfferApproval/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementDeleteofferletter.as_view(), name='crm_website_employeeservices_recruitement_offer_approve_delete'),

##################################################################################################################################################
############################################# offer Formalities  #######################################################################################
    url(r'^hrms/employeeservices/recruitement/OfferStatus/list/$', EmployeeServicesRecruitementOfferStatusList.as_view(), name='crm_website_employeeservices_recruitement_offer_list'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/edit/$', EmployeeServicesRecruitementAllOfferStatusList.as_view(), name='crm_website_employeeservices_recruitement_offer_edit'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/update/(?P<id>[0-9,a-z,A-Z]+)/$', employeservicesrecruitementeditoffterformalities, name='crm_website_employeeservices_recruitement_offer_update'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesrecuitementOfferDelete.as_view(), name='crm_website_employeeservices_recruitement_offer_formalities_delete'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementOfferFormalitiesEdit,name='offer_formalities_modify'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesrecuitementOfferformalitiesReject.as_view(),name='offer_formalities_rejected'),

            #################################### Offer Status #################################

    url(r'^hrms/employeeservices/recruitement/OfferStatus/$', EmployeeServicesRecruitementOfferStatus2.as_view(), name='crm_website_employeeservices_recruitement_offer_status'),
    url(r'^hrms/employeeservices/recruitement/OfferStatus/accept/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitmentApproveStatus.as_view(), name='crm_website_employeeservices_recruitement_offer_accept'),

            ################################### Vacancy Status ##############################
    url(r'^hrms/employeeservices/recruitement/vacancystatus/list/$', EmployeeServicesRecruitementVacancyStatusList.as_view(), name='crm_website_employeeservices_recruitement_vacancystatus_list'),
    url(r'^hrms/employeeservices/recruitement/vacancystatus/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementVacancyStatusEdit,name='vacancy_status_edit'),
###################################################################################################################################################
################################# Resume Bank ##############################################################################333
    url(r'^hrms/employeeservices/recruitement/resumebank/list/$',EmployeeServicesRecruitementResumeBankList.as_view(), name='crm_website_employeeservices_recruitement_resume_bank_list'),

###############################################################################################################################
                          
                          
                          
                            ##############################################  Shortlist Resume    #################################################

    url(r'^hrms/employeeservices/recruitement/shortlistedresume/list/$', EmployeeServicesRecruitementResumeShortlistedList.as_view(), name='crm_website_employeeservices_recruitement_shortlistedresume_list'),
    url(r'^hrms/employeeservices/recruitement/all/shortlistedresume/list/$', EmployeeServicesRecruitementAllShortlistedResumeList.as_view(), name='crm_website_employeeservices_recruitement_all_shortlistedresume_list'),
    url(r'^hrms/employeeservices/recruitement/accepted/resume/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementAcceptedResume.as_view(), name="crm_website_employeeservices_recruitement_accepted_resume"),
    url(r'^hrms/employeeservices/recruitement/resume/recipet/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServicesRecruitementRecipetResumeDelete.as_view(),name="employeeservices_recruitement_resume_recipet_delete"),
    url(r'^hrms/employeeservices/recruitement/resume/recipet/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EployeeServiceRecruitementRejectedResume.as_view(),name="employeeservices_recruitement_resume_recipet_rejected"),
    url(r'^hrms/employeeservices/recruitement/resume/recipet/blacklisted/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServiceRecruitementRejectedBlackList.as_view(),name="employeeservices_recruitement_resume_recipet_blacklist"),

    url(r'^hrms/employeeservices/recruitement/shortlist/resumre/modify/(?P<id>[0-9,a-z,A-Z]+)/$',EditEmployeeServicesRecruitementShortlistresumeEdit,name='employeeservices_recruitement_shortlist_resume_modify'), 
                        ############################### interview result ###################
    url(r'^hrms/employeeservices/recruitement/interviewstatus/list/$', EmployeeServicesRecruitementCandidatesInterViewStatusList.as_view(), name='crm_website_employeeservices_recruitement_interviewstatus_list'),
    url(r'^hrms/employeeservices/recruitement/candidatesshortlisted/list/$', EmployeeServicesRecruitementCandidateShortlistedList.as_view(), name='crm_website_employeeservices_recruitement_candidateshortlisted_list'),

    url(r'^hrms/employeeservices/recruitement/interviewstatus/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServiceRecruitemetCandidateUpdate, name="crm_website_employeeservices_recruitement_interview_update"),
    #url(r'^hrms/employeeservices/recruitement/interviewstatus/recommended/$', EmployeeServicesRecruitementInterviewResultRecommended.as_view(), name="crm_website_employeeservices_recruitement_interview_update_recommended"),
    #url(r'^hrms/employeeservices/recruitement/interviewstatus/rejected/$', EmployeeServicesRecruitementInterviewResultRejected.as_view(), name="crm_website_employeeservices_recruitement_interview_update_rejected"),
    #url(r'^hrms/employeeservices/recruitement/interviewstatus/putonhold/$', EmployeeServicesRecruitementInterviewResultputonhold.as_view(), name="crm_website_employeeservices_recruitement_interview_putonhold"),
    url(r'^hrms/employeeservies/recruitement/interviewstatus/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeServiceRecruitemetCandidateDelete.as_view(),name='crm_website_employeeservices_recruitement_interview_delete'),

    url(r'^hrms/employeeservices/recruitement/interviewstatus/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesInterViewStatus.as_view(), name="crm_website_employeeservices_recruitement_interview_status_update"),
    url(r'^hrms/employeeservices/recruitement/candidatesshortlisted/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementCandidatesShortlisted.as_view(), name="crm_website_employeeservices_recruitement_candidatesshortlisted_update"),
    url(r'^hrms/employeeservices/recruitement/offerstatus/list/$', EmployeeServicesRecruitementOfferStatusList.as_view(), name='crm_website_employeeservices_recruitement_offer_status_list'),
    
#    url(r'^hrms/employeeservices/recruitement/document/list/$', EmployeeServicesRecruitementDocumentList.as_view(), name='crm_website_employeeservices_recruitement_document_list'),
    # url(r'^hrms/employeeservices/recruitement/document/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementDocumentEdit.as_view(), name='crm_website_employeeservices_recruitement_document_edit'),
    # url(r'^hrms/employeeservices/recruitement/document/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesRecruitementDocumentDelete.as_view(), name='crm_website_employeeservices_recruitement_document_delete'),

    url(r'^hrms/employeeservices/recruitement/candidateofferstatus/update/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementCandidatesOfferStatus.as_view(), name="crm_website_employeeservices_recruitement_candidateofferstatus_update"),
    url(r'^hrms/employeeservices/recruitement/candidateofferstatus/change/(?P<id>[0-9,a-z,A-Z]+)/$', AddEditCrmEmployeeServicesRecruitementCandidatesOfferUpdateStatus.as_view(), name="crm_website_employeeservices_recruitement_candidateofferstatus_change"),
    url(r'^hrms/employeeservices/employeeregistration/updateregistrations/list/$', EmployeeServicesEmployeeRegistrationUpdateRegistrationsList.as_view(), name='crm_website_employeeservices_employeeregistration_updateregistrations_list'),
    ##
    url(r'^hrms/employeeservices/employeeregistration/updateregistrations/add/$', AddEmployeeServicesEmployeeRegistrationUpdateRegistrations.as_view(), name='crm_website_employeeservices_employeeregistration_updateregistrations_add'),

    url(r'^hrms/employeeservices/recruitement/offerlaytter/list/$', EmployeeServicesEmployeeOfferLatter.as_view(), name='crm_website_employeeservices_offer_latter_list'),

    url(r'^hrms/employeeservices/employeeregistration/updateregistrations/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EditEmployeeServicesEmployeeRegistrationUpdateRegistrations.as_view(), name="crm_website_employeeservices_employeeregistration_updateregistrations_edit"),
    url(r'^hrms/employeeservices/employeeregistration/updateregistrations/delete/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesEmployeeRegistrationUpdateRegistrationsDelete.as_view(), name="crm_website_employeeservices_employeeregistration_updateregistrations_delete"),
    url(r'^hrms/employeeservices/employeeregistration/updatedepartment/update/$', AddEditCrmEmployeeEmployeeRegistrationUpdateDepartment.as_view(), name='crm_website_employeeservices_employeeregistration_updatedeaprtment_update'),
    url(r'^hrms/employeeservices/employeeregistration/updatedepartment/json/$', AddEditCrmEmployeeEmployeeRegistrationUpdateDepartmentJsonEmployee.as_view(), name='crm_website_employeeservices_employeeregistration_updatedeaprtment_json'),

    url(r'^hrms/employeeservices/employeeregistration/employee/list/$', EmployeeServicesEmployeeRegistrationEmployeeListList.as_view(), name='crm_website_employeeservices_employeeregistration_employee_list'),
   
    url(r'^hrms/employeeservices/employeeregistration/employee/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeServicesEmployeeRegistrationEmployeeUpdate.as_view(), name='crm_website_employeeservices_employeeregistration_employee_update'),
    url(r'^hrms/employeeservices/employeeregistration/employee/termination/$',EmployeeServiceEmployeeRegistrationTermination.as_view(),name='employee_services_termination'),
    url(r'^hrms/employeeservices/employeeregistration/add/verificationreport/(?P<id>[0-9,a-z,A-Z]+)/$', AddEmployeeServicesEmployeeRegistrationVerficationReport.as_view(), name='crm_website_employeeservices_employeeregistration_verficationreport_add'),
    url(r'^hrms/employeeservices/employeeregistration/add/documents/(?P<id>[0-9,a-z,A-Z]+)/$', AddEmployeeServicesEmployeeRegistrationDocument.as_view(), name='crm_website_employeeservices_employeeregistration_document_add'),
    # Leaves
    url(r'^hrms/employeeservices/employee/leavequota/list/$', LeavesUpdateLeaveQuotaOfEmployesListView.as_view(), name='crm_website_employeeservices_employees_leavequota_list'),

    url(r'^hrms/employeeservices/employee/leavequota/add/$', LeavesUpdateLeaveQuotaOfEmployesAddView.as_view(), name='crm_website_employeeservices_employees_leavequota_add'),

    url(r'^hrms/employeeservices/employee/leavequota/update/(?P<id>[0-9,a-z,A-Z]+)/$', LeavesUpdateLeaveQuotaOfEmployesUpdateView.as_view(), name="crm_website_employeeservices_employees_leavequota_update"),
    url(r'^hrms/employeeservices/employee/leavequota/delete/(?P<id>[0-9,a-z,A-Z]+)/$', LeavesUpdateLeaveQuotaOfEmployesUpdateViewDelete.as_view(), name="crm_website_employeeservices_employees_leavequota_delete"),

    url(r'^hrms/employeeservices/leaves/apply/$', EmployeeLeavesLeaveRequestPostLeave.as_view(), name='crm_website_employeeservices_leaves_apply'),

    url(r'^hrms/employeeservices/leaves/cancel/(?P<id>[0-9,a-z,A-Z]+)/$', LeavesUpdateLeaveQuotaOfEmployesUpdateViewCancel.as_view(), name='crm_website_employeeservices_leaves_cancele'),
    url(r'^hrms/employeeservices/leaves/quota/$', EmployeeLeavesLeaveRequestPostLeaveJsonData.as_view(), name='crm_website_employeeservices_leaves_quota'),

    url(r'^hrms/employeeservices/leaves/approve/list/$', EmployeeLeavesLeaveRequestPendingforApprovalList.as_view(), name='crm_website_employeeservices_leave_pendingforapproval_list'),

    url(r'^hrms/employeeservices/leaves/pendingforapproval/list/$',allpendingleave.as_view(),name='approve_leave'),

    url(r'^hrms/employeeservices/leaves/approved/(?P<id>[0-9,a-z,A-Z]+)/$',ApproveLeave.as_view(),name='approved_leave'),
    url(r'^hrms/employeeservices/leaves/delete/(?P<id>[0-9,a-z,A-Z]+)/$',DeleteLeave.as_view(),name='delete_leave'),
    url(r'^hrms/employeeservices/leaves/modify/(?P<id>[0-9,a-z,A-Z]+)/$',ModifyLeave ,name='modify_leaves'),
    url(r'^hrms/employeeservices/leaves/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',RejectLeave.as_view(),name='rejected_leaves'),
    url(r'^hrms/employeeservices/leaves/putonhold/(?P<id>[0-9,a-z,A-Z]+)/$',putonholdLeave.as_view(),name='putonhold_leaves'),
   

    url(r'^hrms/employeeservices/leaves/pendingforapproval/status/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeLeavesLeaveRequestPostLeaveUpdate.as_view(), name="crm_website_employeeservices_leave_pendingforapproval_status"),


    url(r'^hrms/employeeservices/leaves/approved/leaves/list/$',EmployeeLeavesLeaveRequestApprvedLeaveList2.as_view(),name='approved_leave_list'),

    url(r'^hrms/employeeservices/leaves/rejected/leaves/list/$',EmployeeLeavesLeaveRequestRejectedLeaveList2.as_view(),name='rejected_leaves_list'),
    

    url(r'^hrms/employeeservices/leaves/approved/list/$', EmployeeLeavesLeaveRequestApprovedLeaveList.as_view(), name="crm_website_employeeservices_leave_approved_list"),
    url(r'^hrms/employeeservices/leaves/rejected/list/$', EmployeeLeavesLeaveRequestRejectedLeaveList.as_view(), name="crm_website_employeeservices_leave_rejected"),
    
    url(r'^hrms/employeeservices/leaves/mybalance/list/$', EmployeeLeavesLeaveRequestMyBalanceLeaveList.as_view(), name="crm_website_employeeservices_leave_mybalance"),
    # Attendance

    url(r'^hrms/employeeservices/attendance/upload/$', EmployeeAttendanceUploadAttendanceUpdate.as_view(), name='crm_employee_services_attendance_upload_attendance'),

    url(r'^hrms/employeeservices/attendance/correction/$',EmployeeAttendanceUpdateAttendanceCorrection.as_view(),name='attendance_correction'),


    url(r'^hrms/employeeservices/attendance/correction/list/$', EmployeeAttendanceUpdateAttendanceList.as_view(), name='crm_employee_services_attendance_update_list'),

    url(r'^hrms/employeeservices/attendance/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeAttendanceUpdateAttendanceUpdate.as_view(), name='crm_employee_services_attendance_update'),

    url(r'^hrms/employeeservices/attendance/status/$', EmployeeAttendanceAttendanceStatusList.as_view(), name='crm_employee_services_attendance_status'),

    url(r'^hrms/employeeservices/attendance/approved/$',EmployeeAttendanceAttendanceStatusListDisplay.as_view(),name='approved_attendance'),

    url(r'^hrms/employeeservices/attendance/status/approve/(?P<id>[0-9,a-z,A-Z]+)/$',ApprovedAttendance.as_view(),name='status_approve'),
    url(r'^hrms/employeeservices/attendance/status/reject/(?P<id>[0-9,a-z,A-Z]+)/$',RejectedAttendance.as_view(),name='status_reject'),

    url(r'^hrms/employeeservices/attendance/status/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeAttendanceAttendanceStatusUpdate.as_view(), name='crm_employee_services_attendance_update'),
    
    
    # HR Policies
    url(r'^hrms/employeeservices/hrpolicies/updatepolicies/$', EmployeeHRPoliciesUpdatePolicy.as_view(), name='crm_employee_services_hrpolicies_upload_update_policies'),
    url(r'^hrms/employeeservices/hrpolicies/updatepolicies/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeHRPoliciesUpdatePolicy.as_view(), name='crm_employee_services_hrpolicies_upload_policies_edit'),
    url(r'^hrms/employeeservices/hrpolicies/updateforms/$', EmployeeHRPoliciesUpdateForms.as_view(), name='crm_employee_services_hrpolicies_upload_update_forms'),
    url(r'^hrms/employeeservices/hrpolicies/updateforms/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeHRPoliciesUpdateForms.as_view(), name='crm_employee_services_hrpolicies_upload_forms_edit'),
    url(r'^hrms/employeeservices/hrpolicies/updatecirculars/$', EmployeeHRUpdateCircularsForms.as_view(), name='crm_employee_services_hrpolicies_upload_update_circulars'),
    url(r'^hrms/employeeservices/hrpolicies/updatecirculars/edit/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeHRUpdateCircularsForms.as_view(), name='crm_employee_services_hrpolicies_upload_circulars_edit'),
    url(r'^hrms/employeeservices/hrpolicies/updatepolicies/list/$', EmployeeHRPoliciesUpdatePolicyList.as_view(), name='crm_employee_services_hrpolicies_upload_update_policies_list'),
    url(r'^hrms/employeeservices/hrpolicies/updatecirculars/list/$', EmployeeHRPoliciesUpdateCircularsmodelList.as_view(), name='crm_employee_services_hrpolicies_upload_update_circulars_list'),
    url(r'^hrms/employeeservices/hrpolicies/updateforms/list/$', EmployeeHRPoliciesUpdateFormmodelList.as_view(), name='crm_employee_services_hrpolicies_upload_update_forms_list'),
    # Claim And Reimbursement

    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/$', EmployeeClaimandReimbursementSubmitClaimsFormView.as_view(), name='crm_employee_services_claimandreimbursement_submitclaims'),

    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/approved/list/$', EmployeeClaimandReimbursementSubmitClaimsApprovedListView.as_view(), name='crm_employee_services_claimandreimbursement_submitclaims_approved_list'),


    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/pending/list/$', EmployeeClaimandReimbursementSubmitClaimsListView.as_view(), name='crm_employee_services_claimandreimbursement_submitclaims_list'),

    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/pending/list/display/$',EmployeeClaimandReimbursementSubmitClaimsListViewDisplay.as_view(),name='travel_claim_display'),

    url(r'^employeeservices/claim/approved/action/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimReimbursementApproveAction.as_view(),name='claim_approval_action'),
    url(r'^employeeservices/claim/rejected/action/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimReimbursementRejectedAction.as_view(),name='claim_rejected_action'),
    url(r'^employeeservices/claim/rejected/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimReimbursementDeleteAction.as_view(),name='claim_deleted'),



    url(r'^hcm/employeeservices/claimandreimbursement/request/$',EmployeeClaimAndReimbursment.as_view(),name='claim_and_reimbursment_request'),


    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/list/$',EmployeClaimdata.as_view(),name='claim_data'),
    
    url(r'^hcm/employeeservices/claim/and/reimbursement/approve/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimandReimbursmentApprove.as_view(),name='approved_claim'),
    url(r'^hcm/employeeservices/claim/and/reimbursement/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimandReimbursmentRejected.as_view(),name='Rejected_claim'),
    url(r'^hcm/employeeservices/claim/and/reimbursement/delete/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeClaimandReimbursmentDelete.as_view(),name='Delete_claim'),


    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/list/display/$',EmployeClaimdatalist.as_view(),name='claim_display'),
   
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/pending/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementSubmitClaimsApprovedView.as_view(), name='crm_employee_services_claimandreimbursement_submitclaims_approved'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/processing/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementApprovedDateOfProcessingView.as_view(), name='crm_employee_services_claimandreimbursement_submitclaims_processing'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/claimprocessed/list/$', EmployeeClaimandReimbursementClaimClaimProcessedListView.as_view(), name='crm_employee_services_claimandreimbursement_claim_claimprocessed_list'),
    
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/claimprocessed/updates/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementClaimClaimProcessedUpdatesView.as_view(), name='crm_employee_services_claimandreimbursement_claim_claimprocessed_update'),
    
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/claimprocess/list/$', EmployeeClaimandReimbursementSubmitReimbursementApprovedClaimToProcessView.as_view(), name='crm_employee_services_claimandreimbursement_claimprocessing_list'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitclaims/status/list/$', EmployeeClaimandReimbursementClaimStatusListView.as_view(), name='crm_employee_services_claimandreimbursement_claim_status_list'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/$', EmployeeClaimandReimbursementSubmitReimbursementFormView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementSubmitReimbursementListView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_update'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/update/status/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementSubmitReimbursementApprovedDateOfProcessingView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_update_staus'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/pending/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementSubmitReimbursementApprovedView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_approved'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/approved/list/$', EmployeeClaimandReimbursementSubmitReimbursementApprovedListView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_approved_list'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/reimbursementprocessing/list/$', EmployeeClaimandReimbursementSubmitReimbursementApprovedClaimToProcessListView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_reimbursementprocessing_list'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/reimbursementprocessed/list/$', EmployeeClaimandReimbursementReimbursementRejectedListView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_reimbursementprocessed_list'), 
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/reimbursementprocessed/Update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeClaimandReimbursementReimbursementRejectedUpdateView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_reimbursementprocessed_Update'),
    url(r'^hrms/employeeservices/claimandreimbursement/submitreimbursement/status/list/$', EmployeeClaimandReimbursementRembursementStatusListView.as_view(), name='crm_employee_services_claimandreimbursement_submitreimbursement_reimbursement_status_list'),
    # Payroll
    url(r'^hrms/employeeservices/payroll/accept/attendance/list/$', EmployeePayrollProcessingAcceptAttendanceListView.as_view(), name='crm_employee_services_payroll_accept_attendance_list'),
    ####
    url(r'^hrms/employeeservices/payroll/accept/attendance/update/(?P<id>[0-9,a-z,A-Z]+)/$',UserAcceptAttendanceUpdateFormView.as_view(), name='crm_employee_services_payroll_accept_attendance_update'),

    url(r'^hrms/employeeservices/payroll/accept/overtime/list/$', EmployeePayrollProcessingAcceptOverTimeListView.as_view(), name='crm_employee_services_payroll_accept_overtime_list'),

    url(r'^hrms/employeeservices/payroll/update/leaves/list/$', EmployeePayrollUpdateLeavesListView.as_view(), name='crm_employee_services_payroll_update_leave_list'),

    url(r'^hrms/employeeservices/payroll/claim/update/list/$', EmployeePayrollAcceptClaimsView.as_view(), name='crm_employee_services_payroll_claim_update_list'),

    url(r'^hrms/employeeservices/payroll/reimbursement/update/list/$', EmployeePayrollUpdateReimbursementView.as_view(), name='crm_employee_services_payroll_reimbursement_update_list'),

    url(r'^hrms/employeeservices/payroll/update/advances/list/$', EmployeePayrollUpdateAdvancesView.as_view(), name='crm_employee_services_payroll_update_advances_list'),

    url(r'^hrms/employeeservices/payroll/update/incentive/list/$', EmployeePayrollIncentivesView.as_view(), name='crm_employee_services_payroll_update_incentive_list'),


    url(r'^hrms/employeeservices/payroll/tax/declaration/list/$', EmployeeUpdateTaxDeclarationView.as_view(), name='crm_employee_services_payroll_tax_declaration_list'),

    url(r'^hrms/employeeservices/payroll/tax/declaration/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeUpdateTaxDeclarationUpdateView, name='crm_employee_services_payroll_tax_declaration_update'),
    
    url(r'^hrms/employeeservices/payroll/tax/recovery/list/$', EmployeeUpdateTaxRecoveryView.as_view(), name='crm_employee_services_payroll_tax_recovery_list'),
    url(r'^hrms/employeeservices/payroll/tax/recovery/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeUpdateTaxRecoveryUpdateView, name='crm_employee_services_payroll_tax_recovery_update'),
    
    url(r'^hrms/employeeservices/payroll/tax/calculation/list/$', EmployeePayrollProcessingTaxCalculationView.as_view(), name='crm_employee_services_payroll_tax_calculation_list'),
    url(r'^hrms/employeeservices/payroll/tax/calculation/update(?P<id>[0-9,a-z,A-Z]+)/$', EmployeePayrollProcessingTaxCalculationUpdateView, name='crm_employee_services_payroll_tax_calculation_update'),    
    url(r'^hrms/employeeservices/payroll/update/recovery/list/$', EmployeePayrollProcessingUpdateRecoveriesView.as_view(), name='crm_employee_services_payroll_update_recovery_list'),
    url(r'^hrms/employeeservices/payroll/update/recovery/add/$', EmployeePayrollProcessingUpdateRecoveriesAdd, name='crm_employee_services_payroll_update_recovery_add'),
    url(r'^hrms/employeeservices/payroll/update/recovery/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeePayrollProcessingUpdateRecoveriesUpdate, name='crm_employee_services_payroll_update_recovery_update'),
    
    url(r'^hrms-employee/emplyeesservices/managepayroll/statutorydeduction/list/$', EmployeeSalaryDeductionsListAddView.as_view(), name='crm_crmemployee_manageemployee_statutorydeductions_list'),
    url(r'^hrms-employee/emplyeesservices/managepayroll/statutorydeduction/update/(?P<id>[0-9,a-z,A-Z]+)/$', PayrollStatutoryDeductionsUpdateView, name='crm_crmemployee_manageemployee_statutorydeductions_update'),
    
    
    url(r'^hrms-employee/emplyeesservices/managepayroll/salaryvoucher/list/$', PayrollSalaryVoucherListAddView.as_view(), name='crm_crmemployee_manageemployee_salaryvoucher_list'),
    url(r'^hrms-employee/emplyeesservices/managepayroll/salaryvoucher/update/(?P<id>[0-9,a-z,A-Z]+)/$', PayrollSalaryVoucherListUpdateView, name='crm_crmemployee_manageemployee_salaryvoucher_update'),
    
    url(r'^hrms-employee/emplyeesservices/managepayroll/salarydisbursement/list/$', PayrollSalaryDisbursementListAddView.as_view(), name='crm_crmemployee_manageemployee_salarydisbursement_list'),
    url(r'^hrms-employee/emplyeesservices/managepayroll/salarydisbursement/add/$', PayrollSalaryDisbursementListAddFormView, name='crm_crmemployee_manageemployee_salarydisbursement_add'),
    url(r'^hrms-employee/emplyeesservices/managepayroll/salarydisbursement/update/(?P<id>[0-9,a-z,A-Z]+)/$', PayrollSalaryDisbursementListUpdate, name='crm_crmemployee_manageemployee_salarydisbursement_update'),
   
   
    # Key Responsibility Areas & Targets
    url(r'^hrms/employeeservices/update/kraandtarget/$', AddEditKeyResponsibilityAreasUpdateTargetsKRATargetsView.as_view(), name='crm_employee_services_payroll_keyresponsibilityareas_update_kra'),
    url(r'^hrms/employeeservices/update/kraandtarget/target/$', AddEditKeyResponsibilityAreasUpdateTargetsView.as_view(), name='KRA_update_targets'),
    url(r'^hrms/employeeservices/approve/KRA/$',AddEditKeyResponsibilityAreasApproveKRAView.as_view(),name='KRA_approve_KRA'),
    url(r'^hrms/employeeservices/approve/target/$',AddEditKeyResponsibilityAreasApproveTargetView.as_view(),name='KRA_approve_target'),
    url(r'^hrms/employeeservices/Kra/performance/$',AddEditKeyResponsibilityKraPeformanceView.as_view(),name='kra_performance'),
    url(r'^hrms/employeeservices/target/achievement/$',AddEditKeyResponsibilityKratargetperformanceachievementView.as_view(),name='target_achievement'),

    # url(r'^hrms/employeeservices/kraandtarget/performance/list/$', KeyResponsibilityAreasTargetsKRATargetsPerformanceListView.as_view(), name='crm_employee_services_payroll_kra_target_performance_list'),
    # url(r'^hrms/employeeservices/kraandtarget/review/list/$', KeyResponsibilityAreasTargetsKRATargetsReviewListView.as_view(), name='crm_employee_services_payroll_kra_target_review_list'),
    # url(r'^hrms/employeeservices/kraandtarget/performance/update/(?P<id>[0-9,a-z,A-Z]+)/$', KeyResponsibilityAreasTargetsKRATargetsPerformanceUpdateView.as_view(), name='crm_employee_services_kra_target_performance_update'),
    # # Resignation
    url(r'^hrms/employeeservices/employee/FandF/upload/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeExitEmployeeResignationFandFView.as_view(), name='employee_services_employee_FandF_upload'),

    url(r'^hrms/employeeservices/employee/reject/(?P<id>[0-9,a-z,A-Z]+)/$',EmployeeExitEmployeeApprove.as_view(),name='exit_reject'),
    url(r'^hrms/employeeservices/employee/resignation/$', EmployeeExitEmployeeResignationLetterView.as_view(), name='employee_services_employee_resignation'),
    url(r'^hrms/employeeservices/employee/recommendation/$',EmployeeExitEmployeeRecommendationView.as_view(),name='employee_exit_management_recommendation'),
    url(r'^hrms/employeeservices/employee/approval/$',EmployeeExitEmployeeApprovalView.as_view(),name='exit_employee_approval'),
    url(r'^hrms/employeeservices/employee/resignation/list/$', EmployeeExitEmployeeResignationLetterListView.as_view(), name='employee_services_employee_resignation_list'),
    url(r'^hrms/employeeservices/employee/relieving/list/$', EmployeeExitEmployeeEmployeeRelievingView.as_view(), name='employee_services_employee_relieving_list'),
    url(r'^hrms/employeeservices/employee/fullandfinalsettlement/list/$', EmployeeExitEmployeeFullandFinalSettlementListView.as_view(), name='employee_services_employee_fullandfinalsettlement_list'),
    url(r'^hrms/employeeservices/employee/resignation/status/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeExitEmployeeResignationLetterResignationStatusView.as_view(), name='employee_services_employee_resignation_status'),
    url(r'^hrms/employeeservices/employee/relieving/status/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeExitEmployeeResignationRelievingStatusView.as_view(), name='employee_services_employee_relieving_status'),
    url(r'^hrms/employeeservices/employee/fullandfinalsettlement/status/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeeExitEmployeeFullandFinalSettlementUpdateStatusView.as_view(), name='employee_services_employee_fullandfinalsettlement_status'),

    url(r'^website/employeeservices/employee/holidaysandleaves/days/list/$', WebsiteHolidaysListView.as_view(), name='website_list_holi_days_add'),

    url(r'^website/employeeservices/employee/holidaysandleaves/days/add/$', WebsiteAddUpdateHoliDaysView.as_view(), name='website_add_update_holi_days'),

    url(r'^website/employeeservices/employee/holidaysandleaves/days/list/(?P<holidaysdaysid>[0-9]+)/$', WebsiteAddUpdateHoliDaysView.as_view(), name='website_list_holi_days_update'),
    url(r'^website/employeeservices/employee/holidaysandleaves/days/delete/(?P<holidaysdaysid>[0-9]+)/$', WebsiteHolidaysDeletView.as_view(), name='website_holi_days_delete'),
    
    url(r'^website/employeeservices/employee/update/overttime/list/$', OvertimeManagementUpdateOvertimeListView.as_view(), name='website_edit_update_over_time_list'),
    
    
    url(r'^website/employeeservices/employee/update/overttime/add/$', OvertimeManagementUpdateOvertimeAddView.as_view(), name='website_edit_update_over_time_add'),


    url(r'^website/employeeservices/employee/update/overttime/status/list/$', OvertimeManagementUpdateOvertimeStatusListView.as_view(), name='website_edit_update_over_time_status_list'),

    url(r'^website/employeeservices/employee/update/overttime/approval/display/$',OvertimeManagementUpdateOvertimeStatusListViewDisplay.as_view(),name='overtime_approval_display'),
    url(r'^website/employeeservices/employee/update/overttime/approval/(?P<id>[0-9,a-z,A-Z]+)/$',OvertimeApprove.as_view(),name='approved_overtime'),
    url(r'^website/employeeservices/employee/update/overttime/approval/(?P<id>[0-9,a-z,A-Z]+)/$',OvertimeRejected.as_view(),name='rejected_overtime'),

    url(r'^website/employeeservices/employee/update/overttime/delete/(?P<id>[0-9]+)/$', OvertimeManagementUpdateOvertimeDeletView.as_view(), name='website_edit_update_over_time_delete'),
    url(r'^website/employeeservices/employee/update/overttime/update/(?P<id>[0-9]+)/$', OvertimeManagementUpdateOvertimeStatusListViewUpdateStatusView.as_view(), name='website_edit_update_over_time_status_update'),

    url(r'^website/employeeservices/employee/travel/request/list/$', TravelClaimManagementTravelConveyanceTravelRequestListView.as_view(), name='website_travel_request_list'),

    url(r'^website/employeeservices/employee/all/travel/request/list/$',TravelClaimManagementTravelConveyanceAllTravelRequest.as_view(),name='website_all_travel_request'),

    url(r'^travel/request/approve/(?P<id>[0-9,a-z,A-Z]+)/$',travelrequestapprove.as_view(),name='travel_request_approved'),
    url(r'^travel/request/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',travelrequestrejected.as_view(),name='travel_request_rejected'),
    url(r'^travel/request/deleted/(?P<id>[0-9,a-z,A-Z]+)/$',travelrequestdelete.as_view(),name='travel_request_delete'),

    # url(r'^website/employeeservices/employee/travel/request/status/list/$', TravelClaimManagementTravelConveyanceTravelRequestStatusView.as_view(), name='website_travel_request_status_list'),
##
    url(r'^website/employeeservices/employee/travel/request/status/Pending/list/$', TravelClaimManagementTravelConveyanceTravelRequestStatusView.as_view(), name='website_travel_request_status_list'),
    url(r'^website/employeeservices/employee/travel/request/status/Approved/list/$', TravelClaimManagementTravelConveyanceTravelRequestStatusApprovedView.as_view(), name='website_travel_request_status_Approved_list1'),
    url(r'^website/employeeservices/employee/travel/request/status/Rejected/list/$', TravelClaimManagementTravelConveyanceTravelRequestStatusRejectedView.as_view(), name='website_travel_request_status_Rejected_list1'),
    

    url(r'^website/employeeservices/employee/travel/request/add/$', TravelClaimManagementTravelConveyanceTravelRequestAddView.as_view(), name='website_travel_request_add'),

    url(r'^website/employeeservices/employee/travel/request/update/status/(?P<id>[0-9]+)/$', TravelClaimManagementTravelConveyanceTravelRequestUpdateStatusView.as_view(), name='website_travel_request_update_status'),

    url(r'^website/employeeservices/employee/submit/request/$', EmployeeAdvancesSubmitAdvanceRequestView.as_view(), name='website_travel_advance_request_submit_request'),
    url(r'^website/employeeservices/employee/advancerequest/status/request/advance/approve/list/$',EmployeeAdvancesSubmitAdvanceRequestListApprovedAdvanceList.as_view(),name='employee_advance_approved'),
    url(r'^website/employeeservices/employee/submit/approved/(?P<id>[0-9,a-z,A-Z]+)/$',ApproveAdvance.as_view(),name='approved_advance'),
    url(r'^website/employeeservices/employee/submit/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',RejectAdvance.as_view(),name='rejected_advance'),


    url(r'^website/employeeservices/employee/advancerequest/status/request/list/$', EmployeeAdvancesSubmitAdvanceRequestListView.as_view(), name='website_travel_advance_request_status_list'),

    url(r'^website/employeeservices/employee/advancerequest/processing/request/list/$', EmployeeAdvancesSubmitAdvanceRequestProcessingListView.as_view(), name='website_travel_advance_request_processing_list'),
    url(r'^website/employeeservices/employee/advancerequest/processed/request/list/$', EmployeeAdvancesSubmitAdvanceRequestProcessedListView.as_view(), name='website_travel_advance_request_processed_list'),
    url(r'^website/employeeservices/employee/advancerequest/status/request/update/(?P<id>[0-9]+)/$', EmployeeAdvancesSubmitAdvanceRequestUpdateView.as_view(), name='website_travel_advance_request_status_update'),

    #######perquisite#########
    #url(r'^hcm/employeeservices/employeeservices/perquisite/request',EmployeePerquistesPerquisiteRequest.as_view(),name='hcm_perquisite_request'),

    ##########################


    url(r'^website/employeeservices/employee/incentive/bonus/add/$', IncentiveBonusUpdateIncentiveBonusAddView.as_view(), name='website_travel_incentive_bonus_add'),


    url(r'^website/employeeservices/employee/incentive/bonus/status/list/$', IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalListView.as_view(), name='website_travel_incentive_bonus_status_list'),

    url(r'^website/employeeservices/employee/incentive/status/list/$',IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalListApprovedIncentive.as_view(),name='incentive_approved_list'),


    url(r'^website/employeeservices/employee/incentive/bonus/status/update/(?P<id>[0-9]+)/$', IncentiveBonusUpdateIncentiveBonusIncentiveBonusApprovalUpdateView.as_view(), name='website_travel_incentive_bonus_status_update'),
    url(r'^website/employeeservices/employee/incentive/bonus/processing/list/$', IncentiveBonusUpdateIncentiveBonusIncentiveBonusProcessingListView.as_view(), name='website_incentive_bonus_status_processing_list'),
    url(r'^website/employeeservices/employee/incentive/bonus/processed/list/$', IncentiveBonusUpdateIncentiveBonusIncentiveBonusProcessedListView.as_view(), name='website_incentive_bonus_status_processed_list'),  
   

    url(r'^website/employeeservices/employee/incentive/approved/(?P<id>[0-9,a-z,A-Z]+)/$',IncentiveApproved.as_view(),name='incentive_approved'),
    url(r'^website/employeeservices/employee/incentive/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',IncentiveRejected.as_view(),name='incentive_rejected'),
    url(r'^website/employeeservices/employee/incentive/delete/(?P<id>[0-9,a-z,A-Z]+)/$',IncentiveDelete.as_view(),name='incentive_deleted'),

    #-------------
    #Tax Declaration
    #---------------
    url(r'^website/employeeservices/updatetaxdeclaration/$',TaxDeclarationUpdateTaxDeclaration.as_view(),name='hcm_update_tax_declaration'),

    url(r'^webiste/employeeservices/update/income/(?P<id>[0-9,a-z,A-Z]+)/$',TaxDeclarationupdateotherincome ,name='update_income'),

    url(r'^webiste/employeeservices/update/exemption/(?P<id>[0-9,a-z,A-Z]+)/$',TaxDeclarationExemption,name='update_exemption'),


    url(r'^website/employeeservices/tax/declaration/approval/$',TaxDeclarationApprovalAll.as_view(),name='tax_declaration_all'),


    url(r'^website/employeeservices/tax/declaration/approval/display/$',TaxDeclarationApprovalDisplay.as_view(),name='tax_declaration_display'),

    url(r'^website/employeeservices/tax/declaration/approval/(?P<id>[0-9,a-z,A-Z]+)/$',TaxDeclarationApprove.as_view(),name='tax_approve'),

    url(r'^website/employeeservices/tax/declaration/delete/(?P<id>[0-9,a-z,A-Z]+)/$',TaxDeclarationDelete.as_view(),name='tax_delete'),
    url(r'^website/employeeservices/tax/declaration/reject/(?P<id>[0-9,a-z,A-Z]+)/$',TaxDeclarationReject.as_view(),name='tax_reject'),

    url(r'^website/employeeservices/income/tax/calculation/$',IncomeTaxCalculation.as_view(),name='income_tax_calculation'),

    url(r'^website/employeeservices/income/tax/calculation/display/$',IncomeTaxCalculationDisplay.as_view(),name='income_tax_calculation_display'),

    url(r'^website/employeeservices/income/tax/approval/$',IncomeTaxApproval.as_view(),name='income_tax_approval'),

    url(r'^website/employeeservices/income/tax/approval/all/$',IncomeTaxApprovalall.as_view(),name='income_tax_approval_all'),
    url(r'^website/employeeservices/income/tax/approval/action/aprove/(?P<id>[0-9,a-z,A-Z]+)/$',IncomeTaxActionApprove.as_view(),name='income_tax_action_approve'),
    url(r'^website/employeeservices/income/tax/approval/action/rejected/(?P<id>[0-9,a-z,A-Z]+)/$',IncomeTaxActionRejected.as_view(),name='income_tax_action_rejected'),
    url(r'^website/employeeservices/income/tax/delete/(?P<id>[0-9,a-z,A-Z]+)/$',IncomeTaxDisplayActionDelete.as_view(),name='income_tax_display_delete'),


    url(r'^website/employeeservices/other/recovery/update/recovery/$',OtherrecoveryUpdateRecoverydisplay.as_view(),name='other_recovery_update_recovery'),
    url(r'^website/employeeservices/other/recovery/update/recovery/form/$',OtherrecoveryUpdateRecovery.as_view(),name='other_recovery_update_recovery_form'),
   

    url(r'^website/employeeservices/recovery/approval//display/$',OtherrecoveryRecoveryApprovalDisplay.as_view(),name='other_recovery_recovey_approval_display'),

    url(r'^website/employeeservices/recovery/approval/$',OtherrecoveryRecoveryApproval.as_view(),name='other_recovery_recovey_approval'),
    url(r'^website/employeeservices/recovery/action/approval/(?P<id>[0-9,a-z,A-Z]+)/$',Otherrecoveryactionapproval.as_view(),name='other_recovery_action_approval'),
    
    url(r'^website/employeeservices/recovery/action/reejcted/(?P<id>[0-9,a-z,A-Z]+)/$',Otherrecoveryactionrejected.as_view(),name='other_recovery_action_rejected'),
    url(r'^website/employeeservices/recovery/action/deleted/(?P<id>[0-9,a-z,A-Z]+)/$',Otherrecoveryactiondelete.as_view(),name='other_recovery_action_delete'),


    # Knowledge and Training
    url(r'^hrms/knowledgeandtraining/update/documents/$', KnowledgeandTrainingUpdateDocumentsView.as_view(), name='crm_knowledgeandtraining_update_documents_view'),
    url(r'^hrms/knowledgeandtraining/update/training/$', KnowledgeandTrainingUpdateTrainingView.as_view(), name='crm_knowledgeandtraining_update_training_view'),
    url(r'^hrms/knowledgeandtraining/update/promotions/$', KnowledgeandTrainingUpdatePromotionsView.as_view(), name='crm_knowledgeandtraining_update_promotions_view'),
    url(r'^hrms/knowledgeandtraining/knowledge/sharing/$', KnowledgeandTrainingKnowledgeSharingView.as_view(), name='crm_knowledgeandtraining_update_knowledge_sharing'),
    url(r'^hrms/knowledgeandtraining/upcoming/traning/list/$', KnowledgeandTrainingUpcomingTraningListView.as_view(), name='crm_knowledgeandtraining_update_upcoming_training_list'),
    url(r'^hrms/knowledgeandtraining/current/promotions/list/$', KnowledgeandTrainingCurrentPromotionsListView.as_view(), name='crm_knowledgeandtraining_update_current_promotions_list'),
    
    url(r'^hrms/knowledgeandtraining/current/promotions/update/(?P<id>[0-9A-Za-z]+)/$', KnowledgeandTrainingCurrentPromotionsUpdateView.as_view(), name='crm_knowledgeandtraining_update_current_promotions_update'),
    url(r'^hrms/knowledgeandtraining/upcoming/promotions/list/$', KnowledgeandTrainingUpcomingPromotionsListView.as_view(), name='crm_knowledgeandtraining_update_current_upcoming_list'),
    url(r'^hrms/knowledgeandtraining/past/promotions/list/$', KnowledgeandTrainingPastPromotionsListView.as_view(), name='crm_knowledgeandtraining_update_current_past_list'),
    url(r'^hrms/knowledgeandtraining/current/traning/list/$', KnowledgeandTrainingCurrentTraningListView.as_view(), name='crm_knowledgeandtraining_update_current_traning_list'),
    url(r'^hrms/knowledgeandtraining/past/traning/list/$', KnowledgeandTrainingPastraningListView.as_view(), name='crm_knowledgeandtraining_update_current_past_traning_list'),
    url(r'^hrms/knowledgeandtraining/request/received/traning/list/$', KnowledgeandTrainingRequestReceivedForTrainignListView.as_view(), name='crm_knowledgeandtraining_request_recevied_for_training'),
    url(r'^hrms/vendorsupport/send/wish/to/attend/$', send_request_to_for_attend_traning.as_view(), name='crm_vendorsupport_send_wish_to_attend'),
    url(r'^traning/attend/$', TrainingAttendListView.as_view(), name='traning_attend'),


###### EmployeeHolidaysAndLeaves
    url(r'^website/employee/services/employee/holidaysandleaves/days/list/$', EmployeeHolidaysAndLeavesList.as_view(), name='EmployeeHolidaysAndLeaveslist'),
    url(r'^website/employee/services/employee/holidaysandleaves/days/add/$', AddEmployeeHolidaysAndLeaves.as_view(), name='EmployeeHolidaysAndLeavesadd'),
    url(r'^website/employee/services/employee/holidaysandleaves/days/edit/(?P<id>[0-9]+)/$', AddEditEmployeeHolidaysAndLeaves, name='EmployeeHolidaysAndLeavesedit'),
    url(r'^website/employee/services/employee/holidaysandleaves/days/delete/(?P<id>[0-9]+)/$', EmployeeHolidaysAndLeavesDelete.as_view(), name='EmployeeHolidaysAndLeavesdelete'),  



###
    url(r'^hrms/employeeservices/recruitement/publishvacancies/add/$', Datapost.as_view(), name='crm_website_employeeservices_recruitement_publishvacancies_update'),
    url(r'^hrms/employeeservices/recruitement/publishvacancies1/add/$', Datapost1.as_view(), name='crm_website_employeeservices_recruitement_publishvacancies_update'),
    
   ### payrollprocessed    EmployeePayrollProcessedListView
    url(r'^hrms-employee/emplyeesservices/payroll/payroll-processed/add/$', EmployeePayrollProcessedAddView, name='crm_crmemployee_manageemployee_payrollprocessed_add'),
    url(r'^hrms-employee/emplyeesservices/payroll/payroll-processed/list/$', EmployeePayrollProcessedListView.as_view(), name='crm_crmemployee_manageemployee_payrollprocessed_list'),
    url(r'^hrms-employee/emplyeesservices/payroll/payroll-processed/pending/list/$', EmployeePayrollProcessedPendingListView.as_view(), name='crm_crmemployee_manageemployee_payrollprocessed_pending_list'),
    url(r'^hrms-employee/emplyeesservices/payroll/payroll-processed/update/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeePayrollProcessedListViewUpdate, name='crm_crmemployee_manageemployee_payrollprocessed_update'),
    url(r'^website/employee/services/employee/payroll-processed/days/delete/(?P<id>[0-9]+)/$', EmployeePayrollProcessedListViewDelete.as_view(), name='EmployeePayrollProcessedListViewdelete'),  
    url(r'^website/employee/services/employee/payroll-processed/list/$', EmployeePayrollstatusListView.as_view(), name='EmployeePayrollstatusListViews'),  
    
    url(r'^website/employee/services/employee/payroll-processing/list/$', EmployeePayrollProcessingListView.as_view(), name='EmployeePayrollProcessingListViews'),  

    url(r'^hrms-employee/emplyeesservices/payroll/payroll-processed/add/$', EmployeesalarySlipAddView, name='EmployeesalarySlipAddView_add'),
    url(r'^website/employee/services/employee/payroll-processed/salary/slip/list/(?P<id>[0-9,a-z,A-Z]+)/$', EmployeePayrollSlipListView.as_view(), name='EmployeePayrollSlipListView'),  

]
# 