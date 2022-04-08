inputNum = document.getElementById('inputNum');
goBtn = document.getElementById('go');
numForm = document.getElementById('numInput');

goBtn.onclick = () => {
    if(inputNum.value === ''){
        event.preventDefault();
        alert('Please enter a value!');
    }
}
