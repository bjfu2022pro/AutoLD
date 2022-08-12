function captchaBtn(){
    $("#captcha_btn").on("click", function(event){
        var email = $("input[id='email']").val();
        if(!email){
            alert("请输入邮箱!");
            return;
        }
        //发送请求,ajax
        $.ajax({
            url:"/mail",
            method:"POST",
            data:{
                "email":email
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    alert("验证码发送成功")
                }
            }
        })
    })
}

$(function(){
    captchaBtn();
});