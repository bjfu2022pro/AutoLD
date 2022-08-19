function beginBtn4() {
    $("#begin21").on("click", function (event) {
        var id = $("td[id='dingdanId21']").text();
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

    $("#begin22").on("click", function (event) {
        var id = $("td[id='dingdanId22']").text();
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

    $("#begin23").on("click", function (event) {
        var id = $("td[id='dingdanId23']").text();
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

    $("#begin24").on("click", function (event) {
        var id = $("td[id='dingdanId24']").text();
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

    $("#begin25").on("click", function (event) {
        var id = $("td[id='dingdanId25']").text();
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
    beginBtn4();
});