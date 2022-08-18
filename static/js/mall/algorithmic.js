function findmore() {
    $("#more1").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more1').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })
    $("#more2").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more2').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })
    $("#more3").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more3').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })
    $("#more4").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more4').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })
    $("#more5").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more5').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })
    $("#more6").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more6').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_details";
                }
            }
        })
    })

}


function select() {
    $("#btn1").on("click", function (event) {
        // var title = document.getElementById("title1").value;
        // var introduce = document.getElementById("introduce1").value;
        $.ajax({
            url: "/cache2",
            method: "POST",
            data: {
                "sort": 1,
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_mall";
                }
            }
        })
    })
    $("#btn2").on("click", function (event) {
        $.ajax({
            url: "/cache2",
            method: "POST",
            data: {
                "sort": 2,
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_mall";
                }
            }
        })
    })
    $("#btn3").on("click", function (event) {
        $.ajax({
            url: "/cache2",
            method: "POST",
            data: {
                "sort": 3,
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/algorithmic_mall";
                }
            }
        })
    })
}

function dataselect() {
    $("#submit").on("click", function (event) {
        $.ajax({
            url: "/upload",
            method: "POST",
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("上传成功！");
                    window.location.href = "/calculate_mall";
                }else(code == 100)
                    alert("出错啦！");
            }
        })
    })

}

$(function () {
    findmore();
    select();
});