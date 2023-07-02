from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Todo
from .forms import Todoform
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.

class List(ListView):
    model = Todo
    template_name = 'list.html'
    context_object_name = 'tasks'


class Detail(DetailView):
    model = Todo
    template_name = 'detail.html'
    context_object_name = 'tasks'

class Update(UpdateView):
    model = Todo
    template_name = 'update.html'
    context_object_name = 'tasks'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs ={'pk': self.object.id})


class Delete(DeleteView):
    model = Todo
    template_name = 'delete.html'
    success_url = reverse_lazy('index')






def index(request):
    tasks = Todo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task',)
        prior = request.POST.get('priority',)
        date = request.POST.get('date',)
        task = Todo(name=name, priority=prior, date=date)
        task.save()
    return render(request, 'index.html', {'tasks': tasks})

def delete(request, id):
    delete = Todo.objects.get(id=id)
    if request.method == 'POST':
        delete.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task_update = Todo.objects.get(id=id)
    f = Todoform(request.POST or None, instance=task_update)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'update.html', {'f': f})

