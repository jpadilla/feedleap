$(function () {
    // Custom selects
    $("select").dropkick();
});

$(document).ready(function() {
    $('.login-link').click(function(e) {
        e.preventDefault();
        $("[data-toggle=tooltip]").tooltip("show");
    });
});

