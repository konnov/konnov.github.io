#!/usr/bin/env python3

from PIL import Image
import base64
import io
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) != 2:
        print("Usage: python webp.py <image_path> <quality>")
        sys.exit(1)

    input_file = args[0]
    output_file = args[0].replace(".png", ".webp")
    quality = int(args[1])

    # Load the PNG image
    with Image.open(args[0]) as img:
        # Convert to RGB if the image has transparency
        if img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        # Save to file
        img.save(output_file, format="WEBP", quality=quality)

        # Save to memory for base64
        buffer = io.BytesIO()
        img.save(buffer, format="WEBP", quality=quality)
        webp_data = buffer.getvalue()
        base64_webp = base64.b64encode(webp_data).decode("utf-8")
        data_url = f"data:image/webp;base64,{base64_webp}"

    # Encode WebP image to base64
    base64_webp = base64.b64encode(webp_data).decode("utf-8")

    # Create the data URL
    data_url = f"data:image/webp;base64,{base64_webp}"

    print(data_url)