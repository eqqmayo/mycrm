async function displayUserDetail(userId) {
    displayPage('user-detail-page');
    
    const data = await loadAllUserData(userId);
    renderAllUserTables(data);
}

async function loadAllUserData(userId) {
    const [userResponse, orderResponse, storeResponse, itemResponse] = await Promise.all([
        fetch(`/api/users/user/${userId}`),
        fetch(`/api/users/orders/${userId}`),
        fetch(`/api/users/goto-stores/${userId}`),
        fetch(`/api/users/goto-items/${userId}`)
    ]);
    
    const [userData, orderData, storeData, itemData] = await Promise.all([
        userResponse.json(),
        orderResponse.json(),
        storeResponse.json(),
        itemResponse.json()
    ]);

    return { userData, orderData, storeData, itemData };
}

function renderAllUserTables(data) {
    const { userData, orderData, storeData, itemData } = data;
        
    const userTable = new Table({
        keys: ['Name', 'Gender', 'Age', 'Birthdate', 'Address'],
        items: userData
    });
    
    const orderTable = new Table({
        keys: ['OrderId', 'OrderAt', 'StoreId'],
        items: orderData
    }, {
        linkColumn: ['OrderId', 'StoreId'],
        baseUrl: ['/orderitems/detail', '/stores/detail']
    });
    
    const storeTable = new Table({
        keys: ['Store', 'Count'],
        items: storeData
    });
    
    const itemTable = new Table({
        keys: ['Item', 'Count'],
        items: itemData
    });
    
    document.querySelector('.user-info-content').innerHTML = userTable.render();
    document.querySelector('.user-orders-content').innerHTML = orderTable.render();
    document.querySelector('.user-stores-content').innerHTML = storeTable.render();
    document.querySelector('.user-items-content').innerHTML = itemTable.render();
}

