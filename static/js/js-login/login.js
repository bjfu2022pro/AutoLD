function logbtn(){
    $("#log_btn").on("click", function(event){
        var email = $("input[id='email']").val();
        var password = $("input[id='password']").val();
        if(!email){
            alert("请输入邮箱!");
            return;
        }
        if(!password){
            alert("请输入密码!");
            return;
        }
        //发送请求,ajax
        $.ajax({
            url:"/login_result",
            method:"POST",
            data:{
                "email":email,
                "password":password
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    window.location.href = '/usercontrol'
                }else if(code == 100){
                    alert("密码与用户名不匹配！");
                }else if(code == 300){
                    alert("邮箱未注册！");
                }
            }
        })
    })
}

$(function(){  
    logbtn();
});