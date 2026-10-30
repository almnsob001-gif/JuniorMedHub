# ==============================================================================
# ملف أدوية الطوارئ والعناية المركزة (Emergency & ICU Drugs)
# الفهرس الشامل لجميع الأدوية + التفاصيل الكاملة
# ==============================================================================

DRUGS_DATA = {
    "Emergency & ICU Drugs": {
        "General": [
            "Epinephrine (Adrenaline)", "Norepinephrine (Noradrenaline)", "Vasopressin", "Dobutamine",
            "Dopamine", "Phenylephrine", "Ephedrine", "Amiodarone", "Lidocaine (Lignocaine)", "Atropine",
            "Adenosine", "Magnesium Sulfate", "Calcium Gluconate", "Calcium Chloride", "Labetalol",
            "Hydralazine", "Furosemide", "Aspirin", "Clopidogrel", "Unfractionated Heparin", 
            "Enoxaparin", "Alteplase (tPA)", "Tranexamic Acid", "Protamine Sulfate", "Vitamin K (Phytonadione)",
            "Salbutamol (Albuterol)", "Ipratropium Bromide", "Budesonide", "Aminophylline", "Terbutaline",
            "Hydrocortisone", "Methylprednisolone", "Dexamethasone", "Diphenhydramine", "Chlorpheniramine",
            "Lorazepam", "Etomidate", "Dexmedetomidine", "Rocuronium", "Succinylcholine (Suxamethonium)",
            "Naloxone", "Flumazenil", "Paracetamol (Acetaminophen)", "Tramadol", "Haloperidol", 
            "Ondansetron", "Metoclopramide", "Levetiracetam", "Phenytoin", "Fosphenytoin", 
            "Sodium Valproate", "Mannitol", "Hypertonic Sodium Chloride (3%)", "Nimodipine", "Thiamine (Vitamin B1)",
            "Meropenem", "Vancomycin", "Metronidazole", "Amikacin", "Gentamicin", "Azithromycin",
            "Doxycycline", "Clindamycin", "Ampicillin-Sulbactam", "Acyclovir", "Fluconazole",
            "Sodium Chloride 0.9% (Normal Saline)", "Lactated Ringer's Solution", "Dextrose 10% (D10W)",
            "Dextrose 50% (D50W)", "Regular Insulin", "Potassium Chloride (KCl)", "Sodium Bicarbonate",
            "Sodium Zirconium Cyclosilicate", "Glucagon", "Octreotide", "Desmopressin",
            "Pantoprazole", "Famotidine", "Lactulose", "Activated Charcoal",
            "N-Acetylcysteine", "Pralidoxime (2-PAM)", "Deferoxamine"
        ]
    }
}

DRUGS_TOPICS = {}

# -------------------- EPINEPHRINE (ADRENALINE) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Epinephrine (Adrenaline)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Cardiac Arrest, Anaphylaxis, Severe Asthma, Shock, Symptomatic Bradycardia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Cardiac Arrest:[/b] 1 mg IV/IO every 3-5 mins.\n• [b]Anaphylaxis:[/b] 0.5 mg IM (1:1000).\n• [b]Bradycardia/Shock:[/b] 0.05–0.5 mcg/kg/min IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Cardiac Arrest:[/b] 0.01 mg/kg IV/IO (max 1 mg).\n• [b]Anaphylaxis:[/b] 0.01 mg/kg IM (max 0.5 mg).\n• [b]Bradycardia/Shock:[/b] 0.05–0.3 mcg/kg/min IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Beta-blockers:[/b] May cause unopposed alpha-adrenergic effects (severe hypertension).\n• [b]MAOIs / TCAs:[/b] Enhances the pressor effect (risk of hypertensive crisis).\n• [b]Halogenated Anesthetics:[/b] Increases risk of ventricular arrhythmias."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, palpitations, arrhythmias (VT/VF).\n• Severe hypertension, myocardial ischemia.\n• Anxiety, tremor, headache.\n• Tissue necrosis at extravasation site.\n• Hyperglycemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]NEVER give IV bolus of 1:1000 (1 mg/mL) in anaphylaxis — fatal error.[/color]\n• High-alert medication; requires independent double-check.\n• Extravasation causes severe tissue injury (use Phentolamine).\n• Use central line for prolonged infusions."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Crosses the placenta.\n• [b]Effect on fetus:[/b] May decrease uterine blood flow and cause fetal tachycardia.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts. Use with caution."),
    ("REFERENCES", "info", "AHA 2025 Guidelines; BNF.")
]

# -------------------- NOREPINEPHRINE (NORADRENALINE) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Norepinephrine (Noradrenaline)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Septic Shock, Cardiogenic Shock, Neurogenic Shock.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 0.05–0.5 mcg/kg/min IV infusion, titrated to MAP ≥ 65 mmHg.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.05–0.3 mcg/kg/min IV infusion, titrated to age-appropriate BP."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]MAOIs / TCAs:[/b] Severe hypertension.\n• [b]Cocaine:[/b] Additive hypertensive effect.\n• [b]Beta-blockers:[/b] May cause reflex bradycardia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypertension, reflex bradycardia, arrhythmias.\n• Myocardial ischemia, peripheral ischemia.\n• Tissue necrosis at extravasation site."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Extravasation causes severe tissue necrosis (use Phentolamine).[/color]\n• Central venous access preferred.\n• Do not stop infusion abruptly (reduce gradually)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. May decrease uterine blood flow.\n• [b]Lactation:[/b] Unknown if excreted in breast milk. Use with caution."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign 2021; BNF.")
]

# -------------------- AMIODARONE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Amiodarone")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Cardiac Arrest (VF/pVT), Stable VT, Atrial Fibrillation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Cardiac Arrest:[/b] 300 mg IV/IO rapid push (1st), 150 mg (2nd).\n• [b]Stable VT:[/b] 150 mg IV over 10 mins, then 1 mg/min x 6h, 0.5 mg/min x 18h.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Cardiac Arrest:[/b] 5 mg/kg IV/IO bolus (max 300 mg).\n• [b]Stable VT:[/b] 5 mg/kg IV over 20-60 mins (max 300 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Warfarin:[/b] Increases INR (risk of bleeding).\n• [b]Digoxin:[/b] Increases digoxin levels.\n• [b]Beta-blockers / CCBs:[/b] Risk of bradycardia and AV block."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bradycardia, hypotension, AV block.\n• QT prolongation.\n• Thyroid dysfunction, pulmonary toxicity (long-term), hepatotoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]MUST dilute in 5% Dextrose (precipitates in saline).[/color]\n• High risk of hypotension if pushed too fast.\n• Avoid in 2nd/3rd-degree AV block without pacing."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Can cause fetal thyroid dysfunction and bradycardia.\n• [b]Lactation:[/b] Excreted in breast milk. Use with caution."),
    ("REFERENCES", "info", "AHA 2025; ESC 2019; BNF.")
]

# -------------------- ATROPINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Atropine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Symptomatic Bradycardia, Organophosphate Poisoning.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Bradycardia:[/b] 1 mg IV q3-5min (max 3 mg).\n• [b]Organophosphate:[/b] 2-5 mg IV, double every 5-10 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Bradycardia:[/b] 0.02 mg/kg IV (min 0.1 mg, max 0.5 mg).\n• [b]Organophosphate:[/b] 0.05 mg/kg IV."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other anticholinergics:[/b] Additive toxicity.\n• [b]MAOIs / TCAs:[/b] Additive anticholinergic effects."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, arrhythmias.\n• Dry mouth, blurred vision, urinary retention.\n• Confusion, delirium (elderly)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]AVOID in infranodal blocks (Mobitz II, 3rd-degree AV block).[/color]\n• Minimum pediatric dose 0.1 mg (paradoxical bradycardia if too low)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. May cause fetal tachycardia.\n• [b]Lactation:[/b] Excreted in breast milk (may decrease milk production)."),
    ("REFERENCES", "info", "AHA 2025 Bradycardia Algorithm; BNF.")
]

