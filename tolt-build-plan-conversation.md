# Tolt Innovations Internship — Build Plan Conversation

**Date:** 31 May 2026
**Context:** Strategy and build plan for a developer internship demo at Tolt Innovations (Dublin AI consultancy, founded by Liz Bancroft-Turner). The build is an EU AI Act Risk Self-Assessment Tool to be delivered Wednesday afternoon via a warm intro through an existing intern.

---

## Me

https://www.tolt.ie/
this company is from https://www.linkedin.com/in/lizbancroftturner/

i have an opportunity to intern as a developer i wanted to open by solving a small problem/ building something as an example to show my work. since its a new startup what should i build to show my interest, innitiative and entruprenerial mindset. something than can be done over a day or 2

---

## Claude

Before I hand you a build list, I'm going to slow you down. There are some weak assumptions in your plan that I'd rather you fix now than after you've sunk 16 hours into the wrong demo.

### What Tolt actually is (so we're not building blind)

Tolt Innovations is a Dublin consultancy founded by Liz Bancroft-Turner. Two visible value props on their site:

1. AI systems and intelligent agents that automate sales, support, and operations for mid-market companies — principal-led, fixed-price, production-grade.
2. AI governance for Irish regulated financial services. An automated Compliance Hub that maps, monitors, and reports AI controls for Central Bank of Ireland audit readiness, framed around the CBI's 2026 Supervisory Roadmap and EU AI Act penalties of up to 7% of global turnover.
3. Liz herself is still working at Microsoft as a Digital Enterprise Sales – Data and AI Solution Specialist (Aug 2024 to present), while running Tolt and Bancroft-Turner Consulting. That's three hats.
4. The company appears to use a hybrid model: UK/Ireland-based strategy with a skilled offshore development team.

### Things I'd push you on before you write a line of code

**1. You're a data analyst pitching for a "developer" role.** Your stack (Python, SQL, R, Power BI, CatBoost, XGBoost, SHAP) is analyst/ML. It's not full-stack web dev. Build something that plays to YOUR strengths, not something that tries to fake being a software engineer. If you build a wobbly React app, you'll look worse than if you build a tight Python tool with a clean Streamlit/Gradio front-end.

**2. A 1–2 day build that's irrelevant to her business is worse than no build at all.** Initiative without judgement = noise. The signal she wants to see is "this person understood our positioning in 10 minutes of reading the site and built something that maps to it."

**3. Stop and answer these for yourself before building:**
- Has Liz already offered the internship, or are you sending this cold? (Changes the tone of the deliverable entirely.)
- Is this paid? Your Stamp 2 caps you at 20hrs/week term-time, 40hrs in holidays — you cannot do unlimited free work without it looking like you don't know your own visa rules.
- What is "developer" here? At a sub-5-person consultancy where the founder has an offshore dev team, this could mean anything from "build prototypes" to "do the work the offshore team won't." Get clarity, ideally before delivery.

**4. Don't clone her actual product.** Building a mini "Compliance Hub" is tempting but politically dumb — it can read as "I think I can do your core IP in a weekend." Build something *adjacent* and *complementary*.

### What to actually build — ranked

#### Tier 1: Build this if you want to be remembered

**EU AI Act Risk Self-Assessment Tool (interactive lead magnet)**

A web tool where an Irish financial services exec answers 8–12 questions about their AI systems (use case, data inputs, automation level, human oversight, customer impact). The tool classifies the system under EU AI Act risk tiers (unacceptable / high / limited / minimal), shows the obligations they'd be on the hook for, estimates max penalty exposure, and outputs a 1-page PDF report branded for Tolt with a "Book a consultation" CTA.

Why this is the right pick:
- Maps directly to Tolt's stated wedge (CBI 2026 + EU AI Act).
- Demonstrates you understand their *market positioning*, not just their tech.
- It's a lead-gen asset — entrepreneurial signal, not just code.
- Plays to your analyst brain (decision-tree logic, scoring) over fake-dev skills.
- Doable in 1.5 days with Streamlit/Gradio + a PDF library (e.g., ReportLab or WeasyPrint).
- You can hand her *the working tool plus a 1-page memo* on how to use it for inbound lead capture. The memo is the real moat — it shows you think like a founder, not an intern.

#### Tier 2: Solid alternative

**"Shadow AI" inventory scanner (concept demo)**

Tolt's pitch references "Shadow AI" — undocumented AI processes that firms can no longer rely on manual spreadsheets to track. Build a Python tool that ingests a CSV of company SaaS/tool usage (you can mock one up), classifies each tool as AI-powered or not, tags the EU AI Act risk tier, and outputs a CBI-flavoured "AI register" Excel file. This is more analyst-coded and less flashy, but it's a clean fit.

#### Tier 3: Skip these

