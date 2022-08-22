function upBtn() {
    $("#up1").on("click", function (event) {
        $.ajax({
            url: "/algorithm_up",
            method: "post",
            data: {
                "id": $('#up1').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已上架");
                } else if(code == 400){
                    alert("该算法已上架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#up2").on("click", function (event) {
        $.ajax({
            url: "/algorithm_up",
            method: "post",
            data: {
                "id": $('#up2').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已上架");
                } else if(code == 400){
                    alert("该算法已上架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#up3").on("click", function (event) {
        $.ajax({
            url: "/algorithm_up",
            method: "post",
            data: {
                "id": $('#up3').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已上架");
                } else if(code == 400){
                    alert("该算法已上架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#up4").on("click", function (event) {
        $.ajax({
            url: "/algorithm_up",
            method: "post",
            data: {
                "id": $('#up4').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已上架");
                } else if(code == 400){
                    alert("该算法已上架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#up5").on("click", function (event) {
        $.ajax({
            url: "/algorithm_up",
            method: "post",
            data: {
                "id": $('#up5').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已上架");
                } else if(code == 400){
                    alert("该算法已上架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    })
}

function downBtn() {
    $("#down1").on("click", function (event) {
        $.ajax({
            url: "/algorithm_down",
            method: "post",
            data: {
                "id": $('#down1').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已下架");
                } else if(code == 400){
                    alert("该算法已下架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#down2").on("click", function (event) {
        $.ajax({
            url: "/algorithm_down",
            method: "post",
            data: {
                "id": $('#down2').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已下架");
                } else if(code == 400){
                    alert("该算法已下架！");
                }下
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#down3").on("click", function (event) {
        $.ajax({
            url: "/algorithm_down",
            method: "post",
            data: {
                "id": $('#down3').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已下架");
                } else if(code == 400){
                    alert("该算法已下架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#down4").on("click", function (event) {
        $.ajax({
            url: "/algorithm_down",
            method: "post",
            data: {
                "id": $('#down4').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已下架");
                } else if(code == 400){
                    alert("该算法已下架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    });

    $("#down5").on("click", function (event) {
        $.ajax({
            url: "/algorithm_down",
            method: "post",
            data: {
                "id": $('#down5').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("已下架");
                } else if(code == 400){
                    alert("该算法已下架！");
                }
                window.location.href = '/admin_algor'
            }
        })
    })
}


$(function(){
    upBtn();
    downBtn();
});