# -------------------- ADENOSINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Adenosine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Stable Narrow-Complex Regular Tachycardia (SVT).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 6 mg rapid IV push (1st). If ineffective, 12 mg rapid IV push (2nd).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1 mg/kg rapid IV push (max 6 mg). If ineffective, 0.2 mg/kg (max 12 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Dipyridamole:[/b] Enhances the effect (reduce dose).\n• [b]Carbamazepine:[/b] Enhances AV block.\n• [b]Caffeine / Theophylline:[/b] Antagonize the effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Flushing, chest pain, dyspnea.\n• Bronchospasm (dangerous in asthmatics).\n• Transient asystole, bradycardia.\n• Headache, dizziness."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Contraindicated in Asthma/COPD (can cause severe bronchospasm).[/color]\n• Contraindicated in irregular or wide-complex tachycardia.\n• Use a proximal IV and rapid saline flush (half-life < 10 seconds)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. May cause fetal bradycardia.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "AHA 2025 Tachycardia Algorithm; ESC 2019 SVT Guidelines.")
]

# -------------------- VASOPRESSIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Vasopressin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Septic Shock (second-line), Variceal Bleeding, Diabetes Insipidus.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Septic Shock:[/b] 0.03 units/min (fixed rate, no titration).\n• [b]Variceal Bleeding:[/b] 0.2–0.4 units/min IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Vasodilatory Shock:[/b] 0.0005–0.002 units/kg/min IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Corticosteroids:[/b] May increase fluid retention and risk of hyponatremia.\n• [b]Other Vasopressors:[/b] Additive effect (may need to reduce norepinephrine dose)."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Ischemia (digital, mesenteric, myocardial).\n• Hyponatremia (water intoxication).\n• Bradycardia, arrhythmias.\n• Abdominal cramps, nausea."),
    ("4. WARNING", "danger", 
     "• High-alert medication.\n• [color=#991B1B]Risk of severe ischemia, especially in patients with cardiovascular disease.[/color]\n• Do not use as a bolus push for shock (only IV infusion)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Oxytocic effect (may stimulate uterine contractions). Use with caution.\n• [b]Lactation:[/b] Excreted in breast milk, but minimal effect."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign 2021; BNF.")
]

# -------------------- DOBUTAMINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dobutamine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Cardiogenic Shock, Acute Heart Failure with low cardiac output.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 2.5–20 mcg/kg/min IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 2–20 mcg/kg/min IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Beta-blockers:[/b] Antagonize the inotropic effect of dobutamine.\n• [b]MAOIs:[/b] Enhances the pressor effect.\n• [b]Nitrates / Vasodilators:[/b] Additive hypotension."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, arrhythmias (VT, AFib).\n• Hypotension (due to vasodilation).\n• Headache, tremor, anxiety.\n• Myocardial ischemia (increased oxygen demand)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]May worsen hypotension in patients with low preload.[/color]\n• Do NOT give as a routine IV bolus.\n• Monitor ECG and BP continuously."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. May cause fetal tachycardia.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "ESC 2021 Heart Failure Guidelines; BNF.")
]

# -------------------- DOPAMINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dopamine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Symptomatic Bradycardia, Shock (less common now).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Bradycardia/Shock:[/b] 5–20 mcg/kg/min IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 5–20 mcg/kg/min IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]MAOIs:[/b] Severe hypertension.\n• [b]Phenytoin:[/b] May cause hypotension and bradycardia.\n• [b]Beta-blockers:[/b] Antagonize cardiac effects."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachyarrhythmias, hypertension.\n• Myocardial ischemia, angina.\n• Nausea, vomiting.\n• Tissue necrosis at extravasation site."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Higher arrhythmia risk than norepinephrine (not first-line).[/color]\n• Extravasation causes severe tissue necrosis (use Phentolamine).\n• Do not mix with sodium bicarbonate."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Decreases uterine blood flow.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "AHA 2025 Bradycardia Algorithm; BNF.")
]

# -------------------- PHENYLEPHRINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Phenylephrine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypotension (especially with tachycardia).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Bolus:[/b] 40–100 mcg IV.\n• [b]Infusion:[/b] 0.1–1 mcg/kg/min IV.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 5–20 mcg/kg IV bolus."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]MAOIs / TCAs:[/b] Severe hypertension.\n• [b]Beta-blockers:[/b] May cause severe hypertension and reflex bradycardia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Reflex bradycardia.\n• Hypertension, myocardial ischemia.\n• Headache, anxiety, tremor.\n• Tissue necrosis at extravasation site."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Use with caution in patients with heart failure or bradycardia.[/color]\n• Extravasation causes severe tissue necrosis."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. May reduce uterine blood flow.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Local Anesthesia Guidelines.")
]

# -------------------- LIDOCAINE (LIGNOCAINE) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Lidocaine (Lignocaine)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Ventricular Arrhythmias (VT/VF), Local Anesthesia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Cardiac Arrest:[/b] 1–1.5 mg/kg IV/IO (1st), 0.5–0.75 mg/kg (2nd).\n• [b]Stable VT:[/b] 1–1.5 mg/kg IV bolus, then 1–4 mg/min infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1 mg/kg IV/IO bolus (for VT/VF)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Cimetidine / Beta-blockers:[/b] Increase lidocaine levels (risk of toxicity).\n• [b]Phenytoin:[/b] May alter lidocaine levels."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• CNS toxicity: Dizziness, confusion, seizures, coma.\n• Bradycardia, hypotension, arrhythmias.\n• Nausea, metallic taste."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Reduce dose in hepatic impairment.[/color]\n• Do not use with epinephrine in digits.\n• Monitor for signs of CNS toxicity."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. May cause fetal bradycardia if high doses used.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "AHA 2025 ACLS Guidelines; BNF.")
]

# -------------------- EPHEDRINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Ephedrine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypotension (especially during spinal anesthesia).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 5–10 mg IV (max 50 mg).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.2–0.3 mg/kg IV."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]MAOIs:[/b] Severe hypertensive crisis (contraindicated).\n• [b]Oxytocin:[/b] Severe hypertension if used together."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, hypertension, arrhythmias.\n• Anxiety, tremor, insomnia.\n• Urinary retention."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Tachyphylaxis (rapid tolerance) develops quickly.[/color]\n• Avoid in tachyarrhythmias or severe CAD."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. May cause fetal tachycardia.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "BNF; Local Anesthesia Guidelines.")
]

# -------------------- MAGNESIUM SULFATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Magnesium Sulfate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Asthma, Eclampsia/Preeclampsia, Torsades de Pointes.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Asthma:[/b] 1.2–2 g IV over 20 mins.\n• [b]Eclampsia:[/b] 4 g IV loading, then 1 g/hour infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Asthma:[/b] 25–50 mg/kg IV (max 2 g) over 20 mins."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Neuromuscular Blockers:[/b] Enhances the effect (risk of prolonged paralysis).\n• [b]CCBs:[/b] Additive hypotension."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Flushing, sweating, hypotension.\n• Loss of deep tendon reflexes (early toxicity).\n• Respiratory depression, coma (severe toxicity).\n• Hypocalcemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]MONITOR: Deep tendon reflexes, respiratory rate (>12/min), urine output (>30 mL/h).[/color]\n• [b]Antidote:[/b] Calcium Gluconate 10% 10 mL IV."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Used routinely for eclampsia.\n• [b]Lactation:[/b] Excreted in breast milk. Use with caution."),
    ("REFERENCES", "info", "GINA 2024; NICE NG133.")
]

