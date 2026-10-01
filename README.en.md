[🇪🇸 Español](README.es.md) | [🇬🇧 English](README.en.md)

# Book of Enoch / Tlacuilo

## 📖 What this is

An independent research project on the textual transmission of the **Book of
Enoch**, from Genesis 6 to Knibb's critical edition (1978). But it is also,
at the same time, a **documented case study on human-AI collaboration**:
every prompt, every logbook entry, every error and correction.

It is not a software project. It is not an academic paper in the traditional
sense. It is an **open lab notebook** kept by a researcher who has no
laboratory, who worked for several months from an Android phone running
Termux, and who since May of this year was able to recover his late-2013
iMac — on which, starting in early 2025, he painstakingly installed a Linux
distribution called Linux Mint, then moved to Linux Mint Debian, and
finally settled on Debian 13 Trixie. It goes without saying that the move
from MacOS to Linux on an iMac was extremely hard. For these and many other
reasons, I have decided to document down to the last detail how he thinks,
how he asks, and how he errs.

---

## 🧑‍🔬 About the author

I am **Marco Antonio Vázquez Elías**, a Mexican surgeon, 60 years old. I
have practiced medicine for decades. In **April 2025**, a rupture — which I
myself provoked in several ways — forced me out of my comfort zone
violently. In some things I was very wrong. In others I was brutally
assertive. Both things are true at the same time. I have learned to accept
the consequences of my actions: I do not cry over them, I move forward, and
I try not to make the same mistakes again. The unjust treatment I received
I keep, for now, to myself. **What will validate me is my work, not my
complaints.**

I learned to program from scratch. I learned to use Termux on an Android
phone. I learned Rust, Julia, C, C++, Go, Python, and assembly — not as an
expert, not even as a programmer, but as someone who needed to solve
concrete problems. I accumulated some 90 GB of scripts in that process. I
learned to move through Ethiopian manuscripts in Ge'ez to work with the
Book of Enoch in its only complete version known to date. I do not know a
single word of that language, but I have managed — and what you see here is
that process, with its errors, mistakes, doubts, and finally, its
successes. I learned to use language models, the various AIs, as research
assistants, not as oracles.

I do not tell this as a story of overcoming. I tell it because it is **the
most important methodological datum of this project**: if an individual,
under adverse conditions and without formal technical training, can build a
reproducible research pipeline, then the problem of access to research is
not one of capacity. It is one of **institutional design**. In my case,
though, it was a very powerful survival instinct — and being in creative
mode preserved my mental and physical health.

I ate Japanese peanuts and amaranth and water. I slept in a shelter and
spent several months in Terminal 1 of Mexico City International Airport.
It is not melodrama, nor a personal-growth speech, much less a reproach. It
is what it is: a travel route. Perhaps less kind than that of James Bruce,
the Scot who brought Enoch to Europe from Ethiopia at the end of the 18th
century. The perfect analogy is amaranth: when water is reduced, it does
not merely survive; it produces more seed. Like adaptogens: they grow on
wood, in cold, in adversity, and produce compounds that help other
organisms resist. Not all individuals respond the same way to stress. Some
break. Others reorganize. **This project is the documented case of one who
reorganized.** It is not representative. It is not prescriptive. It is
evidence that the phenomenon exists. But it is not for everyone — people
can break, I have no doubt.

---

## 🧠 Positioning: I am not a programmer

It must be very clear: **I have not learned to program in the formal
sense.** If asked basic commands, I could not apply them without context. I
do not think like a programmer. One of my advantages.

But if asked whether I could do things in Python on an Android phone just
like that, I would say no — and I would explain why. You would have to
create a slow process, one that takes time to fragment itself, to clean up
the garbage it generates, to manage memory. Python's limitations, its
distance from the metal. R calculations are also far from the metal. That
is why Julia. That is why Rust. That is why C++, which is a firearm: it
can blow up a project or a piece of hardware in a single slip. All of that
I know.

