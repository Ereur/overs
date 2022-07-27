
const getProjectExp = async (project_id) => {
	console.log("hey")
	const response = await fetch('https://8000-achraffaris-leetmove-7972s58uayc.ws-eu54.gitpod.io/api/project-exp/' + project_id).catch(err => console.log(err));
	const projects = await response.json();
	console.log({ projectName: projects[0].project.name, projectExp:  projects[0].difficulty })
} 

getProjectExp(1334);

const getCurrentProjects = async () => {

	const response = await fetch('https://8000-achraffaris-leetmove-7972s58uayc.ws-eu54.gitpod.io/api/projects').catch(err => console.log(err));
	const projects = await response.json();
	const sanitizedProjects = projects.filter((userProject) => { return !userProject.project.slug.includes('exam') })
		.map((userProject) => userProject = { project: userProject.project });


	return sanitizedProjects;
}

const select = document.querySelector('select');

getCurrentProjects().then((projects) => {

	console.log(projects)
	if (!projects.length) {
		console.log(projects)
		select.options.add(new Option("No projects", ""))
	}
	else {
		projects.forEach((project) => {
			console.log(project["project"]["id"])
			select.options.add(new Option(project["project"]["name"], project["project"]["id"]))

		});
	}


})

// e.options[e.selectedIndex].value
// console.log(select.selectedIndex)

function kolchi(project_id) {
	console.log(project_id)
}


function addNewRow() {
	let table = document.getElementById("table");
	let rowCount = table.rows.length;
	let row = table.insertRow(rowCount);
	row.insertCell(0).innerHTML = '<a class="text-heading font-semibold" href="#" class="col-sm-12">' + "Philosophers" + '</a>'
	row.insertCell(1).innerHTML = '<div class="form-group w-20"><input type="number" class="form-control form-control-sm col-sm-12" value="100" min="0" max="125"></div>'
	row.insertCell(2).innerHTML = '<span class="badge rounded-pill bg-soft-success text-success font-semibold">+45</span>'
	let trash = row.insertCell(3)
	select.options.remove(select.selectedIndex)
	trash.innerHTML = '<button type="button" onclick="deleteRow(this)" class="btn btn-sm btn-square btn-neutral text-danger-hover" class="col-sm-1"><i class="bi bi-trash"></i></button>'
	trash.className = "text-end"
}

function deleteRow(ele) {
	ele.parentNode.parentNode.remove();
	select.options.add(new Option("Philosophers", "1334"))
}


//** under dev **//


let addPrjBtn = document.getElementById("submit-option");
addPrjBtn.addEventListener("click", handleSubmit);

function handleSubmit(event) {
	event.preventDefault();
	let addPrjBtn = document.forms["project-form"].prj;
	let project_id = addPrjBtn.value
	if (project_id != "") {
		addNewRow();
	}
}