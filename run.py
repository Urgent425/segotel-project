# run.py
from app.api import db, create_api_app
from app.web import create_web_app
from app.api.models.customer import Customer
from app.api.models.invoice import Invoice
from app.api.models.service import Service
from app.api.models.ticket import Ticket
from app.api.models.employee import Employee
from app.api.models.notification import Notification
from app.api.models.service_usage import ServiceUsage
from app.api.models.customer_activity import CustomerActivity
from app.api.models.integration import Integration

from multiprocessing import Process
import socket

def is_port_in_use(port):
    """Check if the port is already in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex(('localhost', port)) == 0


def run_web_app():
    if not is_port_in_use(5001):
        web_app = create_web_app()
        web_app.run(port=5001, debug=False)


def run_api_app():
     if not is_port_in_use(5000):
        api_app = create_api_app()
        api_app.run(port=5000, debug=False)
        with api_app.app_context():
            db.create_all()


#api_app = create_api_app()
#web_app = create_web_app()
# Create all tables automatically when the app starts
#with api_app.app_context():
    #db.create_all()

#if __name__ == "__main__":
 #   api_app.run(debug=False, port=5000)
  #  web_app.run(debug= False, port = 5001)


if __name__ == '__main__':
    # Create separate processes for web and API
    web_process = Process(target=run_web_app)
    api_process = Process(target=run_api_app)

    # Start both processes
    web_process.start()
    api_process.start()

    # Wait for both processes to complete
   # web_process.join()
   # api_process.join()