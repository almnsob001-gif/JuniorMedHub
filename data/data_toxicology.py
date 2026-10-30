# data_toxicology.py

TOXICOLOGY_DATA = {
    "Toxicology": {
        "A. General Toxicology": [
            "Initial Assessment of the Poisoned Patient",
            "Toxidromes and Clinical Recognition",
            "Gastrointestinal Decontamination",
            "Enhanced Elimination and Hemodialysis",
            "Antidotes and Emergency Antidote Guide"
        ],
        "B. Medication Poisoning": [
            "Paracetamol (Acetaminophen) Poisoning",
            "Salicylate Poisoning",
            "Opioid Toxicity",
            "Benzodiazepine and Sedative Overdose",
            "Tricyclic Antidepressant (TCA) Poisoning",
            "Beta-Blocker Toxicity",
            "Calcium Channel Blocker Toxicity",
            "Digoxin Toxicity",
            "Insulin and Sulfonylurea Poisoning"
        ],
        "C. Chemicals and Toxic Alcohols": [
            "Organophosphate and Carbamate Poisoning",
            "Methanol Poisoning",
            "Ethylene Glycol Poisoning",
            "Carbon Monoxide Poisoning",
            "Cyanide Poisoning",
            "Corrosive Ingestion"
        ],
        "D. Other High-Risk Poisonings": [
            "Iron Poisoning",
            "Lithium Toxicity",
            "Valproate Toxicity",
            "Isoniazid Poisoning",
            "Methemoglobinemia and Oxidizing Agents"
        ],
        "E. Environmental and Special Toxicology": [
            "Hydrocarbon Poisoning",
            "Other Pesticide Poisoning",
            "Snakebite and Envenomation",
            "Scorpion Sting and Dangerous Bites",
            "Toxicologic Cardiac Arrest and Refractory Shock"
        ]
    }
}

TOXICOLOGY_TOPICS = {}

# ==================== GENERAL TOXICOLOGY PRINCIPLES ====================

TOXICOLOGY_TOPICS[("Toxicology", "Initial Assessment of the Poisoned Patient")] = [
    ("01 — RECOGNIZE", "info", 
     "Suspect poisoning in patients presenting with:\n"
     "• Unexplained altered mental status, coma, or agitation.\n"
     "• Seizures, unexplained metabolic acidosis, or elevated lactate.\n"
     "• Respiratory depression, hypoxemia, or unexplained respiratory failure.\n"
     "• Hypotension, shock, bradycardia, tachycardia, or dysrhythmias.\n"
     "• Abnormal pupils, excessive secretions, diaphoresis, dry skin, or hyperthermia.\n"
     "• A known or possible medication overdose, chemical exposure, or intentional ingestion.\n\n"
     "[color=#991B1B]IMPORTANT: A normal initial examination does not exclude serious poisoning. Modified-release preparations and some cardiotoxic agents can cause delayed deterioration.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]1. Scene Safety and Decontamination[/color]\n"
     "• Identify suspected agent and route of exposure.\n"
     "• Use appropriate PPE. Avoid direct contact with contaminated clothing, vomitus, powders, or liquids.\n"
     "• Remove contaminated clothing and irrigate exposed skin or eyes when indicated.\n"
     "• Prevent secondary contamination of healthcare staff.\n"
     "• [color=#991B1B]Do NOT enter a contaminated environment without appropriate PPE and training.[/color]\n\n"
     "[color=#1E3A8A]2. Airway and Breathing[/color]\n"
     "• Assess airway patency, respiratory rate, SpO2, and ventilation.\n"
     "• Provide oxygen for hypoxemia and bag-mask ventilation for inadequate ventilation.\n"
     "• Intubate when airway protection or ventilation cannot be maintained.\n"
     "• Consider capnography in respiratory depressant poisoning and ventilated patients.\n"
     "• [color=#991B1B]In salicylate poisoning, intubation can worsen toxicity if adequate compensatory hyperventilation is not maintained. Avoid intubation unless necessary; if required, manage ventilation carefully.[/color]\n\n"
     "[color=#1E3A8A]3. Circulation[/color]\n"
     "• Establish IV access and continuous cardiac monitoring. Obtain 12-lead ECG.\n"
     "• Assess BP, peripheral perfusion, signs of shock.\n"
     "• Give isotonic crystalloid when clinically indicated, reassessing after each bolus.\n"
     "• Use vasopressors and toxin-specific therapy when shock persists, according to suspected mechanism.\n\n"
     "[color=#1E3A8A]4. Disability[/color]\n"
     "• Assess GCS, pupils, and seizure activity.\n"
     "• Check bedside glucose immediately. Treat hypoglycemia promptly.\n"
     "• Treat toxicologic seizures initially with benzodiazepines and appropriate airway support."),
    ("03 — INITIAL INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Core tests in significant or uncertain poisoning:[/color]\n"
     "• Bedside glucose.\n"
     "• Electrolytes, bicarbonate, urea, creatinine.\n"
     "• Blood gas and lactate in critically ill patients.\n"
     "• 12-lead ECG.\n"
     "• Acetaminophen concentration when indicated.\n"
     "• Salicylate concentration when suspected or history unclear.\n\n"
     "[color=#1E3A8A]Additional tests when indicated:[/color]\n"
     "• Liver function tests. Measured serum osmolality and calculated osmolar gap.\n"
     "• Pregnancy test when clinically relevant. Specific drug concentrations.\n"
     "• Co-oximetry for suspected CO or methemoglobinemia.\n"
     "• CK and urinalysis in prolonged seizures, hyperthermia, or suspected rhabdomyolysis.\n\n"
     "[color=#991B1B]Routine urine drug screens have limitations. A negative screen does not exclude poisoning, and a positive result does not establish current toxicity or its severity.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Maintain oxygenation, ventilation, and perfusion.\n"
     "• Correct clinically significant glucose and electrolyte abnormalities.\n"
     "• Treat seizures, hyperthermia, hypothermia, and dysrhythmias.\n"
     "• Avoid drugs that may worsen the suspected toxidrome or ECG abnormality.\n"
     "• Reassess frequently for delayed deterioration.\n\n"
     "[color=#1E3A8A]Antidote Strategy[/color]\n"
     "• Identify likely toxin and determine whether a specific antidote is indicated.\n"
     "• Do not delay resuscitation while awaiting confirmatory testing.\n"
     "• Follow toxin-specific protocol and monitor for treatment complications.\n"
     "• Consult a poison center or clinical toxicologist whenever available."),
    ("05 — DISPOSITION", "warning", 
     "[color=#1E3A8A]ICU or high-acuity admission:[/color]\n"
     "• Respiratory failure, shock, significant dysrhythmias, recurrent seizures, severe acidosis, or anticipated life-threatening delayed toxicity.\n\n"
     "[color=#1E3A8A]Monitored admission:[/color]\n"
     "• Persistent symptoms, abnormal ECG or laboratory results, or an agent requiring prolonged observation.\n\n"
     "[color=#1E3A8A]Discharge:[/color]\n"
     "• Only after the appropriate observation period, resolution of concerning clinical findings, and assessment of intentional self-harm and safeguarding risks."),
    ("06 — REFERENCES", "info", "AHA 2025 Guidelines: Special Circumstances of Resuscitation; Royal Children's Hospital Melbourne Poisoning Guidance; Goldfrank's Toxicologic Emergencies.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Toxidromes and Clinical Recognition")] = [
    ("01 — RECOGNIZE", "info", 
     "A toxidrome is a recognizable pattern of clinical findings suggesting a particular toxin class. It supports early treatment but does not replace history, ECG, laboratory assessment, or consideration of mixed poisoning."),
    ("02 — COMMON TOXIDROMES", "info", 
     "[color=#1E3A8A]1. Opioid Toxidrome[/color]\n"
     "• Respiratory depression. Reduced consciousness. Miosis (not always pinpoint). Bradycardia/hypotension in severe cases.\n"
     "• Agents: Morphine, heroin, fentanyl, methadone, other opioids.\n"
     "• Action: Support ventilation; administer naloxone when opioid toxicity suspected.\n\n"
     "[color=#1E3A8A]2. Sympathomimetic Toxidrome[/color]\n"
     "• Agitation, anxiety, psychosis. Tachycardia and hypertension. Mydriasis. Diaphoresis and hyperthermia. Tremor, seizures, chest pain.\n"
     "• Agents: Amphetamines, cocaine, other stimulants.\n"
     "• Action: Reduce stimulation; treat agitation with benzodiazepines; monitor temperature/ECG; manage hyperthermia promptly.\n\n"
     "[color=#1E3A8A]3. Anticholinergic Toxidrome[/color]\n"
     "• Delirium and agitation. Mydriasis and blurred vision. Dry skin and mucous membranes. Tachycardia and hyperthermia. Urinary retention and reduced bowel sounds.\n"
     "• Agents: Atropine, diphenhydramine, TCAs, other antimuscarinics.\n"
     "• Action: Supportive care, temperature control, ECG assessment, benzodiazepines for severe agitation/seizures.\n"
     "• [color=#991B1B]Do NOT use physostigmine empirically in undifferentiated poisoning. Avoid in suspected TCA toxicity or significant conduction abnormalities.[/color]\n\n"
     "[color=#1E3A8A]4. Cholinergic Toxidrome[/color]\n"
     "• Salivation, lacrimation, sweating. Bronchorrhea, bronchospasm, respiratory distress. Vomiting, diarrhea, urinary incontinence. Miosis. Bradycardia, fasciculations, muscle weakness/paralysis.\n"
     "• Agents: Organophosphates, carbamates, cholinergic medications.\n"
     "• Action: Protect staff, remove contamination, support ventilation, give atropine promptly. Consider pralidoxime for significant organophosphate poisoning.\n\n"
     "[color=#1E3A8A]5. Sedative-Hypnotic Toxidrome[/color]\n"
     "• Drowsiness, ataxia, slurred speech. Reduced consciousness. Respiratory depression (especially with co-ingestants). Hypotension in severe poisoning.\n"
     "• Agents: Benzodiazepines, barbiturates, alcohol, other sedatives.\n"
     "• Action: Airway/ventilatory support, glucose assessment, ECG, evaluation for co-ingestion.\n"
     "• [color=#991B1B]Flumazenil is NOT routinely recommended in undifferentiated overdose (may precipitate seizures or withdrawal).[/color]\n\n"
     "[color=#1E3A8A]6. Serotonin Toxicity[/color]\n"
     "• Agitation, diaphoresis, hyperthermia. Inducible/spontaneous clonus. Hyperreflexia (often greater in lower limbs). Tremor, autonomic instability.\n"
     "• Agents: Serotonergic antidepressants, drug combinations, recreational substances.\n"
     "• Action: Stop serotonergic agents, supportive care, benzodiazepines for agitation, urgently manage severe hyperthermia.\n\n"
     "[color=#1E3A8A]7. Neuroleptic Malignant Syndrome[/color]\n"
     "• Hyperthermia. Generalized rigidity. Altered mental status. Autonomic instability. Elevated CK may occur.\n"
     "• Agents: Dopamine-blocking medications or abrupt withdrawal of dopaminergic therapy.\n"
     "• Action: Stop causative agent, supportive care, temperature control, assess renal function and CK, critical care for severe cases.\n\n"
     "[color=#1E3A8A]8. Toxic Alcohol Pattern[/color]\n"
     "• Altered consciousness, vomiting, unexplained metabolic acidosis. Elevated osmolar gap may be present early.\n"
     "• Visual disturbance suggests methanol. AKI or hypocalcemia may suggest ethylene glycol.\n"
     "• Action: Obtain blood gas, electrolytes, measured osmolality, specific levels. Contact toxicology early; do not delay antidotal treatment."),
    ("03 — INVESTIGATIONS", "info", 
     "• ECG for suspected cardiotoxic agents.\n"
     "• Blood glucose, electrolytes, bicarbonate, renal function.\n"
     "• Blood gas and lactate in severe illness.\n"
     "• CK in rigidity, hyperthermia, prolonged seizures, or suspected rhabdomyolysis.\n"
     "• Specific drug levels and toxic alcohol studies when indicated."),
    ("04 — TREATMENT PRINCIPLES", "success", 
     "• Treat the patient, not the toxidrome label alone.\n"
     "• Mixed ingestions can produce overlapping or contradictory findings.\n"
     "• Give specific antidotes only when the clinical indication is appropriate.\n"
     "• Use continuous monitoring in severe or evolving toxicity."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with respiratory compromise, seizures, severe hyperthermia, significant ECG abnormalities, hemodynamic instability, or persistent altered mental status.\n"
     "• Discharge only when toxicity has resolved and the required observation period is complete."),
    ("06 — REFERENCES", "info", "Goldfrank's Toxicologic Emergencies; AHA 2025 Guidelines; Royal Children's Hospital Melbourne.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Gastrointestinal Decontamination")] = [
    ("01 — RECOGNIZE", "info", 
     "Consider GI decontamination only after a potentially toxic ingestion and when expected benefit outweighs risk.\n"
     "Decision depends on:\n"
     "• Substance and estimated amount. Time since ingestion.\n"
     "• Immediate-release vs modified-release formulation. Risk of ongoing absorption.\n"
     "• Airway protection and aspiration risk.\n"
     "• Presence of GI obstruction or perforation risk."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation first.\n"
     "• Identify product, strength, formulation, maximum possible dose.\n"
     "• Determine time of ingestion and co-ingestants.\n"
     "• Contact poison center/clinical toxicologist for serious or uncertain exposures.\n"
     "• Do NOT induce vomiting.\n"
     "• Do NOT administer food, milk, neutralizing agents, or home remedies as substitute for medical assessment."),
    ("03 — TREATMENT OPTIONS", "info", 
     "[color=#1E3A8A]A. Single-Dose Activated Charcoal[/color]\n"
     "• Indications: Potentially toxic ingestion of a substance adsorbed by charcoal. Greatest benefit when given early (generally within ~1 hour). Selected later presentations may benefit when absorption is delayed.\n"
     "• Dose: 1 g/kg orally or via gastric tube. Adult max typically 50 g per local protocol.\n"
     "• Use commercial activated charcoal suspension. Administer orally only when patient is cooperative with safe airway. Use gastric tube only when justified and airway protected. Monitor for vomiting, aspiration, deterioration.\n"
     "• [color=#991B1B]Avoid in unprotected airway or substantial aspiration risk. Do NOT use routinely after corrosive ingestion, hydrocarbon ingestion with aspiration risk, or poorly adsorbed substances. Does NOT effectively adsorb many metals (iron) or alcohols (methanol, ethylene glycol).[/color]\n\n"
     "[color=#1E3A8A]B. Multiple-Dose Activated Charcoal[/color]\n"
     "• Potential indications: Selected life-threatening ingestions of carbamazepine, dapsone, phenobarbital, quinine, or theophylline.\n"
     "• Dose: Initial 1 g/kg, followed by repeated doses per poison-center protocol. Adult regimens often 25–50 g every 4–6 hours.\n"
     "• Monitor bowel function, vomiting, aspiration risk, fluid balance, electrolytes.\n"
     "• [color=#991B1B]Do NOT use routinely for all overdoses. Avoid with bowel obstruction, ileus, or unprotected airway. Requires specialist guidance.[/color]\n\n"
     "[color=#1E3A8A]C. Whole-Bowel Irrigation[/color]\n"
     "• Potential indications: Selected sustained-release/enteric-coated ingestions, iron/lithium/other poorly adsorbed substances, body-packing cases (specialist management).\n"
     "• Use appropriate PEG-electrolyte solution. Adult regimens may use ~1.5–2 L/hour, adjusted to tolerance. Continue until rectal effluent is clear.\n"
     "• [color=#991B1B]Do NOT use with bowel obstruction, ileus, perforation, hemodynamic instability, or unprotected airway. Do not delay resuscitation or essential antidotal therapy.[/color]\n\n"
     "[color=#1E3A8A]D. Gastric Lavage[/color]\n"
     "• NOT routine. Consider only in exceptional, potentially life-threatening ingestions with very short interval.\n"
     "• [color=#991B1B]Risks: aspiration, hypoxia, laryngospasm, GI perforation. Never perform routinely or in corrosive/hydrocarbon ingestion.[/color]\n\n"
     "[color=#1E3A8A]E. Induced Emesis[/color]\n"
     "• [color=#991B1B]Do NOT induce vomiting with ipecac or other methods. Does not reliably improve outcomes and may increase complications.[/color]"),
    ("04 — DISPOSITION", "warning", 
     "• Patients requiring decontamination should remain under observation appropriate to the substance and exposure.\n"
     "• Admit patients with significant symptoms, high-risk ingestion, abnormal ECG/labs, or risk of delayed toxicity."),
    ("05 — REFERENCES", "info", "AACT/EAPCCT Position Statements on Activated Charcoal and GI Decontamination; Goldfrank's; Royal Children's Hospital Melbourne.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Enhanced Elimination and Hemodialysis")] = [
    ("01 — RECOGNIZE", "info", 
     "Enhanced elimination may be considered when a toxin can be removed effectively and clinical severity justifies the procedure.\n\n"
     "[color=#1E3A8A]Potential modalities:[/color]\n"
     "• Intermittent hemodialysis. Continuous kidney replacement therapy.\n"
     "• Multiple-dose activated charcoal. Urinary alkalinization for selected substances.\n\n"
     "Decision must consider toxin characteristics, severity, renal function, clinical trajectory, and availability of specialist services."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation.\n"
     "• Identify suspected toxin and obtain relevant concentrations when available.\n"
     "• Check electrolytes, renal function, blood gas, ECG.\n"
     "• Contact clinical toxicologist and nephrology team early when severe poisoning may require extracorporeal treatment.\n"
     "• Do NOT delay essential antidotes or supportive care while arranging dialysis."),
    ("03 — HEMODIALYSIS", "info", 
     "[color=#1E3A8A]Indications (Severe Poisoning):[/color]\n"
     "• Methanol with severe clinical toxicity or significant acidosis.\n"
     "• Ethylene glycol with severe metabolic abnormalities, organ injury, or significant toxic burden.\n"
     "• Salicylate poisoning with severe toxicity, neurologic manifestations, pulmonary edema, renal impairment, or failure of medical treatment.\n"
     "• Lithium poisoning with severe neurologic/cardiac toxicity, impaired clearance, or markedly elevated concentrations.\n"
     "• Severe metformin-associated lactic acidosis.\n"
     "• Selected severe valproate, theophylline, or other dialyzable poisonings.\n\n"
     "[color=#1E3A8A]Preparation and Monitoring:[/color]\n"
     "• Arrange nephrology and toxicology consultation. Confirm toxin and relevant labs.\n"
     "• Prepare vascular access and dialysis equipment per institutional policy.\n"
     "• Review electrolyte abnormalities, hemodynamic status, antidote dosing.\n"
     "• Intermittent hemodialysis preferred when rapid clearance required and patient can tolerate.\n"
     "• CRRT may be used when intermittent unavailable or poorly tolerated.\n"
     "• Monitor BP, ECG, electrolytes, blood gas, renal function, toxin concentrations.\n"
     "• Repeat toxin levels after dialysis when indicated to detect rebound.\n"
     "• Continue/adjust antidotes during/after dialysis (extracorporeal treatment may remove antidote).\n"
     "• [color=#991B1B]Dialysis decisions are toxin-specific and should not be based solely on an elevated osmolar gap or an isolated lab result. Monitor for post-dialysis rebound, ongoing absorption, delayed organ injury. Consult poison center/toxicologist for specific thresholds.[/color]"),
    ("04 — URINARY ALKALINIZATION", "info", 
     "[color=#1E3A8A]Indication:[/color] Clinically significant salicylate poisoning when appropriate and not contraindicated.\n\n"
     "[color=#1E3A8A]Dose and Preparation:[/color]\n"
     "• Commonly: Sodium bicarbonate 150 mEq added to 1 L D5W per local protocol.\n"
     "• Potassium supplementation may be required based on serum K+, renal function, urine output.\n"
     "• [color=#991B1B]The formulation and potassium content must be individualized. Do NOT add potassium automatically in renal impairment, hyperkalemia, or oliguria.[/color]\n\n"
     "[color=#1E3A8A]Administration and Monitoring:[/color]\n"
     "• Administer by IV infusion under continuous clinical supervision.\n"
     "• Common target: urine pH 7.5–8.0.\n"
     "• Monitor urine pH, serum pH, K+, Na+, renal function, fluid balance, clinical status.\n"
     "• Correct hypokalemia (can prevent effective alkalinization).\n"
     "• [color=#991B1B]Avoid uncontrolled alkalinization producing severe alkalemia, hypernatremia, or fluid overload. Must not delay hemodialysis when severe salicylate poisoning meets dialysis criteria.[/color]"),
    ("05 — MULTIPLE-DOSE ACTIVATED CHARCOAL", "info", 
     "May enhance elimination of selected drugs through interruption of enterohepatic circulation or enhanced GI clearance. Use only for toxin-specific indications under appropriate protocol. Refer to Topic 03 for dosing, contraindications, monitoring."),
    ("06 — DISPOSITION", "warning", 
     "• Patients undergoing enhanced elimination generally require admission to a monitored setting.\n"
     "• ICU care appropriate for severe acidosis, neurologic deterioration, respiratory failure, shock, or major electrolyte abnormalities."),
    ("07 — REFERENCES", "info", "EXTRIP Workgroup Recommendations; Goldfrank's; American College of Medical Toxicology.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Antidotes and Emergency Antidote Guide")] = [
    ("01 — RECOGNIZE", "info", 
     "Consider a specific antidote when exposure history, toxidrome, ECG, laboratory findings, or clinical presentation supports a treatable toxic mechanism.\n\n"
     "[color=#1E3A8A]Core principle:[/color] Antidotes complement, rather than replace, airway management, ventilation, circulatory support, and other resuscitative measures."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation.\n"
     "• Check bedside glucose and obtain ECG in significant or uncertain poisoning.\n"
     "• Identify agent, formulation, amount, time of exposure.\n"
     "• Contact poison center/clinical toxicologist for severe or uncertain cases.\n"
     "• Obtain relevant toxin concentrations when indicated, without delaying time-critical treatment."),
    ("03 — COMMON ANTIDOTES", "info", 
     "[color=#1E3A8A]1. Naloxone — Opioid Toxicity[/color]\n"
     "• For suspected opioid-induced respiratory depression: titrate IV naloxone to restore adequate ventilation.\n"
     "• Common initial IV dose: 0.04 mg in patients with opioid dependence, followed by escalating doses (0.1, 0.2, 0.4 mg).\n"
     "• In apnea/severe hypoxia: use larger initial dose and prioritize ventilation.\n"
     "• No IV access: use approved intranasal or IM product per label.\n"
     "• Titrate to adequate respiratory effort rather than full wakefulness. Repeat as required. Consider infusion for recurrent depression.\n"
     "• [color=#991B1B]Naloxone may wear off before the opioid (especially methadone or modified-release). Continue observation and provide ventilatory support.[/color]\n\n"
     "[color=#1E3A8A]2. N-Acetylcysteine (NAC) — Paracetamol Poisoning[/color]\n"
     "• Indication: Potentially toxic ingestion per timed concentration and applicable protocol. Unknown time with detectable paracetamol or evidence of hepatotoxicity may also require treatment.\n"
     "• Common IV regimen: Total 300 mg/kg over ~20–21 hours (divided into protocol-specific infusions).\n"
     "• Start promptly when indicated; do not delay for results in high-risk presentation.\n"
     "• Monitor paracetamol concentration, AST/ALT, INR, renal function, clinical status.\n"
     "• Reassess whether treatment should continue beyond initial regimen using accepted stopping criteria.\n"
     "• [color=#991B1B]Early concentration may be misleading if obtained before 4 hours after single acute ingestion. Use Rumack–Matthew nomogram only for appropriate single acute ingestion with known time. Monitor for anaphylactoid reactions.[/color]\n\n"
     "[color=#1E3A8A]3. Atropine — Cholinergic Toxicity[/color]\n"
     "• Indication: Clinically significant bronchorrhea, bronchospasm, respiratory compromise, or bradycardia due to cholinergic poisoning.\n"
     "• Severe organophosphate poisoning: Common adult initial IV dose 1–3 mg, followed by rapid reassessment and repeated doubling every few minutes until secretions/ventilation improve.\n"
     "• Titrate to improvement in bronchial secretions, bronchospasm, oxygenation, ventilation.\n"
     "• [color=#991B1B]Do NOT use pupil size or heart rate alone as endpoint. Atropine does not reverse nicotinic muscle weakness; respiratory support may still be necessary.[/color]\n\n"
     "[color=#1E3A8A]4. Pralidoxime — Organophosphate Poisoning[/color]\n"
     "• Indication: Significant organophosphate poisoning (especially with muscle weakness, fasciculations, respiratory compromise).\n"
     "• Common adult regimen: 1–2 g IV over ~15–30 minutes, followed by repeat dosing or infusion when indicated.\n"
     "• [color=#991B1B]Do NOT delay atropine or respiratory support while preparing pralidoxime. Benefit depends on agent, timing, clinical circumstances.[/color]\n\n"
     "[color=#1E3A8A]5. Sodium Bicarbonate — Selected Sodium-Channel Blocker Toxicity[/color]\n"
     "• Indication: TCA poisoning or other sodium-channel blocker toxicity with QRS widening, ventricular dysrhythmias, or hemodynamic compromise.\n"
     "• Common adult initial dose: 1–2 mEq/kg IV. Repeat per ECG/hemodynamic response and institutional protocol.\n"
     "• Administer IV with continuous ECG monitoring. Follow QRS duration, BP, rhythm, blood gas, Na+, K+.\n"
     "• [color=#991B1B]Avoid excessive alkalemia and hypernatremia. Do NOT use bicarbonate routinely for every overdose or metabolic acidosis; treatment must match the mechanism.[/color]\n\n"
     "[color=#1E3A8A]6. Digoxin Immune Fab — Severe Digoxin Toxicity[/color]\n"
     "• Indication: Life-threatening dysrhythmias, severe hyperkalemia from acute digoxin poisoning, or other accepted indications.\n"
     "• Calculate using product information, estimated ingested dose, or serum digoxin concentration when appropriate.\n"
     "• [color=#991B1B]Hypokalemia can occur after successful treatment; monitor K+ closely. Do NOT delay life-saving treatment in critically unstable patient while waiting for confirmatory level.[/color]\n\n"
     "[color=#1E3A8A]7. Fomepizole — Methanol or Ethylene Glycol[/color]\n"
     "• Indication: Suspected/confirmed toxic alcohol poisoning meeting accepted treatment criteria.\n"
     "• Common initial adult dose: 15 mg/kg IV. Subsequent doses/intervals depend on protocol, treatment duration, and whether hemodialysis is being performed.\n"
     "• Coordinate dosing with dialysis team (fomepizole dosing may require adjustment during extracorporeal treatment).\n"
     "• [color=#991B1B]Do NOT delay indicated treatment while awaiting toxic alcohol levels when clinical suspicion is high. Contact toxicology and nephrology early.[/color]"),
    ("04 — GENERAL ANTIDOTE SAFETY", "warning", 
     "• Confirm correct antidote, concentration, route, dose, infusion rate.\n"
     "• Check contraindications, interactions, required monitoring.\n"
     "• Use weight-based calculations carefully, especially in children.\n"
     "• Verify high-alert medications and infusion preparations independently when possible.\n"
     "• Document indication, dose, time, response, adverse effects.\n"
     "• Contact poison center/toxicologist for complex cases."),
    ("05 — DISPOSITION", "warning", 
     "• Patients receiving antidotes for life-threatening poisoning require observation appropriate to the toxin and risk of recurrent toxicity.\n"
     "• ICU admission indicated for respiratory failure, shock, serious dysrhythmias, severe metabolic abnormalities, or recurrent toxicity."),
    ("06 — REFERENCES", "info", "AHA 2025 Guidelines; Goldfrank's; EXTRIP Workgroup; Product prescribing information and local poison-center protocols.")
]

