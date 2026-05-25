import streamlit as st
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="K10 - Ôn tập từ vựng - Bài 2", page_icon="📚", layout="centered")

# --- DỮ LIỆU TỪ VỰNG ---
vocab_list = [
    {"hanzi": "重新", "pinyin": "chóngxīn", "meaning": "lại, từ đầu"},
    {"hanzi": "尽管", "pinyin": "jǐnguǎn", "meaning": "mặc dù, cho dù"},
    {"hanzi": "真正", "pinyin": "zhēnzhèng", "meaning": "thật sự"},
    {"hanzi": "友谊", "pinyin": "yǒuyì", "meaning": "tình bạn"},
    {"hanzi": "适应", "pinyin": "shìyìng", "meaning": "thích nghi"},
    {"hanzi": "交", "pinyin": "jiāo", "meaning": "kết giao"},
    {"hanzi": "平时", "pinyin": "píngshí", "meaning": "ngày thường"},
    {"hanzi": "逛", "pinyin": "guàng", "meaning": "dạo"},
    {"hanzi": "短信", "pinyin": "duǎnxìn", "meaning": "tin nhắn"},
    {"hanzi": "正好", "pinyin": "zhènghǎo", "meaning": "đúng lúc"},
    {"hanzi": "聚会", "pinyin": "jùhuì", "meaning": "tụ họp"},
    {"hanzi": "联系", "pinyin": "liánxì", "meaning": "liên lạc"},
    {"hanzi": "差不多", "pinyin": "chàbuduō", "meaning": "gần như, xấp xỉ"},
    {"hanzi": "专门", "pinyin": "zhuānmén", "meaning": "đặc biệt, chuyên"},
    {"hanzi": "毕业", "pinyin": "bìyè", "meaning": "tốt nghiệp"},
    {"hanzi": "麻烦", "pinyin": "máfan", "meaning": "làm phiền"},
    {"hanzi": "好像", "pinyin": "hǎoxiàng", "meaning": "hình như, giống như, dường như"}
]

