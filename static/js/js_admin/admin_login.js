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

function adlogBtn(){
    $("#adlog_btn").on("click", function(event){
        var ad_name = $("input[id='ad_name']").val();
        var password = $("input[id='password']").val();
        if(!ad_name){
            alert("请输入用户名!");
            return;
        }
        if(!password){
            alert("请输入密码!");
            return;
        }

        if(checkSqlInj(ad_name) || checkSqlInj(password)){
            document.getElementById('ad_name').value = '';
            document.getElementById('password').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }

        //发送请求,ajax
        $.ajax({
            url:"/adlog_result",
            method:"POST",
            data:{
                "ad_name": ad_name,
                "password": password
            },
            success:function(res){
                var code = res['code'];
                if(code == 200){
                    window.location.href = '/admin_algor'
                }else if(code == 100){
                    alert("密码与用户名不匹配！");
                }else if(code == 300){
                    alert("该管理员不存在！");
                }
            }
        })
    })
}

$(function(){
    adlogBtn();
});