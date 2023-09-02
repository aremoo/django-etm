# pylint: disable=E1101

from django.conf import settings
import os
from django.core.management.base import BaseCommand
from users.models import CustomUser, EmployeeRecord
from users.utils import parse_employee_data

class Command(BaseCommand):
    help = 'Ingests employee data from a provided text file'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'users', 'data', 'VacBalance.txt')
    
        user_data_list = parse_employee_data(file_path)
        
        for data in user_data_list:
            try:
                # Assuming data contains 'employee_id' which matches a CustomUser instance
                user = CustomUser.objects.get(employee_id=data.pop('employee_id'))

                # Remove the 'user_name' from data dictionary since it's not needed
                data.pop('user_name', None)  # If 'user_name' exists, it'll be removed; otherwise, do nothing
        
                # Now you have the user, and data doesn't contain 'employee_id' or 'user_name' anymore.
                # Use the user instance to create or update the EmployeeRecord
                EmployeeRecord.objects.update_or_create(user=user, defaults=data)
                
                self.stdout.write(self.style.SUCCESS(f'Successfully ingested data for {user.username}'))
            except CustomUser.DoesNotExist:
                self.stdout.write(self.style.ERROR(f"User with employee ID {data.get('employee_id')} does not exist. Skipping..."))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Error ingesting data for {data.get('user_name', 'unknown user')}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS(f'Successfully finished ingesting employee data from "{file_path}"'))
