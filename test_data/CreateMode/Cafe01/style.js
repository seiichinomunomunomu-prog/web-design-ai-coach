(() => {
  const menuButton = document.querySelector('.menu-button');
  const globalNav = document.querySelector('.global-nav');
  const navLinks = document.querySelectorAll('.global-nav a');

  if (!menuButton || !globalNav) {
    return;
  }

  const closeMenu = () => {
    menuButton.classList.remove('is-open');
    globalNav.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'メニューを開く');
  };

  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.classList.toggle('is-open');
    globalNav.classList.toggle('is-open', isOpen);
    menuButton.setAttribute('aria-expanded', String(isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'メニューを閉じる' : 'メニューを開く');
  });

  navLinks.forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 800) {
      closeMenu();
    }
  });
})();