# ==================== SPECIFIC POISONINGS ====================

TOXICOLOGY_TOPICS[("Toxicology", "Paracetamol (Acetaminophen) Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Paracetamol poisoning may initially be asymptomatic despite potentially severe delayed hepatic injury.\n\n"
     "[color=#1E3A8A]Early phase (0–24 hours):[/color] Nausea, vomiting, anorexia, diaphoresis. Patient may appear clinically well. Labs may initially be normal.\n\n"
     "[color=#1E3A8A]Intermediate phase (24–72 hours):[/color] RUQ discomfort. Rising AST/ALT. Increasing INR and possible renal impairment.\n\n"
     "[color=#1E3A8A]Severe phase (72–96 hours and later):[/color] Acute liver failure, coagulopathy, hypoglycemia, lactic acidosis, encephalopathy, multiorgan dysfunction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status, bedside glucose.\n"
     "• Establish IV access in significant poisoning.\n"
     "• Determine time, amount, formulation, pattern of ingestion.\n"
     "• Identify combination products containing paracetamol.\n"
     "• Obtain serum paracetamol concentration at 4 hours or later after single acute ingestion with known time.\n"
     "• If presentation delayed, ingestion time unknown, or liver injury suspected: obtain relevant tests immediately.\n"
     "• Contact poison center/toxicologist for uncertain, massive, or complicated ingestions."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serum paracetamol concentration.\n"
     "• AST, ALT, INR/PT. Electrolytes, urea, creatinine, glucose.\n"
     "• Blood gas and lactate in severe poisoning.\n"
     "• Bilirubin and additional acute liver failure investigations when indicated.\n"
     "• Pregnancy test when clinically relevant.\n\n"
     "[color=#1E3A8A]Interpretation of Paracetamol Concentration:[/color]\n"
     "• For single acute ingestion with reliably known time: plot concentration on locally accepted Rumack–Matthew nomogram (generally used for concentrations obtained 4–24 hours after ingestion).\n"
     "• [color=#991B1B]Do NOT use nomogram for repeated supratherapeutic ingestion, unknown ingestion time, or presentations outside validated circumstances. If time unknown or hepatic injury suspected, treatment decisions based on history, concentration, labs, toxicology advice.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. N-Acetylcysteine (NAC)[/color]\n"
     "NAC replenishes glutathione and reduces risk of hepatic injury. Benefit greatest when started early, but remains indicated in many late presentations.\n"
     "• Indications: Concentration at/above treatment line on appropriate nomogram. Suspected potentially toxic ingestion when concentration result delayed beyond treatment window. Unknown time with detectable concentration concerning for toxicity. Repeated supratherapeutic ingestion with concerning concentration or abnormal liver tests. Suspected paracetamol-related liver injury per specialist guidance.\n"
     "• Common IV regimen: Total 300 mg/kg over ~20–21 hours. One traditional three-infusion regimen: 150 mg/kg over 1 hour; 50 mg/kg over 4 hours; 100 mg/kg over 16 hours. Follow locally approved protocol (two-bag regimens also used). Check maximum dosing weight and infusion volumes.\n"
     "• Start promptly when indicated. Monitor for nausea, vomiting, flushing, rash, wheezing, hypotension, other infusion reactions.\n"
     "• Recheck paracetamol concentration, AST/ALT, INR, creatinine, relevant prognostic markers before planned end of treatment.\n"
     "• Continue NAC beyond initial course if paracetamol remains detectable, hepatic injury worsening, INR remains significantly abnormal, or prognostic markers not improving.\n"
     "• Stop only when accepted clinical and laboratory stopping criteria are met, with toxicology input for complicated cases.\n"
     "• [color=#991B1B]Do NOT stop NAC automatically when initial infusion schedule finishes. Early concentration obtained before 4 hours after single acute ingestion cannot reliably exclude toxicity. Massive ingestion may require modified treatment. Early consultation with liver transplant center essential when acute liver failure develops.[/color]\n\n"
     "[color=#1E3A8A]B. Activated Charcoal[/color]\n"
     "• Dose: Commonly 1 g/kg orally, usually up to 50 g in adults.\n"
     "• Consider early after potentially toxic ingestion when airway protected and aspiration risk acceptable. Later use may be appropriate in selected massive or delayed-absorption ingestions after specialist consultation.\n"
     "• [color=#991B1B]Do NOT give to patient with unprotected airway or substantial aspiration risk.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with hepatotoxicity, coagulopathy, significant metabolic abnormalities, or other evidence of severe poisoning.\n"
     "• ICU care indicated for acute liver failure, encephalopathy, shock, severe acidosis, or hypoglycemia requiring intensive support.\n"
     "• Consider early transfer to liver transplant center when acute liver failure develops."),
    ("06 — REFERENCES", "info", "ACMT Practice Statement: Duration of IV NAC Therapy (2026 update); Goldfrank's; Local poison-center paracetamol protocol.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Salicylate Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Salicylate poisoning can cause severe acid-base disturbances, hyperthermia, neurologic toxicity, pulmonary edema, and death.\n\n"
     "• Tinnitus or hearing changes. Nausea, vomiting, abdominal discomfort.\n"
     "• Tachypnea and hyperventilation. Sweating, fever, dehydration.\n"
     "• Agitation, confusion, seizures, coma.\n"
     "• Pulmonary edema and respiratory failure in severe cases.\n\n"
     "[color=#1E3A8A]Characteristic Acid-Base Pattern:[/color]\n"
     "• Early respiratory alkalosis (direct stimulation of respiratory center).\n"
     "• Anion-gap metabolic acidosis (organic acid accumulation, impaired metabolism).\n"
     "• Mixed respiratory alkalosis and metabolic acidosis is common.\n"
     "• [color=#991B1B]A normal or near-normal pH does NOT exclude severe poisoning because simultaneous respiratory alkalosis and metabolic acidosis may coexist.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, temperature, mental status.\n"
     "• Obtain IV access and continuous monitoring. Check bedside glucose and ECG.\n"
     "• Obtain blood gas, electrolytes, renal function, serum salicylate concentration.\n"
     "• Assess volume status and urine output.\n"
     "• Begin treatment promptly when clinical suspicion is significant.\n"
     "• Contact toxicology and nephrology early in severe poisoning.\n"
     "• [color=#991B1B]Avoid suppressing compensatory hyperventilation unnecessarily. Sedation, paralysis, or intubation can precipitate rapid deterioration if ventilation not carefully maintained.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial salicylate concentrations until clear decline and clinical improvement established.\n"
     "• Blood gas, bicarbonate, anion gap, electrolytes.\n"
     "• Potassium, glucose, urea, creatinine.\n"
     "• Lactate and liver tests when indicated.\n"
     "• Chest imaging for suspected pulmonary edema.\n"
     "• Co-ingestant testing when appropriate."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Sodium Bicarbonate and Urinary Alkalinization[/color]\n"
     "• Indication: Clinically significant salicylate poisoning when urinary alkalinization appropriate.\n"
     "• Common approach: Sodium bicarbonate 1–2 mEq/kg IV as initial bolus when indicated, followed by alkalinizing infusion. Commonly used adult infusion: 150 mEq sodium bicarbonate in 1 L D5W, with potassium supplementation individualized to labs/renal function.\n"
     "• Aim for urine pH ~7.5–8.0. Maintain adequate circulating volume without fluid overload.\n"
     "• Monitor urine pH, serum pH, Na+, K+, bicarbonate, creatinine, fluid balance.\n"
     "• Reassess salicylate concentrations and clinical status frequently. Correct hypokalemia (can make alkalinization difficult).\n"
     "• [color=#991B1B]Avoid severe alkalemia, hypernatremia, fluid overload. Urinary alkalinization does NOT replace hemodialysis in severe poisoning. Clinical deterioration despite treatment requires urgent reassessment.[/color]\n\n"
     "[color=#1E3A8A]B. Hemodialysis[/color]\n"
     "• Indications: Altered mental status or seizures. New hypoxemia or pulmonary edema. Severe acidemia (particularly pH ≤ 7.20). Renal impairment with significant toxicity. Failure of standard therapy. Very high salicylate concentrations.\n"
     "• EXTRIP recommends extracorporeal treatment for severe poisoning. Intermittent hemodialysis preferred when available.\n"
     "• Continue supportive care and bicarbonate therapy while arranging dialysis. Monitor ECG, BP, electrolytes, blood gas, serial salicylate concentrations. Reassess after dialysis for clinical improvement and rebound.\n"
     "• [color=#991B1B]Do NOT use serum concentration alone to determine severity, especially in chronic poisoning or delayed presentation.[/color]\n\n"
     "[color=#1E3A8A]C. Activated Charcoal[/color]\n"
     "• Dose: Commonly 1 g/kg orally, up to 50 g in adults, when indicated.\n"
     "• Consider in selected early presentations with protected airway. Repeated-dose charcoal may be considered in selected serious cases with specialist guidance.\n"
     "• [color=#991B1B]Avoid aspiration risk. Do NOT delay resuscitation or alkalinization.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit symptomatic patients and patients with abnormal acid-base status or rising concentrations.\n"
     "• ICU admission indicated for neurologic toxicity, pulmonary edema, severe acidemia, seizures, or hemodynamic instability.\n"
     "• Transfer to facility capable of urgent hemodialysis when severe toxicity present and local dialysis unavailable."),
    ("06 — REFERENCES", "info", "EXTRIP Salicylates Recommendations; ACMT Guidance Document: Salicylate Toxicity; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Opioid Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Opioid toxicity is a potentially fatal cause of respiratory depression and altered consciousness.\n\n"
     "[color=#1E3A8A]Classic Findings:[/color]\n"
     "• Reduced respiratory rate or inadequate ventilation.\n"
     "• Reduced consciousness.\n"
     "• Miosis (pupils may not always be pinpoint).\n"
     "• Hypoxemia or hypercapnia.\n"
     "• Bradycardia and hypotension in severe cases.\n\n"
     "[color=#991B1B]IMPORTANT: Respiratory depression is the key immediate threat. Do NOT delay ventilation while waiting for naloxone.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, level of consciousness.\n"
     "• Open airway and provide bag-mask ventilation when ventilation inadequate.\n"
     "• Administer oxygen as indicated.\n"
     "• Obtain bedside glucose.\n"
     "• Establish IV or other appropriate access.\n"
     "• Apply continuous SpO2 monitoring and consider capnography.\n"
     "• Administer naloxone when opioid toxicity suspected and respiratory depression clinically significant.\n"
     "• Assess for co-ingestants, trauma, other causes of coma."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside glucose.\n"
     "• ECG and continuous cardiac monitoring in significant toxicity.\n"
     "• Blood gas if respiratory failure or persistent altered consciousness.\n"
     "• Electrolytes and renal function when clinically indicated.\n"
     "• CK, renal function, urinalysis if prolonged immobilization or rhabdomyolysis suspected.\n"
     "• Co-ingestant testing based on clinical context."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Naloxone[/color]\n"
     "• Indication: Suspected opioid-induced respiratory depression or life-threatening opioid toxicity.\n"
     "• Dose: For adult with suspected opioid dependence and spontaneous circulation: titrated IV approach may begin at 0.04 mg, followed by escalating doses according to response. For apnea/severe hypoxia/life-threatening respiratory depression: use appropriate larger initial dose or approved intranasal/IM product without delaying ventilation. Repeat doses as required.\n"
     "• Prioritize restoration of adequate breathing rather than complete wakefulness. Continue bag-mask ventilation as needed.\n"
     "• Reassess respiratory rate, oxygenation, mental status, BP, recurrence of symptoms.\n"
     "• Consider naloxone infusion if repeated boluses needed, particularly with long-acting opioids. Commonly used infusion: approximately two-thirds of effective reversal dose per hour, adjusted to clinical response and local protocol.\n"
     "• [color=#991B1B]Naloxone may wear off before the opioid, causing recurrent respiratory depression. Precipitated withdrawal may cause agitation, vomiting, occasionally severe complications. Patients exposed to long-acting opioids, methadone, or modified-release preparations may require prolonged observation or admission.[/color]\n\n"
     "[color=#1E3A8A]B. Supportive Care[/color]\n"
     "• Maintain ventilation and oxygenation. Treat hypoglycemia and other reversible causes. Evaluate for aspiration, pulmonary edema, trauma, co-ingestants. Monitor temperature, ECG, hemodynamics when indicated.\n"
     "• [color=#991B1B]A response to naloxone supports opioid involvement but does NOT exclude mixed poisoning or another concurrent diagnosis.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with recurrent respiratory depression, persistent hypoxia, aspiration, pulmonary edema, long-acting opioid exposure, or significant co-ingestants.\n"
     "• ICU care appropriate for respiratory failure, severe complications, or ongoing ventilatory support.\n"
     "• Discharge only after appropriate observation period, stable vital signs, adequate ambulation and mentation, and assessment of recurrence risk."),
    ("06 — REFERENCES", "info", "AHA 2025 Guidelines; WHO Community Management of Opioid Overdose; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Benzodiazepine and Sedative Overdose")] = [
    ("01 — RECOGNIZE", "info", 
     "Benzodiazepine overdose commonly causes CNS depression. Severe respiratory or cardiovascular compromise is more likely with large exposures, older or medically vulnerable patients, and co-ingestion of opioids, alcohol, or other sedatives.\n\n"
     "• Drowsiness and reduced consciousness. Slurred speech and ataxia.\n"
     "• Poor coordination and confusion.\n"
     "• Respiratory depression (especially in mixed ingestion).\n"
     "• Hypotension in severe cases."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, GCS.\n"
     "• Check bedside glucose.\n"
     "• Support airway and ventilation as required.\n"
     "• Establish IV access in significant poisoning.\n"
     "• Obtain ECG in suspected mixed or intentional overdose.\n"
     "• Determine whether opioids, alcohol, antidepressants, or other drugs may have been co-ingested.\n"
     "• Avoid routine flumazenil in undifferentiated poisoning."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside glucose.\n"
     "• ECG when significant overdose or co-ingestion suspected.\n"
     "• Blood gas for respiratory failure or persistent altered consciousness.\n"
     "• Electrolytes and renal function when indicated.\n"
     "• Acetaminophen and salicylate concentrations in appropriate intentional or uncertain ingestion cases.\n"
     "• Additional tests based on clinical presentation."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Supportive Care[/color]\n"
     "• No specific antidote routinely required for isolated benzodiazepine overdose.\n"
     "• Maintain airway patency and ventilation. Use positioning and suction when appropriate. Provide bag-mask ventilation or intubation if required.\n"
     "• Monitor SpO2, respiratory rate, BP, level of consciousness. Evaluate for aspiration, trauma, co-ingestants.\n"
     "• [color=#991B1B]Do NOT assume that all coma is caused by benzodiazepines, even when history suggests ingestion.[/color]\n\n"
     "[color=#1E3A8A]B. Flumazenil[/color]\n"
     "• Indication: Consider only in carefully selected cases (known iatrogenic benzodiazepine oversedation or selected isolated benzodiazepine exposures) after assessing seizure and dependence risks.\n"
     "• Common adult IV starting dose: 0.2 mg over ~15 seconds. Further doses per product label and institutional protocol.\n"
     "• Ensure resuscitation equipment and seizure treatment immediately available. Administer slowly under continuous monitoring.\n"
     "• Reassess consciousness, ventilation, vital signs. Monitor for resedation (flumazenil may wear off before benzodiazepine). Observe for seizures and withdrawal symptoms.\n"
     "• [color=#991B1B]Do NOT routinely use flumazenil in: Unknown/mixed overdose, chronic benzodiazepine dependence, seizure disorder or high seizure risk, suspected TCA or other proconvulsant co-ingestion, ECG findings suggestive of sodium-channel blockade. Flumazenil can precipitate seizures or acute withdrawal and may be more dangerous than supportive care in many overdose presentations.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with respiratory failure, persistent altered consciousness, aspiration, significant co-ingestion, or recurrent sedation.\n"
     "• ICU admission indicated for severe respiratory or cardiovascular compromise.\n"
     "• Discharge only after adequate clinical recovery and appropriate observation period based on agent, formulation, and co-ingestants."),
    ("06 — REFERENCES", "info", "Goldfrank's; Product prescribing information for flumazenil; Local poison-center guidance.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Tricyclic Antidepressant (TCA) Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "TCA poisoning can deteriorate rapidly and cause seizures, hypotension, and fatal ventricular dysrhythmias. Common agents include amitriptyline, imipramine, and clomipramine.\n\n"
     "• Altered consciousness, agitation, coma.\n"
     "• Anticholinergic features: dry skin, mydriasis, tachycardia, urinary retention, hyperthermia.\n"
     "• Seizures. Hypotension. QRS widening and ventricular dysrhythmias.\n\n"
     "[color=#1E3A8A]ECG Findings:[/color]\n"
     "• QRS widening, particularly > 100 ms.\n"
     "• Terminal R wave in lead aVR or increased R/S ratio in aVR.\n"
     "• QT prolongation. Ventricular dysrhythmias in severe poisoning.\n"
     "• [color=#991B1B]QRS widening and hemodynamic instability are key triggers for urgent sodium bicarbonate therapy.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Initiate ABC resuscitation and continuous cardiac monitoring.\n"
     "• Obtain 12-lead ECG immediately and repeat frequently.\n"
     "• Establish IV access.\n"
     "• Check bedside glucose, blood gas, electrolytes, potassium, renal function.\n"
     "• Treat hypotension and seizures promptly.\n"
     "• Contact critical care and toxicology early for significant poisoning."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Sodium Bicarbonate[/color]\n"
     "• Indications: QRS widening (commonly 100–110 ms or greater depending on protocol). Ventricular dysrhythmias. Hypotension attributable to TCA cardiotoxicity. Significant sodium-channel blockade with clinical instability.\n"
     "• Dose: 1–2 mEq/kg IV initial bolus. Repeat boluses according to ECG and hemodynamic response and local protocol. Titrate to QRS narrowing and clinical improvement. Common target pH ~7.50–7.55; avoid excessive alkalemia.\n"
     "• [color=#1E3A8A]Preparation:[/color] Sodium bicarbonate 8.4% contains 1 mEq/mL. Calculate dose using body weight. Verify concentration and total dose before administration.\n"
     "• Administer IV bolus under continuous ECG monitoring. Reassess QRS duration, rhythm, BP, perfusion after each dose. Monitor blood gas, Na+, K+, pH.\n"
     "• [color=#991B1B]Monitor for hypernatremia, hypokalemia, fluid overload, excessive alkalemia. Avoid class IA and IC antiarrhythmics in TCA-related sodium-channel blockade. Do NOT use physostigmine in suspected TCA poisoning. If intubation necessary, prevent peri-intubation acidosis and maintain adequate ventilation.[/color]\n\n"
     "[color=#1E3A8A]B. Seizure Management[/color]\n"
     "• Benzodiazepines are first-line for toxicologic seizures. Common adult option: Lorazepam 2–4 mg IV, repeated according to response and local seizure protocol.\n"
     "• Administer IV with airway and respiratory monitoring. Correct hypoglycemia and clinically significant metabolic abnormalities. Escalate promptly for persistent seizures or status epilepticus.\n"
     "• [color=#991B1B]Avoid phenytoin for TCA-induced seizures (can worsen cardiac conduction toxicity). Refractory seizures require critical care and specialist-guided treatment.[/color]\n\n"
     "[color=#1E3A8A]C. Hypotension[/color]\n"
     "• Give isotonic crystalloid when appropriate, reassessing after each bolus. Use sodium bicarbonate when hypotension associated with sodium-channel blockade. If hypotension persists, norepinephrine may be required under critical care guidance.\n"
     "• [color=#991B1B]Avoid excessive fluid administration in patients who develop pulmonary edema or have impaired cardiac function.[/color]\n\n"
     "[color=#1E3A8A]D. Activated Charcoal[/color]\n"
     "• Indication: Selected potentially serious ingestions when presentation early and airway protected.\n"
     "• Dose: Commonly 1 g/kg orally or via gastric tube, up to 50 g in adults, according to protocol.\n"
     "• Consider only after resuscitation and assessment of aspiration risk.\n"
     "• [color=#991B1B]Never give charcoal to patient with unprotected airway or delay essential resuscitation to administer it.[/color]"),
    ("04 — INVESTIGATIONS", "info", 
     "• Serial 12-lead ECGs.\n"
     "• Blood gas and pH.\n"
     "• Electrolytes, especially potassium and sodium.\n"
     "• Glucose and renal function.\n"
     "• Acetaminophen and salicylate concentrations when intentional or uncertain ingestion warrants testing.\n"
     "• Additional tests according to presentation and suspected co-ingestants."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with symptoms, ECG abnormalities, seizures, hypotension, or significant suspected ingestion.\n"
     "• ICU admission indicated for QRS widening with instability, ventricular dysrhythmias, recurrent seizures, severe altered consciousness, or vasopressor requirement.\n"
     "• Selected asymptomatic patients may be considered for discharge only after appropriate observation period, normal ECG, and specialist or local protocol clearance."),
    ("06 — REFERENCES", "info", "Royal Children's Hospital Melbourne TCA Poisoning Guideline; Goldfrank's; Queensland Poisons Information Centre Sodium Bicarbonate Guidance.")
]


