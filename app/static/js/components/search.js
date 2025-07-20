function renderSearch() {
    return `
        <form class='search' onsubmit="handleSubmit(event)">
            <input type="text" name="name" placeholder="Enter name ...">
            <select name="gender" onchange="handleSubmit(event)">
                <option value=''>All</option>
                <option value='Female'>Female</option>
                <option value='Male'>Male</option>
            </select>
        </form>
    `;
}

function handleSubmit(event) {
    event.preventDefault(); 
    
    const form = event.target.tagName === 'SELECT' ? event.target.form : event.target;
    
    const formData = new FormData(form);
    const params = new URLSearchParams(formData);
    
    history.pushState({}, '', `/users?${params.toString()}`);
    window.scrollTo(0,0);
    fetchUsers();
}
