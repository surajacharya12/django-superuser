from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, "users/dashboard.html")


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserCreationForm()
    return render(request, "users/sign_up.html", {"form": form})   