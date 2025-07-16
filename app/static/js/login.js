// 로그인 폼 관리 클래스
class LoginForm {
    constructor() {
        this.form = document.querySelector('.login-form');
        this.submitBtn = document.querySelector('.btn-login');
        this.usernameInput = document.getElementById('username');
        this.passwordInput = document.getElementById('password');
        this.usernameError = document.getElementById('username-error');
        this.passwordError = document.getElementById('password-error');
        
        this.init();
    }
    
    init() {
        // 이벤트 리스너 등록
        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.usernameInput.addEventListener('input', () => this.clearError('username'));
        this.passwordInput.addEventListener('input', () => this.clearError('password'));
        this.usernameInput.addEventListener('blur', () => this.validateUsername());
        this.passwordInput.addEventListener('blur', () => this.validatePassword());
        
        // 비밀번호 표시/숨김 기능 (선택사항)
        this.addPasswordToggle();
    }
    
    // 폼 제출 처리
    async handleSubmit(e) {
        e.preventDefault();
        
        // 유효성 검사
        if (!this.validateForm()) {
            return;
        }
        
        // 로딩 상태 시작
        this.setLoading(true);
        
        try {
            const formData = new FormData(this.form);
            const response = await fetch(this.form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            });
            
            const result = await response.json();
            
            if (response.ok) {
                // 성공 시 리다이렉트
                this.showSuccess('로그인 성공!');
                setTimeout(() => {
                    window.location.href = result.redirect_url || '/admin/dashboard';
                }, 1000);
            } else {
                // 에러 처리
                this.handleServerErrors(result.errors);
            }
            
        } catch (error) {
            console.error('Login error:', error);
            this.showGlobalError('네트워크 오류가 발생했습니다. 다시 시도해주세요.');
        } finally {
            this.setLoading(false);
        }
    }
    
    // 클라이언트 유효성 검사
    validateForm() {
        let isValid = true;
        
        if (!this.validateUsername()) {
            isValid = false;
        }
        
        if (!this.validatePassword()) {
            isValid = false;
        }
        
        return isValid;
    }
    
    validateUsername() {
        const value = this.usernameInput.value.trim();
        
        if (!value) {
            this.showError('username', '사용자명 또는 이메일을 입력해주세요.');
            return false;
        }
        
        // 이메일 형식 또는 사용자명 검사
        if (value.includes('@')) {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(value)) {
                this.showError('username', '올바른 이메일 형식을 입력해주세요.');
                return false;
            }
        } else {
            if (value.length < 3) {
                this.showError('username', '사용자명은 최소 3자 이상이어야 합니다.');
                return false;
            }
        }
        
        this.clearError('username');
        return true;
    }
    
    validatePassword() {
        const value = this.passwordInput.value;
        
        if (!value) {
            this.showError('password', '비밀번호를 입력해주세요.');
            return false;
        }
        
        if (value.length < 6) {
            this.showError('password', '비밀번호는 최소 6자 이상이어야 합니다.');
            return false;
        }
        
        this.clearError('password');
        return true;
    }
    
    // 에러 메시지 표시
    showError(field, message) {
        const errorElement = field === 'username' ? this.usernameError : this.passwordError;
        const inputElement = field === 'username' ? this.usernameInput : this.passwordInput;
        
        errorElement.textContent = message;
        inputElement.classList.add('error');
        
        // 접근성: 스크린 리더에게 알림
        errorElement.setAttribute('aria-live', 'polite');
    }
    
    // 에러 메시지 제거
    clearError(field) {
        const errorElement = field === 'username' ? this.usernameError : this.passwordError;
        const inputElement = field === 'username' ? this.usernameInput : this.passwordInput;
        
        errorElement.textContent = '';
        inputElement.classList.remove('error');
    }
    
    // 서버 에러 처리
    handleServerErrors(errors) {
        if (errors.username) {
            this.showError('username', errors.username);
        }
        if (errors.password) {
            this.showError('password', errors.password);
        }
        if (errors.general) {
            this.showGlobalError(errors.general);
        }
    }
    
    // 전역 에러 메시지
    showGlobalError(message) {
        // 기존 알림 제거
        const existingAlert = document.querySelector('.alert-error');
        if (existingAlert) {
            existingAlert.remove();
        }
        
        // 새 알림 생성
        const alert = document.createElement('div');
        alert.className = 'alert alert-error';
        alert.innerHTML = `
            <span class="alert-message">${message}</span>
            <button class="alert-close" onclick="this.parentElement.remove()">✕</button>
        `;
        
        this.form.insertBefore(alert, this.form.firstChild);
        
        // 자동 제거 (5초 후)
        setTimeout(() => {
            if (alert.parentNode) {
                alert.remove();
            }
        }, 5000);
    }
    
    // 성공 메시지
    showSuccess(message) {
        const alert = document.createElement('div');
        alert.className = 'alert alert-success';
        alert.innerHTML = `
            <span class="alert-message">${message}</span>
        `;
        
        this.form.insertBefore(alert, this.form.firstChild);
    }
    
    // 로딩 상태 관리
    setLoading(isLoading) {
        if (isLoading) {
            this.submitBtn.classList.add('loading');
            this.submitBtn.disabled = true;
            this.usernameInput.disabled = true;
            this.passwordInput.disabled = true;
        } else {
            this.submitBtn.classList.remove('loading');
            this.submitBtn.disabled = false;
            this.usernameInput.disabled = false;
            this.passwordInput.disabled = false;
        }
    }
    
    // 비밀번호 표시/숨김 토글 추가
    addPasswordToggle() {
        const toggleBtn = document.createElement('button');
        toggleBtn.type = 'button';
        toggleBtn.className = 'password-toggle';
        toggleBtn.innerHTML = '👁️';
        toggleBtn.setAttribute('aria-label', '비밀번호 표시/숨김');
        
        const passwordGroup = this.passwordInput.parentNode;
        passwordGroup.style.position = 'relative';
        passwordGroup.appendChild(toggleBtn);
        
        toggleBtn.addEventListener('click', () => {
            const isPassword = this.passwordInput.type === 'password';
            this.passwordInput.type = isPassword ? 'text' : 'password';
            toggleBtn.innerHTML = isPassword ? '🙈' : '👁️';
            toggleBtn.setAttribute('aria-label', 
                isPassword ? '비밀번호 숨김' : '비밀번호 표시'
            );
        });
    }
}