# ==================== NEW TOXICOLOGY TOPICS (11-20) ====================

TOXICOLOGY_TOPICS[("Toxicology", "Beta-Blocker Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Beta-blocker overdose can cause severe bradycardia, hypotension, myocardial depression, conduction abnormalities, and cardiogenic shock.\n"
     "• Common Agents: Propranolol, Metoprolol, Atenolol, Bisoprolol, Carvedilol, Sotalol.\n"
     "• Bradycardia and hypotension. Dizziness, syncope, altered mental status. Cardiogenic shock and poor peripheral perfusion.\n"
     "• Hypoglycemia, particularly in children. Bronchospasm, especially with nonselective agents.\n"
     "• Seizures and QRS widening with propranolol toxicity. QT prolongation and torsades de pointes with sotalol toxicity.\n"
     "• [color=#991B1B]IMPORTANT: Propranolol is highly lipophilic and may cause seizures and sodium-channel blockade. Atenolol and sotalol toxicity may be complicated by renal impairment.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation. Establish IV access and continuous cardiac monitoring.\n"
     "• Obtain 12-lead ECG. Check bedside glucose immediately.\n"
     "• Measure electrolytes, renal function, blood gas, lactate in significant poisoning.\n"
     "• Treat symptomatic bradycardia and shock promptly.\n"
     "• Contact poison center, clinical toxicologist, and critical care team early."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial ECGs. Glucose and electrolytes (including potassium and magnesium).\n"
     "• Renal function. Blood gas and lactate in shock.\n"
     "• Echocardiography when cardiogenic shock or myocardial dysfunction suspected.\n"
     "• Additional investigations guided by co-ingestants and clinical findings."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Initial Hemodynamic Support[/color]\n"
     "• If hypotension and fluid administration appropriate: isotonic crystalloid bolus, commonly 250–500 mL in adult, then reassess. Use smaller aliquots when pulmonary edema or cardiac dysfunction suspected.\n"
     "• Vasopressors may be required for persistent shock.\n"
     "• [color=#991B1B]Excessive fluid administration may worsen pulmonary edema. Standard bradycardia treatment alone may be insufficient in severe beta-blocker poisoning.[/color]\n\n"
     "[color=#1E3A8A]B. Glucagon[/color]\n"
     "• Indication: Significant beta-blocker-associated bradycardia or hypotension, particularly when initial supportive measures insufficient.\n"
     "• Adult initial dose: 3–5 mg IV over approximately 1–2 minutes. If inadequate response, repeat or increase dose per local toxicology protocol. Continuous infusion may be considered after response to bolus.\n"
     "• [color=#991B1B]Vomiting is common and may be severe. Glucagon may have limited/transient effect and must not delay other therapies for shock.[/color]\n\n"
     "[color=#1E3A8A]C. High-Dose Insulin Euglycemia Therapy (HIET)[/color]\n"
     "• Indication: Severe beta-blocker toxicity with myocardial dysfunction or shock refractory to initial treatment.\n"
     "• Regular insulin: commonly 1 unit/kg IV bolus, then infusion at approximately 1 unit/kg/hour. Titrate per hemodynamic response and protocol; substantially higher doses may be required in refractory poisoning under specialist supervision.\n"
     "• Check glucose and potassium before treatment. Monitor glucose every 15–30 minutes initially. Monitor potassium frequently and replace when clinically indicated.\n"
     "• [color=#991B1B]HIET is a high-risk therapy requiring ICU-level monitoring and experienced staff. Hypoglycemia and hypokalemia are major complications. Insulin dosing must be prescribed in units, not milliliters; confirm concentration before administration.[/color]\n\n"
     "[color=#1E3A8A]D. Vasopressors[/color]\n"
     "• Norepinephrine may be useful for vasodilatory shock. Epinephrine may be considered when significant myocardial depression and bradycardia coexist.\n"
     "• Select and titrate therapy according to hemodynamic phenotype and specialist advice.\n"
     "• [color=#991B1B]No single vasopressor is optimal for every beta-blocker overdose. Escalate early when shock persists.[/color]\n\n"
     "[color=#1E3A8A]E. Sodium Bicarbonate[/color]\n"
     "• Indication: QRS widening or ventricular dysrhythmias associated with sodium-channel blockade, particularly in propranolol poisoning.\n"
     "• Common initial adult dose: 1–2 mEq/kg IV. Repeat according to ECG response and local toxicology protocol.\n"
     "• Monitor QRS duration, rhythm, blood gas, sodium, potassium. Avoid excessive alkalemia and hypernatremia.\n\n"
     "[color=#1E3A8A]Refractory Shock[/color]\n"
     "• Specialist-directed options: HIET escalation, lipid emulsion in selected cases (severe propranolol toxicity), temporary pacing for selected conduction abnormalities, VA-ECMO for refractory cardiogenic shock/cardiac arrest."),
    ("05 — DISPOSITION", "warning", 
     "• Admit significant symptomatic overdoses for continuous monitoring.\n"
     "• ICU admission indicated for hypotension, significant bradycardia, conduction abnormalities, seizures, myocardial dysfunction, or need for antidotal infusions.\n"
     "• Consider prolonged observation for sustained-release preparations and agents with delayed toxicity."),
    ("REFERENCES", "info", "Goldfrank's Toxicologic Emergencies; AHA 2025 Guidelines; Poison-center protocols for beta-blocker overdose and high-dose insulin therapy.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Calcium Channel Blocker Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Calcium channel blocker (CCB) overdose may cause profound vasodilation, bradycardia, myocardial depression, and shock. Verapamil and diltiazem frequently produce marked cardiac toxicity, while dihydropyridines such as amlodipine may initially cause prominent vasodilatory shock.\n"
     "• Common Agents: Amlodipine, Nifedipine, Verapamil, Diltiazem.\n"
     "• Hypotension and shock. Bradycardia or AV block.\n"
     "• Hyperglycemia due to impaired insulin secretion and utilization. Altered mental status and elevated lactate. Pulmonary edema in severe cases.\n"
     "• [color=#991B1B]Hyperglycemia may support diagnosis of significant CCB toxicity but is not diagnostic by itself.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Initiate ABC resuscitation. Establish IV access and continuous ECG monitoring.\n"
     "• Obtain 12-lead ECG. Check bedside glucose immediately.\n"
     "• Measure electrolytes, renal function, blood gas, lactate.\n"
     "• Consider bedside echocardiography in shock.\n"
     "• Contact toxicology and critical care early."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV Calcium[/color]\n"
     "• Indication: Significant CCB-associated hypotension, bradycardia, or myocardial dysfunction.\n"
     "• One commonly used adult regimen: Calcium chloride 10%: 10–20 mL IV, OR Calcium gluconate 10%: 30–60 mL IV. Repeat doses may be required according to clinical response, ECG, and ionized calcium.\n"
     "• [color=#991B1B]Verify exact calcium salt and concentration. Calcium chloride 10% contains approximately three times as much elemental calcium per mL as calcium gluconate 10%. Use secure IV line; central access preferred for calcium chloride when feasible. Do NOT substitute equal volumes of calcium chloride and calcium gluconate. Calcium chloride extravasation can cause severe tissue injury. Avoid excessive hypercalcemia.[/color]\n\n"
     "[color=#1E3A8A]B. High-Dose Insulin Euglycemia Therapy (HIET)[/color]\n"
     "• Indication: Significant CCB-associated shock or myocardial dysfunction, especially when initial therapy inadequate.\n"
     "• Regular insulin: commonly 1 unit/kg IV bolus, then infusion at approximately 1 unit/kg/hour. Titrate to clinical response under high-dose insulin protocol; higher doses may be required in severe refractory poisoning.\n"
     "• Check glucose and potassium before treatment. Monitor glucose every 15–30 minutes during initiation and dose changes, then at protocol-defined intervals once stable.\n"
     "• [color=#991B1B]HIET is a high-risk ICU therapy. Hypoglycemia and hypokalemia can be life-threatening. Use a dedicated protocol and independent dose verification.[/color]\n\n"
     "[color=#1E3A8A]C. Vasopressors[/color]\n"
     "• Norepinephrine commonly used for significant vasodilatory shock. Epinephrine may be useful when myocardial depression or bradycardia prominent. Combined vasopressor therapy may be required in severe poisoning.\n"
     "• Titrate to adequate perfusion and institution's blood pressure target.\n"
     "• [color=#991B1B]Vasopressors may not adequately correct myocardial depression without adjunctive therapy.[/color]\n\n"
     "[color=#1E3A8A]D. Additional Therapies[/color]\n"
     "• Consider glucagon in selected cases (evidence and response variable).\n"
     "• Consider lipid emulsion only in selected refractory cases after specialist consultation.\n"
     "• Consider VA-ECMO for refractory cardiogenic shock or cardiac arrest where available.\n"
     "• Do NOT delay escalation when shock is worsening."),
    ("04 — INVESTIGATIONS", "info", 
     "• Serial ECGs. Glucose and electrolytes.\n"
     "• Ionized calcium during IV calcium treatment.\n"
     "• Renal function. Blood gas and lactate.\n"
     "• Echocardiography when myocardial dysfunction suspected."),
    ("05 — DISPOSITION", "warning", 
     "• Admit significant overdoses for continuous cardiac and hemodynamic monitoring.\n"
     "• ICU admission indicated for hypotension, bradycardia, AV block, hyperglycemia with systemic toxicity, myocardial dysfunction, or need for HIET or vasopressors.\n"
     "• Sustained-release preparations may require prolonged observation."),
    ("REFERENCES", "info", "Goldfrank's Toxicologic Emergencies; AHA 2025 Guidelines; Poison-center protocols for calcium channel blocker toxicity and high-dose insulin therapy.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Digoxin Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Digoxin toxicity may result from acute overdose, chronic accumulation, renal impairment, or interactions with other medications.\n"
     "• Nausea, vomiting, anorexia, abdominal discomfort. Weakness, confusion, visual disturbances.\n"
     "• Bradycardia and AV block. Atrial tachycardia with block. Ventricular ectopy or ventricular dysrhythmias. Hyperkalemia in severe acute poisoning.\n"
     "• [color=#991B1B]IMPORTANT: Digoxin toxicity can occur at concentrations that overlap with therapeutic ranges. Clinical findings, renal function, ECG, potassium, and timing of last dose are essential to interpretation.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and establish IV access.\n"
     "• Obtain 12-lead ECG and continuous cardiac monitoring.\n"
     "• Check potassium, magnesium, calcium, renal function, glucose.\n"
     "• Obtain serum digoxin concentration when indicated.\n"
     "• Determine timing of last dose and whether exposure was acute or chronic.\n"
     "• Contact toxicology and cardiology early for significant toxicity."),
    ("03 — INVESTIGATIONS", "info", 
     "• ECG and continuous rhythm monitoring. Serum potassium and magnesium. Urea and creatinine.\n"
     "• Serum digoxin concentration. Blood gas and lactate if unstable.\n"
     "• Additional tests for possible co-ingestants.\n"
     "• [color=#991B1B]A digoxin level obtained too soon after ingestion may not reflect tissue distribution. When feasible, measure at least 6 hours after last dose, but do NOT delay emergency treatment in unstable patient.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Digoxin Immune Fab[/color]\n"
     "• Indications: Life-threatening toxicity (ventricular tachycardia/fibrillation, severe symptomatic bradycardia or high-grade AV block not responding to appropriate measures, significant hyperkalemia attributable to acute digoxin poisoning, hemodynamic instability, large acute ingestion meeting accepted criteria).\n"
     "• Dose: Use product-specific calculation based on estimated ingested dose or serum digoxin concentration when reliable. In immediately life-threatening toxicity, follow emergency institutional protocol and consult toxicology urgently.\n"
     "• [color=#991B1B]Potassium can fall rapidly after successful Fab treatment; monitor closely. Hypersensitivity reactions can occur. Do NOT delay Fab in life-threatening poisoning while waiting for confirmatory serum concentration.[/color]\n\n"
     "[color=#1E3A8A]B. Electrolyte Management[/color]\n"
     "• Correct hypokalemia and hypomagnesemia carefully when present. Treat clinically significant hyperkalemia according to severity and mechanism. In severe acute digoxin toxicity, Fab is preferred specific therapy for digoxin-mediated hyperkalemia.\n\n"
     "[color=#1E3A8A]C. Bradyarrhythmias[/color]\n"
     "• Atropine may be used for symptomatic bradycardia while preparing definitive treatment. Temporary pacing may be necessary in selected unstable cases but requires expert management. Avoid provoking ventricular dysrhythmias during emergency procedures.\n"
     "• [color=#991B1B]Fab is definitive specific treatment for life-threatening digoxin toxicity. Routine electrical cardioversion can precipitate serious dysrhythmias in digoxin-toxic patients; reserve for situations in which necessary and manage with expert input.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with clinically significant toxicity, ECG abnormalities, electrolyte disturbances, or suspected acute overdose.\n"
     "• ICU admission indicated for ventricular dysrhythmias, high-grade AV block, severe hyperkalemia, or hemodynamic instability.\n"
     "• Observation duration should account for renal function, formulation, exposure pattern, and recurrence risk."),
    ("REFERENCES", "info", "Goldfrank's; Digoxin Immune Fab product prescribing information; Poison-center and cardiology protocols.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Insulin and Sulfonylurea Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Insulin and sulfonylurea overdose can cause profound, recurrent, and prolonged hypoglycemia.\n"
     "• Common Causes: Excess insulin administration, accidental administration of another patient's insulin, intentional insulin overdose, sulfonylurea ingestion (glibenclamide/glyburide, glimepiride, gliclazide), medication errors, reduced food intake after glucose-lowering therapy.\n"
     "• Sweating, tremor, palpitations, hunger. Confusion, behavioral changes, reduced consciousness. Seizures or coma. Persistent or recurrent hypoglycemia. Hypokalemia, particularly after substantial insulin exposure."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Check bedside glucose immediately. Treat hypoglycemia without delay.\n"
     "• Assess airway, breathing, circulation, neurologic status. Establish IV access.\n"
     "• Identify exact insulin or sulfonylurea, dose, formulation, time of exposure.\n"
     "• Obtain ECG and electrolytes in significant poisoning.\n"
     "• Contact toxicology early for long-acting insulin or sulfonylurea exposure."),
    ("03 — INVESTIGATIONS", "info", 
     "• Frequent bedside glucose measurements.\n"
     "• Serum potassium, magnesium, phosphate, renal function when indicated.\n"
     "• ECG in significant poisoning or electrolyte abnormalities.\n"
     "• Additional investigations if cause of hypoglycemia unclear."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV Dextrose for Acute Hypoglycemia[/color]\n"
     "• Indication: Symptomatic or clinically significant hypoglycemia, especially altered consciousness or seizures.\n"
     "• Adults: commonly 10–25 g IV dextrose, titrated to glucose response (e.g., 100–250 mL of 10% dextrose for 10–25 g). In severe hypoglycemia, use locally approved concentration and dose. Pediatric dosing must be weight-based.\n"
     "• Recheck glucose promptly after treatment, commonly within 10–15 minutes. Repeat if hypoglycemia persists. Once consciousness restored, provide oral carbohydrate when safe.\n"
     "• [color=#991B1B]Avoid unnecessary large glucose loads that produce extreme hyperglycemia. Do NOT delay IV treatment in severe symptomatic hypoglycemia.[/color]\n\n"
     "[color=#1E3A8A]B. Continuous Dextrose Infusion for Insulin Overdose[/color]\n"
     "• Indication: Recurrent hypoglycemia or large insulin exposure requiring sustained glucose support.\n"
     "• Select concentration and infusion rate according to serial glucose measurements and ongoing insulin effect. No single fixed infusion rate suitable for every insulin overdose.\n"
     "• Titrate to maintain glucose within institution's target range. Monitor glucose frequently during initiation and rate changes. Monitor potassium, magnesium, phosphate, fluid balance.\n"
     "• [color=#991B1B]Long-acting insulin and large subcutaneous injections can produce prolonged toxicity. Avoid excessive fluid administration; more concentrated glucose solution may be needed under appropriate protocols.[/color]\n\n"
     "[color=#1E3A8A]C. Octreotide for Sulfonylurea-Induced Hypoglycemia[/color]\n"
     "• Indication: Recurrent or persistent hypoglycemia after sulfonylurea ingestion, particularly when dextrose treatment alone leads to repeated episodes.\n"
     "• Commonly used adult regimen: octreotide 50–100 micrograms SC every 6 hours. IV administration or infusion may be used under specialist protocol for severe cases. Pediatric dosing requires toxicology guidance and weight-based protocol.\n"
     "• [color=#991B1B]Octreotide suppresses insulin release but does NOT replace immediate glucose correction. Sulfonylurea toxicity may recur after initial improvement; prolonged observation often required.[/color]\n\n"
     "[color=#1E3A8A]D. Glucagon[/color]\n"
     "• Indication: Temporary treatment for hypoglycemia when IV access not immediately available, depending on clinical setting and product.\n"
     "• Adult emergency dosing is product-specific; common preparations use 1 mg IM or SC.\n"
     "• [color=#991B1B]Glucagon may be ineffective when hepatic glycogen stores depleted. It is NOT definitive treatment for sulfonylurea poisoning and may be followed by recurrent hypoglycemia.[/color]"),
    ("05 — ADDITIONAL MANAGEMENT", "info", 
     "• Correct potassium, magnesium, or phosphate abnormalities when indicated.\n"
     "• Consult toxicology regarding large or long-acting insulin exposures.\n"
     "• Consider critical care setting for recurrent hypoglycemia, seizures, or high glucose-infusion requirements.\n"
     "• Evaluate for intentional self-harm and medication-safety issues."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with recurrent hypoglycemia or significant insulin or sulfonylurea exposure.\n"
     "• ICU care indicated for severe neurologic manifestations, recurrent seizures, hemodynamic instability, or intensive glucose support.\n"
     "• Observation must be prolonged when agent or formulation can cause delayed or recurrent hypoglycemia."),
    ("REFERENCES", "info", "Goldfrank's; Poison-center protocols for sulfonylurea and insulin overdose; Local emergency hypoglycemia protocols.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Organophosphate and Carbamate Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Organophosphates and carbamates inhibit acetylcholinesterase, producing excessive acetylcholine activity at muscarinic and nicotinic receptors and within the CNS.\n\n"
     "[color=#1E3A8A]Common Exposure Sources:[/color] Agricultural insecticides, household pesticides, occupational exposure, intentional ingestion.\n\n"
     "[color=#1E3A8A]Muscarinic Features:[/color] Salivation, lacrimation, bronchorrhea, bronchospasm, sweating, miosis, vomiting, diarrhea, abdominal cramping, bradycardia, urinary incontinence.\n\n"
     "[color=#1E3A8A]Nicotinic Features:[/color] Fasciculations, muscle weakness, paralysis, respiratory muscle failure. Tachycardia or hypertension may also occur.\n\n"
     "[color=#1E3A8A]CNS Features:[/color] Anxiety, agitation, confusion, seizures, coma, respiratory depression.\n\n"
     "[color=#991B1B]IMPORTANT: Respiratory failure may result from bronchorrhea, bronchospasm, central respiratory depression, and respiratory muscle weakness simultaneously.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]1. Protect Staff[/color]\n"
     "• Use appropriate PPE. Avoid direct contact with contaminated clothing, vomitus, or skin. Remove contaminated clothing carefully and isolate it. Wash exposed skin with soap and water. Prevent secondary contamination.\n\n"
     "[color=#1E3A8A]2. Airway and Breathing[/color]\n"
     "• Suction secretions and provide oxygen. Use bag-mask ventilation and intubation when required. Anticipate prolonged ventilatory support.\n"
     "• [color=#991B1B]Avoid succinylcholine when possible because cholinesterase inhibition may prolong its paralytic effect; choose an alternative neuromuscular blocker under the airway protocol.[/color]\n\n"
     "[color=#1E3A8A]3. Circulation and Monitoring[/color]\n"
     "• Establish IV access. Apply continuous ECG and SpO2 monitoring. Check glucose, electrolytes, blood gas, renal function. Obtain chest imaging if aspiration/pulmonary edema suspected."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Atropine[/color]\n"
     "• Indication: Clinically significant cholinergic toxicity, especially bronchorrhea, bronchospasm, respiratory compromise, or bradycardia.\n"
     "• Adults: commonly 1–3 mg IV initially. In severe poisoning, rapidly reassess and double the dose every 3–5 minutes until respiratory secretions and ventilation improve. Very large cumulative doses may be required.\n"
     "• [color=#1E3A8A]Monitoring:[/color] Titrate to improvement in bronchial secretions, bronchospasm, oxygenation, ventilation. Once adequate atropinization achieved, continuous infusion may be used in severe cases; common starting approach: 10–20% of total loading dose per hour, adjusted to clinical response.\n"
     "• [color=#991B1B]Do NOT use pupil size or heart rate alone as endpoint. Persistent muscle weakness may continue despite adequate atropine. Recurrent bronchorrhea may require additional boluses or infusion adjustment.[/color]\n\n"
     "[color=#1E3A8A]B. Pralidoxime (2-PAM)[/color]\n"
     "• Indication: Significant organophosphate poisoning, particularly with fasciculations, weakness, respiratory muscle involvement, or severe systemic toxicity.\n"
     "• Adult loading dose commonly 1–2 g IV over approximately 15–30 minutes. Continuous infusion or repeat dosing may follow per specific product and local toxicology protocol. Pediatric doses weight-based.\n"
     "• [color=#991B1B]Do NOT delay atropine or airway support while preparing pralidoxime. Efficacy varies with compound, time since exposure, and whether enzyme has undergone aging. Carbamate poisoning differs from organophosphate poisoning; consult toxicology regarding oxime use when agent uncertain.[/color]\n\n"
     "[color=#1E3A8A]C. Seizure Management[/color]\n"
     "• Benzodiazepines first-line. Common adult option: lorazepam 2–4 mg IV, repeated according to response and status epilepticus protocol. Provide airway support and monitor oxygenation. Escalate promptly for persistent seizures."),
    ("04 — INVESTIGATIONS", "info", 
     "• Cholinesterase activity may support diagnosis but should NOT delay treatment. Plasma butyrylcholinesterase and red-cell acetylcholinesterase may be useful where available.\n"
     "• ECG and continuous rhythm monitoring. Blood gas, electrolytes, glucose, renal function.\n"
     "• Chest imaging when aspiration or pulmonary complications suspected. CK and renal function when prolonged seizures or muscle injury occur."),
    ("05 — COMPLICATIONS", "danger", 
     "• Respiratory failure. Aspiration pneumonitis.\n"
     "• Intermediate syndrome with delayed muscle weakness. Recurrent cholinergic symptoms.\n"
     "• Delayed neuropathy with certain organophosphates. Hypoxic brain injury after severe respiratory compromise."),
    ("06 — DISPOSITION", "warning", 
     "• ICU admission indicated for respiratory compromise, significant bronchorrhea, muscle weakness, altered consciousness, seizures, or ongoing atropine infusion.\n"
     "• Patients may require prolonged observation after initial improvement because respiratory muscle weakness or recurrent toxicity can develop later.\n"
     "• Discharge requires stable respiratory function, no recurrent cholinergic signs, and an appropriate observation period."),
    ("REFERENCES", "info", "WHO Clinical Management of Acute Pesticide Intoxication; Goldfrank's; Local poison-center and organophosphate poisoning protocols.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Methanol Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Methanol is a toxic alcohol found in some solvents, fuels, and adulterated alcoholic products. Toxicity is caused primarily by formate, which produces metabolic acidosis and optic nerve injury.\n"
     "• Nausea, vomiting, abdominal pain, headache. Visual blurring, photophobia, altered color perception, or visual loss. Tachypnea due to metabolic acidosis. Confusion, seizures, coma in severe cases.\n"
     "• High anion-gap metabolic acidosis. Elevated osmolar gap may occur, particularly early.\n"
     "• [color=#991B1B]IMPORTANT: Symptoms may be delayed for several hours. Absence of visual symptoms or a normal early osmolar gap does NOT exclude methanol poisoning.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, neurologic status. Obtain IV access and continuous monitoring.\n"
     "• Check bedside glucose immediately.\n"
     "• Obtain blood gas, electrolytes, bicarbonate, anion gap, renal function, measured serum osmolality.\n"
     "• Send methanol concentration if available.\n"
     "• Contact toxicology and nephrology urgently.\n"
     "• Start antidotal treatment promptly when clinical suspicion and exposure history justify it; do NOT wait for confirmatory levels in high-risk patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood gas, pH, bicarbonate, anion gap. Measured serum osmolality and calculated osmolar gap.\n"
     "• Serum methanol concentration when available. Electrolytes, glucose, urea, creatinine.\n"
     "• Lactate and ketones when clinically indicated. Visual acuity, pupils, neurologic examination. ECG in significant poisoning.\n"
     "• [color=#991B1B]Interpretation: The osmolar gap can be elevated early and decrease as methanol is metabolized, while the anion-gap metabolic acidosis becomes more prominent. Neither gap alone can reliably exclude poisoning.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fomepizole[/color]\n"
     "• Indication: Suspected or confirmed methanol poisoning meeting accepted treatment criteria.\n"
     "• Commonly used adult and pediatric regimen: Loading dose 15 mg/kg IV. Doses 2–5: 10 mg/kg IV every 12 hours. Subsequent doses: increase to 15 mg/kg every 12 hours because of enzyme autoinduction. During hemodialysis, dosing intervals must be shortened because fomepizole is dialyzable.\n"
     "• [color=#991B1B]Do NOT delay treatment in strongly suspected, clinically significant exposure while waiting for methanol level. Fomepizole prevents further toxic metabolite formation but does NOT remove formate already present or correct severe acidosis by itself.[/color]\n\n"
     "[color=#1E3A8A]B. Sodium Bicarbonate[/color]\n"
     "• Indication: Significant metabolic acidemia.\n"
     "• Individualize according to pH, clinical status, sodium concentration, institutional toxicology protocol. No single fixed dose appropriate for all poisonings.\n"
     "• [color=#991B1B]Bicarbonate is supportive treatment, NOT a substitute for fomepizole or hemodialysis when indicated.[/color]\n\n"
     "[color=#1E3A8A]C. Hemodialysis[/color]\n"
     "• Indications: Visual impairment attributable to methanol. Severe metabolic acidosis. Coma, seizures, significant neurologic abnormalities. Renal impairment or other severe clinical manifestations. High methanol concentration meeting accepted extracorporeal treatment criteria. Persistent acidosis or clinical deterioration despite treatment.\n"
     "• Continue fomepizole during dialysis, adjusting dose and interval. Monitor blood gas, electrolytes, methanol concentration, clinical status. Reassess for rebound or ongoing absorption.\n"
     "• [color=#991B1B]Dialysis decisions should follow current EXTRIP recommendations and specialist advice, considering methanol concentration, acid-base status, clinical findings, availability of antidote.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• ICU admission for severe acidosis, visual symptoms, seizures, coma, or hemodynamic instability.\n"
     "• Urgent transfer to dialysis-capable facility when indicated.\n"
     "• Arrange ophthalmology assessment for visual symptoms and follow-up for potential permanent visual impairment."),
    ("REFERENCES", "info", "EXTRIP Workgroup Methanol Recommendations; Fomepizole product prescribing information; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Ethylene Glycol Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Ethylene glycol is commonly found in antifreeze and some industrial fluids. Its toxic metabolites cause metabolic acidosis, neurologic toxicity, and acute kidney injury.\n\n"
     "[color=#1E3A8A]Early phase:[/color] Intoxication-like behavior, dizziness, nausea, vomiting. Ataxia or altered mental status.\n\n"
     "[color=#1E3A8A]Intermediate phase:[/color] Tachypnea and high anion-gap metabolic acidosis. Tachycardia and cardiovascular instability in severe cases.\n\n"
     "[color=#1E3A8A]Later phase:[/color] Acute kidney injury, flank pain, oliguria, or anuria. Hypocalcemia and possible calcium oxalate crystalluria. Seizures or coma in severe poisoning.\n"
     "• [color=#991B1B]Absence of calcium oxalate crystals does NOT exclude ethylene glycol poisoning.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation. Obtain IV access and continuous monitoring.\n"
     "• Check bedside glucose.\n"
     "• Obtain blood gas, electrolytes, bicarbonate, anion gap, renal function, calcium, measured osmolality.\n"
     "• Send ethylene glycol concentration when available.\n"
     "• Contact toxicology and nephrology urgently.\n"
     "• Begin fomepizole promptly when indicated without waiting for confirmatory testing."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood gas, pH, bicarbonate, anion gap. Measured serum osmolality and calculated osmolar gap.\n"
     "• Ethylene glycol concentration, if available. Electrolytes, calcium, magnesium, renal function.\n"
     "• Urinalysis and microscopy. Lactate, glucose, ECG as clinically indicated.\n"
     "• [color=#991B1B]Interpretation: Early poisoning may produce elevated osmolar gap before severe acidosis develops. As ethylene glycol is metabolized, osmolar gap may decline while anion gap increases.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fomepizole[/color]\n"
     "• Indication: Suspected or confirmed ethylene glycol poisoning meeting accepted treatment criteria.\n"
     "• Commonly used regimen: Loading dose 15 mg/kg IV. Doses 2–5: 10 mg/kg IV every 12 hours. Subsequent doses: 15 mg/kg IV every 12 hours. During hemodialysis, adjust dose interval per product label and protocol.\n"
     "• [color=#991B1B]Do NOT delay antidotal therapy when suspicion is high and consequences of delay are significant. Fomepizole prevents formation of additional toxic metabolites but does NOT directly reverse established kidney injury.[/color]\n\n"
     "[color=#1E3A8A]B. Sodium Bicarbonate[/color]\n"
     "• Indication: Significant metabolic acidemia. Individualize according to degree of acidemia and clinical condition.\n"
     "• [color=#991B1B]Avoid excessive alkalemia and fluid overload.[/color]\n\n"
     "[color=#1E3A8A]C. Thiamine and Pyridoxine[/color]\n"
     "• May be considered as adjuncts in selected cases per institutional toxicology protocol. Must never delay fomepizole or indicated hemodialysis.\n\n"
     "[color=#1E3A8A]D. Hemodialysis[/color]\n"
     "• Indications: Severe metabolic acidosis. Significant acute kidney injury. Coma, seizures, other severe clinical manifestations. High ethylene glycol burden or anion-gap abnormalities meeting accepted EXTRIP criteria. Deterioration despite appropriate treatment.\n"
     "• Continue fomepizole with dialysis-adjusted dosing. Monitor pH, electrolytes, renal function, toxin concentrations. Reassess need for continued treatment after dialysis.\n"
     "• [color=#991B1B]Use current EXTRIP criteria and toxicology/nephrology advice. Do NOT base dialysis decision on osmolar gap alone.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• ICU admission for severe acidosis, seizures, coma, shock, or major electrolyte abnormalities.\n"
     "• Urgent transfer to dialysis-capable facility when indicated.\n"
     "• Monitor renal function and urine output for evolving kidney injury."),
    ("REFERENCES", "info", "EXTRIP Workgroup Ethylene Glycol Recommendations; Fomepizole product prescribing information; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Carbon Monoxide Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Carbon monoxide (CO) is a colorless, odorless gas produced by incomplete combustion. It reduces oxygen delivery and interferes with cellular oxygen utilization.\n\n"
     "[color=#1E3A8A]Common Sources:[/color] Generators used indoors or near windows. Charcoal or fuel-burning heaters in poorly ventilated rooms. Vehicle exhaust. Fires and faulty combustion appliances.\n\n"
     "• Headache, dizziness, nausea, vomiting. Confusion, ataxia, syncope.\n"
     "• Chest pain, arrhythmias, myocardial ischemia. Seizures or coma in severe poisoning. Fetal distress in pregnant patients.\n"
     "• [color=#991B1B]IMPORTANT: A normal conventional pulse oximeter reading does NOT exclude carbon monoxide poisoning.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Remove patient from exposure to safe environment without exposing rescuers.\n"
     "• Administer 100% oxygen immediately.\n"
     "• Assess airway, breathing, circulation, neurologic status, glucose.\n"
     "• Obtain IV access and ECG monitoring in significant cases.\n"
     "• Request blood co-oximetry for carboxyhemoglobin (COHb).\n"
     "• Assess for smoke inhalation, trauma, possible cyanide co-poisoning in fire victims.\n"
     "• Contact hyperbaric oxygen service or toxicology specialist for severe presentations."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood co-oximetry for COHb. Blood gas and lactate in significant poisoning.\n"
     "• ECG and cardiac troponin for chest pain, significant exposure, or cardiac risk.\n"
     "• Neurologic assessment. Pregnancy assessment when relevant.\n"
     "• Additional evaluation for airway injury or associated toxic exposures.\n"
     "• [color=#991B1B]COHb concentration may fall after oxygen treatment and may underestimate peak exposure. COHb concentration does NOT correlate reliably with clinical severity or long-term neurologic outcomes. Interpret results alongside exposure history, symptoms, timing, and treatment already given.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. High-Concentration Oxygen[/color]\n"
     "• Indication: Suspected or confirmed CO poisoning.\n"
     "• Administer 100% oxygen using non-rebreather mask with adequate flow, or 100% oxygen through advanced airway when clinically indicated.\n"
     "• Start immediately and continue until symptoms resolve and specialist-guided clinical criteria met. Monitor mental status, vital signs, ECG, clinical response. Repeat COHb testing when it will assist management, without delaying treatment.\n"
     "• [color=#991B1B]Do NOT use a normal pulse oximeter reading to rule out CO poisoning. Do NOT withhold oxygen while waiting for laboratory confirmation.[/color]\n\n"
     "[color=#1E3A8A]B. Hyperbaric Oxygen Consultation[/color]\n"
     "• Consider urgent consultation when: Loss of consciousness or persistent neurologic impairment. Cardiac ischemia, significant myocardial injury, serious dysrhythmia. Severe metabolic acidosis. Significant COHb elevation in appropriate clinical context. Pregnancy with significant exposure or concerning maternal/fetal findings.\n"
     "• [color=#991B1B]There is no single COHb threshold that determines every hyperbaric treatment decision. Hyperbaric oxygen availability should NOT delay initial high-concentration oxygen or essential resuscitation.[/color]\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• Treat seizures and shock per emergency protocols. Assess myocardial injury and manage complications. In smoke inhalation, evaluate for concomitant cyanide poisoning when clinically indicated."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with persistent neurologic symptoms, syncope, myocardial injury, severe acidosis, pregnancy-related concerns, or significant ongoing symptoms.\n"
     "• ICU care appropriate for coma, seizures, hemodynamic instability, or respiratory failure.\n"
     "• Provide discharge instructions about delayed neurologic symptoms and arrange follow-up when indicated."),
    ("REFERENCES", "info", "CDC Clinical Guidance for Carbon Monoxide Poisoning; Undersea and Hyperbaric Medical Society Indications; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Cyanide Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Cyanide inhibits cellular oxygen utilization and can cause rapid cardiovascular collapse. Severe poisoning may occur after exposure to certain industrial chemicals, smoke from enclosed-space fires, or other cyanide-containing materials.\n"
     "• Sudden altered consciousness, seizures, coma. Hypotension, shock, cardiac arrest.\n"
     "• Severe metabolic acidosis. Markedly elevated lactate. Respiratory distress.\n"
     "• Possible soot, airway injury, or smoke exposure in fire victims.\n"
     "• [color=#991B1B]IMPORTANT: No single clinical sign or lactate value definitively diagnoses cyanide poisoning. Interpret findings in context of exposure and clinical presentation.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure scene safety and appropriate responder PPE. Remove patient from exposure when safe.\n"
     "• Initiate ABC resuscitation and high-concentration oxygen.\n"
     "• Establish IV or intraosseous access.\n"
     "• Treat seizures, shock, cardiac arrest per resuscitation protocols.\n"
     "• Obtain blood gas, lactate, electrolytes, ECG.\n"
     "• Administer appropriate antidote promptly when severe cyanide poisoning strongly suspected. Do NOT delay treatment for cyanide concentration."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood gas and lactate. Electrolytes, glucose, renal function. ECG and cardiac monitoring.\n"
     "• Co-oximetry and carboxyhemoglobin when smoke inhalation suspected.\n"
     "• Cyanide concentration if available, recognizing results generally not fast enough to guide initial resuscitation."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Hydroxocobalamin[/color]\n"
     "• Indication: Suspected severe cyanide poisoning, particularly with cardiovascular instability, severe lactic acidosis, seizures, or collapse following compatible exposure.\n"
     "• Adults: 5 g IV over approximately 15 minutes. A second 5 g dose may be administered according to clinical severity and response, following product label and emergency protocol. Pediatric dosing weight-based.\n"
     "• [color=#991B1B]Hydroxocobalamin commonly causes red discoloration of skin and urine. It can interfere with laboratory assays and some dialysis blood-leak detection systems. Hypersensitivity reactions and hypertension may occur. Do NOT delay administration in critically ill patient with strongly compatible exposure.[/color]\n\n"
     "[color=#1E3A8A]B. Sodium Nitrite and Sodium Thiosulfate[/color]\n"
     "• Alternatives in selected circumstances when hydroxocobalamin unavailable or when specialist protocol supports use.\n"
     "• [color=#991B1B]Sodium nitrite can cause methemoglobinemia and hypotension. It may be particularly hazardous when carbon monoxide poisoning or severe anemia also suspected. In smoke-inhalation victims with possible combined CO and cyanide exposure, hydroxocobalamin generally preferred when available.[/color]\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• Provide high-concentration oxygen. Maintain ventilation and circulation. Treat seizures with benzodiazepines. Treat shock with appropriate resuscitation and vasopressors. Manage cardiac arrest using standard protocols while treating suspected toxic cause."),
    ("05 — DISPOSITION", "warning", 
     "• ICU admission indicated for significant suspected cyanide poisoning, antidote administration with ongoing symptoms, severe acidosis, shock, seizures, or respiratory failure.\n"
     "• Evaluate smoke-inhalation victims for coexisting carbon monoxide exposure and airway injury.\n"
     "• Monitor for recurrent or persistent metabolic abnormalities and organ injury."),
    ("REFERENCES", "info", "Cyanokit (hydroxocobalamin) prescribing information; AHA 2025 Guidelines; Goldfrank's.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Corrosive Ingestion")] = [
    ("01 — RECOGNIZE", "info", 
     "Corrosive ingestion can cause chemical burns of the mouth, pharynx, esophagus, and stomach. Severe cases may lead to airway edema, perforation, mediastinitis, peritonitis, and later esophageal strictures.\n\n"
     "[color=#1E3A8A]Common Agents:[/color] Strong acids, strong alkalis (drain/oven cleaners), industrial cleaning agents, concentrated household chemicals.\n\n"
     "• Oral burns, drooling, painful swallowing. Dysphagia or inability to swallow secretions.\n"
     "• Hoarseness, stridor, respiratory distress. Chest or abdominal pain. Vomiting or hematemesis. Signs of shock, perforation, or peritonitis in severe cases.\n"
     "• [color=#991B1B]IMPORTANT: Absence of visible oral burns does NOT exclude serious esophageal or gastric injury.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]1. Airway[/color]\n"
     "• Assess voice, swallowing, drooling, stridor, respiratory effort.\n"
     "• Obtain early anesthesia and ENT support if airway edema suspected. Consider early controlled intubation when progressive airway compromise likely. Prepare for difficult airway and surgical airway rescue.\n"
     "• [color=#991B1B]Delayed intubation can become extremely difficult as edema progresses.[/color]\n\n"
     "[color=#1E3A8A]2. Circulation and Stabilization[/color]\n"
     "• Establish IV access. Monitor vital signs and SpO2. Give IV fluids for shock according to clinical condition.\n"
     "• Keep patient nil by mouth until evaluated. Contact gastroenterology, surgery, and toxicology as appropriate.\n\n"
     "[color=#1E3A8A]3. Exposure History[/color]\n"
     "• Identify product, concentration, amount, time of ingestion. Determine whether acid, alkali, or other corrosive. Assess accidental vs intentional. Bring product container or photograph of label when safe."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, blood gas in significant cases. Lactate when shock or tissue injury suspected.\n"
     "• Chest and abdominal imaging when perforation or aspiration suspected.\n"
     "• CT of neck, chest, and/or abdomen when significant transmural injury or perforation suspected.\n"
     "• Upper GI endoscopy in appropriate patients, generally within 12–24 hours when indicated and after stabilization.\n"
     "• [color=#991B1B]Do NOT perform endoscopy in suspected perforation or when procedure otherwise contraindicated. Timing and need for endoscopy or CT should be decided with specialist team.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Airway and Supportive Care[/color]\n"
     "• No universal medication dose applies to all corrosive ingestions. Treat hypoxemia, shock, and airway compromise per standard emergency protocols.\n"
     "• Prepare suction, oxygen, airway equipment, and IV access. Arrange advanced airway support early when edema or stridor developing.\n"
     "• Monitor airway patency, respiratory effort, oxygenation, hemodynamics, signs of perforation. Keep patient nil by mouth. Provide analgesia and antiemetics when appropriate.\n"
     "• [color=#991B1B]Do NOT induce vomiting. Do NOT attempt chemical neutralization. Do NOT give activated charcoal. Do NOT perform routine gastric lavage.[/color]\n\n"
     "[color=#1E3A8A]B. Oral Dilution[/color]\n"
     "• Do NOT routinely give large volumes of water or milk. Small amounts may be considered only immediately after certain exposures if patient fully alert, able to swallow normally, and poison center or product-specific protocol recommends it.\n"
     "• [color=#991B1B]Never give anything by mouth to patient with drooling, dysphagia, vomiting, reduced consciousness, airway compromise, or suspected perforation. Do NOT delay emergency evaluation to attempt dilution.[/color]\n\n"
     "[color=#1E3A8A]C. Endoscopy and Surgical Assessment[/color]\n"
     "• Indications: Symptoms suggesting significant esophageal or gastric injury. Intentional ingestion. Known ingestion of highly concentrated corrosive. Concerning clinical findings despite relatively normal oral examination.\n"
     "• Perform endoscopy only after stabilization and specialist assessment, usually within first 12–24 hours when appropriate. Use CT and surgical assessment when transmural necrosis or perforation suspected.\n"
     "• [color=#991B1B]Avoid blind nasogastric tube placement in significant corrosive injury unless directed by specialist team. Routine corticosteroids and prophylactic antibiotics are NOT recommended for every corrosive ingestion; use only for specific indications decided by treating team.[/color]"),
    ("05 — COMPLICATIONS", "danger", 
     "• Airway edema and respiratory failure. Esophageal or gastric perforation.\n"
     "• Mediastinitis or peritonitis. Hemorrhage and shock.\n"
     "• Esophageal stricture developing weeks or months later."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with symptoms, significant exposure, abnormal imaging, or suspected GI injury.\n"
     "• ICU care indicated for airway compromise, shock, perforation, severe acidosis, or major organ injury.\n"
     "• Discharge only after appropriate specialist evaluation and determination that significant injury is unlikely.\n"
     "• Arrange follow-up for dysphagia, weight loss, vomiting, or other symptoms suggesting delayed stricture."),
    ("REFERENCES", "info", "WSES Guidelines on Esophageal Emergencies; Goldfrank's; Royal Children's Hospital Melbourne Corrosives Guideline.")
]


