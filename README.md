# blalterman.github.io

This repository hosts my personal research website built with
[Jekyll](https://jekyllrb.com/), the static site generator used by
GitHub Pages.

## Directory layout

```
/          # Repository root
├── _config.yml  # Jekyll configuration (to be added)
├── _posts/      # Blog posts (optional)
├── index.html   # Home page
├── style.css    # Site styling (optional)
├── README.md    # Project documentation
└── AGENTS.md    # Guidelines for using AI assistance
```

Pages and posts are generated via Jekyll templates. The `AGENTS.md` file
outlines how AI tools contribute to the project.

## Viewing the site

To preview the site locally, install dependencies and start the Jekyll
development server:

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000` in your browser.

The site can also be hosted on GitHub Pages by pushing the main branch to GitHub and enabling Pages in the repository settings.
