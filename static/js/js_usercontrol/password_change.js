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

function pwdChange() {
    $("#change_pwd").on("click", function (event) {
        var email = $("input[name='email']").val();
        var old_password = $("input[name='old_password']").val();
        var new_password = $("input[name='new_password']").val();
        var new_repwd = $("input[name='new_repwd']").val();
        if(!old_password){
            alert("请输入旧密码！")
        }
        if(!new_password){
            alert("请输入新密码！");
            return;
        }
        if(!new_repwd){
            alert("请重复新密码！");
            return;
        }

        if(checkSqlInj(email) || checkSqlInj(old_password) || checkSqlInj(new_password)  || checkSqlInj(new_repwd)){
            document.getElementById('email').value = '';
            document.getElementById('old_password').value = '';
            document.getElementById('new_password').value = '';
            document.getElementById('new_repwd').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }

        $.ajax({
            url: "/pwd_change",
            method: "post",
            data:{
                "email":email,
                "old_password":old_password,
                "new_password":new_password,
                "new_repwd":new_repwd
            },
            success:function (res) {
                var code = res['code'];
                if(code == 200){
                    alert("更改成功！即将返回个人中心");
                    window.location.href = '/usercontrol'
                }else if(code == 100){
                    alert("新密码与旧密码相同！");
                }else if(code == 300){
                    alert("两次新密码输入不一致！");
                }else if(code == 400){
                    alert("旧密码不正确！")
                }
            }
        })
    })
}

$(function(){
    pwdChange();
});