function getCurrentPage() {
    const path = window.location.pathname;
    
    if (path.includes('/users/detail/')) {
        const userId = path.split('/users/detail/')[1];
        return {
            type: 'userDetail',
            userId: userId
        };
    }

    return { type: 'user' };
}

function navigateTo(url) {
    history.pushState({}, '', url);
    renderCurrentPage();
    window.scrollTo(0, 0);
}

async function renderCurrentPage() {
    const currentPage = getCurrentPage();
    
    if (currentPage.type === 'user') {
        await displayUser();
    } else {
        await displayUserDetail(currentPage.userId);
    }
}

function displayPage(pageId) {
    document.getElementById('user-page').style.display = 'none';
    document.getElementById('user-detail-page').style.display = 'none';
    document.getElementById(pageId).style.display = 'block';
}

window.addEventListener('popstate', renderCurrentPage);