# -------------------- CALCIUM GLUCONATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Calcium Gluconate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hyperkalemia, Hypocalcemia, Magnesium Toxicity.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Hyperkalemia:[/b] 10–30 mL of 10% solution IV over 10 mins.\n• [b]Hypocalcemia:[/b] 10–20 mL of 10% solution IV.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.5–1 mL/kg of 10% solution IV (max 20 mL)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Ceftriaxone:[/b] Risk of precipitation in neonates.\n• [b]Digoxin:[/b] Risk of digoxin toxicity (calcium can potentiate)."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bradycardia, arrhythmias (if given too fast).\n• Hypotension.\n• Tissue necrosis if extravasation occurs."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT mix with Sodium Bicarbonate (precipitates).[/color]\n• Administer slowly (max 3-5 mL/min) via a large vein."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "UK Kidney Association Guidelines.")
]

# -------------------- CALCIUM CHLORIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Calcium Chloride")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Cardiac Arrest (Hyperkalemia, CCB toxicity), Hypocalcemia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 5–10 mL of 10% solution IV slowly.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1–0.2 mL/kg of 10% solution IV (max 10 mL)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Same as Calcium Gluconate (Ceftriaxone, Digoxin, Thiazides)."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Severe tissue necrosis if extravasation.\n• Bradycardia, arrhythmias.\n• Metabolic acidosis."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Highly irritating; requires central venous access if possible.[/color]\n• Contains 3 times more elemental calcium than Calcium Gluconate."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "AHA 2025 ACLS Guidelines.")
]

# -------------------- LABETALOL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Labetalol")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypertensive Emergency, Aortic Dissection.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]IV Bolus:[/b] 20 mg over 2 mins, then 40–80 mg every 10 mins (max 300 mg total).\n• [b]IV Infusion:[/b] 0.5–2 mg/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.2–1 mg/kg IV (max 40 mg/dose)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]CCBs:[/b] Risk of AV block and bradycardia.\n• [b]MAOIs:[/b] Hypertensive crisis.\n• [b]Cimetidine:[/b] Increases labetalol levels."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bradycardia, hypotension, heart block.\n• Bronchospasm (especially in asthmatics).\n• Scalp tingling, fatigue, dizziness."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Contraindicated in severe asthma, heart block, or decompensated heart failure.[/color]\n• Do not use in cocaine-induced hypertension."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Drug of choice for pregnancy-induced hypertension.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts. Safe."),
    ("REFERENCES", "info", "NICE NG133; BNF.")
]

# -------------------- HYDRALAZINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Hydralazine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypertensive Emergency (pregnancy), Acute Heart Failure.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 5–10 mg IV slowly over 20 mins. Repeat every 20-30 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1–0.2 mg/kg IV (max 20 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]MAOIs:[/b] Severe hypotension.\n• [b]NSAIDs:[/b] Decreased antihypertensive effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Reflex tachycardia, angina, headache.\n• Hypotension.\n• Lupus-like syndrome (with long-term use)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Unpredictable hypotensive effect; monitor BP closely.[/color]\n• Avoid in severe tachycardia or aortic dissection."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Safe in pregnancy for HTN.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "NICE NG133; BNF.")
]

# -------------------- FUROSEMIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Furosemide")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Pulmonary Edema, Fluid Overload, Hypertensive Emergency.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]IV:[/b] 20–40 mg slowly (naive), or 1-2.5x oral dose (chronic). Max rate 4 mg/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.5–2 mg/kg IV (max 40 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]NSAIDs:[/b] Decreased diuretic effect.\n• [b]Aminoglycosides:[/b] Increased ototoxicity.\n• [b]Digoxin:[/b] Hypokalemia increases digoxin toxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypokalemia, hyponatremia, hypovolemia.\n• Ototoxicity (tinnitus, deafness).\n• Acute kidney injury (AKI)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Administer slowly (max 4 mg/min) to avoid ototoxicity.[/color]\n• Monitor electrolytes, renal function, and urine output."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Crosses placenta.\n• [b]Lactation:[/b] Excreted in breast milk (may decrease milk production)."),
    ("REFERENCES", "info", "ESC 2021 Heart Failure Guidelines; BNF.")
]

# -------------------- ASPIRIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Aspirin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] ACS (STEMI/NSTEMI), Secondary prevention.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]ACS:[/b] 162–325 mg PO (chewed), then 75–100 mg daily.\n• [b]Secondary Prevention:[/b] 75–81 mg daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Kawasaki Disease:[/b] 80–100 mg/kg/day divided.\n• [color=#991B1B]CONTRAINDICATED in children with viral illness (Reye's syndrome).[/color]"),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Anticoagulants / NSAIDs:[/b] Increased risk of GI bleeding.\n• [b]Ibuprofen:[/b] Antagonizes the antiplatelet effect.\n• [b]Methotrexate:[/b] Increased toxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• GI irritation, peptic ulcer, upper GI bleeding.\n• Bronchospasm.\n• Tinnitus, hearing loss (high doses).\n• Hypersensitivity reactions."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]NEVER give to children/teenagers with fever/viral illness.[/color]\n• Contraindicated in active bleeding or severe aspirin allergy."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D (3rd trimester). Low-dose safe for preeclampsia. High doses cause premature closure of ductus arteriosus.\n• [b]Lactation:[/b] Excreted in breast milk. Avoid high doses."),
    ("REFERENCES", "info", "ESC 2023 ACS Guidelines; BNF.")
]

# -------------------- CLOPIDOGREL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Clopidogrel")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] ACS (DAPT with Aspirin), Post-PCI, Secondary prevention.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]ACS/PCI:[/b] 300–600 mg PO loading, then 75 mg PO daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• Rarely used; specialist use only."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Omeprazole/Esomeprazole:[/b] Reduce clopidogrel activation (use Pantoprazole).\n• [b]Anticoagulants / NSAIDs:[/b] Increased risk of bleeding."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bleeding (GI, intracranial, bruising).\n• Diarrhea, abdominal pain.\n• Thrombotic Thrombocytopenic Purpura (TTP - rare)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]CYP2C19 poor metabolizers may have reduced efficacy.[/color]\n• Contraindicated in active pathological bleeding.\n• Do not discontinue prematurely after PCI."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Use only if clearly needed.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "ESC 2023 ACS Guidelines; BNF.")
]

# -------------------- UNFRACTIONATED HEPARIN (UFH) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Unfractionated Heparin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] ACS, Venous Thromboembolism (VTE), Hemodialysis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]ACS:[/b] 60 units/kg IV bolus (max 4000 units), then 12 units/kg/hr infusion.\n• [b]VTE:[/b] 80 units/kg bolus, then 18 units/kg/hr infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Infant (<1 yr):[/b] 75 units/kg bolus, then 28 units/kg/hr.\n• [b]Child (>1 yr):[/b] 75 units/kg bolus, then 20 units/kg/hr."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Antiplatelets / NSAIDs:[/b] Increased bleeding risk.\n• [b]Nitroglycerin:[/b] Can reduce heparin activity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bleeding, bruising, hematoma.\n• Heparin-Induced Thrombocytopenia (HIT).\n• Hyperkalemia.\n• Osteoporosis (long-term use)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor platelets daily (risk of HIT).[/color]\n• [b]Antidote:[/b] Protamine Sulfate (1 mg per 100 units of heparin)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Does NOT cross the placenta (safe for fetus).\n• [b]Lactation:[/b] Not excreted in breast milk (large molecule). Safe."),
    ("REFERENCES", "info", "ACCP Guidelines; BNF.")
]

# -------------------- ENOXAPARIN (LMWH) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Enoxaparin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] VTE Prophylaxis/Treatment, ACS.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Prophylaxis:[/b] 40 mg SC once daily.\n• [b]Treatment:[/b] 1 mg/kg SC every 12 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Treatment:[/b] 1 mg/kg SC every 12 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Same as Unfractionated Heparin."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bleeding (less than UFH).\n• HIT (rare).\n• Injection site hematoma."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Reduce dose in severe renal impairment (CrCl < 30).[/color]\n• [b]Antidote:[/b] Protamine Sulfate (partially effective)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Preferred anticoagulant in pregnancy.\n• [b]Lactation:[/b] Not excreted in breast milk. Safe."),
    ("REFERENCES", "info", "ACCP Guidelines; BNF.")
]

