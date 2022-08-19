function beginBtn1() {
    $("#begin6").on("click", function (event) {
        var id = $("td[id='dingdanId6']").text();
        $.ajax({
            url: "/run_instance",
            method: "post",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("开始运行...");
                }else if (code == 300) {
                    alert("正在运行中！");
                }else if(code == 400) {
                    alert("已运行结束！");
                }else if(code == 500) {
                    alert("该订单已退款！");
                }
                window.location.href = '/my_instance'
            }
        })
    });

    $("#begin7").on("click", function (event) {
        var id = $("td[id='dingdanId7']").text();
        $.ajax({
            url: "/run_instance",
            method: "post",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("开始运行...");
                }else if (code == 300) {
                    alert("正在运行中！");
                }else if(code == 400) {
                    alert("已运行结束！");
                }else if(code == 500) {
                    alert("该订单已退款！");
                }
                window.location.href = '/my_instance'
            }
        })
    });

    $("#begin8").on("click", function (event) {
        var id = $("td[id='dingdanId8']").text();
        $.ajax({
            url: "/run_instance",
            method: "post",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("开始运行...");
                }else if (code == 300) {
                    alert("正在运行中！");
                }else if(code == 400) {
                    alert("已运行结束！");
                }else if(code == 500) {
                    alert("该订单已退款！");
                }
                window.location.href = '/my_instance'
            }
        })
    });

    $("#begin9").on("click", function (event) {
        var id = $("td[id='dingdanId9']").text();
        $.ajax({
            url: "/run_instance",
            method: "post",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("开始运行...");
                }else if (code == 300) {
                    alert("正在运行中！");
                }else if(code == 400) {
                    alert("已运行结束！");
                }else if(code == 500) {
                    alert("该订单已退款！");
                }
                window.location.href = '/my_instance'
            }
        })
    });

    $("#begin10").on("click", function (event) {
        var id = $("td[id='dingdanId10']").text();
        $.ajax({
            url: "/run_instance",
            method: "post",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("开始运行...");
                }else if (code == 300) {
                    alert("正在运行中！");
                }else if(code == 400) {
                    alert("已运行结束！");
                }else if(code == 500) {
                    alert("该订单已退款！");
                }
                window.location.href = '/my_instance'
            }
        })
    })

}

$(function(){
    beginBtn1();
});