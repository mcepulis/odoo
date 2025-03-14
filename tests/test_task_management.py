from odoo.tests.common import TransactionCase

class TestTaskManagement(TransactionCase):
    def setUp(self):
        super(TestTaskManagement, self).setUp()
        
        # Create test data
        self.user_1 = self.env['res.users'].create({
            'name': 'User 1',
            'login': 'user_1',
            'email': 'user_1@example.com',
        })
        self.user_2 = self.env['res.users'].create({
            'name': 'User 2',
            'login': 'user_2',
            'email': 'user_2@example.com',
        })
        self.project = self.env['custom.project.management'].create({
            'name': 'Test Project',
            'description': 'This is a test project.',
        })

    def test_task_creation(self):
        """Test that a task can be created."""
        task = self.env['custom.task.management'].create({
            'name': 'Test Task',
            'description': 'This is a test task.',
            'project_id': self.project.id,
            'assigned_to': self.user_1.id,  # Assign a single user
            'state': 'new',
        })
        
        # Verify the task was created
        self.assertEqual(task.name, 'Test Task')
        self.assertEqual(task.description, 'This is a test task.')
        self.assertEqual(task.project_id, self.project)
        self.assertEqual(task.assigned_to, self.user_1)  # Verify the assigned user
        self.assertEqual(task.state, 'new')

    def test_task_assignment(self):
        """Test that a single employee can be assigned to a task."""
        task = self.env['custom.task.management'].create({
            'name': 'Test Task',
            'description': 'This is a test task.',
            'project_id': self.project.id,
            'assigned_to': self.user_1.id,  # Assign a single user
            'state': 'new',
        })
        
        # Verify the assigned user
        self.assertEqual(task.assigned_to, self.user_1)

    def test_task_state_transition(self):
        """Test that the task's state can be updated."""
        task = self.env['custom.task.management'].create({
            'name': 'Test Task',
            'description': 'This is a test task.',
            'project_id': self.project.id,
            'assigned_to': self.user_1.id,  # Assign a single user
            'state': 'new',
        })
        
        # Update the task's state
        task.write({'state': 'in_progress'})
        self.assertEqual(task.state, 'in_progress')

        task.write({'state': 'done'})
        self.assertEqual(task.state, 'done')