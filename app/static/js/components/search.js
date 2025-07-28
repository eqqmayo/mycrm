function renderSearch() {
    return `
        <form class='search' onsubmit="search(event)">
            <input id="name" type="text" name="name" placeholder="Enter name ...">
            <select id="gender" name="gender" onchange="search(event)">
                <option value=''>All</option>
                <option value='Female'>Female</option>
                <option value='Male'>Male</option>
            </select>
        </form>
    `;
}