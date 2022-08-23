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