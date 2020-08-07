from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from locker.models import Account

# Create your views here.
def index(request):
    return render(request, 'index.html')

class AccountListView(LoginRequiredMixin, ListView):
    paginate_by = 10

    def get_queryset(self):
        return Account.objects.filter(account_owner=self.request.user)

class AccountDetailView(UserPassesTestMixin, DetailView):
    model = Account

    def test_func(self):
        return self.request.user == self.get_object().account_owner

class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['name', 'link', 'username', 'password']

    def form_valid(self, form):
        form.instance.account_owner = self.request.user
        return super().form_valid(form)

class AccountUpdate(UserPassesTestMixin, UpdateView):
    model = Account
    fields = ['name', 'link', 'username', 'password']

    def test_func(self):
        return self.request.user == self.get_object().account_owner

class AccountDelete(UserPassesTestMixin, DeleteView):
    model = Account
    success_url = reverse_lazy('account-list')

    def test_func(self):
        return self.request.user == self.get_object().account_owner
