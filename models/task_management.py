from odoo import models, fields, api

class TaskManagement(models.Model):
    _name = 'custom.task.management'
    _description = 'Task Management'
    _inherit = ['mail.thread', 'mail.activity.mixin']  # Add mail.thread and mail.activity.mixin

    name = fields.Char('Task Name', required=True, tracking=True)  # Enable tracking for the name field
    description = fields.Text('Description')
    project_id = fields.Many2one('custom.project.management', string='Project')
    assigned_to = fields.Many2one('res.users', string='Assigned To', tracking=True)  # Enable tracking for the assigned_to field
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done'),
    ], string='State', default='new', tracking=True)  # Enable tracking for the state field

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
        """Send a notification to the assigned user via Odoo's internal messaging system."""
        for task in self:
            if task.assigned_to:
                # Generate the notification message
                message = self._get_notification_message(action)
                if message:
                    # Post the message to the task's chatter
                    task.message_post(
                        body=message,
                        message_type="notification",
                        partner_ids=task.assigned_to.partner_id.ids,  # Notify the assigned user
                    )

    def _get_notification_message(self, action):
        """Generate the notification message."""
        if action == 'created':
            return f"Task '{self.name}' has been created and assigned to you."
        elif action == 'updated':
            return f"Task '{self.name}' has been updated. New status: {self.state}."
        return ""