from django.shortcuts import render

import json
import requests
import logging

from rest_framework.decorators import api_view
from rest_framework.response import Response

api_key = "key"

logger = logging.getLogger(__name__)

@api_view(["POST"])
def stable_diffusion(request):
    logger.info("In image_generation")
    try:
        payload = request.data
        prompt = payload.get("prompt")
        aspect_ratio = payload.get("aspect_ratio")
        output_format = payload.get("output_format")
        
        if not prompt or not aspect_ratio or not output_format:
            logger.error("Missing required fields in the request payload")
            return Response({"status": "error", "detail": "Missing required fields"})

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        
        response = requests.post("https://api.stability.ai/v2beta/stable-image/generate/sd3", headers=headers, json=payload)
        
        if response.status_code == 200:
            pass
        else:
            print(f"Error: {response.status_code} - {response.text}")
 
    except json.DoesNotExist:
        logger.error("Invalid JSON format for scenes")
        return Response({"status": "error", "detail": "Invalid Json format"})
    except Exception as e:
        logger.exception("An unexpected error occured: %s", str(e))
        return Response({"status": "error", "detail": "An unexcepted error occured"}, status=500)


def lightx(request):
    pass