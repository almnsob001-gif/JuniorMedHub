# data_medical.py
MEDICAL_DATA = {
    "Medical Emergencies": {
        "Cardiovascular": [
            "Adult Cardiac Arrest", "Acute Coronary Syndrome (ACS)", 
            "Acute Heart Failure and Cardiogenic Pulmonary Edema", "Cardiogenic Shock", 
            "Symptomatic Bradycardia", "Adult Tachyarrhythmias", 
            "Hypertensive Emergency", "Acute Aortic Dissection",
            "Acute Pericardial Tamponade", "Atrial Fibrillation with RVR", 
            "ACS Complications and Deterioration", "Acute RV Failure and Obstructive Shock",
            "Infective Endocarditis with Acute Complications", 
            "Acute Myocarditis and Fulminant Myocarditis",
            "Acute Limb Ischemia"
        ],
        "Respiratory": [
            "Acute Pulmonary Embolism (PE)", "Acute Severe Asthma",
            "Acute Exacerbation of COPD", "Acute Respiratory Failure",
            "Pneumothorax and Tension Pneumothorax", "Anaphylaxis",
            "Acute Severe Asthma and Near-Fatal Asthma", "Massive Hemoptysis and Airway Bleeding",
            "Sickle Cell Acute Chest Syndrome", "Acute Angioedema with Airway Compromise",
            "Acute Epiglottitis"
        ],
        "Gastrointestinal": [
            "Acute Upper Gastrointestinal Bleeding", "Acute Pancreatitis",
            "Acute Liver Failure and Hepatic Encephalopathy",
            "Acute Upper Gastrointestinal Bleeding and Variceal Hemorrhage",
            "Acute Pancreatitis and Severe Pancreatitis", "Acute Cholangitis and Obstructive Jaundice",
            "Acute Mesenteric Ischemia", "Acute Esophageal Variceal Hemorrhage"
        ],
        "Renal": [
            "Acute Kidney Injury (AKI) and Uremic Emergencies", 
            "Severe Hyperkalemia and Life-Threatening Electrolyte Disorders",
            "Acute Severe Hyponatremia and Sodium Disorders",
            "Acute Severe Metabolic Acidosis",
            "Acute Hyperkalemia and ECG Changes", 
            "Acute Kidney Injury and Emergency Dialysis Indications",
            "Hypernatremia and Severe Water Deficit",
            "Pulmonary–Renal Syndrome and Diffuse Alveolar Hemorrhage",
            "Acute Urinary Retention",
            "Acute Severe Hyperphosphatemia"
        ],
        "Endocrinology": [
            "Hypoglycemia and Hyperglycemic Crises",
            "Adrenal Crisis and Acute Adrenal Insufficiency",
            "Insulin-Related Emergencies and Severe Hypoglycemia",
            "Thyroid Storm and Myxedema Coma",
            "Adrenal Crisis (Acute Adrenal Insufficiency)",
            "Hyperosmolar Hyperglycemic State (HHS)",
            "Severe Calcium Disorders: Hypercalcemia and Hypocalcemia",
            "Acute Adrenal Incidental Hemorrhage with Adrenal Crisis"
        ],
        "Neurology": [
            "Acute Ischemic Stroke", "Spontaneous Intracerebral Hemorrhage (ICH)",
            "Convulsive Status Epilepticus", "Acute Altered Mental Status",
            "Guillain–Barré Syndrome (GBS)", "Myasthenic Crisis",
            "Acute Spinal Cord Compression", "Cauda Equina Syndrome"
        ],
        "Infectious": [
            "Acute Meningitis and Encephalitis", "Sepsis and Septic Shock",
            "Dengue Fever and Severe Dengue", "Chikungunya", 
            "Malaria and Severe Malaria", "Enteric Fever (Typhoid)",
            "Cholera and Severe Dehydration",
            "Retropharyngeal and Parapharyngeal Abscess"
        ],
        "Toxicology": [
            "Acute Poisoning and Toxicological Emergencies",
            "Specific Antidotes and High-Risk Poisonings",
            "Carbon Monoxide (CO) Poisoning",
            "Serotonin Syndrome (Serotonin Toxicity)",
            "Acute Opioid Toxicity",
            "Local Anesthetic Systemic Toxicity (LAST)"
        ],
        "Environmental": [
            "Heat Stroke and Hypothermia",
            "High-Altitude Pulmonary Edema (HAPE)"
        ],
        "Oncology": [
            "Tumor Lysis Syndrome"
        ],
        "Hematology": [
            "Acute Hemolytic Transfusion Reaction"
        ],
        "Ophthalmology": [
            "Acute Angle-Closure Glaucoma",
            "Central Retinal Artery Occlusion"
        ]
    }
}

MEDICAL_TOPICS = {}

# ==================== CARDIOVASCULAR EMERGENCIES ====================

MEDICAL_TOPICS[("Medical Emergencies", "Adult Cardiac Arrest")] = [
    ("01 — RECOGNIZE", "info", 
     "• Unresponsive patient with absent or abnormal breathing, including agonal gasps.\n"
     "• No definite pulse within 10 seconds in a healthcare professional assessment.\n"
     "• Pulseless electrical activity (PEA), asystole, ventricular fibrillation (VF), or pulseless ventricular tachycardia (pVT).\n"
     "• Begin CPR immediately if cardiac arrest is suspected and no definite pulse is detected."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate the resuscitation team and obtain a defibrillator.\n"
     "• Start high-quality CPR: Compression rate 100–120/min, depth 5–6 cm, allow complete recoil, minimize interruptions.\n"
     "• Change compressor approximately every 2 minutes.\n"
     "• Attach monitor/defibrillator and identify the rhythm.\n"
     "• Defibrillate immediately for VF or pVT.\n"
     "• Establish IV access; use IO access if IV access cannot be obtained promptly.\n"
     "• Provide bag-mask ventilation with oxygen; avoid excessive ventilation."),
    ("03 — RESUSCITATION ALGORITHM", "info", 
     "[color=#1E3A8A]Shockable Rhythm: VF / Pulseless VT[/color]\n"
     "• Deliver an unsynchronized shock.\n"
     "• Immediately resume CPR for 2 minutes without checking the pulse immediately after the shock.\n"
     "• Reassess rhythm every 2 minutes and shock again if VF/pVT persists.\n"
     "• Give epinephrine after initial defibrillation attempts according to the current ACLS algorithm.\n"
     "• Give amiodarone or lidocaine for refractory VF/pVT.\n\n"
     "[color=#1E3A8A]Non-Shockable Rhythm: PEA / Asystole[/color]\n"
     "• Continue high-quality CPR. Give epinephrine as soon as feasible.\n"
     "• Reassess rhythm every 2 minutes. Do not defibrillate PEA or asystole unless the rhythm changes to VF/pVT."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]High-Quality CPR[/color]\n"
     "• Compression rate: 100–120/min. Depth: 5–6 cm. Ratio: 30:2 (without advanced airway), continuous compressions with 1 breath every 6 seconds (with advanced airway).\n\n"
     "[color=#1E3A8A]Defibrillation[/color]\n"
     "• Biphasic: manufacturer's recommended energy (commonly 120–200 J). Monophasic: 360 J.\n\n"
     "[color=#1E3A8A]Epinephrine[/color]\n"
     "• 1 mg IV/IO every 3–5 minutes. Concentration: 0.1 mg/mL (10 mL contains 1 mg).\n\n"
     "[color=#1E3A8A]Amiodarone (Refractory VF/pVT)[/color]\n"
     "• First dose: 300 mg IV/IO bolus. Second dose: 150 mg IV/IO."),
    ("05 — REVERSIBLE CAUSES (Hs & Ts)", "warning", 
     "• Hypovolemia. Hypoxia. Hydrogen ion excess (acidosis). Hypokalemia/Hyperkalemia.\n"
     "• Hypothermia. Tension pneumothorax. Cardiac tamponade. Toxins. Pulmonary thrombosis. Coronary thrombosis."),
    ("06 — POST-ROSC CARE", "success", 
     "• Secure oxygenation and ventilation; avoid hypoxemia and hyperoxia (target SpO2 ~92-98%).\n"
     "• Avoid hypotension and support perfusion.\n"
     "• Obtain 12-lead ECG and evaluate for acute coronary occlusion.\n"
     "• Check glucose, blood gas, electrolytes, renal function.\n"
     "• Provide temperature control and post-arrest critical care."),
    ("07 — WARNINGS", "danger", 
     "• Do not delay compressions while obtaining equipment or IV access.\n"
     "• Do not perform prolonged pulse checks.\n"
     "• Ensure nobody is touching the patient during shock delivery.\n"
     "• Do not confuse the cardiac-arrest epinephrine concentration (0.1 mg/mL) with 1 mg/mL."),
    ("REFERENCES", "info", "AHA Adult Advanced Life Support; AHA Adult Basic Life Support.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Coronary Syndrome (ACS)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Central chest pressure, heaviness, squeezing, or pain radiating to the arm, jaw, back, or shoulder.\n"
     "• Dyspnea, diaphoresis, nausea, vomiting, or unexplained weakness.\n"
     "• Atypical presentations are common in older adults, diabetes, kidney disease.\n"
     "• STEMI may require immediate reperfusion; do not wait for troponin results when ECG and presentation establish the diagnosis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, hemodynamic stability.\n"
     "• Obtain 12-lead ECG as soon as possible (within 10 minutes).\n"
     "• Establish IV access and cardiac monitoring. Obtain high-sensitivity troponin.\n"
     "• Give aspirin unless contraindicated.\n"
     "• Activate local reperfusion pathway for STEMI.\n"
     "• Assess for alternative life-threatening diagnoses (aortic dissection, PE, tension pneumothorax)."),
    ("03 — INVESTIGATIONS", "info", 
     "• 12-lead ECG; repeat when indicated.\n"
     "• Serial high-sensitivity cardiac troponin.\n"
     "• CBC, electrolytes, renal function, glucose, coagulation.\n"
     "• Echocardiography for shock, mechanical complications, or diagnostic uncertainty.\n"
     "• Risk assessment using GRACE pathway."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Aspirin[/color]\n"
     "• 162–325 mg orally, chewed once, unless contraindicated. Subsequent maintenance 75–100 mg daily.\n\n"
     "[color=#1E3A8A]Nitroglycerin[/color]\n"
     "• 0.4 mg sublingually, repeated every 5 minutes up to 3 doses while reassessing BP.\n\n"
     "[color=#1E3A8A]Anticoagulation and P2Y12 Inhibition[/color]\n"
     "• Selection depends on STEMI vs NSTE-ACS, reperfusion strategy, bleeding risk, renal function.\n\n"
     "[color=#1E3A8A]Reperfusion for STEMI[/color]\n"
     "• Primary PCI preferred when delivered within guideline time.\n"
     "• If timely PCI unavailable, fibrinolysis may be considered according to local STEMI protocol."),
    ("05 — WARNINGS", "danger", 
     "• Avoid aspirin in true severe allergy or active major bleeding.\n"
     "• Avoid nitroglycerin with hypotension, suspected RV infarction, or recent PDE-5 inhibitor use (sildenafil/vardenafil within 24h, tadalafil within 48h).\n"
     "• Fibrinolysis is not appropriate for NSTEMI or unstable angina.\n"
     "• Do not delay primary PCI for nonessential tests."),
    ("06 — DISPOSITION", "warning", 
     "• STEMI: immediate reperfusion pathway and admission to monitored cardiac unit.\n"
     "• NSTEMI/unstable angina: risk-stratified admission and cardiology management."),
    ("REFERENCES", "info", "AHA/ACC ACS Guidelines; ESC ACS Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Heart Failure and Cardiogenic Pulmonary Edema")] = [
    ("01 — RECOGNIZE", "info", 
     "• Acute dyspnea, orthopnea, paroxysmal nocturnal dyspnea.\n"
     "• Tachypnea, hypoxemia, crackles, increased work of breathing.\n"
     "• Elevated JVP, peripheral edema, pulmonary congestion.\n"
     "• Severe: diaphoresis, exhaustion, cyanosis, altered mental status, frothy sputum.\n"
     "• Precipitants: ACS, arrhythmia, hypertensive emergency, infection, renal dysfunction, medication nonadherence, PE."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, SpO2, BP, mental status. Sit patient upright.\n"
     "• Continuous ECG and SpO2 monitoring. Give oxygen if hypoxemic.\n"
     "• Consider early noninvasive ventilation (CPAP/BiPAP) for significant distress.\n"
     "• Obtain IV access and 12-lead ECG.\n"
     "• Treat precipitating cause (ACS, arrhythmia, severe hypertension).\n"
     "• If shock/severe hypotension, avoid routine nitrates."),
    ("03 — INVESTIGATIONS", "info", 
     "• ECG and serial troponin if ACS possible. Chest X-ray.\n"
     "• BNP or NT-proBNP if diagnosis uncertain.\n"
     "• CBC, electrolytes, urea, creatinine, liver function, glucose, blood gas.\n"
     "• Bedside ultrasound/echocardiography."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Oxygen and Noninvasive Ventilation[/color]\n"
     "• Titrate oxygen to target (commonly 92–96%). CPAP/BiPAP per protocol.\n\n"
     "[color=#1E3A8A]IV Loop Diuretic — Furosemide[/color]\n"
     "• Diuretic-naive: 20–40 mg IV. Already on loop diuretics: initial IV dose often ≥ usual total daily oral dose.\n"
     "• Monitor urine output, BP, renal function, K+, Mg2+.\n\n"
     "[color=#1E3A8A]Nitroglycerin for Hypertensive Pulmonary Edema[/color]\n"
     "• IV infusion 5–10 mcg/min, titrated rapidly according to BP and symptoms."),
    ("05 — WARNINGS", "danger", 
     "• Noninvasive ventilation may be unsuitable in severe hemodynamic instability or inability to protect airway. Do not delay intubation in a deteriorating patient.\n"
     "• Avoid reflexively giving large diuretic doses without reassessment.\n"
     "• Avoid nitrates in hypotension, suspected RV infarction, recent PDE-5 inhibitor use."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for new acute heart failure, significant pulmonary edema, oxygen requirement, or IV diuretic requirement.\n"
     "• ICU/high-dependency for NIV failure, severe distress, shock, or significant arrhythmia."),
    ("REFERENCES", "info", "ESC Acute and Chronic Heart Failure Guidelines; AHA/ACC/HFSA Heart Failure Guideline.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Cardiogenic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "• Persistent hypotension (SBP < 90 mmHg) or need for vasopressors to maintain perfusion.\n"
     "• Tissue hypoperfusion: confusion, cool extremities, delayed cap refill, oliguria, elevated lactate.\n"
     "• May occur with acute MI, severe heart failure, myocarditis, acute valvular disease, or mechanical complications.\n"
     "• Pulmonary congestion may coexist with low systemic perfusion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate critical care and cardiology teams.\n"
     "• Assess ABCs, perfusion. Continuous ECG and frequent BP monitoring.\n"
     "• Obtain IV access; prepare vasoactive support.\n"
     "• Urgent ECG and bedside echocardiography.\n"
     "• Blood gas, lactate, CBC, electrolytes, renal function, troponin.\n"
     "• Avoid indiscriminate fluid loading when pulmonary congestion is present.\n"
     "• Arrange urgent coronary angiography/revascularization if ACS-related."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Norepinephrine — Vasopressor Support[/color]\n"
     "• Initial infusion: 0.05–0.1 mcg/kg/min IV, titrated to perfusion and BP (MAP target ~65 mmHg).\n"
     "• Formula: mL/hour = dose (mcg/kg/min) × weight (kg) × 60 ÷ concentration (mcg/mL).\n\n"
     "[color=#1E3A8A]Dobutamine — Low Cardiac Output[/color]\n"
     "• Starting range: 2–5 mcg/kg/min IV, titrated to cardiac output, perfusion, BP, rhythm.\n\n"
     "[color=#1E3A8A]Fluid Strategy[/color]\n"
     "• Do not give routine large fluid boluses. If preload deficiency, cautious 250 mL isotonic crystalloid challenge followed by immediate reassessment.\n\n"
     "[color=#1E3A8A]Definitive Treatment[/color]\n"
     "• ACS: urgent revascularization. Arrhythmia: rhythm-specific treatment. Tamponade: specialist intervention."),
    ("04 — WARNINGS", "danger", 
     "• Extravasation of norepinephrine may cause tissue injury; follow local guidance.\n"
     "• Do not use blood pressure alone to judge response; assess organ perfusion.\n"
     "• Dobutamine can cause tachyarrhythmias and hypotension.\n"
     "• Excess fluid can worsen pulmonary edema."),
    ("05 — DISPOSITION", "warning", 
     "• Cardiogenic shock requires ICU or cardiac intensive care admission.\n"
     "• Transfer early to a center capable of definitive cardiac intervention."),
    ("REFERENCES", "info", "AHA/ACC ACS and Cardiogenic Shock guidance; ESC ACS Guidelines; SCAI Shock Classification.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Symptomatic Bradycardia")] = [
    ("01 — RECOGNIZE", "info", 
     "• HR typically < 50/min may be clinically significant, but symptoms and perfusion determine urgency.\n"
     "• Compromise signs: Hypotension, acute altered mental status, shock, ischemic chest discomfort, acute heart failure, syncope.\n"
     "• Identify sinus bradycardia, sinus pauses, AV block, medication-related bradycardia.\n"
     "• High-grade AV block may deteriorate rapidly."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, BP. Continuous ECG and SpO2 monitoring.\n"
     "• Obtain IV access and 12-lead ECG.\n"
     "• Identify and treat reversible causes.\n"
     "• If causing cardiopulmonary compromise: give atropine and prepare for pacing.\n"
     "• Do not delay transcutaneous pacing in unstable high-grade AV block."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Atropine[/color]\n"
     "• 1 mg IV bolus, repeated every 3–5 minutes if required. Maximum total dose: 3 mg.\n\n"
     "[color=#1E3A8A]Transcutaneous Pacing[/color]\n"
     "• Apply pads, select pacing mode, increase current until electrical capture, confirm mechanical capture.\n\n"
     "[color=#1E3A8A]Epinephrine Infusion[/color]\n"
     "• ACLS infusion range: 2–10 mcg/min IV, titrated to response.\n\n"
     "[color=#1E3A8A]Dopamine Infusion[/color]\n"
     "• ACLS infusion range: 5–20 mcg/kg/min IV, titrated to response.\n\n"
     "[color=#1E3A8A]Treat Reversible Causes[/color]\n"
     "• Hypoxia, hyperkalemia, medication toxicity, acute coronary ischemia, hypothermia."),
    ("04 — WARNINGS", "danger", 
     "• Atropine may be ineffective in infranodal high-grade AV block or transplanted heart. Do not delay pacing.\n"
     "• Electrical capture does not guarantee effective mechanical perfusion.\n"
     "• Pacing may be painful; provide analgesia/sedation when condition allows."),
    ("05 — DISPOSITION", "warning", 
     "• Unstable symptomatic bradycardia requires emergency resuscitation and monitored admission.\n"
     "• High-grade AV block, recurrent syncope, or need for pacing requires urgent cardiology assessment."),
    ("REFERENCES", "info", "AHA Adult Bradycardia With a Pulse Algorithm; ESC Cardiac Pacing Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Adult Tachyarrhythmias")] = [
    ("01 — RECOGNIZE", "info", 
     "• Tachycardia with a pulse (often ≥150/min). Assess for hypotension, shock, altered mental status, ischemic chest discomfort, acute heart failure.\n"
     "• Classify rhythm:\n"
     "  - Narrow-complex regular: SVT.\n"
     "  - Narrow-complex irregular: AF or atrial flutter.\n"
     "  - Wide-complex regular: VT until proven otherwise.\n"
     "  - Wide-complex irregular: Polymorphic VT (including torsades) or AF with pre-excitation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and hemodynamic stability. Apply ECG, SpO2, BP monitoring.\n"
     "• Obtain IV access and 12-lead ECG.\n"
     "• Treat unstable tachyarrhythmia with immediate electrical therapy.\n"
     "• For stable patients, identify rhythm before choosing medication.\n"
     "• Correct reversible causes (hypoxia, electrolytes, ischemia, fever, toxicity)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Unstable Tachyarrhythmia — Synchronized Cardioversion[/color]\n"
     "• AF: 200 J biphasic. Atrial flutter: 200 J. Regular narrow-complex: 100 J. Monomorphic VT with pulse: 100 J.\n"
     "• Escalate energy if unsuccessful. Confirm synchronization markers.\n\n"
     "[color=#1E3A8A]Regular Narrow-Complex SVT — Adenosine[/color]\n"
     "• 1st dose: 6 mg rapid IV push + rapid saline flush. If unsuccessful: 12 mg rapid IV push.\n\n"
     "[color=#1E3A8A]Stable Regular Monomorphic Wide-Complex Tachycardia[/color]\n"
     "• Treat as VT. Amiodarone 150 mg IV over 10 minutes, followed by infusion if indicated.\n\n"
     "[color=#1E3A8A]Atrial Fibrillation With Rapid Ventricular Response[/color]\n"
     "• Selected stable patients: IV diltiazem 0.25 mg/kg IV over 2 minutes, followed by titrated infusion. Beta-blockers are an alternative."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay cardioversion for sedation, ECG printing, or IV access in a critically unstable patient.\n"
     "• Polymorphic VT cannot be reliably synchronized; treat with unsynchronized high-energy shock.\n"
     "• Do not use adenosine for irregular wide-complex tachycardia or polymorphic VT.\n"
     "• Avoid verapamil or diltiazem to an undifferentiated wide-complex tachycardia.\n"
     "• Avoid IV diltiazem/verapamil in significant systolic dysfunction or pre-excited AF/WPW."),
    ("05 — DISPOSITION", "warning", 
     "• Admit unstable arrhythmia, sustained VT, syncope, ischemia, heart failure, or significant structural heart disease."),
    ("REFERENCES", "info", "AHA Adult Tachyarrhythmia With a Pulse Algorithm (2025); ESC AF Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Hypertensive Emergency")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe BP elevation with acute target-organ damage. A high BP reading alone does not establish the diagnosis.\n"
     "• Hypertensive encephalopathy (confusion, seizures, visual disturbance).\n"
     "• Acute pulmonary edema/heart failure. ACS. Aortic dissection. AKI.\n"
     "• Intracranial hemorrhage/ischemic stroke. Severe pre-eclampsia/eclampsia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, neurologic status, symptoms.\n"
     "• Repeat BP using appropriate cuff, consider both arms if aortic pathology suspected.\n"
     "• Establish IV access, continuous monitoring.\n"
     "• Identify specific target-organ injury.\n"
     "• Select titratable IV agent appropriate for the condition.\n"
     "• Avoid rapid, uncontrolled BP reduction unless condition-specific protocol requires."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]General BP Reduction Strategy[/color]\n"
     "• Reduce MAP by no more than ~20–25% in first hour, then gradually toward ~160/100–110 mmHg over 2–6 hours.\n"
     "• Targets vary by diagnosis (aortic dissection, stroke, pregnancy require specific protocols).\n\n"
     "[color=#1E3A8A]Nicardipine IV[/color]\n"
     "• Starting infusion: 5 mg/hour. Increase by 2.5 mg/hour at defined intervals; usual max 15 mg/hour.\n\n"
     "[color=#1E3A8A]Labetalol IV[/color]\n"
     "• 10–20 mg IV over 1–2 minutes, followed by additional doses or titrated infusion.\n\n"
     "[color=#1E3A8A]Condition-Specific Management[/color]\n"
     "• Aortic dissection: IV beta-blockade first. Pulmonary edema: avoid beta-blockade. Stroke/ICH: specific neurocritical protocols."),
    ("04 — WARNINGS", "danger", 
     "• Excessively rapid BP reduction can cause cerebral, coronary, or renal ischemia.\n"
     "• Do not treat asymptomatic elevated BP with rapid IV reduction solely to normalize the number.\n"
     "• Avoid labetalol in severe bradycardia, heart block, cardiogenic shock, or active bronchospasm."),
    ("05 — DISPOSITION", "warning", 
     "• Admit hypertensive emergencies to ICU or high-dependency care.\n"
     "• Document target-organ injury, BP target, selected drug, titration plan."),
    ("REFERENCES", "info", "AHA Management of Elevated BP in Acute Care (2024); ACC/AHA Aortic Disease Guideline.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Aortic Dissection")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden severe chest, back, or abdominal pain (tearing/ripping).\n"
     "• Syncope, neurologic deficit, limb ischemia, abdominal organ ischemia.\n"
     "• Pulse deficit or substantial BP difference between arms.\n"
     "• New aortic regurgitation murmur, hypotension, tamponade, shock.\n"
     "• Type A involves ascending aorta; Type B does not."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as life-threatening vascular emergency. Activate cardiothoracic/vascular surgery and critical care.\n"
     "• Monitor ECG and BP; obtain IV access and arterial BP monitoring.\n"
     "• Provide analgesia. Urgent CT angiography in stable patient.\n"
     "• Begin anti-impulse therapy to reduce aortic wall stress.\n"
     "• Avoid anticoagulation/fibrinolysis for presumed ACS until dissection excluded."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Esmolol — Heart Rate Control[/color]\n"
     "• IV loading dose 500 mcg/kg over 1 minute, followed by infusion starting around 50 mcg/kg/min, titrated to response.\n"
     "• Target HR 60–80/min. Aim for systolic BP < 120 mmHg (or lowest level maintaining organ perfusion).\n\n"
     "[color=#1E3A8A]Alternative IV Beta-Blocker[/color]\n"
     "• Labetalol may be used according to institutional aortic-dissection protocol.\n\n"
     "[color=#1E3A8A]Additional Vasodilator[/color]\n"
     "• If BP remains above target after adequate HR control, add IV vasodilator (e.g., nicardipine).\n\n"
     "[color=#1E3A8A]Definitive Treatment[/color]\n"
     "• Type A: emergency cardiothoracic surgery. Complicated Type B: urgent vascular/endovascular assessment."),
    ("04 — WARNINGS", "danger", 
     "• Do not initiate vasodilator therapy before adequate heart-rate control (reflex tachycardia may increase aortic wall stress).\n"
     "• Avoid esmolol in severe bradycardia, high-grade AV block, cardiogenic shock."),
    ("05 — DISPOSITION", "warning", 
     "• Admit all suspected/confirmed acute aortic dissection to critical care.\n"
     "• Transfer immediately to center with aortic intervention capability if needed."),
    ("REFERENCES", "info", "ACC/AHA Aortic Disease Guideline; ACC Acute Aortic Syndrome Guidance.")
]

