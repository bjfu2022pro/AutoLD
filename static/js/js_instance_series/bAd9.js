function downloadBtn4() {
    $("#download21").on("click", function (event) {
        var id = $("td[id='dingdanId21']").text();
        $.ajax({
            url: "/model_download",
            method: "POST",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    var path = res['path'];
                    location.href = path;
                }else if(code == 300){
                    alert("未找到该实例的model文件！");
                }
            }
        })
    });

    $("#download22").on("click", function (event) {
        var id = $("td[id='dingdanId22']").text();
        $.ajax({
            url: "/model_download",
            method: "POST",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    var path = res['path'];
                    location.href = path;
                }else if(code == 300){
                    alert("未找到该实例的model文件！");
                }
            }
        })
    });

    $("#download23").on("click", function (event) {
        var id = $("td[id='dingdanId23']").text();
        $.ajax({
            url: "/model_download",
            method: "POST",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    var path = res['path'];
                    location.href = path;
                }else if(code == 300){
                    alert("未找到该实例的model文件！");
                }
            }
        })
    });

    $("#download24").on("click", function (event) {
        var id = $("td[id='dingdanId24']").text();
        $.ajax({
            url: "/model_download",
            method: "POST",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    var path = res['path'];
                    location.href = path;
                }else if(code == 300){
                    alert("未找到该实例的model文件！");
                }
            }
        })
    });

    $("#download25").on("click", function (event) {
        var id = $("td[id='dingdanId25']").text();
        $.ajax({
            url: "/model_download",
            method: "POST",
            data: {
                "id": id
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    var path = res['path'];
                    location.href = path;
                }else if(code == 300){
                    alert("未找到该实例的model文件！");
                }
            }
        })
    })
}

$(function () {
    downloadBtn4();
});