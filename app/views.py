from pyexpat.errors import messages
from sqlite3 import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
from app.forms import ProductForm, UnitForm, UserForm, VendorForm
from app.models import Product, Stock, StockMovement, Unit, Vendor
from django.db.models.aggregates import Sum

from django.http.response import JsonResponse

# Create your views here.
def home(request):
    return render(request,"menubar.html")
def purchase_report(request):
    # Retrieve stock movements with a specific channel type (e.g., 'purchase')
    stockmovements = StockMovement.objects.filter(channel='Purchase')
    
    return render(request, 'purchase_report.html', {'stockmovements': stockmovements})

def sales_report(request):
    stockmovements = StockMovement.objects.filter(channel='Sale')
    
    return render(request, 'sales_report.html', {'stockmovements': stockmovements})

def expiry_report(request):
    stockmovements = StockMovement.objects.filter(channel='Damage')
    
    return render(request, 'expiry_report.html', {'stockmovements': stockmovements})

def product_report(request):
    products = Product.objects.all()
    return render(request, 'product_report.html', {'products': products})

def add_product(request):
    form = ProductForm()
    
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product_report/')
    return render(request, 'add_product.html', {'form': form})

def update_product(request, id):
    # Fetch the product instance or return a 404 error if not found
    product = get_object_or_404(Product, id=id)
    form = ProductForm(instance=product)

    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            # Redirect to the product list or detail page after a successful update
            return redirect('/product_report/')  # Replace 'product_list' with your URL name or path

    return render(request, 'update_product.html', {'form': form})






def stock_report(request):
    # Retrieve all stock movements
    stockmovements = StockMovement.objects.all()

    # Create a dictionary to hold aggregated data
    aggregated_data = {}
    
    for movement in stockmovements:
        if movement.name not in aggregated_data:
            aggregated_data[movement.name] = {
                'quantity': 0,
                'unit': movement.unit,
                'channel': movement.channel,
                'date': movement.date,
                'invoice': movement.invoice,
                'user': movement.User
            }
        
        # Adjust quantity based on channel type
        if movement.channel == 'Opening':
            aggregated_data[movement.name]['quantity'] += movement.quantity
        elif movement.channel == 'Sale':
            aggregated_data[movement.name]['quantity'] -= movement.quantity
        elif movement.channel == 'Purchase':
            aggregated_data[movement.name]['quantity'] += movement.quantity
        elif movement.channel == 'Damage':
            aggregated_data[movement.name]['quantity'] -= movement.quantity
    
    # Prepare context for rendering the template
    context = {
        'aggregated_data': aggregated_data,
    }
    return render(request, 'stock_report.html', context)




def collection_report(request):
    return render(request, 'collection_report.html')

def add_purchase (request):
    return render(request,'add_purchase.html')

def refund_report(request):
    stockmovements = StockMovement.objects.filter(channel='Refund')
    
    return render(request, 'refund_report.html', {'stockmovements': stockmovements})

def add_unit(request):
    form = UnitForm()
    
    if request.method == "POST":
        form = UnitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/unit_report/')
    return render(request, 'add_unit.html', {'form': form})

def update_unit(request, id):
    unit = Unit.objects.get(id=id)
    form = UnitForm(instance=unit)
    if request.method == "POST":
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            return redirect('/unit_report/')
    return render(request, 'update_unit.html', {'form': form})

def unit_report(request):
      units=Unit.objects.all()
      return render(request, 'unit.html', {'units': units})


def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                # Handle custom fields not in UserForm
                user = form.save(commit=False)
                
                # Handle password confirmation
                password = form.cleaned_data.get('password')
                confirm_password = request.POST.get('confirm_password')
                
                if password == confirm_password:
                    user.set_password(password)  # Hash the password
                    user.save()  # Save the user object

                    # Handle custom 'status' field
                    status = form.cleaned_data.get('status')
                    if status is not None:
                        user.is_active = status
                    user.save()

                    return redirect('/user_list/')
                else:
                    form.add_error('password', 'Passwords do not match.')
            except IntegrityError:
                form.add_error('username', 'Username already exists.')
        else:
            print("Form is not valid:", form.errors)  # Debugging print statement
    else:
        form = UserForm()
    
    return render(request, 'add_user.html', {'form': form})

def update_user(request, id):
    user = get_object_or_404(User, id=id)  # Get the user or raise a 404 error if not found
    
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/user_list/')

            # Redirect or give some success message
    else:
        form = UserForm(instance=user)
    
    return render(request, 'update_user.html', {'form': form})












def add_vendor(request):
    if request.method == 'POST':
        vendor_name = request.POST.get('vendor_name')
        vendor_panno = request.POST.get('vendor_panno')
        vendor_address = request.POST.get('vendor_address')
        vendor_contact = request.POST.get('vendor_contact')
        vendor_status = request.POST.get('vendor_status') == 'on'  # Convert to Boolean

        
        Vendor.objects.create(
            vendor=vendor_name,
            panno=vendor_panno,
            address=vendor_address,
            contact=vendor_contact,
            status=vendor_status,
            )
            
        
        return redirect('/add_vendor/')  # Redirect to the same page or another page after submission

    return render(request, 'add_vendor.html')



def check_vendor_exists(request):
    """AJAX endpoint to check if vendor name or PAN exists."""
    vendor_name = request.GET.get('vendor_name', None)
    vendor_panno = request.GET.get('vendor_panno', None)
    
    name_exists = Vendor.objects.filter(vendor=vendor_name).exists() if vendor_name else False
    pan_exists = Vendor.objects.filter(panno=vendor_panno).exists() if vendor_panno else False

    return JsonResponse({'name_exists': name_exists, 'pan_exists': pan_exists})



def update_vendor(request, id):
    vendor = get_object_or_404(Vendor, id=id)

    if request.method == 'POST':
        form = VendorForm(request.POST, instance=vendor)
        if form.is_valid():
            form.save()
            
            return redirect('/vendor_report/')  # Redirect to vendor list or another page
       
    else:
        form = VendorForm(instance=vendor)

    return render(request, 'update_vendor.html', {'form': form})


def vendor_report(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_report.html', {'vendors': vendors})





def sales_channel(request):
    return render(request,'sales_channel.html')

from django.http import JsonResponse
from .models import Product, StockMovement

def api_products(request):
    products = Product.objects.filter(status=True)
    stockmovements = StockMovement.objects.all()

    # Create a dictionary to hold stock data
    stock_data = {}
    
    for movement in stockmovements:
        if movement.name not in stock_data:
            stock_data[movement.name] = {
                'quantity': 0,
                
                'channel': movement.channel,
            }

        # Adjust quantity based on channel type
        if movement.channel == 'Opening':
            stock_data[movement.name]['quantity'] += movement.quantity
        elif movement.channel == 'Sale':
            stock_data[movement.name]['quantity'] -= movement.quantity
        elif movement.channel == 'Purchase':
            stock_data[movement.name]['quantity'] += movement.quantity
        elif movement.channel == 'Damage':
            stock_data[movement.name]['quantity'] -= movement.quantity

    products_list = list(products.values('name', 'price'))

    # Prepare response data
    response_data = {
        'products': products_list,
        'stock': stock_data
    }

    return JsonResponse(response_data)
