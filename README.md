# PixelPick

A minimal image colour picker — upload any image, hover over it, and instantly copy hex, RGB, or other colour codes from any pixel.

**Live:** https://hex-code-picker.onrender.com

> Hosted on a free Render plan. The server may spin down after inactivity, so the first load can take 30–60 seconds.

---

## Features

- Upload images via drag-and-drop or file browser (PNG, JPG, GIF, WEBP, BMP)
- Hover to preview colours live with a magnifier for precise pixel selection
- Click any pixel to lock the colour
- Copies hex, RGB, and other colour codes with a single click
- Clear image and start over at any time

## Running locally

**Requirements:** Python 3.8+

```bash
git clone https://github.com/georgestanley33/hex-code-picker.git
cd hex-code-picker
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000.

## Tech stack

- [Flask](https://flask.palletsprojects.com/) — backend
- [Pillow](https://python-pillow.org/) — image processing
- Vanilla JS + HTML Canvas — frontend colour sampling
