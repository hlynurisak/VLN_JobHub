/* Application process styling */

document.addEventListener('DOMContentLoaded', function() {

    const progressBar = document.getElementById('progress-bar')
    const btnOne = document.getElementById('application-form-btn-one')
    const btnTwo = document.getElementById('application-form-btn-two')
    const btnThree = document.getElementById('application-form-btn-three')
    const btnFour = document.getElementById('application-form-btn-four')
    const btnFive = document.getElementById('application-form-btn-five')
    const continueBtn = document.getElementById('continue-btn')
    const sendApplicationBtn = document.getElementById('send-application-btn')
    const backBtn = document.getElementById('back-btn')
    const applyBtn = document.getElementById('apply-btn')
    const returnBtn = document.getElementById('return-btn')
    const homeScreenBtn = document.getElementById('home-screen-btn')

    const buttons = [btnOne, btnTwo, btnThree, btnFour, btnFive];
    let currentIndex = 0;

    const click = new MouseEvent('click', {
        bubbles: true,
        cancelable: true,
        view: window
    });

    const indexChangeEvent = new Event('indexChange')

    document.addEventListener('indexChange', function () {
        if (currentIndex === 4){
            reviewInformation()
            continueBtn.style.display = 'none';
            sendApplicationBtn.style.display = 'block';
        }
        else {
            continueBtn.style.display = 'block';
            sendApplicationBtn.style.display = 'none';
        }
    });
    function switchButtons(index){
        document.dispatchEvent(indexChangeEvent)
        buttons[index].dispatchEvent(click)
    }

    function returnToHomeScreen () {
        window.location.href = '/';
    }

    homeScreenBtn.addEventListener('click', function() {
        returnToHomeScreen();
    });

    continueBtn.addEventListener('click', function () {
        switchButtons(currentIndex+1)
    });

    backBtn.addEventListener('click', function () {
        if (currentIndex === 0){
            returnBtn.dispatchEvent(click)
        }
        switchButtons(currentIndex-1)
    })



    applyBtn.addEventListener('click', function() {
        document.getElementById('container-applications').style.display = 'none';
        document.getElementById('container-application-form').style.display = 'block';
        applyBtn.style.display = 'none';
        btnOne.dispatchEvent(click)
    });

    returnBtn.addEventListener('click', function() {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('container-applications').style.display = 'block';
        applyBtn.style.display = 'block';
    });

    sendApplicationBtn.addEventListener('click', function () {
        document.getElementById('container-application-form').style.display = 'none';
        document.getElementById('successful-application-container').style.display = 'block';
    });

    /* Progress bar filling */
    function hideAllTabs(){
        document.getElementById('application-form-tab-one').style.display = 'none';
        document.getElementById('application-form-tab-two').style.display = 'none';
        document.getElementById('application-form-tab-three').style.display = 'none';
        document.getElementById('application-form-tab-four').style.display = 'none';
        document.getElementById('application-form-tab-five').style.display = 'none';
    }

    btnOne.addEventListener('click', function() {
        hideAllTabs()
        progressBar.style.width = '20%'
        document.getElementById('application-form-tab-one').style.display = 'block';
        currentIndex = 0;
        document.dispatchEvent(indexChangeEvent)
    });

    btnTwo.addEventListener('click', function() {
        hideAllTabs()
        progressBar.style.width = '40%'
        document.getElementById('application-form-tab-two').style.display = 'block';
        currentIndex = 1
        document.dispatchEvent(indexChangeEvent)
    });

    btnThree.addEventListener('click', function() {
        hideAllTabs()
        progressBar.style.width = '60%'
        document.getElementById('application-form-tab-three').style.display = 'block';
        currentIndex = 2
        document.dispatchEvent(indexChangeEvent)
    });

    btnFour.addEventListener('click', function() {
        hideAllTabs()
        progressBar.style.width = '80%'
        document.getElementById('application-form-tab-four').style.display = 'block';
        currentIndex = 3
        document.dispatchEvent(indexChangeEvent)
    });

    btnFive.addEventListener('click', function() {
        hideAllTabs()
        progressBar.style.width = '100%'
        document.getElementById('application-form-tab-five').style.display = 'block';
        currentIndex = 4
        document.dispatchEvent(indexChangeEvent)
    });

    /* JS Data object definitions */

    const contact = new ContactInfo("", "", "", "", "", "");
    const letter = new CoverLetter("");
    const experiences = new Experiences();
    const recommendations = new Recommendations();

    function ContactInfo(fullName, streetName, houseNumber, city, country, postalCode) {
        this.fullName = fullName;
        this.streetName = streetName;
        this.houseNumber = houseNumber;
        this.city = city;
        this.country = country;
        this.postalCode = postalCode
    }

    function CoverLetter(text) {
        this.text = text;
    }

    function Experiences() {
        this.experiences = []

        this.addExperience = function(placeOfWork, role, startDate, endDate) {
            const experience = [placeOfWork, role, startDate, endDate];
            this.experiences.push(experience);
        };

        this.getAllExperiences = function() {
            return this.experiences;
        };
    }

    function Recommendations() {
        this.recommendations = []

        this.addRecommendation = function(name, email, phoneNumber, role, mayBeContacted) {
            const recommendation = [name, email, phoneNumber, role, mayBeContacted];
            this.recommendations.push(recommendation);
        };

        this.getAllRecommendations = function() {
            return this.recommendations;
        };
    }

    /* Data retrieval for review and database */

    function saveContactInfo() {
        contact.fullName = document.getElementById('name-field').value;
        contact.streetName = document.getElementById('street-field').value;
        contact.houseNumber = document.getElementById('house-field').value;
        contact.city = document.getElementById('city-field').value;
        contact.country = document.getElementById('country-field').value;
        contact.postalCode = document.getElementById('postal-field').value;
    }

    function saveCoverLetter() {
        letter.text = document.getElementById('cover-letter-field').value;
    }

    function saveExperience() {
        const placeOfWork = document.getElementById('workplace-field').value;
        const role = document.getElementById('role-field').value;
        const startDate = document.getElementById('start-date-field').value;
        const endDate = document.getElementById('end-date-field').value;
        experiences.addExperience(placeOfWork, role, startDate, endDate);
    }

    function saveRecommendation() {
        const name = document.getElementById('rec-name-field').value;
        const email = document.getElementById('rec-email-field').value;
        const phoneNumber = document.getElementById('rec-phone-field').value;
        const role = document.getElementById('rec-role-field').value;
        const mayBeContacted = document.getElementById('rec-contact-field').checked;
        recommendations.addRecommendation(name, email, phoneNumber, role, mayBeContacted);
    }

    function reviewInformation() {
        saveContactInfo();
        saveCoverLetter();
        saveExperience();
        saveRecommendation();

        const reviewTab = document.getElementById('application-form-tab-five');
        reviewTab.innerHTML = `
            <div class="review-information-container">
                <div class="contact-information-container">
                    <p class="review-header">Contact Information</p>
                    <div class="review-info">
                        <p>Name: ${contact.fullName}</p>
                        <p>Street: ${contact.streetName} ${contact.houseNumber}</p>
                        <p>City: ${contact.city}</p>
                        <p>Country: ${contact.country}</p>
                        <p>Postal Code: ${contact.postalCode}</p>
                    </div>
                </div>
                <div class="cover-letter-container">
                    <p class="review-header">Cover Letter</p>
                    <div class="review-info">
                        <p>${letter.text}</p>
                    </div>
                </div>
                <div class="experiences-container">
                    <p class="review-header">Experiences</p>
                    <div class="review-info">
                        ${experiences.getAllExperiences().map(experience => `
                            <p>Workplace: ${experience.placeOfWork}</p>
                            <p>Role: ${experience.role}</p>
                            <p>Start Date: ${experience.startDate}</p>
                            <p>End Date: ${experience.endDate}</p>
                        `).join('')}
                    </div>
                </div>
                <div class="recommendations-container">
                    <p class="review-header">Recommendations</p>
                    <div class="review-info">
                        ${recommendations.getAllRecommendations().map(recommendation => `
                            <p>Name: ${recommendation.name}</p>
                            <p>Email: ${recommendation.email}</p>
                            <p>Phone: ${recommendation.phoneNumber}</p>
                            <p>Role: ${recommendation.role}</p>
                            <p>May Be Contacted: ${recommendation.mayBeContacted}</p>
                        `).join('')}
                    </div>
                </div>
            </div>
        `;
    }
});