# Scene and shot breakdown (refined)

## Method and boundary confidence

Full-duration review now includes 136 frames sampled at 1 fps, five dense contact sheets, and 18 before/after checks around candidate transitions (`frames/dense/` and `frames/cutchecks/`). FFmpeg `scdet` ran over all 30 fps frames at thresholds 8 and 4; `freezedetect=n=-48dB:d=1` ran over the full stream. Threshold-8 found seven major changes; threshold-4 found additional candidates but also reacts to shot, prop, and caption changes. Boundaries below combine these tools with direct before/after frame inspection. Times are approximate to within a few frames; source has 30 fps.

Review of the before/after checks shows abrupt composition changes at the listed points: **hard cuts**. No fade or dissolve is visible in the reviewed changes. Some are new locations/scenes, others are new shots within the same riverside or story setting; changes are not automatically counted as new scenes.

## Timeline

| Approx. interval | Shot / visual evidence | Boundary interpretation | Story function |
|---|---|---|---|
| 00:00–00:05.23 | Night bedroom, bed under purple cover, pale face and small oil lamp; opening caption. | Static tableau; cut at 05.23. | Hook and protagonist setup. |
| 00:05.23–00:15.33 | Brown-robed figure points toward tall dark doorway/panel with a hanging green shape. | Hard cut at 05.23 from bed; held pose; cut at 15.33. | Ominous story setup. |
| 00:15.33–00:23.37 | Riverbank village, row of houses, boat and figures. | Hard cut to cooler daylight/dusk tableau; cut at 23.37. | Place and background context. |
| 00:23.37–00:31.67 | Red building and central dark entrance with two silhouettes, striped figure centered in foreground. | Hard cut; symmetrical held composition; cut at 31.67. | Establishes a threatening encounter/location. |
| 00:31.67–00:35.70 | Boat/river tableau with gray-robed figure and several small boats. | Hard cut; new riverside view; cut at 35.70. |
| 00:35.70–00:44.17 | Night river with stakes/boats in the distance and striped figure on shore. | Hard cut; wide locked frame. Cut at 44.17. | Narrative exposition before confrontation. |
| 00:44.17–00:55.73 | Covered stall at water’s edge; brown-robed seller/figure raises an arm toward a dark figure holding a pale blade. | Hard cut; mostly frozen for about 7.8 s by −48 dB freeze threshold (44.37–52.20). Cut at 55.73. | Weapon and threat are made legible. |
| 00:55.73–01:02.27 | Dark bank; upright blade at left and striped figure at right, dialogue captions. | Hard cut to tighter face-off tableau; cut at 62.27. | Sets up the question and demanded answer. |
| 01:02.27–01:09.33 | Blade appears fallen/angled by a dark figure; small objects on ground. | Hard cut/pose change within same night setting; cut at 69.33. | Implies the attack rather than animating it continuously. |
| 01:09.33–01:14.23 | Pale face protrudes from blue water. | Hard cut to close-up; cut at 74.23. | Aftermath/reveal in water. |
| 01:14.23–01:23.13 | Return to bed; altered face/eyes and red vertical marks appear as captions describe illness. | Hard cut; very limited pose changes; cut at 83.13. | Consequence and supernatural explanation. |
| 01:23.13–01:32.47 | Return to dark doorway/panel with hanging green shape and small orange glow/marks at its base; gesturing figure. | Hard cut; static ritual-like view; cut at 92.47. |
| 01:32.47–01:39.30 | Daytime temple/courtyard façade; robed figure carries a rectangular object. | Hard cut; strong day/night palette shift; cut at 99.30. | Introduces a remedy location. |
| 01:39.30–01:46.00 | Simple canopy/well-like structure, slatted surface and bucket; figure holds a small object. | Hard cut; held medium-wide; cut at 106.00. | Remedy instructions. |
| 01:46.00–01:48.30 | Dark water with small face; pale sword/implement above. | Hard cut; scene detector time 106.00; cut at about 108.30. | Reasserts the spirit’s fear/weakness. |
| 01:48.30–01:53.03 | Yellow figure raises a rectangular icon beside a gray silhouette against black. | Hard cut identified visually near 108.30; new symbolic tableau; cut at 113.03. | Emphasizes a specific protector/authority. |
| 01:53.03–02:01.60 | Dark statue on a lit pedestal; pink-clad figure at left. | Hard cut at 113.03; long static shrine tableau; cut at 121.60. | Climactic sacred image and explanation. |
| 02:01.60–02:08.70 | Night riverbank, small hut, standing figure, boat and child’s head in water. | Hard cut at 121.60; wide aftermath tableau; cut at about 128.70. | Narrated resolution/rescue context. |
| 02:08.70–02:15.98 | Close-up of child’s head in water; mouth/expression changes near the end. | Hard cut to close-up around 128.70; short final held image; end cut, no observed fade. | Final uneasy sting/tag. |

## Detector output and frozen-image evidence

`scdet` at threshold 8 detected 05.233, 15.333, 23.367, 31.667, 35.700, 92.467, 99.300. At threshold 4 it additionally detected 35.733 (same transition window), 44.167, 55.733, 62.267, 69.333, 74.233, 83.133, 106.000, 113.033, and 121.600. These are detector candidates; composition checks determine whether they are scene changes or shot/pose changes. A visual close-up around 128.7 was also confirmed despite not passing either threshold.

`freezedetect` found 29 intervals longer than 1 s at `n=-48 dB`, median 3.2 s. Examples include 05.43–10.63 (5.2 s), 23.57–28.53 (4.97 s), 44.37–52.20 (7.83 s), 86.30–91.67 (5.37 s), and 117.07–121.13 (4.07 s). This detects low pixel-level change, not necessarily every layer: subtle water/light movement may remain below the threshold. Overall, the sequence is strongly held-image/tableau-based with occasional prop or pose changes.

## Transitions and motion

Verified at checked boundaries: abrupt hard cuts; no visible fade/dissolve in the sampled before/after frames. No camera pan, tilt, zoom, or parallax was detected in 1 fps review; very small motion between sampled frames remains possible. Face, arm, sword, glow and water states change through a few pose/prop swaps. Exact animation cadence and layer construction remain unknown.
