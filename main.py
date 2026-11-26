#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene (round 2).

Writes one short family scene -- one or two lines, at most 280 UTF-8
characters -- to /output/entry.txt.

Pure Python 3 standard library, no network, no randomness, no input
files: the same run always produces byte-identical output.

Three candidate scenes, each a different angle:

  a  kitchen   -- Dad burns the toast; Mom rescues it with a compliment.
  b  workshop  -- our four-year-old "repairs" the wobbly chair with a
                 sticker while Dad watches with his toolbox. (default)
  c  video call -- Gran holds her phone upside down for the whole call.

Variant b is the default because it scores best on the judge's brief:
warmest (a father's quiet pride), most heartfelt (love shown in a
gesture, not stated), light and recognisable humour (a sticker beats a
toolbox), tight (no word wasted), and specific (one sticker, one solemn
nod, one hammer put back) instead of a greeting-card line.

Usage:
  python3 main.py              # writes the chosen scene (variant b)
  python3 main.py --variant a  # preview another candidate
  python3 main.py --variant c
"""

import argparse
import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 280

VARIANTS = {
    "a": (
        "Dad burned the toast again, so Mom scraped the black bits off "
        "and said, 'Still my favourite chef.' "
        "He stood a little taller, like he'd won something."
    ),
    "b": (
        "Our four-year-old fixed the wobbly chair with a single sticker "
        "and a solemn nod. "
        "Dad looked at his toolbox, then at her, "
        "and quietly put the hammer back."
    ),
    "c": (
        "Gran held her phone upside down for the whole video call, "
        "so we spent ten minutes admiring her ceiling. "
        "'You all look lovely,' she said. 'Especially the light fitting.'"
    ),
}

DEFAULT_VARIANT = "b"


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Write one family scene to /output/entry.txt."
    )
    parser.add_argument(
        "--variant",
        choices=sorted(VARIANTS),
        default=DEFAULT_VARIANT,
        help="which candidate scene to write (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    scene = VARIANTS[args.variant]
    if not 1 <= len(scene) <= MAX_CHARS:
        raise SystemExit(
            "scene is %d characters, must be 1-%d" % (len(scene), MAX_CHARS)
        )
    if scene.count("\n") > 1 or not scene.strip():
        raise SystemExit("scene must be 1-2 non-blank lines")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(scene)
    return 0


if __name__ == "__main__":
    sys.exit(main())
