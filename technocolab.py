
import streamlit as st
import pickle
import numpy as np
model1 = pickle.load(open('model1.pkl','rb'))
def predict_genre(acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence):
    input=np.array([[acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence]]).astype(np.float64)
    prediction=model1.predict(input)
    return float(prediction)
def main():
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;"> Song Genre Classification App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    acousticness = st.text_input("Acousticness")
    danceability = st.text_input("Danceability")
    energy = st.text_input("Energy")
    instrumentalness = st.text_input("Instrumentalness")
    liveness = st.text_input("Liveness")
    speechiness = st.text_input("Speechinesss")
    tempo = st.text_input("Tempo")
    valence = st.text_input("Valence")
    
    rock_html="""  
      <div style="background-color:#F4D03F;padding:10px >
       <h2 style="color:white;text-align:center;"> You like Rock music, enjoy Rock music.</h2>
       </div>
    """
    hiphop_html="""  
      <div style="background-color:#F08080;padding:10px >
       <h2 style="color:black ;text-align:center;"> You like "Hip-Hop" music, enjoy "Hip-Hop" music.</h2>
       </div>
    """
    
    if st.button("Predict"):
        output = predict_genre(acousticness, danceability, energy, instrumentalness, liveness, speechiness, tempo, valence)
        st.success(output)
        if output > 0.5:
            st.markdown(hiphop_html,unsafe_allow_html=True)
        else:
            st.markdown(rock_html,unsafe_allow_html=True)
if __name__=='__main__':
    main()














