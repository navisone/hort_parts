$(function(){
    $('a[href^="#catalog"]').click(function(){
        var target = $(this).attr('href');
        $('html, body').animate({scrollTop: $(target).offset().top}, 1200);
        return false;
    });
});