// DOM 로드 후 초기화
document.addEventListener('DOMContentLoaded', () => {
    new LoginForm();
});

// 키보드 접근성
document.addEventListener('keydown', (e) => {
    // Enter 키로 폼 제출
    if (e.key === 'Enter' && e.target.matches('.form-input')) {
        const form = e.target.closest('form');
        if (form) {
            e.preventDefault();
            form.dispatchEvent(new Event('submit', { bubbles: true }));
        }
    }
});

// 페이지 가시성 변경 시 폼 초기화 (보안)
document.addEventListener('visibilitychange', () => {
    if (document.hidden) {
        // 페이지가 숨겨질 때 민감한 정보 초기화
        const passwordInput = document.getElementById('password');
        if (passwordInput && !passwordInput.value) {
            // 비밀번호가 비어있으면 사용자명도 초기화
            const usernameInput = document.getElementById('username');
            if (usernameInput) {
                usernameInput.value = '';
            }
        }
    }
});

// 자동 로그아웃 방지를 위한 활동 감지
let lastActivity = Date.now();
const ACTIVITY_TIMEOUT = 30 * 60 * 1000; // 30분

['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'].forEach(event => {
    document.addEventListener(event, () => {
        lastActivity = Date.now();
    }, true);
});

// 비활성 상태 체크
setInterval(() => {
    if (Date.now() - lastActivity > ACTIVITY_TIMEOUT) {
        console.log('User inactive - consider auto-logout');
        // 필요시 자동 로그아웃 로직 추가
    }
}, 60000); // 1분마다 체크 