class BucketlistMiddleware(object):
    def process_request(self, request):
        print "Middleware executed"