# ==================== RESPIRATORY EMERGENCIES ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Pulmonary Embolism (PE)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden dyspnea, pleuritic chest pain, tachycardia, unexplained hypoxemia.\n"
     "• Syncope, hypotension, shock, or cardiac arrest (high-risk PE).\n"
     "• Hemoptysis may occur but is not required.\n"
     "• Risk factors: recent surgery, immobilization, previous VTE, active cancer, pregnancy/postpartum, estrogen, thrombophilia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, oxygenation, hemodynamic stability. Give oxygen for hypoxemia.\n"
     "• Obtain ECG (cannot exclude PE). Use validated clinical probability pathway (Wells).\n"
     "• Stable: arrange D-dimer or imaging according to pretest probability.\n"
     "• Unstable: bedside echo and urgent specialist decisions if CT unsafe.\n"
     "• Begin anticoagulation when PE is sufficiently likely and bleeding risk acceptable."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Anticoagulation — Enoxaparin[/color]\n"
     "• 1 mg/kg subcutaneously every 12 hours (adjust for renal impairment).\n\n"
     "[color=#1E3A8A]Unfractionated Heparin[/color]\n"
     "• IV bolus followed by weight-based infusion per institutional nomogram. Preferred if rapid titration/reversal or urgent procedures anticipated.\n\n"
     "[color=#1E3A8A]Systemic Thrombolysis for High-Risk PE[/color]\n"
     "• Persistent hypotension or cardiopulmonary failure with acceptable bleeding risk.\n"
     "• Alteplase 100 mg IV over 2 hours (subject to protocol).\n\n"
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Oxygen, cautious fluids (excessive worsens RV failure), vasopressors if shock."),
    ("04 — WARNINGS", "danger", 
     "• Check for active bleeding, recent major surgery, severe thrombocytopenia, history of HIT.\n"
     "• Review thrombolysis contraindications carefully (previous ICH, active major bleeding, recent major surgery).\n"
     "• Do not use an unverified heparin infusion rate."),
    ("05 — DISPOSITION", "warning", 
     "• Shock, persistent hypotension, severe hypoxemia, or RV failure requires ICU-level care.\n"
     "• RV dysfunction, elevated biomarkers, or increased severity require admission and close observation."),
    ("REFERENCES", "info", "AHA/ACC 2026 PE Guideline; ESC PE Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Severe Asthma")] = [
    ("01 — RECOGNIZE", "info", 
     "• Severe dyspnea, wheeze, chest tightness, cough.\n"
     "• Inability to speak full sentences, accessory muscle use, tachypnea, tachycardia.\n"
     "• PEF markedly reduced from predicted/personal best.\n"
     "• Life-threatening: exhaustion, confusion, cyanosis, silent chest, poor respiratory effort, hypotension, normal/rising PaCO2."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, SpO2. Give controlled oxygen (target 93–95%).\n"
     "• Start repeated inhaled SABA therapy promptly. Add inhaled ipratropium for severe.\n"
     "• Give systemic corticosteroids early.\n"
     "• Reassess work of breathing, speech, oxygenation, PEF.\n"
     "• Consider IV magnesium sulfate for selected severe cases.\n"
     "• Call ICU/anesthesia early for exhaustion, altered consciousness, silent chest, or poor response."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Salbutamol (Albuterol)[/color]\n"
     "• Nebulized: 2.5–5 mg repeated every 20 minutes during first hour, then titrated.\n"
     "• MDI with spacer: 4–10 puffs every 20 minutes during first hour.\n\n"
     "[color=#1E3A8A]Ipratropium Bromide[/color]\n"
     "• 0.5 mg nebulized every 20 minutes for first 3 doses alongside salbutamol.\n\n"
     "[color=#1E3A8A]Systemic Corticosteroid[/color]\n"
     "• Prednisolone 40–50 mg orally once daily for 5–7 days. IV corticosteroid if oral not possible.\n\n"
     "[color=#1E3A8A]IV Magnesium Sulfate[/color]\n"
     "• 2 g IV over ~20 minutes when severe symptoms persist despite initial intensive therapy."),
    ("04 — WARNINGS", "danger", 
     "• Tachycardia, tremor, hypokalemia, lactic acidosis can occur with intensive SABA.\n"
     "• Worsening fatigue or reduced air entry is not reassuring even if wheeze becomes quieter.\n"
     "• Noninvasive ventilation is not a substitute for timely intubation in a tiring/confused patient."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for persistent severe symptoms, poor response, hypoxemia, or life-threatening features.\n"
     "• ICU for respiratory failure, altered consciousness, or need for ventilatory support."),
    ("REFERENCES", "info", "GINA 2025 Strategy Report; AHA Adult Emergency Cardiovascular Care Guidelines.")
]


# ==================== BATCH 3 & 4 (TOPICS 11-20) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Exacerbation of COPD")] = [
    ("01 — RECOGNIZE", "info", 
     "• Acute worsening of dyspnea, cough, sputum volume, or sputum purulence.\n"
     "• Increased respiratory rate and work of breathing. Wheezing, reduced air entry.\n"
     "• Hypoxemia; severe cases may present with confusion, exhaustion, cyanosis.\n"
     "• Hypercapnia and respiratory acidosis may develop.\n"
     "• Consider alternative/additional diagnoses: pneumonia, PE, pneumothorax, acute heart failure, ACS."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, respiratory effort. Position upright.\n"
     "• Give controlled oxygen, generally targeting SpO2 88–92% while assessing blood gases.\n"
     "• Start inhaled SABA. Add ipratropium for significant exacerbations.\n"
     "• Administer systemic corticosteroids early.\n"
     "• Obtain blood gas in severe illness or suspected hypercapnia.\n"
     "• Consider antibiotics if bacterial infection likely (increased sputum purulence/volume).\n"
     "• Consider NIV for persistent hypercapnic respiratory acidosis despite initial therapy."),
    ("03 — INVESTIGATIONS", "info", 
     "• Pulse oximetry and repeated respiratory assessment. Arterial or venous blood gas.\n"
     "• Chest X-ray to assess pneumonia, pneumothorax, edema.\n"
     "• ECG and troponin if ischemia or arrhythmia suspected.\n"
     "• CBC, electrolytes, urea, creatinine, glucose. Sputum culture in selected cases."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Salbutamol[/color]\n"
     "• Nebulized: 2.5–5 mg, repeated every 20 minutes during first hour, then titrate.\n\n"
     "[color=#1E3A8A]Ipratropium[/color]\n"
     "• 0.5 mg nebulized, repeated according to local protocol.\n\n"
     "[color=#1E3A8A]Systemic Corticosteroid[/color]\n"
     "• Prednisolone 40 mg orally once daily for 5 days. IV if oral not possible.\n\n"
     "[color=#1E3A8A]Antibiotics (If Indicated)[/color]\n"
     "• Increased sputum purulence with volume/dyspnea. Common option: Doxycycline 200 mg day 1, then 100 mg daily. Amoxicillin/clavulanate alternative.\n\n"
     "[color=#1E3A8A]Noninvasive Ventilation (NIV)[/color]\n"
     "• Persistent hypercapnic respiratory acidosis (pH ≤7.35 with elevated PaCO2) despite initial treatment."),
    ("05 — WARNINGS", "danger", 
     "• Worsening exhaustion or decreasing air entry may indicate respiratory failure rather than improvement.\n"
     "• Reassess if symptoms persist; corticosteroids do not replace bronchodilation, antibiotics, or ventilatory support.\n"
     "• NIV must not delay intubation when respiratory failure is worsening."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for persistent hypoxemia, hypercapnia/acidosis, poor response, or need for NIV.\n"
     "• ICU assessment for deteriorating consciousness, severe acidosis, shock, or NIV failure."),
    ("REFERENCES", "info", "GOLD 2026 Report; British Thoracic Society Emergency Oxygen Guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Respiratory Failure")] = [
    ("01 — RECOGNIZE", "info", 
     "• Hypoxemic Respiratory Failure: Significant hypoxemia despite room air/supplemental oxygen. (Pneumonia, edema, ARDS, PE, asthma).\n"
     "• Hypercapnic Respiratory Failure: Elevated PaCO2 with respiratory acidosis. (COPD, severe asthma with fatigue, neuromuscular weakness, opioid toxicity).\n"
     "• Danger Signs: Exhaustion, confusion, reduced consciousness, cyanosis, weak respiratory effort, silent chest, hemodynamic instability."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for senior emergency, respiratory, and critical care support.\n"
     "• Assess airway, respiratory effort, circulation, mental status. Clear secretions.\n"
     "• Administer oxygen and titrate to appropriate target.\n"
     "• Use high-flow nasal oxygen (HFNO) or NIV in selected patients.\n"
     "• Prepare for intubation if airway protection, oxygenation, or ventilation is failing.\n"
     "• Treat the underlying cause without delay."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Oxygen Therapy[/color]\n"
     "• Most acutely ill adults: target SpO2 94–98%.\n"
     "• At risk of hypercapnic respiratory failure (e.g., COPD): target SpO2 88–92% pending blood gas results.\n\n"
     "[color=#1E3A8A]High-Flow Nasal Oxygen (HFNO)[/color]\n"
     "• Flow and FiO2 titrated according to distress, oxygenation, tolerance. Flows up to ~60 L/min.\n\n"
     "[color=#1E3A8A]Noninvasive Ventilation[/color]\n"
     "• Particularly useful for COPD-related hypercapnic acidosis and acute cardiogenic pulmonary edema.\n\n"
     "[color=#1E3A8A]Endotracheal Intubation and Invasive Ventilation[/color]\n"
     "• Inability to protect airway, refractory hypoxemia/hypercapnia, severe exhaustion, apnea, or impending arrest.\n"
     "• Use lung-protective ventilation when indicated (especially ARDS)."),
    ("04 — WARNINGS", "danger", 
     "• Do not withhold oxygen from a severely hypoxemic patient because of concern about CO2 retention; provide controlled oxygen and monitor.\n"
     "• Avoid unnecessary hyperoxia.\n"
     "• Do not allow a trial of HFNO/NIV to delay intubation in a deteriorating patient.\n"
     "• Intubation can precipitate hypotension or cardiac arrest in critically ill patients."),
    ("05 — DISPOSITION", "warning", 
     "• Acute respiratory failure generally requires hospital admission.\n"
     "• ICU admission for invasive ventilation, worsening gas exchange, shock, severe acidosis, or rapidly deteriorating mental status."),
    ("REFERENCES", "info", "British Thoracic Society; GOLD 2026; ARDS Network.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Pneumothorax and Tension Pneumothorax")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Pneumothorax[/color]\n"
     "• Sudden pleuritic chest pain and dyspnea. Reduced breath sounds and chest expansion. Hyperresonance.\n\n"
     "[color=#1E3A8A]Tension Pneumothorax[/color]\n"
     "• Severe respiratory distress, rapidly worsening hypoxemia.\n"
     "• Hypotension, tachycardia, obstructive shock, peri-arrest.\n"
     "• Positive-pressure ventilation may precipitate or worsen tension."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, hemodynamic stability. Provide oxygen.\n"
     "• If tension pneumothorax is strongly suspected in an unstable patient, decompress immediately without waiting for imaging.\n"
     "• Prepare for definitive pleural drainage after emergency decompression.\n"
     "• In a stable patient, confirm diagnosis with lung ultrasound or chest imaging."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Emergency Decompression for Tension[/color]\n"
     "• Needle/catheter decompression at an approved site (e.g., 2nd ICS mid-clavicular or 5th ICS anterior axillary) or finger thoracostomy in trained hands.\n\n"
     "[color=#1E3A8A]Chest Drainage[/color]\n"
     "• Persistent/large pneumothorax, secondary spontaneous, traumatic, or associated with mechanical ventilation.\n"
     "• Confirm drain function, monitor for persistent air leak, bleeding, infection.\n\n"
     "[color=#1E3A8A]Stable Primary Spontaneous Pneumothorax[/color]\n"
     "• Conservative management, needle aspiration, or ambulatory management in selected minimally symptomatic patients."),
    ("04 — WARNINGS", "danger", 
     "• Needle decompression may fail due to inadequate catheter length, kinking, or incorrect placement.\n"
     "• Do not clamp a bubbling chest drain routinely unless directed by a specific specialist protocol.\n"
     "• A small pneumothorax can be clinically important in a patient with underlying lung disease.\n"
     "• Tension physiology is a clinical emergency and must not be managed by observation alone."),
    ("05 — DISPOSITION", "warning", 
     "• Tension pneumothorax requires immediate decompression and hospital-level care.\n"
     "• Admit for significant symptoms, secondary pneumothorax, trauma, persistent air leak, or need for drainage."),
    ("REFERENCES", "info", "British Thoracic Society Pleural Disease Guideline.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Anaphylaxis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden onset of airway, breathing, or circulatory compromise after allergen exposure.\n"
     "• Urticaria, flushing, angioedema (may be absent).\n"
     "• Wheeze, stridor, throat tightness, hoarseness, difficulty swallowing.\n"
     "• Hypotension, collapse, syncope, shock. GI symptoms (cramps/vomiting).\n"
     "• Triggers: foods, medications, insect stings, latex.\n"
     "• [color=#991B1B]Do not delay epinephrine while waiting for rash or tests.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for emergency resuscitation support. Stop exposure.\n"
     "• Lay flat with legs elevated (position of comfort if severe respiratory distress). Do not allow standing/walking suddenly.\n"
     "• Give IM epinephrine immediately.\n"
     "• Provide oxygen, monitoring, IV access. Give isotonic crystalloid for hypotension/shock.\n"
     "• Prepare for early airway intervention if progressive edema.\n"
     "• Repeat IM epinephrine if symptoms persist (every 5–15 minutes)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Epinephrine (Adrenaline) — First-Line[/color]\n"
     "• 0.5 mg IM for an adult using 1 mg/mL solution (0.5 mL). Inject mid-anterolateral thigh.\n\n"
     "[color=#1E3A8A]IV Crystalloid[/color]\n"
     "• Initial 500–1,000 mL isotonic crystalloid bolus for significant hypotension, reassess and repeat.\n\n"
     "[color=#1E3A8A]Bronchodilator[/color]\n"
     "• Nebulized salbutamol 2.5–5 mg for persistent wheeze (adjunct after epinephrine).\n\n"
     "[color=#1E3A8A]Adjuncts[/color]\n"
     "• Antihistamines: Only for persistent skin symptoms after stabilization.\n"
     "• Corticosteroids: Not routine first-line; delayed onset; do not delay epinephrine."),
    ("04 — WARNINGS", "danger", 
     "• Do not use IV epinephrine bolus as routine initial treatment for anaphylaxis.\n"
     "• Salbutamol does not treat upper-airway edema or shock and must never replace epinephrine.\n"
     "• Antihistamines do not treat airway obstruction or hypotension."),
    ("05 — DISPOSITION", "warning", 
     "• Observe after stabilization according to severity and risk of biphasic reaction.\n"
     "• Admit for severe reactions, recurrent symptoms, airway involvement, or need for repeated epinephrine.\n"
     "• Provide epinephrine auto-injector, action plan, and allergy follow-up."),
    ("REFERENCES", "info", "World Allergy Organization; AAAAI/ACAAI; Resuscitation Council UK.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Hypoglycemia and Hyperglycemic Crises")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Hypoglycemia[/color]\n"
     "• < 70 mg/dL (3.9 mmol/L) alert threshold; < 54 mg/dL (3.0 mmol/L) clinically significant.\n"
     "• Severe = need for assistance due to altered mental/physical status.\n"
     "• Sweating, tremor, palpitations, confusion, seizures, coma.\n\n"
     "[color=#1E3A8A]DKA / HHS[/color]\n"
     "• DKA: Hyperglycemia, ketosis, metabolic acidosis. May occur with normal-ish glucose (SGLT2i, pregnancy).\n"
     "• HHS: Severe hyperglycemia, hyperosmolality, dehydration, minimal ketosis/acidosis.\n"
     "• Mixed presentations occur."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, hydration, bedside glucose. Obtain IV access and ECG.\n"
     "• If hypoglycemic, treat immediately (do not wait for lab).\n"
     "• If DKA/HHS, obtain electrolytes, VBG, ketones, renal function, osmolality.\n"
     "• Identify precipitant: infection, missed insulin, MI, stroke, pancreatitis, new-onset diabetes.\n"
     "• Monitored area for DKA/HHS with frequent glucose, K+, fluid, and neuro reassessment."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Hypoglycemia (Cannot Swallow)[/color]\n"
     "• IV glucose 10–25 g (e.g., 100 mL of 10% dextrose). Recheck in 10–15 mins. Glucagon 1 mg IM if no IV.\n\n"
     "[color=#1E3A8A]Initial Fluids for DKA/HHS[/color]\n"
     "• Isotonic saline/balanced crystalloid at 500–1,000 mL/hour for first 2–4 hours (adjust for heart/kidney).\n\n"
     "[color=#1E3A8A]IV Insulin for DKA[/color]\n"
     "• Regular insulin IV infusion at 0.1 units/kg/hour.\n"
     "• Do not start if K+ < 3.5 mmol/L; replace K+ first.\n"
     "• Add dextrose when glucose < ~250 mg/dL to allow ketone clearance.\n\n"
     "[color=#1E3A8A]IV Insulin for HHS[/color]\n"
     "• Regular insulin IV at 0.05 units/kg/hour (if no significant ketosis).\n\n"
     "[color=#1E3A8A]Potassium Replacement[/color]\n"
     "• If K+ < 3.5, start replacement and defer insulin.\n"
     "• If 3.5–5.0, add K+ to IV fluids.\n"
     "• If > 5.0, withhold initially.\n\n"
     "[color=#1E3A8A]Bicarbonate[/color]\n"
     "• Not routinely recommended. Consider only if pH < 7.0 under specialist protocol."),
    ("04 — WARNINGS", "danger", 
     "• Sulfonylurea-related hypoglycemia may recur and require prolonged observation.\n"
     "• Avoid rapid uncontrolled correction of hyperosmolality (especially HHS).\n"
     "• Insulin can rapidly lower potassium and precipitate life-threatening arrhythmias.\n"
     "• Do not stop insulin solely because glucose normalized if ketoacidosis persists."),
    ("05 — DISPOSITION", "warning", 
     "• Severe DKA, HHS, shock, altered mental status, severe electrolyte abnormalities require ICU/high-dependency care.\n"
     "• Establish cause, treatment plan, sick-day rules, and follow-up before discharge."),
    ("REFERENCES", "info", "Umpierrez GE, et al. Diabetes Care 2024; Local DKA/HHS protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Ischemic Stroke")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden focal neurologic deficit: Facial droop, arm/leg weakness, speech disturbance, visual loss, ataxia, neglect.\n"
     "• Posterior circulation: vertigo, diplopia, dysarthria, ataxia, reduced consciousness.\n"
     "• Establish exact last-known-well time.\n"
     "• Consider mimics: hypoglycemia, seizure, migraine.\n"
     "• Time-sensitive reperfusion assessment is essential."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate stroke pathway immediately. Record last-known-well time.\n"
     "• Assess ABCs, glucose, oxygenation, neurologic deficit.\n"
     "• Establish IV access and obtain ECG without delaying brain imaging.\n"
     "• Obtain urgent non-contrast CT brain to exclude hemorrhage. Add CTA when LVO suspected.\n"
     "• Assess eligibility for IV thrombolysis and endovascular thrombectomy.\n"
     "• Keep patient NPO until swallowing safety assessed.\n"
     "• Avoid unnecessary delays from routine tests."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Thrombolysis — Tenecteplase[/color]\n"
     "• 0.25 mg/kg IV single bolus (max 25 mg) for eligible adults.\n\n"
     "[color=#1E3A8A]IV Thrombolysis — Alteplase[/color]\n"
     "• 0.9 mg/kg IV (max 90 mg). 10% as initial bolus over 1 min, remaining 90% over 60 mins.\n\n"
     "[color=#1E3A8A]Blood Pressure Management[/color]\n"
     "• Before thrombolysis: BP < 185/110 mmHg.\n"
     "• After thrombolysis: maintain < 180/105 mmHg for first 24 hours.\n"
     "• Use titratable IV antihypertensive (labetalol/nicardipine).\n\n"
     "[color=#1E3A8A]Endovascular Thrombectomy[/color]\n"
     "• Eligible patients with confirmed LVO, within 6 hours or up to 24 hours based on imaging criteria.\n\n"
     "[color=#1E3A8A]Antiplatelet[/color]\n"
     "• Aspirin within 24–48 hours after hemorrhage excluded (not treated with thrombolysis).\n"
     "• After thrombolysis: wait 24 hours and obtain follow-up imaging before starting."),
    ("04 — WARNINGS", "danger", 
     "• Only administer thrombolysis after hemorrhage excluded and eligibility confirmed.\n"
     "• Do not give routine antiplatelets/anticoagulants during first 24 hours after IV thrombolysis.\n"
     "• Do not delay eligible thrombolysis for nonessential advanced imaging.\n"
     "• Do not use a single BP target for every stroke patient."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to stroke unit or monitored setting.\n"
     "• ICU for airway compromise, severe deficits, malignant edema, hemorrhagic transformation, or instability."),
    ("REFERENCES", "info", "AHA/ASA 2026 Acute Ischemic Stroke Guideline; NICE NG128.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Spontaneous Intracerebral Hemorrhage (ICH)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden focal neurological deficit, severe headache, vomiting, reduced consciousness, or seizure.\n"
     "• Risk factors: chronic hypertension, anticoagulant use, cerebral amyloid angiopathy, vascular malformations, coagulopathy.\n"
     "• Consider raised ICP: declining consciousness, pupillary asymmetry, abnormal posturing."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate stroke/emergency response and document exact last-known-well time.\n"
     "• Assess ABCs, GCS, pupils, capillary glucose.\n"
     "• Provide oxygen if hypoxemic; avoid hypoxemia and hypotension.\n"
     "• Establish IV access, cardiac monitoring, frequent neuro observations.\n"
     "• Obtain urgent non-contrast CT brain. Add CTA when indicated.\n"
     "• Stop anticoagulants/antiplatelet agents initially.\n"
     "• Contact stroke, neurosurgical, and critical-care services early."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Blood Pressure Control[/color]\n"
     "• Mild-to-moderate spontaneous ICH with SBP 150–220: target SBP ~140 mmHg (range 130–150).\n"
     "• Nicardipine: Start 5 mg/hour, increase by 2.5 mg/hour every 5-15 mins (max 15 mg/hour).\n\n"
     "[color=#1E3A8A]Reversal of Anticoagulation[/color]\n"
     "• Warfarin: 4F-PCC (dose per INR) + Vitamin K 10 mg IV slowly.\n"
     "• Dabigatran: Idarucizumab 5 g IV.\n"
     "• Factor Xa inhibitor: Andexanet alfa or 4F-PCC per protocol.\n"
     "• Heparin: Protamine per type/dose/timing.\n\n"
     "[color=#1E3A8A]Raised ICP / Herniation[/color]\n"
     "• Hypertonic saline or mannitol (e.g., 0.5–1 g/kg IV) under neurocritical care protocol.\n"
     "• Elevate head ~30 degrees if tolerated. Maintain neutral neck."),
    ("04 — WARNINGS", "danger", 
     "• Avoid abrupt BP reduction and hypotension. Do not target SBP below 130 routinely.\n"
     "• Avoid routine corticosteroids for ICH-related edema.\n"
     "• Avoid prophylactic platelet transfusion for antiplatelet-associated ICH unless specific indication (e.g., emergency neurosurgery)."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to stroke unit, neurocritical care, or ICU depending on severity.\n"
     "• Urgent neurosurgical review for cerebellar hemorrhage with deterioration, hydrocephalus, or significant mass effect."),
    ("REFERENCES", "info", "AHA/ASA 2022 Spontaneous ICH Guideline; Local reversal protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Convulsive Status Epilepticus")] = [
    ("01 — RECOGNIZE", "info", 
     "• Continuous convulsive seizure ≥ 5 minutes.\n"
     "• Recurrent seizures without recovery of consciousness between episodes.\n"
     "• Causes: missed meds, hypoglycemia, electrolytes, stroke, CNS infection, toxic, alcohol withdrawal, eclampsia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for emergency assistance, record onset.\n"
     "• Protect from injury, position safely, suction, provide oxygen.\n"
     "• Assess airway/breathing, check bedside glucose, establish IV access.\n"
     "• Give benzodiazepine promptly at 5 minutes.\n"
     "• If seizures continue after 2 benzodiazepine doses, proceed to second-line."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]First-line: Lorazepam IV[/color]\n"
     "• 0.1 mg/kg IV (max 4 mg). May repeat once after 3–5 mins.\n\n"
     "[color=#1E3A8A]Alternative (No IV): Midazolam[/color]\n"
     "• IM midazolam 10 mg (for >40 kg) per protocol.\n\n"
     "[color=#1E3A8A]Second-line: Levetiracetam[/color]\n"
     "• 60 mg/kg IV (max 4,500 mg) over 10–15 mins.\n\n"
     "[color=#1E3A8A]Alternatives[/color]\n"
     "• Fosphenytoin/phenytoin (20 mg/kg IV max 50 mg/min, monitor ECG/BP) or sodium valproate.\n\n"
     "[color=#1E3A8A]Refractory[/color]\n"
     "• Continuous anesthetic infusions (midazolam/propofol) in ICU. Secure airway. Continuous EEG."),
    ("04 — WARNINGS", "danger", 
     "• Benzodiazepines can cause respiratory depression/hypotension. Have airway equipment ready.\n"
     "• Do not delay treatment while waiting for IV access (use IM/buccal/intranasal).\n"
     "• A loading dose is not the same as a maintenance dose (e.g., levetiracetam)."),
    ("05 — DISPOSITION", "warning", 
     "• ICU for refractory seizures, respiratory compromise, or persistent depressed consciousness.\n"
     "• Admit for first seizure, persistent deficit, suspected CNS infection, or significant metabolic abnormalities."),
    ("REFERENCES", "info", "NICE NG217 (2025); Local status epilepticus protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Altered Mental Status")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute confusion, delirium, agitation, drowsiness, stupor, or coma.\n"
     "• Reversible/life-threatening causes: Hypoglycemia, hypoxia, hypercapnia, shock, sepsis, stroke, ICH, seizure, CNS infection, drug toxicity, opioid overdose, alcohol withdrawal, electrolyte disturbances, renal/hepatic failure, endocrine emergencies, trauma, temperature extremes."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE. Check capillary glucose immediately.\n"
     "• Assess SpO2, temp, BP, pulse, RR, GCS, pupils.\n"
     "• Treat hypoxia, hypoglycemia, shock, seizures immediately.\n"
     "• Obtain collateral history.\n"
     "• Consider C-spine protection if trauma possible."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Hypoglycemia[/color]\n"
     "• Unable to swallow: IV dextrose (10–25 g). E.g., 100 mL of 10% dextrose. Glucagon 1 mg IM if no IV.\n\n"
     "[color=#1E3A8A]Suspected Opioid Toxicity[/color]\n"
     "• Naloxone 0.04–0.1 mg IV (titrate carefully). 0.4–2 mg IV/IM for severe respiratory compromise.\n"
     "• Goal is adequate ventilation, not complete wakefulness. Repeat every 2–3 mins.\n\n"
     "[color=#1E3A8A]Suspected Wernicke Encephalopathy[/color]\n"
     "• Thiamine 200–500 mg IV three times daily (give before/with glucose).\n\n"
     "[color=#1E3A8A]Suspected Sepsis/CNS Infection[/color]\n"
     "• Cultures, empiric antibiotics promptly.\n\n"
     "[color=#1E3A8A]Agitation/Delirium[/color]\n"
     "• Treat underlying cause, pain, urinary retention. Verbal de-escalation. Avoid routine sedation that obscures reassessment."),
    ("04 — WARNINGS", "danger", 
     "• Do not give oral fluids/food to a patient with impaired consciousness.\n"
     "• Naloxone may precipitate acute withdrawal, agitation, vomiting. Duration may be shorter than opioid.\n"
     "• Do not delay life-saving glucose in hypoglycemia while waiting for thiamine."),
    ("05 — DISPOSITION", "warning", 
     "• Admit/transfer for unexplained, persistent, recurrent altered mental status or serious underlying cause.\n"
     "• ICU for airway compromise, severe coma, shock, or need for organ support."),
    ("REFERENCES", "info", "NICE guidance on delirium; Local emergency protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Meningitis and Encephalitis")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Meningitis[/color]\n"
     "• Fever, headache, neck stiffness, photophobia, vomiting, altered mental status.\n"
     "• Petechial/purpuric rash may suggest meningococcal infection.\n\n"
     "[color=#1E3A8A]Encephalitis[/color]\n"
     "• Altered behavior/consciousness, fever, seizures, focal deficits, memory disturbance. HSV encephalitis suspicion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as medical emergency. Assess ABCs, GCS, bedside glucose.\n"
     "• Droplet precautions for suspected meningococcal disease.\n"
     "• Obtain blood cultures promptly if no delay.\n"
     "• Start empiric IV antibiotics immediately for bacterial meningitis.\n"
     "• Give empiric IV acyclovir if encephalitis (especially HSV) suspected.\n"
     "• Do not delay treatment for CT or LP when they cause significant delay."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric Antibiotics (Bacterial Meningitis)[/color]\n"
     "• Ceftriaxone 2 g IV every 12 hours.\n"
     "• Add Vancomycin (if resistant pneumococcus concern).\n"
     "• Add Ampicillin 2 g IV every 4 hours (if Listeria coverage needed: >50y, pregnancy, immunocompromised).\n\n"
     "[color=#1E3A8A]Dexamethasone[/color]\n"
     "• 10 mg IV every 6 hours for up to 4 days. Give before/with first antibiotic dose if pneumococcal suspected.\n\n"
     "[color=#1E3A8A]Suspected HSV Encephalitis: Acyclovir[/color]\n"
     "• 10 mg/kg IV every 8 hours (adjust for renal function). Infuse slowly; ensure hydration.\n\n"
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Treat seizures. Maintain oxygenation. Manage ICP with specialist guidance. Isolation/public-health notification."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay antibiotics to administer dexamethasone.\n"
     "• Acyclovir can cause crystal-associated kidney injury (dehydration, rapid infusion, renal impairment).\n"
     "• Severe beta-lactam allergy requires an individualized alternative regimen."),
    ("05 — DISPOSITION", "warning", 
     "• Admit urgently; ICU for shock, severe encephalopathy, airway compromise, recurrent seizures, or raised ICP."),
    ("REFERENCES", "info", "WHO Guidelines on Meningitis (2025, 2026); Local protocols.")
]


