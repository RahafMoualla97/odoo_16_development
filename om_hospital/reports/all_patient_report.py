# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class AllPatientReport(models.AbstractModel):
    _name = 'report.om_hospital.report_all_patient_list'
    _description = 'Patient Report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        domain = []
        gender = data.get('form_data').get('gender')
        age = data.get('form_data').get('age')
        if gender != 0 :
            domain += [('gender', '=', gender)]
        if age :
            domain += [('age', '=', age)]
        docs = self.env['hospital.patient'].search(domain)
        return {
            'docs' : docs,
        }
        
        
class PatientDetailsReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient_details'
    _description = 'Patient Details Report'
    
    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.env['hospital.patient'].browse(docids)
        return {
            'docs' : docs,
        }