class Pagination {
    constructor(start, end, current_page, last_page, baseUrl = '/users', onPageChange = null) {
        this.start = start;
        this.end = end;
        this.current_page = current_page;
        this.last_page = last_page;
        this.baseUrl = baseUrl;
        this.onPageChange = onPageChange;
    }

    render() {
        let pagination = '<ul class="pagination">';
        
        if (this.current_page != 1) {
            pagination += `<li><a href="#" onclick="changePage(${this.current_page - 1}); return false;">&lt; Prev</a></li>`;
        }
        
        for (let page = this.start; page <= this.end; page++) {
            const activeClass = page === this.current_page ? 'inactive' : '';
            pagination += `<li><a href="#" onclick="changePage(${page}); return false;" class="${activeClass}">${page}</a></li>`;
        }
        
        if (this.current_page != this.last_page) {
            pagination += `<li><a href="#" onclick="changePage(${this.current_page + 1}); return false;">Next &gt;</a></li>`;
        }
        
        pagination += '</ul>';
        return pagination;
    }

}

function changePage(page) {
    history.pushState({}, '', `/users/${page}`);
    window.scrollTo(0,0);
    fetchUsers();
}
