from PIL import Image, ImageDraw, ImageFont
import random
import os
import json

def create_erc721_metadata(file_path,nr,image,cuteness,hairy):
    
    data = {
        "name": "QuantumCert",
        "description": f"Quantum Teleportation Cert #{nr}",
        "image": image,
        "attributes": [
            {
                "trait_type": "cuteness",
                "value": int(cuteness)
            },
            {
                "trait_type": "hairy",
                "value": int(hairy)
            }
        ]
    }    
    
    with open(file_path, "w") as json_file:
        json.dump(data, json_file)
    
    return file_path

def generate_certificate(name, issued_date, certificate_holder, quantum_computer, num_qubits):
    # Create a blank white image with appropriate dimensions (you can customize the size as needed)
    image_width, image_height = 600, 500
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)

    # Load a suitable font (you can change the font and size as desired)
    #font_path = "path_to_your_font_file.ttf"  # Replace with the path to your chosen font file
    #font_size = 24
    #font = ImageFont.truetype(font_path, font_size)

    # Define the text content and positions for each field
    certificate_name = "Quantum Teleportation Certificate"
    certificate_number = f"Certificate Number: {random.randint(1000, 9999)}"
    issued_date_text = f"Issued Date: {issued_date}"
    holder_name = f"Certification Holder: {certificate_holder}"
    quantum_computer_info = f"Quantum Computer: {quantum_computer} ({num_qubits} qubits)"

    # Calculate text positions to center-align them on the image
    text_x = image_width // 2
    line_spacing = 32
    starting_y = 30
    positions = [
        (text_x, starting_y),
        (text_x, starting_y + line_spacing),
        (text_x, starting_y + 2 * line_spacing),
        (text_x, starting_y + 3 * line_spacing),
        (text_x, starting_y + 4 * line_spacing),
    ]

    # Write the text on the image
    draw.text((text_x, 20), certificate_name,  fill='black', anchor='mt')
    for text, position in zip([certificate_number, issued_date_text, holder_name, quantum_computer_info], positions):
        draw.text(position, text,  fill='black', anchor='mt')

    # Save the image with a unique filename
    output_filename = f"certs/Quantum_Teleportation_Cert_{name}.png"
    image.save(output_filename)

    # Display the generated filename
    print(f"Certificate image saved as: {output_filename}")


    #generate_certificate(name, issued_date, certificate_holder, quantum_computer, num_qubits)