# ==================== NEW TOXICOLOGY TOPICS (21-30) ====================

TOXICOLOGY_TOPICS[("Toxicology", "Iron Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Iron poisoning typically follows ingestion of iron-containing tablets (ferrous sulfate, fumarate, gluconate). Toxicity depends on the amount of elemental iron ingested, not total tablet weight.\n\n"
     "[color=#1E3A8A]Stage 1 — GI phase:[/color] Vomiting, abdominal pain, diarrhea. Hematemesis or GI bleeding. Dehydration/volume depletion.\n"
     "[color=#1E3A8A]Stage 2 — Apparent improvement:[/color] Symptoms may temporarily improve despite ongoing systemic toxicity.\n"
     "[color=#1E3A8A]Stage 3 — Systemic toxicity:[/color] Severe metabolic acidosis. Hypotension/shock. Altered mental status, seizures, coma. Hepatic injury, coagulopathy, multiorgan failure.\n"
     "[color=#1E3A8A]Stage 4 — Hepatic injury:[/color] Elevated aminotransferases, hypoglycemia, coagulopathy, possible hepatic failure.\n"
     "[color=#1E3A8A]Late complication:[/color] GI scarring/obstruction may develop after severe injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status.\n"
     "• Establish IV access and continuous monitoring. Check bedside glucose.\n"
     "• Obtain blood gas, electrolytes, renal function, liver function, coagulation, CBC.\n"
     "• Obtain serum iron concentration at appropriate time and repeat when indicated.\n"
     "• Identify formulation, number of tablets, time of ingestion, estimated elemental iron dose.\n"
     "• Contact toxicology early for significant/uncertain exposures."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serum iron concentration, commonly measured around 4–6 hours after ingestion for immediate-release preparations. Earlier and serial measurements may be required for modified-release preparations or uncertain timing.\n"
     "• Blood gas, bicarbonate, anion gap, lactate.\n"
     "• Glucose, electrolytes, renal function, liver enzymes, coagulation profile.\n"
     "• Abdominal radiograph may show radiopaque tablets but normal image does NOT exclude ingestion.\n"
     "• [color=#991B1B]IMPORTANT: A single serum iron measurement can be misleading if obtained too early or after peak concentration. Interpret with formulation, timing, symptoms, and serial results.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Gastrointestinal Decontamination[/color]\n"
     "• Indication: Whole-bowel irrigation may be considered for significant tablet ingestion, especially when numerous radiopaque tablets are visible or sustained-release tablets were ingested.\n"
     "• [color=#991B1B]Activated charcoal does NOT effectively bind iron. Do NOT perform routine induced emesis or gastric lavage. Avoid whole-bowel irrigation in bowel obstruction, ileus, perforation, hemodynamic instability, or unprotected airway.[/color]\n\n"
     "[color=#1E3A8A]B. Deferoxamine[/color]\n"
     "• Indication: Consider IV deferoxamine for severe iron poisoning, particularly with shock, severe metabolic acidosis, altered mental status, significant hepatic injury, or markedly elevated serum iron in appropriate context.\n"
     "• Commonly used IV infusion rate: 15 mg/kg/hour initially, with dose and duration determined by severity and specialist guidance. Do NOT exceed maximum rate/total dose per product label and local protocol.\n"
     "• [color=#991B1B]Rapid infusion may cause hypotension. Prolonged/high-dose treatment can cause serious adverse effects, including pulmonary toxicity. Severe cases require ICU care and toxicology consultation.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit symptomatic patients and patients with significant or uncertain ingestion.\n"
     "• ICU care indicated for shock, severe acidosis, altered consciousness, or hepatic failure.\n"
     "• Arrange follow-up for complications after significant GI injury."),
    ("REFERENCES", "info", "Goldfrank's; Deferoxamine product prescribing information; Royal Children's Hospital Melbourne Iron Poisoning Guideline.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Lithium Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Lithium toxicity may be acute, acute-on-chronic, or chronic. Chronic toxicity can cause severe neurologic manifestations even when measured serum concentration is not extremely high.\n\n"
     "[color=#1E3A8A]Risk Factors:[/color] Dehydration/sodium depletion. Acute kidney injury or CKD. Interactions with NSAIDs, ACEi, ARBs, thiazides. Recent dose changes/overdose. Reduced oral intake, vomiting, diarrhea.\n\n"
     "[color=#1E3A8A]Clinical Features:[/color] GI: nausea, vomiting, diarrhea. Neurologic: coarse tremor, ataxia, dysarthria, confusion, agitation, lethargy, hyperreflexia, myoclonus, seizures, coma. Other: renal impairment, ECG changes/dysrhythmias, nephrogenic diabetes insipidus."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, bedside glucose.\n"
     "• Establish IV access and cardiac monitoring.\n"
     "• Obtain serum lithium concentration, electrolytes, renal function, glucose.\n"
     "• Obtain ECG. Review timing of last dose, formulation, chronic dose, interacting medicines.\n"
     "• Contact toxicology and nephrology early for significant toxicity."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serum lithium concentration. Serial lithium concentrations until clear downward trend and appropriate clinical improvement established.\n"
     "• Creatinine, urea, sodium, potassium, bicarbonate, other electrolytes. ECG.\n"
     "• Additional testing based on altered consciousness, seizures, suspected co-ingestion.\n"
     "• [color=#991B1B]IMPORTANT: Interpret lithium concentrations in relation to timing of ingestion, formulation, renal function, clinical status. A single level does NOT reliably establish severity in every case.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV Isotonic Fluids[/color]\n"
     "• Indication: Volume depletion/dehydration when no contraindication.\n"
     "• Give 0.9% sodium chloride according to degree of volume depletion, BP, urine output, cardiac/renal function.\n"
     "• [color=#991B1B]Do NOT use forced diuresis or large fluid volumes solely to accelerate lithium elimination. Patients with heart failure or renal impairment require individualized fluid management.[/color]\n\n"
     "[color=#1E3A8A]B. Gastrointestinal Decontamination[/color]\n"
     "• Whole-bowel irrigation may be considered after significant ingestion of sustained-release lithium tablets, following toxicology advice.\n"
     "• [color=#991B1B]Activated charcoal does NOT meaningfully bind lithium. Do NOT perform GI decontamination in unprotected airway or patients with ileus, obstruction, hemodynamic instability.[/color]\n\n"
     "[color=#1E3A8A]C. Hemodialysis[/color]\n"
     "• Indication (per EXTRIP): Impaired kidney function with markedly elevated lithium concentrations. Decreased consciousness, seizures, life-threatening dysrhythmias regardless of concentration. Severe clinical toxicity or concentrations remaining high despite appropriate treatment. Predicted time to safe lithium clearance prolonged.\n"
     "• Intermittent hemodialysis generally preferred when feasible. Continue serial lithium measurements during and after dialysis. Monitor for rebound due to redistribution. Repeat dialysis when indicated by rebound levels or persistent toxicity.\n"
     "• [color=#991B1B]Do NOT make dialysis decisions based on lithium concentration alone. Chronic toxicity can produce severe neurologic injury at lower concentrations than acute ingestion. Consult nephrology and toxicology promptly.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with significant symptoms, renal impairment, rising levels, or suspected chronic toxicity.\n"
     "• ICU care indicated for seizures, coma, severe dysrhythmias, or hemodynamic instability.\n"
     "• Monitor for persistent neurologic sequelae after severe poisoning."),
    ("REFERENCES", "info", "EXTRIP Workgroup Lithium Recommendations; Goldfrank's; Lithium product prescribing information.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Valproate Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Valproate overdose can cause CNS depression, metabolic abnormalities, hyperammonemia, and in severe cases, cerebral edema and cardiovascular instability.\n"
     "• Nausea/vomiting. Drowsiness, confusion, ataxia. Respiratory depression/coma. Hypotension in severe poisoning.\n"
     "• Hyperammonemia with or without marked liver enzyme elevation. Metabolic acidosis and electrolyte abnormalities. Cerebral edema in severe cases.\n"
     "• Delayed toxicity can occur after ingestion of enteric-coated or extended-release preparations."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status. Check bedside glucose.\n"
     "• Establish IV access and continuous monitoring.\n"
     "• Obtain serum valproate concentration, electrolytes, renal function, liver function, blood gas, ammonia.\n"
     "• Consider acetaminophen level and other tests if intentional/mixed overdose suspected.\n"
     "• Contact toxicology early in severe poisoning."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial serum valproate concentrations. Ammonia concentration.\n"
     "• Blood gas, electrolytes, glucose, renal function. Liver enzymes and coagulation studies in significant poisoning. ECG.\n"
     "• Neuroimaging when cerebral edema or another intracranial complication suspected.\n"
     "• [color=#991B1B]IMPORTANT: Clinical deterioration can occur despite initially reassuring valproate concentration, particularly with delayed-release products. Repeat levels when indicated.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Airway and Supportive Care[/color]\n"
     "• Provide airway protection and ventilatory support when necessary. Treat hypotension with IV fluids and vasopressors if indicated. Correct glucose/electrolyte abnormalities. Monitor neurologic status and respiratory function.\n\n"
     "[color=#1E3A8A]B. L-Carnitine[/color]\n"
     "• Indication: Consider IV L-carnitine in severe valproate poisoning, especially with significant altered consciousness, hyperammonemia, hepatotoxicity, or metabolic complications. Seek toxicology guidance.\n"
     "• Commonly used regimen: Loading dose 100 mg/kg IV (max 6 g). Maintenance: 50 mg/kg IV every 8 hours (max 3 g per dose). Optimal regimen/duration vary; follow institutional protocol and toxicology advice.\n"
     "• [color=#991B1B]L-carnitine is an adjunct, not a substitute for airway support or indicated extracorporeal treatment. Do NOT delay stabilization while obtaining medication.[/color]\n\n"
     "[color=#1E3A8A]C. Hemodialysis[/color]\n"
     "• Indications: Very high serum valproate concentrations. Shock or cerebral edema. Coma or respiratory failure requiring mechanical ventilation. Severe metabolic acidosis. Acute hyperammonemia associated with severe clinical toxicity.\n"
     "• EXTRIP provides concentration-based and clinical criteria. Decisions should be made with toxicology and nephrology specialists.\n"
     "• [color=#991B1B]Severe hyperammonemia can occur even when liver enzymes are not markedly elevated. Consider cerebral edema in a deteriorating patient with severe poisoning.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit symptomatic patients and those with significant or rising concentrations.\n"
     "• ICU care indicated for coma, respiratory failure, shock, severe acidosis, or cerebral edema.\n"
     "• Continue monitoring for delayed toxicity with extended-release products."),
    ("REFERENCES", "info", "EXTRIP Workgroup Valproic Acid Recommendations; Goldfrank's; L-carnitine product information.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Isoniazid Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Isoniazid (INH), used in TB treatment, can cause severe and rapidly developing seizures by interfering with pyridoxine-dependent GABA synthesis. Refractory seizures and profound metabolic acidosis may occur.\n"
     "• Recurrent or refractory generalized seizures. Altered consciousness or coma.\n"
     "• Severe metabolic acidosis, often with elevated lactate. Vomiting and agitation. Respiratory depression and hemodynamic instability in severe poisoning.\n"
     "• [color=#991B1B]IMPORTANT: Standard anticonvulsants may be insufficient if pyridoxine deficiency caused by isoniazid remains untreated.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Protect airway and support ventilation. Check bedside glucose immediately.\n"
     "• Establish IV or intraosseous access. Treat seizures promptly.\n"
     "• Obtain blood gas, electrolytes, lactate, renal function, liver function.\n"
     "• Identify estimated amount and time of ingestion.\n"
     "• Obtain pyridoxine urgently and contact toxicology."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood gas, pH, bicarbonate, anion gap, lactate. Glucose and electrolytes.\n"
     "• Renal and liver function. ECG.\n"
     "• Evaluation for co-ingestants when appropriate.\n"
     "• [color=#991B1B]Do NOT delay pyridoxine while waiting for confirmatory toxicology testing.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Pyridoxine (Vitamin B6)[/color]\n"
     "• Indication: Suspected significant isoniazid overdose, particularly with seizures or severe metabolic acidosis.\n"
     "• Dose: If amount of isoniazid ingested known: give pyridoxine gram-for-gram relative to estimated amount of isoniazid ingested. If amount unknown in adult with severe suspected poisoning: commonly used initial dose is 5 g IV. In children: weight-based regimen, commonly 70 mg/kg IV, up to adult maximum of 5 g per initial administration. Additional doses may be required if seizures or severe toxicity persist.\n"
     "• [color=#991B1B]Do NOT delay pyridoxine in a patient with severe compatible poisoning. Dose may be large; independently verify calculation, especially in children. Do NOT assume that seizure cessation alone excludes ongoing toxicity.[/color]\n\n"
     "[color=#1E3A8A]B. Benzodiazepines[/color]\n"
     "• Indication: Immediate seizure control while pyridoxine is prepared and administered.\n"
     "• Use established IV benzodiazepine seizure protocol (e.g., lorazepam 0.1 mg/kg IV, max 4 mg per dose, with repeat dosing according to status epilepticus protocol).\n"
     "• [color=#991B1B]Benzodiazepines alone may NOT control seizures caused by isoniazid toxicity. Avoid delaying pyridoxine while repeatedly administering anticonvulsants.[/color]\n\n"
     "[color=#1E3A8A]C. Metabolic Acidosis and Supportive Care[/color]\n"
     "• Restore adequate ventilation and circulation. Treat underlying seizure activity and toxic exposure. Consider bicarbonate only for selected severe acidemia or specific indications, with toxicology guidance. Monitor potassium and other electrolytes during correction of severe acidosis."),
    ("05 — DISPOSITION", "warning", 
     "• ICU admission indicated for seizures, severe acidosis, coma, respiratory failure, or hemodynamic instability.\n"
     "• Continue neurologic and metabolic monitoring after seizure control.\n"
     "• Evaluate for aspiration, rhabdomyolysis, and complications of prolonged seizures."),
    ("REFERENCES", "info", "Goldfrank's; AHA Guidelines for Seizures and Emergency Cardiovascular Care; Poison center and institutional protocols for isoniazid overdose.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Methemoglobinemia and Oxidizing Agents")] = [
    ("01 — RECOGNIZE", "info", 
     "Methemoglobinemia occurs when hemoglobin iron is oxidized from ferrous (Fe²⁺) to ferric (Fe³⁺) state, reducing oxygen delivery to tissues.\n\n"
     "[color=#1E3A8A]Common Causes:[/color] Benzocaine and prilocaine. Dapsone. Nitrates and nitrites. Aniline dyes and other oxidizing chemicals. Certain medication overdoses.\n\n"
     "• Cyanosis that may not improve with oxygen alone. Headache, dizziness, fatigue, dyspnea.\n"
     "• Chocolate-brown or dark blood. Tachycardia and confusion. Seizures, dysrhythmias, coma, or shock in severe cases.\n"
     "• [color=#991B1B]IMPORTANT: Conventional pulse oximetry may remain near 85% and may not accurately reflect oxygenation. Confirm suspected methemoglobinemia with blood co-oximetry.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop exposure to suspected oxidizing agent.\n"
     "• Assess airway, breathing, circulation, mental status. Administer oxygen while evaluating patient.\n"
     "• Obtain IV access and continuous monitoring.\n"
     "• Send blood gas with co-oximetry and relevant lab tests.\n"
     "• Identify causative substance and assess for G6PD deficiency and serotonergic medication use.\n"
     "• Contact toxicology for significant or uncertain cases."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood co-oximetry for methemoglobin concentration. Blood gas and lactate.\n"
     "• CBC and renal function. ECG in symptomatic or severe cases. Hemolysis investigations when indicated.\n"
     "• Review of medications, chemical exposures, possible inherited causes.\n"
     "• [color=#991B1B]IMPORTANT: A calculated arterial oxygen saturation from a standard blood gas may be misleading. Use direct co-oximetry when available.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Methylene Blue[/color]\n"
     "• Indication: Symptomatic acquired methemoglobinemia or clinically significant methemoglobin elevation, interpreted in context of symptoms, comorbidities, and oxygen-delivery risk.\n"
     "• Initial dose: 1–2 mg/kg IV over approximately 5 minutes per product instructions. If significant symptoms persist or methemoglobin remains elevated, further dose may be considered after 30–60 minutes under specialist guidance. Do NOT continue repeated dosing without reassessment and toxicology advice.\n"
     "• [color=#991B1B]Methylene blue may be ineffective and can cause severe hemolysis in patients with G6PD deficiency. It can precipitate serotonin syndrome in patients taking serotonergic medicines (SSRIs, SNRIs, others). Use specialist guidance in pregnancy and significant renal impairment. Methylene blue can interfere with pulse oximetry and some laboratory measurements.[/color]\n\n"
     "[color=#1E3A8A]B. Alternative Management[/color]\n"
     "• When methylene blue is contraindicated, ineffective, or inappropriate: stop causative agent, supportive oxygen therapy, consult toxicology/hematology urgently. Consider ascorbic acid in selected cases (effect slow, not adequate substitute for urgent definitive therapy in severe cases). Exchange transfusion or hyperbaric oxygen may be considered for severe refractory poisoning in selected patients with specialist input.\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• Maintain airway and circulation. Treat seizures and dysrhythmias per emergency protocols. Evaluate for hemolysis and renal injury. Provide advanced support in severe tissue hypoxia."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with significant symptoms, high methemoglobin levels, ongoing exposure, hemolysis, or need for antidotal treatment and observation.\n"
     "• ICU care indicated for seizures, coma, shock, severe hypoxia, or refractory methemoglobinemia.\n"
     "• Monitor for rebound toxicity after agents with prolonged absorption or activity."),
    ("REFERENCES", "info", "Methylene blue injection prescribing information; Goldfrank's; Clinical toxicology guidance on acquired methemoglobinemia.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Hydrocarbon Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "Hydrocarbons include kerosene, gasoline, lamp oil, lighter fluid, industrial solvents. Major immediate danger after ingestion is aspiration into lungs, causing chemical pneumonitis.\n"
     "• Respiratory: Coughing/choking during or after ingestion. Tachypnea, wheezing, hypoxemia. Increased work of breathing. Chemical pneumonitis and, in severe cases, respiratory failure.\n"
     "• Neurologic: Dizziness, drowsiness, confusion, seizures after significant exposure.\n"
     "• Other: Nausea/vomiting. Cardiac dysrhythmias after exposure to certain hydrocarbons (particularly some halogenated solvents)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status.\n"
     "• Remove patient from exposure and ensure adequate ventilation.\n"
     "• Give oxygen if hypoxemia or respiratory distress present. Establish IV access if clinically indicated.\n"
     "• Identify substance, route, amount, time of exposure. Assess for aspiration, altered consciousness, co-ingestants.\n"
     "• Contact toxicology for significant exposure or uncertain product."),
    ("03 — INVESTIGATIONS", "info", 
     "• Continuous SpO2 monitoring in symptomatic patients.\n"
     "• Chest radiograph for respiratory symptoms or suspected aspiration. Blood gas when respiratory failure or significant hypoxemia suspected.\n"
     "• ECG and cardiac monitoring for significant solvent exposure.\n"
     "• [color=#991B1B]IMPORTANT: Respiratory symptoms and radiographic abnormalities may develop after initially reassuring examination. A normal early chest radiograph does NOT exclude subsequent pneumonitis.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Supportive Respiratory Care[/color]\n"
     "• Oxygen therapy titrated to patient's oxygenation and clinical condition. No specific antidote exists for most hydrocarbon exposures.\n"
     "• Monitor respiratory rate, oxygenation, work of breathing, mental status. Provide bronchodilators for clinically significant bronchospasm. Consider noninvasive or invasive ventilatory support when indicated.\n"
     "• [color=#991B1B]Do NOT intubate solely because ingestion occurred; base airway intervention on clinical indications. Avoid unnecessary procedures that increase aspiration risk.[/color]\n\n"
     "[color=#1E3A8A]B. Gastrointestinal Decontamination[/color]\n"
     "• Do NOT induce vomiting. Do NOT perform routine gastric lavage.\n"
     "• Do NOT routinely administer activated charcoal (binds many hydrocarbons poorly, may increase aspiration risk).\n"
     "• Do NOT give oral liquids to patient with respiratory symptoms, reduced consciousness, or swallowing difficulty.\n"
     "• [color=#991B1B]GI decontamination generally avoided because aspiration can be more dangerous than GI absorption.[/color]\n\n"
     "[color=#1E3A8A]C. Antibiotics and Corticosteroids[/color]\n"
     "• Do NOT routinely administer prophylactic antibiotics for chemical pneumonitis. Do NOT routinely use corticosteroids for uncomplicated hydrocarbon aspiration. Treat documented bacterial infection or another specific indication."),
    ("05 — DISPOSITION", "warning", 
     "• Observe asymptomatic patients for appropriate period per product, route, local toxicology protocol.\n"
     "• Admit patients with persistent cough, hypoxemia, abnormal respiratory examination, radiographic injury, or neurologic symptoms.\n"
     "• ICU care indicated for respiratory failure, severe hypoxemia, seizures, or hemodynamic instability."),
    ("REFERENCES", "info", "Goldfrank's; Royal Children's Hospital Melbourne Hydrocarbon Poisoning Guideline; ATSDR Medical Management Guidelines.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Other Pesticide Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "This topic covers pesticide poisoning other than organophosphate and carbamate poisoning (addressed separately).\n\n"
     "[color=#1E3A8A]Important agents:[/color] Pyrethroids/pyrethrins. Paraquat and other toxic herbicides. Glyphosate-containing herbicide formulations. Rodenticides, including anticoagulant products. Other agricultural chemicals with product-specific toxicity.\n"
     "• [color=#991B1B]IMPORTANT: Management depends on exact active ingredient and formulation. The word 'pesticide' alone is insufficient to select an antidote.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Protect healthcare staff from secondary contamination. Use appropriate PPE.\n"
     "• Remove contaminated clothing and bag safely. Wash exposed skin thoroughly with soap and water. Irrigate exposed eyes with clean water or saline.\n"
     "• Assess ABCs, mental status, glucose, vital signs.\n"
     "• Identify product from label or container.\n"
     "• Contact toxicology early in significant or uncertain exposures."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, liver function. Blood gas and lactate in significant poisoning.\n"
     "• ECG for systemic toxicity or suspected cardiotoxicity.\n"
     "• Coagulation profile for suspected anticoagulant rodenticide ingestion.\n"
     "• Serial renal function and respiratory assessment in paraquat poisoning.\n"
     "• Additional agent-specific testing as indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Pyrethroid Poisoning[/color]\n"
     "• Commonly cause skin irritation, paresthesia, nausea, vomiting, tremor, seizures in severe cases.\n"
     "• No specific antidote routinely available. Treat seizures with standard benzodiazepine protocols.\n"
     "• [color=#991B1B]Some products contain additional solvents/active ingredients that may produce more severe toxicity than pyrethroid itself. Do NOT assume all pesticide-associated cholinergic symptoms are caused by organophosphates; confirm likely agent and clinical syndrome.[/color]\n\n"
     "[color=#1E3A8A]B. Paraquat Poisoning[/color]\n"
     "• Can cause severe GI injury, acute kidney/liver injury, delayed pulmonary fibrosis.\n"
     "• Immediate actions: prevent further exposure, decontaminate skin/eyes, urgent hospital evaluation, contact toxicology immediately, assess renal/liver/acid-base/respiratory status.\n"
     "• GI decontamination: Activated charcoal or Fuller's earth may be considered after ingestion under product-specific toxicology protocol, provided airway protected and no contraindications.\n"
     "• [color=#991B1B]There is NO established specific antidote that reliably reverses paraquat poisoning. Do NOT administer high-concentration oxygen routinely to patient who is not hypoxemic. However, never withhold oxygen from a hypoxemic patient; titrate respiratory support to clinical need. Avoid delaying decontamination or specialist consultation.[/color]\n\n"
     "[color=#1E3A8A]C. Anticoagulant Rodenticide Poisoning[/color]\n"
     "• Some rodenticides interfere with vitamin K-dependent coagulation factors. Others have different toxic mechanisms.\n"
     "• Investigations: PT/INR and baseline coagulation profile. Repeat coagulation tests per product, exposure time, toxicology advice. Assess for bleeding, anemia, hemodynamic instability.\n"
     "• Treatment: Vitamin K1 (Phytonadione). Indication: confirmed or strongly suspected clinically significant anticoagulant rodenticide poisoning with coagulopathy, or another specific indication identified by toxicology. Dose/route depend on product, degree of coagulopathy, bleeding severity, whether long-acting anticoagulant involved. Use product-specific toxicology protocol. IV vitamin K1 must be administered with particular caution because severe infusion reactions can occur.\n"
     "• [color=#991B1B]Do NOT administer vitamin K routinely for every rodenticide exposure. Do NOT assume all rodenticides are anticoagulants; identify active ingredient.[/color]\n\n"
     "[color=#1E3A8A]D. Glyphosate-Containing Formulations[/color]\n"
     "• Severe poisoning can produce GI irritation, hypotension, metabolic abnormalities, renal injury, respiratory complications.\n"
     "• Provide supportive care and hemodynamic monitoring. Assess for shock, electrolyte disturbances, renal injury. Treat complications per standard critical care protocols.\n"
     "• [color=#991B1B]The formulation and surfactants may contribute substantially to toxicity. There is NO universally effective specific antidote.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with systemic symptoms, abnormal coagulation, respiratory symptoms, significant paraquat exposure, or organ injury.\n"
     "• ICU care appropriate for shock, seizures, respiratory failure, severe acidosis, or evolving multiorgan dysfunction.\n"
     "• Arrange follow-up laboratory testing when delayed toxicity possible."),
    ("REFERENCES", "info", "CDC Paraquat Chemical Emergencies; Goldfrank's; WHO Clinical Management of Pesticide Poisoning; Product-specific toxicology guidance.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Snakebite and Envenomation")] = [
    ("01 — RECOGNIZE", "info", 
     "Snake envenomation may cause neurotoxicity, coagulopathy, hemorrhage, rhabdomyolysis, acute kidney injury, shock, and local tissue destruction. Clinical effects vary by snake species and geographic region. Do NOT rely solely on visual identification of the snake.\n\n"
     "[color=#1E3A8A]Local:[/color] Pain, swelling, bruising, blistering. Progressive swelling extending along limb. Local tissue necrosis in some species.\n"
     "[color=#1E3A8A]Systemic:[/color] Ptosis, ophthalmoplegia, bulbar weakness, respiratory paralysis. Spontaneous bleeding or abnormal coagulation. Hypotension or shock. Dark urine from hemoglobinuria/myoglobinuria. Oliguria or acute kidney injury. Nausea, vomiting, collapse.\n"
     "• [color=#991B1B]IMPORTANT: Some neurotoxic bites may produce severe paralysis with little local swelling.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure scene safety and move away from snake.\n"
     "• Reassure patient and minimize movement. Immobilize affected limb with a splint.\n"
     "• Remove rings, watches, tight clothing before swelling progresses.\n"
     "• Arrange urgent transport to facility capable of monitoring and administering appropriate antivenom.\n"
     "• Assess ABCs, especially bulbar function and respiratory effort. Establish IV access and monitor vital signs.\n"
     "• Mark leading edge of swelling and record time.\n\n"
     "[color=#1E3A8A]Do NOT:[/color]\n"
     "• Apply a tight arterial tourniquet.\n"
     "• Cut, suck, burn, or electrically treat the bite.\n"
     "• Apply ice or unproven herbal preparations.\n"
     "• Attempt to catch or kill the snake.\n"
     "• Delay transfer to identify the species.\n"
     "• Pressure-immobilization techniques are appropriate only for selected snake species and regional protocols; do not apply indiscriminately."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC and platelet count. PT/INR, aPTT, fibrinogen when available.\n"
     "• Creatinine, urea, electrolytes, urine output. Urinalysis for blood or myoglobin.\n"
     "• Blood group and crossmatch in significant bleeding or severe envenomation.\n"
     "• ECG and blood gas when clinically indicated.\n"
     "• Serial assessment of swelling, neurologic function, coagulation.\n"
     "• Where locally validated, standardized 20-minute whole-blood clotting test may help identify venom-induced coagulopathy when lab coagulation testing unavailable."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Snake Antivenom[/color]\n"
     "• Indication: Give appropriate region- and species-specific antivenom when there is evidence of clinically significant envenomation, including neurotoxicity/progressive paralysis, coagulopathy or spontaneous systemic bleeding, shock/cardiovascular instability, acute kidney injury or significant hemoglobinuria/myoglobinuria, rapidly progressive local swelling meeting regional criteria, other established indications in relevant regional protocol. A bite without evidence of envenomation does NOT automatically require antivenom.\n"
     "• Dose: Use product-specific dose recommended for implicated species or regional envenomation syndrome. Dose is NOT reliably determined by patient weight alone; children generally require same venom-neutralizing dose as adults for same degree of envenomation. Do NOT use a universal vial count across different antivenoms.\n"
     "• [color=#991B1B]Antivenom can cause severe acute hypersensitivity reactions. Should be administered in setting equipped to recognize and treat anaphylaxis. Do NOT delay appropriate antivenom in patient with life-threatening envenomation while waiting for snake identification. Unnecessary antivenom exposes patients to risk without assured benefit.[/color]\n\n"
     "[color=#1E3A8A]B. Anaphylaxis During Antivenom Administration[/color]\n"
     "• Epinephrine (adrenaline) IM: 0.01 mg/kg of 1 mg/mL solution, max 0.5 mg per dose in adults. Repeat every 5–15 minutes if required per anaphylaxis protocol.\n"
     "• [color=#991B1B]IV epinephrine bolus is NOT routine treatment for anaphylaxis and carries significant risk. Use IV infusion only in appropriate monitored settings with experienced clinicians when indicated.[/color]\n\n"
     "[color=#1E3A8A]C. Respiratory Paralysis and Shock[/color]\n"
     "• Secure airway and provide assisted ventilation when indicated. Treat shock with carefully reassessed IV fluids and vasopressors when necessary. Monitor urine output and renal function. Treat clinically significant bleeding and coagulopathy with specialist guidance; antivenom is primary venom-specific treatment when indicated."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with suspected envenomation for serial clinical and laboratory assessment.\n"
     "• ICU care indicated for respiratory weakness, bulbar dysfunction, shock, significant bleeding, severe coagulopathy, or acute kidney injury.\n"
     "• Arrange follow-up for delayed bleeding, renal complications, tissue injury, and serum sickness after antivenom when relevant."),
    ("REFERENCES", "info", "WHO Snakebite Envenoming: Treatment and Prevention; WHO regional guidelines; Goldfrank's; Current regional antivenom product information.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Scorpion Sting and Dangerous Bites")] = [
    ("01 — RECOGNIZE", "info", 
     "Scorpion venom may cause severe autonomic stimulation, neuromuscular symptoms, cardiopulmonary complications. Severity depends on species, amount of venom, patient age, time to treatment.\n\n"
     "[color=#1E3A8A]Local:[/color] Severe pain or burning. Paresthesia, tingling, local swelling.\n"
     "[color=#1E3A8A]Systemic:[/color] Sweating, agitation, vomiting, excessive salivation. Tachycardia or hypertension. Muscle twitching or abnormal eye movements. Respiratory distress or excessive airway secretions. Pulmonary edema, myocardial dysfunction, or shock in severe envenomation.\n"
     "• Children may deteriorate more rapidly than adults."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure patient in safe environment. Assess ABCs and vital signs.\n"
     "• Establish IV access for systemic symptoms. Monitor ECG and SpO2 when systemic toxicity suspected.\n"
     "• Provide local wound care.\n"
     "• Contact toxicology or regional envenomation service for severe symptoms and species-specific treatment advice."),
    ("03 — INVESTIGATIONS", "info", 
     "• ECG and continuous cardiac monitoring in systemic toxicity.\n"
     "• Blood gas and lactate in respiratory distress or shock. Electrolytes, renal function, glucose.\n"
     "• Troponin and echocardiography when myocardial injury or dysfunction suspected. Chest imaging for suspected pulmonary edema."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Local Pain Control[/color]\n"
     "• Use appropriate analgesia according to age, weight, contraindications, local protocols. Clean sting site. Apply cool compress if appropriate; avoid ice-related tissue injury. Reassess pain and monitor for evolving systemic symptoms.\n"
     "• [color=#991B1B]Do NOT cut, suck, burn, or apply tight tourniquet to sting site. Avoid local anesthetic techniques unless performed by clinician familiar with relevant anatomy and indications.[/color]\n\n"
     "[color=#1E3A8A]B. Antivenom[/color]\n"
     "• Indication: Use antivenom only when effective against local scorpion species and patient meets regional treatment criteria. Severe systemic manifestations, particularly in children, require urgent specialist assessment.\n"
     "• Dose: Follow exact product-specific regional protocol. Do NOT assume antivenom products for different scorpion species are interchangeable.\n"
     "• [color=#991B1B]Antivenom efficacy and indications differ by region and product. Do NOT delay airway support or treatment of shock while obtaining antivenom.[/color]\n\n"
     "[color=#1E3A8A]C. Severe Autonomic or Cardiovascular Toxicity[/color]\n"
     "• Provide oxygen and ventilatory support as needed. Treat shock with careful fluid assessment and specialist-directed vasoactive therapy. Manage pulmonary edema and myocardial dysfunction in ICU. In selected regional syndromes, prazosin or other specific treatment may be recommended by local protocols.\n"
     "• [color=#991B1B]Do NOT give prazosin routinely to every scorpion-sting patient. Its use depends on local species, clinical syndrome, hemodynamic state, regional evidence. Avoid excessive fluid administration when myocardial dysfunction or pulmonary edema present.[/color]"),
    ("05 — DISPOSITION", "warning", 
     "• Observe patients according to local species-specific guidance.\n"
     "• Admit patients with systemic symptoms, abnormal vital signs, significant pain requiring repeated parenteral treatment, or relevant pediatric risk.\n"
     "• ICU care indicated for respiratory failure, pulmonary edema, shock, or myocardial dysfunction."),
    ("06 — OTHER DANGEROUS BITES", "info", 
     "For bites from mammals, bats, or other animals, assess separately for:\n"
     "• Wound infection and tissue injury.\n"
     "• Rabies exposure and need for post-exposure prophylaxis.\n"
     "• Tetanus immunization status.\n"
     "• Indications for antibiotics, surgical exploration, or specialist review.\n"
     "• Do NOT assume all animal bites require antibiotics, and do NOT delay rabies assessment when a potentially rabid animal was involved."),
    ("REFERENCES", "info", "WHO Guidelines for Management of Snakebites and Other Envenoming; Goldfrank's; Regional scorpion antivenom guidance.")
]

