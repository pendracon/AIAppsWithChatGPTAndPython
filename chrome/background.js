chrome.browserAction.onClicked.addListener(function() {
    chrome.windows.create({
        url: 'popup.html',
        type: 'popup',
        width: 600,
        height: 600
    });
});