# -------------------- ALTEPLASE (tPA) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Alteplase (tPA)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Acute Ischemic Stroke, STEMI, Massive PE.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Stroke:[/b] 0.9 mg/kg IV (max 90 mg). 10% bolus, rest over 60 mins.\n• [b]STEMI:[/b] 15 mg bolus, 0.75 mg/kg over 30 mins, then 0.5 mg/kg over 60 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• Specialized use only."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Anticoagulants / Antiplatelets:[/b] Severe bleeding risk.\n• [b]ACE inhibitors:[/b] Increased risk of angioedema."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Severe bleeding (Intracranial hemorrhage).\n• Reperfusion arrhythmias.\n• Allergic reactions."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]STRICT contraindications: Recent stroke, ICH, recent surgery, uncontrolled BP.[/color]\n• Monitor for neurological deterioration."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Risk of maternal hemorrhage.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "AHA/ASA Stroke Guidelines; ESC 2023.")
]

# -------------------- TRANEXAMIC ACID (TXA) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Tranexamic Acid")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Trauma Hemorrhage, Postpartum Hemorrhage.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 1 g IV over 10 mins, then 1 g IV infusion over 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 15 mg/kg IV (max 1 g) over 10 mins, then 2 mg/kg/hr for 8 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Prothrombotic agents:[/b] Increased risk of thrombosis.\n• [b]Anticoagulants:[/b] Antagonizes their effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nausea, vomiting, diarrhea.\n• Thromboembolism (rare but serious).\n• Seizures (high doses)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Give within 3 hours of trauma.[/color]\n• Reduce dose in renal impairment."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe (used for PPH).\n• [b]Lactation:[/b] Excreted in breast milk in very small amounts. Safe."),
    ("REFERENCES", "info", "CRASH-2 Trial; WOMAN Trial; BNF.")
]

# -------------------- PROTAMINE SULFATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Protamine Sulfate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Reversal of Unfractionated Heparin (UFH).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 1 mg neutralizes 100 units of heparin. Give 25–50 mg IV slowly over 10 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• Same ratio."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Blood products:[/b] Can interact.\n• [b]NPH insulin:[/b] Risk of severe allergic reaction."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Severe hypotension and bradycardia.\n• Anaphylaxis.\n• Pulmonary hypertension."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Administer SLOWLY (max 5 mg/min).[/color]\n• Have epinephrine ready."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "ACCP Guidelines; BNF.")
]

# -------------------- VITAMIN K (PHYTONADIONE) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Vitamin K (Phytonadione)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Reversal of Warfarin, Vitamin K deficiency.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Warfarin Reversal:[/b] 1–5 mg PO/IV (major bleeding: 5–10 mg IV).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Deficiency bleeding:[/b] 1 mg IV (0.5 mg if < 1 year)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Warfarin:[/b] Directly antagonizes its effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Anaphylactoid reactions (rare, with rapid IV push).\n• Injection site pain."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]IV administration should be very slow.[/color]\n• Prefer Oral/SC route if not life-threatening."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Safe (standard at birth).\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BCSH Guidelines; BNF.")
]

# -------------------- SALBUTAMOL (ALBUTEROL) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Salbutamol (Albuterol)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Asthma, COPD Exacerbation, Hyperkalemia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Nebulized:[/b] 2.5–5 mg every 20 mins.\n• [b]MDI:[/b] 4–10 puffs every 20 mins.\n• [b]IV:[/b] 5–20 mcg/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Nebulized:[/b] 2.5 mg (<5 yrs) or 5 mg (>5 yrs) every 20 mins."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Non-selective Beta-blockers:[/b] Antagonize bronchodilator effect.\n• [b]Diuretics:[/b] Increased risk of hypokalemia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, palpitations, arrhythmias.\n• Fine tremor.\n• Hypokalemia and hyperglycemia.\n• Lactic acidosis."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High doses can cause dangerous tachyarrhythmias and lactic acidosis.[/color]\n• Monitor K+ levels."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Safe for acute asthma.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "GINA 2024; BTS/SIGN Guidelines.")
]

# -------------------- IPRATROPIUM BROMIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Ipratropium Bromide")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Asthma, COPD Exacerbation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Nebulized:[/b] 0.5 mg every 4-6 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Nebulized:[/b] 0.25 mg (<5 years) or 0.5 mg (>5 years)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• No significant interactions. Can be mixed with salbutamol."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Dry mouth, bitter taste.\n• Urinary retention (rare).\n• Glaucoma exacerbation."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid contact with eyes (risk of acute angle-closure glaucoma).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Unknown if excreted in breast milk."),
    ("REFERENCES", "info", "GINA 2024; GOLD 2024.")
]

# -------------------- BUDESONIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Budesonide")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Asthma (maintenance), Croup (nebulized).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Asthma:[/b] Inhaled 200–800 mcg BID.\n• [b]Nebulized:[/b] 1–2 mg BID.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Croup:[/b] 2 mg nebulized as a single dose."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]CYP3A4 inhibitors:[/b] Increase systemic levels of budesonide."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Oral candidiasis (thrush).\n• Dysphonia.\n• Adrenal suppression (high doses)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Rinse mouth with water after inhalation to prevent oral thrush.[/color]\n• Do not use as a rescue inhaler."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Inhaled budesonide is safe.\n• [b]Lactation:[/b] Excreted in breast milk in minimal amounts. Safe."),
    ("REFERENCES", "info", "GINA 2024; BNF.")
]

# -------------------- AMINOPHYLLINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Aminophylline")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Asthma, COPD (rarely used now).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Loading Dose:[/b] 5 mg/kg IV over 20 mins (omit if on oral theophylline).\n• [b]Maintenance:[/b] 0.5 mg/kg/hour IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Loading Dose:[/b] 5–10 mg/kg IV over 20 mins.\n• [b]Maintenance:[/b] 0.5–1 mg/kg/hour IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Ciprofloxacin / Erythromycin:[/b] Increase aminophylline levels (risk of toxicity).\n• [b]Phenytoin / Rifampicin:[/b] Decrease aminophylline levels."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, arrhythmias.\n• Nausea, vomiting, abdominal pain.\n• Seizures (sign of severe toxicity)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Very narrow therapeutic window. Monitor theophylline levels if possible.[/color]\n• Reduce dose in heart failure or liver disease."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Crosses placenta.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "GINA 2024; BNF.")
]

# -------------------- TERBUTALINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Terbutaline")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Acute Asthma (SC), Tocolysis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]SC:[/b] 0.25–0.5 mg (max 1 mg in 24h).\n• [b]Nebulized:[/b] 5–10 mg.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]SC:[/b] 0.01 mg/kg (max 0.3 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Beta-blockers:[/b] Antagonize effect.\n• [b]Corticosteroids:[/b] Increased risk of hypokalemia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Tachycardia, palpitations, tremor.\n• Hypokalemia.\n• Pulmonary edema (prolonged tocolysis)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Prolonged use as a tocolytic is contraindicated (risk of maternal pulmonary edema).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Used with strict monitoring.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "GINA 2024; BNF.")
]

# -------------------- HYDROCORTISONE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Hydrocortisone")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Adrenal Crisis, Anaphylaxis (adjunct), Severe Asthma.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Adrenal Crisis:[/b] 100–200 mg IV bolus, then 50–100 mg q6h.\n• [b]Asthma:[/b] 100–200 mg IV q6h.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Adrenal Crisis:[/b] 2–4 mg/kg IV bolus, then 2–4 mg/kg q6h."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]NSAIDs:[/b] Increased risk of GI ulceration.\n• [b]Live vaccines:[/b] Contraindicated.\n• [b]Insulin:[/b] Corticosteroids raise blood glucose."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperglycemia, fluid retention, hypertension.\n• Hypokalemia.\n• Immunosuppression."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do not stop abruptly if used for > 2 weeks (risk of adrenal crisis).[/color]\n• Watch for signs of infection."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Safe when indicated.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts. Safe."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign 2021; BNF.")
]

