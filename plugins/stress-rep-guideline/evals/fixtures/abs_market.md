SYNTHETIC TEST DOCUMENT — fictional study written for evaluating the stress-rep-guideline skill; not real research

# Adoption of a mobile payment service among consumers and firms: an agent-based simulation

D. Nobody and E. Nonexistent — Imaginary Business School, University of Elsewhere (fictional)

## 1. Purpose of the model

A regional bank (fictional) plans to launch a mobile payment service and wants to know whether a one-off subsidy to the first firms that accept the service would speed up adoption among consumers. Because adoption depends on who a consumer's acquaintances are and which shops they use, we built an agent-based simulation (ABS) of consumers and firms connected through a social network. The model is intended to compare launch strategies for this service; it is not a general diffusion model.

## 2. Model outputs

The system-level output that emerges from agent interactions is the adoption curve: the share of consumers who have adopted the service in each week. We report two quantitative measures: (a) the adoption share at week 52, and (b) the time to 50 % adoption (weeks; set to 104 if not reached). Both are computed at the end of each weekly step from the agents' adoption state. Across replications we report the mean and a 95 % interval given by the 2.5th and 97.5th percentiles of the replication values.

## 3. Experimentation aims

The model was used for scenario-based analysis of two launch strategies: L0, no subsidy (base case), and L1, a subsidy that lowers the acceptance threshold of the 10 largest firms to zero in week 1. The rationale is the bank's proposal to subsidise large firms first. We did not test theories, run a designed experiment, or use simulation optimisation.

## 4. Model logic

### 4.1 Overview diagram

Figure 1 is a state chart with the two consumer states (non-adopter, adopter) and the two firm states (not accepting, accepting) and the transitions between them; Figure 2 is a flow chart of one weekly step.

### 4.2 Base model logic

In each weekly step, every consumer observes the share of adopters among its network neighbours and the share of accepting firms among the firms it shops at; it adopts if a weighted sum of the two shares exceeds its personal threshold. Every firm observes the share of adopting consumers among its customers and starts accepting if that share exceeds the firm's threshold, after which it adjusts its service fee once (see 4.4). Adoption is permanent for consumers and firms. Intermediate calculations per step: neighbour adoption share, customer adoption share, firm acceptance share, and the weighted social pressure p_i = 0.6 · neighbour share + 0.4 · accepting-firm share.

### 4.3 Scenario logic

L1 differs from L0 only in the initial threshold value of the 10 largest firms (set to 0 instead of the sampled value); the step logic is identical.

### 4.4 Algorithms

Firms set their service fee with the following heuristic, which mimics the manual pricing rule used by the bank's merchant team:

```
on first acceptance by firm j:
    if share of adopting customers of j >= 0.5: fee_j = 1.5 %
    else: fee_j = 2.0 %
    fee_j is fixed thereafter
```

### 4.5 Components

**Environment.** There is no spatial environment. Agents live on an abstract social network generated at the start of each run as a Watts–Strogatz small-world graph with n = 5,000 consumer nodes, mean degree 6 and rewiring probability 0.1; each consumer is additionally linked to 3 firms drawn with probability proportional to firm size.

**Agents.** Consumers (n = 5,000): states non-adopter / adopter; transition non-adopter → adopter when p_i > threshold_i; attributes income (used only to sample the threshold), threshold_i, list of neighbours, list of firms. Firms (n = 50): states not accepting / accepting; transition when customer adoption share > threshold_j; attributes size, threshold_j, fee_j. Decision rules are the threshold comparisons stated in 4.2 (equation form). Data accessed: consumers read the adoption state of neighbours and the acceptance state of their firms; firms read the adoption state of their customers. Objectives: none beyond the threshold rules; agents do not optimise. There are no agent groups or group membership rules, and agents do not predict future events.

