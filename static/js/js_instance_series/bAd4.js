function beginBtn2() {
    $("#begin11").on("click", function (event) {
        var id = $("td[id='dingdanId11']").text();
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

    $("#begin12").on("click", function (event) {
        var id = $("td[id='dingdanId12']").text();
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

    $("#begin13").on("click", function (event) {
        var id = $("td[id='dingdanId13']").text();
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

    $("#begin14").on("click", function (event) {
        var id = $("td[id='dingdanId14']").text();
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

    $("#begin15").on("click", function (event) {
        var id = $("td[id='dingdanId15']").text();
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
    beginBtn2();
});