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