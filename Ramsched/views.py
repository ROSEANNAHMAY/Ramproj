from django.shortcuts import render, redirect
from .models import *
from .forms import *

def MainPage(request):
      if request.method == "POST":
         ClientInformations.objects.create(
            last=request.POST['last'],
            first=request.POST['first'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            gender=request.POST['gender'],
            age=request.POST['age']
            )
         return redirect('/')
      client = ClientInformations.objects.all()
      return render(request,'new_mainpage.html',{'client':client})
  
def AddVoucher(request):
    form = CreateVoucher()
    if request.method == 'POST':
        voucher = CreateVoucher(request.POST)
        if voucher.is_valid():
            voucher.save()
            return redirect('mainpage')
    value = {'form':form}
    return render(request, 'add.html',value)

def AddClient(request):
    form = CreateClient()
    if request.method == 'POST':
        client = CreateClient(request.POST)
        if client.is_valid():
            client.save()
            return redirect('mainpage')
    value = {'form':form}
    return render(request, 'add.html',value)

def ClientPage(request):
      client = ClientInformations.objects.all()
      context = {'clients':client}
      return render(request,'client.html',context)

def ServicePage(request):
      service = Service.objects.all()
      context = {'service':service}
      return render(request,'service.html',context)

def ArtistPage(request):
      artists = ArtistInformation.objects.all()
      context = {'artists':artists}
      return render(request,'artist.html',context)

def AddArtist(request):
    form = CreateArtist()
    if request.method == 'POST':
        artists = CreateArtist(request.POST)
        if artists.is_valid():
            artists.save()
            return redirect('artist')
    value = {'form':form}
    artist_names = ArtistInformation.objects.all()
    return render(request,'add.html',value)

def AddService(request):
    form = CreateService()
    if request.method == 'POST':
        service = CreateService(request.POST)
        if service.is_valid():
            service.save()
            return redirect('service')
    value = {'form':form}
    return render(request, 'add.html',value)

def AddPayment(request):
    form = CreatePayment()
    if request.method == 'POST':
        payment = CreatePayment(request.POST)
        if payment.is_valid():
            payment.save()
            return redirect('artist')
    value = {'form':form}
    artist_names = ArtistInformation.objects.all()
    return render(request,'add.html',value)

def UpdateClient(request,pk):
    updateditem = ClientInformations.objects.get(id=pk)
    form = CreateClient(instance=updateditem)
    if request.method == "POST":
        client = CreateClient(request.POST,instance=updateditem)
        if client.is_valid:
            client.save()
            return redirect('mainpage')

    value = {'form':form}
    return render(request, 'add.html',value)

def UpdateArtist(request,pk):
    updateditem = ArtistInformation.objects.get(id=pk)
    form = CreateArtist(instance=updateditem)
    if request.method == "POST":
        artist = CreateArtist(request.POST,instance=updateditem)
        if artist.is_valid:
            artist.save()
            return redirect('artist')

    value = {'form':form}
    return render(request, 'add.html',value)

def UpdateService(request,pk):
    updateditem = Service.objects.get(id=pk)
    form = CreateService(instance=updateditem)
    if request.method == "POST":
        service = CreateService(request.POST,instance=updateditem)
        if service.is_valid:
            service.save()
            return redirect('service')

    value = {'form':form}
    return render(request, 'add.html',value)

def DeleteClient(request,pk):
    deleteclient = ClientInformations.objects.get(id=pk)
    if request.method == "POST":
        deleteclient.delete()
        return redirect('mainpage')
    value = {'item':deleteclient}
    return render(request, 'add.html',value)

def DeleteArtist(request,pk):
    deleteartist = ArtistInformation.objects.get(id=pk)
    if request.method == "POST":
        deleteartist.delete()
        return redirect('artist')
    value = {'item':deleteartist}
    return render(request, 'add.html',value)

def DeleteService(request,pk):
    deleteitem = Service.objects.get(id=pk)
    if request.method == "POST":
        deleteitem.delete()
        return redirect('service')
    value = {'item':deleteitem}
    return render(request, 'add.html',value)
