/* marks/static/marks/scripts.js */

// Function to show the correct section
function showPage(pageId) {
    const sections = document.querySelectorAll('.content-section');
    sections.forEach(section => {
        section.style.display = 'none';
    });
    document.getElementById(pageId).style.display = 'block';
}

// Function to save records and show next button
function saveRecords() {
    const numStudents = document.getElementById('num_students').value;
    const numModules = document.getElementById('num_modules').value;
    const errorMessage = document.getElementById('home_error_message');
    const continueButtonContainer = document.getElementById('continue_button_container');

    if (!numStudents || !numModules) {
        errorMessage.textContent = 'Please enter both number of students and number of modules.';
        return;
    }

    errorMessage.textContent = '';

    const data = [
        ['Number of Students', numStudents],
        ['Number of Modules', numModules]
    ];

    let csvContent = 'data:text/csv;charset=utf-8,';
    data.forEach(rowArray => {
        let row = rowArray.join(',');
        csvContent += row + '\r\n';
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'Records.csv');
    document.body.appendChild(link);

    link.click();

    continueButtonContainer.style.display = 'block';
}

// Function to navigate to the next page
function continueToNextPage() {
    window.location.href = '/input-marks/';
}

// Function to save marks and show next button
function submitMarks() {
    const moduleCode = document.getElementById('module_code').value;
    const moduleName = document.getElementById('module_name').value;
    const coursework1Mark = document.getElementById('coursework_1_mark').value;
    const coursework2Mark = document.getElementById('coursework_2_mark').value;
    const coursework3Mark = document.getElementById('coursework_3_mark').value;
    const studentId = document.getElementById('student_id').value;
    const studentName = document.getElementById('student_name').value;
    const genderMale = document.getElementById('male').checked ? 'Male' : '';
    const genderFemale = document.getElementById('female').checked ? 'Female' : '';
    const dateOfEntry = document.getElementById('date_of_entry').value;

    const errorMessage = document.getElementById('input_marks_error_message');
    const continueButtonContainer = document.getElementById('continue_button_container');

    if (!moduleCode || !moduleName || !coursework1Mark || !coursework2Mark || !coursework3Mark || !studentId || !studentName || (!genderMale && !genderFemale) || !dateOfEntry) {
        errorMessage.textContent = 'Please fill in all required fields.';
        return;
    }

    errorMessage.textContent = '';

    const data = [
        ['Module Code', moduleCode],
        ['Module Name', moduleName],
        ['Coursework 1 Mark', coursework1Mark],
        ['Coursework 2 Mark', coursework2Mark],
        ['Coursework 3 Mark', coursework3Mark],
        ['Student ID', studentId],
        ['Student Name', studentName],
        ['Gender', genderMale || genderFemale],
        ['Date of Entry', dateOfEntry]
    ];

    let csvContent = 'data:text/csv;charset=utf-8,';
    data.forEach(rowArray => {
        let row = rowArray.join(',');
        csvContent += row + '\r\n';
    });

    const encodedUri = encodeURI(csvContent);
    const link = document.createElement('a');
    link.setAttribute('href', encodedUri);
    link.setAttribute('download', 'Student Marks.csv');
    document.body.appendChild(link);

    link.click();

    continueButtonContainer.style.display = 'block';
}

// Function to reset form fields
function resetMarks() {
    document.getElementById('module_code').value = '';
    document.getElementById('module_name').value = '';
    document.getElementById('coursework_1_mark').value = '';
    document.getElementById('coursework_2_mark').value = '';
    document.getElementById('coursework_3_mark').value = '';
    document.getElementById('student_id').value = '';
    document.getElementById('student_name').value = '';
    document.getElementById('male').checked = false;
    document.getElementById('female').checked = false;
    document.getElementById('date_of_entry').value = '';
    document.getElementById('input_marks_error_message').textContent = '';
}

// Function to navigate to the next page
function continueToViewMarks() {
    window.location.href = '/view-marks/';
}

// Function to view marks
function viewMarks() {
    const moduleCodeInput = document.getElementById('module_code_input').value;
    const marksDisplay = document.getElementById('marks_display');
    const errorMessage = document.getElementById('error_message');

    if (!moduleCodeInput) {
        errorMessage.textContent = 'Please enter a valid module code';
        return;
    }

    errorMessage.textContent = '';

    fetch(`/view-marks/?module_code=${moduleCodeInput}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                errorMessage.textContent = data.error;
                marksDisplay.innerHTML = '';
            } else {
                displayData(data.columns, data.data);
                errorMessage.textContent = '';
            }
        })
        .catch(error => {
            errorMessage.textContent = 'An error occurred while fetching marks';
            console.error('Error:', error);
        });
}

// Function to display data
function displayData(columns, data) {
    let tableHtml = '<table><thead><tr>';
    columns.forEach(col => {
        tableHtml += `<th>${col}</th>`;
    });
    tableHtml += '</tr></thead><tbody>';

    data.forEach(row => {
        tableHtml += '<tr>';
        columns.forEach(col => {
            tableHtml += `<td>${row[col]}</td>`;
        });
        tableHtml += '</tr>';
    });

    tableHtml += '</tbody></table>';
    document.getElementById('marks_display').innerHTML = tableHtml;
}

// Function to show update marks page
function showUpdateMarksPage() {
    showPage('update-marks');
}


// Function to display data
function displayData(columns, data) {
    let tableHtml = '<table><thead><tr>';
    columns.forEach(col => {
        tableHtml += `<th>${col}</th>`;
    });
    tableHtml += '</tr></thead><tbody>';

    data.forEach(row => {
        tableHtml += '<tr>';
        columns.forEach(col => {
            tableHtml += `<td>${row[col]}</td>`;
        });
        tableHtml += '</tr>';
    });

    tableHtml += '</tbody></table>';
    document.getElementById('marks_display').innerHTML = tableHtml;
}

// Function to show update marks page
function showUpdateMarksPage() {
    showPage('update-marks');
}
