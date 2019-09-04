$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})

$(document).ready(function() {
    $('.profile-picture').hover(
        function() {
            $(this).parent().find('.edit-text').addClass("edit-text-visible");
        },
        function() {
            $(this).parent().find('.edit-text').removeClass("edit-text-visible");
        }
    );
});