TOXICOLOGY_TOPICS[("Toxicology", "Toxicologic Cardiac Arrest and Refractory Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Toxicologic cardiac arrest occurs when a drug or chemical causes severe hypoxia, myocardial depression, dysrhythmia, or circulatory collapse.\n\n"
     "[color=#1E3A8A]Potential causes:[/color] Sodium-channel blocker toxicity (e.g., TCAs). Beta-blocker or calcium-channel blocker overdose. Digoxin toxicity. Opioid-induced respiratory arrest. Cyanide or severe toxic alcohol poisoning. Local anesthetic systemic toxicity. Severe hyperkalemia or other toxic-metabolic disturbances.\n"
     "• [color=#991B1B]IMPORTANT: Standard resuscitation remains essential, but selected poisonings require specific antidotes and modified treatment strategies.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Confirm cardiac arrest and activate resuscitation team. Start high-quality CPR immediately.\n"
     "• Apply defibrillator pads and identify rhythm. Provide oxygenation and ventilation while avoiding excessive ventilation.\n"
     "• Establish IV or intraosseous access. Check bedside glucose and consider reversible metabolic causes.\n"
     "• Obtain focused exposure history from witnesses, medication containers, or records.\n"
     "• Identify and administer relevant antidote when indicated.\n"
     "• Contact toxicology and critical care early. Consider extracorporeal CPR or other advanced rescue options in selected refractory cases where available."),
    ("03 — INVESTIGATIONS", "info", 
     "During resuscitation, obtain tests when they do not interrupt CPR:\n"
     "• Blood gas, pH, lactate, electrolytes. Potassium, glucose, renal function.\n"
     "• ECG and rhythm analysis. Specific drug concentrations when available and clinically useful.\n"
     "• Echocardiography during appropriate pauses or after ROSC. Evaluation for co-ingestion and additional reversible causes."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Standard Resuscitation[/color]\n"
     "• Follow current adult/pediatric advanced life support algorithm. For adult cardiac arrest, epinephrine commonly 1 mg IV/IO every 3–5 minutes per applicable algorithm. Defibrillation energy and medication selection depend on rhythm and current protocol.\n"
     "• [color=#991B1B]Standard resuscitation is necessary but may be insufficient without toxin-specific treatment. Avoid unstructured administration of multiple antidotes without plausible toxicologic indication.[/color]\n\n"
     "[color=#1E3A8A]B. Sodium Bicarbonate for Sodium-Channel Blocker Toxicity[/color]\n"
     "• Indication: Suspected sodium-channel blocker poisoning with QRS widening, ventricular dysrhythmia, or hemodynamic instability, particularly with TCAs or selected other agents.\n"
     "• Commonly used initial dose: 1–2 mEq/kg IV. Repeat according to ECG response, hemodynamics, blood gas, and institutional toxicology protocol.\n"
     "• [color=#991B1B]Bicarbonate is NOT a universal antidote for every toxicologic arrest. Use for appropriate indications and monitor response.[/color]\n\n"
     "[color=#1E3A8A]C. High-Dose Insulin Euglycemia Therapy[/color]\n"
     "• Indication: Consider for severe beta-blocker or calcium-channel blocker poisoning with myocardial dysfunction or refractory shock, under specialist-led critical care protocols.\n"
     "• Commonly used starting regimen: Regular insulin 1 unit/kg IV bolus, then 1 unit/kg/hour IV infusion, with escalation according to hemodynamic response and institutional protocol. Doses may require substantial escalation in severe poisoning, but must occur under dedicated high-dose insulin protocol.\n"
     "• [color=#991B1B]High-dose insulin therapy can cause severe and delayed hypoglycemia and hypokalemia. Requires trained staff, frequent laboratory testing, and standardized protocol. Do NOT initiate without clear indication and appropriate monitoring capability.[/color]\n\n"
     "[color=#1E3A8A]D. Lipid Emulsion Therapy[/color]\n"
     "• Indication: Consider 20% lipid emulsion for severe local anesthetic systemic toxicity and selected other highly lipophilic drug poisonings when recommended by relevant toxicology protocol.\n"
     "• For adult LAST: 20% lipid emulsion 1.5 mL/kg IV bolus, followed by 0.25 mL/kg/min infusion. If instability persists, repeat bolus and increase infusion per current local checklist. Use ASRA checklist or equivalent for exact dosing, duration, maximum cumulative dose.\n"
     "• [color=#991B1B]Lipid emulsion is NOT recommended routinely for every poisoning or cardiac arrest. Avoid indiscriminate administration because it may cause complications and interfere with lab testing or extracorporeal circuits.[/color]\n\n"
     "[color=#1E3A8A]E. Calcium for Calcium-Channel Blocker Toxicity[/color]\n"
     "• Indication: Use IV calcium for clinically significant CCB poisoning with hypotension, bradycardia, or myocardial dysfunction, per local protocol.\n"
     "• Calcium chloride 10% or calcium gluconate 10% may be used; volume differs because elemental calcium content differs. Select preparation and dose according to clinical situation and institutional toxicology protocol.\n"
     "• [color=#991B1B]Avoid extravasation and monitor for hypercalcemia. Calcium is an adjunct and must NOT delay high-dose insulin or vasopressors when indicated.[/color]\n\n"
     "[color=#1E3A8A]F. Toxin-Specific Antidotes[/color]\n"
     "• Choose antidote according to suspected cause: Opioid toxicity: naloxone + ventilation. Cyanide poisoning: hydroxocobalamin. Digoxin toxicity: digoxin immune Fab. LAST: lipid emulsion per ASRA checklist. Beta-blocker/CCB toxicity: high-dose insulin and other specialist-directed therapies. Toxic alcohol poisoning: fomepizole and hemodialysis when indicated. Isoniazid poisoning with seizures: pyridoxine.\n"
     "• [color=#991B1B]Antidotes are NOT interchangeable. Use relevant poisoning-specific protocol and involve toxicology early.[/color]\n\n"
     "[color=#1E3A8A]G. Refractory Shock and Extracorporeal Support[/color]\n"
     "• Indications for specialist consideration: Persistent shock despite appropriate antidotes, fluids, vasopressors, toxin-specific therapies. Refractory cardiogenic shock from selected beta-blocker or CCB poisonings. Selected cases of severe cardiotoxic drug poisoning where recovery possible and local resources permit.\n"
     "• [color=#991B1B]ECMO and extracorporeal CPR require specialized teams and patient selection. They are NOT substitutes for immediate CPR, defibrillation, or indicated antidotes.[/color]"),
    ("05 — POST-RESUSCITATION CARE", "info", 
     "• Secure airway and optimize ventilation/oxygenation. Treat shock and monitor cardiac function. Correct glucose/electrolyte abnormalities. Repeat blood gas, lactate, relevant toxin levels. Evaluate for hypoxic brain injury and other complications. Continue treatment for underlying poisoning and assess for recurrent toxicity."),
    ("06 — DISPOSITION", "warning", 
     "• ICU admission required after toxicologic cardiac arrest or severe refractory shock.\n"
     "• Continue monitoring for recurrent dysrhythmia, delayed hypoglycemia, rebound toxicity, organ injury.\n"
     "• Arrange specialist follow-up and document suspected agent, antidotes, response, complications."),
    ("REFERENCES", "info", "AHA 2025 Guidelines; ASRA LAST Checklist; EXTRIP Workgroup Recommendations; Goldfrank's.")
]