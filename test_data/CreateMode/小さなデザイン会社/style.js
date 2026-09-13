(() => {
  const menuButton = document.querySelector('.menu-button');
  const navigation = document.querySelector('.global-navigation');
  const navigationLinks = navigation.querySelectorAll('a');

  const closeMenu = () => {
    menuButton.classList.remove('is-open');
    navigation.classList.remove('is-open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.setAttribute('aria-label', 'メニューを開く');
  };

  menuButton.addEventListener('click', () => {
    const isOpen = menuButton.getAttribute('aria-expanded') === 'true';

    menuButton.classList.toggle('is-open', !isOpen);
    navigation.classList.toggle('is-open', !isOpen);
    menuButton.setAttribute('aria-expanded', String(!isOpen));
    menuButton.setAttribute('aria-label', isOpen ? 'メニューを開く' : 'メニューを閉じる');
  });

  navigationLinks.forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 767) {
      closeMenu();
    }
  });
})();