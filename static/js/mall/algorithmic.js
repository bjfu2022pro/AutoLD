function findmore() {
    $("#more").on("click", function (event) {
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id":$('#more').attr('value')
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

$(function () {
    findmore();
    select();
});