import streamlit as st
from datetime import datetime

# KONFIGURASI HALAMAN
st.set_page_config(
    page_title="Chatbot Kesehatan",
    page_icon="icon1.png",
    layout="wide"
)

# CSS STYLING 
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #1e1e2e 0%, #2d2d44 100%);
    }
    .chat-box {
        background: rgba(255, 255, 255, 0.95);
        padding: 25px;
        border-radius: 15px;
        margin: 10px 0;
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .user-msg {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
        color: white;
        font-weight: 500;
    }
    .bot-msg {
        background: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        color: #2c3e50;
    }
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.98);
    }
    h1 {
        color: white;
        text-align: center;
        padding: 20px;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    }
    h3 {
        color: #2c3e50;
    }
    .chat-box p, .chat-box li {
        color: #2c3e50;
    }
    </style>
""", unsafe_allow_html=True)

# DATABASE PENGETAHUAN KESEHATAN
knowledge_base = {
    "sarapan": [
        "Sarapan sehat untuk pemula:\n• Oatmeal dengan buah\n• Roti gandum + telur rebus\n• Smoothie pisang + yogurt\n• Nasi merah + ayam + sayur",
        "Ingat: Sarapan penting untuk energi pagi hari! 💪"
    ],
    "olahraga": [
        "Olahraga untuk pemula:\n• Jalan kaki 30 menit/hari\n• Lari ringan 15-20 menit\n• Yoga/stretching 20 menit\n• Bersepeda santai",
        "Mulai dari yang ringan, konsisten lebih penting! 🏃"
    ],
    "air": [
        "Kebutuhan air minum:\n• Dewasa: 8 gelas (2 liter) per hari\n• Lebih banyak jika:\n  - Berolahraga\n  - Cuaca panas\n  - Sedang sakit",
        "Tips: Minum air saat bangun tidur dan sebelum makan 💧"
    ],
    "tidur": [
        "Tips tidur berkualitas:\n• Tidur 7-8 jam per malam\n• Matikan gadget 1 jam sebelum tidur\n• Kamar gelap dan sejuk\n• Tidur-bangun di jam yang sama",
        "Tidur cukup = tubuh dan pikiran sehat! 😴"
    ],
    "stress": [
        "Cara mengatasi stress:\n• Napas dalam-dalam (4-7-8)\n• Olahraga ringan\n• Meditasi 10 menit\n• Curhat ke teman/keluarga\n• Hobi yang menyenangkan",
        "Jangan simpan sendiri, cerita ke orang terdekat ya! 🤗"
    ],
    "diet": [
        "Tips diet sehat:\n• Makan teratur 3x sehari\n• Perbanyak sayur dan buah\n• Kurangi gorengan dan manis\n• Protein cukup (ayam, ikan, telur)\n• Hindari makan malam terlalu larut",
        "Diet = pola makan sehat, bukan kelaparan! 🥗"
    ],
    "vitamin": [
        "Vitamin penting:\n• Vitamin C: Jeruk, jambu, paprika\n• Vitamin D: Sinar matahari pagi\n• Vitamin B: Telur, daging, kacang\n• Vitamin A: Wortel, bayam",
        "Lebih baik dari makanan alami daripada suplemen! 🍊"
    ],
    "workout": [
        "Program workout pemula (3x seminggu):\n\nHari 1: Upper Body\n• Push up 3x10\n• Plank 3x30 detik\n\nHari 2: Lower Body\n• Squat 3x15\n• Lunges 3x10\n\nHari 3: Cardio\n• Lari/jalan 30 menit",
        "Jangan lupa pemanasan dan pendinginan! 💪"
    ]
}

# FUNGSI CHATBOT
def get_bot_response(user_input):
    """
    Fungsi untuk mendapatkan respons bot berdasarkan input user
    """
    user_input = user_input.lower()
    
    # Cek kata kunci dalam input
    for keyword, responses in knowledge_base.items():
        if keyword in user_input:
            return "\n\n".join(responses)
    
    # Respons umum berdasarkan topik
    if any(word in user_input for word in ["halo", "hai", "hello", "hi"]):
        return "Halo!👋 Saya Chatbot Kesehatan. Saya bisa bantu informasi tentang:\n\n• Sarapan sehat\n• Olahraga\n• Minum air\n• Tidur\n• Stress\n• Diet\n• Vitamin\n• Workout\n\nMau tanya apa?"
    
    elif any(word in user_input for word in ["makan", "makanan", "menu"]):
        return knowledge_base["sarapan"][0] + "\n\n" + knowledge_base["diet"][0]
    
    elif any(word in user_input for word in ["berat badan", "turun", "kurus"]):
        return "Tips menurunkan berat badan:\n• Defisit kalori (makan < bakar)\n• Olahraga rutin 3-5x seminggu\n• Minum air cukup\n• Tidur 7-8 jam\n• Kurangi gula dan gorengan\n\nIngat: Turun 0.5-1 kg per minggu itu sehat! 💪"
    
    elif any(word in user_input for word in ["gemuk", "naik"]):
        return "Tips menaikkan berat badan:\n• Surplus kalori (makan > bakar)\n• Makan 4-5x sehari porsi kecil\n• Protein tinggi\n• Workout (angkat beban)\n• Istirahat cukup\n\nKonsultasi ke ahli gizi lebih baik! 📈"
    
    elif any(word in user_input for word in ["terima kasih", "makasih", "thanks"]):
        return "Sama-sama! 😊Semoga sehat selalu ya! Ada yang mau ditanyakan lagi?"
    
    else:
        return "Maaf, saya belum paham pertanyaan Anda. 🤔\n\nCoba tanyakan tentang:\n• Sarapan sehat\n• Olahraga pemula\n• Minum air\n• Tips tidur\n• Mengatasi stress\n• Diet sehat\n• Vitamin\n• Workout\n\nAtau konsultasi ke dokter untuk masalah kesehatan serius ya! 👨‍⚕️"

# INISIALISASI SESSION STATE
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_name" not in st.session_state:
    st.session_state.user_name = ""

if "user_age" not in st.session_state:
    st.session_state.user_age = 25

if "user_goals" not in st.session_state:
    st.session_state.user_goals = []

# SIDEBAR - PROFIL PENGGUNA
with st.sidebar:
    page_icon="profil.png",
    layout="wide"
    st.title("Profil Anda")
    
    # Input Nama
    st.session_state.user_name = st.text_input(
        "Nama:", 
        value=st.session_state.user_name,
        placeholder="Masukkan nama Anda"
    )
    
    # Input Usia
    st.session_state.user_age = st.slider(
        "Usia:", 
        min_value=15, 
        max_value=80, 
        value=st.session_state.user_age
    )
    
    # Pilih Tujuan Kesehatan
    st.session_state.user_goals = st.multiselect(
        "Tujuan Kesehatan:",
        ["Turun Berat Badan", "Naik Berat Badan", "Lebih Fit", "Tidur Lebih Baik", "Kurangi Stress"],
        default=st.session_state.user_goals
    )
    
    st.divider()
    
    # Statistik
    st.subheader("Statistik")
    st.metric("Total Chat", len(st.session_state.messages))
    st.metric("Tujuan Aktif", len(st.session_state.user_goals))
    
    st.divider()
    
    # Tombol Reset
    if st.button("Hapus Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.divider()
    
    # Info
    st.info("💡 **Tips:**\nTanyakan tentang sarapan, olahraga, diet, stress, dll.")
    
    st.success("**Gratis** - Tanpa API Key")

# HEADER UTAMA
col1, col2 = st.columns([0.05, 1])

with col1:
    st.image("icon1.png", width=50)  

with col2:
    st.markdown("""
        <div style="display:flex; align-items:center; height:100%;">
            <h1 style="
                color:white; 
                font-weight:700; 
                text-shadow:2px 2px 4px rgba(0,0,0,0.3);
                margin: 0;
            ">
                Chatbot Kesehatan
            </h1>
        </div>
    """, unsafe_allow_html=True)

st.markdown("### *Asisten Kesehatan Digital Anda* 💪")

# Welcome message
if not st.session_state.messages:
    name = st.session_state.user_name if st.session_state.user_name else "Sobat Sehat"
    welcome = f"""
     <div class="chat-box">
        <h3 style="color: black;">👋 Halo {name}!</h3>
        <p>Saya <strong>Chatbot Kesehatan</strong>, siap membantu Anda dengan informasi seputar:</p>
        <ul>
            <li>🥗 Nutrisi dan makanan sehat</li>
            <li>💪 Program olahraga</li>
            <li>😴 Tips tidur berkualitas</li>
            <li>🧘 Manajemen stress</li>
            <li>💊 Vitamin dan suplemen</li>
        </ul>
        <p><strong>Silakan tanyakan apa saja!</strong></p>
        <small>⚠️ Untuk masalah kesehatan serius, konsultasi ke dokter ya!</small>
    </div>
    """
    st.markdown(welcome, unsafe_allow_html=True)

# ============================================
# DISPLAY CHAT HISTORY
# ============================================
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user-msg">
            <strong>👤 Anda:</strong><br>
            {msg["content"]}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-msg">
            <strong>🤖 Bot:</strong><br>
            {msg["content"]}
        </div>
        """, unsafe_allow_html=True)

# ============================================
# CHAT INPUT
# ============================================
user_question = st.chat_input("💬 Ketik pertanyaan Anda di sini...")

if user_question:
    # Simpan pertanyaan user
    st.session_state.messages.append({
        "role": "user",
        "content": user_question,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Dapatkan jawaban bot
    bot_answer = get_bot_response(user_question)
    
    # Simpan jawaban bot
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_answer,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })
    
    # Refresh halaman
    st.rerun()

# ============================================
# FOOTER
# ============================================
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💬 Pesan", len(st.session_state.messages))

with col2:
    if st.session_state.user_name:
        st.metric("👤 User", st.session_state.user_name)
    else:
        st.metric("👤 User", "Guest")

with col3:
    st.metric("🎯 Goals", len(st.session_state.user_goals))

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white;'>
    <p>💚 <strong>Chatbot Kesehatan v1.0</strong></p>
    <small>Dibuat dengan ❤️ menggunakan Streamlit</small><br>
    <small>⚠️ Selalu konsultasi dengan profesional kesehatan untuk masalah serius</small>
</div>
""", unsafe_allow_html=True)