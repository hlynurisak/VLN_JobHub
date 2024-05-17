/* Application process styling */

document.addEventListener('DOMContentLoaded', function() {

    const formTabs = document.querySelectorAll('.application-form-tab');
    const reviewTab = document.getElementById('application-form-tab-five');
    const reviewContent = document.getElementById('review-content');
    const progressBar = document.getElementById('progress-bar');
    const btnOne = document.getElementById('application-form-btn-one');
    const btnTwo = document.getElementById('application-form-btn-two');
    const btnThree = document.getElementById('application-form-btn-three');
    const btnFour = document.getElementById('application-form-btn-four');
    const btnFive = document.getElementById('application-form-btn-five');
    const continueBtn = document.getElementById('continue-btn');
    const sendApplicationBtn = document.getElementById('send-application-btn');
    const backBtn = document.getElementById('back-btn');
    const returnBtn = document.getElementById('return-btn');

    const buttons = [btnOne, btnTwo, btnThree, btnFour, btnFive];
    let currentIndex = 0;

    const click = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        view: window
    });

    const indexChangeEvent = new Event('indexChange')


    function switchButtons(index) {
        document.dispatchEvent(indexChangeEvent)
        buttons[index].dispatchEvent(click)
    }

    /* Progress bar filling */
    function hideAllTabs() {
        formTabs.forEach((tab, index) => {
            tab.style.display = 'none'
        });
    }

    function validateForm() {
        const inputs = formTabs[currentIndex].querySelectorAll('input, textarea, select');
        let valid = true;
        inputs.forEach(input => {
            if (input.required && !input.value.trim()) {
                input.style.borderColor = 'red';
                valid = false;
            } else {
                input.style.borderColor = '';
            }
        });
        return valid;
    }
    function updateReviewContent() {
        reviewContent.innerHTML = '';
        formTabs.forEach(tab => {
            const inputs = tab.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                if (input.type !== 'hidden' && input.value.trim()) {
                    const label = tab.querySelector(`label[for=${input.id}]`) || {};
                    const text = document.createElement('p');
                    text.innerText = `${label.innerText || input.name}: ${input.value}`;
                    reviewContent.appendChild(text);
                }
            });
        });
    }

    document.addEventListener('indexChange', function () {
        if (currentIndex === 4) {
            continueBtn.style.display = 'none';
            sendApplicationBtn.style.display = 'block';
            updateReviewContent();
        } else {
            continueBtn.style.display = 'block';
            sendApplicationBtn.style.display = 'none';
        }
    });

    continueBtn.addEventListener('click', function () {
        switchButtons(currentIndex + 1)
    });

    backBtn.addEventListener('click', function () {
        if (currentIndex === 0) {
            returnBtn.dispatchEvent(click)
        }
        switchButtons(currentIndex - 1)
    })


    returnBtn.addEventListener('click', function () {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('container-applications').style.display = 'block';
    });

    btnOne.addEventListener('click', function () {
        hideAllTabs()
        progressBar.style.width = '20%'
        document.getElementById('application-form-tab-one').style.display = 'block';
        currentIndex = 0;
        document.dispatchEvent(indexChangeEvent)
    });

    btnTwo.addEventListener('click', function () {
        hideAllTabs()
        progressBar.style.width = '40%'
        document.getElementById('application-form-tab-two').style.display = 'block';
        currentIndex = 1
        document.dispatchEvent(indexChangeEvent)
    });

    btnThree.addEventListener('click', function () {
        hideAllTabs()
        progressBar.style.width = '60%'
        document.getElementById('application-form-tab-three').style.display = 'block';
        currentIndex = 2
        document.dispatchEvent(indexChangeEvent)
    });

    btnFour.addEventListener('click', function () {
        hideAllTabs()
        progressBar.style.width = '80%'
        document.getElementById('application-form-tab-four').style.display = 'block';
        currentIndex = 3
        document.dispatchEvent(indexChangeEvent)
    });

    btnFive.addEventListener('click', function () {
        hideAllTabs()
        progressBar.style.width = '100%'
        document.getElementById('application-form-tab-five').style.display = 'block';
        currentIndex = 4
        document.dispatchEvent(indexChangeEvent)
    });

        document.getElementById('add-experience').addEventListener('click', function() {
        let formIdx = document.querySelectorAll('.application-form-tab-three .dynamic-form').length;
        let formTemplate = document.getElementById('id_experiences-TOTAL_FORMS').value;
        let newForm = formTemplate.replace(/__prefix__/g, formIdx);
        document.querySelector('.application-form-tab-three').insertAdjacentHTML('beforeend', newForm);
        document.getElementById('id_experiences-TOTAL_FORMS').value = formIdx + 1;
    });

    document.getElementById('add-recommendation').addEventListener('click', function() {
        let formIdx = document.querySelectorAll('.application-form-tab-four .dynamic-form').length;
        let formTemplate = document.getElementById('id_recommendations-TOTAL_FORMS').value;
        let newForm = formTemplate.replace(/__prefix__/g, formIdx);
        document.querySelector('.application-form-tab-four').insertAdjacentHTML('beforeend', newForm);
        document.getElementById('id_recommendations-TOTAL_FORMS').value = formIdx + 1;
    });
});