# ==============================================================================
# ملف البروتوكولات السريرية (Clinical Protocols) - كامل
# ==============================================================================

PROTOCOLS_DATA = {
    "Clinical Protocols": {
        "General": [
            "Adult ALS Protocol", 
            "ATLS Primary Survey", 
            "Sepsis Six Bundle", 
            "Stroke Thrombolysis Pathway", 
            "DKA Management Protocol"
        ]
    }
}

PROTOCOLS_TOPICS = {}

# -------------------- ADULT ALS PROTOCOL --------------------
PROTOCOLS_TOPICS[("Clinical Protocols", "Adult ALS Protocol")] = [
    ("1. RECOGNIZE CARDIAC ARREST", "info", 
     "• Unresponsive.\n"
     "• No normal breathing (or only gasping).\n"
     "• No pulse for 10 seconds.\n\n"
     "[color=#991B1B]Start CPR immediately.[/color]"),
    ("2. IMMEDIATE ACTIONS (BLS)", "success", 
     "• [b]Chest Compressions:[/b] 100–120/min, depth 5–6 cm.\n"
     "• [b]Airway:[/b] Head-tilt/chin-lift, bag-mask ventilation (30:2).\n"
     "• [b]Attach Defibrillator/Monitor:[/b] As soon as possible.\n"
     "• [b]IV/IO Access:[/b] Do not interrupt CPR."),
    ("3. SHOCKABLE RHYTHM (VF/pVT)", "success", 
     "• [b]Defibrillate:[/b] Biphasic 120–200 J.\n"
     "• [b]CPR:[/b] Immediate 2 minutes (do not check rhythm).\n"
     "• [b]Epinephrine:[/b] 1 mg IV/IO (after 2nd shock), repeat every 3-5 mins.\n"
     "• [b]Amiodarone:[/b] 300 mg IV/IO (after 3rd shock), then 150 mg.\n"
     "• [b]Reversible Causes:[/b] Treat 5Hs & 5Ts."),
    ("4. NON-SHOCKABLE RHYTHM (Asystole/PEA)", "warning", 
     "• [color=#991B1B]DO NOT DEFIBRILLATE.[/color]\n"
     "• [b]CPR:[/b] Continuous 2-minute cycles.\n"
     "• [b]Epinephrine:[/b] 1 mg IV/IO as soon as possible, repeat every 3-5 mins.\n"
     "• [b]Reversible Causes:[/b] Treat 5Hs & 5Ts."),
    ("5. POST-ROSC CARE", "info", 
     "• [b]Airway:[/b] Secure (ETT) + Capnography.\n"
     "• [b]Oxygen:[/b] Target SpO2 94–98%.\n"
     "• [b]Ventilation:[/b] Target PaCO2 35–45 mmHg.\n"
     "• [b]Circulation:[/b] Target MAP ≥ 65 mmHg.\n"
     "• [b]TTM:[/b] Targeted Temperature Management (32–36°C) if comatose.\n"
     "• [b]ECG & Labs:[/b] 12-lead ECG, blood gas, lactate, electrolytes."),
    ("6. DON'T MISS", "danger", 
     "• Do not delay defibrillation.\n"
     "• Do not over-ventilate (reduces venous return).\n"
     "• Do not stop CPR to check rhythm for prolonged periods."),
    ("REFERENCES", "info", "AHA 2025 ACLS Guidelines; ERC 2025.")
]