**Interaction topology.** Consumers interact only with their network neighbours and their 3 linked firms; firms interact with their customers. Each week every consumer reads all of its neighbours (no sampling of recipients). All interactions occur once per weekly step. Concurrent decisions in the same step are resolved by synchronous updating: all agents read the state at the end of the previous week, so the order of activation does not affect the outcome. Interactions depend on agent states (only adopters and accepting firms exert pressure); there is no environment state. The pressure equation and the step pseudo-code are given in 4.2 and Figure 2.

**Entry / exit.** The populations of consumers (n = 5,000) and firms (n = 50) are fixed for the duration of a run; no agents are created or destroyed, so rules for agent entry and exit are not applicable to this model.

## 5. Data

### 5.1 Data sources

- Consumer survey commissioned by the bank, March 2023 (n = 1,200 respondents): income and stated willingness to adopt, used to fit the threshold distribution.
- Regional firm registry, December 2023 (n = 50 firms in the target district): firm size (annual transactions), used for the firm-size weights.
- Published diffusion studies (Nobody et al., 2020) for the weights 0.6 / 0.4 in the pressure equation.

### 5.2 Pre-processing

Survey responses were re-weighted to the district's income distribution, and 14 respondents with incomplete answers were removed before fitting.

### 5.3 Input parameters

| Parameter | Value / distribution | Base case | L1 |
|---|---|---|---|
| Consumer threshold_i | Beta(2, 5) rescaled to [0.1, 0.9], fitted by maximum likelihood to the survey | sampled per agent | same |
| Firm threshold_j | Uniform(0.2, 0.6) | sampled per agent | 0 for the 10 largest firms |
| Pressure weights | 0.6 (neighbours), 0.4 (firms) | fixed | same |
| Network: n, mean degree, rewiring | 5,000; 6; 0.1 | fixed | same |
| Initial adopters | 2 % of consumers, chosen at random | fixed | same |

No parameter is time- or space-dependent and no correlation between parameters is modelled. The Beta family was chosen over the normal and uniform families because it gave the highest likelihood on the survey data.

### 5.4 Assumptions

We assume: (i) adoption is permanent; (ii) each consumer shops at exactly 3 firms; (iii) consumers weight neighbour and firm influence 0.6 / 0.4; (iv) firms never withdraw from the service.

## 6. Experimentation

### 6.1 Initialisation

Each run starts with 5,000 consumers of which 2 % (100, chosen at random) are adopters and the rest non-adopters, and 50 firms all not accepting. Thresholds are sampled per agent from the distributions in Table 5.3, and the network is generated as described in 4.5, so initialisation is stochastic (different in every replication).

### 6.2 Run length

Each replication runs for 104 weeks with a time step of one week.

### 6.3 Estimation approach

The model is stochastic (random network, random thresholds, random initial adopters). Each scenario was run for 100 replications, and the reported intervals are the 2.5th and 97.5th percentiles across replications.

## 7. Implementation

### 7.1 Software

Python 3.10.12 with Mesa 2.1.1 and NetworkX 3.1, on Ubuntu 22.04.3 LTS (kernel 6.2.0).

### 7.2 Random sampling

All random draws use NumPy's default generator (PCG64) via numpy.random.default_rng; replication r uses seed r (r = 1 … 100) for both the network generation and the agent attributes.

### 7.3 Model execution

Time is modelled in fixed weekly steps. Within a step the scheduler activates consumers then firms; because updating is synchronous (all agents read the previous week's state), the activation order does not change results. The model is not parallel or distributed.

### 7.4 System specification

Hardware specification: not applicable for a model of this size.

## 8. Model availability

The complete model code, the fitted parameter files and the analysis notebooks are available at https://github.com/example-fictional/mobile-pay-abs and archived at Zenodo (doi:10.5281/zenodo.0000000, fictional).

## 9. Results (summary)

Under L0, 50 % adoption was reached in a median of 61 weeks; under L1 in 38 weeks. The adoption share at week 52 rose from 41 % (95 % interval 36–47 %) to 63 % (57–68 %).