I am a good project manager. I know how to choose tools, how to find
shortcuts, how to build profiles. But formally I am not a programmer, I
repeat, I do not think like one. I am myself thinking in a non-reductionist
and fragmentary way, because it is absurd to self-limit through
specializations, which are more an excuse not to delve into the
complexities of a human being. My opinion. I am a general physician, with
pride and competencies — I refer to the evidence. I know how to do research
and what I do is to solve problems; that is my engine and the reason for my
existence. I will not stop doubting and asking; certainty is not for me.

What I can do is **use and apply**. I have applied even Refal, the Soviet
logic tool, which is complex. I understood it and used it. I do not know
every command by heart, but I know perfectly well what it is for, what
Prolog is for, what the others are for. I do not put them on as decoration.
**I design systems, I design solutions, I design shortcuts, and I build
them myself.** I am stubborn, persistent, resilient. I do not accept a "no"
as an answer. But I also do not stupidly obsess over things having to come
out one single way.

That is what I have built for myself. And I built it because my response to
extreme situations was **to order myself mentally as best I could** and,
with a phone, to start building things. That construction was what allowed
me to survive the disorder, the disaster around me, the defencelessness,
the absolute vulnerability. I built myself a shell that now, when I think
about it, I do not even know how — but there are **90 GB that justify it**.
And now I am putting it in order on a phone. Impossible, but there it is.

---

## 🧠 Hybrid human-AI method

This project **uses artificial intelligence intensively and transparently**.
It does not hide it. It studies it.

- The scripts are mine. The query strategy is mine too.
- The AI is a tool, not an authority.
- Every hypothesis is classified as **documentary evidence** or **reasonable
  doubt**.
- The logbooks are, in themselves, the corpus of study of the method.

### Hypothesis classification

| Category | Meaning | Presentation |
|---|---|---|
| **Documentary evidence** | Primary or secondary source confirming it | As fact, with citation |
| **Reasonable doubt** | Documentary silence or indications, without proof | As declared hypothesis |

This distinction is not cosmetic. It is the line separating publishable
speculation from irresponsible assertion.

---

## 🔬 Documented example of associative thinking

On September 30, 2026, while working on the project, I came across a YouTube
video: an interview by neurologist Dr. David Perlmutter with Dr. M. Marc
Abreu about a case of ALS reversal through controlled brain hyperthermia. I
shared it with a rehabilitation physician friend who has a patient with
ALS, and wrote to her the following:

> *"I just came across this. I'm not sure if it's real or not, but there's
> something in the mechanisms of fever that got me thinking. I should
> clarify that it may very well not work, or be useful only for certain
> patients. Fever and the mechanisms it sets in motion could theoretically
> repair some of what happens in ALS — I mean the anomalous folding of
> certain proteins, and that I do believe is a legitimate datum. This
> Brazilian physician doesn't say it that way, but that's how I understood
> it."*

And later, I expanded:

> *"I have doubts about how he raises brain temperature, whether it's safe,
> and whether it's backed by solid data. The costs cannot be low, but fever
> can indeed refold those misfolded proteins and explain some of the
> improvements he has seen. From there to it being applicable to all cases
> and offering something more is very complicated to assert. But current
> ALS treatments don't offer much either; they are very expensive and have
> been compared with placebos. The main error of the current predominant
> model is thinking that with ONE single molecule or a few you are going to
> resolve a mess the size of ALS; that is impossible and extremely
> expensive. In contrast, these fungi offer more than a molecule — they are
> a host of molecules — and that is where an opportunity may lie."*

### What this episode reveals

This chain of associations is not a product of the AI. It is the result of
**interdisciplinary thinking forged by life experience, neurodivergence,
and the need to solve problems without institutional resources**. The AI
documents, organizes, and verifies. The human connects, intuits, and
decides what is worth investigating.

The author connected:

1. The historical observation of Wagner-Jauregg (Nobel 1927) on
   malaria-induced fever for treating neurosyphilis.
