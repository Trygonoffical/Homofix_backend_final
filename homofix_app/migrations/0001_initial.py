# Generated by Django 4.2 on 2023-04-11 00:12

import ckeditor.fields
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('1', 'HOD'), ('2', 'Technician'), ('3', 'Support'), ('4', 'Customer')], default='1', max_length=10)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Inprocess', 'Inprocess'), ('cancelled', 'Cancelled'), ('completed', 'Completed'), ('Reached', 'Reached'), ('Assign', 'Assign'), ('Proceed', 'Proceed')], default='New', max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('order_id', models.CharField(blank=True, max_length=9, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='BookingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('total_price', models.IntegerField()),
                ('total_price_with_tax', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=50)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal', 'Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnatka', 'Karnatka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Delhi', 'Delhi')], max_length=100, null=True)),
                ('area', models.CharField(blank=True, max_length=50, null=True)),
                ('zipcode', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HodSharePercentage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='JobEnquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('resume', models.FileField(blank=True, null=True, upload_to='Job/Job Enquiry Form')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_pic', models.ImageField(upload_to='Product Image')),
                ('product_title', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('dis_amt', models.IntegerField(blank=True, null=True)),
                ('warranty', models.CharField(blank=True, max_length=50, null=True)),
                ('warranty_desc', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Support')),
                ('address', models.CharField(max_length=100)),
                ('permanent_address', models.CharField(blank=True, max_length=50, null=True)),
                ('father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('mobile', models.CharField(max_length=50)),
                ('marital_status', models.CharField(blank=True, max_length=50, null=True)),
                ('d_o_b', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('New', 'New'), ('Hold', 'Hold')], default='Active', max_length=50)),
                ('support_id', models.CharField(blank=True, max_length=12)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('application_form', models.FileField(blank=True, null=True, upload_to='Support/Application Form')),
                ('document_form', models.FileField(blank=True, null=True, upload_to='Support/Document Form')),
                ('can_assign_task', models.BooleanField(default=False)),
                ('can_new_booking', models.BooleanField(default=False)),
                ('can_cancel_booking', models.BooleanField(default=False)),
                ('can_rebooking', models.BooleanField(default=False)),
                ('can_expert_create', models.BooleanField(default=False)),
                ('can_contact_us_enquiry', models.BooleanField(default=False)),
                ('can_job_enquiry', models.BooleanField(default=False)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('bookings', models.ManyToManyField(blank=True, related_name='supported_by_staff', to='homofix_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='Technician')),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('expert_id', models.CharField(blank=True, max_length=12)),
                ('Father_name', models.CharField(blank=True, max_length=100, null=True)),
                ('present_address', models.TextField(blank=True, null=True)),
                ('permanent_address', models.TextField(blank=True, null=True)),
                ('Id_Proof', models.CharField(blank=True, max_length=100, null=True)),
                ('id_type', models.CharField(blank=True, max_length=100, null=True)),
                ('id_proof_document', models.ImageField(blank=True, null=True, upload_to='ID Proof')),
                ('application_form', models.ImageField(blank=True, null=True, upload_to='Expert/Application Form')),
                ('rating', models.CharField(blank=True, max_length=50, null=True)),
                ('serving_area', models.CharField(blank=True, max_length=100, null=True)),
                ('highest_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal', 'Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnatka', 'Karnatka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttarakhand', 'Uttarakhand'), ('Uttar Pradesh', 'Uttar Pradesh'), ('West Bengal', 'West Bengal'), ('Delhi', 'Delhi')], max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('New', 'New'), ('Hold', 'Hold')], default='Active', max_length=50)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now_add=True)),
                ('joining_date', models.DateField(blank=True, null=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('subcategories', models.ManyToManyField(blank=True, null=True, to='homofix_app.subcategory')),
                ('supported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homofix_app.support')),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_share', models.IntegerField(default=0)),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='WalletHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('bonus', 'Bonus'), ('deduction', 'Deduction')], max_length=10)),
                ('amount', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.wallet')),
            ],
        ),
        migrations.CreateModel(
            name='TechnicianLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('booking_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homofix_app.booking')),
                ('technician_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.booking')),
                ('supported_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='homofix_app.support')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='SpareParts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_part', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='showonline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('technician_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Share',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('technician_share', models.IntegerField(default=0)),
                ('hod_share', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('hod_share_percentage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.hodsharepercentage')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.task')),
            ],
        ),
        migrations.CreateModel(
            name='RechargeHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True)),
                ('technician_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='Rebooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Assign', 'Assign'), ('Inprocess', 'Inprocess'), ('completed', 'Completed')], default='Assign', max_length=20)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('booking_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rebookings', to='homofix_app.bookingproduct')),
                ('technician', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.subcategory'),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_mode', models.CharField(choices=[('Online', 'Online'), ('Cash On Services', 'Cash On Services'), ('Qr', 'Qr')], max_length=20)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Kyc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ac_no', models.CharField(max_length=50)),
                ('ifsc_code', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('bank_holder_name', models.CharField(max_length=100)),
                ('technician_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.technician')),
            ],
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.customer')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=255)),
                ('answer', ckeditor.fields.RichTextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='faqs', to='homofix_app.product')),
            ],
        ),
        migrations.AddField(
            model_name='bookingproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.product'),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.customer'),
        ),
        migrations.AddField(
            model_name='booking',
            name='products',
            field=models.ManyToManyField(related_name='bookings', through='homofix_app.BookingProduct', to='homofix_app.product'),
        ),
        migrations.AddField(
            model_name='booking',
            name='supported_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings_supported_by', to='homofix_app.support'),
        ),
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('admin', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Addon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('booking_prod_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.bookingproduct')),
                ('spare_parts_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homofix_app.spareparts')),
            ],
        ),
    ]
