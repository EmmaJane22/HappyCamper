/*-------- sendmail() function --------*/
function sendMail(contactForm) {
    emailjs.send("service_c23rfuq", "happycamper", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contactsummary": contactForm.contactsummary.value
    })
    .then(
        function(response) {
            alert("Email sent successfully!");
            console.log("YES SUCCESS", response);
            window.location.href = "/";
            return true;
        },
        function(error) {
            alert("Email failed-please try again");
            console.log("OH NO!!!!", error);
        }
    );
    return false;
}