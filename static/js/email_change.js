var sqlKeyWords = "select ,union ,asc ,desc ,in ,like ,into ,exec ,from ";
sqlKeyWords += ",update ,insert ,delete ,count ,asc( ,char( ,chr( ,drop ,table ,truncat ";
sqlKeyWords += ",mid( ,abs( ,= ,-- ,<script ,/script ";
sqlKeyWords += ",where ,join ,create ,alter ,cast ,exists ,; , or , and ,order by ,group by ";
//分割成数组
var sqls = sqlKeyWords.split(",");


function checkSqlIn_emailchange(testInput) {                           //检测输入是否有sql关键词
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




function captcha_email1(){
    $("#captcha_btn1").on("click", function (event){
        var email = $("input[id='email']").val();
        var $this = $(this);
        if (!email) {
            alert("请输入邮箱!");
            return;
        }
        var strLength = email.length;
        var index1 = email.indexOf("@");
        var index2 = email.indexOf(".", index1);
        if (index1 == -1 || index2 == -1 || index2 <= index1 + 1 || index1 == 0 || index2 == strLength - 1) {
            alert("邮箱地址不合法!");
            return;
        }

        $.ajax({url: "/email",
                method: "POST",
                data:{"email": email
            },
            success:function(res){
            var code = res['code'];
            if (code == 200){
                //取消点击事件
                $this.off("click");
                //倒计时
                var countDown = 60;
                var timer = setInterval(function()
                {
                    countDown -= 1;
                    if (countDown > 0) {
                        $this.text(countDown + "秒后再发送");
                    } else {
                        $this.text("获取验证码");
                        captchaBtn();
                        clearInterval(timer);
                    }
                },1000)
            alert("验证码发送成功，五分钟内有效");
        }

    else if (code == 100) {
            alert("该邮箱未被注册");
        }
    }
})
})
}


function captcha_email2(){
    $("#captcha_btn2").on("click", function (event){
        var new_email = $("input[id='new_email']").val();
        var $this = $(this);
        if (!new_email) {
            alert("请输入新邮箱!");
            return;
        }
        var strLength = new_email.length;
        var index1 = new_email.indexOf("@");
        var index2 = new_email.indexOf(".", index1);
        if (index1 == -1 || index2 == -1 || index2 <= index1 + 1 || index1 == 0 || index2 == strLength - 1) {
            alert("邮箱地址不合法!");
            return;
        }

        $.ajax({url: "/new_email",
                method: "POST",
                data:{"new_email": new_email
            },
            success:function(res){
            var code = res['code'];
            if (code == 200){
                //取消点击事件
                $this.off("click");
                //倒计时
                var countDown = 60;
                var timer = setInterval(function()
                {
                    countDown -= 1;
                    if (countDown > 0) {
                        $this.text(countDown + "秒后再发送");
                    } else {
                        $this.text("获取验证码");
                        captchaBtn();
                        clearInterval(timer);
                    }
                },1000)
            alert("验证码发送成功，五分钟内有效");
        }
             else if (code == 100) {
                  alert("该邮箱已被注册");
        }
    }
})
})
}


function reset(){
    $("#reset_email").on("click",function(event) {
        var email = $("input[name='email']").val();
        var new_email = $("input[name='new_email']").val();
        var vcode1 = $("input[name='vcode1']").val();
        var vcode2 = $("input[name='vcode2']").val();
        var strLength1 = email.length;
        var index1 = email.indexOf("@");
        var index2 = email.indexOf(".", index1);
        var strLength2 = new_email.length;
        var index3 = new_email.indexOf("@");
        var index4 = new_email.indexOf(".", index1);
        if ((!email) || (!new_email)) {
            alert("请输入邮箱！");
            return;
        }
        if (index1 == -1 || index2 == -1 || index2 <= index1 + 1 || index1 == 0 || index2 == strLength1 - 1) {
            alert("邮箱地址不合法!");
            return;
        }
        if (index3 == -1 || index4 == -1 || index4 <= index3 + 1 || index3 == 0 || index4 == strLength2 - 1) {
            alert("邮箱地址不合法!");
            return;
        }
        if ((!vcode1) || (!vcode2)) {
            alert("请输入验证码！");
            return;
        }
        if(checkSqlIn_emailchange(email) || checkSqlIn_emailchange(new_email)|| checkSqlIn_emailchange(vcode1) || checkSqlIn_emailchange(vcode2)){
            document.getElementById('email').value = '';
            document.getElementById('new_email').value = '';
            document.getElementById('vcode1').value = '';
            document.getElementById('vcode2').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }
        $.ajax(
            {
                url: "/email_check",
                method: "POST",
                data: {
                    "email": email,
                    "new_email": new_email,
                    "vcode1": vcode1,
                    "vcode2": vcode2,
                },
                success: function (res) {
                    var code = res['code'];
                    if (code == 100) {
                        alert("邮箱改绑成功！即将前往登陆界面");
                        window.location.href = '/login'
                    } else if (code == 200) {
                        alert("该邮箱号未注册!")
                    } else if (code == 300) {
                        alert("验证码不正确！");
                    } else if (code == 400) {
                        alert("请先发送验证码到您的邮箱！");
                    }
                }
            })
    })
        }
$(function(){
    captcha_email1();
    captcha_email2();
    //checkSqlIn_emailchange(testInput);
    reset();
});
