from odoo import models, fields, api

class TaskFilterWizard(models.TransientModel):
    _name = 'custom.task.filter.wizard'
    _description = 'Task Filter Wizard'

    project_id = fields.Many2one('custom.project.management', string='Project')
    assigned_to = fields.Many2many('res.users', string='Assigned To')  
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')

    def action_filter_tasks(self):
        domain = []
        if self.project_id:
            domain.append(('project_id', '=', self.project_id.id))
        if self.assigned_to:
            domain.append(('assigned_to', 'in', self.assigned_to.ids))  
        if self.start_date:
            domain.append(('create_date', '>=', self.start_date))
        if self.end_date:
            domain.append(('create_date', '<=', self.end_date))

        return {
            'type': 'ir.actions.act_window',
            'name': 'Filtered Tasks',
            'res_model': 'custom.task.management',
            'domain': domain,
            'view_mode': 'tree,form',
            'target': 'current',
        }
