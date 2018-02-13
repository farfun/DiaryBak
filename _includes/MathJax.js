MathJax.Hub.Config({

    showProcessingMessages: false, //关闭js加载过程信息
    messageStyle: "none", //不显示信息
    extensions: ["tex2jax.js"],
    
    tex2jax: {
        inlineMath: [['$', '$'], ["\\(", "\\)"]],
        displayMath: [['$$', '$$'], ["\\[", "\\]"]],
        processEscapes: true,
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'],
    },
    TeX: {equationNumbers: {autoNumber: "AMS"}}
});
MathJax.Hub.Queue(function () {
    var all = MathJax.Hub.getAllJax(), i;
    for (i = 0; i < all.length; i += 1) {
        all[i].SourceElement().parentNode.className += ' has-jax';
    }
});


MathJax.Hub.Config({
    showProcessingMessages: false, //关闭js加载过程信息

    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
        inlineMath: [["$", "$"]], //行内公式选择$
        displayMath: [["$$", "$$"]], //段内公式选择$$
        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code', 'a'], //避开某些标签
        ignoreClass: "comment-content" //避开含该Class的标签
    },
    "HTML-CSS": {
        availableFonts: ["STIX", "TeX"], //可选字体
        showMathMenu: false //关闭右击菜单显示
    }
});
MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
