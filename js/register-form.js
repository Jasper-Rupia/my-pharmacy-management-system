
// ---------------------------------- form wizard (register)
function summaryPaste() {
    document.getElementById("userNamePaste").innerHTML = document.getElementById("userName").value + ",";
    var emailToLowerString = document.getElementById("email").value.toLowerCase();
    document.getElementById("email").value = emailToLowerString;
    document.getElementById("emailPaste").innerHTML = emailToLowerString;
}
var form = $("#register-form");
form.validate({
  errorPlacement: function errorPlacement(error, element) {
    element.before(error);
  },
  rules: {
    confirm: {
      equalTo: "#password",
    },
  },
});
form.children("div").steps({
  headerTag: "h3",
  bodyTag: "section",
  transitionEffect: "slideLeft",
  onStepChanging: function (event, currentIndex, newIndex) {
    form.validate().settings.ignore = ":disabled,:hidden";
    return form.valid();
  },
  onFinishing: function (event, currentIndex) {
    form.validate().settings.ignore = ":disabled";
    return form.valid();
  },
  onFinished: function (event, currentIndex) {
    alert("Account created!");
    document.getElementById("register-form").submit();
  },
});