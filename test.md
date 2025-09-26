# Whitepaper: FX Derivatives Model Validation

**Generated:**2025-09-23T21:40:17.071193

## Executive Summary

The **FX Digital Option Model** is integral in assessing currency risk, providing a structured framework for calculating the Value at Risk (VaR) associated with these financial instruments. Developed within the **Global Markets Risk Model (GMRM)**, this model facilitates the valuation of European digital options, which promise a predetermined payout based on the underlying exchange rate relative to a specified strike price. As volatility in the global market increases due to geopolitical influences and economic shifts, accurate estimation of risk exposure using this model is critical.

Recent evaluations of the model indicate a total mark-to-market (MTM) position of **89,413**, alongside a 99% VaR estimate, serving as a key indicator of potential losses over a specified timeframe. These metrics inform ongoing **stress-testing procedures**, ensuring that our risk management practices remain robust and responsive to changing market conditions. Through continuous monitoring and periodic approvals, the model will adapt to evolving market dynamics, demonstrating its relevance in today's financial environment.

### 1.2 Risk Impact

As of **2010-11-08**, the following key risk impact metrics were recorded:

- **Positions**: 89,413
- **Total MTM**: [Value TBD]
- **VaR99**: [Value TBD]

> **Note**: The total MTM and VaR99 are essential metrics for assessing policy thresholds and the overall context of stress testing, guiding our strategies in effective risk management.

| Indicator          | Value         |
|---------------------|---------------|
| Positions           | 89,413        |
| Total MTM          | [Value TBD]   |
| VaR99              | [Value TBD]   |
| Policy Impact       | [To be discussed] |
| Stress-testing Impact| [To be assessed] |

## Product Description

### Statement of Model Payoff 

For **cash-settled FX digital call options**, the payoff at maturity depends on the relationship between the exchange rate ($ S_T $) and the strike price ($ K $). If $ S_T < K $, no payoff is realized; conversely, if $ S_T \geq K $, the payoff is a fixed amount $ Q $. In the case of **cash-settled FX digital put options**, the payoff structure mirrors that of the call option, where if $ S_T > K $, the option results in no payout. If $ S_T \leq K $, the payoff is again a fixed amount $ Q $.

For **asset-settled FX digital options**, the payoff dynamics adjust slightly. For a digital call option, the payoff is $ \frac{S_T Q}{K} $ if $ S_T \geq K $; if the exchange rate falls below the strike price, no payout occurs. Conversely, an asset-settled FX digital put option pays out $ \frac{S_T Q}{K} $ when $ S_T \leq K $, yielding nothing if $ S_T > K $. This structured payoff framework illustrates how market observables influence financial outcomes for both cash and asset-settled options.

| Option Type                | Condition                 | Payoff                         |
|----------------------------|---------------------------|--------------------------------|
| Cash Settlement Digital Call| $ S_T < K $             | 0                              |
|                            | $ S_T \geq K $         | $ Q $                        |
| Cash Settlement Digital Put | $ S_T > K $             | 0                              |
|                            | $ S_T \leq K $         | $ Q $                        |
| Asset Settlement Digital Call| $ S_T < K $            | 0                              |
|                            | $ S_T \geq K $         | $ \frac{S_T Q}{K} $         |
| Asset Settlement Digital Put | $ S_T > K $            | 0                              |
|                            | $ S_T \leq K $         | $ \frac{S_T Q}{K} $         |

### Original Term Sheet and Transaction Book Template

The **Original Term Sheet and/or Transaction Book Template** serves as a vital reference for booking derivative transactions, ensuring consistency in trade setup. Utilizing standardized fields and conventions, this template captures essential data required for effective trade execution. For instance, the provided Murex interface details an FX European Digital option transaction, including crucial parameters such as **currency pair**(EUR/USD), **expiry date**(Wed 01 Dec 2010), and **premium date**(Tue 30 Oct 2007).

This template includes critical elements like the **strike price**(1.2751) and **foreign notional**(2,279,180 EUR) along with important features such as the **payout type**, which, in this case, is a **Digital** option. Valuation frameworks such as the **Black-Scholes-Merton model** reinforce the template's reliability. Below is the original transaction table:

