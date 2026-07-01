# Prototype — logic branch (terminal app)

For the `prototype` skill, when the question is "does this state model / logic feel right?" Build a tiny interactive terminal app that pushes the state machine through cases that are hard to reason about on paper.

1. **State the question** in one paragraph at the top — a logic prototype that answers the wrong question is pure waste.
2. **Use the host project's language/runtime.**
3. **Isolate the logic in a portable, pure module** behind a small interface — a pure `reducer(state, action) => state`, an explicit state machine, pure functions over a data type, or a class with a clear method surface. **Keep it pure:** no I/O, no terminal code, no `console.log` for control flow. The TUI shell is throwaway; the logic module is the durable asset — the validated reducer/machine gets lifted into real code and the shell deleted.
4. **Build the smallest TUI — full-frame redraw.** Every tick, clear the screen (`console.clear()` / `\033[2J\033[H`) and redraw so the user sees one stable view, not growing scrollback. Each frame: current state pretty-printed one field per line (bold field names, dim IDs/timestamps via ANSI), then a shortcut bar: `[a] add  [d] delete  [t] tick clock  [q] quit`. Loop: init in-memory state → read one keystroke → dispatch to a handler that mutates state → redraw the full frame → repeat until quit. The whole frame fits one screen.
5. **One command** via the existing task runner.
6. **Hand over the run command;** the user drives it. Add actions if asked. Capture the answer, then delete the shell (keep the pure logic module if it's going into production).

Anti-patterns: tests, a real DB, generalising, blurring the logic with the TUI, shipping the TUI shell.
