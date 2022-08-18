function canl(){
    jQuery("#cancel_btn").click(function () {
     jQuery.ajax({
                url: "/canl",
                method: "POST",
                data: {
                     "danhao":$('#cancel_btn').attr('value')
                },
                success: function (res) {
                    var cod = res['cod'];
                    if (cod == 400) {
                        alert("订单已取消！")
                        location.reload()
                    }

                }
            })
        }
    )
}

jQuery(function () {
    canl();
});