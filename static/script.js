const cells = document.querySelectorAll('[data-cell]');
let currentPlayer = 'X';

cells.forEach(cell => {
    cell.addEventListener('click', handleClick, { once: true });
});

function handleClick(e) {
    const cell = e.target;
    const classToAdd = currentPlayer === 'X' ? 'X' : 'O';
    cell.classList.add(classToAdd);
    cell.textContent = currentPlayer;
    currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
}