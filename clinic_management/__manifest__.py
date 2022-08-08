{
    "name": "Clinic System",
    "descreption": "Clinic Management System",
    "author":" ayman",
    "data":
        [
            'security/clinical_security.xml',
            'security/ir.model.access.csv',
            'report/appointment_template.xml',
            'report/appointment_report.xml',
            'data/appointment_sequence.xml',
            'wizard/create_appointment_wizard_view.xml',
            'views/clinic_management_patient_view.xml',
            'views/clinic_management_clinic_view.xml',
            'views/clinic_management_appointment_view.xml'

        ],
   'depends': ['base','mail'],
}