/**
 * Toggle fullscreen function who work with webkit and firefox.
 * @function toggleFullScreen
 * @param {Object} event
 */
 function toggleFullScreen(event) {
    var element = event.target.parentNode.parentNode;

    var isFullscreen = document.webkitIsFullScreen || document.mozFullScreen || false;

    element.requestFullScreen = element.requestFullScreen || element.webkitRequestFullScreen || element.mozRequestFullScreen || function() {
        return false;
    };
    document.cancelFullScreen = document.cancelFullScreen || document.webkitCancelFullScreen || document.mozCancelFullScreen || function() {
        return false;
     };

    isFullscreen ? document.cancelFullScreen() : element.requestFullScreen();
 }