from django.db import models

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
    
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='reviews')
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    years_of_experience = models.CharField(max_length=50)
    
    # Compensation
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    annual_salary = models.IntegerField()
    pay_type = models.CharField(max_length=20, choices=PAY_TYPE_CHOICES)
    currency = models.CharField(max_length=3, default='USD')
    
    # Ratings (1-5 scale)
    overall_rating = models.DecimalField(max_digits=2, decimal_places=1)
    work_life_balance = models.DecimalField(max_digits=2, decimal_places=1)
    salary_benefits = models.DecimalField(max_digits=2, decimal_places=1)
    management = models.DecimalField(max_digits=2, decimal_places=1)
    workplace_happiness = models.DecimalField(max_digits=2, decimal_places=1)
    career_growth = models.DecimalField(max_digits=2, decimal_places=1)
    staffing_levels = models.DecimalField(max_digits=2, decimal_places=1)
    patient_care_quality = models.DecimalField(max_digits=2, decimal_places=1)
    safety = models.DecimalField(max_digits=2, decimal_places=1)
    training_support = models.DecimalField(max_digits=2, decimal_places=1)
    
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


"""from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="projects")
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
"""