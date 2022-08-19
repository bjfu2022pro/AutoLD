function quxiao() {
    jQuery("#quxiao_btn").click(function () {
            jQuery.ajax({
                url: "/quxiao",
                method: "POST",
                data: {
                    a: 123
                },
                success: function (res) {
                    var cod = res['cod'];
                    if (cod == 800) {
                        window.location.replace("algorithmic_mall");
                        alert("订单已取消！");

                    }

                }
            })
        }
    )
}

jQuery(function () {
    quxiao();
});