function renderSearch() {
        return `
            <form class='search'>
                <input type="text" name="name" placeholder="Enter name ...">
                <select name="gender">
                    <option value=''>All</option>
                    <option value='female'>Female</option>
                    <option value='male'>Male</option>
                </select>
            </form>
        `;
    }

