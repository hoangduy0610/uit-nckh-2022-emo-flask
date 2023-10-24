from __main__ import app

from controllers.image import confirm_image_controller, image_process_controller

# Process images
@app.route("/process", methods=["POST"])
def image_process_route():
    return image_process_controller()

# Confirm image
@app.route("/confirm", methods=["POST"])
def confirm_image_route():
    return confirm_image_controller()