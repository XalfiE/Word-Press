import json
import os

template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} | Alfie Njeru</title>
  <meta name="description" content="{description}" />
  <link rel="stylesheet" href="../css/style.css" />
</head>
<body>
  <div class="glow-orb glow-orb--gold"></div>
  <div class="glow-orb glow-orb--blue"></div>

  <nav class="navbar" id="navbar">
    <div class="container">
      <a href="../index.html" class="nav-logo">
        <div class="logo-icon">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 2.18l7 3.12v4.7c0 4.83-3.23 9.36-7 10.57-3.77-1.21-7-5.74-7-10.57V6.3l7-3.12z"/><path d="M12 7a3 3 0 00-3 3v1H8v5h8v-5h-1v-1a3 3 0 00-3-3zm1 4h-2v-1a1 1 0 112 0v1z"/></svg>
        </div>
        the-<span>infosec</span>
      </a>
      <div class="nav-links" id="navLinks">
        <a href="../index.html">Home</a>
        <a href="../about.html">About</a>
        <a href="../index.html#tools">Tools</a>
        <a href="../index.html#blog" class="active">Blog</a>
        <a href="../contact.html" class="nav-cta">Hire Me</a>
      </div>
      <button class="nav-toggle" id="navToggle" aria-label="Toggle menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <article class="blog-article">
    <div class="container">
      <div class="article-header reveal">
        <div class="article-meta">
          <span class="article-date">{date}</span>
        </div>
        <h1>{title}</h1>
      </div>
      <div class="article-content reveal reveal-delay-1">
        <p class="lead" style="font-size: 20px; color: var(--gold-500);">{description}</p>
        
        <div class="archive-notice" style="background: rgba(255,255,255,0.03); padding: 32px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); margin-top: 48px;">
          <h3 style="margin-top: 0;">Archive Notice</h3>
          <p>This article was originally published on the legacy WordPress blog. The content is currently preserved in archive format.</p>
          <p>You can view the original snapshot, complete with any images and comments, on the Wayback Machine:</p>
          <a href="{archive_url}" target="_blank" rel="noopener" class="btn btn-primary" style="display: inline-flex; margin-top: 16px;">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" style="width: 20px; height: 20px; margin-right: 8px;"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6M15 3h6v6M10 14L21 3"/></svg>
            View Full Archive
          </a>
        </div>
      </div>
      <div class="article-nav reveal reveal-delay-2">
        <a href="../index.html#blog" class="back-to-blog">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
          Back to all articles
        </a>
      </div>
    </div>
  </article>

  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-brand">
          <div class="logo-icon">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4z"/></svg>
          </div>
          <span>the-infosec</span>
        </div>
        <div class="footer-links">
          <a href="../index.html">Home</a>
          <a href="../about.html">About</a>
          <a href="../index.html#tools">Tools</a>
          <a href="../contact.html">Contact</a>
        </div>
        <div class="footer-social">
          <a href="https://www.linkedin.com/in/alfrednjeru" target="_blank" rel="noopener" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></a>
          <a href="https://github.com/XalfiE" target="_blank" rel="noopener" aria-label="GitHub"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg></a>
          <a href="https://twitter.com/alfienjeru" target="_blank" rel="noopener" aria-label="X (Twitter)"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/></svg></a>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2026 Alfie Njeru | the-infosec.com · Securing Digital Solutions</p>
      </div>
    </div>
  </footer>
  <script src="../js/main.js"></script>
