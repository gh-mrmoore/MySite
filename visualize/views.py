from django.shortcuts import render
import pandas as pd

# Create your views here.
# Since we're not using a database any longer to save some money, we're going to use the csv files that I've saved on my GitHub account.

def index(request):  # Create a company-wide overview home page to start from
    revenue_df = pd.read_csv("https://raw.githubusercontent.com/gh-mrmoore/MySite/main/visualize/static/visualize/test_data.csv")  # Get my data and create a pandas DataFrame with it

    revenue_unique_states = revenue_df["order_state"].unique()  # get my unique state values to pass to the template

    order_count_by_state = revenue_df["order_state"].value_counts().to_frame(name="order_count")

    # Create my context variable to pass objects to the template page
    home_context = {
        'revenue_unique_states': revenue_unique_states, 
        'order_count_by_state': order_count_by_state, 
        }
    
    # Render the template page and pass in the context dictionary
    return render(request, 'visualize/index.html', context=home_context)

"""
def revenue(request):  # Create my home page for the revenue section of the reporting site
    if request.method == 'POST':
        # do something with the form input
        selected_state = request.POST['state']

        if selected_state == 'All':
            order_count_by_state = OrderData.objects.values('order_state').order_by('order_state').annotate(state_order_count=Count('order_state'))
            revenue_sum_by_state = OrderData.objects.values('order_state').order_by('order_state').annotate(state_revenue_sum=Sum('order_revenue'))
        else:
            order_count_by_state = OrderData.objects.filter(order_state=selected_state).values('order_state').order_by('order_state').annotate(state_order_count=Count('order_state'))
            revenue_sum_by_state = OrderData.objects.filter(order_state=selected_state).values('order_state').order_by('order_state').annotate(state_revenue_sum=Sum('order_revenue'))

        # Get the distinct states from the database data
        distinct_states = OrderData.objects.order_by('order_state').values('order_state').distinct()

        revenue_context = {
            'order_count_by_state': order_count_by_state, 
            'order_revenue_by_state': revenue_sum_by_state, 
            'distinct_states': distinct_states
            }
        return render(request, 'visualize/revenue.html', context=revenue_context)
    else:
        # Get the distinct states from the database data
        distinct_states = OrderData.objects.order_by('order_state').values('order_state').distinct()

        # Create my context variable to pass objects to the template page
        revenue_context = {
            'order_count_by_state': order_count_by_state, 
            'order_revenue_by_state': revenue_sum_by_state, 
            'distinct_states': distinct_states
            }

        # Render the templage page and pass in the context dictionary
        return render(request, 'visualize/revenue.html', context=revenue_context)


def products(request):  # Create my home page for the products section of the reporting site
    

    # Create my context variable to pass objects to the template page
    products_context = {}

    
    return render(request, 'visualize/products.html', context=products_context)  # Render the template page and pass in the context dictionary


def expense(request):  # Create my home page for the expense section of the reporting site
    

    # Create my context variable to pass objects to the template page
    expense_context = {}

    return render(request, 'visualize/expense.html', context=expense_context)  # Render the template page and pass in the context dictionary


def vendors(request):  # Create my home page for the vendors section of the reporting site
    

    # Create my context variable to pass objects to the template page
    vendor_context = {}

    return render(request, 'visualize/vendors.html', context=vendor_context)  # Render the template page and pass in the context dictionary


def detail(request, state_id):  # Use the state from the URL to get the list of all companies in that state from the database
    companies_by_state = OrderData.objects.filter(order_state = state_id).values().order_by('order_company')

    # Use the state from the URL to get the order count by company for that state
    order_count_by_state_company = OrderData.objects.filter(order_state = state_id).values('order_company', 'order_state').annotate(company_total=Count('order_number')).order_by('order_company')

    # Create my context variable to pass to the templage page for display
    detail_context = {
        'companies_by_state_list': companies_by_state, 
        'order_count_by_state_company': order_count_by_state_company
    }

    return render(request, 'visualize/companies.html', context=detail_context)  # Render the template page with the context variable


def more_detail(request, state_id, company_id):
    # Use the state id and company from the URL to get the list of all the orders for that company in that state
    company_orders_for_state = OrderData.objects.filter(order_state = state_id, order_company=company_id).values()

    # Create my context variable to pass to the template page for display
    more_detail_context = {
        'company_orders_for_state': company_orders_for_state
    }
    
    return render(request, 'visualize/final_detail.html', context=more_detail_context)  # Render the templage page with the context variable
"""