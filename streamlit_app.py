import streamlit as st
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(page_title="K10 - Ôn tập từ vựng - Bài 2", page_icon="📚", layout="centered")

# --- DỮ LIỆU TỪ VỰNG ---
vocab_list = [
    {"hanzi": "重新", "pinyin": "chóngxīn", "meaning": "lại, từ đầu"},
    {"hanzi": "尽管", "pinyin": "jǐnguǎn", "meaning": "mặc dù, cho dù / cứ việc"},
    {"hanzi": "真正", "pinyin": "zhēnzhèng", "meaning": "thật sự"},
    {"hanzi": "友谊", "pinyin": "yǒuyì", "meaning": "tình bạn"},
    {"hanzi": "适应", "pinyin": "shìyìng", "meaning": "thích nghi"},
    {"hanzi": "交", "pinyin": "jiāo", "meaning": "kết giao"},
    {"hanzi": "平时", "pinyin": "píngshí", "meaning": "ngày thường"},
    {"hanzi": "逛", "pinyin": "guàng", "meaning": "dạo"},
    {"hanzi": "短信", "pinyin": "duǎnxìn", "meaning": "tin nhắn"},
    {"hanzi": "正好", "pinyin": "zhènghǎo", "meaning": "đúng lúc, vừa vặn"},
    {"hanzi": "聚会", "pinyin": "jùhuì", "meaning": "tụ họp, bữa tiệc"},
    {"hanzi": "联系", "pinyin": "liánxì", "meaning": "liên lạc"},
    {"hanzi": "差不多", "pinyin": "chàbuduō", "meaning": "gần như, xấp xỉ"},
    {"hanzi": "专门", "pinyin": "zhuānmén", "meaning": "đặc biệt, chuyên môn"},
    {"hanzi": "毕业", "pinyin": "bìyè", "meaning": "tốt nghiệp"},
    {"hanzi": "麻烦", "pinyin": "máfan", "meaning": "làm phiền, phiền phức"},
    {"hanzi": "好像", "pinyin": "hǎoxiàng", "meaning": "hình như, dường như"}
]

