import requests

# Thông tin cần thiết
access_token = 'EAARgrIZCppJABOzabdllZB2s0kwhNJCmvDa5FDuaCWosZAdtDvDLdgj5QaxfOLcjKzHXPNmOisrIPS9u01w6SgYDWeX9Bkg3DbEeUFkbbRZBpiwZCkynyO8ZChVcWyOj4fwONY5UseeyPDwATpW4y8N613ZAOBlNZANWBDnOu8cuhACNX3Has8DSHukG3DZB4zcNRmMMfc59ZBkJZCnNTZB23TaLyXcL'
page_id = '561778363696859'
message = 'Đây là bài viết được đăng tự động bằng Python!'

# Gửi yêu cầu POST đến Graph API
url = f'https://graph.facebook.com/{page_id}/feed'
payload = {
    'message': message,
    'access_token': access_token
}

response = requests.post(url, data=payload)

# Kiểm tra kết quả
if response.status_code == 200:
    print('✅ Đăng bài thành công!')
    print('Post ID:', response.json().get('id'))
else:
    print('❌ Đăng bài thất bại.')
    print('Lỗi:', response.text)
