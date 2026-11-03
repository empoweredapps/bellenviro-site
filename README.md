# bellenviro.au

Static site for Bell Enviro. `site/` is the deployed output; `src/` holds the generator.

- Edit content in `src/build.py`, styles in `src/assets/style.css`
- Rebuild: `cd src && python3 build.py` then copy `out/` to `../site/`
- cPanel cron runs `deploy.sh` every 10 min: pulls `main` and copies `site/` into `public_html/bellenviro.au/`