# --- DỮ LIỆU CÂU HỎI TRẮC NGHIỆM (33 Câu: 15 Cũ + 18 Mới) ---
# Format: (Câu hỏi, Đáp án đúng, [3 đáp án nhiễu có độ khó cao])
raw_quiz_data = [
    # Nhóm 重新
    ("这张画没画好，我要_____画。", "重新", ["专门", "平时", "差不多"]),
    ("这个计划有些问题，经理要求大家_____考虑一下。", "重新", ["专门", "真正", "好像"]), 
    
    # Nhóm 尽管
    ("_____外面的雨下得很大，他还是坚持去跑步了。", "尽管", ["好像", "平时", "正好"]),
    ("你以后有什么困难_____跟我们说，大家都会帮你的。", "尽管", ["专门", "重新", "差不多"]),
    
    # Nhóm 真正
    ("一个人除了钱什么都没有，那不是_____的幸福。", "真正", ["专门", "正好", "重新"]),
    ("只有经历过困难，才能体会到什么叫_____的朋友。", "真正", ["平时", "差不多", "好像"]),
    
    # Nhóm 友谊
    ("让我们为了两国人民的_____干杯！", "友谊", ["聚会", "联系", "短信"]),
    ("时间和距离都不能改变我们之间的_____。", "友谊", ["聚会", "短信", "麻烦"]),
    
    # Nhóm 适应
    ("我们要改变自己，努力去_____新的环境。", "适应", ["联系", "麻烦", "毕业"]),
    ("刚到国外留学时，他在饮食和气候上都很难_____。", "适应", ["麻烦", "联系", "交"]),
    
    # Nhóm 交
    ("我很高兴自己能_____到一个喜欢学汉语的朋友。", "交", ["逛", "联系", "麻烦"]),
    ("他性格很开朗，在大学里_____了许多新朋友。", "交", ["联系", "聚会", "适应"]),
    
    # Nhóm 平时
    ("你注意到没有？小明今天和_____不太一样。", "平时", ["差不多", "正好", "好像"]),
    ("他_____不怎么爱说话，可是今天却说了很多。", "平时", ["差不多", "专门", "重新"]),
    
    # Nhóm 逛
    ("昨天我跟朋友_____街逛到晚上10点多才回家。", "逛", ["交", "聚会", "联系"]),
    ("周末我不想待在家里，我们去商场_____吧。", "逛", ["聚会", "联系", "交"]),
    
    # Nhóm 短信
    ("麻烦你发一条_____，告诉我见面的时间和地点。", "短信", ["联系", "友谊", "聚会"]),
    ("上课的时候不能接电话，有急事你可以给我发_____。", "短信", ["联系", "聚会", "友谊"]),
    
    # Nhóm 正好
    ("我下午也要去踢足球，_____一起去吧。", "正好", ["专门", "重新", "差不多"]),
    ("这件衣服不大不小，你穿_____。", "正好", ["差不多", "真正", "平时"]),
    
    # Nhóm 聚会
    ("跟老朋友_____，吃吃饭、聊聊天儿，多高兴啊！", "聚会", ["联系", "友谊", "适应"]),
    ("大家都忙于工作，连春节的家庭_____都没时间参加。", "聚会", ["联系", "友谊", "逛"]),
    
    # Nhóm 联系
    ("电子邮件是我和老师最常用的_____方式。", "联系", ["聚会", "友谊", "交"]),
    ("换了新手机号码后，记得及时跟所有的客户_____。", "联系", ["交", "适应", "聚会"]),
    
    # Nhóm 差不多
    ("昨天晚上我_____一夜没有睡。", "差不多", ["平时", "重新", "好像"]),
    ("这两支笔的颜色看起来_____，很难分清楚。", "差不多", ["好像", "正好", "平时"]),
    
    # Nhóm 专门
    ("这一年我打算_____学电脑，别的什么事都不做。", "专门", ["重新", "平时", "真正"]),
    ("为了欢迎你回国，我_____做了一桌你最爱吃的菜。", "专门", ["正好", "重新", "差不多"]),
    
    # Nhóm 毕业
    ("他儿子才17岁，已经高中_____了。", "毕业", ["联系", "适应", "麻烦"]),
    ("大学_____以后，他决定留在北京发展。", "毕业", ["联系", "聚会", "适应"]),
    
    # Nhóm 麻烦
    ("我找不到我的手机了，能不能_____你们帮我找一下。", "麻烦", ["联系", "交", "适应"]),
    ("这件事处理起来太_____了，我们需要更多的时间。", "麻烦", ["适应", "联系", "毕业"]),
    
    # Nhóm 好像
    ("他_____从来都不会累，总是一副很有精神的样子。", "好像", ["差不多", "平时", "尽管"]),
    ("天阴了，看样子_____要下大雨，出门记得带伞。", "好像", ["差不多", "尽管", "重新"])
]

# --- QUẢN LÝ TRẠNG THÁI (SESSION STATE) ---
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0

def init_quiz():
    """Khởi tạo hoặc làm mới bài Quiz"""
    questions = []
    
    for q_text, correct, distractors in raw_quiz_data:
        options = [correct] + distractors
        random.shuffle(options) # Đảo vị trí các đáp án A B C D
        
        questions.append({
            "question": q_text,
            "answer": correct,
            "options": options
        })
    
    # Xáo trộn thứ tự 33 câu hỏi
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
st.info("Bài tập gồm 33 câu. Hãy vận dụng ngữ cảnh để chọn từ chính xác nhất điền vào chỗ trống.")

score = 0
total_questions = len(st.session_state.quiz_questions)

# Tạo form để nộp bài
with st.form(key='quiz_form'):
    for i, q in enumerate(st.session_state.quiz_questions):
        st.markdown(f"**Câu {i+1}:** {q['question']}")
        
        # Streamlit radio để chọn đáp án
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
    elif score >= 25:
        st.info("Rất tốt! Bạn nắm vững cách dùng từ và ngữ cảnh. 👍")
    elif score >= 16:
        st.warning("Khá ổn, nhưng hãy cẩn thận với các từ loại giống nhau nhé! 💪")
    else:
        st.error("Kết quả chưa tốt lắm, bạn hãy lật lại Flashcard để đọc kỹ ví dụ nhé! 📖")
        
    st.button("🔄 Làm lại bài (Đảo câu hỏi & Đáp án)", on_click=init_quiz, type="primary")
