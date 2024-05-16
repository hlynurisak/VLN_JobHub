/* Application process styling */

document.addEventListener('DOMContentLoaded', function() {

    const progress_bar = document.getElementById('progress-bar')
    const btn_one = document.getElementById('application-form-btn-one')
    const btn_two = document.getElementById('application-form-btn-two')
    const btn_three = document.getElementById('application-form-btn-three')
    const btn_four = document.getElementById('application-form-btn-four')
    const btn_five = document.getElementById('application-form-btn-five')
    const continue_btn = document.getElementById('continue-btn')
    const back_btn = document.getElementById('back-btn')
    const apply_btn = document.getElementById('apply-btn')
    const return_btn = document.getElementById('return-btn')

    const buttons = [btn_one, btn_two, btn_three, btn_four, btn_five];
    let currentIndex = 0;

    const click = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        view: window
    });

    function switchButtons(index){
        buttons[index].dispatchEvent(click)
    }

    continue_btn.addEventListener('click', function () {
       switchButtons(currentIndex+1)
    });

    back_btn.addEventListener('click', function () {
        if (currentIndex === 0){
            return_btn.dispatchEvent(click)
        }
        switchButtons(currentIndex-1)
    })

    apply_btn.addEventListener('click', function() {
        document.getElementById('container-applications').style.display = 'none';
        document.getElementById('container-application-form').style.display = 'block';
        apply_btn.style.display = 'none';
        btn_one.dispatchEvent(click)
    });

    return_btn.addEventListener('click', function() {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('container-applications').style.display = 'block';
        apply_btn.style.display = 'block';
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
        progress_bar.style.width = '20%'
        document.getElementById('application-form-tab-one').style.display = 'block';
        currentIndex = 0;
    });

    btn_two.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '40%'
        document.getElementById('application-form-tab-two').style.display = 'block';
        currentIndex = 1
    });

    btn_three.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '60%'
        document.getElementById('application-form-tab-three').style.display = 'block';
        currentIndex = 2
    });

    btn_four.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '80%'
        document.getElementById('application-form-tab-four').style.display = 'block';
        currentIndex = 3
    });

    btn_five.addEventListener('click', function() {
        hideAllTabs()
        progress_bar.style.width = '100%'
        document.getElementById('application-form-tab-five').style.display = 'block';
        currentIndex = 4
    });
});