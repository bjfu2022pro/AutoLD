function beginBtn3() {
    $("#begin16").on("click", function (event) {
        var id = $("td[id='dingdanId16']").text();
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

    $("#begin17").on("click", function (event) {
        var id = $("td[id='dingdanId17']").text();
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

    $("#begin18").on("click", function (event) {
        var id = $("td[id='dingdanId18']").text();
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

    $("#begin19").on("click", function (event) {
        var id = $("td[id='dingdanId19']").text();
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

    $("#begin20").on("click", function (event) {
        var id = $("td[id='dingdanId20']").text();
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
    beginBtn3();
});