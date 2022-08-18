function findmore() {
    $("#more1").on("click", function (event) {
        // var title = document.getElementById("title1").value;
        // var introduce = document.getElementById("introduce1").value;
        $.ajax({
            url: "/cache",
            method: "POST",
            data: {
                "id": 1,
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
                "id": 2,
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
                "id": 3,
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
                "id": 4,
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
                "id": 5,
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
                "id": 6,
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