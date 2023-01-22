/*-------- sendmail() function --------*/
function sendMail(contactForm) {
    emailjs.send("gmail", "happycamper", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contactsummary": contactForm.contactsummary.value
    })
    .then(
        function(response) {
            console.log("YES SUCCESS", response);
        },
        function(error) {
            console.log("OH NO!!!!", error);
        }
    );
    return false;
}