# -------------------- METHYLPREDNISOLONE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Methylprednisolone")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Asthma/COPD, MS relapse.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Asthma/COPD:[/b] 40–125 mg IV q6-8h.\n• [b]MS Relapse:[/b] 1 g IV daily for 3-5 days.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Asthma:[/b] 1–2 mg/kg IV daily (max 60 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Similar to Hydrocortisone."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperglycemia, hypertension, fluid retention.\n• Psychosis, insomnia.\n• Peptic ulcer disease."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High doses can cause arrhythmias (especially IV push).[/color]\n• Administer slowly."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "GINA 2024; BNF.")
]

# -------------------- DEXAMETHASONE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dexamethasone")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Croup (Pediatric), Meningitis, Cerebral Edema.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Meningitis:[/b] 10 mg IV q6h.\n• [b]Cerebral Edema:[/b] 10 mg IV bolus, then 4 mg q6h.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Croup:[/b] 0.15–0.6 mg/kg PO/IV (max 10 mg) single dose."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Antidiabetics:[/b] Dexamethasone raises blood sugar.\n• [b]Phenytoin / Rifampicin:[/b] Decrease steroid effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperglycemia, hypertension.\n• GI upset.\n• Hiccups, insomnia, mood changes."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT use steroids in traumatic brain injury.[/color]\n• Give before or with first dose of antibiotics in meningitis."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Used for fetal lung maturity.\n• [b]Lactation:[/b] Excreted in breast milk in minimal amounts."),
    ("REFERENCES", "info", "NICE NG240; BNF.")
]

# -------------------- DIPHENHYDRAMINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Diphenhydramine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Allergic reactions, Dystonic reactions.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 25–50 mg IV/IM/PO q4-6h (max 400 mg/day).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1 mg/kg IV/PO q6h (max 50 mg/dose)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]CNS Depressants:[/b] Additive sedation.\n• [b]MAOIs:[/b] Prolonged anticholinergic effects."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Drowsiness, dizziness.\n• Dry mouth, blurred vision.\n• Paradoxical excitation (children)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT use as a substitute for adrenaline in anaphylaxis.[/color]\n• Avoid in neonates."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Use with caution.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Resuscitation Council UK.")
]

# -------------------- CHLORPHENIRAMINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Chlorpheniramine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Allergic reactions.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 10–20 mg IV/IM slowly (max 40 mg/day).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.35 mg/kg/day divided into 4 doses."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]CNS Depressants:[/b] Additive sedation."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Drowsiness, dizziness.\n• Dry mouth, blurred vision."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid in neonates and premature infants.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B.\n• [b]Lactation:[/b] Excreted in breast milk. Use with caution."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- LORAZEPAM --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Lorazepam")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Status Epilepticus, Sedation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Status Epilepticus:[/b] 0.1 mg/kg IV (max 4 mg).\n• [b]Sedation:[/b] 1–2 mg IV slowly.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Status Epilepticus:[/b] 0.1 mg/kg IV (max 4 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Opioids / CNS Depressants:[/b] Severe respiratory depression and coma."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Respiratory depression, apnea.\n• Hypotension.\n• Sedation, confusion."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High-alert medication. Have bag-mask ventilation ready.[/color]\n• Flumazenil is the antidote."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Risk of fetal malformations (cleft lip/palate).\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "NCS Status Epilepticus Guideline; BNF.")
]

# -------------------- ETOMIDATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Etomidate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Rapid Sequence Intubation (RSI).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 0.3 mg/kg IV bolus (usually 20 mg).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.3 mg/kg IV bolus."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other CNS depressants:[/b] Additive sedation."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Adrenal suppression (transient).\n• Myoclonus.\n• Nausea, vomiting."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT use in septic shock (adrenal suppression worsens mortality).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "Difficult Airway Society Guidelines; BNF.")
]

# -------------------- DEXMEDETOMIDINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dexmedetomidine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] ICU Sedation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Loading:[/b] 1 mcg/kg IV over 10 mins (optional).\n• [b]Maintenance:[/b] 0.2–0.7 mcg/kg/hour IV infusion.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Maintenance:[/b] 0.2–0.7 mcg/kg/hour IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Anesthetics / Opioids / Benzodiazepines:[/b] Additive sedative effects.\n• [b]Beta-blockers:[/b] Additive bradycardia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Bradycardia, hypotension.\n• Hypertension (transient).\n• Dry mouth, nausea."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor heart rate and BP continuously.[/color]\n• Avoid in advanced heart block."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "ICU Sedation Guidelines; BNF.")
]

# -------------------- ROCURONIUM --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Rocuronium")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Rapid Sequence Intubation (RSI), Muscle relaxation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]RSI:[/b] 1–1.2 mg/kg IV push.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]RSI:[/b] 1.2 mg/kg IV push."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Aminoglycosides / Magnesium:[/b] Enhance neuromuscular blockade.\n• [b]Phenytoin:[/b] May decrease the effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Prolonged paralysis.\n• Anaphylaxis (rare).\n• Tachycardia, hypertension (mild)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Prolonged paralysis in renal or hepatic failure.[/color]\n• Ensure sedation is adequate.\n• [b]Antidote:[/b] Sugammadex or Neostigmine."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Used in C-section.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "Difficult Airway Society; BNF.")
]

# -------------------- SUCCINYLCHOLINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Succinylcholine (Suxamethonium)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Rapid Sequence Intubation (RSI).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]RSI:[/b] 1–1.5 mg/kg IV push.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]RSI:[/b] 2 mg/kg IV push.\n"
     "[color=#991B1B]CONTRAINDICATED in children with unknown neuromuscular disease.[/color]"),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Digoxin:[/b] Increased risk of arrhythmias.\n• [b]Non-depolarizing muscle relaxants:[/b] Antagonize effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperkalemia (can cause fatal cardiac arrest).\n• Malignant hyperthermia.\n• Bradycardia (children with repeated doses).\n• Muscle fasciculations."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]CONTRAINDICATED in major burns, crush injuries, spinal cord injury (after 24-48h), or hyperkalemia.[/color]\n• Avoid in personal/family history of malignant hyperthermia."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Used in C-section.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "AHA 2025; BNF.")
]

# -------------------- NALOXONE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Naloxone")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Opioid Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 0.04–0.4 mg IV, titrate every 2-3 mins to RR > 12/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1 mg/kg IV (max 2 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Opioids:[/b] Directly antagonizes their effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Acute opioid withdrawal (agitation, tachycardia, hypertension).\n• Pulmonary edema (rare).\n• Seizures (rare)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Short half-life (30-90 mins). Patients may re-sedate after drug wears off.[/color]\n• Can precipitate fatal withdrawal in opioid-dependent neonates."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Use with caution in opioid-dependent mothers.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "AHA 2025; BNF.")
]

# -------------------- FLUMAZENIL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Flumazenil")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Benzodiazepine Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 0.2 mg IV over 15 seconds. Repeat 0.3 mg, then 0.5 mg every 1 min (max 3 mg).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.01 mg/kg (max 0.2 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Benzodiazepines:[/b] Antagonizes their effect.\n• [b]TCAs:[/b] Flumazenil can induce seizures in mixed TCA/benzo overdose."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Seizures (especially in mixed overdose).\n• Acute withdrawal syndrome.\n• Nausea, vomiting."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]CONTRAINDICATED in TCA overdose or chronic benzodiazepine users (risk of fatal seizures).[/color]\n• Short half-life - patients may re-sedate."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Not recommended.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "BNF; Toxicology Guidelines.")
]