# -------------------- ATLS PRIMARY SURVEY --------------------
PROTOCOLS_TOPICS[("Clinical Protocols", "ATLS Primary Survey")] = [
    ("1. A - AIRWAY (C-SPINE)", "success", 
     "• Manual in-line stabilization (MILS).\n"
     "• Assess patency (speak to patient).\n"
     "• Suction, airway adjuncts (OPA/NPA).\n"
     "• Definitive airway (ETT) if GCS < 8."),
    ("2. B - BREATHING", "success", 
     "• High-flow oxygen (15 L/min).\n"
     "• Auscultate (tension pneumothorax, hemothorax).\n"
     "• [b]Tension Pneumothorax:[/b] Immediate needle decompression.\n"
     "• [b]Open Pneumothorax:[/b] 3-sided occlusive dressing."),
    ("3. C - CIRCULATION", "success", 
     "• Assess pulse, BP, capillary refill.\n"
     "• Stop external bleeding (pressure, tourniquet).\n"
     "• 2 large-bore IVs, crossmatch blood.\n"
     "• [b]Permissive Hypotension:[/b] Target SBP 80-90 mmHg (except TBI).\n"
     "• [b]TXA:[/b] 1 g IV over 10 mins if within 3 hours of injury."),
    ("4. D - DISABILITY", "success", 
     "• GCS (Glasgow Coma Scale).\n"
     "• Pupils (size, reactivity).\n"
     "• Focal neurological deficit (spinal cord injury)."),
    ("5. E - EXPOSURE", "success", 
     "• Fully undress to assess all injuries.\n"
     "• [b]PREVENT HYPOTHERMIA:[/b] Warm blankets, warm fluids.\n"
     "• Log-roll to examine the back."),
    ("6. ADJUNCTS", "info", 
     "• [b]ECG, BP, SpO2, Capnography.[/b]\n"
     "• [b]Urinary & Gastric Catheters.[/b]\n"
     "• [b]X-rays:[/b] Chest, Pelvis.\n"
     "• [b]FAST Scan:[/b] Free fluid in abdomen/pericardium."),
    ("REFERENCES", "info", "ATLS 10th/11th Edition.")
]