# ==================== BATCH 5 & 6 (TOPICS 21-30) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Kidney Injury (AKI) and Uremic Emergencies")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute kidney injury is an abrupt decline in kidney function.\n\n"
     "[color=#1E3A8A]KDIGO diagnostic criteria (any one):[/color]\n"
     "• Increase in serum creatinine by at least 0.3 mg/dL within 48 hours.\n"
     "• Increase in serum creatinine to at least 1.5 times baseline within 7 days.\n"
     "• Urine output below 0.5 mL/kg/hour for at least 6 hours.\n\n"
     "[color=#1E3A8A]Dangerous complications:[/color] Hyperkalemia, pulmonary edema, severe metabolic acidosis, uremic encephalopathy/pericarditis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, BP, perfusion, oxygen saturation, and volume status.\n"
     "• Measure urine output; insert catheter if clinically indicated.\n"
     "• Obtain urgent electrolytes, urea, creatinine, bicarbonate, glucose, and ECG.\n"
     "• Stop or review nephrotoxic drugs and medications.\n"
     "• Treat shock, sepsis, dehydration, obstruction, or other reversible causes.\n"
     "• Contact nephrology early for severe AKI or dialysis indications."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fluid resuscitation for hypovolemia[/color]\n"
     "• Isotonic crystalloid bolus (commonly 250–500 mL in adults), then reassess.\n"
     "• Do not give repeated fluid boluses to a patient who is already fluid overloaded. Oliguria alone does not prove that more fluid is needed.\n\n"
     "[color=#1E3A8A]B. Medication review[/color]\n"
     "• Stop NSAIDs. Review ACE inhibitors, ARBs, diuretics, aminoglycosides, contrast exposure. Adjust doses of renally cleared medications.\n\n"
     "[color=#1E3A8A]C. Urinary obstruction[/color]\n"
     "• Check for catheter blockage. Bladder catheterization for acute retention.\n"
     "• Urgent urological assessment for upper urinary tract obstruction (especially with infection, solitary kidney, or worsening renal function).\n\n"
     "[color=#1E3A8A]D. Dialysis and renal replacement therapy[/color]\n"
     "• Urgent indications: Refractory hyperkalemia, severe metabolic acidosis, pulmonary edema/fluid overload, uremic complications (encephalopathy/pericarditis), selected dialyzable poisonings."),
    ("04 — WARNINGS", "danger", 
     "• Do not give repeated fluid boluses to a patient who is already fluid overloaded.\n"
     "• Infected obstructed urinary systems require urgent drainage and antimicrobial treatment.\n"
     "• Do not initiate or defer dialysis based on a single creatinine or urea value alone."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for severe AKI, significant electrolyte/acid-base abnormalities, oliguria/anuria, suspected obstruction, sepsis, or uncertain cause.\n"
     "• ICU/high-dependency for shock, refractory hyperkalemia, pulmonary edema, or multiorgan failure."),
    ("REFERENCES", "info", "KDIGO Clinical Practice Guideline for Acute Kidney Injury; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Severe Hyperkalemia and Life-Threatening Electrolyte Disorders")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Hyperkalemia[/color]\n"
     "• Mild: 5.5–5.9 mmol/L. Moderate: 6.0–6.4 mmol/L. Severe: ≥ 6.5 mmol/L.\n"
     "• ECG changes: Tall peaked T waves, PR prolongation, flattened/absent P waves, QRS widening, bradyarrhythmia, sine-wave pattern.\n\n"
     "[color=#1E3A8A]Other emergencies:[/color] Severe symptomatic hyponatremia, severe hypernatremia, symptomatic hypocalcemia, severe hypomagnesemia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain urgent 12-lead ECG and continuous cardiac monitoring.\n"
     "• Establish IV access. Review renal function, medications, urine output.\n"
     "• Stop potassium supplements and contributing drugs.\n"
     "• For severe symptomatic sodium or calcium disorders, avoid rapid unmonitored correction."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Stabilize myocardium: IV Calcium[/color]\n"
     "• Calcium gluconate 10%: 30 mL IV over ~10 mins (or Calcium chloride 10%: 10 mL IV via central access).\n\n"
     "[color=#1E3A8A]B. Shift potassium: Insulin/Glucose[/color]\n"
     "• Regular insulin 10 units IV with 25 g glucose. Monitor glucose for at least 4–6 hours (delayed hypoglycemia risk).\n\n"
     "[color=#1E3A8A]C. Nebulized Salbutamol[/color]\n"
     "• 10–20 mg nebulized as an adjunct.\n\n"
     "[color=#1E3A8A]D. Remove potassium[/color]\n"
     "• Potassium-binding agents (e.g., sodium zirconium cyclosilicate). Loop diuretics (if renal function/urine output adequate). Hemodialysis for refractory/life-threatening cases.\n\n"
     "[color=#1E3A8A]E. Severe symptomatic hyponatremia[/color]\n"
     "• 3% hypertonic saline: 100 mL IV over 10 mins, repeated up to two additional times if severe symptoms persist. Goal is small initial sodium rise to reduce cerebral edema.\n\n"
     "[color=#1E3A8A]F. Severe hypernatremia[/color]\n"
     "• Restore circulation first if in shock. Then replace free water (oral/enteral or IV hypotonic fluid). Controlled correction to reduce cerebral edema risk.\n\n"
     "[color=#1E3A8A]G. Symptomatic hypocalcemia[/color]\n"
     "• Calcium gluconate 10%: 10–20 mL IV over ~10 mins."),
    ("04 — WARNINGS", "danger", 
     "• Calcium stabilizes the cardiac membrane but does not lower serum potassium.\n"
     "• Do not confuse calcium gluconate with calcium chloride (not equivalent volume-for-volume).\n"
     "• Insulin shifts potassium temporarily; it does not remove potassium from the body.\n"
     "• Avoid overly rapid correction of sodium (osmotic demyelination risk)."),
    ("05 — DISPOSITION", "warning", 
     "• Severe hyperkalemia, ECG abnormalities, severe symptomatic sodium disturbance, or significant arrhythmia requires urgent monitored care.\n"
     "• ICU and urgent nephrology referral for refractory electrolyte abnormalities."),
    ("REFERENCES", "info", "UK Kidney Association Guidelines; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Upper Gastrointestinal Bleeding")] = [
    ("01 — RECOGNIZE", "info", 
     "• Hematemesis, coffee-ground vomitus, melena, or occasionally hematochezia.\n"
     "• Tachycardia, hypotension, syncope, pallor, confusion, shock.\n"
     "• Common causes: Peptic ulcer disease, erosive gastritis, esophagitis, varices, Mallory–Weiss tears.\n"
     "• Risk factors: NSAIDs, anticoagulants, previous ulcer, liver disease, heavy alcohol use."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs; protect airway if massive hematemesis.\n"
     "• Obtain two large-bore IV lines. Send CBC, urea/creatinine, electrolytes, liver tests, coagulation, type & crossmatch.\n"
     "• Resuscitate shock with crystalloid while arranging blood products.\n"
     "• Stop/review anticoagulants and antiplatelet agents.\n"
     "• Contact gastroenterology/endoscopy and critical care early.\n"
     "• Arrange endoscopy after initial stabilization (generally within 24 hours)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Resuscitation and blood transfusion[/color]\n"
     "• Restrictive red-cell transfusion threshold (~7 g/dL) in many hospitalized patients; individualize in massive bleeding or myocardial ischemia.\n\n"
     "[color=#1E3A8A]B. Suspected non-variceal bleeding[/color]\n"
     "• IV pantoprazole: 80 mg IV loading dose followed by 8 mg/hour infusion for high-risk ulcer bleeding after endoscopic hemostasis.\n\n"
     "[color=#1E3A8A]C. Suspected variceal bleeding[/color]\n"
     "• Octreotide: 50 mcg IV bolus, followed by 50 mcg/hour continuous IV infusion (for 2–5 days).\n"
     "• Antibiotic prophylaxis: Ceftriaxone 1 g IV every 24 hours (often for up to 7 days).\n\n"
     "[color=#1E3A8A]D. Erythromycin before endoscopy[/color]\n"
     "• 250 mg IV ~30–120 mins before endoscopy in selected patients with severe bleeding to improve gastric visualization."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay resuscitation in a patient with shock while waiting for hemoglobin.\n"
     "• PPI treatment does not replace resuscitation or endoscopic control of active bleeding.\n"
     "• Use erythromycin cautiously in patients with significant QT prolongation."),
    ("05 — DISPOSITION", "warning", 
     "• ICU or high-dependency for shock, ongoing major hemorrhage, airway compromise, or severe comorbidity.\n"
     "• Very-low-risk patients (e.g., Glasgow-Blatchford Score 0–1) may be suitable for outpatient management."),
    ("REFERENCES", "info", "ACG Upper GI Bleeding Guideline; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Pancreatitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Diagnosis requires at least 2 of 3:\n"
     "• Characteristic acute, persistent epigastric pain radiating to back.\n"
     "• Serum lipase/amylase ≥ 3 times upper limit of normal.\n"
     "• Imaging findings consistent with acute pancreatitis.\n\n"
     "• Common causes: Gallstones, alcohol, hypertriglyceridemia.\n"
     "• Severe features: Persistent organ failure, hypotension, hypoxemia, AKI, altered consciousness."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, hemodynamics, pain, oxygenation, urine output.\n"
     "• Establish IV access and obtain blood tests.\n"
     "• Provide analgesia and antiemetics.\n"
     "• Start isotonic crystalloid resuscitation when needed.\n"
     "• Identify and treat cause (biliary obstruction, cholangitis, hypertriglyceridemia)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV fluids[/color]\n"
     "• Moderately aggressive, individualized isotonic crystalloid. Initial approach: 1–1.5 mL/kg/hour, with a 10 mL/kg bolus if hypovolemic, followed by reassessment. Lactated Ringer's commonly preferred.\n"
     "• Avoid indiscriminate large-volume fluid administration (fluid overload worsens outcomes).\n\n"
     "[color=#1E3A8A]B. Analgesia[/color]\n"
     "• Opioid or non-opioid according to severity. Adjust for renal impairment.\n\n"
     "[color=#1E3A8A]C. Nutrition[/color]\n"
     "• Start oral feeding early as tolerated in mild cases. Enteral nutrition preferred if oral not possible.\n\n"
     "[color=#1E3A8A]D. Antibiotics and biliary intervention[/color]\n"
     "• Do NOT give prophylactic antibiotics for sterile acute pancreatitis or sterile necrosis.\n"
     "• Urgent ERCP for pancreatitis complicated by cholangitis.\n"
     "• Cholecystectomy during same admission for mild gallstone pancreatitis."),
    ("04 — WARNINGS", "danger", 
     "• Avoid indiscriminate large-volume fluid administration.\n"
     "• NSAIDs may be unsuitable in AKI, dehydration, or GI bleeding.\n"
     "• Do not keep every patient fasting until enzymes normalize."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for significant pain, dehydration, persistent vomiting, organ dysfunction, or diagnostic uncertainty.\n"
     "• ICU for shock, respiratory failure, persistent organ failure, or severe metabolic complications."),
    ("REFERENCES", "info", "ACG Guidelines: Management of Acute Pancreatitis (2024); Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Adrenal Crisis and Acute Adrenal Insufficiency")] = [
    ("01 — RECOGNIZE", "info", 
     "• Hypotension or shock responding poorly to initial fluids.\n"
     "• Vomiting, abdominal pain, weakness, fever, altered consciousness.\n"
     "• Hyponatremia, hyperkalemia, hypoglycemia, unexplained volume depletion.\n"
     "• Known adrenal insufficiency, recent withdrawal of chronic corticosteroids, or pituitary/adrenal disease.\n"
     "• Triggers: Infection, surgery, trauma, severe illness, missed glucocorticoid replacement, bilateral adrenal hemorrhage."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as life-threatening endocrine emergency.\n"
     "• Assess ABCs, BP, perfusion, glucose, electrolytes, mental status.\n"
     "• Obtain IV access and blood samples for cortisol/ACTH if feasible, but do NOT delay hydrocortisone.\n"
     "• Give IV/IM hydrocortisone immediately.\n"
     "• Start isotonic saline resuscitation and treat hypoglycemia.\n"
     "• Search for and treat precipitating infection."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Hydrocortisone[/color]\n"
     "• 100 mg IV or IM immediately.\n"
     "• Then 200 mg over 24 hours by continuous IV infusion, or 50 mg IV/IM every 6 hours.\n\n"
     "[color=#1E3A8A]B. IV fluid resuscitation[/color]\n"
     "• 1 litre of 0.9% sodium chloride IV over ~30 mins, subsequent fluid guided by clinical response.\n\n"
     "[color=#1E3A8A]C. Hypoglycemia[/color]\n"
     "• IV glucose if hypoglycemic and cannot swallow safely.\n\n"
     "[color=#1E3A8A]D. Hyperkalemia[/color]\n"
     "• Treat severe hyperkalemia per protocol. (May improve with hydrocortisone and volume restoration, but do not rely on steroid alone if ECG toxicity is present).\n\n"
     "[color=#1E3A8A]E. Treat the precipitating cause[/color]\n"
     "• Empiric antibiotics promptly if bacterial infection suspected. Investigate adrenal hemorrhage."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay the initial dose for laboratory confirmation.\n"
     "• There is no meaningful risk of overdose from the emergency initial hydrocortisone dose when adrenal crisis is suspected.\n"
     "• Patients receiving chronic glucocorticoids may have HPA suppression even without known adrenal disease."),
    ("05 — DISPOSITION", "warning", 
     "• All suspected adrenal crises require urgent hospital treatment.\n"
     "• ICU/high-dependency for refractory shock, severe electrolyte disturbance, or multiorgan dysfunction.\n"
     "• Arrange endocrinology review, sick-day rules, and emergency steroid education."),
    ("REFERENCES", "info", "NICE NG243; Society for Endocrinology.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Liver Failure and Hepatic Encephalopathy")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute liver failure (ALF) is acute liver injury with coagulopathy (INR ≥1.5) and hepatic encephalopathy in a patient without pre-existing cirrhosis.\n"
     "• Jaundice, nausea, vomiting, RUQ discomfort.\n"
     "• Confusion, agitation, drowsiness, coma.\n"
     "• Hypoglycemia, metabolic acidosis, coagulopathy, AKI, cerebral edema.\n"
     "• Causes: Paracetamol toxicity, viral hepatitis, drug-induced liver injury, autoimmune hepatitis, ischemic hepatitis, Wilson disease, pregnancy-related."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, GCS, bedside glucose, oxygenation, hemodynamic status.\n"
     "• Check INR, liver enzymes, bilirubin, renal function, electrolytes, blood gas, glucose urgently.\n"
     "• Identify all medications and toxic exposures (especially paracetamol).\n"
     "• Start N-acetylcysteine promptly when paracetamol toxicity possible; consider in early-stage non-paracetamol ALF under specialist guidance.\n"
     "• Contact a liver-transplant center urgently. Do not wait for advanced encephalopathy."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. N-acetylcysteine (NAC) for suspected paracetamol toxicity[/color]\n"
     "• 150 mg/kg IV over 1 hour.\n"
     "• 50 mg/kg IV over 4 hours.\n"
     "• 100 mg/kg IV over 16 hours.\n"
     "• Do not automatically stop NAC at 21 hours if persistent liver injury.\n\n"
     "[color=#1E3A8A]B. Hypoglycemia[/color]\n"
     "• IV glucose if hypoglycemic. Consider continuous glucose infusion if recurrent.\n\n"
     "[color=#1E3A8A]C. Hepatic encephalopathy and cerebral edema[/color]\n"
     "• Elevate head ~30 degrees. Maintain oxygenation, avoid hypotension, fever, severe hypercapnia.\n"
     "• Consider early airway protection. Hypertonic saline or mannitol for suspected intracranial hypertension under specialist protocol.\n"
     "• Lactulose is not a substitute for specialist management of cerebral edema in ALF.\n\n"
     "[color=#1E3A8A]D. Coagulopathy[/color]\n"
     "• Monitor INR. Use blood products for clinically significant bleeding or procedure-specific indications. INR elevation alone does not necessarily mean prophylactic plasma is beneficial."),
    ("04 — WARNINGS", "danger", 
     "• Do not automatically stop NAC at 21 hours if persistent liver injury.\n"
     "• Hypoglycemia may recur because hepatic glycogen stores are impaired.\n"
     "• Unnecessary plasma may cause fluid overload and obscure progression of liver failure."),
    ("05 — DISPOSITION", "warning", 
     "• Urgent admission and early transfer discussion with a liver-transplant center.\n"
     "• ICU for encephalopathy, hypoglycemia, shock, severe acidosis, AKI, or organ failure."),
    ("REFERENCES", "info", "AASLD Management of Acute Liver Failure; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Sepsis and Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Sepsis is life-threatening organ dysfunction caused by a dysregulated response to infection.\n"
     "• Altered mental status. Hypotension/poor peripheral perfusion.\n"
     "• Tachypnea, hypoxemia, respiratory failure. Oliguria/AKI.\n"
     "• Elevated lactate, thrombocytopenia, coagulopathy.\n"
     "• Septic shock: Need for vasopressors to maintain MAP ≥65 mmHg and lactate >2 mmol/L despite adequate volume resuscitation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and initiate resuscitation immediately.\n"
     "• Measure lactate. Obtain blood cultures before antibiotics if no significant delay.\n"
     "• Start empiric IV antibiotics promptly (especially in septic shock).\n"
     "• Give IV crystalloid for hypoperfusion/shock with frequent reassessment.\n"
     "• Start norepinephrine if hypotension persists during/after fluid resuscitation.\n"
     "• Identify and control the infection source (drainage, device removal)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Empiric antibiotics[/color]\n"
     "• Select regimen based on likely source, severity, local resistance, allergies, renal function.\n"
     "• Examples: Ceftriaxone (community-acquired) or Piperacillin-tazobactam / Cefepime (severe hospital-associated).\n"
     "• Add MRSA or anaerobic coverage only when indicated.\n\n"
     "[color=#1E3A8A]B. Initial IV fluids[/color]\n"
     "• Initial crystalloid volume around 30 mL/kg within first 3 hours (suggested, not inflexible). Use smaller boluses with reassessment if heart failure/kidney disease.\n"
     "• Stop/reduce fluids when signs of fluid overload develop.\n\n"
     "[color=#1E3A8A]C. Norepinephrine[/color]\n"
     "• First-line vasopressor. Titrate to MAP target ~65 mmHg.\n\n"
     "[color=#1E3A8A]D. Additional vasopressors[/color]\n"
     "• Add vasopressin when norepinephrine requirements escalate. Consider epinephrine if MAP remains inadequate.\n\n"
     "[color=#1E3A8A]E. Hydrocortisone[/color]\n"
     "• 200 mg/day IV (50 mg every 6 hours or continuous infusion) in vasopressor-dependent shock."),
    ("04 — WARNINGS", "danger", 
     "• In septic shock, do not delay treatment for imaging or culture collection.\n"
     "• Persistent hypotension after fluid administration requires vasopressor assessment, not endless fluid boluses.\n"
     "• Steroids do not replace appropriate antibiotics, source control, fluids, or vasopressors."),
    ("05 — DISPOSITION", "warning", 
     "• ICU/high-dependency for vasopressor-dependent shock, respiratory failure, altered consciousness, or progressive organ dysfunction."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign; Local antimicrobial protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Insulin-Related Emergencies and Severe Hypoglycemia")] = [
    ("01 — RECOGNIZE", "info", 
     "• Hypoglycemia after insulin administration or missed meals.\n"
     "• Repeated low glucose during renal/hepatic impairment.\n"
     "• Insulin pump failure or interruption of basal insulin.\n"
     "• Accidental insulin overdose or wrong insulin type.\n"
     "• Marked hyperglycemia after missed insulin/pump interruption.\n"
     "• Risk factors: Reduced food intake, vomiting, exercise, alcohol, renal impairment, medication errors."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Check bedside glucose immediately.\n"
     "• Assess ABCs, consciousness, seizure activity, ability to swallow.\n"
     "• If conscious and can swallow safely, give rapid-acting oral glucose.\n"
     "• If unable to swallow safely, give IV glucose; use glucagon if IV access unavailable.\n"
     "• Review insulin type, concentration, dose, timing, food intake.\n"
     "• Consult toxicology/poison services for major overdose. Assess for ketosis/DKA if pump failure suspected."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Conscious patient with mild-to-moderate hypoglycemia[/color]\n"
     "• 15–20 g rapid-acting oral glucose. Recheck in 15 mins. Repeat if low. Provide longer-acting carbohydrate once corrected.\n\n"
     "[color=#1E3A8A]B. Severe hypoglycemia: IV glucose[/color]\n"
     "• 10–25 g IV glucose (e.g., 100 mL of 10% dextrose). Recheck within 10–15 mins. Consider continuous glucose infusion if recurrent.\n\n"
     "[color=#1E3A8A]C. Glucagon (No IV access)[/color]\n"
     "• 1 mg IM in adults. Recheck glucose and provide oral carbohydrate once awake.\n"
     "• May be less effective after prolonged fasting or severe liver disease.\n\n"
     "[color=#1E3A8A]D. Suspected insulin overdose[/color]\n"
     "• Correct hypoglycemia with IV glucose. May require titrated continuous glucose infusion. Obtain toxicology advice for large/long-acting exposures.\n\n"
     "[color=#1E3A8A]E. Insulin pump interruption[/color]\n"
     "• Check glucose and blood ketones. Assess for DKA. Restore insulin delivery or use alternative regimen."),
    ("04 — WARNINGS", "danger", 
     "• Do not give oral food/drink to a patient with impaired consciousness or unsafe swallowing.\n"
     "• Long-acting insulin overdoses may cause recurrent hypoglycemia for many hours.\n"
     "• Patients with type 1 diabetes must not be left without basal insulin coverage."),
    ("05 — DISPOSITION", "warning", 
     "• Admit/observe for recurrent hypoglycemia, insulin overdose, persistent neurological symptoms, or unstable comorbidities.\n"
     "• ICU/high-dependency for prolonged severe hypoglycemia, seizures, airway compromise, or major overdose."),
    ("REFERENCES", "info", "ADA Standards of Care 2026; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Poisoning and Toxicological Emergencies")] = [
    ("01 — RECOGNIZE", "info", 
     "Unexplained altered consciousness, seizures, respiratory depression, arrhythmia, metabolic acidosis, abnormal pupils, unusual secretions, or history of exposure.\n\n"
     "[color=#1E3A8A]Important toxidromes:[/color]\n"
     "• Opioid: Reduced consciousness, slow breathing, pinpoint pupils.\n"
     "• Sympathomimetic: Agitation, sweating, hypertension, tachycardia, hyperthermia.\n"
     "• Anticholinergic: Agitation, hot dry skin, dilated pupils, urinary retention.\n"
     "• Cholinergic: Salivation, lacrimation, bronchorrhea, diarrhea, bradycardia, seizures.\n"
     "• Sedative-hypnotic: Drowsiness, ataxia, slurred speech, respiratory depression."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Protect staff and patient from ongoing contamination.\n"
     "• Assess ABCs, glucose, temperature, ECG, vital signs.\n"
     "• Remove contaminated clothing and irrigate exposed skin/eyes.\n"
     "• Support ventilation and circulation. Identify agent, amount, route, time.\n"
     "• Contact a poison center or clinical toxicologist.\n"
     "• Do NOT induce vomiting. Avoid routine antidote use without indication."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Activated charcoal[/color]\n"
     "• 50 g orally or via gastric tube in selected poisonings. Consider only for selected substances when ingestion recent (within ~1 hour) and benefit outweighs risks. Protect airway.\n\n"
     "[color=#1E3A8A]B. Opioid toxicity: Naloxone[/color]\n"
     "• Titrate IV naloxone to restore adequate ventilation (e.g., 0.04–0.1 mg IV initially). Larger doses may be required in severe respiratory depression.\n\n"
     "[color=#1E3A8A]C. Acetaminophen/Paracetamol toxicity: NAC[/color]\n"
     "• Start NAC according to established protocol. Assess timing, concentration, LFTs, INR, renal function.\n\n"
     "[color=#1E3A8A]D. Cholinergic poisoning[/color]\n"
     "• Atropine IV, repeat rapidly and escalate doses according to clinical response. Endpoint is improvement in bronchial secretions, oxygenation, ventilation, circulation.\n\n"
     "[color=#1E3A8A]E. Benzodiazepines for toxicological seizures[/color]\n"
     "• Use appropriate benzodiazepine regimen. Monitor respiratory status, oxygenation, BP, consciousness.\n\n"
     "[color=#1E3A8A]F. General management[/color]\n"
     "• Treat hypoglycemia, hypoxia, shock, hyperthermia, arrhythmias. Agent-specific antidotes when indicated. Consider hemodialysis for selected severe poisonings."),
    ("04 — WARNINGS", "danger", 
     "• Do not give charcoal to patients with unprotected airway or for caustics, alcohols, metals (e.g., iron).\n"
     "• The aim of naloxone is adequate ventilation, not necessarily complete awakening.\n"
     "• Flumazenil is not routinely recommended in undifferentiated overdose.\n"
     "• Do not delay life-saving supportive care while waiting for toxicology test results."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for persistent symptoms, significant ECG abnormalities, metabolic acidosis, seizures, respiratory depression, or exposure to potentially lethal substance.\n"
     "• ICU for severe poisoning requiring airway support, vasopressors, or management of life-threatening arrhythmia.\n"
     "• Intentional poisoning requires mental-health assessment once medically stable."),
    ("REFERENCES", "info", "WHO clinical protocols for poisoning; Local toxicology guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Heat Stroke and Hypothermia")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Heat stroke[/color]\n"
     "• Severe heat illness with CNS dysfunction (confusion, seizures, coma) associated with heat exposure/exertion.\n"
     "• Core temperature often > 40°C.\n"
     "• Complications: Rhabdomyolysis, AKI, liver injury, coagulopathy, shock.\n\n"
     "[color=#1E3A8A]Hypothermia[/color]\n"
     "• Core temperature < 35°C.\n"
     "• Shivering, confusion, bradycardia, poor coordination, reduced consciousness, dysrhythmias.\n"
     "• Severe hypothermia may produce profound bradycardia or apparent death."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]Heat stroke[/color]\n"
     "• Move patient away from heat, remove excess clothing.\n"
     "• Assess ABCs, glucose, core temperature, neurological status.\n"
     "• Begin active cooling immediately. Establish IV access.\n\n"
     "[color=#1E3A8A]Hypothermia[/color]\n"
     "• Move to warm environment. Remove wet clothing, insulate from ground.\n"
     "• Handle gently. Assess circulation/breathing carefully.\n"
     "• Begin appropriate rewarming and continuous cardiac monitoring."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Heat stroke: rapid active cooling[/color]\n"
     "• Whole-body cold-water immersion is preferred for exertional heat stroke. If impractical, use cold wet towels, ice sheets, evaporative cooling.\n"
     "• Aim to reduce core temp rapidly to ~39°C, then stop intensive cooling to avoid overcooling.\n"
     "• Antipyretics are NOT effective for heat stroke and may worsen hepatic/renal injury.\n\n"
     "[color=#1E3A8A]B. Heat stroke with shock[/color]\n"
     "• Isotonic crystalloid boluses guided by perfusion and response.\n\n"
     "[color=#1E3A8A]C. Seizures during heat illness[/color]\n"
     "• Treat with benzodiazepine regimen. Continue rapid cooling.\n\n"
     "[color=#1E3A8A]D. Hypothermia: rewarming[/color]\n"
     "• Mild: Insulation, dry clothing, passive rewarming.\n"
     "• Moderate/Severe: Active external rewarming and warmed IV fluids. Forced-air warming or approved devices.\n\n"
     "[color=#1E3A8A]E. Cardiac arrest in severe hypothermia[/color]\n"
     "• Follow ALS protocol adapted for hypothermia. Consider extracorporeal life support where available."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay cooling while waiting for laboratory results.\n"
     "• Avoid uncontrolled overcooling.\n"
     "• Avoid direct high heat on insensate skin and rough handling in hypothermia.\n"
     "• Do not conclude death solely from profound cooling without following appropriate resuscitation protocols."),
    ("05 — DISPOSITION", "warning", 
     "• Heat stroke requires emergency hospital assessment and usually admission; ICU for organ dysfunction, shock, seizures, or persistent encephalopathy.\n"
     "• Moderate-to-severe hypothermia, dysrhythmias, reduced consciousness, or hemodynamic instability requires monitored hospital care."),
    ("REFERENCES", "info", "AHA/Red Cross 2024 First Aid Guidelines; AHA 2024 Hypothermia Update.")
]


