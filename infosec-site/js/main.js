/* ========================================
   THE-INFOSEC.COM — Main JavaScript
   Scroll animations, nav, counters, email
   ======================================== */

document.addEventListener('DOMContentLoaded', () => {

  // ── Navbar Scroll Effect ──
  const navbar = document.getElementById('navbar');

  const handleNavbarScroll = () => {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };

  window.addEventListener('scroll', handleNavbarScroll);
  handleNavbarScroll(); // Run on load

  // ── Mobile Menu Toggle ──
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');

  if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
      navToggle.classList.toggle('active');
      navLinks.classList.toggle('active');
    });

    // Close menu when clicking a link
    navLinks.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        navToggle.classList.remove('active');
        navLinks.classList.remove('active');
      });
    });

    // Close menu when clicking outside
    document.addEventListener('click', (e) => {
      if (!navToggle.contains(e.target) && !navLinks.contains(e.target)) {
        navToggle.classList.remove('active');
        navLinks.classList.remove('active');
      }
    });
  }

  // ── Scroll Reveal Animations ──
  const revealElements = document.querySelectorAll('.reveal');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('active');
        revealObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.15,
    rootMargin: '0px 0px -40px 0px'
  });

  revealElements.forEach(el => revealObserver.observe(el));

  // ── Counter Animation ──
  const counters = document.querySelectorAll('.count-up');

  const animateCounter = (element) => {
    const target = parseInt(element.getAttribute('data-target'));
    const duration = 2000; // 2 seconds
    const startTime = performance.now();

    const updateCounter = (currentTime) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);

      // Ease-out cubic
      const easeOut = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(easeOut * target);

      element.textContent = current + '+';

      if (progress < 1) {
        requestAnimationFrame(updateCounter);
      }
    };

    requestAnimationFrame(updateCounter);
  };

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        animateCounter(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, {
    threshold: 0.5
  });

  counters.forEach(counter => counterObserver.observe(counter));

  // ── Smooth Scroll for Anchor Links ──
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;

      e.preventDefault();
      const target = document.querySelector(href);
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });

  // ── Logo Card Tilt Effect ──
  const logoCards = document.querySelectorAll('.logo-card');

  logoCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      const rotateX = (y - centerY) / 12;
      const rotateY = (centerX - x) / 12;

      card.style.transform = `perspective(500px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(500px) rotateX(0) rotateY(0) translateY(0)';
    });
  });

  // ── Tool Card Hover Glow ──
  const toolCards = document.querySelectorAll('.tool-card');

  toolCards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;

      card.style.background = `radial-gradient(400px circle at ${x}px ${y}px, rgba(202, 171, 87, 0.06), rgba(6, 15, 41, 0.6))`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.background = 'rgba(6, 15, 41, 0.6)';
    });
  });

  // ── Active Nav Link Based on Current Page ──
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a:not(.nav-cta)').forEach(link => {
    const href = link.getAttribute('href').split('#')[0];
    if (href === currentPage) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });

  // ══════════════════════════════════════
  //  CONTACT FORM — Send via Email (mailto)
  // ══════════════════════════════════════
  const contactForm = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');

  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();

      // Get form values
      const name = document.getElementById('name').value.trim();
      const email = document.getElementById('email').value.trim();
      const subject = document.getElementById('subject').value.trim() || 'Website Inquiry';
      const message = document.getElementById('message').value.trim();

      // Validate
      if (!name || !email || !message) {
        alert('Please fill in all required fields.');
        return;
      }

      // Build the email body
      const emailBody = [
        `Hello Alfie,`,
        ``,
        `You have a new message from your website:`,
        ``,
        `——————————————————`,
        `Name: ${name}`,
        `Email: ${email}`,
        `——————————————————`,
        ``,
        message,
        ``,
        `——————————————————`,
        `This message was sent from the-infosec.com contact form.`
      ].join('\n');

      // Construct mailto URL
      // This opens the visitor's default email client with the message pre-filled
      const mailtoURL = `mailto:alfie@the-infosec.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(emailBody)}`;

      // Open email client
      window.location.href = mailtoURL;

      // Show success state
      const submitBtn = document.getElementById('submitBtn');
      submitBtn.innerHTML = `
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:18px;height:18px">
          <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><path d="M22 4 12 14.01l-3-3"/>
        </svg>
        Email Client Opened!
      `;
      submitBtn.style.background = 'linear-gradient(135deg, #10b981, #059669)';
      submitBtn.disabled = true;

      // Show the success message below
      if (formSuccess) {
        contactForm.style.display = 'none';
        formSuccess.classList.add('show');
      }

      // Reset after 5 seconds so they can send another
      setTimeout(() => {
        contactForm.reset();
        contactForm.style.display = '';
        submitBtn.innerHTML = `
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width:18px;height:18px">
            <line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/>
          </svg>
          Send Message
        `;
        submitBtn.style.background = '';
        submitBtn.disabled = false;
        if (formSuccess) {
          formSuccess.classList.remove('show');
        }
      }, 5000);
    });
  }

});