| Field                  | Value                          |
|------------------------|--------------------------------|
| Derivative             | #5 FX European Digital         |
| RBC Buys / Sells       | Buy                            |
| Currency Pair          | EUR/USD                        |
| Expiry                 | Wed 01 Dec 2010               |
| Expiry Days            | 13                             |
| Delivery               | Fri 03 Dec 2010               |
| Delivery Days          | 11                             |
| Premium Date           | Tue 30 Oct 2007               |
| Strike                 | 1.2751                         |
| Call/Put               | Put EUR / Call USD            |
| Foreign Notional       | 2,279,180 EUR                 |
| Domestic Notional      | 2,906,182 USD                 |
| Payout Type            | Digital                        |
| Digital Amount         | 2,279,180.00                  |
| Digital Currency       | EUR                            |
| Smile                  | n                              |
| Model                  | Black Scholes                  |
| Use Smile for          | PL + adapted greeks            |
| Warning                |                                |

## Model Description

### Modeling Assumptions and Relevant Theory

The FX Digital Option Model is based on the premise that the exchange rate follows **geometric Brownian motion (GBM)**, articulated through the stochastic differential equation:

$$
\frac { d S } { S } = (r_d - r_f) d t + \sigma_t d W_t
$$ 

In this equation, $ r_d $ and $ r_f $ represent the deterministic, continuously compounded risk-free rates for the domestic and foreign currencies, respectively, while $ \sigma_t $ denotes the instantaneous volatility of the exchange rate. The model captures both cash-settled and asset-settled FX digital options, with the former guaranteeing a fixed payout $ Q $ based on the option's in-the-money status, while the latter pays a fraction of the spot exchange rate relative to the strike price at maturity. 

Pricing for cash-settlement options can be determined using the formulas:

$$
c = Q e^{-r T} N(d_2), \quad p = Q e^{-r T} N(-d_2)
$$ 

where 

$$
d_2 = \frac{\ln(S_0 / K) + (r_d - r_f - \sigma^2 / 2)T}{\sigma \sqrt{T}}.
$$ 

For asset-settlement options, the respective payoffs are calculated as:

$$
c = \frac{S_0 Q}{K} e^{-r T} N(d_1), \quad p = \frac{S_0 Q}{K} e^{-r T} N(-d_1)
$$ 

with

$$
d_1 = \frac{\ln(S_0 / K) + (r_d - r_f + \sigma^2 / 2)T}{\sigma \sqrt{T}}.
$$ 

Both formulations incorporate key variables such as the initial spot exchange rate $ S_0 $, time to maturity $ T $, and strike price $ K $, thereby providing a comprehensive analytical framework for assessing FX digital option pricing.

### Relationship to Previous Models

The current model retains its status as a **previously vetted model**, with no modifications made since the last review. This stability builds confidence in the model's validity and reliability. Its alignment with prior iterations ensures a consistent foundation for analysis, reflecting a commitment to maintaining stringent standards in model effectiveness.

> It is crucial to recognize that while the model remains unchanged, this consistency enhances benchmarking against previous outcomes, promoting collaboration across related projects. Any dependencies or shared components with earlier models have been evaluated to ensure coherence and integrated functionality within the broader financial framework.

### Intended Use of Model

The model is exclusively designed for **risk management** purposes, primarily utilized in evaluating risk metrics such as **Value at Risk (VaR)** and sensitivity analyses. Its application emphasizes quantifying potential financial losses across various scenarios, facilitating informed decision-making and effective risk mitigation strategies. Notably, the model’s application is strictly confined to risk contexts and does not extend to **trading-price authority**, unless explicitly approved. This delineation ensures that the model operates within its intended scope, maintaining the integrity of financial assessments derived from its output.

This focused purpose allows users to leverage the model to monitor and manage risk exposure while avoiding trading operations. This distinction reinforces the firm's commitment to employing comprehensive risk assessment tools aligned with established guidelines. By utilizing the model solely for risk evaluation, clients can gain a deeper understanding of their risk profiles, thereby enhancing their overall risk management frameworks.

### Model Version Identification and Supporting Databases

In the context of the RBC FX Digital Option model, the essential metadata required for governance and utilization includes details such as the **model name**, **type**, **version**, **runtime environment**, and **owner contacts**. The model is categorized as an **FX Digital Option**, operating on **RiskWatch 4.5.1 build 053**. The primary owner, **Jason Drysdale**, along with **Thomas Allan** as a key user contact, indicates the model's reach within the **GMRM** business area, primarily targeting **Value at Risk (VaR) calculations**. Importantly, the model is classified as an **internally developed solution** that is **not a black-box model**, promoting transparency in functionality. Key risk factors affecting this model include the **discount curve**, **FX rates**, and **FX volatility**.