# -------------------- SEPSIS SIX BUNDLE --------------------
PROTOCOLS_TOPICS[("Clinical Protocols", "Sepsis Six Bundle")] = [
    ("1. GIVE OXYGEN", "success", 
     "• Target SpO2 94–98% (or 88–92% if COPD).\n"
     "• High-flow oxygen if hypoxemic."),
    ("2. TAKE BLOOD CULTURES", "success", 
     "• At least 2 sets (aerobic and anaerobic).\n"
     "• Do not delay antibiotics for cultures in unstable patients."),
    ("3. GIVE IV ANTIBIOTICS", "success", 
     "• Broad-spectrum antibiotics within 1 HOUR.\n"
     "• Follow local guidelines (e.g., Piperacillin-tazobactam 4.5g IV)."),
    ("4. GIVE IV FLUIDS", "success", 
     "• 30 mL/kg crystalloid for hypotension or lactate ≥ 4.\n"
     "• Use balanced crystalloids (Ringer's Lactate) if available.\n"
     "• Reassess after each bolus."),
    ("5. CHECK LACTATE", "success", 
     "• Measure serum lactate.\n"
     "• Repeat within 2-4 hours if initial > 2 mmol/L."),
    ("6. MONITOR URINE OUTPUT", "success", 
     "• Insert urinary catheter.\n"
     "• Target urine output ≥ 0.5 mL/kg/hour."),
    ("DON'T MISS", "danger", 
     "• Do not delay antibiotics for investigations.\n"
     "• Do not miss the source (abscess, perforation, infected line).\n"
     "• Escalate to ICU if patient remains hypotensive."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign 2021; NICE NG51.")
]

# -------------------- STROKE THROMBOLYSIS PATHWAY --------------------
PROTOCOLS_TOPICS[("Clinical Protocols", "Stroke Thrombolysis Pathway")] = [
    ("1. TIME IS BRAIN", "info", 
     "• Record exact time of onset (last known well).\n"
     "• Goal: Door-to-needle time < 30-60 minutes.\n"
     "• Exclude hypoglycemia (check glucose immediately)."),
    ("2. IMMEDIATE IMAGING", "success", 
     "• Urgent Non-Contrast CT Head (within 20 mins).\n"
     "• Exclude intracranial hemorrhage (ICH).\n"
     "• CTA if Large Vessel Occlusion (LVO) suspected."),
    ("3. INCLUSION & EXCLUSION", "warning", 
     "• [b]Window:[/b] Within 4.5 hours of onset.\n"
     "• [b]BP:[/b] Must be < 185/110 mmHg (lower with Labetalol).\n"
     "[color=#991B1B]Exclusions: Active bleeding, recent surgery/stroke (<3 months), platelets < 100,000, INR > 1.7 (on warfarin).[/color]"),
    ("4. THROMBOLYSIS DOSING", "success", 
     "• [b]Alteplase:[/b] 0.9 mg/kg IV (max 90 mg).\n"
     "• Give 10% as a bolus over 1 min, rest over 60 mins.\n"
     "• OR [b]Tenecteplase (TNK):[/b] 0.25 mg/kg IV single bolus (max 25 mg)."),
    ("5. POST-THROMBOLYSIS CARE", "info", 
     "• Strict BP < 180/105 mmHg for 24 hours.\n"
     "• Neuro checks every 15 mins for 2 hours.\n"
     "• No antiplatelets/anticoagulants for 24 hours.\n"
     "• Repeat CT head if sudden deterioration (headache, vomiting, reduced GCS)."),
    ("6. THROMBECTOMY", "success", 
     "• Indicated for Large Vessel Occlusion (LVO).\n"
     "• Within 6 hours (or up to 24 hours with favorable perfusion imaging).\n"
     "• Contact Interventional Radiology / Neurointervention team."),
    ("REFERENCES", "info", "AHA/ASA 2019/2021 Stroke Guidelines.")
]

# -------------------- DKA MANAGEMENT PROTOCOL --------------------
PROTOCOLS_TOPICS[("Clinical Protocols", "DKA Management Protocol")] = [
    ("1. IMMEDIATE ACTIONS", "success", 
     "• ABCDE, hourly glucose, 2-hourly K+.\n"
     "• IV access, VBG, blood ketones, U&E.\n"
     "• Identify precipitant (infection, missed insulin, MI)."),
    ("2. FLUIDS (CRITICAL)", "success", 
     "• [b]0.9% NaCl:[/b] 15-20 mL/kg in first hour (approx 1L).\n"
     "• Adjust in HF/renal impairment.\n"
     "• When glucose < 14 mmol/L: switch to 5% Dextrose + 0.45% NaCl."),
    ("3. POTASSIUM (HOLD INSULIN IF LOW)", "warning", 
     "• [color=#991B1B]K+ < 3.3 mmol/L:[/color] HOLD insulin. Give IV potassium first.\n"
     "• [b]K+ 3.3-5.2 mmol/L:[/b] Add 20-30 mmol KCl to each liter of fluid.\n"
     "• [b]K+ > 5.2 mmol/L:[/b] Hold potassium, recheck 2-hourly."),
    ("4. INSULIN INFUSION", "success", 
     "• [b]Start:[/b] After K+ is safe (≥3.3) and fluids begun.\n"
     "• [b]Dose:[/b] 0.1 unit/kg/hour IV infusion (no bolus).\n"
     "• [b]Preparation:[/b] 50 units regular insulin in 50 mL 0.9% NaCl (1 unit/mL).\n"
     "• Continue until ketones < 0.6 and pH > 7.30."),
    ("5. MONITORING", "info", 
     "• Hourly glucose.\n"
     "• 2-hourly K+ and U&E.\n"
     "• 2-4 hourly VBG.\n"
     "• Hourly urine output.\n"
     "• Neuro checks (cerebral edema is rare in adults)."),
    ("6. DON'T MISS", "danger", 
     "• Never start insulin if K+ < 3.3.\n"
     "• Never stop insulin when glucose normalizes (add dextrose).\n"
     "• Bicarbonate is not routine (only if pH < 6.9 with shock).\n"
     "• Do not mistake DKA abdominal pain for surgical abdomen."),
    ("REFERENCES", "info", "ADA 2024 Consensus; JBDS DKA Guidelines.")
]