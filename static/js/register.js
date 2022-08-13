function captchaBtn(){
    $("#captcha_btn").on("click", function(event){
        var email = $("input[id='email']").val();
        var $this = $(this);
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
                            captchaBtn();
                            clearInterval(timer);
                        }
                        
                    },1000)
                    alert("验证码发送成功");
                }
            }
        })
    })
}

$(function(){
    captchaBtn();
});