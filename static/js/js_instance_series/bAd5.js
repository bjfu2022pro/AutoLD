function downloadBtn2() {
    $("#download11").on("click", function (event) {
        var id = $("td[id='dingdanId11']").text();
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

    $("#download12").on("click", function (event) {
        var id = $("td[id='dingdanId12']").text();
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

    $("#download13").on("click", function (event) {
        var id = $("td[id='dingdanId13']").text();
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

    $("#download14").on("click", function (event) {
        var id = $("td[id='dingdanId14']").text();
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

    $("#download15").on("click", function (event) {
        var id = $("td[id='dingdanId15']").text();
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
    downloadBtn2();
});