$(function(){
  $(document).on('click', function() {   
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideUp();
    $('.show-card').removeClass('slideInDown').addClass('hidden');
  });
  
  //弹出框显示后的一些操作
  $('.modal').on({
    'show.bs.modal': function (e) {
      $(this).children('.modal-dialog')
      .css('margin','0 auto')
      .wrap('<div class="wrap-modal-main"></div>')
      .wrap('<div class="wrap-modal-con"></div>');
      $('.wrap-modal-main').css({
        'display': 'table',
        'width': '100%',
        'height': '100%'
      });
      $('.wrap-modal-con').css({
        'display': 'table-cell',
        'width': '100%',
        'vertical-align': 'middle'
      });

    },
    'shown.bs.modal': function (e) {
      $(this).find('.form-control').first().focus();
    }
  });
  
  //登陆
  $('#btnLogin').on('click', function () {
    $('#registerModal').modal('hide');
  });
  $('.show-card').on('click', function (event) {
    event.stopPropagation();
  });
  $('.dt-username').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();
    $('.show-card').toggleClass('hidden slideInDown');
  });

  //忘记密码
  $('#btnForgetpsw').on('click', function () {
    $('#loginModal').modal('hide');
  });

  //注册
  $('#btnRegister').on('click', function () {
    $('#loginModal').modal('hide');
  });

  //创建班级
  
  //search
  $('#search').on({
    click: function(event) {
      event.stopPropagation();
    },
    focus: function() {
      if($(this).val() == '') {
        $('#hotkeyword').slideDown();
      }
    },
    keyup:function() {
      $('#hotkeyword').slideUp();
      $('#keyword-group').slideDown();
    }
  });
  $('.search-dp').click(function(event) {
    event.stopPropagation();
  });
  $('#hotkeyword a').click(function(event) {
    event.preventDefault();
    $('#search').val($(this).text());
    $('#hotkeyword').slideUp();
    $('#keyword-group').slideDown();
  });


  //点击收藏
  $('.house').on('click', function (event) {
    event.preventDefault();
    var _thisI = $(this).children('i');
    var _thisIclass = _thisI.hasClass('v5-icon-saved');
    _thisI.toggleClass('v5-icon-saved');
    var _text = (_thisIclass == true) ? '收藏' : '已收藏';
    $(this).children('span').text(_text);
  });
  
  $('.plan-tip').hover(function() {
    $('.plan-tip-box').addClass('show');
  }, function() {
    $('.plan-tip-box').removeClass('show');
  });
  
  $('.feedback-switch').click(function(){
    $(this).toggleClass('active');
    var _has_active = $(this).hasClass('active');
    if(_has_active){
      $(this).parent('.feedback').animate({
        bottom:0
      },500);
    }
    else{
      $(this).parent('.feedback').animate({
        bottom:'-300px'
      },500);
    }
  });
  
  $('img#viptips').hover(function(){
    $(this).tooltip({
      template: '<div class="tooltip tooltip-vip" role="tooltip"><div class="tooltip-arrow"></div><div class="tooltip-inner"></div></div>'
    });
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('[data-toggle="tooltip"]').hover(function(){
    $(this).tooltip('show');
  },function(){
    $(this).tooltip('hide');
  });
  
  $('.class-list li').click(function(){
    event.preventDefault();
    $(this).toggleClass('active');
    if($(this).hasClass('active')){
      $(this).siblings().removeClass('active');
      $('#btn-okpay').removeClass('btn-micv5-disabled1').removeAttr('disabled');
    }
    else{
      $('#btn-okpay').addClass('btn-micv5-disabled1').attr('disabled','disabled');
    }
  })
});

function v5_popover_tpl(tpl_class,elem,popover_container,popover_placement,popover_trigger){
  var elem_popover = document.getElementById(elem);
  var popover_c = $('.' + popover_container);
  popover_c.popover({
    content:elem_popover,
    container:'body',
    template:'<div class="popover ' + tpl_class + '" role="tooltip"><div class="arrow"></div><h3 class="popover-title"></h3><div class="popover-content"></div></div>',
    placement:popover_placement,
    trigger:popover_trigger,
    html: true
  });
}