</body>
</html>"""

articles = [
    {'slug': 'password-complexity-reuse-audit-tool', 'title': 'Password Complexity & Reuse Audit Tool', 'date': 'October 2025', 'desc': 'A deep dive into auditing cracked credentials for password strength, complexity patterns, and reuse detection across enterprise environments.', 'url': 'https://web.archive.org/web/2025/https://the-infosec.com/2025/10/30/password-complexity-reuse-audit-tool/'},
    {'slug': 'automating-cisco-configuration-audits', 'title': 'Automating Cisco Configuration Audits', 'date': 'March 2025', 'desc': 'Strengthen your Cisco network by automating configuration audits with ease. A practical guide to security compliance checking.', 'url': 'https://web.archive.org/web/2025/https://the-infosec.com/2025/03/14/strengthen-your-cisco-network-automating-configuration-audits-with-ease/'},
    {'slug': 'fortigate-configuration-audit-tool', 'title': 'FortiGate Configuration Files Audit Tool (FCFAT)', 'date': 'March 2025', 'desc': 'Enhancing firewall security with automated analysis of FortiGate configuration files for misconfigurations and compliance gaps.', 'url': 'https://web.archive.org/web/2025/https://the-infosec.com/2025/03/14/fortigate-configuration-files-audit-tool-fcfat-enhancing-firewall-security-with-automated-analysis/'},
    {'slug': 'oracle-ebs-security-auditing', 'title': 'Oracle EBS Security Auditing', 'date': 'November 2018', 'desc': 'An in-depth approach to auditing Oracle E-Business Suite, covering default credentials, weak passwords, application-level tests and database security controls.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2018/11/06/oracle-ebs-security-auditing/'},
    {'slug': 'from-shodan-to-rce-3-belkin-routers', 'title': 'From Shodan to RCE #3: Hacking the Belkin N600DB Wireless Router', 'date': 'January 2018', 'desc': 'The third instalment of the Shodan to RCE series, discovering and exploiting vulnerabilities in Belkin routers found exposed on the internet.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2018/01/18/from-shodan-to-rce-3-hacking-belkin-routers/'},
    {'slug': 'blackhat-europe-2017-conference-notes', 'title': 'Blackhat Europe 2017 – Conference Notes', 'date': 'December 2017', 'desc': 'Key takeaways from Blackhat Europe 2017 in London, with links to slide decks, videos, and tools from briefings and demonstrations.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/12/29/blackhat-europe-2017-conference-notes/'},
    {'slug': 'from-shodan-to-rce-1-hacking-jenkins', 'title': 'From Shodan to Remote Code Execution #1 – Hacking Jenkins', 'date': 'June 2017', 'desc': 'Exploring how misconfigured Jenkins automation servers exposed on the internet can lead to full remote code execution.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/06/22/from-shodan-to-remote-code-execution-1-hacking-jenkins/'},
    {'slug': 'samba-cve-2017-7494', 'title': 'SAMBAry Save Us!! (CVE-2017-7494)', 'date': 'May 2017', 'desc': 'Exploiting the Samba remote code execution vulnerability (CVE-2017-7494), where all versions from 3.5.0 onwards were vulnerable to a malicious shared library upload attack.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/05/26/samba-cve-2017-7494/'},
    {'slug': 'from-shodan-to-rce-2-opendreambox', 'title': 'From Shodan to RCE #2 – Hacking OpenDreambox 2.0.0', 'date': 'May 2017', 'desc': 'The second part of the Shodan to RCE series, exploiting misconfigured Dreambox digital TV set-top boxes for remote code execution.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/05/12/from-shodan-to-rce-opendreambox-2-0-0-code-execution/'},
    {'slug': 'exploiting-windows-eternalblue-doublepulsar', 'title': 'Exploiting Windows with Eternalblue & Doublepulsar with Metasploit', 'date': 'May 2017', 'desc': "Hands-on walkthrough of the NSA's EternalBlue and DoublePulsar exploits using Metasploit, the tools behind the WannaCry outbreak.", 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/05/01/exploiting-windows-with-eternalblue-and-doublepulsar-with-metasploit/'},
    {'slug': 'penetration-testing-sharepoint', 'title': 'Penetration Testing Sharepoint', 'date': 'April 2017', 'desc': 'Reconnaissance and security testing techniques for Microsoft Sharepoint, using Google dorks and OWASP Top 10 vulnerability checks.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/04/18/penetration-testing-sharepoint/'},
    {'slug': 'word-heist', 'title': 'Word Heist!', 'date': 'April 2017', 'desc': 'Leveraging MS Word documents for social engineering, capturing NTLM hashes without macros using a clever spear-phishing technique.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/04/04/word-heist/'},
    {'slug': 'do-you-know-what-your-erp-is-telling-us', 'title': 'Do You Know What Your ERP Is Telling Us?', 'date': 'March 2017', 'desc': 'Auditing Oracle E-Business Suite from an insider threat and external attacker perspective, uncovering information disclosure in ERP systems.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/03/29/do-you-know-what-your-erp-is-telling-us/'},
    {'slug': 'lateral-movement-part-ii', 'title': 'Lateral Movement: Part II', 'date': 'March 2017', 'desc': 'Continuation of the lateral movement series, focusing on techniques for privilege escalation and moving through a Windows domain environment.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/03/26/lateral-movement-part-ii/'},
    {'slug': 'should-we-be-worried-huawei-router-part-ii', 'title': 'Should We Be Worried? Huawei Router: Part II', 'date': 'March 2017', 'desc': 'Digging into the Huawei HG8245H router configuration, analysing suspicious parameters like X_HW_MonitorCollector and external server URLs.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/03/23/should-we-be-worried-huawei-router-part-ii/'},
    {'slug': 'auditing-linux-unix-os-120-seconds', 'title': 'Auditing Linux/Unix OS in 120 Seconds Flat', 'date': 'March 2017', 'desc': 'A baseline security auditing script for Linux and Unix operating systems, modelled around CIS benchmark controls that runs in under 2 minutes.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/03/20/auditing-linux-unix-os-in-120-seconds-flat/'},
    {'slug': 'huawei-hg8245h-router-privilege-escalation', 'title': 'Huawei HG8245H Router "Privilege Escalation": Part I', 'date': 'March 2017', 'desc': 'Exploring the Huawei HG8245H home router, from default credentials to privilege escalation and full configuration extraction.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/03/20/huawei-hg8245h-router-privilege-escalatio/'},
    {'slug': 'lateral-movement-part-i', 'title': 'Lateral Movement: Part I', 'date': 'January 2017', 'desc': 'How a normal domain user with no admin privileges can exploit Group Policy Preferences (GPP) passwords to become local administrator across the organisation.', 'url': 'https://web.archive.org/web/2024/https://the-infosec.com/2017/01/02/lateral-movement-part-i/'}
]

for a in articles:
    content = template.format(
        title=a['title'],
        date=a['date'],
        description=a['desc'],
        archive_url=a['url']
    )
    with open(f"blog/{a['slug']}.html", "w", encoding="utf-8") as f:
        f.write(content)

print("Generated 18 articles successfully.")
