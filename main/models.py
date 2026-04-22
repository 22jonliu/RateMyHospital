from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Facility(models.Model):
    name = models.CharField(max_length=255)
    full_address = models.TextField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Facilities"
    
    def __str__(self):
        return self.name


class Review(models.Model):
    PAY_TYPE_CHOICES = [
        ('hourly', 'Hourly'),
        ('salary', 'Salary'),
    ]
    #user name for Review card, work in progress
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")

    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='reviews')
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    years_of_experience = models.CharField(max_length=50)
    
    # Compensation
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    annual_salary = models.IntegerField(null=True, blank=True)
    pay_type = models.CharField(max_length=20, choices=PAY_TYPE_CHOICES)
    currency = models.CharField(max_length=3, default='USD')
    
    # Ratings (1-5 scale)
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    work_life_balance = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    salary_benefits = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    management = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    workplace_happiness = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    career_growth = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    staffing_levels = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    patient_care_quality = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    safety = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    training_support = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    
    # Review content
    pros = models.TextField()
    cons = models.TextField()
    would_recommend = models.BooleanField(default=True)
    
    # Metadata
    date_posted = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_posted']
    
    def __str__(self):
        return f"{self.job_title} at {self.facility.name}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    work_title = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