# ==================== BATCH 7 & 8 (TOPICS 31-40) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Severe Hyponatremia and Sodium Disorders")] = [
    ("01 — RECOGNIZE", "info", 
     "• Hyponatremia: Serum sodium < 135 mmol/L.\n"
     "• Mild: 130–134. Moderate: 125–129. Profound: < 125 mmol/L.\n"
     "• Severe neuro symptoms: Seizures, coma, marked reduction in consciousness, severe confusion, cerebral edema.\n"
     "• Causes: Hypovolemic (GI losses, diuretics, adrenal insufficiency), Euvolemic (SIADH, hypothyroidism, excess water), Hypervolemic (HF, cirrhosis, CKD).\n"
     "• Hyperglycemia may cause translocational hyponatremia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, GCS, seizures, bedside glucose.\n"
     "• Obtain urgent serum sodium, K+, glucose, renal function, serum osmolality.\n"
     "• If severe neuro symptoms, give 3% hypertonic saline promptly.\n"
     "• Identify duration: acute (<48h) vs chronic/unknown.\n"
     "• Stop contributing medications. Monitor sodium frequently."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Severe symptomatic hyponatremia[/color]\n"
     "• 3% NaCl 100 mL IV over 10 mins. Repeat up to 2 additional times if severe symptoms persist.\n"
     "• Goal: Initial rise of ~4–6 mmol/L to reduce severe symptoms.\n"
     "• Do not aim to normalize sodium rapidly. Avoid rise > 10 mmol/L in first 24h, > 8 mmol/L per 24h thereafter.\n\n"
     "[color=#1E3A8A]B. Hypovolemic hyponatremia[/color]\n"
     "• 0.9% NaCl IV when volume depletion present. Monitor for sudden urine output increase (may cause rapid Na+ rise).\n\n"
     "[color=#1E3A8A]C. SIADH/Euvolemic[/color]\n"
     "• Treat cause. Fluid restriction in stable chronic SIADH. Severe symptoms require hypertonic saline.\n\n"
     "[color=#1E3A8A]D. Overcorrection[/color]\n"
     "• If sodium rises too quickly: desmopressin + electrolyte-free water (D5W) under specialist guidance to halt/reverse."),
    ("04 — WARNINGS", "danger", 
     "• High-risk for osmotic demyelination: severe malnutrition, alcohol use disorder, advanced liver disease, hypokalemia, very low initial sodium.\n"
     "• Do not apply fluid restriction indiscriminately to hypovolemic patients.\n"
     "• Do not attempt rapid sodium relowering without a monitored protocol."),
    ("05 — DISPOSITION", "warning", 
     "• Admit severe symptomatic hyponatremia, profound reduction, rapidly changing sodium, or serious underlying cause.\n"
     "• ICU for seizures, coma, respiratory compromise, or hypertonic saline requiring intensive monitoring."),
    ("REFERENCES", "info", "European clinical practice guideline on hyponatraemia; Society for Endocrinology.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Severe Asthma and Near-Fatal Asthma")] = [
    ("01 — RECOGNIZE", "info", 
     "• Severe: Marked breathlessness, inability to complete sentences, RR >30, tachycardia, accessory muscle use. PEF substantially reduced.\n"
     "• Life-threatening: Silent chest, exhaustion, cyanosis, poor respiratory effort, confusion, reduced consciousness, hypotension, bradycardia.\n"
     "• Normal/rising PaCO2 in severe distress indicates impending respiratory failure."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and call for senior emergency/critical-care support. Sit upright.\n"
     "• Controlled oxygen (target 93–95%).\n"
     "• Start repeated inhaled bronchodilator therapy immediately.\n"
     "• Add inhaled ipratropium for severe exacerbations.\n"
     "• Give systemic corticosteroids early.\n"
     "• Consider IV magnesium sulfate for severe disease with inadequate response.\n"
     "• Arrange early airway support if deterioration/exhaustion."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Salbutamol[/color]\n"
     "• 2.5–5 mg nebulized, repeated every 20 mins during first hour. Continuous nebulization in selected severe cases.\n\n"
     "[color=#1E3A8A]B. Ipratropium[/color]\n"
     "• 0.5 mg nebulized every 20 mins for up to 3 doses in first hour.\n\n"
     "[color=#1E3A8A]C. Systemic Corticosteroids[/color]\n"
     "• Prednisolone 40–50 mg orally daily for 5–7 days. IV if oral impossible.\n\n"
     "[color=#1E3A8A]D. IV Magnesium Sulfate[/color]\n"
     "• 2 g IV over ~20 mins in selected severe exacerbations with poor response.\n\n"
     "[color=#1E3A8A]E. Near-fatal asthma[/color]\n"
     "• Involve experienced airway/critical-care team early. NIV should not delay intubation. Intubation for exhaustion, worsening consciousness, refractory hypoxemia.\n"
     "• Ventilator settings designed to minimize dynamic hyperinflation and auto-PEEP."),
    ("04 — WARNINGS", "danger", 
     "• High-dose beta2-agonists can cause tachycardia, hypokalemia, and lactic acidosis.\n"
     "• Persistent tachypnea may reflect lactic acidosis or fatigue rather than bronchospasm.\n"
     "• Positive-pressure ventilation can precipitate hypotension and barotrauma."),
    ("05 — DISPOSITION", "warning", 
     "• Admit life-threatening features, persistent severe symptoms, poor response, or significant comorbidity.\n"
     "• ICU for respiratory failure, ventilatory support, altered consciousness, or impending arrest."),
    ("REFERENCES", "info", "GINA 2026 Strategy Report; Local emergency asthma protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Pericardial Tamponade")] = [
    ("01 — RECOGNIZE", "info", 
     "• Cardiac tamponade occurs when pericardial pressure impairs cardiac filling and causes reduced cardiac output.\n"
     "• Hypotension, tachycardia, dyspnea, raised JVP. Pulsus paradoxus. Muffled heart sounds (not always present).\n"
     "• Obstructive shock, oliguria, altered consciousness, cardiac arrest.\n"
     "• Causes: Malignancy, TB/infection, trauma/iatrogenic, aortic dissection, uremia, inflammatory."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, BP, perfusion, oxygenation.\n"
     "• Obtain urgent bedside echocardiography.\n"
     "• Activate cardiology/cardiothoracic surgery/emergency procedural team.\n"
     "• Prepare for urgent pericardial drainage if hemodynamic compromise.\n"
     "• Use cautious IV fluid administration as a temporary bridge if preload responsive."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Urgent pericardial drainage[/color]\n"
     "• Hemodynamic instability/shock requires urgent drainage. Echo-guided pericardiocentesis. Surgical drainage for traumatic bleeding, purulent effusion, clotted hemopericardium.\n\n"
     "[color=#1E3A8A]B. Temporary hemodynamic support[/color]\n"
     "• Cautious isotonic crystalloid bolus (e.g., 250 mL) if hypotensive and awaiting drainage, then immediate reassessment.\n"
     "• Fluids are only a temporary bridge, not definitive treatment. Avoid routine diuretics."),
    ("04 — WARNINGS", "danger", 
     "• Pericardiocentesis is high-risk; do not attempt by untrained operator.\n"
     "• Do not delay life-saving drainage for CT or nonessential investigations.\n"
     "• Avoid positive-pressure ventilation when possible in severe tamponade (can reduce venous return and precipitate collapse)."),
    ("05 — DISPOSITION", "warning", 
     "• Emergency admission and definitive drainage.\n"
     "• ICU or cardiac critical-care monitoring after drainage."),
    ("REFERENCES", "info", "ESC 2025 Guidelines for Myocarditis and Pericarditis; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Atrial Fibrillation with RVR")] = [
    ("01 — RECOGNIZE", "info", 
     "• Irregularly irregular rhythm with absent consistent P waves.\n"
     "• Rapid ventricular rate, often > 100–110 beats/min.\n"
     "• Symptoms: Palpitations, dyspnea, chest discomfort, dizziness, fatigue.\n"
     "• Assess for hemodynamic instability, acute HF, myocardial ischemia, sepsis, PE."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, BP, perfusion, mental status, chest pain. 12-lead ECG and continuous monitoring.\n"
     "• If hemodynamically unstable: urgent synchronized electrical cardioversion.\n"
     "• If stable: determine rate vs rhythm control. Identify/treat reversible triggers (infection, hypovolemia, hypoxia, ischemia, electrolytes).\n"
     "• Assess stroke risk and anticoagulation needs after stabilization."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Unstable AF: Synchronized Cardioversion[/color]\n"
     "• Indications: Hypotension/shock, ongoing ischemia, acute pulmonary edema, altered consciousness.\n"
     "• Biphasic energy (e.g., 200 J). Sedation if feasible without delaying.\n\n"
     "[color=#1E3A8A]B. Stable AF: Diltiazem[/color]\n"
     "• IV 0.25 mg/kg over 2 mins. Second dose 0.35 mg/kg after 15 mins if needed. Infusion 5–10 mg/hour.\n\n"
     "[color=#1E3A8A]C. Stable AF: Metoprolol[/color]\n"
     "• IV 2.5–5 mg over 2 mins. Repeat every 5 mins to max 15 mg.\n\n"
     "[color=#1E3A8A]D. Alternative rate control[/color]\n"
     "• Digoxin (selected HF), IV amiodarone (critically ill/decompensated HF).\n\n"
     "[color=#1E3A8A]E. Anticoagulation[/color]\n"
     "• Assess CHA2DS2-VASc. Elective cardioversion requires appropriate anticoagulation or imaging. Emergency cardioversion must NOT be delayed for anticoagulation."),
    ("04 — WARNINGS", "danger", 
     "• Avoid IV diltiazem in moderate-to-severe LV systolic dysfunction or decompensated heart failure.\n"
     "• Avoid AV-nodal blockers in pre-excited AF/WPW.\n"
     "• Do not combine multiple AV-nodal blockers casually (bradycardia/hypotension risk)."),
    ("05 — DISPOSITION", "warning", 
     "• Admit instability, acute HF, ischemia, major precipitating illness, or inadequate rate control.\n"
     "• Discharge only after stability and appropriate plan for anticoagulation and rate/rhythm management."),
    ("REFERENCES", "info", "2023 ACC/AHA/ACCP/HRS AF Guideline; AHA Tachyarrhythmia Algorithm.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Specific Antidotes and High-Risk Poisonings")] = [
    ("01 — RECOGNIZE", "info", 
     "Consider specific toxic exposures when history, toxidrome, ECG, or labs suggest:\n"
     "• Paracetamol, Salicylates, Methanol/Ethylene glycol, Tricyclic antidepressants (TCA), Beta-blockers/Calcium channel blockers (CCB), Digoxin, Isoniazid."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize ABCs, glucose, temperature. Obtain ECG, electrolytes, renal function, blood gas, targeted drug concentrations.\n"
     "• Contact poison center/toxicologist early.\n"
     "• Do not delay life-saving antidotes when indication is clear.\n"
     "• Assess need for hemodialysis in severe toxic alcohol, salicylate, lithium poisonings."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Salicylate poisoning[/color]\n"
     "• Sodium bicarbonate IV to alkalinize serum/urine (e.g., 150 mEq in 1 L D5W). Goal urine pH 7.5–8.0. Monitor K+.\n"
     "• Hemodialysis for severe neuro toxicity, pulmonary edema, renal failure, refractory acid-base disturbances.\n\n"
     "[color=#1E3A8A]B. Methanol/Ethylene glycol[/color]\n"
     "• Fomepizole: 15 mg/kg IV initial dose, subsequent doses per protocol. Urgent toxicology/nephrology for possible dialysis.\n\n"
     "[color=#1E3A8A]C. Tricyclic antidepressant (TCA)[/color]\n"
     "• Sodium bicarbonate 1–2 mEq/kg IV for significant QRS widening, ventricular dysrhythmia, or hypotension. Repeat per ECG/hemodynamics.\n\n"
     "[color=#1E3A8A]D. Beta-blocker/CCB overdose[/color]\n"
     "• High-dose insulin euglycemia therapy. IV calcium (for CCB). Vasopressors. Glucagon (for beta-blocker). Consult toxicology early.\n\n"
     "[color=#1E3A8A]E. Digoxin toxicity[/color]\n"
     "• Digoxin immune Fab (dosing based on level/dose/severity). Monitor K+ closely (may change rapidly).\n\n"
     "[color=#1E3A8A]F. Isoniazid-associated seizures[/color]\n"
     "• Pyridoxine (Vitamin B6): Gram-for-gram with INH ingested. If unknown in severe presentation, 5 g IV initial."),
    ("04 — WARNINGS", "danger", 
     "• Do not use flumazenil routinely in undifferentiated overdose.\n"
     "• Do not induce vomiting.\n"
     "• Avoid intubation in salicylate poisoning if possible (loss of compensatory hyperventilation can worsen acidemia).\n"
     "• Do not use physostigmine in suspected TCA poisoning."),
    ("05 — DISPOSITION", "warning", 
     "• Admit significant toxicity, abnormal ECG, metabolic acidosis, persistent symptoms, or dangerous exposures.\n"
     "• ICU for refractory seizures, shock, severe acid-base disturbances, or antidote infusions.\n"
     "• Intentional overdose requires psychosocial assessment after stabilization."),
    ("REFERENCES", "info", "EXTRIP Workgroup; ACMT Guidance; Local poison-center protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "ACS Complications and Deterioration")] = [
    ("01 — RECOGNIZE", "info", 
     "Suspect deterioration in a patient with STEMI/NSTEMI when:\n"
     "• Persistent/recurrent chest pain despite treatment.\n"
     "• New hypotension (SBP < 90), cold extremities, oliguria, confusion, rising lactate (cardiogenic shock).\n"
     "• Acute pulmonary edema, increasing oxygen requirement, respiratory failure.\n"
     "• Sustained VT, VF, severe bradycardia, high-grade AV block.\n"
     "• New loud systolic murmur, sudden pulmonary edema, or shock (mechanical complication: papillary muscle rupture, VSD, free-wall rupture).\n"
     "• Sudden collapse, JVD, PEA (tamponade/rupture)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate emergency response and contact interventional cardiology immediately.\n"
     "• Assess ABCs, perfusion. Attach continuous ECG monitoring and defibrillator pads. 12-lead ECG immediately.\n"
     "• Establish 2 IV lines. Bedside echocardiography urgently if shock, new murmur, or unexplained deterioration.\n"
     "• Check glucose, blood gas, lactate, electrolytes, CBC, renal function, coagulation, serial troponin.\n"
     "• Arrange emergency coronary angiography/revascularization when indicated."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Recurrent ischemia or cardiogenic shock[/color]\n"
     "• Aspirin 162–325 mg chewed if not already given. Do not delay emergency revascularization.\n\n"
     "[color=#1E3A8A]B. Cardiogenic shock[/color]\n"
     "• Norepinephrine infusion 0.05–0.1 mcg/kg/min IV, titrated to MAP ≥ 65 mmHg.\n"
     "• Do not routinely administer large fluid boluses if pulmonary congestion is present.\n"
     "• Revascularization of culprit vessel is the priority. Mechanical circulatory support decisions require specialist assessment.\n\n"
     "[color=#1E3A8A]C. Life-threatening arrhythmias[/color]\n"
     "• Pulseless VF/pVT: immediate unsynchronized defibrillation.\n"
     "• Unstable tachyarrhythmia with pulse: synchronized cardioversion.\n\n"
     "[color=#1E3A8A]D. Mechanical complications[/color]\n"
     "• Emergency echocardiography. Contact cardiac surgery/interventional cardiology immediately. Consider temporary mechanical circulatory support as bridge."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay emergency revascularization while waiting for serial biomarkers.\n"
     "• Do not use synchronized cardioversion for VF or pulseless VT.\n"
     "• Mechanical complications can deteriorate rapidly; medical stabilization alone is not definitive."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to cardiac ICU or equivalent monitored critical-care setting.\n"
     "• Immediate transfer to PCI-capable center if emergency revascularization/surgery unavailable locally."),
    ("REFERENCES", "info", "2025 ACC/AHA ACS Guideline; AHA ACLS Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute RV Failure and Obstructive Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute right ventricular (RV) failure occurs when the RV cannot deliver adequate blood through the pulmonary circulation. Obstructive shock may result from massive PE, cardiac tamponade, tension pneumothorax.\n"
     "• Hypotension, tachycardia, cool extremities, confusion, oliguria.\n"
     "• Elevated JVP. Clear lungs despite severe hypotension (though varies with cause).\n"
     "• Bedside echo: RV dilatation/dysfunction, septal flattening, or pericardial effusion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate emergency/critical-care teams. Assess ABCs.\n"
     "• Give oxygen for hypoxemia and support ventilation if necessary.\n"
     "• Continuous ECG, SpO2, frequent BP monitoring. Obtain bedside echocardiography ASAP.\n"
     "• Identify obstructive cause urgently; treat the cause rather than hypotension alone.\n"
     "• Avoid indiscriminate fluid loading (can worsen RV dilatation and reduce LV filling)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fluid management[/color]\n"
     "• If hypovolemia suspected and no significant RV overdistension: cautious 250 mL IV bolus, reassess immediately.\n"
     "• Stop fluid loading if RV dilatation, venous congestion, or oxygenation worsens.\n\n"
     "[color=#1E3A8A]B. Vasopressor support[/color]\n"
     "• Norepinephrine 0.05–0.1 mcg/kg/min IV, titrated to adequate systemic pressure and organ perfusion.\n\n"
     "[color=#1E3A8A]C. Suspected high-risk PE[/color]\n"
     "• Activate PE response team. Urgent reperfusion (systemic thrombolysis, surgical embolectomy, catheter-based treatment).\n\n"
     "[color=#1E3A8A]D. Suspected cardiac tamponade[/color]\n"
     "• Urgent image-guided pericardial drainage. Small fluid boluses only as temporary bridge.\n\n"
     "[color=#1E3A8A]E. Tension pneumothorax[/color]\n"
     "• Immediate decompression according to local protocol, followed by definitive pleural drainage."),
    ("04 — WARNINGS", "danger", 
     "• Large empiric fluid boluses can worsen RV failure. Do not assume every hypotensive patient needs more fluid.\n"
     "• Excessive vasoconstriction can impair peripheral perfusion.\n"
     "• Diuretics and unnecessary positive-pressure ventilation can worsen preload-dependent tamponade physiology."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to ICU for persistent hypotension, RV failure, vasopressor use, or reperfusion treatment.\n"
     "• Transfer urgently to a center with required cardiology/interventional/surgical capability."),
    ("REFERENCES", "info", "2026 AHA/ACC PE Guideline; ESC/ERS PE Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Severe Metabolic Acidosis")] = [
    ("01 — RECOGNIZE", "info", 
     "Metabolic acidosis is a primary reduction in serum bicarbonate, generally accompanied by acidemia.\n"
     "• Deep, rapid breathing (Kussmaul). Altered mental status, weakness, hypotension, shock.\n"
     "• Arrhythmias/ECG changes from electrolyte disturbances.\n"
     "• Causes: Lactic acidosis (shock, sepsis), DKA, renal failure, toxic alcohols, salicylates, diarrhea/RTA.\n"
     "• Anion gap = Na − (Cl + HCO3). Low albumin can mask elevated gap."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status. Treat shock, hypoxemia, sepsis, DKA, poisoning immediately.\n"
     "• Obtain blood gas, electrolytes, glucose, renal function, lactate, ketones. Calculate anion gap.\n"
     "• Check potassium urgently before initiating insulin in suspected DKA.\n"
     "• Contact critical care/nephrology/toxicology early for severe or refractory acidemia."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Treat the underlying cause[/color]\n"
     "• DKA: Isotonic IV fluids, IV insulin (after checking K+), K+ replacement, add dextrose when glucose falls.\n"
     "• Lactic acidosis (shock/sepsis): Restore oxygen delivery/perfusion, treat infection, fluids/vasopressors.\n"
     "• Toxic ingestion: Specific antidotes, dialysis when indicated.\n\n"
     "[color=#1E3A8A]B. Sodium bicarbonate[/color]\n"
     "• No single routine dose. Consider selectively in severe acidemia with defined indication (e.g., severe AKI, specific toxicologic emergencies).\n"
     "• In DKA: routine bicarbonate not recommended; only exceptional severe acidemia (pH < 7.0) under senior supervision.\n"
     "• Ensure adequate ventilation (bicarbonate generates CO2).\n\n"
     "[color=#1E3A8A]C. Renal replacement therapy[/color]\n"
     "• Discuss urgently for severe/refractory acidemia, significant AKI, or dialyzable toxins."),
    ("04 — WARNINGS", "danger", 
     "• If potassium severely low in DKA, delay insulin while replacing potassium.\n"
     "• A normal/mildly elevated glucose does not exclude DKA (especially with SGLT2 inhibitors).\n"
     "• Bicarbonate can cause hypernatremia, hypokalemia, reduced ionized calcium, volume overload, and increased CO2 generation."),
    ("05 — DISPOSITION", "warning", 
     "• Severe acidemia, hemodynamic instability, altered mental status, respiratory fatigue, or serious electrolyte abnormalities require ICU-level care."),
    ("REFERENCES", "info", "ADA Standards of Care 2026; EXTRIP recommendations; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Thyroid Storm and Myxedema Coma")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Thyroid storm[/color] (life-threatening thyrotoxicosis, precipitated by infection/surgery/trauma):\n"
     "• Fever, marked tachycardia, AF, HF. Agitation, delirium, psychosis, coma. Vomiting, diarrhea, jaundice. Shock.\n\n"
     "[color=#1E3A8A]Myxedema coma[/color] (severe decompensated hypothyroidism):\n"
     "• Hypothermia, bradycardia, hypotension, hypoventilation. Altered mental status, stupor, coma. Hyponatremia, hypoglycemia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and obtain ICU support for organ dysfunction.\n"
     "• Continuous ECG, SpO2, temperature, BP monitoring. Obtain glucose and correct hypoglycemia.\n"
     "• Send TSH, free T4, T3, but do NOT delay treatment while awaiting results.\n"
     "• Check CBC, electrolytes, renal/liver function, cortisol, cultures if infection suspected.\n"
     "• Identify and treat precipitating cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Thyroid Storm[/color]\n"
     "• Beta-blockade: Propranolol 60–80 mg PO every 4–6 hours (IV reserved for monitored settings).\n"
     "• Thionamide: PTU 500–1,000 mg PO/NG loading, then 250 mg every 4 hours (or Methimazole).\n"
     "• Iodine therapy: Give at least 1 hour after thionamide (do not give iodine first).\n"
     "• Glucocorticoid: Hydrocortisone 100 mg IV every 8 hours.\n"
     "• Supportive: External cooling, acetaminophen (avoid aspirin).\n\n"
     "[color=#1E3A8A]B. Myxedema Coma[/color]\n"
     "• IV Levothyroxine: Loading dose 200–400 mcg IV once (lower in older/cardiac disease).\n"
     "• Empiric Glucocorticoids: Hydrocortisone 100 mg IV every 8 hours.\n"
     "• Supportive: Controlled rewarming, respiratory support, cautious fluid/electrolyte correction, treat hypoglycemia."),
    ("04 — WARNINGS", "danger", 
     "• Beta-blockers can precipitate cardiovascular collapse in severe low-output HF or shock.\n"
     "• PTU can cause severe hepatotoxicity.\n"
     "• Rapid thyroid hormone replacement in myxedema can provoke ischemia or arrhythmias.\n"
     "• Avoid sedatives and opioids in myxedema coma where possible."),
    ("05 — DISPOSITION", "warning", 
     "• Both conditions generally require ICU or high-dependency care when severe or associated with organ dysfunction."),
    ("REFERENCES", "info", "2026 Joint Consensus Statement (ETA/BTA/SfE/WEDS).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Massive Hemoptysis and Airway Bleeding")] = [
    ("01 — RECOGNIZE", "info", 
     "Life-threatening hemoptysis is bleeding into the respiratory tract that threatens airway patency, gas exchange, or circulation.\n"
     "• Inability to clear blood/clots from airway. Hypoxemia, respiratory distress, rapidly increasing O2 requirement.\n"
     "• Hemodynamic instability. Large or recurrent episodes of fresh blood. Reduced consciousness.\n"
     "• Causes: Bronchiectasis, TB, malignancy, pulmonary infection, fungal disease, PE, vascular abnormalities."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate emergency, anesthesia/airway, respiratory, and interventional radiology teams early.\n"
     "• Assess ABCs. Provide oxygen and suction blood/clots.\n"
     "• If bleeding side known, position bleeding lung dependent to reduce contamination of unaffected lung.\n"
     "• Establish large-bore IV access; send CBC, coagulation, renal function, crossmatch.\n"
     "• Review/reverse anticoagulants. Prepare for urgent airway protection if unable to maintain oxygenation/airway clearance."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Airway and respiratory support[/color]\n"
     "• Oxygen titrated to needs. Prepare suction, airway equipment, large-bore ETT.\n"
     "• Intubation with experienced airway clinician (plan for blood/clot obstruction). Bronchoscopy for clot removal/localization.\n"
     "• Danger is airway flooding and asphyxiation rather than exsanguination alone.\n\n"
     "[color=#1E3A8A]B. Tranexamic acid (selected cases)[/color]\n"
     "• Nebulized TXA (e.g., 500 mg TID) has been used in selected non-massive/persistent hemoptysis. Do not substitute for airway management/definitive control.\n\n"
     "[color=#1E3A8A]C. Definitive control[/color]\n"
     "• Bronchial artery embolization (BAE) is key definitive treatment for life-threatening/recurrent hemoptysis after stabilization and CT angiography.\n"
     "• Surgical management if embolization fails or underlying lesion requires surgery."),
    ("04 — WARNINGS", "danger", 
     "• The major immediate danger is often airway flooding and asphyxiation.\n"
     "• Avoid unnecessary delays for diagnostic imaging when airway protection is urgently required.\n"
     "• BAE requires careful identification of vessels supplying spinal cord, brain, or heart to avoid catastrophic non-target embolization."),
    ("05 — DISPOSITION", "warning", 
     "• Life-threatening hemoptysis requires admission to ICU or equivalent critical-care setting.\n"
     "• Arrange urgent transfer to facility with airway expertise, bronchoscopy, CT angiography, and IR if unavailable locally."),
    ("REFERENCES", "info", "CIRSE Standards of Practice; Society of Chest Imaging and Interventions Consensus Guidelines.")
]