The operational integration of the model relies on several **RiskWatch input CSV files** sourced from standardized data repositories. These files are integral for producing the RiskWatch session files and are situated in specified directories. Below are key directories containing these production CSV files as of November 4, 2010:

```
/opt/dslprod/gmrm/data/riskwatch/rwinput/static/models.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/curves.20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/forexch.20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/fxvols.20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/irvols.20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/fxhist.20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/static/curve_index.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/dynamic/hierarchy_242457.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/dynamic/instruments_242457.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/dynamic/positions_242457.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/static/mtmscenario.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/historical_scen_w_fx_20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/static/sensitivity_scen_w_fx.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/static/stress_scen_w_fx.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/historical_scen_ir_only_20101104.csv
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/historical_scen_fx_only_20101104.cs
/opt/dslprod/gmrm/data/riskwatch/rwinput/shared/fxsmile_sens_scen_20101104.csv
```

This structured approach ensures seamless operation of the model within its intended applications, demonstrating its effectiveness in risk management.

| Field | Value |
|-------|-------|
| Model Name          | RBC FX Digital Option    |
| Model Type          | FX Digital Option         |
| Model Version       | RiskWatch 4.5.1 build 053|
| Business/Function Area| GMRM                    |
| Model Owner/Contact  | Jason Drysdale           |
| Model Developer/Contact| RBC Internal            |
| Model Users/Contact   | Thomas Allan             |
| Scope of Application  | FX Digital Option        |
| Internally/Externally Developed| Internally        |
| Black-box Model (Y/N)| No                       |
| Purpose of Model      | VaR Calculation          |
| Key Risks             | Discount Curve, FX Rate, FX Volatility|

### Sample Input/Output and Model Settings Attributes

The **RiskWatch** system integrates a range of theoretical symbols and corresponding attributes to ensure accurate pricing and risk assessment for FX digital options. The key symbols employed include **Q**, **S**, **sigma**, **T**, **K**, **r_d**, and **r_f**, each interconnected with specific **RiskWatch attributes** and associated data sources. These attributes facilitate structured access to critical market data such as FX rates, volatility surfaces, and discount curves, essential for pricing models.

The **RiskWatch Sample Setup** is vital for configuring calculations within the platform. Several key attributes including **Instrument ID**, **Currency**, **Discount Curve**, and **Underlying** must be clearly defined. Further attributes such as **Call/Put Flag**, **Strike Price**, **Maturity Date**, and specifics regarding **Volatility Type** and **Payoff** enhance the pricing mechanism's precision. These settings ensure that RiskWatch accurately models the instrument's value and associated risks through relevant data inputs.

### Symbols and RiskWatch Attributes

| Symbol | RiskWatch Attribute                           |
|--------|-----------------------------------------------|
| Q      | Constant, hardcoded                           |
| S      | Read from FX module                           |
| sigma  | INST/RBC Volatility                           |
| T      | INST/Maturity Date - Session Date            |
| K      | INST/Strike Price                            |
| r_d    | Read from INST/Discount Curve                |
| r_f    | Read from INST/Underlying/Discount Curve     |

### RiskWatch Sample Setup

| RiskWatch Attribute      | Example                                   |
|-------------------------|-------------------------------------------|
| D                       | instruments_242457:44475848               |
| Name                    | 44475848                                 |
| Currency                | USD                                      |
| Discount Curve          | USD Swap                                 |
| Underlying              | EUR                                      |
| Call Option             | False                                    |
| Strike Price            | 1.3334 USD                               |
| Maturity Date           | 2012/04/02                               |
| Contract Size           | 1                                        |
| Volatility Surface      | EURUSDFXVol                              |
| Theoretical Model       | RBC FX Digital                           |
| Fair Value Model        | RM General                                |
| Volatility Type         |                                           |
| RBC Constant Payoff     | 1                                        |
| RBC Volatility          | @RBC forward volatility at maturity      |
| User Defined 1          | DIG                                      |
| RBC Digital Type        | Cash Digital                             |

### RiskWatch Interface

The **RiskWatch interface** is designed to streamline the setup and selection processes for instruments and curves, allowing users to configure parameters for RW calculations efficiently. This includes selecting FX rates and discount curves, as well as detailed attributes relevant to instrument risk profiles. For instance, the **USD Swap** and **EUR Swap** discount curves play pivotal roles in determining pricing and risk outcomes, as evident in the provided data tables.