2. The finding that in both cases (neurosyphilis and ALS) the misfolded
   protein TDP-43 appears.
3. The mechanism of **heat shock proteins (HSPs)** as molecular chaperones.
4. The literature on **adaptogens** (fungi such as *Hericium erinaceus* or
   compounds such as withaferin A) that activate those same pathways.
5. The botanical observation that controlled water stress improves the
   yield of certain plants (amaranth).
6. The hypothesis, against the dominant model, that neurodegenerative
   diseases are **systemic**, not exclusively cerebral.

This hypothesis is classified as **reasonable doubt with a plausible
biological mechanism**. It is not a fact. It is not presented as a cure. It
is presented as a line of investigation that deserves exploration with
well-selected cohorts and methodological rigor.

---

## 📂 Repository structure
henoch/
├── scripts/ # Source code (AGPLv3)
├── worklog/ # Session logbooks (CC BY 4.0)
├── config/ # Metadata, preregistered criteria
├── translations/ # Primary source texts
├── hashes/ # Integrity verification
├── logs/ # Execution logs
├── results/ # Metrics and analysis
├── prompts/ # Documented prompt system
├── fuentes/ # Bibliographic corpus (metadata; PDFs in .gitignore)
├── README.md # This document (Spanish version by default)
├── README.en.md # English version (this file)
├── README.es.md # Spanish version
├── LICENSE-CODE # AGPLv3
└── LICENSE-DOCS # CC BY 4.0


---

## ⚖️ Licenses

This project uses a **dual license model**, differentiating between content
types:

- **Code** (scripts, pipelines, notebooks): **AGPLv3**
- **Documentation** (logbooks, texts, analyses): **CC BY 4.0**

### Why dual?

Because software and documentation are works of a different nature. AGPLv3
protects code against use in network services. CC BY 4.0 allows maximum
dissemination and reuse of textual content, with the sole obligation of
attribution.

### Radical transparency

This project **does not reserve** its methodology. It publishes the prompts,
the query sequence, the source curation, and the complete logbooks. The
value of this work is not in a secret formula: it is in the unrepeatable
way in which a specific individual thinks, asks, and errs. The formula is
not a procedure. The formula is the author.

---

## 🚫 On vetoes against AI use

Some repositories, such as Codeberg, exclude projects that use AI
intensively. This project **does not submit to that veto**. Using AI is not
cheating. It is using the tools available in the 21st century to ask
questions of the 1st. An independent researcher without access to
institutional infrastructure deserves the same opportunities as one with a
budget.

---

## 🌍 Languages

This project is multilingual by vocation. The README and logbooks are
published in:

| Language | Status | Notes |
|---|---|---|
| **Spanish** (es) | ✅ Primary | Author's native language |
| **English** (en) | ✅ Primary | Lingua franca of research |
| **Portuguese** (pt) | 🔄 In progress | Connection with Brazil and Latin American community |
| **Others** | ⏳ Planned | Arabic, Hebrew, Amharic are natural candidates |

---

## 📬 Contact

- **GitLab** (primary repository):
  [republica_imperfecta-group/henoch](https://gitlab.com/republica_imperfecta-group/henoch)
- **GitHub** (read-only mirror):
  [unamuno1936/henoch](https://github.com/unamuno1936/henoch)
- **Email**: `1936.unamuno.libre@proton.me`

---

## 📝 Final note

This README is not a declaration of results. It is a **declaration of
method**.

I do not claim that fever cures ALS. I do not claim that adaptogenic fungi
are a treatment. I do not claim that my case is replicable. I claim that
there are **patterns** — controlled stress, chaperones, protein folding,
systemic response — that deserve rigorous investigation, and that my way of
connecting those patterns, forged under atypical circumstances, produces
hypotheses that others do not formulate.

If anyone understands this, welcome. If no one does, so be it. The work is
done and documented. That is what matters.

---

*Last updated: 2026-10-01*
*Version: 2.0*