# --- DỮ LIỆU CÂU HỎI TRẮC NGHIỆM ---
raw_quiz_data = [
    ("我想_____开始。", "重新"),
    ("这张画没画好，我要_____画。", "重新"),
    ("衣服没洗干净，你再_____洗一下。", "重新"),
    ("一个人除了钱什么都没有，那不是_____的幸福。", "真正"),
    ("我们12岁的时候第一次见面，我们的_____就开始了。", "友谊"),
    ("让我们为了两国人民的_____干杯！", "友谊"),
    ("我已经_____这里的生活了。", "适应"),
    ("我们要改变自己，努力去_____新的环境。", "适应"),
    ("我喜欢_____朋友。", "交"),
    ("我很高兴自己能_____到一个喜欢学汉语的朋友。", "交"),
    ("我很喜欢画画，_____一有时间就会画一画。", "平时"),
    ("你注意到没有？小明今天和_____不太一样。", "平时"),
    ("昨天_____书店的时候，我买了几本书。", "逛"),
    ("昨天我跟朋友_____街逛到晚上10点多才回家。", "逛"),
    ("我收到了一条新_____。", "短信"),
    ("麻烦你发一条_____，告诉我见面的时间和地点。", "短信"),
    ("我下午也要去踢足球，_____一起去吧。", "正好"),
    ("明年大学同学_____，你能不能去？", "聚会"),
    ("跟老朋友_____，吃吃饭、聊聊天儿，多高兴啊！", "聚会"),
    ("我们一定要保持_____！", "联系"),
    ("电子邮件是我和老师最常用的_____方式。", "联系"),
    ("昨天晚上我_____一夜没有睡。", "差不多"),
    ("我是_____来看你的。", "专门"),
    ("这一年我打算_____学电脑，别的什么事都不做。", "专门"),
    ("他是翻译方面的_____人才。", "专门"),
    ("他儿子才17岁，已经高中_____了。", "毕业"),
    ("我爸爸_____于清华大学。", "毕业"),
    ("王老师_____于1994年。", "毕业"),
    ("_____您了，还专门送我回家，谢谢。", "麻烦"),
    ("我找不到我的手机了，能不能_____你们帮我找一下。", "麻烦"),
    ("_____帮我拿一下水杯，我上个洗手间。", "麻烦"),
    ("你_____很困，睡一会儿吧。", "好像"),
    ("他_____从来都不会累，总是一副很有精神的样子。", "好像")
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0

def init_quiz():
    """Khởi tạo hoặc làm mới bài Quiz"""
    all_words = [item["hanzi"] for item in vocab_list]
    questions = []
    
    for q_text, ans in raw_quiz_data:
        options = [ans]
        # Lấy thêm 3 đáp án sai ngẫu nhiên
        while len(options) < 4:
            w = random.choice(all_words)
            if w not in options:
                options.append(w)
        random.shuffle(options)
        
        questions.append({
            "question": q_text,
            "answer": ans,
            "options": options
        })
    
    # Xáo trộn thứ tự các câu hỏi
    random.shuffle(questions)
    st.session_state.quiz_questions = questions
    st.session_state.submitted = False

# Chạy khởi tạo lần đầu tiên
if 'quiz_questions' not in st.session_state:
    init_quiz()

def next_card():
    if st.session_state.card_index < len(vocab_list) - 1:
        st.session_state.card_index += 1
    else:
        st.session_state.card_index = 0

def prev_card():
    if st.session_state.card_index > 0:
        st.session_state.card_index -= 1
    else:
        st.session_state.card_index = len(vocab_list) - 1

def submit_quiz():
    st.session_state.submitted = True

# --- GIAO DIỆN CHÍNH ---
st.title("📚 K10 - Ôn tập từ vựng - Bài 2")
st.markdown("---")

# ==========================================
# 1. KHU VỰC FLASHCARD
# ==========================================
st.subheader("💡 Ôn tập Flashcard")
st.caption("Di chuột (hoặc chạm vào thẻ) để xem Pinyin và Nghĩa.")

current_word = vocab_list[st.session_state.card_index]

flip_card_css = f"""
<style>
.flip-card {{
  background-color: transparent;
  width: 100%;
  height: 250px;
  perspective: 1000px;
  margin-bottom: 20px;
}}
.flip-card-inner {{
  position: relative;
  width: 100%;
  height: 100%;
  text-align: center;
  transition: transform 0.6s;
  transform-style: preserve-3d;
  box-shadow: 0 4px 12px 0 rgba(0,0,0,0.15);
  border-radius: 15px;
}}
.flip-card:hover .flip-card-inner {{
  transform: rotateY(180deg);
}}
.flip-card-front, .flip-card-back {{
  position: absolute;
  width: 100%;
  height: 100%;
  -webkit-backface-visibility: hidden;
  backface-visibility: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  border-radius: 15px;
  padding: 20px;
}}
.flip-card-front {{
  background-color: #ffffff;
  color: #1565c0;
  border: 2px solid #bbdefb;
}}
.flip-card-back {{
  background-color: #1565c0;
  color: white;
  transform: rotateY(180deg);
}}
.hanzi-text {{
  font-size: 70px;
  font-weight: bold;
  font-family: 'KaiTi', 'SimSun', serif;
}}
.pinyin-text {{
  font-size: 28px;
  margin-bottom: 15px;
}}
.meaning-text {{
  font-size: 22px;
}}
</style>

<div class="flip-card">
  <div class="flip-card-inner">
    <div class="flip-card-front">
      <div class="hanzi-text">{current_word['hanzi']}</div>
    </div>
    <div class="flip-card-back">
      <div class="pinyin-text">{current_word['pinyin']}</div>
      <div class="meaning-text">{current_word['meaning']}</div>
    </div>
  </div>
</div>
"""
st.markdown(flip_card_css, unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    st.button("⬅️ Trước", on_click=prev_card, use_container_width=True)
with col2:
    st.markdown(f"<div style='text-align: center; font-size: 16px; padding-top: 5px;'>Từ {st.session_state.card_index + 1} / {len(vocab_list)}</div>", unsafe_allow_html=True)
with col3:
    st.button("Tiếp ➡️", on_click=next_card, use_container_width=True)

st.markdown("---")

# ==========================================
# 2. KHU VỰC QUIZ
# ==========================================
st.subheader("📝 Kiểm tra: Điền từ vào chỗ trống")
st.info("Chọn từ thích hợp để điền vào chỗ trống trong các câu dưới đây.")

score = 0
total_questions = len(st.session_state.quiz_questions)

# Tạo form để nộp bài
with st.form(key='quiz_form'):
    for i, q in enumerate(st.session_state.quiz_questions):
        st.markdown(f"**Câu {i+1}:** {q['question']}")
        
        # Streamlit radio để chọn đáp án (index=None bắt người dùng phải tự click)
        user_choice = st.radio(
            label=f"Đáp án câu {i+1}",
            options=q['options'],
            horizontal=True,
            index=None,
            label_visibility="collapsed",
            key=f"q_{i}"
        )
        
        # Nếu đã nộp bài, hiển thị kết quả đúng/sai ngay bên dưới câu hỏi
        if st.session_state.submitted:
            if user_choice == q['answer']:
                score += 1
                st.success(f"✅ Chính xác! ({q['answer']})")
            elif user_choice is None:
                st.warning(f"⚠️ Bạn chưa chọn đáp án. Đáp án đúng là: **{q['answer']}**")
            else:
                st.error(f"❌ Sai rồi! Đáp án đúng là: **{q['answer']}**")
                
        st.write("---") # Đường kẻ mờ chia cách các câu

    # Nút bấm nộp bài
    submit_button = st.form_submit_button(label="Nộp bài chấm điểm", on_click=submit_quiz)

# Sau khi nộp, hiện điểm và nút làm lại bài
if st.session_state.submitted:
    st.subheader("📊 Kết quả của bạn:")
    st.markdown(f"<h2 style='color:#d32f2f;'>{score} / {total_questions}</h2>", unsafe_allow_html=True)
    
    if score == total_questions:
        st.balloons()
        st.success("Tuyệt vời! Bạn đã làm đúng tất cả các câu! 🥳")
    elif score > total_questions * 0.7:
        st.info("Rất tốt! Bạn nắm khá vững từ vựng rồi đó. 👍")
    else:
        st.warning("Cố gắng ôn tập thêm trên Flashcard nhé! 💪")
        
    st.button("🔄 Làm lại bài (Đổi ngẫu nhiên câu hỏi & đáp án)", on_click=init_quiz, type="primary")
