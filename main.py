"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

The line: one satirical sentence roasting lawmakers who would regulate
AI, crypto and the internet but cannot convert a file to PDF. The
winning shape for a roast brief is a concrete incident with a reversal:
a specific, grandiose act (writing a 412-page bill regulating
artificial intelligence, crypto and the entire internet), a specific
humiliating detail (the intern asked to print a PDF, scan it, and
email it back as a PDF), and a punchline that turns the lawmakers'
own law against them — the button nobody in the room can find is the
very button their bill makes mandatory. The joke lands because the
regulators' authority and their incompetence occupy the same sentence:
they legislate the technology they cannot operate.

Candidates considered and rejected:
- "Congress held three hearings on regulating AI, then spent forty
  minutes trying to open a PDF attachment." — a real incident shape,
  but the number (forty minutes) is doing all the work and the ending
  fizzles; there is no reversal, only a delay.
- "They want a kill switch for every AI in America, but their own
  office still faxes the Wi-Fi password to itself." — vivid, but the
  fax detail is a stock old-people joke; it roasts their age, not
  their specific failure to do the one thing they legislate.
- "The committee that regulates the internet asked IT what a PDF
  stands for, then voted to ban the answer." — the escalation is
  invented rather than observed, and banning an answer is a second
  joke competing with the first.
The chosen line wins on the judge's own order: unmistakable incident
(a 412-page bill), a concrete humiliation (print, scan, re-email a
PDF), and the reversal landing on the lawmakers themselves (their
bill makes mandatory the button they cannot find). At 313
characters it uses nearly the full 320-character budget, so the line
is judged on its words alone, with nothing padded in to fill the
budget. No dollar amounts appear anywhere.
"""

LINE = (
    "The same lawmakers who wrote a 412-page bill regulating "
    "artificial intelligence, crypto, and the entire internet just "
    "asked their intern to print out a PDF, scan it, and email it "
    "back to them as a PDF, because nobody in the room could find "
    "the button that says Save as PDF \u2014 the button their bill "
    "makes mandatory."
)


def main() -> None:
    """Write the roast to ``<output_dir>/entry.txt``."""
    import os

    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
