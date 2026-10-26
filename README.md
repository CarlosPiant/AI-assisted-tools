# AI-assisted tools

AI tools for academic research built on Claude. Each tool is a self-contained
[Claude Code](https://claude.com/claude-code) plugin: install only the ones you need, and each carries its
own documentation, evaluation, and licence notes.

| Plugin | What it does |
|---|---|
| [**skill-generator**](plugins/skill-generator/) | Turns a manuscript, methods paper, framework, guideline, or tutorial into a tested Claude Code skill: a design brief with page-level locators, the skill itself, a benchmark against Claude without the skill, and a usage guide with a worked example. |
| [**stress-rep-guideline**](plugins/stress-rep-guideline/) | Audits the write-up of a discrete-event, system dynamics, agent-based, or hybrid simulation study against the STRESS reporting checklist (Monks et al. 2019), reporting each of the 20 items with quoted evidence. Built with skill-generator; benchmark 0.92 with the skill against 0.33 without. |
| [**cheers-checklist**](plugins/cheers-checklist/) | Audits the report of a health economic evaluation (model-based, trial-based, or cost analysis) against the 28-item CHEERS 2022 checklist (Husereau et al. 2022), with quoted evidence and a paste-ready submission table. Built with skill-generator; benchmark 0.87 with the skill against 0.37 without. |

## Install

In Claude Code, add this repository as a plugin marketplace once, then install the plugins you want:

```text
/plugin marketplace add CarlosPiant/AI-assisted-tools
/plugin install skill-generator@ai-assisted-tools
/plugin install stress-rep-guideline@ai-assisted-tools
/plugin install cheers-checklist@ai-assisted-tools
```

Update later with `/plugin marketplace update ai-assisted-tools`. Requirements are listed in each
plugin's README.

## Repository layout

```text
.claude-plugin/marketplace.json   # lists the plugins
plugins/
├── skill-generator/              # skill + bundled agent + references
├── stress-rep-guideline/         # skill + references + scripts + evals
└── cheers-checklist/             # skill + references + scripts + evals
```

## Licence

Original work © 2026 Carlos Pineda, under the [PolyForm Noncommercial License 1.0.0](LICENSE): free for
research, teaching, and personal use; commercial use needs permission. Third-party material keeps its own
licence; see each plugin's `NOTICE` file. The STRESS checklist text is CC BY 4.0, © its authors; the CHEERS 2022 checklist text is CC BY 4.0, © ISPOR.
