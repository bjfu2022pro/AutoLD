function expot() {
    $("#daochu_btn").click(function () {
            $.ajax({
                url: "/expt",
                method: "POST",
                data: {
                    "in": 123
                },
                success: function (res) {
                    var od = res['od'];
                    if (od == 400) {
                        var lujing = res['lujing'];
                        location.href = lujing;
                    }

                }
            })
        }
    )
}

$(function () {
    expot();
});