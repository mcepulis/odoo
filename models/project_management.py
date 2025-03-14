from odoo import models, fields

class ProjectManagement(models.Model):
    _name = 'custom.project.management'
    _description = 'Project Management'

    name = fields.Char('Project Name', required=True)
    description = fields.Text('Description')
    task_ids = fields.One2many('custom.task.management', 'project_id', string='Tasks')
