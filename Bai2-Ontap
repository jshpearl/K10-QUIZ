import streamlit as st
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="Ôn tập Từ vựng HSK 4", page_icon="📚", layout="centered")

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

# --- DỮ LIỆU CÂU LÀM BÀI TẬP ---
sentences = [
    "我想重新开始。",
    "这张画没画好，我要重新画。",
    "衣服没洗干净，你再重新洗一下。",
    "一个人除了钱什么都没有，那不是真正的幸福。",
    "我们12岁的时候第一次见面，我们的友谊就开始了。",
    "让我们为了两国人民的友谊干杯！",
    "我已经适应这里的生活了。",
    "我们要改变自己，努力去适应新的环境。",
    "我喜欢交朋友。",
    "我很高兴自己能交到一个喜欢学汉语的朋友。",
    "我很喜欢画画，平时一有时间就会画一画。",
    "你注意到没有？小明今天和平时不太一样。",
    "昨天逛书店的时候，我买了几本书。",
    "昨天我跟朋友逛街逛到晚上10点多才回家。",
    "我收到了一条新短信。",
    "麻烦你发一条短信，告诉我见面的时间和地点。",
    "我下午也要去踢足球，正好一起去吧。",
    "明年大学同学聚会，你能不能去？",
    "跟老朋友聚会，吃吃饭、聊聊天儿，多高兴啊！",
    "我们一定要保持联系！",
    "电子邮件是我和老师最常用的联系方式。",
    "昨天晚上我差不多一夜没有睡。",
    "我是专门来看你的。",
    "这一年我打算专门学电脑，别的什么事都不做。",
    "他是翻译方面的专门人才。",
    "他儿子才17岁，已经高中毕业了。",
    "我爸爸毕业于清华大学。",
    "王老师毕业于1994年。",
    "麻烦您了，还专门送我回家，谢谢。",
    "我找不到我的手机了，能不能麻烦你们帮我找一下。",
    "麻烦帮我拿一下水杯，我上个洗手间。",
    "你好像很困，睡一会儿吧。",
    "他好像从来都不会累，总是一副很有精神的样子。"
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0

# Khởi tạo danh sách câu đã xáo trộn lần đầu
if 'shuffled_sentences' not in st.session_state:
    temp_sentences = sentences.copy()
    random.shuffle(temp_sentences)
    st.session_state.shuffled_sentences = temp_sentences

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

def reshuffle_sentences():
    temp_sentences = sentences.copy()
    random.shuffle(temp_sentences)
    st.session_state.shuffled_sentences = temp_sentences

# --- GIAO DIỆN CHÍNH ---
st.title("📚 Lớp học HSK 4 - Ôn tập Từ vựng")
st.markdown("---")

# 1. KHU VỰC FLASHCARD
st.subheader("💡 Flashcard (Di chuột hoặc chạm vào thẻ để lật)")

current_word = vocab_list[st.session_state.card_index]

flip_card_css = f"""
<style>
.flip-card {{
  background-color: transparent;
  width: 100%;
  height: 300px;
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
  color: #d32f2f;
  border: 2px solid #ffcdd2;
}}
.flip-card-back {{
  background-color: #d32f2f;
  color: white;
  transform: rotateY(180deg);
}}
.hanzi-text {{
  font-size: 80px;
  font-weight: bold;
  font-family: 'KaiTi', 'SimSun', serif;
}}
.pinyin-text {{
  font-size: 30px;
  margin-bottom: 15px;
}}
.meaning-text {{
  font-size: 24px;
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
    st.button("⬅️ Từ trước", on_click=prev_card, use_container_width=True)
with col2:
    st.markdown(f"<div style='text-align: center; font-size: 18px; padding-top: 10px;'>Từ {st.session_state.card_index + 1} / {len(vocab_list)}</div>", unsafe_allow_html=True)
with col3:
    st.button("Từ tiếp ➡️", on_click=next_card, use_container_width=True)

st.markdown("---")

# 2. KHU VỰC ÔN TẬP CÂU
st.subheader("📝 Luyện Đọc: Ôn tập mẫu câu")
st.info("Hãy đọc to và dịch nghĩa các câu dưới đây (Không sử dụng Pinyin để luyện phản xạ mặt chữ).")

# Nút để xáo trộn lại
st.button("🔀 Xáo trộn câu hỏi", on_click=reshuffle_sentences)
st.write("") # Tạo khoảng trắng

# In danh sách các câu đã được xáo trộn
for i, sentence in enumerate(st.session_state.shuffled_sentences, 1):
    st.markdown(f"**{i}.** {sentence}")