- A generic chatbot demo. Everyone has built one. No signal.
- A scraped competitor analysis dashboard. Looks like a school project.
- A rebuild of any part of her existing site. Insulting.

### The actual play

Build the **EU AI Act Risk Self-Assessment Tool**. Deliver it as:
1. A live link (deploy on Streamlit Cloud, Vercel, or Hugging Face Spaces — free).
2. The GitHub repo (clean README, decisions documented).
3. A 1-page PDF memo: "Here's what this is, here's how I'd embed it on tolt.ie as a lead capture, here's the data you'd start collecting from it, here's what I'd build next if you brought me on."

That memo is the thing that gets you the offer. The code is the price of admission; the strategic framing is what separates you from every other CV in her inbox.

One thing I'm not sure about and won't pretend to be: I don't know how technical Liz wants her intern to be. Her LinkedIn reads strategy/consulting more than engineering. If you can find out (a quick LinkedIn DM asking what the role actually involves is fair game and itself signals initiative), tailor the build accordingly.

What's the actual job description — and have you spoken to Liz yet, or is this cold?

---

## Me

The conversation was done by my friend who's an intern there and she explicitly is looking for tech/developer interns. I sent an email on Friday night asking clarity of the role. Yet to get a response (Monday 5pm right now) I'm considering building something to showcase interest and initiative and present it through him

---

## Claude

Okay, three things to fix before you do anything.

**1. Friday night to Monday 5pm is not silence. It's a weekend plus six hours.**

You're pattern-matching ghosting onto normal founder response times. Liz juggles Microsoft (full-time), Tolt, and Bancroft-Turner Consulting. Founders like that often batch email on Sunday nights or Tuesday mornings. If you act anxious by Monday afternoon, you'll telegraph "this person needs constant feedback to stay calm" — which is the opposite of what someone running a lean consultancy wants in a hire. Give it until end of day Wednesday at minimum before you read anything into the silence.

**2. The "present through my friend" mechanic is the part I'd interrogate hardest.**

Right now your plan is: email founder → don't wait for reply → build something → push it through a side channel. Stop and look at how that lands from her seat. It can read as:
- "He couldn't wait two business days."
- "He's using an internal contact to jump the queue on a question he already asked me directly."
- It puts the friend in an awkward spot — now *he* has to vouch for you to his boss, on his political capital, for a job he probably wasn't asked to recruit for.

Some sharp questions you need to answer honestly:

- Did the friend actually *offer* to advocate for you, or did you decide he would? Big difference.
- Does the friend know you've already emailed Liz directly? If not, he needs to know before you hand him anything — otherwise he walks into a conversation he hasn't been briefed for.
- What does the friend *think* the best move is? He works there. He knows her communication style. Ask him before you build.

If the friend is genuinely bought in and willing to say "Liz, you should look at this guy's stuff," then yes, building something is a great use of the waiting period. If he's lukewarm or you haven't actually checked, you're about to torch a relationship.

**3. The build recommendation stands, with one adjustment.**

Now that "tech/developer intern" is confirmed, the EU AI Act Risk Self-Assessment Tool is still the right call. It hits both signals — dev chops *and* business understanding — and that combination is what wins at a tiny consultancy where the founder doesn't have time to babysit specialists.

One adjustment: since dev signal matters more now, make sure the build looks like a real piece of software, not a Jupyter notebook with a UI bolted on:

