function beginBtn() {
    $("#begin1").on("click", function (event) {
        var id = $("td[id='dingdanId1']").text();
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

    $("#begin2").on("click", function (event) {
        var id = $("td[id='dingdanId2']").text();
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

    $("#begin3").on("click", function (event) {
        var id = $("td[id='dingdanId3']").text();
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

    $("#begin4").on("click", function (event) {
        var id = $("td[id='dingdanId4']").text();
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

    $("#begin5").on("click", function (event) {
        var id = $("td[id='dingdanId5']").text();
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
    beginBtn();
});