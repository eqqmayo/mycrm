class Pagination {
    constructor(start, end, currentPage, lastPage) {
        this.start = start;
        this.end = end;
        this.currentPage = currentPage;
        this.lastPage = lastPage;
    }
    
    render() {
        let pagination = '<ul class="pagination">';
        
        if (this.currentPage != 1) {
            pagination += `<li><a href="#" onclick="changePage(${this.currentPage - 1}, event)">&lt; Prev</a></li>`;
        }
        
        for (let page = this.start; page <= this.end; page++) {
            const activeClass = page === this.currentPage ? 'inactive' : '';
            pagination += `<li><a href="#" onclick="changePage(${page}, event)" class="${activeClass}">${page}</a></li>`;
        }
        
        if (this.currentPage != this.lastPage) {
            pagination += `<li><a href="#" onclick="changePage(${this.currentPage + 1}, event)">Next &gt;</a></li>`;
        }
        
        pagination += '</ul>';
        return pagination;
    }
}