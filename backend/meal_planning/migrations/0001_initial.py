# Generated by Django 4.2.7 on 2025-07-26 11:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='My Meal Plan', max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meal_plans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'meal_plans',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MealPlanEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('meal_type', models.CharField(choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner'), ('snack', 'Snack')], max_length=20)),
                ('servings', models.PositiveIntegerField(default=1)),
                ('notes', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('meal_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='meal_planning.mealplan')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipe')),
            ],
            options={
                'db_table': 'meal_plan_entries',
                'ordering': ['date', 'meal_type'],
                'unique_together': {('meal_plan', 'date', 'meal_type')},
            },
        ),
    ]
