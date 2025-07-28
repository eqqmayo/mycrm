async function displayUser() {
    displayPage('user-page');
  
    document.querySelector('.search-container').innerHTML = renderSearch();
    setSearchFormValues();
        
    const apiUrl = getUserApiUrl();
    const response = await fetch(apiUrl);
    const data = await response.json();
        
    const table = new Table({
        keys: ['Id', 'Name', 'Gender', 'Age', 'Birthdate'],
        items: data.users
    }, {
        linkColumn: ['Id'],
        baseUrl: ['/users/detail']
    });
        
    document.querySelector('.user-table-container').innerHTML = table.render();
        
    const pagination = new Pagination(
        data.pagination.start,
        data.pagination.end,
        data.pagination.current_page,
        data.pagination.last_page
    );
    document.querySelector('.pagination-container').innerHTML = pagination.render();
}

function setSearchFormValues() {
    const params = new URLSearchParams(window.location.search);
    
    const nameInput = document.getElementById('name');
    if (nameInput && params.get('name')) {
        nameInput.value = params.get('name');
    }
    
    const genderSelect = document.getElementById('gender');
    if (genderSelect && params.get('gender')) {
        genderSelect.value = params.get('gender');
    }
}

function getUserApiUrl() {
    let apiUrl = '/api/users';
    const path = window.location.pathname;
    const search = window.location.search;
    
    if (path.startsWith('/users/')) {
        const page = path.split('/users/')[1];
        if (!isNaN(page)) { apiUrl += `/${page}`; }
    }

    if (search) { apiUrl += search; }
    return apiUrl;
}

function changePage(page, event) {
    event.preventDefault();
    const params = window.location.search;
    navigateTo(`/users/${page}${params}`);
}

function search(event) {
    event.preventDefault();
    const form = event.target.tagName === 'SELECT' ? event.target.form : event.target;
    const formData = new FormData(form);
    const params = new URLSearchParams(formData);
    navigateTo(`/users?${params.toString()}`);
}