# ==================== BATCH 9 (TOPICS 41-50) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Hyperkalemia and ECG Changes")] = [
    ("01 — RECOGNIZE", "info", 
     "Hyperkalemia can cause fatal conduction abnormalities and cardiac arrest. Severe hyperkalemia is generally defined as serum potassium ≥6.5 mmol/L.\n"
     "• Muscle weakness, paresthesia, or flaccid paralysis.\n"
     "• Bradycardia, palpitations, syncope, or cardiac arrest.\n"
     "• ECG changes: Tall peaked T waves, PR prolongation, flattening or loss of P waves, QRS widening, bradyarrhythmias, or a sine-wave pattern.\n"
     "• Risk factors: AKI, advanced CKD, missed dialysis, potassium supplements, ACE inhibitors, ARBs, MRAs, and tissue breakdown.\n"
     "• [color=#991B1B]A normal ECG does not exclude dangerous hyperkalemia.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and attach continuous cardiac monitoring.\n"
     "• Obtain a 12-lead ECG immediately.\n"
     "• Establish IV access and repeat potassium urgently if a hemolyzed sample is suspected; do not delay treatment if severe hyperkalemia is likely.\n"
     "• Stop potassium-containing fluids and contributing medications.\n"
     "• Check glucose, renal function, blood gas, bicarbonate, calcium, and magnesium.\n"
     "• Contact nephrology early if advanced renal failure, missed dialysis, or refractory hyperkalemia."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Stabilize the cardiac membrane[/color]\n"
     "• Calcium gluconate 10%: 30 mL IV over ~10 minutes for severe hyperkalemia with ECG changes. Reassess ECG; further dose may be required.\n"
     "• Alternative: Calcium chloride 10% 10 mL IV over ~5 minutes (central access preferred).\n\n"
     "[color=#1E3A8A]B. Shift potassium into cells[/color]\n"
     "• Regular insulin 10 units IV plus 25 g glucose IV (e.g., 250 mL of 10% dextrose). Monitor glucose for at least 4–6 hours.\n"
     "• Nebulized salbutamol 10–20 mg as an adjunct. Do not use as sole therapy.\n\n"
     "[color=#1E3A8A]C. Remove potassium from the body[/color]\n"
     "• Urgent hemodialysis for severe/refractory hyperkalemia, especially in advanced renal failure.\n"
     "• Potassium binders (e.g., sodium zirconium cyclosilicate) as adjuncts.\n"
     "• Loop diuretics if renal function and urine output permit."),
    ("04 — WARNINGS", "danger", 
     "• Calcium stabilizes the myocardium but does not lower serum potassium.\n"
     "• Do not delay calcium in a patient with dangerous ECG changes while preparing insulin.\n"
     "• Insulin can cause delayed, severe hypoglycemia, especially in kidney failure.\n"
     "• Response to salbutamol may be variable, particularly in patients taking beta-blockers."),
    ("05 — DISPOSITION", "warning", 
     "• ICU or high-dependency care for ECG changes, severe hyperkalemia, arrhythmia, or hemodynamic instability.\n"
     "• Discharge only after potassium is safely controlled, cause is addressed, and monitoring/follow-up plan is in place."),
    ("REFERENCES", "info", "UK Kidney Association Guidelines (2026); Resuscitation Council UK (2025).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Upper Gastrointestinal Bleeding and Variceal Hemorrhage")] = [
    ("01 — RECOGNIZE", "info", 
     "Upper gastrointestinal bleeding (UGIB) originates proximal to the ligament of Treitz.\n"
     "• Hematemesis or coffee-ground vomitus. Melena; occasionally hematochezia with massive upper GI bleeding.\n"
     "• Tachycardia, hypotension, syncope, pallor, or shock.\n"
     "• History of peptic ulcer disease, NSAID use, anticoagulation, cirrhosis, or portal hypertension.\n"
     "• Non-variceal bleeding: peptic ulcer, erosive gastritis, esophagitis, or Mallory–Weiss tear.\n"
     "• Variceal bleeding: esophageal or gastric varices in portal hypertension."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and activate major hemorrhage protocol if bleeding is severe.\n"
     "• Consider early airway protection if ongoing massive hematemesis or impaired consciousness.\n"
     "• Insert two large-bore IV cannulas.\n"
     "• Send CBC, urea, creatinine, electrolytes, liver tests, coagulation profile, and group-and-crossmatch.\n"
     "• Resuscitate with blood products and appropriate IV fluids.\n"
     "• Review anticoagulants/antiplatelet agents; plan reversal when indicated.\n"
     "• Contact gastroenterology/endoscopy urgently.\n"
     "• If variceal bleeding is suspected, start vasoactive medication and antibiotic prophylaxis promptly."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Resuscitation and blood transfusion[/color]\n"
     "• Initial 250–500 mL IV crystalloid bolus if hypotensive while arranging blood.\n"
     "• Restrictive transfusion threshold around Hb 7 g/dL in hospitalized UGIB (individualize in shock/ischemia).\n\n"
     "[color=#1E3A8A]B. Suspected non-variceal ulcer bleeding[/color]\n"
     "• Pantoprazole 80 mg IV loading dose followed by 8 mg/hour IV infusion for 72 hours after endoscopic hemostasis of high-risk ulcer.\n\n"
     "[color=#1E3A8A]C. Suspected variceal hemorrhage[/color]\n"
     "• Octreotide: 50 mcg IV bolus, followed by continuous infusion at 25–50 mcg/hour for 2–5 days.\n"
     "• Ceftriaxone: 1 g IV every 24 hours for up to 5–7 days.\n\n"
     "[color=#1E3A8A]D. Endoscopy[/color]\n"
     "• Generally within 24 hours for hospitalized UGIB; suspected acute variceal bleeding generally requires endoscopy within 12 hours."),
    ("04 — WARNINGS", "danger", 
     "• Do not wait for Hb to fall before treating hemorrhagic shock.\n"
     "• Avoid over-transfusion in portal hypertensive bleeding (increases portal pressure).\n"
     "• Do not use epinephrine injection alone as definitive endoscopic treatment for a bleeding ulcer.\n"
     "• Vasoactive therapy is a bridge to definitive endoscopic treatment."),
    ("05 — DISPOSITION", "warning", 
     "• ICU for shock, ongoing massive bleeding, airway compromise, or severe organ dysfunction.\n"
     "• Low-risk discharge only after formal risk assessment (Glasgow-Blatchford Score 0–1) and reliable follow-up."),
    ("REFERENCES", "info", "ACG Upper GI Bleeding Guideline; Baveno VII; AASLD guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Adrenal Crisis (Acute Adrenal Insufficiency)")] = [
    ("01 — RECOGNIZE", "info", 
     "Adrenal crisis is a life-threatening deficiency of cortisol, sometimes with aldosterone deficiency.\n"
     "• Triggers: Infection, sepsis, surgery, trauma, abrupt cessation of long-term glucocorticoids, bilateral adrenal hemorrhage.\n"
     "• Hypotension/shock responding poorly to initial fluids.\n"
     "• Weakness, vomiting, abdominal pain, dehydration.\n"
     "• Hyponatremia, hyperkalemia, hypoglycemia, fever.\n"
     "• Confusion, reduced consciousness, collapse."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat suspected adrenal crisis immediately; do not wait for cortisol results.\n"
     "• Assess ABCs, attach monitoring, establish IV access.\n"
     "• Check bedside glucose and treat hypoglycemia promptly.\n"
     "• Send electrolytes, glucose, renal function, CBC, cortisol, and ACTH if feasible.\n"
     "• Start IV hydrocortisone and isotonic saline.\n"
     "• Identify and treat precipitating cause (e.g., infection)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Immediate glucocorticoid replacement[/color]\n"
     "• Hydrocortisone 100 mg IV immediately (or IM if no IV access).\n"
     "• Continue 200 mg over 24 hours by continuous IV infusion, or 50 mg IV/IM every 6 hours.\n\n"
     "[color=#1E3A8A]B. Fluid resuscitation[/color]\n"
     "• 0.9% sodium chloride: 1 L IV over 30 minutes in adults (if no contraindication).\n"
     "• Reassess BP, pulse, capillary refill, urine output, lung findings.\n\n"
     "[color=#1E3A8A]C. Hypoglycemia[/color]\n"
     "• IV dextrose per protocol if severe hypoglycemia present.\n\n"
     "[color=#1E3A8A]D. Treat the precipitating cause[/color]\n"
     "• Cultures, appropriate antimicrobials, correct electrolyte abnormalities."),
    ("04 — WARNINGS", "danger", 
     "• Short-term emergency hydrocortisone should not be withheld because of concern about a high dose.\n"
     "• Failure to treat adrenal crisis promptly can be fatal.\n"
     "• Avoid unmonitored fluid loading in patients at risk of pulmonary edema."),
    ("05 — DISPOSITION", "warning", 
     "• Admit; ICU for persistent shock, severe electrolyte abnormalities, altered consciousness, or vasopressor need.\n"
     "• Before discharge, ensure patient understands sick-day rules and has access to emergency steroid treatment."),
    ("REFERENCES", "info", "Society for Endocrinology; NICE NG243.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Kidney Injury and Emergency Dialysis Indications")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute kidney injury (AKI) is an acute reduction in kidney function.\n"
     "• Oliguria or anuria. Dehydration, hypotension, or shock.\n"
     "• Peripheral edema, pulmonary edema, or hypertension.\n"
     "• Nausea, vomiting, confusion, pericarditic chest pain, or bleeding.\n"
     "• Hyperkalemia, metabolic acidosis, or other electrolyte abnormalities.\n"
     "• Causes: Prerenal (hypovolemia, sepsis, low CO), Intrinsic (ATN, GN, rhabdomyolysis), Postrenal (obstruction)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, volume status, and urine output.\n"
     "• Obtain IV access and treat shock or sepsis promptly.\n"
     "• Check potassium and ECG urgently if severe AKI is suspected.\n"
     "• Stop/review nephrotoxic medications and adjust renally cleared drugs.\n"
     "• Insert urinary catheter when clinically indicated. Bladder scanning and renal US when obstruction suspected.\n"
     "• Contact nephrology urgently if there are dialysis indications or rapidly worsening renal function."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Correct reversible hemodynamic causes[/color]\n"
     "• If hypovolemic, initial 250–500 mL IV isotonic crystalloid bolus, followed by reassessment.\n"
     "• Do not give repeated fluid boluses to an already overloaded or anuric patient.\n\n"
     "[color=#1E3A8A]B. Medication and nephrotoxin review[/color]\n"
     "• Stop/temporarily hold contributory medications (NSAIDs, ACEi/ARBs, diuretics, contrast, aminoglycosides).\n\n"
     "[color=#1E3A8A]C. Emergency dialysis / renal replacement therapy[/color]\n"
     "• Urgent indications: Refractory/life-threatening hyperkalemia, severe metabolic acidosis refractory to medical treatment, pulmonary edema/fluid overload causing severe hypoxemia, uremic complications (encephalopathy/pericarditis/bleeding), selected severe poisonings.\n"
     "• Do not delay dialysis for an arbitrary creatinine/urea threshold when a life-threatening indication is present."),
    ("04 — WARNINGS", "danger", 
     "• Diuretics do not treat AKI itself; use them for volume overload when appropriate.\n"
     "• Do not automatically discontinue every chronic cardiovascular medication in every patient.\n"
     "• Dialysis decisions should be based on the overall clinical picture and complications, not creatinine alone."),
    ("05 — DISPOSITION", "warning", 
     "• ICU for shock, severe hyperkalemia, refractory acidosis, pulmonary edema with respiratory compromise, or uremic complications.\n"
     "• Ensure repeat renal function and electrolyte testing and a clear medication review before discharge."),
    ("REFERENCES", "info", "KDIGO AKI Guidelines (2026); Local nephrology protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Hyperosmolar Hyperglycemic State (HHS)")] = [
    ("01 — RECOGNIZE", "info", 
     "HHS is a life-threatening hyperglycemic emergency characterized by severe hyperglycemia, hyperosmolality, and profound dehydration, typically with little or no significant ketoacidosis.\n"
     "• Polyuria, polydipsia, progressive dehydration.\n"
     "• Weakness, tachycardia, hypotension, reduced skin turgor.\n"
     "• Confusion, lethargy, seizures, or coma.\n"
     "• Often in older adults with type 2 diabetes.\n"
     "• Triggers: Infection, missed meds, stroke, MI, drugs."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, perfusion, degree of dehydration.\n"
     "• Check bedside glucose immediately.\n"
     "• Establish IV access; obtain electrolytes, renal function, blood gas, ketones, serum osmolality.\n"
     "• Start IV fluid replacement promptly, tailored to cardiac/renal status.\n"
     "• Measure potassium before insulin and correct significant hypokalemia first.\n"
     "• Identify and treat precipitating cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV fluid replacement[/color]\n"
     "• 0.9% NaCl or balanced crystalloid: initial rate 500–1,000 mL/hour for first 2–4 hours in adults without significant cardiac/renal compromise.\n"
     "• In older adults/HF/CKD: use smaller boluses (e.g., 250 mL) and reassess frequently.\n\n"
     "[color=#1E3A8A]B. Potassium management[/color]\n"
     "• If < 3.5 mmol/L: replace and delay insulin until > 3.5.\n"
     "• If 3.5–5.0: add K+ to IV fluids.\n"
     "• If > 5.0: do not add initially; recheck frequently.\n\n"
     "[color=#1E3A8A]C. Insulin therapy[/color]\n"
     "• Regular insulin IV at 0.05 units/kg/hour (for HHS without significant ketoacidosis).\n"
     "• If mixed DKA/HHS, use DKA pathway (0.1 units/kg/hour).\n"
     "• Add 5–10% dextrose when glucose < ~250 mg/dL.\n\n"
     "[color=#1E3A8A]D. Treat the precipitating cause[/color]\n"
     "• Treat infection, evaluate for MI/stroke, review meds. Provide thrombosis prevention."),
    ("04 — WARNINGS", "danger", 
     "• Excessively rapid osmotic shifts may cause neurologic complications.\n"
     "• Do not start insulin before addressing significant hypokalemia.\n"
     "• Mixed DKA/HHS requires a different insulin strategy."),
    ("05 — DISPOSITION", "warning", 
     "• ICU or equivalent high-dependency care for severe HHS, shock, altered consciousness, seizures, significant electrolyte disturbances, or critical illness."),
    ("REFERENCES", "info", "Umpierrez et al., Diabetes Care 2024; ADA Standards of Care 2026.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Severe Calcium Disorders: Hypercalcemia and Hypocalcemia")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Severe hypercalcemia[/color]\n"
     "• Total serum calcium commonly ≥14 mg/dL (3.5 mmol/L), especially when symptomatic.\n"
     "• Confusion, lethargy, coma, muscle weakness. Polyuria, dehydration, nausea, vomiting, constipation.\n"
     "• AKI, shortened QT interval, arrhythmias. Causes: malignancy, primary hyperparathyroidism.\n\n"
     "[color=#1E3A8A]Severe hypocalcemia[/color]\n"
     "• Perioral numbness, paresthesia, muscle cramps, carpopedal spasm.\n"
     "• Tetany, seizures, laryngospasm, altered mental status. Prolonged QT interval.\n"
     "• Causes: hypoparathyroidism, vitamin D deficiency, severe hypomagnesemia, pancreatitis, massive transfusion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and attach ECG monitoring if severe symptoms.\n"
     "• Check calcium, albumin, magnesium, phosphate, renal function, glucose.\n"
     "• Measure ionized calcium in critically ill patients or when albumin/pH makes total calcium difficult to interpret.\n"
     "• Obtain ECG and assess QT interval. Establish IV access.\n"
     "• Treat symptomatic severe hypocalcemia immediately.\n"
     "• For severe hypercalcemia, begin appropriate hydration if tolerated and identify cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Severe symptomatic hypocalcemia[/color]\n"
     "• Calcium gluconate 10%: 10–20 mL IV diluted in 50–100 mL of 0.9% NaCl or D5W over ~10 mins.\n"
     "• Repeat if severe symptoms/ECG abnormalities persist. Continuous infusion may be required.\n"
     "• Correct hypomagnesemia (can make hypocalcemia refractory).\n\n"
     "[color=#1E3A8A]B. Severe hypercalcemia[/color]\n"
     "• Isotonic IV crystalloid: 100–200 mL/hour after initial assessment (if hypovolemic).\n"
     "• Calcitonin: 4 international units/kg SC or IM every 12 hours (rapid, short-term adjunct).\n"
     "• Definitive: IV bisphosphonate or denosumab (especially malignancy-associated). Treat underlying cause."),
    ("04 — WARNINGS", "danger", 
     "• Rapid calcium administration may cause hypotension, bradycardia, or arrhythmias.\n"
     "• Calcium chloride contains more elemental calcium and is more damaging if extravasation occurs.\n"
     "• Do not force high-volume hydration in patients with pulmonary edema or severe heart failure.\n"
     "• Calcitonin effect is temporary (tachyphylaxis develops within 48–72 hours)."),
    ("05 — DISPOSITION", "warning", 
     "• ICU or monitored admission for severe symptoms, arrhythmias, seizures, marked calcium abnormalities, or organ dysfunction."),
    ("REFERENCES", "info", "Society for Endocrinology emergency guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Hypernatremia and Severe Water Deficit")] = [
    ("01 — RECOGNIZE", "info", 
     "Hypernatremia is a serum sodium concentration above 145 mmol/L and usually reflects a deficit of water relative to sodium.\n"
     "• Intense thirst, weakness, dehydration.\n"
     "• Confusion, irritability, lethargy, or seizures in severe cases.\n"
     "• Hypotension, tachycardia, and oliguria if intravascular volume depleted.\n"
     "• Causes: Inadequate water intake, GI losses, excessive sweating, osmotic diuresis, diabetes insipidus."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, circulation, mental status, volume status.\n"
     "• Check bedside glucose and serum electrolytes immediately.\n"
     "• If shock/severe hypovolemia: restore circulation first with isotonic crystalloid.\n"
     "• Determine if hypernatremia is acute or chronic.\n"
     "• Measure urine output. Begin controlled free-water replacement after initial stabilization.\n"
     "• Monitor sodium frequently to prevent overly rapid correction."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Initial circulatory resuscitation[/color]\n"
     "• If hypotensive/shock: 0.9% NaCl in reassessed boluses (e.g., 250–500 mL).\n"
     "• Do not use hypotonic fluid as the sole initial resuscitation fluid in shock.\n\n"
     "[color=#1E3A8A]B. Free-water replacement[/color]\n"
     "• Estimate water deficit: Total body water × [(serum Na / 140) − 1].\n"
     "• Oral/enteral free water preferred when safe. IV 5% dextrose provides free water. 0.45% NaCl may be appropriate.\n"
     "• For chronic/unknown duration: lower sodium by no more than ~10–12 mmol/L in 24 hours.\n"
     "• Check sodium every 4–6 hours during active correction.\n\n"
     "[color=#1E3A8A]C. Treat the cause[/color]\n"
     "• Replace GI losses, address inadequate intake, treat diabetes insipidus, manage hyperglycemia."),
    ("04 — WARNINGS", "danger", 
     "• Avoid unmonitored correction.\n"
     "• Do not rely on a calculated water deficit alone: ongoing urine and GI losses must also be replaced."),
    ("05 — DISPOSITION", "warning", 
     "• ICU or high-dependency care for severe neurologic symptoms, shock, very high sodium, or rapidly changing sodium.\n"
     "• Admit patients requiring IV correction or frequent laboratory monitoring."),
    ("REFERENCES", "info", "UpToDate (2026); NHS guidance; Local electrolyte protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Pancreatitis and Severe Pancreatitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Diagnosis requires at least 2 of 3:\n"
     "• Characteristic acute upper abdominal pain radiating to back.\n"
     "• Serum lipase/amylase ≥ 3 times upper limit of normal.\n"
     "• Imaging findings consistent with acute pancreatitis.\n"
     "• Assess for persistent vomiting, dehydration, tachycardia, hypotension, hypoxemia, AKI, altered mental status.\n"
     "• Severe pancreatitis = persistent organ failure lasting > 48 hours."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, hemodynamic stability, oxygenation, pain.\n"
     "• Establish IV access. Obtain lipase, CBC, electrolytes, renal function, liver tests, glucose, calcium, triglycerides.\n"
     "• Perform transabdominal ultrasound for gallstones/biliary dilation.\n"
     "• Begin moderately aggressive IV fluid resuscitation with frequent reassessment.\n"
     "• Provide analgesia and antiemetics.\n"
     "• Do not routinely prescribe prophylactic antibiotics for uncomplicated pancreatitis."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV fluids[/color]\n"
     "• Lactated Ringer's: ~1.5 mL/kg/hour, adjusted to volume status.\n"
     "• If hypovolemic, consider 10 mL/kg bolus over 1–2 hours, then reassess.\n"
     "• Avoid overly aggressive fluid administration (worsens respiratory failure).\n\n"
     "[color=#1E3A8A]B. Analgesia[/color]\n"
     "• IV opioid titrated to severity (e.g., morphine 2–4 mg IV).\n\n"
     "[color=#1E3A8A]C. Nutrition and cause-specific treatment[/color]\n"
     "• Oral feeding early as tolerated (low-fat solid diet). Enteral nutrition if oral not possible.\n"
     "• Urgent biliary drainage (ERCP) if cholangitis.\n"
     "• Cholecystectomy during same admission for mild gallstone pancreatitis.\n"
     "• Do not routinely perform early ERCP without cholangitis/obstruction."),
    ("04 — WARNINGS", "danger", 
     "• Avoid overly aggressive fluid administration in cardiac/renal impairment.\n"
     "• Analgesia should not delay evaluation of shock or other causes of abdominal pain.\n"
     "• Antibiotics not indicated for sterile pancreatic necrosis."),
    ("05 — DISPOSITION", "warning", 
     "• ICU for persistent organ failure, shock, respiratory failure, or severe metabolic abnormalities.\n"
     "• Monitor closely during first 48 hours because severity can evolve."),
    ("REFERENCES", "info", "ACG Guidelines: Management of Acute Pancreatitis (2024).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Cholangitis and Obstructive Jaundice")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute cholangitis is an infection of the biliary tree, commonly caused by obstruction of the common bile duct.\n"
     "• Fever or rigors. RUQ or epigastric pain. Jaundice.\n"
     "• Severe disease: hypotension, confusion, renal dysfunction, organ failure.\n"
     "• Classic triad (fever, pain, jaundice) is not always present. Suspect in biliary obstruction + sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and identify septic shock or organ dysfunction.\n"
     "• Obtain IV access, blood cultures, CBC, liver tests, renal function, electrolytes, lactate, coagulation.\n"
     "• Start appropriate IV antibiotics promptly. Give IV fluids according to perfusion.\n"
     "• Arrange urgent gastroenterology and surgical consultation.\n"
     "• Organize biliary drainage, usually by ERCP, according to severity."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Antibiotics[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (for selected community-acquired cases).\n"
     "• Broader therapy for severe sepsis/resistant organisms.\n\n"
     "[color=#1E3A8A]B. Sepsis resuscitation[/color]\n"
     "• For sepsis-induced hypoperfusion: up to 30 mL/kg IV within first 3 hours, with frequent reassessment.\n"
     "• Norepinephrine if hypotension persists despite fluids.\n\n"
     "[color=#1E3A8A]C. Biliary decompression[/color]\n"
     "• ERCP with biliary drainage is generally preferred. Severe cholangitis with shock requires urgent drainage after initial stabilization.\n"
     "• Percutaneous or surgical drainage if ERCP unavailable/unsuccessful."),
    ("04 — WARNINGS", "danger", 
     "• Antibiotics alone may not control infection when biliary obstruction persists.\n"
     "• Do not delay source control while repeatedly administering fluids to a patient who remains in shock."),
    ("05 — DISPOSITION", "warning", 
     "• ICU for septic shock, altered consciousness, respiratory failure, or other organ dysfunction.\n"
     "• Admit all suspected acute cholangitis for IV treatment and assessment for drainage."),
    ("REFERENCES", "info", "Tokyo Guidelines 2018; ACG Guidelines (2024).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Tumor Lysis Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Tumor lysis syndrome (TLS) results from rapid release of intracellular contents after cancer cell breakdown (spontaneously or after treatment).\n"
     "• Associated with high-grade lymphomas, acute leukemias, large tumor burden, elevated baseline uric acid, renal impairment.\n"
     "• Typical biochemical abnormalities: Hyperkalemia, hyperphosphatemia, hyperuricemia, secondary hypocalcemia.\n"
     "• AKI, arrhythmias, seizures, or sudden death."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, cardiac rhythm, renal function, neurologic status.\n"
     "• Attach ECG monitoring if significant potassium abnormalities or severe TLS suspected.\n"
     "• Obtain urgent electrolytes, calcium, phosphate, uric acid, creatinine, urea, LDH, glucose.\n"
     "• Start appropriate IV hydration if not contraindicated.\n"
     "• Treat dangerous hyperkalemia immediately.\n"
     "• Involve hematology and nephrology urgently."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV hydration[/color]\n"
     "• Preventive approach in high-risk patients: ~2–3 L/m²/day (individualized).\n"
     "• Established TLS requires individualized fluid management. Do not force hydration in oliguria/pulmonary edema.\n\n"
     "[color=#1E3A8A]B. Allopurinol (Prevention)[/color]\n"
     "• 100 mg/m² orally every 8 hours (max 800 mg/day) adjusted for renal function.\n\n"
     "[color=#1E3A8A]C. Rasburicase (Established hyperuricemia)[/color]\n"
     "• 0.15–0.2 mg/kg IV once, repeat per uric acid response/protocol.\n"
     "• [color=#991B1B]Contraindicated in G6PD deficiency (risk of hemolysis/methemoglobinemia).[/color]\n\n"
     "[color=#1E3A8A]D. Manage dangerous electrolyte abnormalities[/color]\n"
     "• Hyperkalemia: Emergency protocol (Calcium, Insulin/Glucose, definitive removal).\n"
     "• Hyperphosphatemia: Restrict intake, phosphate binders. Nephrology input for severe/refractory.\n"
     "• Hypocalcemia: Treat only if symptomatic or specific indication. Avoid unnecessary calcium (worsens calcium-phosphate precipitation)."),
    ("04 — WARNINGS", "danger", 
     "• Routine urine alkalinization with bicarbonate is not recommended for TLS prevention (worsens calcium-phosphate precipitation).\n"
     "• Rasburicase is contraindicated in G6PD deficiency.\n"
     "• Severe TLS may require urgent renal replacement therapy."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with established TLS to a monitored inpatient setting; ICU for severe electrolyte abnormalities, arrhythmias, seizures, shock, or significant renal failure."),
    ("REFERENCES", "info", "British Society for Haematology (2025); Local oncology protocols.")
]


# ==================== BATCH 10 (TOPICS 51-60) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Dengue Fever and Severe Dengue")] = [
    ("01 — RECOGNIZE", "info", 
     "Dengue is a mosquito-borne viral infection that may progress from a febrile illness to plasma leakage, shock, severe bleeding, or organ failure.\n"
     "• Fever, severe headache, retro-orbital pain, myalgia, arthralgia.\n"
     "• Nausea, vomiting, maculopapular rash, leukopenia, thrombocytopenia.\n\n"
     "[color=#991B1B]Warning Signs:[/color]\n"
     "• Severe/persistent abdominal pain. Persistent vomiting. Mucosal bleeding.\n"
     "• Lethargy, restlessness, altered mental status. Fluid accumulation (ascites/pleural effusion).\n"
     "• Hepatomegaly. Rising hematocrit with falling platelet count. Reduced urine output/narrowing pulse pressure.\n\n"
     "[color=#1E3A8A]Severe Dengue:[/color] Severe plasma leakage (shock/respiratory distress), severe bleeding, or severe organ impairment (hepatitis, encephalopathy, myocarditis, AKI).\n"
     "• Deterioration may occur as fever subsides (days 3–8)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, urine output.\n"
     "• Record BP, pulse pressure, cap refill, temperature, SpO2, weight.\n"
     "• Establish IV access if warning signs, shock, bleeding, or poor oral intake.\n"
     "• Obtain CBC with hematocrit/platelets. Assess for bleeding/fluid leakage.\n"
     "• Avoid unnecessary IM injections and invasive procedures if bleeding risk is high.\n"
     "• Activate resuscitation team for shock, respiratory distress, severe bleeding."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Without Warning Signs[/color]\n"
     "• Oral fluids/ORS. Paracetamol 500–1,000 mg orally every 6–8 hours (max daily limit).\n"
     "• [color=#991B1B]Avoid aspirin, NSAIDs, corticosteroids, prophylactic platelets.[/color]\n\n"
     "[color=#1E3A8A]B. With Warning Signs[/color]\n"
     "• Admit for observation. Monitor vitals, pulse pressure, fluid balance, urine output.\n"
     "• IV isotonic crystalloid (0.9% NaCl or Ringer's lactate) at ~5–7 mL/kg/hour for 1–2 hours, then reassess and reduce.\n"
     "• Avoid excessive IV fluids (risk of life-threatening pulmonary edema).\n\n"
     "[color=#1E3A8A]C. Severe Dengue / Shock[/color]\n"
     "• Initial crystalloid bolus 10–20 mL/kg over ~15–30 minutes depending on shock degree.\n"
     "• Reassess perfusion, pulse pressure, cap refill, mental status, urine output, lactate, hematocrit after each bolus.\n"
     "• If hematocrit falls while unstable, suspect significant bleeding. Do NOT repeat boluses automatically without reassessment.\n\n"
     "[color=#1E3A8A]D. Bleeding / Organ Failure[/color]\n"
     "• Transfuse PRBCs/whole blood for significant hemorrhage. Do NOT transfuse platelets solely for low count.\n"
     "• Treat AKI, hepatitis, encephalopathy, myocarditis per organ-support protocols."),
    ("04 — WARNINGS", "danger", 
     "• Excessive IV fluid administration can cause life-threatening pulmonary edema, particularly during recovery.\n"
     "• Deterioration may occur as fever subsides (days 3–8).\n"
     "• Do not use NSAIDs due to bleeding and renal risks."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for warning signs, significant comorbidities, pregnancy, inability to maintain oral hydration.\n"
     "• ICU for shock, respiratory distress, severe bleeding, altered consciousness, or severe organ dysfunction."),
    ("REFERENCES", "info", "WHO Guidelines for Clinical Management of Arboviral Diseases (2025); CDC Dengue (2026).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Chikungunya")] = [
    ("01 — RECOGNIZE", "info", 
     "Mosquito-borne viral illness characterized by abrupt fever and often severe, symmetric polyarthralgia.\n"
     "• Sudden high fever.\n"
     "• Severe pain in multiple joints (wrists, hands, ankles, feet). Joint swelling, difficulty walking/using hands.\n"
     "• Myalgia, headache, rash, fatigue. Persistent/recurrent joint symptoms for weeks/months.\n\n"
     "[color=#991B1B]Red Flags:[/color] Altered mental status, seizures, focal deficits. Chest pain, arrhythmia, myocarditis. Dyspnea, hypoxemia. Hypotension, AKI, severe dehydration, significant bleeding.\n"
     "• Dengue and chikungunya can present similarly. Do not assume severe arthralgia excludes dengue."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vitals, hydration, perfusion, mental status.\n"
     "• Evaluate for dengue, malaria, sepsis, leptospirosis.\n"
     "• [color=#991B1B]Avoid NSAIDs until dengue is reasonably excluded.[/color]\n"
     "• Admit for organ dysfunction, hemodynamic instability, severe dehydration, or inability to care for self."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fever and Pain[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours (within daily max).\n"
     "• Avoid aspirin/NSAIDs while dengue remains possible.\n\n"
     "[color=#1E3A8A]B. Hydration[/color]\n"
     "• Oral fluids/ORS. IV isotonic crystalloid for inadequate oral hydration or significant dehydration.\n\n"
     "[color=#1E3A8A]C. Persistent Joint Pain[/color]\n"
     "• After dengue excluded: Consider limited course of NSAID (lowest effective dose). Avoid in active bleeding, renal impairment, dehydration, peptic ulcer disease.\n\n"
     "[color=#1E3A8A]D. Severe Disease[/color]\n"
     "• Organ-specific supportive care for shock, myocarditis, encephalitis, AKI, respiratory failure."),
    ("04 — WARNINGS", "danger", 
     "• Do not routinely prescribe systemic corticosteroids during acute uncomplicated infection.\n"
     "• Persistent symptoms should prompt reassessment for alternative diagnoses and post-viral inflammatory arthritis."),
    ("05 — DISPOSITION", "warning", 
     "• Outpatient for stable patients who can maintain hydration and have reliable follow-up.\n"
     "• Consider admission for neonates, older adults with comorbidities, pregnancy, severe pain preventing mobility, or organ dysfunction."),
    ("REFERENCES", "info", "WHO Guidelines for Clinical Management of Arboviral Diseases (2025).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Malaria and Severe Malaria")] = [
    ("01 — RECOGNIZE", "info", 
     "Potentially fatal parasitic infection. Maintain a low threshold for testing in patients with fever and relevant exposure.\n"
     "• Fever, chills, sweating, headache, myalgia. Nausea, vomiting, weakness, abdominal discomfort.\n"
     "• Anemia, jaundice, thrombocytopenia, splenomegaly.\n\n"
     "[color=#1E3A8A]Severe Malaria Features:[/color] Impaired consciousness/coma, repeated seizures, severe anemia, hypoglycemia, metabolic acidosis, shock/bleeding, AKI/hemoglobinuria, pulmonary edema."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, consciousness, glucose immediately.\n"
     "• Perform malaria RDT and/or thick/thin films urgently.\n"
     "• Obtain IV access, CBC, electrolytes, renal/liver function, blood gas/lactate if severe.\n"
     "• Treat hypoglycemia immediately.\n"
     "• Do not delay treatment for suspected severe malaria while awaiting confirmatory results if suspicion is high.\n"
     "• Assess for bacterial sepsis/coinfections."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Severe Malaria[/color]\n"
     "• IV Artesunate: Adults/children ≥20 kg: 2.4 mg/kg at 0, 12, 24 hours, then every 24 hours.\n"
     "• Children < 20 kg: 3 mg/kg per dose.\n"
     "• Continue parenteral until oral meds tolerated (min 24 hours). Complete with full course of oral ACT.\n"
     "• Arrange follow-up for delayed hemolytic anemia.\n\n"
     "[color=#1E3A8A]B. Uncomplicated Falciparum Malaria[/color]\n"
     "• Artemisinin-based combination therapy (ACT), e.g., Artemether-lumefantrine (4 tablets per dose for ≥35 kg; 6 doses over 3 days). Administer with food/milk to improve absorption.\n\n"
     "[color=#1E3A8A]C. Hypoglycemia[/color]\n"
     "• Check bedside glucose immediately and repeat frequently. IV dextrose per protocol.\n\n"
     "[color=#1E3A8A]D. Fluids and Organ Support[/color]\n"
     "• Cautious, individualized fluid management (risk of pulmonary edema).\n"
     "• Treat seizures, acidosis, renal failure, anemia, respiratory failure per standard protocols."),
    ("04 — WARNINGS", "danger", 
     "• Severe malaria is a medical emergency requiring admission and close monitoring.\n"
     "• Do not use oral therapy alone for severe malaria.\n"
     "• Do not treat suspected malaria with an incomplete or unverified antimalarial regimen."),
    ("05 — DISPOSITION", "warning", 
     "• All severe malaria requires admission, urgent parenteral treatment, close monitoring (ICU).\n"
     "• Uncomplicated malaria outpatient only if tolerating oral therapy, no severe features, reliable follow-up."),
    ("REFERENCES", "info", "WHO Guidelines for Malaria (2026); National Malaria Protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Enteric Fever (Typhoid)")] = [
    ("01 — RECOGNIZE", "info", 
     "Systemic infection caused by Salmonella enterica serovars Typhi or Paratyphi.\n"
     "• Sustained fever, headache, malaise, anorexia. Abdominal pain, constipation, or diarrhea.\n"
     "• Hepatosplenomegaly. Relative bradycardia (not sensitive/specific).\n"
     "• Severe: encephalopathy, GI bleeding, intestinal perforation, shock.\n"
     "• Consider malaria, dengue, brucellosis, leptospirosis, bacterial sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess hemodynamic stability and screen for sepsis.\n"
     "• Look for peritonitis, GI bleeding, altered mental status, dehydration.\n"
     "• Obtain blood cultures before antibiotics when possible.\n"
     "• Review recent antibiotic exposure, travel, local resistance.\n"
     "• Start empiric treatment promptly in severe illness after cultures."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Antibiotic Therapy[/color]\n"
     "• Ceftriaxone: Adults 2 g IV every 24 hours (for hospitalized uncomplicated). Severe/complicated may require specialist-directed treatment.\n"
     "• Adjust according to culture/susceptibility.\n"
     "• Fluoroquinolones not used empirically where resistance is prevalent.\n\n"
     "[color=#1E3A8A]B. Supportive Care[/color]\n"
     "• Oral fluids if tolerated. IV isotonic crystalloid for significant dehydration/shock.\n"
     "• Correct electrolytes/glucose. Paracetamol for fever.\n"
     "• Avoid antimotility drugs in severe inflammatory diarrhea.\n\n"
     "[color=#1E3A8A]C. Perforation / Hemorrhage[/color]\n"
     "• Urgent surgical assessment, resuscitation, crossmatch, broad-spectrum IV antibiotics covering enteric organisms + anaerobes."),
    ("04 — WARNINGS", "danger", 
     "• Widal testing alone is not reliable to establish acute enteric fever.\n"
     "• A negative blood culture does not completely exclude the diagnosis (especially after prior antibiotics)."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for shock, severe dehydration, persistent vomiting, GI bleeding, suspected perforation, encephalopathy, inability to take oral therapy.\n"
     "• Outpatient only for stable patients with reliable follow-up and suitable oral regimen."),
    ("REFERENCES", "info", "WHO guidance on enteric fever; CDC Typhoid guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Cholera and Severe Dehydration")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute intestinal infection causing profuse watery diarrhea, rapid dehydration, hypovolemic shock, and death if fluids not replaced.\n"
     "• Sudden profuse watery diarrhea. Vomiting, muscle cramps.\n"
     "• Thirst, dry mucous membranes, sunken eyes, reduced skin turgor.\n"
     "• Tachycardia, weak pulse, hypotension, delayed cap refill, oliguria/anuria.\n"
     "• Do NOT wait for laboratory confirmation before rehydrating."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess circulation, mental status, pulse, BP, cap refill, urine output.\n"
     "• Estimate dehydration degree. Start immediate rehydration.\n"
     "• Use ORS as soon as patient can drink safely.\n"
     "• Implement infection-prevention measures and outbreak notification.\n"
     "• Obtain electrolytes/renal function in severe dehydration when available."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Severe Dehydration / Shock[/color]\n"
     "• Ringer's lactate preferred (or appropriate isotonic crystalloid).\n"
     "• WHO Plan C: 100 mL/kg total over 3 hours (≥1 year) or 6 hours (<1 year), with first 30 mL/kg delivered more rapidly.\n"
     "• Replace ongoing stool/vomit losses. Start ORS as soon as safe.\n\n"
     "[color=#1E3A8A]B. Oral Rehydration Solution (ORS)[/color]\n"
     "• Frequent small amounts as tolerated. Replace ongoing stool losses.\n\n"
     "[color=#1E3A8A]C. Antibiotics[/color]\n"
     "• Adjunct for severe cholera (never replace rehydration). Doxycycline or azithromycin (if susceptible/appropriate).\n\n"
     "[color=#1E3A8A]D. Additional Care[/color]\n"
     "• Continue feeding/breastfeeding. Correct electrolyte abnormalities. Monitor for AKI/hypoglycemia. Zinc in children."),
    ("04 — WARNINGS", "danger", 
     "• Avoid hypotonic solutions as initial resuscitation fluid for hypovolemic shock.\n"
     "• Reassess frequently in patients with heart failure or renal impairment."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for severe dehydration, shock, persistent vomiting, electrolyte disturbance, AKI.\n"
     "• Mild/no dehydration may be treated with ORS and return precautions."),
    ("REFERENCES", "info", "WHO cholera treatment and outbreak management guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Carbon Monoxide (CO) Poisoning")] = [
    ("01 — RECOGNIZE", "info", 
     "CO is a colorless, odorless gas causing tissue hypoxia/cellular toxicity.\n"
     "• Sources: Generators/heaters indoors, charcoal, fires/smoke, vehicle exhaust.\n"
     "• Headache, dizziness, weakness, nausea, vomiting, confusion, impaired coordination.\n"
     "• Chest pain, arrhythmias, myocardial ischemia. Seizures, syncope, coma, cardiac arrest.\n"
     "• Suspect when several people in same environment develop symptoms.\n"
     "• [color=#991B1B]A normal conventional pulse oximeter does NOT exclude CO poisoning.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Remove from exposure without endangering rescuers.\n"
     "• Administer 100% oxygen immediately.\n"
     "• Assess ABCs, mental status, glucose. Obtain IV access and continuous ECG monitoring.\n"
     "• Contact poison center/hyperbaric service for severe poisoning.\n"
     "• Assess for concurrent burns, smoke inhalation, cyanide toxicity."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. High-Concentration Oxygen[/color]\n"
     "• 100% oxygen via non-rebreather mask. If airway inadequate, assist ventilation/intubate.\n"
     "• Continue oxygen until symptoms resolve and assessment supports stopping (often ~4–5 hours).\n"
     "• Do not withhold oxygen while waiting for lab results.\n\n"
     "[color=#1E3A8A]B. Hyperbaric Oxygen (HBO) Assessment[/color]\n"
     "• Consider for COHb ~25–30%+, LOC/neurological impairment, cardiac ischemia, severe acidosis, pregnancy.\n\n"
     "[color=#1E3A8A]C. Severe Poisoning[/color]\n"
     "• Manage seizures, shock, myocardial ischemia per protocols. Intubate for coma/airway compromise."),
    ("04 — WARNINGS", "danger", 
     "• Conventional pulse oximetry cannot reliably distinguish oxyhemoglobin from carboxyhemoglobin.\n"
     "• COHb may be deceptively low if oxygen was administered before sampling."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for LOC, persistent neuro abnormalities, cardiac injury, severe acidosis, ongoing symptoms.\n"
     "• Discharged patients need clear instructions about delayed neurological symptoms."),
    ("REFERENCES", "info", "CDC CO Poisoning Guidance (2026); UHMS Guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Guillain–Barré Syndrome (GBS)")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute immune-mediated peripheral neuropathy causing rapidly progressive weakness, autonomic instability, respiratory failure.\n"
     "• Progressive, usually symmetric limb weakness. Reduced/absent deep tendon reflexes.\n"
     "• Paresthesia/neuropathic pain. Recent respiratory/GI infection. Facial weakness, dysphagia.\n\n"
     "[color=#991B1B]Red Flags:[/color] Rapidly ascending weakness. Weak cough/difficulty clearing secretions. Dysphagia/dysarthria/aspiration. Neck flexor weakness. Declining FVC. Marked BP fluctuations/arrhythmias."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Admit for close monitoring.\n"
     "• Assess airway protection, swallowing, cough strength, limb power, cranial nerves.\n"
     "• Measure FVC and inspiratory pressure. Repeat every 4 hours if rapidly progressing.\n"
     "• Obtain ECG, monitor BP/rhythm.\n"
     "• Early neurology/ICU consult for progression, bulbar dysfunction, respiratory compromise."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Respiratory/Autonomic Monitoring[/color]\n"
     "• Serial FVC, respiratory effort, cough, bulbar function. Continuous ECG/BP in severe cases.\n"
     "• Consider early elective intubation when respiratory function deteriorates (FVC ~20 mL/kg or lower, or rapidly falling).\n\n"
     "[color=#1E3A8A]B. IVIG[/color]\n"
     "• 0.4 g/kg/day IV for 5 days (total 2 g/kg). Infuse slowly, monitor renal function/thrombotic risk.\n"
     "• IVIG and plasma exchange are alternative disease-modifying treatments. Do NOT routinely do plasma exchange immediately followed by IVIG.\n"
     "• Corticosteroids are NOT recommended as routine treatment.\n\n"
     "[color=#1E3A8A]C. Plasma Exchange[/color]\n"
     "• 4–5 exchanges over 1–2 weeks under specialist supervision.\n\n"
     "[color=#1E3A8A]D. Supportive Care[/color]\n"
     "• VTE prophylaxis, pressure injury prevention, nutritional support, aspiration precautions, pain management, rehab."),
    ("04 — WARNINGS", "danger", 
     "• Do not wait for hypoxemia or respiratory arrest before escalating care.\n"
     "• CSF protein may be normal early. Normal early CSF does not exclude GBS."),
    ("05 — DISPOSITION", "warning", 
     "• Generally require hospital admission. ICU for declining respiratory function, bulbar dysfunction, rapidly progressive weakness, or severe autonomic instability."),
    ("REFERENCES", "info", "EAN/PNS GBS Guideline (2023).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Myasthenic Crisis")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe worsening of myasthenia gravis causing respiratory muscle weakness and impending/established respiratory failure.\n"
     "• Fluctuating muscle weakness. Ptosis, diplopia.\n"
     "• Dysarthria, dysphagia, weak cough. Neck flexor weakness.\n"
     "• Difficulty counting in one breath/speaking full sentences. Shallow breathing, orthopnea, inability to clear secretions.\n"
     "• Precipitants: Respiratory infection, aspiration, surgery, medication changes, drugs impairing neuromuscular transmission."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Admit to monitored setting, involve ICU/neurology early.\n"
     "• Assess respiratory effort, bulbar function, cough strength, secretion handling.\n"
     "• Measure FVC and inspiratory pressure serially.\n"
     "• Prepare for intubation if respiratory function deteriorating.\n"
     "• Identify/treat triggers (infection). Review meds for exacerbating agents."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Airway and Ventilation[/color]\n"
     "• Intubate for progressive respiratory fatigue, severe bulbar dysfunction, inability to protect airway, or inadequate ventilation.\n"
     "• Noninvasive ventilation only in selected patients who can protect airway; must not delay intubation.\n\n"
     "[color=#1E3A8A]B. IVIG[/color]\n"
     "• 0.4 g/kg/day IV for 5 days (total 2 g/kg). Monitor for infusion reactions, thrombosis, renal injury.\n\n"
     "[color=#1E3A8A]C. Plasma Exchange[/color]\n"
     "• Alternative rapid immunomodulatory treatment (several exchanges over 1–2 weeks).\n\n"
     "[color=#1E3A8A]D. Pyridostigmine / Other Meds[/color]\n"
     "• May be temporarily withheld/adjusted during intubated crisis (can increase secretions).\n"
     "• Corticosteroid initiation/escalation requires specialist planning (early transient worsening risk)."),
    ("04 — WARNINGS", "danger", 
     "• Avoid waiting for hypercapnia, severe hypoxemia, or respiratory arrest.\n"
     "• Succinylcholine and nondepolarizing neuromuscular blockers may have unpredictable effects in myasthenia."),
    ("05 — DISPOSITION", "warning", 
     "• Impending/established myasthenic crisis requires ICU or equivalent high-dependency monitoring."),
    ("REFERENCES", "info", "International/Regional Consensus Guidelines for Myasthenia Gravis (2023, 2025).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Infective Endocarditis with Acute Complications")] = [
    ("01 — RECOGNIZE", "info", 
     "Infection of endocardial surface, usually heart valve. May cause sepsis, acute valve failure, embolic events, conduction abnormalities.\n"
     "• Fever + new/changing murmur. Persistent bacteremia/unexplained sepsis.\n"
     "• Prosthetic valves/intracardiac devices. Previous endocarditis. Injection drug use.\n"
     "• Embolic stroke, splenic infarction, systemic emboli. New heart failure or conduction abnormalities.\n\n"
     "[color=#1E3A8A]Life-Threatening Complications:[/color] Acute severe mitral/aortic regurgitation, pulmonary edema, cardiogenic shock, perivalvular abscess/new AV block, stroke/ICH, persistent bacteremia/septic shock."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess sepsis, hemodynamic status, heart failure, neurological deficits.\n"
     "• Obtain blood cultures before antibiotics when feasible without delaying urgent treatment.\n"
     "• Urgent echocardiography (TEE when indicated).\n"
     "• Involve cardiology, infectious disease, microbiology, cardiac surgery early for severe disease.\n"
     "• Avoid delaying surgery assessment in acute valve failure."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Empiric Antibiotics[/color]\n"
     "• Choose based on native vs prosthetic valve, community vs healthcare-associated, prior antibiotics, likely pathogens, renal function, local resistance.\n"
     "• In severe sepsis, administer promptly after cultures.\n"
     "• Narrow when cultures/susceptibilities available.\n\n"
     "[color=#1E3A8A]B. Acute Heart Failure / Cardiogenic Shock[/color]\n"
     "• Oxygen/ventilatory support. Cautious hemodynamic support tailored to valve lesion/shock phenotype.\n"
     "• Avoid indiscriminate fluid boluses in severe acute valve regurgitation/pulmonary edema.\n"
     "• Immediate cardiothoracic surgical assessment for acute severe valve dysfunction.\n\n"
     "[color=#1E3A8A]C. Embolic/Neurological Complications[/color]\n"
     "• Activate appropriate stroke/neuro pathway. Urgently assess ICH/infectious aneurysm.\n"
     "• Anticoagulation is NOT routinely initiated solely to prevent septic emboli.\n\n"
     "[color=#1E3A8A]D. Surgical Assessment[/color]\n"
     "• Urgent for HF from valve dysfunction, uncontrolled infection, large vegetations with embolic risk, prosthetic valve/device infection."),
    ("04 — WARNINGS", "danger", 
     "• There is no single empiric regimen appropriate for every endocarditis presentation.\n"
     "• Do not delay life-saving treatment in unstable patients while awaiting cultures."),
    ("05 — DISPOSITION", "warning", 
     "• Suspected IE requires hospital assessment/admission. Shock, acute HF, conduction block, neuro complications, or persistent bacteremia require urgent specialist management/ICU."),
    ("REFERENCES", "info", "2023 ESC Guidelines for the Management of Endocarditis.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Sickle Cell Acute Chest Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute chest syndrome (ACS) is a potentially fatal complication of sickle cell disease, characterized by a new pulmonary infiltrate + fever and/or respiratory symptoms.\n"
     "• Chest pain, cough, fever, dyspnea. Hypoxemia/increasing O2 requirement.\n"
     "• Tachypnea, increased work of breathing. Falling hemoglobin or rapidly worsening respiratory status.\n"
     "• Mechanisms: infection, pulmonary vaso-occlusion, fat embolism, hypoventilation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Admit, assess respiratory distress and oxygenation.\n"
     "• Give supplemental oxygen if hypoxemic. Obtain chest radiography, CBC with reticulocytes.\n"
     "• Assess for pneumonia, PE, other causes of deterioration.\n"
     "• Provide prompt analgesia while avoiding excessive sedation.\n"
     "• Involve hematology/critical care early for progressive hypoxemia/severe disease.\n"
     "• Encourage incentive spirometry in appropriate patients."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Oxygen/Respiratory Support[/color]\n"
     "• Correct hypoxemia. Escalate to high-flow O2, NIV, or invasive ventilation if indicated.\n\n"
     "[color=#1E3A8A]B. Antibiotics[/color]\n"
     "• Empiric regimen covering typical/atypical respiratory pathogens per local guidelines.\n\n"
     "[color=#1E3A8A]C. Analgesia/Pulmonary Care[/color]\n"
     "• Appropriate analgesia (opioids if needed) with careful respiratory monitoring.\n"
     "• Avoid excessive sedation/hypoventilation. Incentive spirometry, mobilization.\n"
     "• Cautious fluid management (avoid dehydration but prevent fluid overload).\n\n"
     "[color=#1E3A8A]D. Red Cell Transfusion[/color]\n"
     "• Simple transfusion: clinically significant anemia or worsening oxygenation.\n"
     "• Exchange transfusion: urgently for severe/rapidly progressive ACS, increasing O2 requirement, multilobar disease.\n"
     "• Discuss with hematology/transfusion service. Avoid excessive post-transfusion hemoglobin elevation (hyperviscosity risk)."),
    ("04 — WARNINGS", "danger", 
     "• All suspected ACS cases require hospital admission.\n"
     "• Transfusion decisions depend on severity and baseline hemoglobin; do not use a single threshold in isolation."),
    ("05 — DISPOSITION", "warning", 
     "• ICU care for progressive hypoxemia, increasing respiratory support, hemodynamic instability, or other organ failure."),
    ("REFERENCES", "info", "ASH transfusion guidelines; BSH guidance; CDC ACS in SCD.")
]


