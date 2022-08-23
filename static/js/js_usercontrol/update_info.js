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

function updateBtn() {
    $("#update_btn").on("click", function (event) {
        var email = $("input[id='email']").val();
        var username = $("input[id='username']").val();
        var gender = $("input[id='gender']").val();
        var company = $("input[id='company']").val();
        var grjm = $("input[id='grjm']").val();
        var describe = $("textarea[id='describe']").val();
        if(checkSqlInj(email) || checkSqlInj(username) || checkSqlInj(gender) || checkSqlInj(company) || checkSqlInj(grjm) || checkSqlInj(describe)){
            document.getElementById('email').value = '';
            document.getElementById('username').value = '';
            document.getElementById('gender').value = '';
            document.getElementById('company').value = '';
            document.getElementById('grjm').value = '';
            document.getElementById('describe').value = '';
            alert("你的输入中有敏感词！请重新输入！");
            return;
        }
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