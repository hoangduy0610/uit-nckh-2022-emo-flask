from __main__ import app

from controllers.image import image_process_controller

# Process images
@app.route("/process", methods=["POST"])
def image_process_route():
    return image_process_controller()