# ==================== BATCH 11 (TOPICS 61-70) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Angioedema with Airway Compromise")] = [
    ("01 — RECOGNIZE", "info", 
     "Angioedema is sudden swelling of the deeper skin or mucosa. It may be histamine-mediated or bradykinin-mediated.\n"
     "• Triggers: ACE inhibitors, foods, insect stings, medications, hereditary/acquired C1-inhibitor deficiency.\n\n"
     "[color=#991B1B]Features Suggesting Airway Threat:[/color]\n"
     "• Tongue, floor-of-mouth, or pharyngeal swelling.\n"
     "• Hoarse voice, voice change. Stridor, drooling, difficulty swallowing secretions.\n"
     "• Progressive swelling or respiratory distress.\n"
     "• Swelling of tongue/larynx can threaten airway even without urticaria or hypotension."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call airway, anesthesia, and critical care teams early.\n"
     "• Assess voice, tongue, oropharynx, respiratory effort, ability to handle secretions.\n"
     "• Prepare for early definitive airway management if swelling is progressing.\n"
     "• Give IM epinephrine immediately if anaphylaxis or histamine-mediated airway involvement is suspected.\n"
     "• Stop a suspected causative medication (especially ACE inhibitor).\n"
     "• Establish IV access and continuously monitor SpO2, ECG, BP."),
    ("03 — INVESTIGATIONS", "info", 
     "• Diagnosis is primarily clinical.\n"
     "• Flexible nasolaryngoscopy by experienced clinician may help assess laryngeal involvement if stable.\n"
     "• C4 and C1-inhibitor concentration/function may help investigate hereditary/acquired angioedema after stabilization.\n"
     "• Serum tryptase may support suspected anaphylaxis, but treatment must not wait for result."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Suspected Histamine-Mediated Angioedema/Anaphylaxis[/color]\n"
     "• Epinephrine: 0.3–0.5 mg IM (1 mg/mL preparation) into mid-anterolateral thigh. Repeat every 5–15 minutes if symptoms persist.\n"
     "• Provide oxygen and IV isotonic crystalloid if indicated.\n"
     "• Do NOT delay IM epinephrine for antihistamines or corticosteroids.\n\n"
     "[color=#1E3A8A]B. Suspected Bradykinin-Mediated Angioedema[/color]\n"
     "• Features: No urticaria/itching, ACE-inhibitor exposure, recurrent episodes, poor response to allergy meds.\n"
     "• Prioritize airway protection. Stop ACE inhibitor permanently when implicated.\n"
     "• For hereditary angioedema: C1-inhibitor concentrate or icatibant according to availability/protocol.\n"
     "• Epinephrine, antihistamines, and corticosteroids may be ineffective in bradykinin-mediated angioedema."),
    ("05 — WARNINGS", "danger", 
     "• If mechanism is uncertain and anaphylaxis remains plausible, treat anaphylaxis while managing the airway.\n"
     "• IV epinephrine boluses are not routine treatment for anaphylaxis."),
    ("06 — DISPOSITION", "warning", 
     "• Admit to ICU or closely monitored setting for laryngeal involvement, progressive tongue swelling, respiratory compromise, or airway intervention."),
    ("REFERENCES", "info", "World Allergy Organization; International Hereditary Angioedema Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Myocarditis and Fulminant Myocarditis")] = [
    ("01 — RECOGNIZE", "info", 
     "Myocarditis is inflammation of the myocardium that may present with chest pain, arrhythmias, heart failure, or cardiogenic shock.\n"
     "• Chest pain resembling ACS. Dyspnea, fatigue, or new heart failure.\n"
     "• Palpitations, syncope, or ventricular arrhythmias. Recent viral/systemic illness.\n"
     "• Elevated troponin with or without ECG changes.\n\n"
     "[color=#991B1B]High-Risk Features:[/color] Hypotension/cardiogenic shock, sustained VT/VF, high-grade AV block, rapidly declining ventricular function, severe hypoxemia/pulmonary edema."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, mental status. Obtain ECG, cardiac biomarkers, bedside echocardiography.\n"
     "• Monitor continuously for arrhythmias/conduction abnormalities.\n"
     "• Treat shock according to hemodynamic phenotype.\n"
     "• Avoid strenuous physical activity.\n"
     "• Obtain urgent cardiology/critical care consultation if dysfunction, arrhythmias, or shock."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Hemodynamic Support[/color]\n"
     "• Treat hypoxemia/respiratory failure. Assess fluid responsiveness carefully; avoid indiscriminate fluid loading.\n"
     "• Use vasopressors/inotropes for shock. Consider temporary mechanical circulatory support for refractory cardiogenic shock.\n"
     "• Fulminant myocarditis can be reversible; early escalation to an advanced cardiac center may be lifesaving.\n\n"
     "[color=#1E3A8A]B. Arrhythmias and Conduction Disease[/color]\n"
     "• Treat unstable tachyarrhythmias per ACLS. Correct K+/Mg2+. Manage high-grade heart block with pacing as indicated.\n\n"
     "[color=#1E3A8A]C. Disease-Specific Treatment[/color]\n"
     "• Standard HF treatment when tolerated. Avoid routine immunosuppression for presumed viral myocarditis without specific indication."),
    ("04 — WARNINGS", "danger", 
     "• A normal initial echocardiogram does not exclude myocarditis.\n"
     "• Avoid indiscriminate fluid loading in ventricular dysfunction."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with suspected clinically significant myocarditis for cardiac assessment.\n"
     "• ICU for shock, sustained ventricular arrhythmias, high-grade heart block, or rapidly deteriorating ventricular function."),
    ("REFERENCES", "info", "2025 ESC Guidelines for the Management of Myocarditis and Pericarditis.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Pulmonary–Renal Syndrome and Diffuse Alveolar Hemorrhage")] = [
    ("01 — RECOGNIZE", "info", 
     "Pulmonary–renal syndrome is a life-threatening combination of pulmonary capillary injury (often causing diffuse alveolar hemorrhage) and rapidly progressive glomerulonephritis.\n"
     "• Causes: ANCA-associated vasculitis, anti-GBM disease, SLE, infections, drug reactions.\n"
     "• Dyspnea, cough, hypoxemia, or hemoptysis. Falling hemoglobin. Bilateral pulmonary infiltrates.\n"
     "• AKI, hematuria, proteinuria. Red cell casts on urine microscopy.\n"
     "• [color=#991B1B]Diffuse alveolar hemorrhage can occur without obvious hemoptysis.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess respiratory failure, hemodynamic stability, degree of bleeding.\n"
     "• Provide oxygen and escalate respiratory support as required.\n"
     "• Obtain urgent nephrology, respiratory, and critical care consultation.\n"
     "• Check CBC, renal function, coagulation, urinalysis, blood gas.\n"
     "• Send autoimmune testing and microbiological samples promptly.\n"
     "• Consider early intubation for worsening hypoxemia, exhaustion, or inability to protect airway."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Respiratory Support[/color]\n"
     "• Oxygen, high-flow oxygen, or mechanical ventilation as required. Use lung-protective ventilation if ARDS develops.\n\n"
     "[color=#1E3A8A]B. Suspected Severe Immune-Mediated Disease[/color]\n"
     "• Organ-threatening ANCA-associated vasculitis or anti-GBM disease: urgent induction may include IV glucocorticoids + rituximab or cyclophosphamide.\n"
     "• Anti-GBM disease generally requires urgent specialist assessment for plasma exchange alongside immunosuppression.\n"
     "• Monitor glucose, BP, CBC, renal function, and infection.\n\n"
     "[color=#1E3A8A]C. Acute Kidney Injury[/color]\n"
     "• Monitor fluid balance, K+, acid-base, urine output. Treat hyperkalemia. Arrange RRT for standard indications."),
    ("04 — WARNINGS", "danger", 
     "• Do not start high-dose immunosuppression indiscriminately in undifferentiated pulmonary infiltrates; infection and other causes of hemorrhage must be evaluated urgently.\n"
     "• Plasma exchange is not routinely indicated for every patient with ANCA-associated vasculitis."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to ICU for severe hypoxemia, rapidly progressive pulmonary hemorrhage, shock, or severe metabolic complications."),
    ("REFERENCES", "info", "KDIGO Guidelines for ANCA-Associated Vasculitis and anti-GBM disease.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Hemolytic Transfusion Reaction")] = [
    ("01 — RECOGNIZE", "info", 
     "An acute hemolytic transfusion reaction may occur when transfused red cells are destroyed rapidly, commonly because of ABO incompatibility.\n"
     "• Fever, chills, or rigors. Back, flank, chest, or infusion-site pain.\n"
     "• Hypotension, tachycardia, or dyspnea. Dark urine or hemoglobinuria.\n"
     "• Unexpected bleeding or oozing. Rapid deterioration or unexplained shock.\n"
     "• Consider other reactions (bacterial contamination, anaphylaxis, TRALI)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• [color=#991B1B]STOP the transfusion immediately.[/color]\n"
     "• Maintain IV access using new tubing and compatible isotonic fluid per protocol.\n"
     "• Assess ABCs. Recheck patient identity and blood product details.\n"
     "• Notify blood bank and treating senior clinician immediately.\n"
     "• Send blood bag and tubing for investigation. Do NOT restart the implicated blood unit."),
    ("03 — INVESTIGATIONS", "info", 
     "• Repeat patient/blood-product identity checks. Direct antiglobulin test (DAT).\n"
     "• CBC and serial hemoglobin. Plasma free hemoglobin, bilirubin, LDH, haptoglobin.\n"
     "• Renal function, potassium, urinalysis. PT/INR, aPTT, fibrinogen, platelets if DIC suspected.\n"
     "• Blood cultures from patient and product if bacterial contamination suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Supportive Resuscitation[/color]\n"
     "• Oxygen, careful IV crystalloid, and vasopressors for hypotension. Monitor ECG, BP, SpO2, urine output, renal function.\n\n"
     "[color=#1E3A8A]B. Kidney Protection[/color]\n"
     "• Monitor urine output, creatinine, K+, acid-base. Maintain renal perfusion while avoiding fluid overload. Treat hyperkalemia promptly. Arrange dialysis for standard indications.\n\n"
     "[color=#1E3A8A]C. Disseminated Intravascular Coagulation[/color]\n"
     "• Monitor platelets, coagulation, fibrinogen. Treat underlying reaction and support circulation. Use blood components per active bleeding/procedures.\n\n"
     "[color=#1E3A8A]D. Reporting and Prevention[/color]\n"
     "• Document suspected reaction. Preserve implicated product/samples. Formally report and investigate."),
    ("05 — WARNINGS", "danger", 
     "• Do not give fluids without reassessment in patients with heart failure or pulmonary edema.\n"
     "• Diuretics are not a substitute for adequate resuscitation."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected acute hemolysis, hypotension, hemoglobinuria, renal injury, coagulopathy, or other systemic complications."),
    ("REFERENCES", "info", "AABB Transfusion-Reaction Guidance; BSH Transfusion Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "High-Altitude Pulmonary Edema (HAPE)")] = [
    ("01 — RECOGNIZE", "info", 
     "HAPE is a potentially fatal form of noncardiogenic pulmonary edema that occurs after rapid ascent to high altitude without adequate acclimatization (generally > 2,500–3,000 m).\n"
     "• Early: Reduced exercise tolerance, exaggerated breathlessness on exertion, dry cough, chest tightness, unusual fatigue.\n"
     "• Progressive: Dyspnea at rest, marked tachypnea/tachycardia, cough with pink/blood-stained sputum, crackles, hypoxemia, cyanosis, confusion.\n"
     "• Consider pneumonia, PE, asthma, cardiogenic pulmonary edema."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop ascent and minimize exertion.\n"
     "• Give supplemental oxygen immediately.\n"
     "• [color=#991B1B]Arrange descent to a lower altitude as soon as safely possible.[/color]\n"
     "• Keep the patient warm and avoid unnecessary exertion.\n"
     "• Use a portable hyperbaric chamber if descent is impossible and available."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Oxygen and Descent[/color]\n"
     "• Give supplemental O2 sufficient to improve oxygenation and symptoms (aim SpO2 > 90%).\n"
     "• Descend promptly (generally at least 1,000 m or until substantial clinical improvement).\n"
     "• Descent and oxygen are the primary treatments; do not delay them for imaging/labs.\n\n"
     "[color=#1E3A8A]B. Nifedipine[/color]\n"
     "• Consider only when descent is delayed/impossible and oxygen/HBO unavailable/inadequate.\n"
     "• Extended-release nifedipine 30 mg PO every 12 hours (or 20 mg every 8 hours) per protocol.\n"
     "• Avoid rapid-release sublingual nifedipine. Use caution in hypotension/shock.\n\n"
     "[color=#1E3A8A]C. Respiratory Support[/color]\n"
     "• Escalate to high-flow O2 or positive-pressure ventilation when necessary. Transfer severe cases to critical care."),
    ("04 — WARNINGS", "danger", 
     "• Nifedipine is not a substitute for descent and oxygen.\n"
     "• Do not delay descent and oxygen while obtaining imaging or laboratory results."),
    ("05 — DISPOSITION", "warning", 
     "• All suspected HAPE cases require urgent medical assessment and descent.\n"
     "• Severe hypoxemia, respiratory distress, confusion, or failure to improve requires emergency evacuation and hospital admission."),
    ("REFERENCES", "info", "CDC Yellow Book; Wilderness Medical Society Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Spinal Cord Compression")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute spinal cord compression is a time-critical emergency caused by pressure on the spinal cord (metastatic tumors, epidural abscess, hematoma, trauma).\n"
     "• Severe/progressive neck or back pain. Radicular pain radiating to limbs.\n"
     "• Limb weakness or progressive paralysis. Sensory loss, sensory level, paresthesia.\n"
     "• Hyperreflexia/pathological reflexes. New bladder/bowel dysfunction. Gait disturbance.\n\n"
     "[color=#991B1B]Red Flags:[/color] Known cancer with new severe back pain, fever/bacteremia/immunosuppression with spinal pain, recent spinal procedure/trauma, rapidly progressive deficits, new urinary retention/saddle sensory disturbance."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, neurological status. Document limb power, sensation, reflexes, bladder function.\n"
     "• Maintain spinal precautions if traumatic instability suspected.\n"
     "• Arrange emergency MRI of relevant spine.\n"
     "• Obtain urgent neurosurgical/spinal surgical consultation.\n"
     "• If metastatic cord compression suspected with neuro signs, initiate specialist-directed emergency management without waiting for deterioration."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Suspected Metastatic Spinal Cord Compression[/color]\n"
     "• Dexamethasone 16 mg PO or IV promptly, followed by 16 mg daily while awaiting definitive treatment per protocol.\n"
     "• Monitor glucose, mental status, infection risk, GI effects. Arrange urgent MRI and definitive oncology/surgical assessment.\n\n"
     "[color=#1E3A8A]B. Suspected Spinal Epidural Abscess[/color]\n"
     "• Blood cultures promptly. Start empiric IV antibiotics covering Staph aureus per local resistance. Arrange emergency surgical assessment for neuro deficits/compression.\n"
     "• Do not delay antibiotics in septic/unstable patient.\n\n"
     "[color=#1E3A8A]C. Traumatic Compression or Spinal Hematoma[/color]\n"
     "• Maintain spinal precautions. Reverse anticoagulation if indicated. Arrange urgent spinal surgical evaluation.\n"
     "• Avoid routine high-dose methylprednisolone unless specialist protocol supports."),
    ("04 — WARNINGS", "danger", 
     "• Dexamethasone regimen applies to suspected metastatic cord compression, not every cause of spinal pain.\n"
     "• Do not delay surgery/radiotherapy assessment while administering steroids."),
    ("05 — DISPOSITION", "warning", 
     "• Admit urgently. Progressive weakness, respiratory involvement, severe compression, or suspected epidural abscess requires emergency specialist management and often ICU."),
    ("REFERENCES", "info", "NICE NG234; NICE Spinal Injury; Local protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Cauda Equina Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Cauda equina syndrome (CES) results from compression of lumbosacral nerve roots (commonly large lumbar disc herniation). May cause permanent bladder, bowel, sexual, and lower-limb dysfunction.\n"
     "• New urinary retention, difficulty initiating urination, loss of awareness of bladder filling.\n"
     "• New urinary/fecal incontinence. Saddle/perineal numbness. Bilateral sciatica or leg weakness.\n"
     "• Reduced anal sensation. New sexual dysfunction.\n"
     "• [color=#991B1B]No single symptom or exam finding reliably excludes CES.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat suspected CES as a time-critical neurological emergency.\n"
     "• Document onset/progression of urinary, bowel, sensory, motor symptoms.\n"
     "• Perform focused lower-limb neuro exam. Assess perineal sensation when appropriate with consent.\n"
     "• Measure post-void residual bladder volume (low residual does NOT reliably exclude CES).\n"
     "• Arrange emergency lumbar MRI and urgent spinal surgical consultation. Do NOT delay MRI."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Confirmed Compressive CES[/color]\n"
     "• Arrange urgent decompression by spinal surgical team. Goal is to relieve compression as quickly as safely possible.\n"
     "• Document neurological status before and after intervention.\n\n"
     "[color=#1E3A8A]B. Bladder Management[/color]\n"
     "• Catheterize for acute urinary retention when indicated. Monitor renal function/urine output. Avoid assuming catheterization treats the emergency.\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• Analgesia, safe mobility/fall precautions, bowel function/pressure injury risk assessment. Arrange rehab/bladder/bowel follow-up."),
    ("04 — WARNINGS", "danger", 
     "• Do not postpone surgical consultation while trying analgesics, physiotherapy, or outpatient investigations.\n"
     "• There is no universally safe delay that can be applied to every patient."),
    ("05 — DISPOSITION", "warning", 
     "• All suspected CES require emergency assessment and usually emergency MRI. Confirmed compression requires urgent spinal surgical management and inpatient care."),
    ("REFERENCES", "info", "HSE National Clinical Guideline (2025); NHS England Pathway (2025).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Angle-Closure Glaucoma")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute angle-closure glaucoma is a sight-threatening ophthalmic emergency caused by sudden increase in intraocular pressure due to impaired aqueous humor drainage.\n"
     "• Severe unilateral eye pain. Blurred vision or colored halos.\n"
     "• Headache, nausea, vomiting. Red eye with hazy cornea.\n"
     "• Mid-dilated, poorly reactive pupil. Markedly elevated IOP.\n"
     "• May be mistaken for migraine, GI illness, or other headache causes."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Arrange immediate ophthalmology consultation.\n"
     "• Assess visual acuity in both eyes. Measure IOP if trained/equipped.\n"
     "• Check pupil, cornea, degree of redness. Provide analgesia/antiemetic.\n"
     "• Start appropriate pressure-lowering treatment while arranging definitive ophthalmic care."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Lower Intraocular Pressure[/color]\n"
     "• Acetazolamide: 500 mg IV or PO initial dose. Monitor response, renal function, K+, bicarbonate.\n"
     "• Topical: Timolol 0.5% one drop, Brimonidine 0.2% one drop (if appropriate). Monitor for systemic beta-blocker effects.\n\n"
     "[color=#1E3A8A]B. Pilocarpine[/color]\n"
     "• 1–2% eye drops may be used under ophthalmology guidance once IOP has begun to fall and iris likely to respond. May be ineffective at extremely high pressure.\n\n"
     "[color=#1E3A8A]C. Refractory Severe Pressure Elevation[/color]\n"
     "• IV mannitol may be considered by ophthalmology for very high pressure/inadequate response. Assess cardiac/renal status first.\n\n"
     "[color=#1E3A8A]D. Definitive Treatment[/color]\n"
     "• Laser peripheral iridotomy is commonly used for pupillary-block angle closure. Fellow eye must be assessed."),
    ("04 — WARNINGS", "danger", 
     "• Avoid or use only with specialist direction in significant renal/hepatic disease, severe electrolyte abnormalities, or relevant drug hypersensitivity.\n"
     "• Do not use pilocarpine automatically in every red eye; inappropriate in some secondary angle-closure mechanisms."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate ophthalmology management is required. Do not discharge before urgent specialist assessment and documented treatment plan."),
    ("REFERENCES", "info", "AAO Primary Angle-Closure Disease PPP (2025); RCOphth Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Central Retinal Artery Occlusion")] = [
    ("01 — RECOGNIZE", "info", 
     "Central retinal artery occlusion (CRAO) is acute retinal ischemia and is managed as an eye stroke. It may cause permanent monocular visual loss and indicates possible systemic vascular disease.\n"
     "• Sudden, painless loss of vision in one eye. Markedly reduced visual acuity.\n"
     "• Relative afferent pupillary defect. Retinal whitening or cherry-red spot on funduscopy.\n"
     "• Consider giant cell arteritis in patients > 50 years with new headache, jaw claudication, scalp tenderness."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Establish exact time patient was last known to have normal vision.\n"
     "• Arrange immediate transfer to ED or stroke center with ophthalmology support.\n"
     "• Perform focused neuro and cardiovascular assessment. Check glucose and BP.\n"
     "• Activate acute stroke pathway where appropriate.\n"
     "• Do not delay referral for outpatient eye investigations."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Acute Stroke-Center Assessment[/color]\n"
     "• Immediate stroke and ophthalmology consultation. Evaluate eligibility for time-sensitive reperfusion under receiving center protocol.\n"
     "• IV thrombolysis may be considered in selected patients with disabling visual loss who meet criteria; evidence is evolving.\n"
     "• Ocular massage and anterior chamber paracentesis have not demonstrated reliable benefit and may cause harm; should not delay stroke-center referral.\n\n"
     "[color=#1E3A8A]B. Suspected Giant Cell Arteritis[/color]\n"
     "• If strongly suspected, arrange immediate specialist assessment and systemic corticosteroid treatment to protect the other eye. Do not delay treatment while awaiting temporal artery imaging/biopsy.\n\n"
     "[color=#1E3A8A]C. Secondary Prevention[/color]\n"
     "• Investigate carotid disease, AF, other embolic sources. Manage HTN, diabetes, dyslipidemia, smoking."),
    ("04 — WARNINGS", "danger", 
     "• Do not assume an intervention is beneficial simply because it is traditionally used for retinal artery occlusion."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate transfer to a stroke-capable center is required. Sudden monocular visual loss should never be managed as a routine outpatient eye complaint."),
    ("REFERENCES", "info", "AHA Scientific Statement on CRAO (2021); AAO Guidance (2025–2026).")
]

MEDICAL_TOPICS[("Medical Emergencies", "Serotonin Syndrome (Serotonin Toxicity)")] = [
    ("01 — RECOGNIZE", "info", 
     "Serotonin syndrome is a potentially life-threatening drug-induced toxidrome caused by excessive serotonergic activity. May develop after overdose, drug interaction, or increased dose.\n"
     "• Triggers: SSRIs/SNRIs, MAOIs, tramadol, linezolid, combinations of serotonergic drugs, certain recreational substances.\n"
     "• Agitation, confusion, restlessness. Diaphoresis, tachycardia, hypertension.\n"
     "• Tremor, hyperreflexia, inducible/spontaneous clonus. Ocular clonus.\n"
     "• Hyperthermia and muscle rigidity in severe cases.\n"
     "• [color=#991B1B]Clonus and hyperreflexia strongly support serotonin toxicity.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop suspected serotonergic agents immediately.\n"
     "• Assess ABCs, temperature, mental status. Establish IV access and continuous monitoring in moderate/severe cases.\n"
     "• Check glucose, electrolytes, renal function, CK, blood gas when severe.\n"
     "• Begin active cooling for significant hyperthermia.\n"
     "• Contact toxicology/poison center for severe cases."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Discontinue Causative Agents[/color]\n"
     "• Stop serotonergic drugs. Review all prescribed/OTC/recreational substances.\n\n"
     "[color=#1E3A8A]B. Benzodiazepines[/color]\n"
     "• Lorazepam 1–2 mg IV for significant agitation, tremor, or muscle activity. Repeat titrated doses per protocol. Monitor respiratory rate, SpO2, BP, consciousness.\n\n"
     "[color=#1E3A8A]C. Hyperthermia and Severe Toxicity[/color]\n"
     "• Active external cooling for significant hyperthermia. IV isotonic fluid if indicated. Severe cases require ICU assessment (intubation, deep sedation, neuromuscular paralysis may be required).\n"
     "• Antipyretics are NOT effective for serotonin-related hyperthermia. Avoid physical restraints (increase exertion/heat).\n\n"
     "[color=#1E3A8A]D. Cyproheptadine (Adjunct)[/color]\n"
     "• Consider only as adjunct in selected patients with persistent moderate/severe symptoms after supportive treatment, with toxicology advice.\n"
     "• 12 mg initial PO, followed by 2 mg every 2 hours until improvement, then 8 mg every 6 hours if needed. Follow local toxicology guidance."),
    ("04 — WARNINGS", "danger", 
     "• There is no confirmatory serum serotonin test; diagnosis is clinical.\n"
     "• Cyproheptadine must not delay airway management, cooling, or sedation."),
    ("05 — DISPOSITION", "warning", 
     "• Mild symptoms: observe until resolution and stable vitals per toxicology guidance.\n"
     "• Admit for persistent autonomic instability, significant clonus, hyperthermia, rhabdomyolysis, or organ dysfunction. Severe cases require ICU."),
    ("REFERENCES", "info", "Irish Association for Emergency Medicine (2024); Chiew & Isbister (2025); Local toxicology protocols.")
]


# ==================== BATCH 12 (TOPICS 71-80) ====================

MEDICAL_TOPICS[("Medical Emergencies", "Acute Mesenteric Ischemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute mesenteric ischemia is a life-threatening reduction in intestinal blood flow that may rapidly progress to bowel infarction, perforation, and death.\n"
     "• Causes: Arterial embolism (AF), arterial thrombosis (atherosclerosis), non-occlusive ischemia (shock), venous thrombosis.\n"
     "• Sudden severe abdominal pain (often disproportionate to exam). Nausea, vomiting, diarrhea.\n"
     "• GI bleeding in advanced disease. Abdominal tenderness, guarding, rigidity when infarction develops.\n"
     "• Shock, metabolic acidosis, altered mental status in advanced disease.\n"
     "• [color=#991B1B]A normal early abdominal exam or normal lactate does NOT exclude acute mesenteric ischemia.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and signs of shock.\n"
     "• Keep patient nil by mouth. Establish two large-bore IV lines.\n"
     "• Start isotonic crystalloid resuscitation when indicated, reassessing frequently.\n"
     "• Provide IV analgesia and antiemetics.\n"
     "• Obtain urgent surgical and vascular surgery consultation.\n"
     "• Arrange emergency CT angiography of abdomen and pelvis.\n"
     "• Start broad-spectrum IV antibiotics covering enteric gram-negative organisms and anaerobes.\n"
     "• Do not delay definitive intervention for lab results if deteriorating."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Resuscitation[/color]\n"
     "• Isotonic crystalloid boluses according to perfusion, BP, volume status; reassess after each.\n"
     "• Monitor BP, HR, urine output, lactate, respiratory status.\n\n"
     "[color=#1E3A8A]B. Broad-Spectrum Antibiotics[/color]\n"
     "• Example: Piperacillin–tazobactam 4.5 g IV every 6–8 hours (adjust for renal function).\n\n"
     "[color=#1E3A8A]C. Anticoagulation[/color]\n"
     "• IV unfractionated heparin commonly initiated when arterial/venous thrombosis suspected, unless contraindicated. Use institutional weight-based protocol.\n\n"
     "[color=#1E3A8A]D. Definitive Management[/color]\n"
     "• Endovascular or open revascularization may be required.\n"
     "• Urgent surgical exploration for peritonitis, bowel necrosis, perforation, or deterioration.\n"
     "• Resect nonviable bowel and preserve viable bowel whenever possible."),
    ("04 — WARNINGS", "danger", 
     "• Excessive fluid administration can worsen bowel edema and respiratory status.\n"
     "• Antibiotics do not replace revascularization or surgery."),
    ("05 — DISPOSITION", "warning", 
     "• Admit urgently under surgical and vascular team. Shock, peritonitis, bowel infarction, or organ failure require ICU care."),
    ("REFERENCES", "info", "WSES Guidelines 2022; ESVS guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Limb Ischemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute limb ischemia is a sudden reduction in arterial perfusion that threatens limb viability. Causes: embolism, thrombosis, graft occlusion, trauma.\n"
     "• The Six Ps: Pain, Pallor, Pulselessness, Paresthesia, Paralysis, Poikilothermia (cold limb).\n"
     "• Viable limb: no sensory/motor deficit. Threatened limb: sensory loss and weakness. Irreversible: profound anesthesia, paralysis, absent arterial and venous Doppler signals."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain immediate vascular surgery consultation.\n"
     "• Document symptom onset and last known normal limb function.\n"
     "• Examine both limbs and compare temperature, color, sensation, motor power, pulses.\n"
     "• Use handheld Doppler if available. Establish IV access, provide analgesia, keep NPO.\n"
     "• Begin IV unfractionated heparin promptly unless contraindicated, per protocol.\n"
     "• Do not delay vascular intervention for imaging when limb is immediately threatened."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Anticoagulation[/color]\n"
     "• Unfractionated heparin: Use institutional weight-based IV bolus and infusion protocol. Monitor aPTT/anti-Xa. Avoid in active major bleeding.\n\n"
     "[color=#1E3A8A]B. Pain Management[/color]\n"
     "• Titrated IV analgesia according to severity and hemodynamic status.\n\n"
     "[color=#1E3A8A]C. Revascularization[/color]\n"
     "• Options: Catheter-directed thrombolysis, surgical embolectomy/thrombectomy, endovascular thrombectomy/angioplasty, bypass surgery, amputation if irreversibly ischemic.\n\n"
     "[color=#1E3A8A]D. Reperfusion Injury[/color]\n"
     "• After restoration: monitor for hyperkalemia, metabolic acidosis, rhabdomyolysis/AKI, compartment syndrome, arrhythmias, hemodynamic instability."),
    ("04 — WARNINGS", "danger", 
     "• Heparin prevents thrombus propagation but does not independently restore adequate blood flow.\n"
     "• Thrombolysis is inappropriate in several bleeding-risk situations."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate vascular admission. Threatened limb requires emergency intervention; irreversible ischemia requires urgent specialist assessment."),
    ("REFERENCES", "info", "ESVS Acute Limb Ischaemia Guidelines (2020); SVS guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Esophageal Variceal Hemorrhage")] = [
    ("01 — RECOGNIZE", "info", 
     "Major cause of upper GI bleeding in patients with portal hypertension, commonly due to cirrhosis.\n"
     "• Hematemesis (fresh blood or coffee-ground). Melena or hematochezia in massive bleeding.\n"
     "• Tachycardia, hypotension, or shock.\n"
     "• Known cirrhosis, ascites, splenomegaly, or prior variceal bleeding.\n"
     "• Hepatic encephalopathy in advanced liver disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status. Activate major hemorrhage protocol if indicated.\n"
     "• Obtain two large-bore IV lines. Send CBC, coagulation studies, renal/liver function, type and crossmatch.\n"
     "• Resuscitate carefully; avoid unnecessary over-transfusion.\n"
     "• Start vasoactive agent (terlipressin or octreotide) promptly when variceal bleeding suspected.\n"
     "• Start IV antibiotic prophylaxis per local cirrhosis/GI bleeding protocol.\n"
     "• Arrange urgent endoscopy after initial stabilization.\n"
     "• Consider early airway protection for massive ongoing hematemesis or inability to protect airway."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Blood Product Resuscitation[/color]\n"
     "• Restrictive transfusion strategy (Hb threshold ~7 g/dL) in most stabilized patients; individualize for massive hemorrhage or cardiovascular disease.\n\n"
     "[color=#1E3A8A]B. Vasoactive Therapy[/color]\n"
     "• Terlipressin: 2 mg IV initially, then 1–2 mg IV every 4–6 hours per protocol (commonly 2–5 days). Monitor BP, HR, Na+, ischemia.\n"
     "• Alternative: Octreotide 50 mcg IV bolus, then 50 mcg/hour infusion.\n\n"
     "[color=#1E3A8A]C. Antibiotic Prophylaxis[/color]\n"
     "• Ceftriaxone 1 g IV every 24 hours is commonly used.\n\n"
     "[color=#1E3A8A]D. Endoscopic Treatment[/color]\n"
     "• Urgent upper endoscopy. Endoscopic variceal band ligation is preferred.\n"
     "• If uncontrolled: rescue endoscopic treatment, temporary bridging devices, or TIPS in selected patients."),
    ("04 — WARNINGS", "danger", 
     "• Over-transfusion can increase portal pressure and worsen bleeding.\n"
     "• Use caution with terlipressin in ischemic cardiovascular disease, peripheral vascular disease, and respiratory compromise."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to monitored setting. Shock, ongoing massive bleeding, airway compromise, or advanced liver failure require ICU care."),
    ("REFERENCES", "info", "Baveno VII (2022); AASLD guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Urinary Retention")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute urinary retention is the sudden inability to pass urine despite a full bladder.\n"
     "• Common causes: BPH, urethral stricture/stones, medications (anticholinergics, opioids), constipation, neurological disease (spinal cord/cauda equina), postoperative.\n"
     "• Suprapubic pain and palpable bladder. Urgency with inability to void. Overflow dribbling.\n"
     "• Reduced urine output or rising creatinine. Fever/systemic illness if infection present."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, pain, and evidence of sepsis.\n"
     "• Examine abdomen and assess bladder distension. Ask about back pain, leg weakness, saddle numbness, bowel dysfunction.\n"
     "• Perform bladder ultrasound when available.\n"
     "• Insert urinary catheter promptly unless urethral injury or another contraindication suspected.\n"
     "• If urethral injury possible, seek urgent urological advice and avoid repeated blind catheter attempts."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Bladder Decompression[/color]\n"
     "• Aseptic urethral catheterization using appropriate catheter size and technique. Record volume drained and urine appearance.\n"
     "• If urethral injury suspected, do NOT proceed with routine blind catheterization.\n"
     "• Monitor urine output, pain relief, hematuria, BP, renal function.\n\n"
     "[color=#1E3A8A]B. Suspected Prostatic Obstruction[/color]\n"
     "• Tamsulosin 0.4 mg PO once daily when appropriate. Monitor for dizziness/orthostatic hypotension.\n"
     "• Arrange trial without catheter after a short period of treatment.\n\n"
     "[color=#1E3A8A]C. Post-Obstructive Diuresis[/color]\n"
     "• Measure urine output frequently. Monitor Na+, K+, Mg2+, creatinine, fluid balance.\n"
     "• Replace fluid losses according to hemodynamics, electrolytes, urine output. Avoid automatic replacement of every milliliter.\n\n"
     "[color=#1E3A8A]D. Infection or Renal Impairment[/color]\n"
     "• Treat documented/strongly suspected infection per local guidance. Urgent urological assessment for infected obstruction, renal impairment, persistent obstruction, or failed catheterization."),
    ("04 — WARNINGS", "danger", 
     "• Routine gradual clamping of the catheter is generally unnecessary.\n"
     "• If resistance is encountered, do not force the catheter; obtain experienced assistance."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge may be appropriate after uncomplicated retention when stable, drainage adequate, renal function and infection risks assessed, and reliable urological follow-up arranged.\n"
     "• Admit for sepsis, AKI, significant electrolyte abnormalities, suspected neurological compression, or unresolved obstruction."),
    ("REFERENCES", "info", "NICE LUTS Guidance; EAU Guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Adrenal Incidental Hemorrhage with Adrenal Crisis")] = [
    ("01 — RECOGNIZE", "info", 
     "Adrenal hemorrhage can cause acute primary adrenal insufficiency and adrenal crisis, especially when bilateral. Risk factors: anticoagulation, severe sepsis, trauma, major surgery, underlying adrenal disease.\n"
     "• Hypotension or shock responding poorly to initial fluids.\n"
     "• Abdominal, flank, or back pain. Nausea, vomiting, profound weakness.\n"
     "• Hyponatremia, hyperkalemia, or hypoglycemia. Fever or altered mental status.\n"
     "• History of anticoagulation, trauma, or severe systemic illness.\n"
     "• [color=#991B1B]Normal potassium or sodium does NOT exclude adrenal crisis.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat suspected adrenal crisis immediately; do NOT wait for laboratory confirmation.\n"
     "• Assess ABCs, glucose, mental status.\n"
     "• Obtain IV access and blood samples for cortisol/ACTH before steroids only if no treatment delay.\n"
     "• Check glucose and electrolytes promptly.\n"
     "• Give IV hydrocortisone and isotonic fluid resuscitation.\n"
     "• Correct hypoglycemia immediately.\n"
     "• Investigate and treat precipitating cause (sepsis, hemorrhage)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Immediate Glucocorticoid Replacement[/color]\n"
     "• Hydrocortisone 100 mg IV or IM immediately. Follow with 200 mg over 24 hours by continuous IV infusion, or 50 mg IV every 6 hours.\n\n"
     "[color=#1E3A8A]B. Fluid Resuscitation[/color]\n"
     "• 0.9% NaCl: 1 L IV during first hour (adjusted for hemodynamics/comorbidities). Further fluid individualized.\n\n"
     "[color=#1E3A8A]C. Hypoglycemia[/color]\n"
     "• IV dextrose per protocol if hypoglycemia present. Recheck and monitor.\n\n"
     "[color=#1E3A8A]D. Hyperkalemia[/color]\n"
     "• If significant hyperkalemia or ECG changes, initiate emergency hyperkalemia protocol. Do not assume hydrocortisone alone will correct immediately dangerous hyperkalemia.\n\n"
     "[color=#1E3A8A]E. Identify and Treat the Cause[/color]\n"
     "• Assess for sepsis, trauma, anticoagulant-associated bleeding. Review anticoagulants with specialist. Arrange endocrinology and surgical consultation."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay hydrocortisone while waiting for cortisol results.\n"
     "• Use more cautious fluid replacement in patients at risk of fluid overload."),
    ("05 — DISPOSITION", "warning", 
     "• Admit all patients with suspected adrenal crisis. Shock, severe electrolyte disturbance, hypoglycemia, or ongoing hemorrhage requires ICU-level monitoring."),
    ("REFERENCES", "info", "Society for Endocrinology; Endocrine Society Guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Epiglottitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute epiglottitis is a potentially fatal infection and inflammation of the epiglottis and adjacent supraglottic structures. Can rapidly cause complete upper-airway obstruction.\n"
     "• Severe sore throat and painful swallowing. Drooling or inability to swallow saliva.\n"
     "• Muffled voice. Fever and toxic appearance. Inspiratory stridor or respiratory distress.\n"
     "• Tripod positioning and reluctance to lie flat.\n"
     "• [color=#991B1B]Symptoms may be severe despite a relatively normal-looking oral cavity. Stridor can be a late sign of critical obstruction.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway patency, breathing, oxygenation, mental status.\n"
     "• Call anesthesia, ENT, and critical care teams immediately if airway compromise suspected.\n"
     "• Keep patient calm and in preferred position. Provide supplemental oxygen if tolerated.\n"
     "• Keep patient nil by mouth.\n"
     "• Prepare for controlled airway management in operating room or equivalent high-acuity setting.\n"
     "• Do NOT force patient to lie down or perform unnecessary throat examinations."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Airway Protection[/color]\n"
     "• Early expert airway management for progressive respiratory distress, stridor, hypoxemia, exhaustion, or inability to handle secretions.\n"
     "• Difficult-airway strategy and immediate surgical-airway backup. Avoid repeated intubation attempts.\n\n"
     "[color=#1E3A8A]B. Antibiotics[/color]\n"
     "• Ceftriaxone: Adults 2 g IV every 24 hours (commonly used for severe bacterial epiglottitis). Pediatric dosing weight-based.\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• IV fluids when oral intake unsafe/inadequate. Analgesia and antipyretics. Monitor SpO2, respiratory effort, fatigue continuously."),
    ("04 — WARNINGS", "danger", 
     "• Sedation or airway manipulation without an appropriate rescue plan may precipitate complete obstruction.\n"
     "• Do not delay airway protection for imaging or routine laboratory tests.\n"
     "• Antibiotics do not replace airway management."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for specialist assessment and monitored treatment. Airway compromise requires ICU or equivalent critical care."),
    ("REFERENCES", "info", "IDSA Guidance; Local ENT/Airway protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Retropharyngeal and Parapharyngeal Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "Deep neck space infections can spread rapidly and cause airway obstruction, sepsis, mediastinitis, or vascular complications.\n"
     "• Fever and severe sore throat. Neck pain, stiffness, restricted neck movement.\n"
     "• Dysphagia, odynophagia, or drooling. Muffled voice or trismus. Neck swelling or asymmetry.\n"
     "• Stridor, respiratory distress, toxic appearance in severe cases.\n"
     "• Retropharyngeal abscess particularly important in young children; parapharyngeal in both children and adults."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and signs of sepsis.\n"
     "• Obtain urgent ENT and anesthesia consultation if airway compromise possible.\n"
     "• Keep patient nil by mouth. Establish IV access and obtain relevant blood tests.\n"
     "• Start IV antibiotics promptly in suspected severe infection.\n"
     "• Arrange contrast-enhanced CT of neck in stable patients when needed to define extent.\n"
     "• Do not delay airway protection or surgical assessment for imaging in an unstable patient."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Empiric IV Antibiotics[/color]\n"
     "• Select according to age, allergy, local resistance, severity.\n"
     "• Example: Ampicillin–sulbactam 3 g IV every 6 hours (adults), adjusted for renal function.\n\n"
     "[color=#1E3A8A]B. Airway Management[/color]\n"
     "• Early expert airway intervention for progressive obstruction, distress, inability to manage secretions, rapidly worsening swelling.\n"
     "• Difficult-airway and surgical-airway backup plan.\n\n"
     "[color=#1E3A8A]C. Drainage[/color]\n"
     "• Urgent surgical drainage for significant drainable abscesses, airway compromise, complications, or failure to improve with medical therapy. Small collections may be managed medically under close supervision.\n\n"
     "[color=#1E3A8A]D. Supportive Care[/color]\n"
     "• IV fluids, analgesia, antipyretics. Monitor for sepsis, mediastinal extension, vascular complications."),
    ("04 — WARNINGS", "danger", 
     "• Broader coverage (including MRSA) may be required based on risk factors and local epidemiology.\n"
     "• Avoid unnecessary sedation and repeated airway manipulation."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for IV treatment and ENT assessment. Airway compromise, sepsis, extensive infection, or need for airway intervention requires ICU-level care."),
    ("REFERENCES", "info", "IDSA antimicrobial principles; Local ENT protocols.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Severe Hyperphosphatemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe hyperphosphatemia may cause symptomatic hypocalcemia, calcium-phosphate deposition, acute kidney injury, and cardiac complications. Causes: advanced renal failure, tumor lysis syndrome, rhabdomyolysis, phosphate-containing preparations, severe tissue breakdown.\n"
     "• Muscle cramps, paresthesia, tetany due to hypocalcemia.\n"
     "• Seizures or altered mental status. Arrhythmias when significant calcium/electrolyte abnormalities coexist.\n"
     "• Oliguria or renal failure. History of tumor lysis, rhabdomyolysis, or phosphate ingestion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, neurological status. Obtain ECG if significant calcium disturbance or cardiac symptoms.\n"
     "• Check phosphate, calcium, magnesium, potassium, renal function, glucose.\n"
     "• Stop phosphate-containing medications, supplements, enemas, or infusions.\n"
     "• Treat symptomatic hypocalcemia and life-threatening associated electrolyte abnormalities.\n"
     "• Involve nephrology early if severe hyperphosphatemia with renal failure or refractory abnormalities."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Remove the Phosphate Source[/color]\n"
     "• Stop exogenous phosphate. Treat underlying cause (TLS, rhabdomyolysis).\n\n"
     "[color=#1E3A8A]B. Hydration[/color]\n"
     "• Isotonic IV fluid when volume depletion present and patient can tolerate. Avoid aggressive hydration in anuria, severe renal failure, or fluid overload.\n\n"
     "[color=#1E3A8A]C. Phosphate Binders[/color]\n"
     "• In selected patients who can take enteral medication, a phosphate binder (e.g., sevelamer) may be used under specialist guidance. Dosing depends on phosphate, formulation, dialysis status.\n\n"
     "[color=#1E3A8A]D. Symptomatic Hypocalcemia[/color]\n"
     "• IV calcium may be required for tetany, seizures, significant QT prolongation, or hemodynamic instability. Use local IV calcium protocol and monitor ECG and ionized calcium. (Caution: calcium-phosphate precipitation in severe hyperphosphatemia).\n\n"
     "[color=#1E3A8A]E. Dialysis[/color]\n"
     "• Urgent nephrology assessment for dialysis when severe hyperphosphatemia with significant renal failure, refractory/dangerous electrolyte disturbances, severe symptomatic hypocalcemia, or other established indications."),
    ("04 — WARNINGS", "danger", 
     "• Oral binders are not a substitute for emergency treatment in severe symptomatic cases or significant renal failure.\n"
     "• Administer calcium only when clinically indicated and with close monitoring."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for severe symptomatic abnormalities, AKI, TLS, or associated dangerous electrolyte disturbances. ICU for seizures, arrhythmias, shock, or multiorgan failure."),
    ("REFERENCES", "info", "KDIGO CKD-MBD; ASCO TLS protocols; Local nephrology guidelines.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Acute Opioid Toxicity")] = [
    ("01 — RECOGNIZE", "info", 
     "Opioid toxicity can cause life-threatening respiratory depression. May follow therapeutic use, accidental ingestion, intentional overdose, or illicit opioid exposure.\n"
     "• Reduced respiratory rate or shallow breathing.\n"
     "• Reduced consciousness. Pinpoint pupils (may be absent).\n"
     "• Hypoxemia, cyanosis, or hypercapnia. Bradycardia and hypotension in severe cases.\n"
     "• Aspiration or pulmonary edema in complicated presentations."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, level of consciousness. Call for emergency airway/resuscitation support.\n"
     "• Open airway and provide assisted ventilation when breathing inadequate.\n"
     "• Administer oxygen and use bag-mask ventilation when indicated.\n"
     "• Give naloxone promptly for suspected opioid-induced respiratory depression.\n"
     "• Check blood glucose. Consider co-ingestants and alternative causes of reduced consciousness.\n"
     "• Do NOT delay ventilation while preparing naloxone."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Naloxone[/color]\n"
     "• If IV access available: 0.04 mg IV initially (if opioid dependence possible and not in immediate life-threatening apnea).\n"
     "• Escalate to 0.1–0.2 mg, 0.4 mg, then larger doses as needed per protocol.\n"
     "• In apnea or severe life-threatening respiratory depression: do NOT delay effective treatment for cautious low-dose titration; use appropriate initial dose (commonly 0.4–2 mg IV/IM/IN).\n"
     "• Repeat doses may be necessary.\n\n"
     "[color=#1E3A8A]B. Recurrent Respiratory Depression[/color]\n"
     "• Repeat naloxone per clinical response.\n"
     "• Consider naloxone infusion when repeated boluses required or long-acting opioid toxicity suspected (starting ~two-thirds of effective reversal bolus dose per hour).\n\n"
     "[color=#1E3A8A]C. Supportive Care[/color]\n"
     "• Maintain airway and ventilation. Treat hypoglycemia and other reversible causes. Assess for aspiration, trauma, co-ingestion. Avoid flumazenil as routine treatment."),
    ("04 — WARNINGS", "danger", 
     "• Naloxone may precipitate acute withdrawal, agitation, vomiting, aspiration in opioid-dependent patients.\n"
     "• Its duration may be shorter than that of the opioid (especially methadone or extended-release preparations)."),
    ("05 — DISPOSITION", "warning", 
     "• Observe until respiratory function and consciousness remain stable without repeated naloxone and risk from suspected opioid assessed.\n"
     "• Admit for recurrent respiratory depression, long-acting opioid exposure, aspiration, pulmonary complications, significant co-ingestion, or ongoing oxygen/ventilatory requirements."),
    ("REFERENCES", "info", "AHA Opioid-Associated Emergencies; WHO Guidance.")
]

MEDICAL_TOPICS[("Medical Emergencies", "Local Anesthetic Systemic Toxicity (LAST)")] = [
    ("01 — RECOGNIZE", "info", 
     "Life-threatening complication of local anesthetic exposure, commonly following inadvertent intravascular injection or excessive dosing. Can cause seizures, cardiovascular collapse, malignant arrhythmias.\n"
     "• Early neuro: Circumoral numbness, metallic taste, tinnitus, agitation, confusion, dizziness, seizures.\n"
     "• Severe: Reduced consciousness, hypotension, bradycardia/conduction abnormalities, ventricular arrhythmias, cardiac arrest.\n"
     "• Presentation may be atypical or delayed, especially after infiltration or long-acting local anesthetics."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop local anesthetic administration immediately.\n"
     "• Call for resuscitation assistance and LAST rescue kit.\n"
     "• Provide 100% oxygen and support ventilation.\n"
     "• Treat seizures promptly with benzodiazepines.\n"
     "• Start standard resuscitation while recognizing LAST requires modifications to routine ACLS.\n"
     "• Administer 20% IV lipid emulsion promptly for serious LAST.\n"
     "• Arrange ICU-level monitoring and expert consultation."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Seizure Control[/color]\n"
     "• Midazolam 1–2 mg IV increments, titrated to seizure control per protocol.\n\n"
     "[color=#1E3A8A]B. 20% Lipid Emulsion[/color]\n"
     "• If weight <70 kg: 1.5 mL/kg IV over 2–3 mins, then 0.25 mL/kg/min.\n"
     "• If weight ≥70 kg: 100 mL IV over 2–3 mins, then ~250 mL over 15–20 mins.\n"
     "• May repeat bolus and increase infusion if instability persists. Maximum cumulative dose ~12 mL/kg.\n\n"
     "[color=#1E3A8A]C. Modified Resuscitation[/color]\n"
     "• Follow ASRA LAST checklist.\n"
     "• Avoid vasopressin, beta-blockers, calcium-channel blockers, and additional local anesthetic drugs when protocol advises.\n"
     "• Epinephrine: smaller-than-standard doses (initially <1 mcg/kg).\n\n"
     "[color=#1E3A8A]D. Monitoring After Stabilization[/color]\n"
     "• Observe for recurrent neuro/cardiovascular toxicity. Prolonged monitored observation (at least 4–6 hours after stabilization; longer after cardiac arrest)."),
    ("04 — WARNINGS", "danger", 
     "• Do not confuse 20% lipid emulsion with propofol.\n"
     "• Lipid emulsion is a rescue treatment for serious LAST, not routine treatment for minor local anesthetic symptoms."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with seizures, significant neurological symptoms, cardiovascular instability, or lipid rescue treatment for monitored care. Cardiac arrest or persistent instability requires ICU admission."),
    ("REFERENCES", "info", "ASRA LAST Checklist (2020 and updates).")
]