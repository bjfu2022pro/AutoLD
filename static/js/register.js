var sqlKeyWords = "select ,union ,asc ,desc ,in ,like ,into ,exec ,from ";
sqlKeyWords += ",update ,insert ,delete ,count ,asc( ,char( ,chr( ,drop ,table ,truncat ";
sqlKeyWords += ",mid( ,abs( ,= ,-- ,<script ,/script ";
sqlKeyWords += ",where ,join ,create ,alter ,cast ,exists ,; , or , and ,order by ,group by ";
//分割成数组
var sqls = sqlKeyWords.split(",");


function checkSqlInj(testInput) {                           //检测输入是否有sql关键词，有返回true,实际应用见108行
	var invalid = false;
	var chkInput = (testInput + "").toLowerCase();
	var pos = -1;
	for (var i = 0, n = sqls .length; i < n; i++) {
		pos = chkInput.indexOf(sqls [i]);
		if (pos != -1) {
			invalid = true;
			break;
		}
	}
	return invalid;
}


function captchaBtn(){
    $("#captcha_btn").on("click", function(event){
        var email = $("input[id='email']").val();
        var $this = $(this);
        if(!email){
            alert("请输入邮箱!");
            return;
        }
        var strLength=email.length;
        var index1=email.indexOf("@");
        var index2=email.indexOf(".",index1);
        if(index1==-1||index2==-1||index2<=index1+1||index1==0||index2==strLength-1){
           alert("邮箱地址不合法!");
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
                    alert("验证码发送成功,五分钟内有效");
                }else if(code == 100){
                    alert("该邮箱已被注册");
                }
            }
        })
    })
}


function regbtn(){
    $("#reg_btn").on("click", function(event){
        var email = $("input[id='email']").val();
        var vcode = $("input[id='vcode']").val();
        var password = $("input[id='password']").val();
        var repwd = $("input[id='repwd']").val();
        var agreement = document.getElementById("agreement");
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
        if(!agreement.checked){
            alert("请先同意服务协议!");
            return;
        }
        if(!vcode){
            alert("请输入验证码!");
            return;
        }
        if(!password){
            alert("请输入密码!");
            return;
        }
        if(!repwd){
            alert("请重复密码!");
            return;
        }

        if(checkSqlInj(email) || checkSqlInj(vcode) || checkSqlInj(password)  || checkSqlInj(repwd)){
            document.getElementById('email').value = '';
            document.getElementById('vcode').value = '';
            document.getElementById('password').value = '';
            document.getElementById('repwd').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }

        //发送请求,ajax
        $.ajax({
            url:"/reg_result",
            method:"POST",
            data:{
                "email":email,
                "vcode":vcode,
                "password":password,
                "repwd":repwd
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    alert("注册成功！即将前往跳转页面");
                    window.location.href = '/login'
                }else if(code == 100){
                    alert("两次密码输入不一致！");
                }else if(code == 300){
                    alert("验证码不正确！");
                }else if(code == 400){
                    alert("您还没有发送验证码！")
                }
            }
        })
    })
}

$(function(){
    captchaBtn();
    regbtn();
});