# -------------------- PARACETAMOL (ACETAMINOPHEN) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Paracetamol (Acetaminophen)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Mild to moderate pain, Fever.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 500–1000 mg every 4-6 hours (max 4 g/24h).\n• IV: 1 g every 6 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 15 mg/kg every 4-6 hours (max 60 mg/kg/day)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Warfarin:[/b] Regular high-dose can increase INR.\n• [b]Alcohol:[/b] Increases risk of hepatotoxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hepatotoxicity (in overdose).\n• Nausea, rash (rare)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]STRICT MAXIMUM DOSE: 4 g/day (reduce to 2-3 g in liver disease or alcoholics).[/color]\n• Antidote: N-Acetylcysteine.\n• Check total dose in combination products."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safest analgesic in pregnancy.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts. Safe."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- TRAMADOL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Tramadol")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Moderate to severe pain.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 50–100 mg every 4-6 hours (max 400 mg/day).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1–2 mg/kg (max 100 mg/dose). [color=#991B1B]Not recommended < 12 years.[/color]"),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]SSRIs / SNRIs / MAOIs:[/b] Risk of Serotonin Syndrome.\n• [b]Benzodiazepines:[/b] Severe respiratory depression."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nausea, vomiting, dizziness, drowsiness.\n• Seizures (lowers seizure threshold).\n• Serotonin syndrome."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid in patients with epilepsy.[/color]\n• High risk of dependence."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Crosses placenta.\n• [b]Lactation:[/b] Excreted in breast milk. Avoid."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- HALOPERIDOL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Haloperidol")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Acute Agitation/Psychosis, Delirium.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 2–5 mg IV/IM (max 20 mg/day).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.01–0.05 mg/kg (specialist use)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]QT-prolonging drugs:[/b] Additive QT prolongation.\n• [b]CNS Depressants:[/b] Additive sedation."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Extrapyramidal symptoms (EPS).\n• QT prolongation, Torsades.\n• Neuroleptic Malignant Syndrome (NMS)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High risk of QT prolongation (monitor ECG).[/color]\n• Have Diphenhydramine ready for acute dystonia."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Risk of neonatal EPS.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; ICU Delirium Guidelines.")
]

# -------------------- ONDANSETRON --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Ondansetron")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Nausea and Vomiting.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 4–8 mg IV/PO every 8-12 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1–0.15 mg/kg IV/PO (max 4 mg per dose)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]QT-prolonging drugs:[/b] Additive QT prolongation.\n• [b]Apomorphine:[/b] Severe hypotension."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Headache, constipation.\n• QT prolongation.\n• Transient elevation in liver enzymes."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]QT prolongation (monitor ECG in high-risk patients).[/color]\n• Single IV dose > 16 mg is contraindicated."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe for hyperemesis gravidarum.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- METOCLOPRAMIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Metoclopramide")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Nausea/Vomiting, Gastroparesis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 10 mg IV/IM/PO every 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.1–0.15 mg/kg every 8 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Anticholinergics:[/b] Antagonize the prokinetic effect.\n• [b]Antipsychotics:[/b] Increased risk of EPS."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Extrapyramidal symptoms (acute dystonia).\n• Restlessness (akathisia).\n• Hyperprolactinemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High risk of acute dystonic reactions. Have Procyclidine ready.[/color]\n• Do NOT use for more than 5 days."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- LEVETIRACETAM --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Levetiracetam")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Status Epilepticus, Seizure prophylaxis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Status Epilepticus:[/b] 60 mg/kg IV (max 4500 mg) over 15 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 40–60 mg/kg IV (max 4500 mg) over 15 mins."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Minimal drug interactions compared to older antiepileptics."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Somnolence, dizziness, fatigue.\n• Behavioral changes (irritability, aggression).\n• Stevens-Johnson Syndrome (rare)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Requires dose adjustment in renal impairment.[/color]\n• Do not stop abruptly."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "NCS Status Epilepticus Guidelines; BNF.")
]

# -------------------- PHENYTOIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Phenytoin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Status Epilepticus.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 20 mg/kg IV (max 1500 mg) at max rate 50 mg/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 20 mg/kg IV (max 1500 mg) at max rate 1–3 mg/kg/min."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Warfarin:[/b] Alters anticoagulant effect.\n• [b]Corticosteroids:[/b] Reduces steroid effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypotension, bradycardia, arrhythmias.\n• Nystagmus, ataxia.\n• Purple glove syndrome."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]MUST dilute in 0.9% Saline ONLY (precipitates in Dextrose).[/color]\n• Do NOT give faster than 50 mg/min."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Fetal hydantoin syndrome.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "NCS Status Epilepticus Guidelines; BNF.")
]

# -------------------- FOSPHENYTOIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Fosphenytoin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Status Epilepticus.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 20 mg PE/kg IV (max 1500 mg PE) at max rate 150 mg PE/min.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 20 mg PE/kg IV (max 1500 mg PE) at max rate 3 mg PE/kg/min."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Same as Phenytoin."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Paresthesias, pruritus.\n• Hypotension, bradycardia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Dosing is in Phenytoin Equivalents (PE).[/color]\n• Can be diluted in D5W or NaCl."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Same risks as Phenytoin.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "NCS Status Epilepticus Guidelines; BNF.")
]

# -------------------- SODIUM VALPROATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Sodium Valproate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Status Epilepticus, Bipolar disorder.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Status Epilepticus:[/b] 40 mg/kg IV (max 3000 mg) over 10 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 40 mg/kg IV (max 3000 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Lamotrigine:[/b] Increases risk of severe rash.\n• [b]Carbapenems:[/b] Reduce valproate levels drastically."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperammonemia, hepatotoxicity.\n• Pancreatitis.\n• Thrombocytopenia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Highly teratogenic (neural tube defects). Contraindicated in women of childbearing potential unless essential.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D (highly teratogenic).\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "NCS Status Epilepticus Guidelines; BNF.")
]

# -------------------- MANNITOL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Mannitol")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Raised Intracranial Pressure (ICP).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 0.25–1 g/kg IV over 20 mins.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.25–1 g/kg IV over 20 mins."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Nephrotoxic drugs:[/b] Increased risk of AKI."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Fluid overload, pulmonary edema.\n• Hypernatremia.\n• Acute Kidney Injury."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Use an in-line filter (crystallization can occur).[/color]\n• Monitor electrolytes and osmolality."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "BTF Guidelines; BNF.")
]

# -------------------- HYPERTONIC SODIUM CHLORIDE (3%) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Hypertonic Sodium Chloride (3%)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe symptomatic hyponatremia, Raised ICP.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Hyponatremia:[/b] 100–150 mL IV over 20 mins.\n• [b]Raised ICP:[/b] 250 mL IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 2.5–5 mL/kg IV over 15-20 mins."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other sodium-containing fluids:[/b] Additive hypernatremia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypernatremia, metabolic acidosis.\n• Pulmonary edema.\n• Osmotic demyelination."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Central line preferred (highly irritating).[/color]\n• Monitor Na+ levels every 2-4 hours."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "European Guidelines on Hyponatremia; BNF.")
]

# -------------------- NIMODIPINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Nimodipine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Prevention of cerebral vasospasm after SAH.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 60 mg PO/NG every 4 hours for 21 days.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• Not established."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]CYP3A4 inhibitors:[/b] Increase nimodipine levels (severe hypotension).\n• [b]CYP3A4 inducers:[/b] Decrease nimodipine levels."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypotension.\n• Headache.\n• Reflex tachycardia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor BP closely.[/color]\n• If given via NG tube, crush and extract immediately."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "AHA/ASA SAH Guidelines; BNF.")
]

