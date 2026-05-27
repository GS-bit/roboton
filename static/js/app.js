/* Eventos do intro container: */

const playBtn = document.getElementById('play-btn');
const introContainer = document.getElementById('intro-container');
const gameContainer = document.getElementById('game-container');

playBtn.addEventListener('click', () => {
    introContainer.classList.toggle('animation');
    playBtn.style.visibility = 'hidden';
    gameContainer.style.display = 'grid';
});

/* Eventos do game container: */

const offensivesBtn = document.getElementById('offensives-btn');
const specialsBtn = document.getElementById('specials-btn');

const offensivesList = document.getElementById('offensives-list');
const specialsList = document.getElementById('specials-list');

const movementBtns = document.getElementsByClassName('movement-btn');

const movementDescription = document.getElementById('movement-description');

offensivesBtn.addEventListener('click', (e) => {
    if(!offensivesList.classList.contains('reveal')){
        offensivesList.classList.toggle('reveal');
        offensivesList.classList.toggle('animation');
        specialsList.classList.remove('reveal');
        specialsList.classList.remove('animation');

        offensivesBtn.style.backgroundColor = '#555';
        specialsBtn.style.backgroundColor = '#333';
    }
});

specialsBtn.addEventListener('click', (e) => {
    if(!specialsList.classList.contains('reveal')){
        specialsList.classList.toggle('reveal');
        specialsList.classList.toggle('animation');
        offensivesList.classList.remove('reveal');
        offensivesList.classList.remove('animation');

        specialsBtn.style.backgroundColor = '#555';
        offensivesBtn.style.backgroundColor = '#333';
    }
});

Array.from(movementBtns).forEach(btn => {
    btn.addEventListener('mouseover', (e) => {
        const moveDesc = e.target.dataset.desc;
        const movePower = e.target.dataset.power;

        movementDescription.innerHTML = `<p>${moveDesc}</p><p>Poder: ${movePower}</p>`;
        movementDescription.classList.add('active');
    });
});

Array.from(movementBtns).forEach(btn => {
    btn.addEventListener('mouseleave', () => {
        movementDescription.classList.remove('active');
    });
});

Array.from(movementBtns).forEach(btn => {
    btn.addEventListener('click', (e) => {
        const moveName = e.target.textContent;

        fetch('/move', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ move: moveName })
        })
        .then(response => response.json())
        .then(data => {
            const dialog = document.getElementById('dialog');
            dialog.innerHTML = `<p>${data.dialog}</p>`;

            const log = document.querySelector('#log textarea');
            if(data.log != ""){
                log.innerHTML += `\n${data.log}`;
                log.scrollTop = log.scrollHeight;
            }

            const benignotonBar = document.getElementById('benignoton-current-health');
            const malignotonBar = document.getElementById('malignoton-current-health'); 
            benignotonBar.style.width = `${data.benignotonVidaPercentual}%`;
            malignotonBar.style.width = `${data.malignotonVidaPercentual}%`;

            // Mostrando as condições de Benignoton e Malignoton:

            // Primeiro resetamos tudo e depois adicionamos a condição:

            const benignotonParalyzed = document.querySelector("#benignoton-status .paralyzed");
            const benignotonFrozen = document.querySelector("#benignoton-status .frozen");
            const benignotonBurned = document.querySelector("#benignoton-status .burned");
            if(benignotonParalyzed) benignotonParalyzed.style.display = "none";
            if(benignotonFrozen) benignotonFrozen.style.display = "none";
            if(benignotonBurned) benignotonBurned.style.display = "none";

            if(data.benignotonCondicao == "Paralisado"){
                const benignotonParalyzed = document.querySelector("#benignoton-status .paralyzed");
                if(benignotonParalyzed) benignotonParalyzed.style.display = "inline";
            }

            else if(data.benignotonCondicao == "Congelado"){
                const benignotonFrozen = document.querySelector("#benignoton-status .frozen");
                if(benignotonFrozen) benignotonFrozen.style.display = "inline";
            }

            else if(data.benignotonCondicao == "Queimado"){
                const benignotonBurned = document.querySelector("#benignoton-status .burned");
                if(benignotonBurned) benignotonBurned.style.display = "inline";
            }

            const malignotonParalyzed = document.querySelector("#malignoton-status .paralyzed");
            const malignotonFrozen = document.querySelector("#malignoton-status .frozen");
            const malignotonBurned = document.querySelector("#malignoton-status .burned");
            if(malignotonParalyzed) malignotonParalyzed.style.display = "none";
            if(malignotonFrozen) malignotonFrozen.style.display = "none";
            if(malignotonBurned) malignotonBurned.style.display = "none";

            if(data.malignotonCondicao == "Paralisado"){
                const malignotonParalyzed = document.querySelector("#malignoton-status .paralyzed");
                if(malignotonParalyzed) malignotonParalyzed.style.display = "inline";
            }

            else if(data.malignotonCondicao == "Congelado"){
                const malignotonFrozen = document.querySelector("#malignoton-status .frozen");
                if(malignotonFrozen) malignotonFrozen.style.display = "inline";
            }

            else if(data.malignotonCondicao == "Queimado"){
                const malignotonBurned = document.querySelector("#malignoton-status .burned");
                if(malignotonBurned) malignotonBurned.style.display = "inline";
            }

            // Atualizando as cores das barras de vida de Benignoton e Malignoton:
            if(data.benignotonVidaPercentual >= 50) {
                benignotonBar.style.backgroundColor = 'green';
            }

            else if(data.benignotonVidaPercentual >= 15) {
                benignotonBar.style.backgroundColor = 'rgb(216, 216, 37)';
            }

            else{
                benignotonBar.style.backgroundColor = 'rgb(175, 31, 31)';
            }

            if(data.malignotonVidaPercentual >= 50) {
                malignotonBar.style.backgroundColor = 'green';
            }

            else if(data.malignotonVidaPercentual >= 15) {
                malignotonBar.style.backgroundColor = 'rgb(216, 216, 37)';
            }

            else{
                malignotonBar.style.backgroundColor = 'rgb(175, 31, 31)';
            }
        })
        .catch(error => {
            alert('Erro ao processar o movimento: ', error);
        });
    });
});