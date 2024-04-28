import streamlit as st
from tooth_detection import run_model


uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    placeholder = st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_image.read())

    run_model(image_path)

    placeholder.empty()

    st.image('static/output/output.jpg', caption="Processed Image", use_column_width=True)
