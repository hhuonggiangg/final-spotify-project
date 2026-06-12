# 🎵 SPOTIFY POPULARITY PREDICTOR - ULTIMATE PRO VERSION

A beautiful, interactive Streamlit web application that predicts Spotify song popularity using machine learning!

## 🌟 NEW FEATURES (Upgraded Version)

### ✨ **Spotify-Like UI Design**
- Modern glassmorphism design inspired by Spotify
- Dark theme with smooth animations and transitions
- Spotify green accent colors (#1DB954)
- Custom scrollbars, buttons, and cards
- Smooth page transitions and hover effects

### 📱 **Direct Share to Social Media**
- **Instagram** - Share directly with pop-up link
- **Twitter/X** - Tweet your predictions instantly
- **WhatsApp** - Message friends about tracks
- **TikTok** - Share music trend insights
- **Facebook** - Post to your timeline

Each share button opens the respective platform with pre-filled messages!

### 🎵 **Interactive Elements**
- Music visualizer animation (bouncing bars)
- Animated metrics cards
- Interactive sliders for song features
- Browse and filter songs database
- Search by artist functionality
- Like/Favorite system with timestamps

### 🎯 **Prediction System**
- Input song features (danceability, energy, valence, etc.)
- Real-time prediction of popularity score (0-100)
- Key insights on what drives popularity
- Confidence scoring
- Visual progress indicators

### 📊 **Analytics Dashboard**
- Average popularity metrics across database
- Top 10 artists ranking
- Song filtering by popularity range
- Feature comparison tools
- Trending tracks section

### 👤 **User Features**
- User authentication (Sign In / Sign Up)
- Personal profile with statistics
- Favorites list with timestamps
- Prediction history
- Badge system (coming soon)

---

## 📋 REQUIREMENTS

```
streamlit>=1.28.0
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.0.0
pickle5>=0.0.12 (Python < 3.8)
```

---

## 🚀 INSTALLATION & SETUP

### 1. **Clone/Download the Project**
```bash
cd your-project-folder
```

### 2. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 3. **Prepare Your Files**

Make sure you have these files in your project directory:
```
├── app_upgraded.py           # Main app file
├── spotify_songs_expanded.csv # Dataset (~500 songs)
├── model_lr.pkl              # Pre-trained model
├── scaler.pkl                # Feature scaler
├── model_info.pkl            # Model info
└── requirements.txt
```

### 4. **Run the Application**
```bash
streamlit run app_upgraded.py
```

The app will open in your browser at: `http://localhost:8501`

---

## 🎮 HOW TO USE

### **Step 1: Authentication**
- Create an account or sign in
- Use any username/password (it's demo authentication)

### **Step 2: Predict Popularity**
1. Go to "🎵 Predictor" section
2. Enter song title and artist name
3. Adjust song features using sliders:
   - 💃 **Danceability** - How suitable for dancing (0-1)
   - ⚡ **Energy** - Intensity and activity (0-1)
   - 😊 **Valence** - Musical positivity (0-1)
   - 🎸 **Acousticness** - Acoustic vs electronic (0-1)
   - 🎤 **Speechiness** - Spoken words presence (0-1)
   - 🎼 **Instrumentalness** - Instrumental vs vocal (0-1)
   - 🎤 **Liveness** - Live recording feel (0-1)
   - 🎹 **Key** - Musical key (0-11)
   - 🎶 **Tempo** - Speed in BPM (50-200)
   - ⏱️ **Duration** - Length in milliseconds

4. Click "🚀 PREDICT POPULARITY"
5. Get instant prediction result!

### **Step 3: Share Your Prediction**
Click any share button to open:
- 📸 **Instagram** - Share song prediction image
- 𝕏 **Twitter** - Tweet the prediction
- 💬 **WhatsApp** - Message friends
- ❤️ **Favorites** - Save to your collection
- 📊 **Analytics** - View detailed stats

### **Step 4: Browse Database**
- Go to "🎧 Browse" section
- Filter by popularity range
- Search for specific artists
- Like songs to add to favorites
- View song features and metrics

### **Step 5: View Analytics**
- Check average metrics across all songs
- See top 10 most popular artists
- Explore trends in music database

### **Step 6: Check Your Profile**
- View prediction statistics
- See saved favorites list
- Track your usage metrics

---

## 📊 SONG FEATURES EXPLAINED

| Feature | Range | Meaning |
|---------|-------|---------|
| Danceability | 0-1 | How suitable for dancing |
| Energy | 0-1 | Intensity and activity level |
| Key | 0-11 | Musical key/pitch |
| Loudness | dB | Amplitude/volume |
| Mode | 0-1 | Major/minor mode |
| Speechiness | 0-1 | Presence of spoken words |
| Acousticness | 0-1 | Acoustic vs electronic |
| Instrumentalness | 0-1 | Lack of vocals |
| Liveness | 0-1 | Audience/live feeling |
| Valence | 0-1 | Musical positivity |
| Tempo | BPM | Speed of track |
| Duration | ms | Length of track |
| Time Signature | - | Beats per measure |

---

## 🎨 DESIGN FEATURES

### **Color Scheme**
- Primary: Spotify Green (#1DB954)
- Secondary: Cyan (#06B6D4)
- Background: Dark Navy (#0F172A)
- Accents: Light (#1ed760)

### **Animations**
- Fade-in transitions
- Slide animations on cards
- Hover scale effects
- Pulse on active elements
- Floating animations
- Bounce effects on visualizer

### **Components**
- Glassmorphism cards (frosted glass effect)
- Gradient text backgrounds
- Music visualizer bars
- Progress indicators
- Smooth scrollbar
- Custom tags and badges

---

## 💾 DATA FORMAT

The CSV should have these columns:
```csv
track_name,artist_name,popularity,danceability,energy,key,loudness,
mode,speechiness,acousticness,instrumentalness,liveness,valence,
tempo,duration_ms,time_signature
```

Example:
```csv
Blinding Lights,The Weeknd,86,0.73,0.72,11,-5.313,1,0.246,0.166,0.002,0.1,0.334,174100,200040,4
```

---

## 🔗 SHARE URLS GENERATED

Each share button generates dynamic URLs:

**Instagram:**
```
https://www.instagram.com/?text=Your%20Message
```

**Twitter:**
```
https://twitter.com/intent/tweet?text=Your%20Tweet
```

**WhatsApp:**
```
https://wa.me/?text=Your%20Message
```

---

## 🛠️ CUSTOMIZATION

### Change Colors
Edit the CSS color variables in the app:
```python
--spotify-green: #1DB954;
--spotify-black: #191414;
--spotify-gray: #282828;
```

### Modify Share Message
Edit the `get_share_url()` function:
```python
message = f"Your Custom Message: {song_title}"
```

### Add More Features
Extend the song features section by adding more sliders and updating the prediction model.

---

## 📈 PERFORMANCE TIPS

1. **Optimize Dataset Size**
   - Keep CSV files under 50MB
   - Filter historical data if needed

2. **Cache Data**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv('data.csv')
   ```

3. **Lazy Load Images**
   - Load images only when needed
   - Use low-res thumbnails initially

---

## 🐛 TROUBLESHOOTING

### **App won't run**
```bash
# Clear Streamlit cache
rm -rf ~/.streamlit/
streamlit run app_upgraded.py
```

### **Dataset not found**
- Ensure CSV file is in correct directory
- Check file permissions
- Verify file name matches code

### **Model predictions are off**
- Retrain model with new data
- Check feature scaling
- Verify feature order matches training

### **Share buttons not working**
- Check internet connection
- Clear browser cache
- Try incognito mode
- Update browser

---

## 📝 FILE STRUCTURE

```
project/
├── app_upgraded.py              # Main application
├── spotify_songs_expanded.csv    # Dataset
├── model_lr.pkl                  # Trained model
├── scaler.pkl                    # Feature scaler
├── model_info.pkl                # Model metadata
├── requirements.txt              # Dependencies
├── 01_EDA.py                     # Exploratory analysis
├── 02_Model_Training.py          # Model training script
└── README.md                     # This file
```

---

## 🎯 FUTURE ENHANCEMENTS

- [ ] Real Spotify API integration
- [ ] User playlists management
- [ ] Genre-specific predictions
- [ ] Collaboration features
- [ ] Advanced analytics dashboard
- [ ] Export predictions as CSV/PDF
- [ ] Mobile app version
- [ ] Real-time trend analysis
- [ ] ML model improvements
- [ ] Admin dashboard

---

## 📄 LICENSE

This project is open source and available for educational and commercial use.

---

## 👨‍💻 SUPPORT

For issues or questions:
1. Check the troubleshooting section
2. Review Streamlit documentation
3. Check console for error messages
4. Verify all dependencies are installed

---

## 🎉 ENJOY!

This is your ultimate Spotify music prediction tool. Have fun predicting and sharing! 🎵

**Made with ❤️ and Music** 🎧
