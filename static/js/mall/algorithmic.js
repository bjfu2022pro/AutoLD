function al_to_da() {
    $("#more1").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id": $('#more1').attr('value')
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
                "id": $('#more2').attr('value')
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
                "id": $('#more3').attr('value')
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
                "id": $('#more4').attr('value')
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
                "id": $('#more5').attr('value')
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
                "id": $('#more6').attr('value')
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


function al_to_al() {
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

function da_to_ca() {
    $("#data1").on("click", function (event) {
        $.ajax({
            url: "/calculate_cache",
            method: "POST",
            data: {
                "data": $('#data1').attr('value'),
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/calculate_mall";
                } else (code == 400)
                    window.location.href = "/pay";
            }
        })
    })
    $("#data2").on("click", function (event) {
        $.ajax({
            url: "/calculate_cache",
            method: "POST",
            data: {
                "data": $('#data2').attr('value'),
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/calculate_mall";
                } else (code == 400)
                    window.location.href = "/pay";
            }
        })
    })
    $("#data3").on("click", function (event) {
        $.ajax({
            url: "/calculate_cache",
            method: "POST",
            data: {
                "data": $('#data3').attr('value'),
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/calculate_mall";
                } else (code == 400)
                    window.location.href = "/pay";
            }
        })
    })

}

function ca_to_dj() {
    $("#DJ1").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ1').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })
    $("#DJ2").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ2').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })
    $("#DJ3").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ3').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })
    $("#DJ4").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ4').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })
    $("#DJ5").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ5').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })
    $("#DJ6").on("click", function (event) {
        $.ajax({
            url: "/DJ_cache",
            method: "POST",
            data: {
                "ca": $('#DJ6').attr('value')
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    window.location.href = "/pay";
                }
            }
        })
    })

}

$(function () {
    al_to_da();
    al_to_al();
    da_to_ca();
    ca_to_dj();

});