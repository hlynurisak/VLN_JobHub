/* Application process styling */

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('apply-btn').addEventListener('click', function() {
        document.getElementById('container-applications').style.display = 'none';
        document.getElementById('apply-btn').style.display = 'none';
        document.getElementById('container-application-form').style.display = 'block';
    });

    document.getElementById('return-btn').addEventListener('click', function() {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('container-applications').style.display = 'block';
        document.getElementById('apply-btn').style.display = 'block';
    })

    /* Progress bar filling */
    function hideAllTabs(){
        document.getElementById('application-form-tab-one').style.display = 'none';
        document.getElementById('application-form-tab-two').style.display = 'none';
        document.getElementById('application-form-tab-three').style.display = 'none';
        document.getElementById('application-form-tab-four').style.display = 'none';
        document.getElementById('application-form-tab-five').style.display = 'none';
    }

    document.getElementById('application-form-btn-one').addEventListener('click', function() {
        hideAllTabs()
        document.getElementById('progress-bar').style.width = '20%'
        document.getElementById('application-form-tab-one').display.style = 'block';
    })
    document.getElementById('application-form-btn-tow').addEventListener('click', function() {
        hideAllTabs()
        document.getElementById('progress-bar').style.width = '40%'
        document.getElementById('application-form-tab-two').display.style = 'block';
    })
    document.getElementById('application-form-btn-three').addEventListener('click', function() {
        hideAllTabs()
        document.getElementById('progress-bar').style.width = '60%'
        document.getElementById('application-form-tab-three').display.style = 'block';
    })
    document.getElementById('application-form-btn-four').addEventListener('click', function() {
        hideAllTabs()
        document.getElementById('progress-bar').style.width = '80%'
        document.getElementById('application-form-tab-four').display.style = 'block';
    })
    document.getElementById('application-form-btn-five').addEventListener('click', function() {
        hideAllTabs()
        document.getElementById('progress-bar').style.width = '100%'
        document.getElementById('application-form-tab-five').display.style = 'block';
    })
});