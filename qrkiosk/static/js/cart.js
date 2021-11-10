var updateBtns = document.getElementsByClassName('update-cart')

for(var i =0; i < updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        var table = this.dataset.table
        console.log('productId:', productId, 'action:', action,'table:',table)
        console.log('product:', this.dataset)
        updateUserOrder(productId, action,table)
        
    })
}

function updateUserOrder(productId, action,table){
    console.log("csrftoken:",csrftoken)
    var url = '/update_item/'
    
    console.log('table:', table)
    fetch(url, {
        method:'POST', headers:{
            'Content-Type':'application/json',
            // 'Accept': 'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action':action, 'table':table})
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        location.reload()
    });
}