function zhifu() {
    jQuery("#zhifu_btn").click(function () {
        jQuery.ajax({
            url: "/zhifu",
            method: "POST",
            data: {
                a: 123
            },
            success: function (res) {
                var cod = res['cod'];
                if (cod == 200) {
                    alert("支付成功！")
                    window.location.href = "/my_instance"
                } else if (cod == 400) {
                    alert("余额不足，前往充值界面")
                    window.location.href = "/recharge"
                }

            

        }
    })
}

)
}

jQuery(function () {
    zhifu();
});