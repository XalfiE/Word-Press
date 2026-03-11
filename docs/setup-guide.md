# Local Development Setup Guide

**Project:** John Kimani Consulting — WordPress Website  
**Last Updated:** April 5, 2026

This guide walks you through setting up the project locally on your machine for development or review purposes. All steps assume a Windows or macOS environment.

---

## Prerequisites

Before starting, ensure you have the following installed:

- **[LocalWP](https://localwp.com/)** — Free local WordPress development tool (Windows/macOS/Linux)
- **[Git](https://git-scm.com/)** — Version control
- **A code editor** — VS Code is recommended
- Elementor Pro license key (required to activate the Pro plugin)
- WPForms license key (optional; Lite version works for local development)

---

## Step 1: Install LocalWP

1. Download LocalWP from [https://localwp.com/](https://localwp.com/)
2. Run the installer and follow the default prompts
3. Launch LocalWP once installation is complete

---

## Step 2: Clone the Repository

Open your terminal (PowerShell on Windows, Terminal on macOS) and run:

```bash
git clone https://github.com/your-username/john-kimani-consulting.git
cd john-kimani-consulting
```

---

## Step 3: Create a New Local WordPress Site

1. In LocalWP, click the **"+"** button (bottom left) to create a new site
2. Enter a site name: `john-kimani-consulting`
3. When prompted, choose:
   - **PHP version:** 8.1 (recommended)
   - **Web server:** Nginx or Apache (either works)
   - **Database:** MySQL 8.0
4. Set a WordPress admin username and password you'll remember
5. Click **Create Site**, then once it's ready, click **Start Site**

Your site will be accessible at:  
`http://john-kimani-consulting.local`

---

## Step 4: Import the WordPress XML Export

The repository includes a full WordPress XML export of the site's content (pages, posts, menus, and settings).

1. Log in to your local WordPress admin:  
   `http://john-kimani-consulting.local/wp-admin`

2. Navigate to **Tools → Import**

3. Under the **WordPress** option, click **Install Now**, then **Run Importer**

4. Click **Choose File** and select:  
   `assets/exports/john-kimani-wordpress-export.xml`

5. On the next screen:
   - Assign posts to an existing user (your local admin account)
   - **Check the box** for "Download and import file attachments"

6. Click **Submit** and wait for the import to complete

> **Note:** Some media attachments may fail to import if they were hosted externally. This is expected — re-upload any missing images manually from `assets/screenshots/after/`.

---

## Step 5: Install Required Plugins

Navigate to **Plugins → Add New** in your WordPress admin and install the following:

| Plugin | Version | Notes |
|--------|---------|-------|
| Elementor | Latest free | Required base plugin |
| Elementor Pro | Latest | License key required |
| WPForms Lite | Latest | Lite is sufficient for local dev |
| Hello Elementor | Latest | Required base theme |

After installing, activate all plugins.

---

## Step 6: Copy and Activate the Child Theme

1. Locate the child theme files in this repository:
   ```
   wp-content/themes/hello-elementor-child/
   ```

2. Copy the entire `hello-elementor-child` folder into your local WordPress themes directory:

   **Windows (LocalWP default path):**
   ```
   C:\Users\<YourUsername>\Local Sites\john-kimani-consulting\app\public\wp-content\themes\
   ```

   **macOS (LocalWP default path):**
   ```
   ~/Local Sites/john-kimani-consulting/app/public/wp-content/themes/
   ```

3. In WordPress admin, go to **Appearance → Themes** and activate **Hello Elementor Child**

---

## Step 7: Regenerate Elementor Data

After importing and activating the theme and plugins:

1. Go to **Elementor → Tools** in the WordPress admin sidebar
2. Click the **"Regenerate CSS & Data"** button
3. Wait for the process to complete
4. Clear any caching if you have a caching plugin active

This ensures all Elementor-managed styles are correctly compiled for your local environment.

---

## Step 8: Verify the Site

Visit the following pages on your local site to confirm everything loaded correctly:

- **Homepage:** `http://john-kimani-consulting.local/`
- **About:** `http://john-kimani-consulting.local/about/`
- **Blog:** `http://john-kimani-consulting.local/blog/`
- **Free Tools:** `http://john-kimani-consulting.local/free-tools/`
- **Contact:** `http://john-kimani-consulting.local/contact/`

If any page shows the default WordPress theme or a blank layout, repeat Step 7 and ensure the child theme is active.

---

## Step 9: Working with Git

### Recommended Workflow

To avoid committing sensitive WordPress files, always ensure your `.gitignore` is active before staging changes:

```bash
git status   # Review what files have changed
git add .    # Stage relevant changes only
git commit -m "your message here"
git push origin main
```

### What to Commit

Only commit files that are part of the **theme, documentation, or project configuration**:

```
✅ wp-content/themes/hello-elementor-child/
✅ docs/
✅ assets/exports/
✅ README.md
✅ CHANGELOG.md
✅ .gitignore
```

### What NOT to Commit

The `.gitignore` in this repo already excludes these, but verify manually:

```
❌ wp-config.php         (contains database credentials)
❌ wp-content/uploads/   (large media files — export separately)
❌ .env                  (environment variables)
❌ node_modules/         (never commit these)
❌ *.sql / *.bak         (database dumps — store securely elsewhere)
```

### Exporting a Fresh WordPress XML

When you've made content changes locally and want to commit an updated export:

1. Go to **Tools → Export** in WordPress admin
2. Select **"All content"**
3. Click **Download Export File**
4. Replace the existing file in `assets/exports/` with the new one
5. Commit the updated export:

```bash
git add assets/exports/john-kimani-wordpress-export.xml
git commit -m "chore: update WordPress XML export with latest content changes"
git push origin main
```

---

## Troubleshooting

| Problem | Solution |
|---------|---------|
| Elementor shows broken layout after import | Run Regenerate CSS & Data (Step 7) |
| Contact form not sending emails locally | This is expected — SMTP is configured for production only; use WPForms test mode locally |
| Media images missing | Re-upload from `assets/screenshots/` or the original export |
| Child theme not showing in Appearance | Confirm the folder was copied to the correct path (Step 6) |
| Site returns 404 on all pages | Go to **Settings → Permalinks** and click **Save Changes** to flush rewrite rules |