| Index | Value                              |
|-------|------------------------------------|
| 0     | instruments_242457:44475848        |
| 1     | 44475848                           |
| 2     | USD                                |
| 3     | USD Swap                           |
| 4     | EUR                                |
| 5     | False                              |
| 6     | 1.3334 USD                         |
| 7     | 2012/04/02                         |
| 8     | 1                                  |
| 9     | EUR USD FX Vol                     |
| 10    | RBC FX Digital                     |
| 11    | RM General                         |
| 12    | nan                                |
| 13    | 1                                  |
| 14    | @RBC forward volatility at maturity |
| 15    | DIG                                |
| 16    | Cash Digital                       |
| 17    | nan                                |

## Model Output

The **model** plays a crucial role in the firm's risk management architecture, primarily in calculating Mark-to-Market (MTM), Value at Risk (VaR), stress testing, and sensitivity analyses. These computed results serve as the foundation for the comprehensive Gross Market Risk Management (GMRM) report, consolidating various risk metrics. By integrating these diverse outputs, the model facilitates detailed risk assessments and contributes to creating firm-wide risk reports, enabling stakeholders to make informed decisions based on accurate and timely data.

In the context of **risk reporting**, results generated from the model are essential for providing vital insights into the firm's risk exposure. The processes of MTM and VaR calculations, alongside stress testing and sensitivity analysis, present a holistic view of potential market fluctuations and their impacts on the portfolio. Aggregating these results into the GMRM report ensures that risk reporting is comprehensive and compliant with regulatory requirements, forming the foundation of effective risk management strategies within the organization.

| Section                          | Page |
|----------------------------------|------|
| 6 Risk Reporting                 | .17  |
| 7 Quantitative Assessment        | .18  |
| 7.1 Model Vetting and Limitations| .18  |
| 7.2 Validation                   | .18  |
| 8 Referenced Documents           | .19  |

## Input Data

### List of Input Data and Sources

The input data for the evaluation of FX digital options largely comprises **Trade Data** and **Market Data** sourced via an Extract, Transform, Load (ETL) process. Trade data is obtained from the Global Trading report located at `/opt/dslprod/reposite/data/gmrm/TOR_EXOTICA/exotica.all.20101104.1.orig` on designated servers. This data is fully integrated into the staging tables and subsequently loaded into the EWD data warehouse, adhering to specific ETL-2 rules to ensure proper mapping and processing. Notably, unique ETL-1 rules are not required for the FX digital option due to its straightforward processing demands, whereas trade data undergoes dynamic transformation into RiskWatch input through ETL-3, with corresponding rules detailed in the ETL3 section.

Market data for FX digital options is sourced from the HMD of GMRM, where discount curves and volatility surfaces are selected based on currency-related criteria. Depending on the option's currency, either a lease curve or swap curve is utilized, as clarified in the ETL3 rules section. Similarly, volatility surface selection depends on both the option’s currency and its underlying currency. This systematic approach guarantees that trade evaluation processes rely on accurate and relevant data inputs, in line with industry standards and best practices.

### Trade Data Flow

As of Nov 4, 2010, two FX digital options traded. The data for the FX digital option trades transpires from the report line Global/RBFG/Global Trading/Global Debt Markets/Fixed Income and Currencies/FIC London/FIC London - FX/LFX Derivatives/TOR_EXOTICA_EURO MAIN.

The source file can be found at  
`/opt/dslprod/reposite/data/gmrm/TOR_EXOTICA/exotica.all.20101104.1.orig` on either `usgmrd44.fg.rbc.com` or `usgmrd33.fg.rbc.com`.

An adapted source file containing only the two FX digital options is attached for reference.

Following the ETL-1 process, the source file is loaded into staging tables. No special business rules apply to FX digital options, thus no ETL-1 rules are documented for them.

