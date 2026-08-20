/**
 * CareerSync Core JavaScript
 */

function dismissAlert(el) {
    if (!el) return;
    el.style.opacity = '0';
    el.style.transform = 'translateY(-6px)';
    setTimeout(() => {
        el.remove();
    }, 300);
}

document.addEventListener('DOMContentLoaded', () => {
    // Prevent Form Resubmission dialog on browser refresh
    if (window.history.replaceState) {
        window.history.replaceState(null, null, window.location.href);
    }

    // Flash message auto-dismiss
    const alerts = document.querySelectorAll('.alert-msg');
    alerts.forEach(alert => {
        setTimeout(() => {
            dismissAlert(alert);
        }, 4000);
    });

    // Auto-scroll handler for applications table pagination/sort
    if (window.location.search.includes('page=') || window.location.search.includes('sort=')) {
        const table = document.getElementById('applications-table');
        if (table) {
            const y = table.getBoundingClientRect().top + window.scrollY - 24;
            window.scrollTo({ top: y, behavior: 'instant' });
        }
    }

    // Auto-scroll handler for AI Insights section
    const aiInsightsSection = document.getElementById('ai-insights');
    if (aiInsightsSection && (window.location.search.includes('ai=1') || window.location.hash === '#ai-insights')) {
        const targetElement = (aiInsightsSection.previousElementSibling && aiInsightsSection.previousElementSibling.classList.contains('alert-msg')) 
            ? aiInsightsSection.previousElementSibling 
            : aiInsightsSection;
        const y = targetElement.getBoundingClientRect().top + window.scrollY - 110;
        window.scrollTo({ top: Math.max(0, y), behavior: 'instant' });
        window.history.replaceState({}, document.title, window.location.pathname);
    }

    // Mobile menu toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const mobileMenuIcon = document.getElementById('mobile-menu-icon');

    if (mobileMenuBtn && mobileMenu && mobileMenuIcon) {
        mobileMenuBtn.addEventListener('click', () => {
            const isHidden = mobileMenu.classList.contains('hidden');
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                mobileMenuIcon.classList.remove('fa-bars');
                mobileMenuIcon.classList.add('fa-times');
            } else {
                mobileMenu.classList.add('hidden');
                mobileMenuIcon.classList.remove('fa-times');
                mobileMenuIcon.classList.add('fa-bars');
            }
        });
    }
});