# -------------------- THIAMINE (VITAMIN B1) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Thiamine (Vitamin B1)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Wernicke's Encephalopathy, Thiamine deficiency.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Prophylaxis:[/b] 100 mg IV/IM daily.\n• [b]Encephalopathy:[/b] 500 mg IV TID for 3-5 days.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 10–50 mg IV/IM daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [color=#991B1B]CRITICAL: Always give thiamine BEFORE glucose in alcoholics.[/color]"),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Anaphylaxis (rare).\n• Local irritation."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Must be given BEFORE glucose in alcoholics to prevent Wernicke's.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "NICE Alcohol Guidelines; BNF.")
]

# -------------------- MEROPENEM --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Meropenem")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe infections (intra-abdominal, pneumonia, meningitis).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Severe infection:[/b] 1 g IV every 8 hours.\n• [b]Meningitis:[/b] 2 g IV every 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 20 mg/kg IV every 8 hours (max 1 g)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Valproate:[/b] Significantly reduces valproate levels. Avoid combination."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Seizures (especially in renal impairment).\n• Diarrhea, nausea, vomiting.\n• C. difficile-associated diarrhea."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Requires dose adjustment in renal impairment.[/color]\n• High risk of seizures."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- VANCOMYCIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Vancomycin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] MRSA infections, C. difficile (oral).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]IV:[/b] 15–20 mg/kg IV every 8-12 hours.\n• [b]PO (C. diff):[/b] 125 mg PO every 6 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 15 mg/kg IV every 6 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Aminoglycosides:[/b] Additive nephrotoxicity and ototoxicity.\n• [b]Loop diuretics:[/b] Increased risk of ototoxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nephrotoxicity, ototoxicity.\n• Red Man Syndrome.\n• Phlebitis."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Infuse over at least 60 minutes to prevent Red Man Syndrome.[/color]\n• Monitor trough levels (target 15-20 mcg/mL)."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B.\n• [b]Lactation:[/b] Excreted in breast milk in small amounts."),
    ("REFERENCES", "info", "IDSA MRSA Guidelines; BNF.")
]

# -------------------- METRONIDAZOLE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Metronidazole")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Anaerobic infections, C. difficile.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 500 mg IV/PO every 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 7.5 mg/kg IV/PO every 8 hours (max 500 mg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Alcohol:[/b] Disulfiram-like reaction.\n• [b]Warfarin:[/b] Increases INR."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nausea, metallic taste.\n• Dark urine (harmless).\n• Peripheral neuropathy."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid alcohol during and for 48 hours after treatment.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe in 2nd/3rd trimester.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- AMIKACIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Amikacin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe gram-negative infections.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 15 mg/kg once daily IV/IM.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 15–20 mg/kg once daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other nephrotoxins:[/b] Severe nephrotoxicity.\n• [b]Loop diuretics:[/b] Increased ototoxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nephrotoxicity.\n• Ototoxicity.\n• Neuromuscular blockade."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor renal function and drug levels.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Fetal ototoxicity.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- GENTAMICIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Gentamicin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe gram-negative infections.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 5–7 mg/kg once daily IV/IM.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 5–7.5 mg/kg once daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• Same as Amikacin."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nephrotoxicity, ototoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor renal function and drug levels.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. Fetal ototoxicity.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- AZITHROMYCIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Azithromycin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Community-acquired pneumonia, Pertussis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]IV:[/b] 500 mg daily.\n• [b]PO:[/b] 500 mg day 1, then 250 mg daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 10 mg/kg day 1, then 5 mg/kg daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]QT-prolonging drugs:[/b] Additive QT prolongation.\n• [b]Antacids:[/b] Reduce absorption."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Diarrhea, nausea.\n• QT prolongation.\n• Hepatotoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor ECG in patients with risk factors for QT prolongation.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF; IDSA CAP Guidelines.")
]

# -------------------- DOXYCYCLINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Doxycycline")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Atypical pneumonia, Rickettsial infections.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 100 mg every 12 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 2.2 mg/kg every 12 hours.\n[color=#991B1B]Avoid in children < 8 years.[/color]"),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Antacids / Iron / Calcium:[/b] Reduce absorption."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Photosensitivity.\n• Esophageal irritation.\n• Teeth discoloration (children)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid in pregnancy and children <8 (except life-threatening infections).[/color]\n• Take with plenty of water."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- CLINDAMYCIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Clindamycin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Anaerobic infections, MRSA skin infections.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]IV:[/b] 600–900 mg every 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]IV:[/b] 10 mg/kg every 8 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Neuromuscular blockers:[/b] Enhances blockade."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• C. difficile-associated diarrhea (high risk).\n• Diarrhea, nausea."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High risk of C. difficile colitis.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- AMPICILLIN-SULBACTAM --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Ampicillin-Sulbactam")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Intra-abdominal infections, skin infections.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 1.5–3 g IV every 6 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 100–200 mg/kg/day divided q6h."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Allopurinol:[/b] Increased risk of rash.\n• [b]Methotrexate:[/b] Increased toxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Diarrhea, nausea.\n• Rash (penicillin allergy)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Contraindicated in severe penicillin allergy.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- ACYCLOVIR --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Acyclovir")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] HSV, VZV, Encephalitis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]HSV/VZV:[/b] 5–10 mg/kg IV every 8 hours.\n• [b]Encephalitis:[/b] 10 mg/kg IV every 8 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Neonatal HSV:[/b] 20 mg/kg IV every 8 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Nephrotoxic drugs:[/b] Additive nephrotoxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nephrotoxicity (crystal nephropathy).\n• Neurotoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Ensure good hydration.[/color]\n• Infuse slowly over 1 hour."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- FLUCONAZOLE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Fluconazole")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Candida infections, Cryptococcal meningitis.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Loading:[/b] 400 mg, then 200–400 mg daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 12 mg/kg loading, then 6–12 mg/kg daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]QT-prolonging drugs:[/b] Additive QT prolongation.\n• [b]Warfarin:[/b] Increases INR."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• QT prolongation.\n• Hepatotoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor liver function and ECG.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category D. High doses in 1st trimester associated with birth defects.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF; Sanford Guide.")
]

# -------------------- SODIUM CHLORIDE 0.9% --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Sodium Chloride 0.9% (Normal Saline)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Fluid resuscitation, Maintenance, Dilution.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 500–1000 mL IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 10–20 mL/kg IV bolus."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Lithium:[/b] Sodium restriction increases lithium reabsorption."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypernatremia, hyperchloremic acidosis.\n• Fluid overload."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid in fluid overload (heart failure, renal failure).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "NICE IV Fluids Guidelines; BNF.")
]

# -------------------- LACTATED RINGER'S --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Lactated Ringer's Solution")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Fluid resuscitation, Burns, Trauma.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 500–1000 mL IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 10–20 mL/kg IV bolus."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Blood Transfusion:[/b] Contains calcium, can cause clotting (flush line).\n• [b]Ceftriaxone:[/b] Avoid mixing."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperkalemia (contains K+).\n• Fluid overload."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Avoid in severe hyperkalemia.[/color]\n• Preferred over normal saline in large-volume resuscitation."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "ATLS Guidelines; BNF.")
]

# -------------------- DEXTROSE 10% --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dextrose 10% (D10W)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypoglycemia, Maintenance fluid.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 150–200 mL IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 2–5 mL/kg IV bolus."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Insulin:[/b] Directly opposes the effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperglycemia.\n• Fluid overload.\n• Hyponatremia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT use in isolation for resuscitation.[/color]\n• Give thiamine first in alcoholics."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "BNF; BSPED Guidelines.")
]

# -------------------- DEXTROSE 50% --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Dextrose 50% (D50W)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Hypoglycemia (adults only).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 25–50 mL IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [color=#991B1B]CONTRAINDICATED in children (use D10W).[/color]"),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Insulin:[/b] Directly opposes the effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Severe tissue necrosis if extravasation.\n• Hyperglycemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]NEVER give to children.[/color]\n• Administer via a large vein."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- REGULAR INSULIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Regular Insulin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] DKA, HHS, Hyperkalemia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]DKA:[/b] 0.1 unit/kg/hour IV infusion.\n• [b]Hyperkalemia:[/b] 10 units IV with 25g glucose.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]DKA:[/b] 0.05–0.1 unit/kg/hour IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Beta-blockers:[/b] Mask symptoms of hypoglycemia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypoglycemia.\n• Hypokalemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]NEVER give if K+ < 3.3 mmol/L.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "ADA 2024 Guidelines; JBDS DKA Guidelines.")
]

