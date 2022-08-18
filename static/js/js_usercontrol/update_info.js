function updateBtn() {
    $("#update_btn").on("click", function (event) {
        var email = $("input[id='email']").val();
        var username = $("input[id='username']").val();
        var gender = $("input[id='gender']").val();
        var company = $("input[id='company']").val();
        var grjm = $("input[id='grjm']").val();
        var describe = $("textarea[id='describe']").val();
        $.ajax({
            url: "/user_update",
            method: "get",
            data: {
                "email": email,
                "username": username,
                "gender": gender,
                "company": company,
                "grjm": grjm,
                "describe": describe
            },
            success: function (res) {
                var code = res['code'];
                if (code == 200) {
                    alert("更新成功！");
                    window.location.href = '/usercontrol'
                }
            }
        })
    })
}

$(function(){
    updateBtn();
});