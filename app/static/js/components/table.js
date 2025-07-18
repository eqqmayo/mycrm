class Table {
    constructor(title, data, options = {linkColumn: []}) {
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
                            if (this.options.linkColumn && this.options.linkColumn.includes(key)) {
                                const index = this.options.linkColumn.indexOf(key);
                                const url = this.options.baseUrl[index];
                                return `<td><a href="${url}/${item[key]}">
                                        ${item[key]}</a></td>`;
                            }
                            return `<td>${item[key]}</td>`;
                        }).join('')}
                    </tr>
                `).join('')}
            </table>
        `;
    }
}
