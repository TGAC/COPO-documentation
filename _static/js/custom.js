window.addEventListener('DOMContentLoaded', () => {
  const logoLink = document.querySelector('.wy-side-nav-search a');

  if (logoLink) {
    const subtitle = document.createElement('p');
    subtitle.textContent = 'Collaborative OPen Omics';
    subtitle.className = 'logo-subtitle';

    logoLink.insertAdjacentElement('afterend', subtitle);
  }
});