import streamlit as st
from tooth_detection import run_model


uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    ph3 = st.empty()
    placeholder = st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    image_path = "uploaded_image.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_image.read())

    b1 = st.empty()
    b1click = b1.button('Segment')
    if(b1click):
        b1.empty()

        has_disease, fp = run_model(image_path)

        placeholder.empty()

        # ph2 = st.image(f'{fp}/image0.jpg', caption="Segmented Image", use_column_width=True)
        st.image('static/output/output.jpg', caption="Processed Image", use_column_width=True)

        if not has_disease:
            st.subheader(':green[NO DISEASES FOUND -- YOU HAVE VERY HEALTHY TEETH]')

