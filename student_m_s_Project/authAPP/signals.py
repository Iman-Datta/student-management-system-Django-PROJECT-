from django.db.models.signals import post_migrate
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from resultAPP.models import Marksheet
from django.dispatch import receiver

@receiver(post_migrate)
def create_default_groups(sender, **kwargs):
    student_group, _ = Group.objects.get_or_create(name='Student') # Student group created
    teacher_group, _ = Group.objects.get_or_create(name='Teacher') # Teacher group created

    content_type = ContentType.objects.get_for_model(Marksheet) # It assign permisson related to specific model

    # Permissions for Teacher group
    teacher_permissions = Permission.objects.filter(
        content_type=content_type,
        codename__in=[
            'add_marksheet',
            'change_marksheet',
            # 'delete_marksheet',
            'view_marksheet'
        ]
    )
    teacher_group.permissions.set(teacher_permissions)

    # Permission for Student group
    view_permission = Permission.objects.get(
        content_type=content_type,
        codename='view_marksheet'
    )
    student_group.permissions.set([view_permission])
