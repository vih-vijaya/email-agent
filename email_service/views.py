from django.shortcuts import render

# Create your views here.
import csv
from io import TextIOWrapper
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import CSVUploadSerializer

@api_view(['POST'])
def upload_csv(request):
    if request.method == 'POST':
        serializer = CSVUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            # Decode the file into a string to read as CSV
            csv_file = TextIOWrapper(file, encoding='utf-8')
            csv_reader = csv.reader(csv_file)

            senders = []
            receivers = []
            for row in csv_reader:
                sender_email, receiver_email = row
                senders.append(sender_email)
                receivers.append(receiver_email)

            # Call send_email function
            send_bulk_emails(senders, receivers)
            
            return Response({"message": "CSV uploaded and emails sent successfully."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_bulk_emails(senders, receivers):
    for sender_email, receiver_email in zip(senders, receivers):
        send_mail(
            'Subject here',  # Subject
            'Here is the message.',  # Body
            sender_email,  # Sender
            [receiver_email],  # Receiver
            fail_silently=False,
        )
