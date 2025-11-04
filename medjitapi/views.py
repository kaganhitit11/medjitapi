from django.http import JsonResponse
from django.db import connection
from django.core.exceptions import ImproperlyConfigured
import json


def health_check(request):
    """
    Health check endpoint that verifies:
    - Application is running
    - Database connection is working
    """
    health_status = {
        "status": "healthy",
        "checks": {
            "application": "ok",
            "database": "unknown"
        },
        "timestamp": None
    }
    
    try:
        from django.utils import timezone
        health_status["timestamp"] = timezone.now().isoformat()
    except:
        import datetime
        health_status["timestamp"] = datetime.datetime.now().isoformat()
    
    # Test database connection
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        health_status["checks"]["database"] = "ok"
    except Exception as e:
        health_status["checks"]["database"] = f"error: {str(e)}"
        health_status["status"] = "unhealthy"
    
    # Return appropriate HTTP status code
    status_code = 200 if health_status["status"] == "healthy" else 503
    
    return JsonResponse(health_status, status=status_code)