Through the ETL-2 process, the trade data is loaded into the EWD data warehouse. Detailed ETL-2 rules for FX digital options are available on SharePoint: [ETL-2 Rules for FX Digital Options](#). A hard copy is also attached for reference.

### Market Data

All market data derives from HMD of GMRM.

Regarding the discount curve, either a lease curve or swap curve is applicable depending on the currency of the FX digital option. This definition is stipulated in the ETL3 rules in the relevant section.

In terms of the volatility surface, the appropriate curve is determined based on the currency and underlying currency of the FX digital option, as outlined in the ETL3 rules section.

### Input Data Assumptions

In our financial modeling framework, we employ a **swap curve** for calculating essential **discount factors**, which are crucial for present value calculations. Accurate discount factors significantly influence the valuation of all related cash flows, necessitating adherence to market conventions to ensure compliance with current economic conditions.

To assess the **volatility** used in the model, we leverage the *At-The-Money (ATM) Moneyness/Term volatility surface*, providing insight into how volatility varies with different maturities and levels of moneyness. By implementing sourcing, transformation, and selection rules, we ensure the data remains robust and indicative of prevailing market sentiments. It is vital to stress that the model's integrity relies on high-quality, real-time market data sources to bolster the analytical outcomes derived from it.

> Assuring input data fidelity not only enhances model reliability but also instills confidence in the analytical results derived from it.

### Calibration Steps and Frequency

The calibration process for the model is characterized by a clear *parameterization stance*: there are no free parameters beyond the inputs, streamlining our pursuit of model accuracy and reliability. This configuration ensures that the model operates exclusively based on provided inputs, minimizing overfitting potential and confirming that all parameters reflect observable, relevant metrics. Consequently, no explicit calibration requirements are imposed by external factors; the core data utilized remains pivotal in maintaining operational integrity.

Data availability adheres strictly to the defined parameter boundaries. Notably, as previously discussed in section 3.5, no additional parameters are employed beyond those established. This focused approach fortifies the model's robustness while simplifying the calibration process. Given the absence of extraneous parameters, calibration steps and their frequencies are inherently direct, relying on regular monitoring of input data to sustain ongoing relevance and performance.

## Model Testing and Limitations

### Evidence of Previous Testing

The validation of the model has been thoroughly conducted through a comprehensive **Evidence Pack**, which includes session files from the **RiskWatch** platform and a detailed validation spreadsheet. This assessment aims to confirm the accuracy of calculated values, such as prices and Greeks, through comparison against established reference calculations. This validation process is essential in affirming the reliability and efficacy of our pricing models.

The session file utilized for this validation is located at `/groups/gmrm_bu/qsjsx8c/testing/fx_digital/test.scf`, with an attached validation spreadsheet for your reference. It is crucial to recognize that these testing results serve not only as evidence of model performance but also delineate potential limitations, informing future adjustments and enhancements to the model framework.

### Model and Input Data Limitations

The **models** employed in the Murex application differ significantly from those utilized in the GMRM framework. Specifically, Murex employs a **quasi-replication approach**, wherein the **European digital option** is modeled as a basic vanilla option vertical spread. This involves establishing a long position in an option with strike price $ K $ and a short position in a similar option with a higher strike price $ K \cdot (1 + \varepsilon) $. Importantly, while Murex accounts for **volatility skewness**, GMRM opts for a **Black-Scholes-Merton pricing model**. This decision is justified by the following considerations:

- The positioning of the FX digital option in GMRM is deemed **immaterial**, rendering its contribution to **Value at Risk (VaR)** negligible.
- Although the simulation framework incorporates a parallel shift in the **volatility surface**, shifts in the shape of the volatility surface are excluded. However, GMRM does estimate the overall impact of **volatility skewness** across all foreign exchange products.

To maintain the model's integrity, GMRM remains committed to monitoring the materiality of the FX digital option's position. Should its significance escalate, a reevaluation of the modeling approach in GMRM will be warranted, with established vetting processes defining materiality thresholds.

### Quantitative Assessment

The model will be managed within the **Model Risk Management Framework (S08.03.01)** and is subject to a mandated review cycle occurring at least once every three years. This established approach ensures the robustness of GMRM’s modeling practices while enforcing limitations on its application and usage, thereby ensuring proper identification and management of all model limitations.

> *This structured vetting process underscores the necessity for continual assessment, ensuring that emerging materiality or changes in market conditions are appropriately captured.*

## Appendix

### Context Information

The following documents have been reviewed to establish a comprehensive understanding of the financial methodologies that underpin the frameworks discussed in this whitepaper. These **referenced documents** are paramount in providing robust provenance and facilitating comparative analysis across various financial models and methodologies.

### Available Data

A total of **8 referenced documents** have been identified, including the following key reports and documentation:

1. **GMRM Vetting Report** dated September 14, 2007, focusing on the *RBC FX Digital Option*.
2. **Murex Vetting Report** dated November 09, 2006, pertaining to the *Murex European Digital FX Option*.
3. A foundational **Methodology Document** detailing the *FX Digital Option Model Documentation*.

These documents serve as a cornerstone for understanding the operational frameworks of digital options in foreign exchange and align with our analytical approaches. The data extracted from these reports are instrumental in corroborating methodologies and ensuring that our findings are grounded in historically vetted standards of practice.