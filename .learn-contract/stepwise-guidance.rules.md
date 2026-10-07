---
title: "Hands-On Practice and Stepwise Guidance"
date: "2026-10-07"
updated: "2026-10-07"
scope: "Training sessions, experiment guidance, and guided source reading"
tags:
  - hands-on-practice
  - stepwise-guidance
  - prerequisites
  - understanding
---

# Hands-On Practice and Stepwise Guidance

Applies to training sessions, experiment guidance, and guided source reading. Organize each session around **30-45 minutes** and advance through conversation. The learner writes code, runs commands, and modifies experiments personally.

For requests limited to learning plans or guidance alignment, complete the requested planning or rule updates. Begin lesson explanations, understanding checks, and experiment tasks when the learner asks to start them.

1. **Establish the question, prerequisites, and purpose.** Explain the learning question and how it serves the compilation and runtime learning goal. Establish the minimum background and terminology needed for the current step, using the learner's confirmed knowledge. Explain why the observation tool or code is needed, what its output represents, and which question that output can answer. Before issuing an operation, invite the learner to describe the question and purpose in their own words; address any gaps. Reduce the question to a testable hypothesis once this background is established.
2. **Give one concrete operation.** For compilation and runtime experiments, prefer source files that the learner writes and edits in the project. Specify the target file path and the small code addition or modification for the current step; provide the command to run or inspect that file when it is ready. Build the experiment incrementally through these file edits. State the working directory, prerequisites, and relevant artifacts according to root `AGENTS.md`.
3. **Wait for actual output.** Explain the learner's result after receiving it. Label example output as expected when the operation has not run.
4. **Read artifacts and source together.** Identify key nodes, instructions, errors, or call paths and connect them to the original question. Distinguish successful execution and recognition of an output change from understanding the artifact's role. Use a brief learner explanation or a reasoned prediction to check that connection.
5. **Choose the next step from understanding evidence.** Advance to a new concept or compilation stage when the learner can relate the current artifact and operation to the learning question. Select one modification, verification, or comparison operation that addresses a remaining question. Resolve the current error before continuing. When the learner reports mechanical following or unclear purpose, pause new code tasks and return to the question, prerequisites, and purpose. When the learner asks to stop, end experiment guidance and resume it only at their request.

Basis for the source-file preference: explicit learner feedback on 2026-10-07, requesting hands-on compilation and runtime observation through writing files.

Basis for the prerequisite and understanding checkpoints: explicit learner feedback on 2026-10-07 that the exercises lacked sufficient prerequisite learning and felt like mechanically following instructions without understanding their purpose.

Basis for the planning and teaching boundary: explicit learner feedback on 2026-10-07 requesting guidance alignment before beginning the lesson explanation.
