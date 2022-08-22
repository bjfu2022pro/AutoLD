function downloadBtn3() {
    $("#download16").on("click", function (event) {
        var id = $("td[id='dingdanId16']").text();
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

    $("#download17").on("click", function (event) {
        var id = $("td[id='dingdanId17']").text();
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

    $("#download18").on("click", function (event) {
        var id = $("td[id='dingdanId18']").text();
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

    $("#download19").on("click", function (event) {
        var id = $("td[id='dingdanId19']").text();
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

    $("#download20").on("click", function (event) {
        var id = $("td[id='dingdanId20']").text();
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
    downloadBtn3();
});