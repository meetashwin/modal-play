import modal

# Stub is an object that defines everything that we run on the cloud
# It is our handle to the cloud runtime engine
stub = modal.Stub("example-get-started")

# Modal function that will be executed on the cloud, remotely
# All resource and runtime provisioning will be handled by Modal
@stub.function()
def square(x):
    print("This code is running on a remote worker!")
    return x**2

# Runs locally and invokes the cloud function
# When it is called, following happens
# Take the code, put inside a container and run it, stream all output back to computer
@stub.local_entrypoint()
def main():
    print("the square is", square.remote(42))
