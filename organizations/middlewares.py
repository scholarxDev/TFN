from .models import Organization

class OrganizationAwareMiddleware:
    """
    Middleware to attach organization property to request object
    """

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("Middleware called")

        request.organization = self.organization_from_request(request)

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    def hostname_from_request(self, request):
        # split on `:` to remove port
        return request.get_host().split(':')[0].lower()


    def organization_from_request(self, request):
        hostname = self.hostname_from_request(request)
        subdomain_prefix = hostname.split('.')[0]
        try:
            org = Organization.objects.get(subdomain_prefix=subdomain_prefix)
            print(f"Organization detected: {org}")
        except Organization.DoesNotExist:
            org = Organization.objects.get_or_create(subdomain_prefix="scholarx", name='scholarx')

        return org