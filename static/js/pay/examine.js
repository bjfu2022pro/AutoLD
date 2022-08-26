function examine(){
    jQuery("#examine_btn").click(function () {
     jQuery.ajax({
                url: "/examine",
                method: "POST",
                data: {
                     "danhao":$('#examine_btn').attr('value')
                },
                success: function (res) {
                    var cod = res['od'];
                    if (cod == 400) {
                        alert("等待管理员处理")
                        location.reload()
                    }

                }
            })
        }
    )
}

jQuery(function () {
    examine();
});