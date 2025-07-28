class Table {
    constructor(
        data = {keys: [], items: []}, 
        options = {linkColumn: [], baseUrl: []}
    ) {
        this.data = data;
        this.options = options;
    }

    render() {
        return `
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
                                
                                if (url.includes('/users')) {
                                    return `<td><a href="#" onclick="navigateTo('${url}/${item[key]}'); return false;">
                                            ${item[key]}</a></td>`;
                                } else {
                                    return `<td><a href="${url}/${item[key]}">
                                            ${item[key]}</a></td>`;
                                }
                            }
                            return `<td>${item[key]}</td>`;
                        }).join('')}
                    </tr>
                `).join('')}
            </table>
        `;
    }
}