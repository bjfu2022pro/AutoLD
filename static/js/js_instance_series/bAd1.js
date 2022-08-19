function downloadBtn() {
    $("#download1").on("click", function (event) {
        var id = $("td[id='dingdanId1']").text();
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

    $("#download2").on("click", function (event) {
        var id = $("td[id='dingdanId2']").text();
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

    $("#download3").on("click", function (event) {
        var id = $("td[id='dingdanId3']").text();
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

    $("#download4").on("click", function (event) {
        var id = $("td[id='dingdanId4']").text();
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

    $("#download5").on("click", function (event) {
        var id = $("td[id='dingdanId5']").text();
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
    downloadBtn();
});