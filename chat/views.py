from .models import Chat, Profile
from django.views.generic import CreateView, ListView
from .forms import ChatForm
from .mixins import FormMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.urls import reverse


class ChatListView(ListView):
    model = Chat
    template_name = 'chat.html'
    context_object_name = 'text'


class ChatCreateView(FormMessageMixin, CreateView):
    model = Chat
    template_name = 'chat_create.html'
    form_class = ChatForm
    form_valid_message = 'created successfully!'

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        form.instance.author = profile
        return super(ChatCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('chat', args=(self.object.id,))

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('chat.html')
    template_name = 'signup.html'

    def form_valid(self, form):
        created_user = form.save()
        profile = Profile.objects.create(user=created_user)
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username'),
            password=form.cleaned_data.get('password1'),
        )
        login(self.request, authenticated_user)
        return redirect('chat.html', profile.id)