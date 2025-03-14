from odoo import models

class TaskReport(models.AbstractModel):
    _name = 'report.project_management.task_report_template'
    _description = 'Task Report'

    def _get_report_values(self, docids, data=None):
        tasks = self.env['custom.task.management'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'custom.task.management',
            'docs': tasks,
        }