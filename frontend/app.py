import streamlit as st
from api_client import APIClient

client = APIClient()

st.set_page_config(page_title="Pro Notes", page_icon="📓")

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user is None:
    st.title("🔐 Đăng nhập")
    tab_in, tab_up = st.tabs(["Đăng nhập", "Đăng ký"])
    
    with tab_in:
        e = st.text_input("Email")
        p = st.text_input("Mật khẩu", type="password")
        if st.button("Vào hệ thống"):
            res = client.auth_request(e, p)
            if "localId" in res:
                st.session_state.user = res
                st.rerun()
            else: st.error("Thất bại!")
            
    with tab_up:
        re = st.text_input("Email mới")
        rp = st.text_input("Mật khẩu mới", type="password")
        if st.button("Tạo tài khoản"):
            res = client.auth_request(re, rp, mode="signUp")
            if "localId" in res: st.success("Xong! Hãy đăng nhập.")
            else: st.error("Lỗi đăng ký.")

else:
    st.sidebar.write(f"Chào: {st.session_state.user['email']}")
    if st.sidebar.button("Thoát"):
        st.session_state.user = None
        st.rerun()

    st.title("📓 Ghi chú cá nhân")
    
    with st.form("add_note"):
        text = st.text_area("Nội dung ghi chú...")
        if st.form_submit_button("Lưu lại") and text:
            client.save_note(st.session_state.user['localId'], text)
            st.toast("Đã lưu!")

    st.subheader("Lịch sử")
    notes_res = client.fetch_notes(st.session_state.user['localId'])
    if notes_res.status_code == 200:
        for n in notes_res.json():
            with st.expander(f"Ngày: {n['created_at'][:16]}"):
                st.write(n['content'])