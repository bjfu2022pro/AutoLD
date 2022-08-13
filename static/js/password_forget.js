function reset_Captcha(){
    $("#reset_captcha").on("click", function(event){
        var email = $("input[name='email']").val();
        var $this = $(this);
        var strLength=email.length;
        var index1=email.indexOf("@");
        var index2=email.indexOf(".",index1);
        if(!email){
            alert("请输入邮箱!");
            return;
        }
        if(index1==-1||index2==-1||index2<=index1+1||index1==0||index2==strLength-1){
           alert("邮箱地址不合法!");
           return;
        }
        $.ajax({
            url:"/reset_mail",
            method:"POST",
            data:{
                "email":email
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    //取消点击事件
                    $this.off("click");
                    //倒计时
                    var countDown = 60;
                    var timer = setInterval(function(){
                        countDown -= 1;
                        if(countDown>0){
                            $this.text(countDown+"秒后再发送");
                        }else{
                            $this.text("获取验证码");
                            reset_Captcha();
                            clearInterval(timer);
                        }
                    },1000)
                    alert("验证码发送成功");
                }else if(code == 100){
                    alert("该邮箱未被注册！");
                }
            }
        })
    })
}


function reset_pwd(){
    $("#reset_pwd").on("click", function(event) {
        var email = $("input[name='email']").val();
        var vcode = $("input[name='vcode']").val();
        var new_password = $("input[name='new_password']").val();
        var new_repwd = $("input[name='new_repwd']").val();
        var strLength=email.length;
        var index1=email.indexOf("@");
        var index2=email.indexOf(".",index1);
        if(!email){
            alert("请输入邮箱！");
            return;
        }
        if(index1==-1||index2==-1||index2<=index1+1||index1==0||index2==strLength-1){
           alert("邮箱地址不合法!");
           return;
        }
        if(!vcode){
            alert("请输入验证码！");
            return;
        }
        if(!new_password){
            alert("请输入新密码！");
            return;
        }
        if(!new_repwd){
            alert("请重复新密码！");
            return;
        }
        $.ajax({
            url:"/pwd_fgt_ck",
            method:"POST",
            data:{
                "email":email,
                "vcode":vcode,
                "password":new_password,
                "repwd":new_repwd
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    alert("重置成功！即将前往登录界面");
                    window.location.href = '/login'
                }else if(code == 100){
                    alert("两次密码输入不一致！");
                }else if(code == 300){
                    alert("验证码不正确！");
                }
                else if(code == 400) {
                    alert("请先发送验证码到您的邮箱！");
                }
            }
        })
    })
}

$(function(){
    reset_Captcha();
    reset_pwd();
});