# -------------------- POTASSIUM CHLORIDE (KCL) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Potassium Chloride (KCl)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypokalemia.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 20–40 mmol KCl in 1 L of fluid over 1-4 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.3–0.5 mmol/kg/hour (max 20 mmol/hr)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]ACE inhibitors / ARBs:[/b] Increase risk of hyperkalemia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperkalemia (fatal arrhythmias).\n• Phlebitis."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]NEVER give as IV bolus or undiluted (fatal cardiac arrest).[/color]\n• Use an infusion pump."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category A. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "UK Kidney Association Guidelines; BNF.")
]

# -------------------- SODIUM BICARBONATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Sodium Bicarbonate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Severe Metabolic Acidosis, Hyperkalemia, TCA Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Acidosis:[/b] 1–2 amps (8.4%) IV slowly.\n• [b]TCA Overdose:[/b] 1–2 mmol/kg IV bolus.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1–2 mEq/kg IV slowly."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Calcium:[/b] Forms precipitate (do not mix).\n• [b]Catecholamines:[/b] Inactivated if mixed."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Metabolic alkalosis.\n• Hypernatremia.\n• Cerebral edema (in DKA)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Do NOT use routinely in DKA.[/color]\n• Do NOT mix with calcium or catecholamines."),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "AHA 2025; BNF.")
]

# -------------------- SODIUM ZIRCONIUM CYCLOSILICATE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Sodium Zirconium Cyclosilicate")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hyperkalemia (chronic).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 10 g TID for up to 48 hours, then 5–10 g daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• Not established."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other Oral Medications:[/b] May reduce absorption (separate by 2 hours)."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Edema (fluid retention).\n• Hypokalemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Not for emergency treatment of hyperkalemia.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "UK Kidney Association Hyperkalemia Guidelines.")
]

# -------------------- GLUCAGON --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Glucagon")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hypoglycemia (no IV), Beta-blocker OD.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Hypoglycemia:[/b] 1 mg IM/SC.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.5 mg IM/SC (<25 kg) or 1 mg (>25 kg)."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Beta-blockers:[/b] May be ineffective for hypoglycemia."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Nausea, vomiting.\n• Hyperglycemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Ineffective in alcoholics.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "BNF; Toxicology Guidelines.")
]

# -------------------- OCTREOTIDE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Octreotide")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Variceal Bleeding, Sulfonylurea Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Variceal:[/b] 50 mcg IV bolus, then 50 mcg/hr.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]Sulfonylurea OD:[/b] 1–2 mcg/kg SC."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Insulin/Sulfonylureas:[/b] Octreotide suppresses insulin secretion."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyperglycemia/hypoglycemia.\n• Abdominal pain."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor blood glucose closely.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "Baveno VII Guidelines; TOXBASE.")
]

# -------------------- DESMOPRESSIN --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Desmopressin")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Diabetes Insipidus, Hemophilia A.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]DI:[/b] 1–4 mcg IV/SC daily.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• [b]DI:[/b] 0.3–1 mcg IV/SC daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Carbamazepine:[/b] Enhances antidiuretic effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hyponatremia (seizures).\n• Headache."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Monitor sodium levels.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "BNF; Endocrine Society Guidelines.")
]

# -------------------- PANTOPRAZOLE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Pantoprazole")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] GI Bleeding, GERD.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]GI Bleed:[/b] 80 mg IV bolus, then 8 mg/hr.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.5–1 mg/kg IV/PO daily."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Clopidogrel:[/b] Minimal interaction (preferred PPI)."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Headache, diarrhea.\n• Hypomagnesemia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Use oral route when possible.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Use if clearly needed.\n• [b]Lactation:[/b] Excreted in breast milk."),
    ("REFERENCES", "info", "NICE CG141; BNF.")
]

# -------------------- FAMOTIDINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Famotidine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Peptic Ulcer Disease, GERD.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 20 mg every 12 hours.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 0.25–0.5 mg/kg every 12 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Ketoconazole:[/b] Reduced absorption."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Headache.\n• Confusion (elderly)."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Reduce dose in renal impairment.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Excreted in breast milk. Safe."),
    ("REFERENCES", "info", "BNF.")
]

# -------------------- LACTULOSE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Lactulose")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Hepatic Encephalopathy, Constipation.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• [b]Hepatic Encephalopathy:[/b] 30–45 mL TID.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1–3 mL/kg/day."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Antibiotics:[/b] May reduce lactulose efficacy."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Diarrhea, abdominal cramps.\n• Hypernatremia."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Adjust dose to achieve 2-3 soft stools per day.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "EASL Hepatic Encephalopathy Guidelines; BNF.")
]

# -------------------- ACTIVATED CHARCOAL --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Activated Charcoal")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Acute Poisoning (within 1 hour).\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 50 g PO/NG.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 1 g/kg PO/NG."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Other Oral Medications:[/b] Adsorbs them."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Constipation, bowel obstruction.\n• Aspiration pneumonitis."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]CONTRAINDICATED in unprotected airway or ingestion of caustic substances.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "TOXBASE; BNF.")
]

# -------------------- N-ACETYLCYSTEINE (NAC) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "N-Acetylcysteine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Paracetamol Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• Bag 1: 150 mg/kg over 1 hour.\n• Bag 2: 50 mg/kg over 4 hours.\n• Bag 3: 100 mg/kg over 16 hours."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Nitroglycerin:[/b] NAC can potentiate hypotension."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Anaphylactoid reaction.\n• Nausea, vomiting."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]High risk of anaphylactoid reactions.[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category B. Safe (do not withhold in overdose).\n• [b]Lactation:[/b] Safe."),
    ("REFERENCES", "info", "TOXBASE; Paracetamol Overdose Guidelines.")
]

# -------------------- PRALIDOXIME (2-PAM) --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Pralidoxime (2-PAM)")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Organophosphate Poisoning.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 1–2 g IV over 15-30 mins, then 500 mg/hour.\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 20–50 mg/kg IV over 15-30 mins, then 10–20 mg/kg/hour."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Atropine:[/b] Synergistic effect."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypertension, tachycardia.\n• Muscle rigidity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Must be given early (before 'aging' of the enzyme occurs - usually within 24-48 hours).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "TOXBASE.")
]

# -------------------- DEFEROXAMINE --------------------
DRUGS_TOPICS[("Emergency & ICU Drugs", "Deferoxamine")] = [
    ("1. DOSAGE AND INDICATIONS", "success", 
     "[b]INDICATIONS:[/b] Iron Overdose.\n\n"
     "[b]ADULT DOSAGE:[/b]\n• 15 mg/kg/hour IV infusion (max 80 mg/kg/day).\n\n"
     "[b]PEDIATRIC DOSAGE:[/b]\n• 15 mg/kg/hour IV infusion."),
    ("2. INTERACTION WITH OTHER DRUGS", "warning", 
     "• [b]Vitamin C:[/b] Enhances iron excretion but may increase cardiac toxicity."),
    ("3. ADVERSE EFFECTS", "danger", 
     "• Hypotension, tachycardia.\n• Nephrotoxicity."),
    ("4. WARNING", "danger", 
     "• [color=#991B1B]Infuse slowly (rapid infusion causes severe hypotension).[/color]"),
    ("5. SAFETY IN PREGNANCY AND LACTATION", "info", 
     "• [b]Pregnancy:[/b] Category C. Use only for life-threatening iron toxicity.\n• [b]Lactation:[/b] Unknown."),
    ("REFERENCES", "info", "TOXBASE; BNF.")
]