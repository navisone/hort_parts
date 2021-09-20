
        vw5.Kwf.loadDeferred(function() {
        

        (function() {
            if (!window.vw5) window.vw5 = {};
            var kwfUp = window.vw5;

            var kwfNamespaces = ["Kwf", "Kwc", "Ext2", "Ext", "$", "jQuery", "Modernizr", "require", "define", "_kwfTrl", "_kwfTrlp"];

            var kwfOrigExports = {};
            for (var i=0; i<kwfNamespaces.length; i++) {
                var name = kwfNamespaces[i];
                kwfOrigExports[name] = window[name];
                if (kwfUp[name]) {
                    window[name] = kwfUp[name];
                } else {
                    window[name] = undefined;
                    try {
                        delete window[name];
                    } catch (e) {
                    }
                }
            }
            if (!window.Ext2) window.Ext2 = {};
        
window.require = (function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({"NewsGrid_Item_Image_Square_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-newsGridItemImageSquare .vw5-newsGridItemImageSquare__container");


},{"kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"NewsGrid_Item_Image_OneThird_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-newsGridItemImageOneThird .vw5-newsGridItemImageOneThird__container");


},{"kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"NewsGrid_Item_Image_TwoThird_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-newsGridItemImageTwoThird .vw5-newsGridItemImageTwoThird__container");


},{"kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"NewsGrid_Item_Image_FullWidth_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-newsGridItemImageFullWidth .vw5-newsGridItemImageFullWidth__container");


},{"kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"NewsGrid_Item_Image_FullWidthSlim_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-newsGridItemImageFullWidthSlim .vw5-newsGridItemImageFullWidthSlim__container");


},{"kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"HomePage_Stage_Image_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-homePageStageImage .vw5-homePageStageImage__container");
var $=require("jQuery");var onReady=require("kwf/on-ready");onReady.onRender(".vw5-homePageStageImage",function(el){if(!window.requestAnimationFrame||el.parents(".vw5-themeFulltextSearchSearchView__viewContainer").length||$('body[class*="dealerPage"]').length)return;var containerEl=el.find(".vw5-homePageStageImage__outerContainer");var transform=Modernizr.prefixed("transform")||"";var posTop=0;var ticking=false;function moveImage(){containerEl.css(transform,"translateY("+posTop+"px");ticking=false}function requestTick(){if(!ticking){requestAnimationFrame(moveImage);ticking=true}}if($(window).width()>1024){$(window).on("scroll",function(){posTop=$(window).scrollTop()/6;requestTick()})}});
var $=require("jQuery");var onReady=require("kwf/on-ready");onReady.onRender(".vw5-homePageStageImage",function(el){var img=el.find("img");if(img.length&&img[0].src){el.find(".vw5-homePageStageImage__outerContainer").css("background-image","url("+img[0].src+")")}el.on("changesrc",function(ev,imageSrc){el.find(".vw5-homePageStageImage__outerContainer").css("background-image","url("+imageSrc+")")})});


},{"jQuery":"jquery/dist/jquery.js","kwf/on-ready":"kwf/commonjs/on-ready.js","kwf/responsive-img":"kwf/commonjs/responsive-img.js"}],"HomeStyleguideConform_Slider_Component-defer-js":[function(require,module,exports){
"use strict";var $=require("jQuery");var onReady=require("kwf/on-ready");var flickity=require("flickity");onReady.onRender(".vw5-homeStyleguideConformSlider",function(el){var config=el.data("config");var elements=el.find(".vw5-homeStyleguideConformSlider__listItem");if(elements.length<=1){if(elements.length){elements.css("visibility","visible")}return}elements.first().css("visibility","visible");if(config["lazyImages"]>0){for(var i=0;i<=parseInt(config["lazyImages"]);i++){if(i>parseInt(elements.length/2))break;elements.eq(i).css("visibility","visible");elements.eq(elements.length-i).css("visibility","visible")}}else{elements.css("visibility","visible")}var flkty=new flickity(el[0],config);el.data("flkty",flkty);flkty.on("cellSelect",function(){if(flkty.selectedIndex+config["lazyImages"]<=flkty.cells.length-1&&elements.eq(flkty.selectedIndex+config["lazyImages"]).css("visibility")!="visible"){elements.eq(flkty.selectedIndex+config["lazyImages"]).css("visibility","visible")}else if(flkty.selectedIndex-config["lazyImages"]>=0&&elements.eq(flkty.selectedIndex-config["lazyImages"]).css("visibility")!="visible"){elements.eq(flkty.selectedIndex-config["lazyImages"]).css("visibility","visible")}onReady.callOnContentReady(el,{action:"show"})})},{checkVisibility:true});


},{"flickity":"flickity/js/index.js","jQuery":"jquery/dist/jquery.js","kwf/on-ready":"kwf/commonjs/on-ready.js"}],"HomeStyleguideConform_Stage_Image_Component-defer-js":[function(require,module,exports){
var responsiveImg=require("kwf/responsive-img");responsiveImg(".vw5-homeStyleguideConformStageImage .vw5-homeStyleguideConformStageImage__container");
var $=require("jQuery");var onReady=require("kwf/on-ready");onReady.onRender(".vw5-homeStyleguideConformStageImage",function(el){if(!window.requestAnimationFrame||el.parents(".vw5-themeFulltextSearchSearchView__viewContainer").length||$('body[class*="dealerPage"]').length)return;var containerEl=el.find(".vw5-homeStyleguideConformStageImage__outerContainer");var transform=Modernizr.prefixed("transform")||"";var posTop=0;var ticking=false;function moveImage(){containerEl.css(transform,"translateY("+posTop+"px");ticking=false}function requestTick(){if(!ticking){requestAnimationFrame(moveImage);ticking=true}}if($(window).width()>1024){$(window).on("scroll",function(){posTop=$(window).scrollTop()/6;requestTick()})}});
var $=require("jQuery");var onReady=require("kwf/on-ready");onReady.onRender(".vw5-homeStyleguideConformStageImage",function(el){var img=el.find("img");if(img.length&&img[0].src){el.find(".vw5-homeStyleguideConformStageImage__outerContainer").css("background-image","url("+img[0].src+")")}el.on("changesrc",function(ev,imageSrc){el.find(".vw5-homeStyleguideConformStageImage__outerContainer").css("background-image","url("+imageSrc+")")})});


},{"jQuery":"jquery/dist/jquery.js","kwf/on-ready":"kwf/commonjs/on-ready.js","kwf/responsive-img":"kwf/commonjs/responsive-img.js"}]},{},["NewsGrid_Item_Image_Square_Component-defer-js","NewsGrid_Item_Image_OneThird_Component-defer-js","NewsGrid_Item_Image_TwoThird_Component-defer-js","NewsGrid_Item_Image_FullWidth_Component-defer-js","NewsGrid_Item_Image_FullWidthSlim_Component-defer-js","HomePage_Stage_Image_Component-defer-js","HomeStyleguideConform_Slider_Component-defer-js","HomeStyleguideConform_Stage_Image_Component-defer-js"]);

        for (var i=0; i<kwfNamespaces.length; i++) {
                var name = kwfNamespaces[i];
                try {
                    kwfUp[name] = window[name] || eval(name);
                } catch(e) {
                }
                if (kwfOrigExports[name]) {
                    window[name] = kwfOrigExports[name];
                } else {
                    window[name] = undefined;
                    try {
                        delete window[name];
                    } catch (e) {
                    }
                }
                eval("var "+name+" = kwfUp."+name+";");
            }
        })();
        

        });
        
//# sourceMappingURL=/assets/dependencies/Kwf_Assets_Package_ComponentPackage/HomePage/de/defer.js.map?v=1503465726
