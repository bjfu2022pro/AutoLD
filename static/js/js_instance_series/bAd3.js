function downloadBtn1() {
    $("#download6").on("click", function (event) {
        var id = $("td[id='dingdanId6']").text();
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

    $("#download7").on("click", function (event) {
        var id = $("td[id='dingdanId7']").text();
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

    $("#download8").on("click", function (event) {
        var id = $("td[id='dingdanId8']").text();
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

    $("#download9").on("click", function (event) {
        var id = $("td[id='dingdanId9']").text();
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

    $("#download10").on("click", function (event) {
        var id = $("td[id='dingdanId10']").text();
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
    downloadBtn1();
});