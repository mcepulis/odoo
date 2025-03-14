from odoo import models, fields

class TaskManagement(models.Model):
    _name = 'custom.task.management'
    _description = 'Task Management'

    name = fields.Char('Task Name', required=True)
    description = fields.Text('Description')
    project_id = fields.Many2one('custom.project.management', string='Project')
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='State', default='new')
