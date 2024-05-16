/* Application process styling */

document.addEventListener('DOMContentLoaded', function() {

    const progress_bar = document.getElementById('progress-bar')
    const btn_one = document.getElementById('application-form-btn-one')
    const btn_two = document.getElementById('application-form-btn-two')
    const btn_three = document.getElementById('application-form-btn-three')
    const btn_four = document.getElementById('application-form-btn-four')
    const btn_five = document.getElementById('application-form-btn-five')

    const click = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        view: window
    });

    document.getElementById('apply-btn').addEventListener('click', function() {
        document.getElementById('container-applications').style.display = 'none';
        document.getElementById('apply-btn').style.display = 'none';
        document.getElementById('container-application-form').style.display = 'block';
        btn_one.dispatchEvent(click)
    });

    document.getElementById('return-btn').addEventListener('click', function() {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('container-applications').style.display = 'block';
        document.getElementById('apply-btn').style.display = 'block';
    });

    /* Progress bar filling */
    function hideAllTabs(){
        document.getElementById('application-form-tab-one').style.display = 'none';
        document.getElementById('application-form-tab-two').style.display = 'none';
        document.getElementById('application-form-tab-three').style.display = 'none';
        document.getElementById('application-form-tab-four').style.display = 'none';
        document.getElementById('application-form-tab-five').style.display = 'none';
    }

    btn_one.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '0%'
        document.getElementById('application-form-tab-one').style.display = 'block';
    });
    btn_two.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '25%'
        document.getElementById('application-form-tab-two').style.display = 'block';
    });
    btn_three.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '50%'
        document.getElementById('application-form-tab-three').style.display = 'block';
    });
    btn_four.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '75%'
        document.getElementById('application-form-tab-four').style.display = 'block';
    });
    btn_five.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '100%'
        document.getElementById('application-form-tab-five').style.display = 'block';
    });
});