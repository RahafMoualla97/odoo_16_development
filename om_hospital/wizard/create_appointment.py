# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class CreateAppointmentWizard (models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"
    
    @api.model
    def default_get(self, fields):
        res = super(CreateAppointmentWizard, self).default_get(fields)
        if self._context.get('active_id'):
            res['patient_id'] = self._context.get('active_id')
        return res
    
    date_appointment = fields.Date (string= "Date", required=False)
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one('hospital.doctor', string="Doctor", required=True)
    
    
    def action_create_appointment(self):
        print("Created New Appointment")
        vals = {
            'patient_id': self.patient_id.id,
            'date_appointment': self.date_appointment,
            'doctor_id': self.doctor_id.id
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            # 'target': 'new'
        }

    def action_view_appointment(self):
        # All Patients Appointment Records
        action = self.env.ref('om_hospital.hospital_appointment_action').read()[0]
        # Current Patient Appointment Record
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        # All Patients Appointment Records Another Way
        # action = self.env['ir.actions.actions']._for_xml_id("om_hospital.hospital_appointment_action")
        
        #Also Another Way
        # return {
        #      'type': 'ir.actions.act_window',
        #      'name': 'Appointment',
        #      'res_model': 'hospital.appointment',
        #      'view_type': 'form',
        #      'domain': [('patient_id', '=', self.patient_id.id)],
        #      'view_mode': 'tree,form',
        #      'target': 'new'
             
        # }
        return action