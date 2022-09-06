function payWithPaystack(){
    const proxyurl = "https://scholarxx.herokuapp.com";
    const url = "/payment/create";
    var user = "{{ user.id }}";
    var email = "{{ user.email }}";
    var amt = +document.getElementById("amount").value * 100;
    var handler = PaystackPop.setup({
      key: 'pk_test_3e832f6afe8035be0b2e66762af681ada8b5a847',
      email: email,
      amount: amt,
      currency: "NGN",
      ref: ''+Math.floor((Math.random() * 1000000000) + 1), // generates a pseudo-unique reference. Please replace with a reference you generated. Or remove the line entirely so our API will generate one for you
      metadata: {
         custom_fields: [
            {
                display_name: "Mobile Number",
                variable_name: "mobile_number",
                value: "+2348012345678"
            }
         ]
      },
      callback: function(response){
        data = {
          ref_id : response.reference,
          amount : amt,
          user: user,
          email: email
          
        }
        console.log("---", data)
        // var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance 
        // var theUrl = proxyurl + url;
        // xmlhttp.open("POST", theUrl);
        // xmlhttp.setRequestHeader("Content-Type", "application/json; charset=UTF-8");
        // xmlhttp.send(JSON.stringify(data))
        console.log("---", JSON.stringify(data))
        
        fetch(proxyurl + url, 
        {
          method: 'POST',
          body: JSON.stringify(data),
          mode: 'cors',
          headers:{
            'Content-Type': 'application/x-www-form-urlencoded'
            }
        }

      ).then(res => console.log("-----", JSON.stringify(data)))
      .then(response => console.log('Success:', JSON.stringify(data)))
      .catch(error => console.error('Error:', error));
        alert('success. transaction ref is ' + response.reference);
      
       }, onClose: function(){
          alert('window closed');
      }
    });
    handler.openIframe();
  }