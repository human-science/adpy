$(document).ready(function() {
  checkWindowWidth();
  checkWindowScroll();
  currentHighlight();
  menuOpenClose();
  anchorScroller();
  toTopButton();
});

$(window).resize(function() {
  $('#hamburger-button').removeClass('active');
  checkWindowWidth();
});

$(window).on('scroll', function() {
  checkWindowScroll();
});

function checkWindowWidth() {
  var windowWidth = window.innerWidth;
  var drwrNavDisp = $('#drawer-nav').css('display');
  // Over 1024px show drawer-nav.
  if (windowWidth > '1023' && drwrNavDisp == 'none') {
    $('#drawer-nav').css('display', 'block');
  // Less than 1023px, hide drawer-nav and drawer-overlay
  } else if (windowWidth <= '1023' && drwrNavDisp == 'block') {
    $('#drawer-nav, .drawer-overlay').css('display', 'none');
  } else if (windowWidth <= '1023' && drwrNavDisp == '') {
    $('#drawer-nav, .drawer-overlay').css('display', 'none');
  } else {
    return true;
  }
}

function checkWindowScroll() {
  var sect2Elem = $('.sect2');
  var contentsArr = new Array();
  for (var i = 0; i < sect2Elem.length; i++) {
    var sectArea = sect2Elem.eq(i);
    var sectHref = sect2Elem.eq(i).children('h3').children('a').attr('href');
    if (sectHref.charAt(0) == '#') {
      var sectAreaTop = sectArea.offset().top;
      var sectAreaBtm = sectAreaTop + sectArea.outerHeight();
      sectAreaTop = sectAreaTop*10;
      sectAreaBtm = sectAreaBtm*10;
      sectAreaTop = Math.ceil(sectAreaTop);
      sectAreaBtm = Math.ceil(sectAreaBtm);
      sectAreaTop = sectAreaTop/10;
      sectAreaBtm = sectAreaBtm/10;
      contentsArr[i] = [sectAreaTop, sectAreaBtm];
    }
    currentCheck();
  }
  function currentCheck() {
    var windowScrolltop = $(window).scrollTop() + 1.3;
    var dmenuAnchor = $('.drawer-dropdown.current ul li a');
    for (var i = 0; i < contentsArr.length; i++) {
      if (contentsArr[i][0] <= windowScrolltop && contentsArr[i][1] >= windowScrolltop) {
        dmenuAnchor.removeClass('current');
        dmenuAnchor.eq(i).addClass('current');
        i == contentsArr.length;
      }
    }
  }
}

function currentHighlight() {
  var url = location.pathname;
  var url_dir_length = url.split('/').length;
  var url_file_name = url.split('/')[url_dir_length - 1];
  $('.drawer-dropdown-menu-item').each(function(i, elem) {
    var href = $(elem).attr('href');
    var full = href.split('#');
    var html = full[0];
    if (url_file_name == html) {
      $(elem).closest('.drawer-dropdown').addClass('current');
    } else {
      return true;
    }
  });
}

function menuOpenClose() {
  $('#hamburger-button, .drawer-overlay').on('click', function () {
    $('#drawer-nav').fadeToggle();
    $('.drawer-overlay.drawer-toggle').fadeToggle(300);
    $('#hamburger-button').toggleClass('active');
    if ($('#searchbutton').hasClass('active') == true) {
      $('#search-bar').fadeToggle();
      $('#searchbutton').toggleClass('active');
    }
  });
}

function anchorScroller() {
  $('a[href^="#"]').on('click', function() {
    var thisElem = $(this);
    var clickedElemHref = thisElem.attr('href');
    $('a[class="link"]').each(function(i, elem) {
      var targetElemHref = $(elem).attr('href');
      if (clickedElemHref == targetElemHref) {
        var targetElemPosi = $(elem).offset().top;
        $('html,body').animate({
          scrollTop: targetElemPosi - 90
        }, 1000, 'easeOutExpo');
      } else {
        return true;
      }
    });
  });
}

function toTopButton() {
  var toTopBtn = $('.totop');
  toTopBtn.hide();
  $(window).scroll(function() {
    if ($(this).scrollTop() > 90) {
      toTopBtn.fadeIn();
    } else {
      toTopBtn.fadeOut();
    }
  });
  toTopBtn.click(function() {
    $('body,html').animate({
      scrollTop: 0
    }, 500, 'easeOutExpo');
    return false;
  });
}
