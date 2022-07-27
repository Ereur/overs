var myHeaders = new Headers();
myHeaders.append("Authorization", "Bearer 2b02f873ad47b78b18b4d654ad74fef6c71f35515bcd20204188e135cf96bd64");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://api.intra.42.fr/v2/users/94528/projects_users?filter[status]=in_progress", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));