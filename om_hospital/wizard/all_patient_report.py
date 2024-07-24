# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class PatientReportWizard (models.TransientModel):
    _name = "patient.report.wizard"
    _description = "Print Patient Wizard"
    
    gender = fields.Selection ([('other', 'Other'), ('male', 'Male'), ('female','Female')], string="Gender")
    age = fields.Integer (string= "Age")
    
    def print_report_action(self):
        data = {
            'form_data': self.read()[0],
        }
        return self.env.ref('om_hospital.report_all_patient_details_action').report_action(self, data=data)