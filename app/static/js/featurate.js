$("document").ready(function () {
    $("#qbtn").on("click", function () {
        $("#cspinner").css("display", "block");
        $.getJSON($SCRIPT_ROOT + "agq", {
            para: $("#qdata").val()
        }, function (data) {
            $("#cspinner").css("display", "none");
            $("#adata").html();
            $("#adata").html(data);
            $("#feedbform").css("display", "block");
        });
        return false;
    })
    $("#submit_final").on("click", function () {
        $.getJSON($SCRIPT_ROOT + "submit_data", {
            name: $("#name").val(),
            email: $("#email").val(),
            para: $("#qdata").val(),
            ques: $("#adata").html(),
            feeds: $("#feeds").val()
        });
        Metro.dialog.create({
            title: "",
            content: "<p style='font-weight:100;font-size:36px;'>Thank you for your feedback</p>",
            actions: [
                {
                    caption: "OK",
                    cls: "js-dialog-close secondary",
                    onclick: function () {
                        $.ajax({
                            url: "",
                            context: document.body,
                            success: function (s) {
                                $('html[manifest=saveappoffline.appcache]').attr('content', '');
                                $(this).html(s);
                            }
                        });
                        window.location.replace("http://127.0.0.1:5000/about");
                    }
                }
            ]
        });
        return false;
    })
});