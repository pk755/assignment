from django.shortcuts import render, redirect
from .forms import NumberForm
from collections import Counter

def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

#def is_armstrong(n):
#    s = str(n)
 #   p = len(s)
  #  return n == sum(int(d)**p for d in s)

def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return n == sum(d ** power for d in digits)


def process_file(f):
    data = f.read().decode('utf-8').strip()
    return [int(x) for x in data.split(',') if x.strip()]

def calculate_statistics(numbers):
    # numbers guaranteed non-empty
    total = sum(numbers)
    mean = total / len(numbers)
    sorted_nums = sorted(numbers)
    mid = len(sorted_nums) // 2
    if len(sorted_nums) % 2:
        median = sorted_nums[mid]
    else:
        median = (sorted_nums[mid-1] + sorted_nums[mid]) / 2

    counts = Counter(sorted_nums)
    max_count = max(counts.values())
    mode = [n for n, c in counts.items() if c == max_count]

    rng = sorted_nums[-1] - sorted_nums[0]
    primes = [n for n in sorted_nums if is_prime(n)]
    armstrongs = [n for n in sorted_nums if is_armstrong(n)]

    return {
        'sum': total,
        'mean': mean,
        'median': median,
        'mode': mode,
        'range': rng,
        'prime': primes,
        'armstrong': armstrongs
    }

def homepage(request):
    """Display only the form & cart count."""
    
    form = NumberForm()
    cart = request.session.get('cart', [])
    unique_count = len(set(cart))
    return render(request, 'Statistics/homepage.html', {
        'form': form,
        'unique_count': unique_count
    })

def results(request):
    """Handle POST from homepage; calculate & display stats."""
    unique_count = request.session.get('unique_count', 0)

    if request.method != 'POST':
        return redirect('homepage')

    form = NumberForm(request.POST, request.FILES)
    stats = None

    if form.is_valid():
        nums = []
        raw = form.cleaned_data['numbers'].strip()
        if raw:
            try:
                nums = [int(x) for x in raw.split(',') if x.strip()]
            except ValueError:
                form.add_error('numbers', 'Enter only integers separated by commas.')

        if not nums and form.cleaned_data['file']:
            try:
                nums = process_file(form.cleaned_data['file'])
            except Exception:
                form.add_error('file', 'Could not parse file; use comma-separated integers.')

        if not nums:
            form.add_error(None, 'Please enter numbers or upload a valid file.')
        else:
            unique_nums = list(set(nums))
            request.session['cart'] = unique_nums
            request.session['unique_count'] = len(unique_nums)
            stats = calculate_statistics(nums)
    return render(request, 'Statistics/results.html', {
        'form': form,               # in case you want to show errors
        'stats': stats,
        'count': request.session.get('unique_count', 0)
    })

def cart(request):
    unique_numbers = request.session.get('cart', [])
    return render(request, 'Statistics/cart.html', {'cart': unique_numbers})

def clear(request):
    request.session['cart'] = []
    return redirect('cart')
