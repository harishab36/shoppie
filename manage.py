#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
        if len(sys.argv) == 1 and "runserver" not in sys.argv:
            pass
        # Check if runserver is being called without an explicit port
        if "runserver" in sys.argv and len(sys.argv) == 2:
            port = os.getenv('DJANGO_PORT', '8080')
            sys.argv.append(f"127.0.0.1:{port}")
        execute_from_command_line(sys.argv)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
