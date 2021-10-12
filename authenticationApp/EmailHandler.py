from django.core.mail import EmailMessage, message
class EmailHandlerClass:
    @staticmethod
    def sendEmail(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], to=[data['email_to']])
        email.send()
        # email.send()
        
        