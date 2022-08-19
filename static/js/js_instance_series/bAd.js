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
                    alert("运行中...");
                }
            }
        })
    })

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
                    alert("运行中...");
                }
            }
        })
    })

    $(".begin3").on("click", function (event) {
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
                    alert("运行中...");
                }
            }
        })
    })

    $(".begin4").on("click", function (event) {
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
                    alert("运行中...");
                }
            }
        })
    })

    $(".begin5").on("click", function (event) {
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
                    alert("运行中...");
                }
            }
        })
    })

}

$(function(){
    beginBtn();
});