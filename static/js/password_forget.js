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

        if(checkSqlInj(email) || checkSqlInj(vcode) || checkSqlInj(new_password)  || checkSqlInj(new_repwd)){
            document.getElementById('email').value = '';
            document.getElementById('vcode').value = '';
            document.getElementById('new_password').value = '';
            document.getElementById('new_repwd').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }

        $.ajax({
            url:"/pwd_fgt_ck",
            method:"POST",
            data:{
                "email":email,
                "vcode":vcode,
                "new_password":new_password,
                "new_repwd":new_repwd
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