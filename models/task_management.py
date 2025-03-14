from odoo import models, fields, api

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

    @api.model
    def create(self, vals):
        # Send notification when a task is created
        task = super(TaskManagement, self).create(vals)
        task._send_notification('created')
        return task

    def write(self, vals):
        # Send notification when the task's state is updated
        if 'state' in vals:
            self._send_notification('updated')
        return super(TaskManagement, self).write(vals)

    def _send_notification(self, action):
        # Send an email notification to the assigned user
        for task in self:
            if task.assigned_to:
                template = self.env.ref('project_management.task_status_notification_template')
                template.send_mail(task.id, force_send=True)

    def _get_notification_message(self, action):
        # Generate the notification message
        if action == 'created':
            return f"Task '{self.name}' has been created and assigned to you."
        elif action == 'updated':
            return f"Task '{self.name}' has been updated. New status: {self.state}."
        return ""
