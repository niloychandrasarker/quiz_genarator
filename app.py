import streamlit as st
from api_calling import audio_Transcription, note_genarator, quiz_genarator
from PIL import Image

#Tittle
st.markdown(
	"""
	<h1 style='white-space: nowrap; font-size: 2.2rem; margin-bottom: 0.4rem;'>
	Notes Summary and Quiz Generator
	</h1>
	""",
	unsafe_allow_html=True,
)
st.markdown("upload your notes and get a summary and quiz questions")
st.divider()

#Sidebar
with st.sidebar:
    st.header("Controls")
    #image uploader
    images = st.file_uploader(
        "Upload the photo of your notes",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True,
    )

    pil_images = []
    for image in images:
        pil_image = Image.open(image)
        pil_images.append(pil_image)

    if images:
        if len(images) > 5:
           st.error("Please upload a maximum of 5 images.")
        else:
            st.subheader("Uploaded Notes")
            col = st.columns(len(images))
            for i, image in enumerate(images):
                with col[i]:
                    st.image(image)
    
    #Dificulty level
    selected_optiopn = st.selectbox(
        "Select the difficulty level of the quiz",
        ("Easy", "Medium", "Hard"),
        index=None,
    )



    pressed = st.button("Generate Summary and Quiz",type="primary")


if pressed:
    if not images:  
        st.error("Please upload at least one image of your notes.")
    if not selected_optiopn:
        st.error("Please select a difficulty level for the quiz.")

    if images and selected_optiopn:
        #notes
        with st.container(border=True): 
            st.subheader("Summary")
            with st.spinner("Generating summary..."):
                summary = note_genarator(pil_images)
                st.write(summary)

        #Audio_Transcription
        with st.container(border=True): 
            st.subheader("Audio Transcription")
            with st.spinner("Generating audio transcription..."):
                summary = summary.replace("\n", " ")
                summary = summary.replace("•", "")
                summary = summary.replace("~", "")
                summary = summary.replace("-", "")
                summary = summary.replace("*", "")
                summary = summary.replace("#", "")

                audio = audio_Transcription(summary)
                st.audio(audio)


        #Quiz
        with st.container(border=True): 
            st.subheader(f"Quiz Questions - {selected_optiopn} Level")

            with st.spinner("Generating quiz questions..."):
                quiz = quiz_genarator(pil_images, selected_optiopn)
                st.markdown(quiz)