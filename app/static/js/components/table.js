class Table {
    constructor(title, data, options = {}) {
        this.title = title;
        this.data = data;
        this.options = options;
    }

    render() {
        return `
            <p>&nbsp;${this.title}</p>
            <table>
                <tr>
                    ${this.data.keys.map(key => 
                        `<th>${key}</th>`
                    ).join('')}
                </tr>
                ${this.data.items.map(item => `
                    <tr>
                        ${this.data.keys.map(key => {
                            if (this.options.linkColumn === key) {
                                return `<td><a href="${this.options.baseUrl}/${item[key]}">${item[key]}</a></td>`;
                            }
                            return `<td>${item[key]}</td>`;
                        }).join('')}
                    </tr>
                `).join('')}
            </table>
        `;
    }
}

// 사용 예시:
const table = new Table('Monthly Revenue', monthRev, {
    linkColumn: 'Month',
    baseUrl: '/stores/detail'
});
document.querySelector('#tableContainer').innerHTML = table.render();
