---
title: "Multi-Gait Locomotion Planning and Tracking for Tendon-Actuated Terrestrial Soft Robot (TerreSoRo)"
collection: publications
category: conferences
permalink: /publication/2023-10-16-multigait-planning
excerpt: 'Abstract: The adaptability of soft robots makes them ideal candidates to maneuver through unstructured environments. However, locomotion challenges arise...'
date: 2023-10-16
venue: '<a href="https://ieeexplore.ieee.org/document/10341926">2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</a>'
paperurl: 'https://arxiv.org/pdf/2307.16385'
citation: 'A. N. Mahendran, C. Freeman, A. H. Chang, M. McDougall, P. A. Vela, and V. Vikas, “Multi-Gait Locomotion Planning and Tracking for Tendon-Actuated Terrestrial Soft Robot (TerreSoRo),” <i>2023 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)</i>, Detroit, MI, USA, 2023, pp. 2542-2549, doi: 10.1109/IROS55552.2023.10341926.'
---

Abstract: The adaptability of soft robots makes them ideal candidates to maneuver through unstructured environments. However, locomotion challenges arise due to complexities in modeling the body mechanics, actuation, and robot-environment dynamics. These factors contribute to the gap between their potential and actual autonomous field deployment. A closed-loop path planning framework for soft robot locomotion is critical to close the real-world realization gap. This paper presents a generic path planning framework applied to TerreSoRo (Tetra-Limb Terrestrial Soft Robot) with pose feedback. It employs a gait-based, lattice trajectory planner to facilitate navigation in the presence of obstacles. The locomotion gaits are synthesized using a data-driven optimization approach that allows for learning from the environment. The trajectory planner employs a greedy breadth-first search strategy to obtain a collision-free trajectory. The synthesized trajectory is a sequence of rotate-then-translate gait pairs. The control architecture integrates high-level and low-level controllers with real-time localization (using an overhead webcam). Terre-SoRo successfully navigates environments with obstacles where path re-planning is performed. To best of our knowledge, this is the first instance of real-time, closed-loop path planning of a non-pneumatic soft robot.