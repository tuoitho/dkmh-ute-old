    
Hướng dẫn lấy token: sau khi đăng nhập trang dkmh thành công thì dán vào thanh địa chỉ đoạn sau:

javascript: JSON.parse(Object.keys(localStorage).reduce(function(obj, str) { obj[str] = localStorage.getItem(str); return obj }, {}).authorizationData).Token 

(lưu ý khi dán thì sẽ bị mất chữ javascript: nên phải gõ lại bằng tay). Ấn Enter