- Streamlit or Gradio is fine for the front-end (don't pretend to be a React dev in 2 days)
- But put the scoring logic in a separate Python module with type hints and at least a few unit tests
- Clean GitHub repo with a proper README — setup instructions, architecture diagram, design decisions
- Deploy it live (Streamlit Community Cloud or Hugging Face Spaces, both free)
- Use environment variables for any config — small thing, but signals you've shipped before

The thing that will actually move the needle is still the 1-page memo: "Here's what I built, here's why, here's how Tolt could use this as a lead capture asset on tolt.ie, here's what I'd build next if hired." That's the founder-brain signal she's looking for in a dev intern at a startup. Pure code monkeys are cheap; people who code AND think commercially are what she'd actually pay for.

**My actual recommended sequence:**

1. **Tonight:** Message the friend. Tell him you've emailed Liz directly on Friday, no reply yet, and you're considering building a demo. Ask him: (a) does Liz tend to be slow on email, (b) would she find a proactive demo impressive or pushy, (c) is he comfortable being the channel for it. Let *him* tell you whether to proceed.

2. **If he greenlights:** Build Tuesday and Wednesday. Send Thursday.

3. **If he hesitates:** Build anyway, but send it via a follow-up email to Liz on Thursday/Friday yourself. Subject line: "Following up on Friday's note — built a small thing for Tolt." Don't apologise for the follow-up, don't explain the gap, just lead with the work.

What did the friend actually say when you told him you were going to do this?

---

## Me

He's already spoken about me and Liz asked him to share her email to me and he's more than eager to help n advocate for me. He thinks building something is a great idea and was even okay with the idea of him showing the build I made

---

## Claude

Good. That changes the calculus on the political risk but raises the bar on everything else.

**What just changed:**

- Liz already asked your friend to pass her email to you. That's a positive signal you didn't tell me earlier — she's actively curious, not passively receiving applications.
- Your Friday email isn't sitting in a cold inbox. She's seen it or will soon. Treat the silence as routine, not negative.
- Warm intro + insider advocate is the strongest position you can be in for a small-startup hire. Most candidates would kill for this setup.

**What this means in practice — and the new risks:**

1. **The build now has to actually be good.** A warm intro raises expectations, it doesn't lower them. If you ship something half-finished, you've burned your friend's political capital AND positioned yourself as "the person who under-delivers when given a runway." The bar moved from "shows initiative" to "would I let this person ship to a paying client."

2. **Don't let your friend be the messenger. Let him be the lubricant.** There's a difference. Wrong: friend opens a tab on his laptop and shows Liz the demo. Right: friend gives Liz a heads-up — "the guy I mentioned built a small thing for you, expect an email from him" — and *you* send the email directly. Reasons:
   - She wants to evaluate you, not your friend's pitch of you.
   - Direct delivery means she can reply to you, ask you questions, see how you write. All hiring signal.
   - Having your friend present it makes it look like you're hiding. You're not.
   - If she likes it, you want the conversation to start between *you and her*, not through a relay.

3. **Reply on the Friday email thread, not a new email.** Subject line stays the same. Body: "Hi Liz, while waiting to hear back I built a small demo of an EU AI Act risk self-assessment tool — thought it might be useful as a lead-capture asset for Tolt. Live link, repo, and a 1-page note on how I'd embed it on the site: [links]. Happy to walk through it whenever works." That's it. No apology for following up, no over-explanation.

4. **Be ready for her to reply mid-build.** If she emails you Tuesday morning asking for a call, you do not say "let me finish my project first." You take the call. You mention you're already mid-build of a demo as natural conversation. Initiative shown, no awkward delay. Don't let the build become a thing you're hiding behind because you're not ready to talk to her.

**Execution priorities for the next 48 hours, in order:**

1. **Tonight (Mon):** Tell your friend the plan — he gives Liz a heads-up Wednesday morning, you send the email Wednesday afternoon. Confirm he's good with that role rather than being the deliverer.
2. **Tue:** Build the core logic + scoring rubric. Get the EU AI Act tier classification *right*. If you screw up the regulatory mapping, you look worse than if you hadn't built anything — she sells AI governance for a living, she'll spot bad classifications in 30 seconds. Sources: EUR-Lex Article 6 for risk classification, Annex III for high-risk use cases, Article 99 for penalties. Read the actual regulation, not just summaries.
3. **Wed morning:** Build the UI in Streamlit, deploy, write the README, write the 1-page memo.
4. **Wed afternoon:** Friend gives Liz the heads-up, you send the follow-up email on the Friday thread.

**One last thing to think about honestly:** Does your friend understand he's putting his name on this? If your build is sloppy, his judgement looks bad. That's not a reason to back out — it's a reason to make sure the work is tight before he sees it. Show him the demo *before* he tells Liz it's coming. If he hesitates when he sees it, that's your signal to fix things, not push through.

Are you set on the EU AI Act tool, or do you want to pressure-test the build choice once more before you start?

---

## Me

lets do it

---

## Claude

Before I hand you the spec, I'm going to verify the EU AI Act details myself rather than dump them from memory — the regulation has a phased rollout and you cannot afford a wrong classification in front of someone who sells this for a living.

[Research conducted on EU AI Act Article 6, Annex III, and CBI 2026 Supervisory Roadmap]

Research is in. The regulatory landscape has just moved in your favour: the European Commission published 148 pages of draft guidelines on Article 6 classification on 19 May 2026, with stakeholder consultation open until 23 June 2026. Eleven days ago. That means a tool that reflects the current state of the regulation is genuinely useful, not a generic explainer.

And the timing on the Irish side is just as sharp: the CBI's 2026 Regulatory & Supervisory Outlook explicitly elevates AI as a supervisory priority, with model risk, data quality, transparency, and oversight named as supervisory concerns, and firms held fully accountable for outcomes generated by AI systems including those operated by third parties. That last clause is Tolt's whole "Shadow AI" sales pitch in a single line from the regulator.

Here is the spec.

### The Build: EU AI Act Risk Self-Assessment Tool

#### What it does
A user (a compliance officer at an Irish financial services firm) answers ~15 questions about an AI system they're considering deploying. The tool classifies it under the EU AI Act risk framework, lists the obligations triggered, estimates penalty exposure, cross-references CBI 2026 supervisory expectations, and outputs a Tolt-branded PDF report.

#### Classification decision tree — this is your core logic, do not get it wrong

```
1. PROHIBITED check (Article 5)
   → Subliminal manipulation, exploiting vulnerabilities, social scoring,
     predictive policing based on profiling alone, untargeted facial
     image scraping, emotion recognition in workplace/education,
     biometric categorisation by sensitive characteristics, real-time
     remote biometric ID in public spaces (with narrow exceptions)
   → If YES on any: PROHIBITED. Outcome: banned, max penalty 7% turnover.

2. Article 6(1) safety-component check
   → Is the AI a safety component of, or itself, a product covered by
     Annex I EU harmonisation legislation (medical devices, machinery,
     toys, in vitro diagnostics, lifts, etc.)?
   → AND does that product require third-party conformity assessment?
   → If YES to both: HIGH-RISK (Article 6(1) path).

3. Article 6(2) Annex III check
   → Does intended purpose fall under any of these 8 areas:
     biometrics; critical infrastructure; education/vocational training;
     employment & worker management; essential private services
     (including credit scoring & insurance pricing) and public services;
     law enforcement; migration & border; justice & democratic processes.
   → If NO: classified as LIMITED or MINIMAL risk (apply transparency
     obligations if it interacts with humans / generates content).
   → If YES: provisionally high-risk, proceed to filter.

4. Article 6(3) filter check (only if step 3 hit)
   → Does the system meet ANY of these four conditions:
     (a) narrow procedural task only
     (b) improves the result of a previously completed human activity
     (c) detects decision-making patterns or deviations without
         replacing/influencing prior human assessment
     (d) preparatory task only
   → BLOCKER: if the system performs profiling of natural persons,
     filter is unavailable regardless of conditions met.
   → If filter applies: NOT HIGH-RISK, but provider must document
     assessment (Art 6(4)) and register under Art 49(2).
   → If filter does not apply: HIGH-RISK confirmed.
```

Source the four filter conditions verbatim from the Commission's draft guidelines: narrow procedural task; improve the result of a previously completed human activity; detect decision-making patterns or deviations without replacing or influencing prior human assessment; perform a preparatory task to an assessment. Quote them in the tool. Make clear the exemptions must be interpreted narrowly per Article 6(3).

#### Output: what the user sees + the PDF

For each classification, generate:
- **Risk tier** (Prohibited / High-risk / Limited / Minimal)
- **Pathway** ("Classified high-risk via Annex III, area: employment; Article 6(3) filter not applicable due to profiling")
- **Obligations triggered** — cite articles. For high-risk: Art 9 (risk mgmt), Art 10 (data governance), Art 11 (technical documentation), Art 12 (record-keeping), Art 13 (transparency), Art 14 (human oversight), Art 15 (accuracy/robustness/cybersecurity)
- **Max penalty exposure** under Article 99 — €35M or 7% turnover (Art 5 prohibited), €15M or 3% turnover (high-risk obligations), €7.5M or 1% (incorrect info to authorities)
- **CBI overlay** — if user identifies as regulated FS firm, add a section mapping obligations to CBI 2026 RSO expectations on model governance, explainability, human oversight, third-party AI accountability
- **Action checklist** — concrete next 5 steps based on tier
- **PDF download** with Tolt branding (place Tolt logo top, your name + date footer, "Prepared by [name] as a demonstration tool for Tolt Innovations" in fine print)

#### Tech stack — and why I'm telling you not to overbuild

```
Frontend:  Streamlit
Backend:   Pure Python (classification module separate from UI)
PDF:       ReportLab or WeasyPrint
Hosting:   Streamlit Community Cloud (free, custom subdomain)
Repo:      GitHub, public
Tests:     pytest, 8-10 unit tests on the classifier covering edge cases
```

**Why Streamlit and not a "real" React/FastAPI build:** You have 1.5 days. You're not a frontend developer. A wobbly hand-rolled React app will look worse than a clean Streamlit app with a tight backend module and proper tests. The signal you want to send is "I can ship working software with judgement," not "I can fake being a full-stack dev." Liz has 25+ years in tech — she will see through the latter immediately.

**What lifts it above "just a Streamlit app":**
1. The classifier is a separate, typed, tested Python module (`risk_classifier.py`) that could be imported into any other application — including a FastAPI service later. Make this clear in the README.
2. Every decision in the classifier cites the relevant EU AI Act article inline as a comment. This is the killer detail. It tells Liz you read the regulation, not just a blog post.
3. The PDF report looks polished, not auto-generated.
4. The README shows architecture, decisions, what you'd build next.

#### File structure

```
tolt-ai-act-tool/
├── README.md                  # architecture, decisions, demo link, "what next"
├── app.py                     # Streamlit UI only
├── risk_classifier.py         # core logic, fully typed, no UI imports
├── obligations.py             # mapping risk tier → article obligations
├── report_generator.py        # PDF generation
├── data/
│   └── annex_iii_use_cases.json   # structured list of use cases
├── tests/
│   └── test_classifier.py     # 8-10 cases incl. edge cases
├── requirements.txt
└── assets/
    └── tolt_logo.svg          # only if you can grab it cleanly
```

#### Build sequence

**Tuesday morning (3-4 hrs):** Write `risk_classifier.py` and `obligations.py` first. Cite article numbers in comments. Write the tests alongside. No UI yet.

**Tuesday afternoon (3-4 hrs):** Streamlit app — five sections matching the decision tree. Don't try to make it pretty yet, just functional.

**Wednesday morning (3-4 hrs):** PDF report generation. Polish UI — typography, spacing, Tolt colour scheme. Deploy to Streamlit Community Cloud. Write the README.

**Wednesday afternoon (2 hrs):** Write the memo. Test the live link from a different browser/device. Friend gives Liz a heads-up. You send the email.

If anything slips, cut the CBI overlay first — it's the cherry on top, not the cake.

#### The memo — 1 page, this is what actually sells the build

```
TO:      Liz Bancroft-Turner, Tolt Innovations
FROM:    Advaith A Bijoor
DATE:    [Wed]
RE:      EU AI Act Risk Self-Assessment Tool — proof of concept

What it is
A working tool that lets a compliance officer classify any AI system under
the EU AI Act risk framework in under 5 minutes, get the obligations and
penalty exposure, and download an audit-ready PDF. Reflects the Commission's
draft Article 6 guidelines published 19 May 2026.

Live: [URL]
Code: [GitHub URL]

Why I built it
Your site flags the Shadow AI problem and the CBI 2026 supervisory mandate.
Most firms don't know which of their AI systems are high-risk under the Act
— they need a fast, defensible first-pass screen before bringing in a
consultant. This tool is that screen.

How Tolt could use it
1. Embed it on tolt.ie as a free lead-capture asset. Every PDF download
   captures email + firm + use case + risk tier — qualified inbound.
2. Use it in client kickoffs as a structured intake for AI inventory
   discovery. Saves billable hours.
3. White-label per client as a self-service portal for ongoing compliance.

What I'd build next if I joined
- Article 6(3) filter walkthrough as a guided UI rather than checklist
- Persistent client AI register (the "Evidence Layer" Tolt sells)
- CBI-specific reporting templates
- Integration with the draft Commission guidelines as they finalise after
  the 23 June 2026 consultation close

Happy to walk through anything. I'm in Dublin.
```

That memo is the difference between "intern candidate" and "person I want to hire before someone else does."

### Sources used (verify yourself before you cite anything in the build)

- EU AI Act Article 6 — https://artificialintelligenceact.eu/article/6/
- Annex III — https://artificialintelligenceact.eu/annex/3/
- Commission draft guidelines (19 May 2026) — https://digital-strategy.ec.europa.eu/en/library/draft-commission-guidelines-classification-high-risk-ai-systems
- Article 6(3) filter analysis — https://www.addleshawgoddard.com/en/insights/insights-briefings/2026/technology/eu-ai-act-draft-commission-guidelines-classification-high-risk-ai-systems/
- CBI 2026 RSO (PDF) — https://www.centralbank.ie/docs/default-source/publications/regulatory-and-supervisory-outlook-reports/regulatory-supervisory-outlook-report-2026.pdf
- Pinsent Masons analysis of CBI 2026 priorities — https://www.pinsentmasons.com/out-law/analysis/central-bank-ireland-2026-supervisory-priorities

Two things I'm genuinely uncertain about and you should sanity-check before shipping:
1. The Article 99 penalty figures I quoted (€35M/7%, €15M/3%, €7.5M/1%) match my recall but I haven't pulled them from EUR-Lex in this session — open Article 99 directly and verify the exact numbers before the tool reports them.
2. The eight Annex III areas I listed — I'm confident on the categories but the sub-use-cases inside each (e.g. which specific employment uses qualify) have nuance worth checking against the actual Annex III text before you encode them.

Get those two right and the rest of the build is defensible.

Want me to draft the actual `risk_classifier.py` skeleton with the decision tree implemented, or do you want to write it yourself and have me review?

---

## Me

lets put all our focus on delivering the product asap and if its not perfect that's okay as it can be something i can mention im working on. give me a road map of what to do in exact order with details as clear as possible

---

## Claude

Stopping the debate. Here's the roadmap. Follow it in order. Where I give time estimates, those are budgets — if you blow past them, cut features, not corners on the next step.

**Total budget: ~16 hours of focused work over Tue + Wed. If you're running behind, follow the CUT instructions in each phase.**

---

### PHASE 0 — Pre-flight (do this tonight, 30 min)

```bash
mkdir tolt-ai-act-tool && cd tolt-ai-act-tool
git init
python3 -m venv venv
source venv/bin/activate
pip install streamlit reportlab pytest
pip freeze > requirements.txt
```

Create these empty files (will fill them in order):
```
touch app.py risk_classifier.py obligations.py report_generator.py README.md
mkdir tests && touch tests/test_classifier.py
mkdir data && touch data/annex_iii.json
```

Push the empty scaffold to GitHub now. Repo name: `eu-ai-act-risk-tool`. Make it public. This way you're committing in small chunks throughout — no "first commit at 11pm Wednesday" red flag in the history.

**Also tonight:** Open Article 99 of the EU AI Act on EUR-Lex or https://artificialintelligenceact.eu/article/99/, copy the exact penalty figures into a notes file. Open Annex III, copy the 8 areas and their sub-use-cases into `data/annex_iii.json`. This is "boring research" time — don't do it during your build hours tomorrow.

---

### PHASE 1 — Build the brain (Tue morning, 4 hours max)

#### Step 1.1 — `data/annex_iii.json` (45 min)

Structure each Annex III area as:
```json
{
  "areas": [
    {
      "id": "employment",
      "name": "Employment, workers management, access to self-employment",
      "annex_reference": "Annex III(4)",
      "use_cases": [
        "Recruitment / selection of natural persons (job ads, screening, evaluation of candidates)",
        "Decisions affecting terms of work-related relationships, promotion, termination",
        "Task allocation based on behaviour or personal traits",
        "Monitoring and evaluation of performance"
      ]
    }
  ]
}
```

Do this for all 8 areas. Source: artificialintelligenceact.eu/annex/3. **45 minutes, no thinking — just transcribe.**

#### Step 1.2 — `risk_classifier.py` (2 hours)

Single function, fully typed. Here's the skeleton — fill in the body:

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class RiskTier(Enum):
    PROHIBITED = "Prohibited"
    HIGH_RISK = "High-risk"
    LIMITED = "Limited risk"
    MINIMAL = "Minimal risk"

@dataclass
class AssessmentInput:
    # Article 5 — prohibited practices
    uses_subliminal_manipulation: bool
    exploits_vulnerabilities: bool
    social_scoring: bool
    predictive_policing_profiling: bool
    untargeted_facial_scraping: bool
    emotion_recognition_workplace_education: bool
    biometric_categorisation_sensitive: bool
    realtime_remote_biometric_id: bool

    # Article 6(1) — safety component path
    is_safety_component_annex_i: bool
    requires_third_party_conformity: bool

    # Article 6(2) — Annex III path
    annex_iii_areas: list[str]  # IDs from annex_iii.json, empty if none

    # Article 6(3) — filter
    narrow_procedural_task: bool
    improves_completed_human_activity: bool
    detects_patterns_no_replacement: bool
    preparatory_task_only: bool
    performs_profiling: bool  # blocker for filter

    # Context
    is_regulated_fs_firm: bool
    intended_purpose: str

@dataclass
class AssessmentResult:
    tier: RiskTier
    pathway: str           # e.g. "Article 6(2) — Annex III area: employment"
    article_citations: list[str]
    obligations: list[str]
    max_penalty: str
    cbi_overlay: Optional[list[str]]
    next_steps: list[str]

def classify(input: AssessmentInput) -> AssessmentResult:
    # STEP 1: Article 5 — prohibited
    if any([
        input.uses_subliminal_manipulation,
        input.exploits_vulnerabilities,
        # ... all 8 prohibited checks
    ]):
        return AssessmentResult(
            tier=RiskTier.PROHIBITED,
            pathway="Article 5 — Prohibited AI practice",
            article_citations=["Article 5", "Article 99(3)"],
            # ...
        )

    # STEP 2: Article 6(1) — safety component
    if input.is_safety_component_annex_i and input.requires_third_party_conformity:
        return _build_high_risk_result(
            pathway="Article 6(1) — Safety component of regulated product",
            ...
        )

    # STEP 3: Article 6(2) — Annex III
    if input.annex_iii_areas:
        # STEP 4: Article 6(3) filter check
        filter_conditions_met = any([
            input.narrow_procedural_task,
            input.improves_completed_human_activity,
            input.detects_patterns_no_replacement,
            input.preparatory_task_only,
        ])

        if filter_conditions_met and not input.performs_profiling:
            return AssessmentResult(
                tier=RiskTier.LIMITED,
                pathway=f"Annex III hit ({input.annex_iii_areas}) but Art 6(3) filter applies",
                article_citations=["Article 6(2)", "Article 6(3)", "Article 6(4)", "Article 49(2)"],
                obligations=["Document the Art 6(3) assessment (Art 6(4))", "Register under Art 49(2)"],
                # ...
            )

        return _build_high_risk_result(
            pathway=f"Article 6(2) — Annex III area: {input.annex_iii_areas}",
            ...
        )

    # STEP 5: Default — limited or minimal
    return AssessmentResult(tier=RiskTier.LIMITED, ...)
```

Every branch returns the article citations. **Comment every decision with the article number.** That comment trail is the killer detail Liz will see when she opens your repo.

#### Step 1.3 — `tests/test_classifier.py` (1 hour)

Five tests. No more. Names should describe what they assert:

```python
def test_subliminal_manipulation_is_prohibited()
def test_credit_scoring_for_natural_persons_is_high_risk_via_annex_iii()
def test_medical_device_ai_is_high_risk_via_article_6_1()
def test_recruitment_ai_with_profiling_cannot_use_filter_exemption()
def test_marketing_chatbot_is_limited_risk()
```

These tests double as documentation. Liz will read them.

#### Step 1.4 — `obligations.py` (15 min)

Just a dict mapping `RiskTier` → list of obligation strings with article citations. Trivial. Don't overthink.

**CUT IF BEHIND:** Drop to 3 tests instead of 5. Skip the CBI overlay logic.

**CHECKPOINT (Tue lunch):** `pytest` passes. You can import classifier and call `classify()` from a Python REPL and get sensible output. **If this isn't done by 1pm Tuesday, you're already behind.**

---

### PHASE 2 — Wire up the UI (Tue afternoon, 4 hours max)

#### Step 2.1 — `app.py` (3 hours)

Streamlit, single file, five sections matching the decision tree. Use `st.session_state` to carry data between sections. Layout:

```python
import streamlit as st
from risk_classifier import classify, AssessmentInput

st.set_page_config(page_title="EU AI Act Risk Self-Assessment", layout="wide")

st.title("EU AI Act Risk Self-Assessment Tool")
st.caption("Reflects Commission draft guidelines published 19 May 2026")

# Section 1: System identification
st.header("1. Your AI system")
intended_purpose = st.text_area("Intended purpose (1-2 sentences)")
is_regulated_fs = st.checkbox("My organisation is a CBI-regulated financial services firm")

# Section 2: Article 5 prohibited check
st.header("2. Prohibited practices (Article 5)")
st.markdown("Tick any that apply. **If any apply, the system is banned outright.**")
prohibited_flags = {
    "subliminal": st.checkbox("Uses subliminal techniques beyond a person's consciousness"),
    "vulnerabilities": st.checkbox("Exploits vulnerabilities due to age, disability, social/economic situation"),
    # ... all 8
}

# Section 3: Article 6(1) safety component
st.header("3. Safety component check (Article 6(1))")
# ...

# Section 4: Annex III multiselect
st.header("4. Annex III use cases (Article 6(2))")
# Load annex_iii.json, render as expanders with checkboxes per use case
# ...

# Section 5: Article 6(3) filter (only show if section 4 hit)
# ...

# Submit button
if st.button("Classify this AI system", type="primary"):
    result = classify(AssessmentInput(...))
    st.session_state.result = result

# Render result
if "result" in st.session_state:
    render_result(st.session_state.result)
    st.download_button("Download PDF report", data=generate_pdf(...))
```

Use `st.expander` for each Annex III area so the page isn't a wall of checkboxes. Use `st.info`, `st.warning`, `st.error` to colour-code the result tier.

#### Step 2.2 — End-to-end smoke test (1 hour)

Run through the full flow as four hypothetical users:
1. A bank deploying AI for credit scoring → should classify HIGH-RISK via Annex III area "essential services"
2. A retailer using AI for product recommendations → MINIMAL
3. An insurer using AI for life insurance pricing → HIGH-RISK
4. A firm wanting to deploy AI emotion recognition in their call centre → PROHIBITED

Fix any bugs that surface. **Don't polish the UI yet.**

**CUT IF BEHIND:** Skip Section 1 free-text fields. Skip session state, just compute on every interaction.

**CHECKPOINT (Tue 7pm):** Tool works end-to-end locally. `streamlit run app.py` and you can complete the full flow. **If not done by 7pm, drop the PDF feature tomorrow.**

---

### PHASE 3 — PDF + deploy + polish (Wed morning, 4 hours max)

#### Step 3.1 — `report_generator.py` (2 hours)

ReportLab. Don't try to make this beautiful. Make it readable and professional.

```python
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

def generate_pdf(result, intended_purpose, organisation_name=None) -> bytes:
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()

    story = []
    story.append(Paragraph("EU AI Act Risk Assessment Report", styles['Title']))
    story.append(Paragraph(f"Generated: {date.today()}", styles['Normal']))
    story.append(Spacer(1, 12))

    story.append(Paragraph(f"<b>System purpose:</b> {intended_purpose}", styles['Normal']))
    story.append(Paragraph(f"<b>Risk tier:</b> {result.tier.value}", styles['Heading2']))
    story.append(Paragraph(f"<b>Classification pathway:</b> {result.pathway}", styles['Normal']))

    # Obligations section
    story.append(Paragraph("Obligations triggered", styles['Heading3']))
    for ob in result.obligations:
        story.append(Paragraph(f"• {ob}", styles['Normal']))

    # Penalty exposure
    story.append(Paragraph("Maximum penalty exposure (Article 99)", styles['Heading3']))
    story.append(Paragraph(result.max_penalty, styles['Normal']))

    # Footer
    story.append(Spacer(1, 36))
    story.append(Paragraph(
        "<i>This assessment is a first-pass screen and does not constitute legal advice. "
        "Prepared as a demonstration tool by Advaith A Bijoor for Tolt Innovations.</i>",
        styles['Italic']
    ))

    doc.build(story)
    return buffer.getvalue()
```

#### Step 3.2 — Deploy to Streamlit Community Cloud (45 min)

1. Go to https://share.streamlit.io, sign in with GitHub
2. "New app" → point at your repo, branch `main`, main file `app.py`
3. Deploy. Wait 3-5 minutes.
4. You get a URL like `eu-ai-act-risk-tool.streamlit.app`. Test it from your phone (different network).

If deploy fails: 90% of the time it's missing dependencies in `requirements.txt`. Run `pip freeze > requirements.txt` and push.

#### Step 3.3 — Write `README.md` (1 hour)

Structure (use exactly these headings):
```markdown
# EU AI Act Risk Self-Assessment Tool

[Live demo](URL) • Built for Tolt Innovations

## What this does
[2-3 sentences. Plain English.]

## Why it exists
[3-4 sentences linking to CBI 2026 RSO + Commission's May 2026 draft guidelines]

## How the classification works
[Paste the decision tree from the spec. This is the audit trail.]

## Architecture
- `risk_classifier.py` — pure logic, no UI dependencies, fully tested
- `app.py` — Streamlit UI
- `report_generator.py` — PDF output
- `data/annex_iii.json` — structured Annex III reference data

## Running locally
[3 lines: venv, pip install, streamlit run]

## What this is not
A legal opinion. A substitute for compliance counsel. A complete implementation
of the EU AI Act framework.

## What I'd build next
[5 bullets — same as the memo. Shows you're thinking forward.]

## Sources
[Bullet list with links to EUR-Lex, Commission guidelines, CBI 2026 RSO]
```

**CUT IF BEHIND:** Skip PDF entirely — display results in the app only, mention PDF as "next step" in the memo. This is the single biggest time-saver if you're behind.

**CHECKPOINT (Wed 1pm):** Live URL works. Friend can open it on his phone. README is on GitHub.

---

### PHASE 4 — Send it (Wed afternoon, 2 hours)

#### Step 4.1 — Friend heads-up (15 min)
Message him: "I'm sending Liz a follow-up on the Friday email with a demo I built. Going out around 3pm. Can you give her a heads-up before then?"

#### Step 4.2 — Final QA (45 min)
- Open the live URL in incognito mode. Click through full flow.
- Open the GitHub repo logged out. Make sure repo is public.
- Read your README out loud. Fix anything that sounds bad.
- Test PDF download (if you kept it).

#### Step 4.3 — Write the email + memo (45 min)

Reply on the Friday thread. Subject stays the same. Body:

```
Hi Liz,

While waiting to hear back I spent yesterday and today building a small
demo — an EU AI Act Risk Self-Assessment tool. Thought it might be useful
as a lead-capture asset for Tolt given the CBI's 2026 supervisory priorities
and the Commission's draft Article 6 guidelines from May.

Live: [URL]
Repo: [GitHub URL]
1-page memo on how I'd embed it on tolt.ie: [attached or inline below]

It's a first version, not a finished product — I'm sure there are edges
to refine — but it works end-to-end and I wanted to show what I'd build
unprompted rather than just describe it.

Happy to walk through it whenever works.

Best,
Advaith
```

The memo from my previous message goes either inline below the email or as a PDF attachment. Don't make it a Google Doc — friction.

#### Step 4.4 — Send. Close the laptop. (15 min)

Do not edit the email five times. Send it. Tell your friend it's gone. Then walk away from your computer for a few hours.

---

### The "everything is on fire" fallback

If by Wednesday lunch you have NO working tool, here is the minimum acceptable delivery:

- A clean GitHub repo with `risk_classifier.py` working and tested
- A README with the decision tree, architecture, and "what I'd build next"
- Email Liz with: "I started building this — here's the logic and architecture, here's where I'd take it next, didn't want to ship a UI that wasn't ready"

That is still a respectable signal. It's "I think before I code." Worse than shipping the full thing, but not embarrassing.

---

Start Phase 0 now. Don't reply asking for clarification on anything in Phases 1-4 until you've actually started Phase 0 — most of your questions will dissolve once you're in the code.

---

*End of conversation. Get to work.*
