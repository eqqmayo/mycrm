function getCurrentPage() {
    const route = window.AppData.route;
    return { type: route.type, param: route.param };
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
        await displayUserDetail(currentPage.param);
    }
}

function displayPage(pageId) {
    document.getElementById('user-page').style.display = 'none';
    document.getElementById('user-detail-page').style.display = 'none';
    document.getElementById(pageId).style.display = 'block';
}

window.addEventListener('popstate', renderCurrentPage);