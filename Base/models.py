from django.db import models

# Create your models here.
class Project(models.Model):  
    title = models.CharField(max_length=200)  
    description = models.TextField()  
    technologies = models.TextField()  
    project_link= models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  

    def __str__(self):  
        return f"{self.title}"

class Education(models.Model):  
    institution = models.CharField(max_length=200) 
    location =models.CharField(max_length=30, default='India',null=True) 
    degree = models.CharField(max_length=200)  
    start_date = models.CharField(max_length=20) 
    end_date = models.CharField(max_length=20) 
    field = models.CharField(max_length=50)
    gpa_or_percentage = models.CharField(max_length=50)  

    def __str__(self):  
        return f"{self.institution }"

class Experience(models.Model):  
    title = models.CharField(max_length=200)  
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=20)  
    start_date = models.CharField(max_length=50)  
    end_date = models.CharField(max_length=50)
    description = models.TextField()  

    def __str__(self):  
        return f"{self.company}"

class Skill(models.Model):  
    CATEGORY_CHOICES = [  
        ('Languages', 'Language'),  
        ('Frameworks', 'Framework'),  
        ('Tools', 'Tool'),  
        ('Courses', 'Course'),  
        ('Soft Skills', 'Soft Skill')  
    ]  

    name = models.CharField(max_length=100)  
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)  

    def __str__(self):  
        return f"{self.name} ({self.category})"  
    
class Achievement(models.Model):
    description = models.TextField()  
    ac_link= models.URLField(blank=True, null=True)

    def __str__(self):  
        return f"{self.description }"
    
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.name}"
