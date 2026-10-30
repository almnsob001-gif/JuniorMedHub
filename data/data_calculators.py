# ==============================================================================
# ملف الآلات الحاسبة الطبية (Clinical Calculators) - النسخة الكاملة
# ==============================================================================

CALCULATORS_DATA = {
    "Clinical Calculators": {
        "General": [
            "Mean Arterial Pressure (MAP)", "Shock Index", "Anion Gap",
            "Corrected Calcium", "Corrected Sodium", "Creatinine Clearance",
            "Ideal Body Weight", "Parkland Formula", "qSOFA Score", "CURB-65 Score",
            "Glasgow Coma Scale (GCS)", "Holliday-Segar Maintenance Fluids",
            "Free Water Deficit", "Bicarbonate Deficit", "FENa (Fractional Excretion of Sodium)",
            "Wells Score for DVT", "Wells Score for PE", "CHA2DS2-VASc Score",
            "HAS-BLED Score", "Child-Pugh Score"
        ]
    }
}

CALCULATOR_DEFINITIONS = {
    "Mean Arterial Pressure (MAP)": {
        "description": "Mean arterial pressure (MAP) is the average arterial pressure throughout one cardiac cycle, important for organ perfusion.",
        "fields": [
            {"key": "sbp", "label": "Systolic BP (mmHg)", "placeholder": "e.g., 120"},
            {"key": "dbp", "label": "Diastolic BP (mmHg)", "placeholder": "e.g., 80"}
        ],
        "formula_text": "MAP = DBP + (SBP - DBP) / 3",
        "formula": "dbp + (sbp - dbp) / 3",
        "unit": "mmHg",
        "interpretation": "Normal: 70-100 mmHg.\nTarget in Sepsis/Septic Shock: ≥ 65 mmHg.\nTarget in TBI: ≥ 80 mmHg.",
        "reference": "Standard physiological formula."
    },
    "Shock Index": {
        "description": "The Shock Index is a rapid bedside tool to assess the severity of hypovolemic/hemorrhagic shock.",
        "fields": [
            {"key": "hr", "label": "Heart Rate (bpm)", "placeholder": "e.g., 110"},
            {"key": "sbp", "label": "Systolic BP (mmHg)", "placeholder": "e.g., 100"}
        ],
        "formula_text": "Shock Index = HR / SBP",
        "formula": "hr / sbp",
        "unit": "",
        "interpretation": "Normal: 0.5 - 0.7.\nElevated (> 0.9): Suggests significant hypovolemia/shock.\n> 1.0: Severe shock, high mortality risk.",
        "reference": "Allgöwer and Burri (1967)."
    },
    "Anion Gap": {
        "description": "Calculates the anion gap in serum to help differentiate causes of metabolic acidosis.",
        "fields": [
            {"key": "na", "label": "Sodium (Na+)", "placeholder": "e.g., 140"},
            {"key": "cl", "label": "Chloride (Cl-)", "placeholder": "e.g., 104"},
            {"key": "hco3", "label": "Bicarbonate (HCO3-)", "placeholder": "e.g., 24"}
        ],
        "formula_text": "Anion Gap = Na+ - (Cl- + HCO3-)",
        "formula": "na - (cl + hco3)",
        "unit": "mEq/L",
        "interpretation": "Normal: 8-12 mEq/L.\nElevated (> 12): High anion gap metabolic acidosis.\nNormal: Normal anion gap (e.g., diarrhea, RTA).",
        "reference": "Standard laboratory formula."
    },
    "Corrected Calcium": {
        "description": "Corrects measured calcium for low albumin levels.",
        "fields": [
            {"key": "ca", "label": "Measured Calcium (mg/dL)", "placeholder": "e.g., 8.0"},
            {"key": "alb", "label": "Albumin (g/dL)", "placeholder": "e.g., 2.5"}
        ],
        "formula_text": "Corrected Ca = Measured Ca + 0.8 × (4.0 - Albumin)",
        "formula": "ca + 0.8 * (4.0 - alb)",
        "unit": "mg/dL",
        "interpretation": "Normal: 8.5 - 10.5 mg/dL.\n< 8.5: Hypocalcemia.\n> 10.5: Hypercalcemia.",
        "reference": "Payne et al. (1973)."
    },
    "Corrected Sodium": {
        "description": "Corrects sodium level for hyperglycemia (pseudohyponatremia).",
        "fields": [
            {"key": "na", "label": "Measured Sodium (Na+)", "placeholder": "e.g., 130"},
            {"key": "glu", "label": "Glucose (mg/dL)", "placeholder": "e.g., 400"}
        ],
        "formula_text": "Corrected Na = Measured Na + 0.016 × (Glucose - 100)",
        "formula": "na + 0.016 * (glu - 100)",
        "unit": "mEq/L",
        "interpretation": "For every 100 mg/dL rise in glucose above 100, sodium falls by ~1.6 mEq/L.\nUsed to assess true sodium status in DKA/HHS.",
        "reference": "Hillier et al. (1999)."
    },
    "Creatinine Clearance": {
        "description": "Cockcroft-Gault formula to estimate creatinine clearance (CrCl) and guide drug dosing.",
        "fields": [
            {"key": "age", "label": "Age (years)", "placeholder": "e.g., 65"},
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 70"},
            {"key": "cr", "label": "Serum Creatinine (mg/dL)", "placeholder": "e.g., 1.2"},
            {"key": "sex", "label": "Sex (1=Male, 0.85=Female)", "placeholder": "1 or 0.85"}
        ],
        "formula_text": "CrCl = ((140 - Age) × Weight) / (72 × Creatinine) × Sex Factor",
        "formula": "((140 - age) * wt) / (72 * cr) * sex",
        "unit": "mL/min",
        "interpretation": "Normal: 90-120 mL/min.\n60-89: Mild impairment.\n30-59: Moderate (dose adjust).\n15-29: Severe.\n< 15: Kidney failure.",
        "reference": "Cockcroft & Gault (1976)."
    },
    "Ideal Body Weight": {
        "description": "Calculates Ideal Body Weight (IBW) using the Devine formula, essential for tidal volume calculation in mechanical ventilation.",
        "fields": [
            {"key": "ht", "label": "Height (cm)", "placeholder": "e.g., 175"},
            {"key": "sex", "label": "Sex (1=Male, 0=Female)", "placeholder": "1 or 0"}
        ],
        "formula_text": "IBW = 45.5 + 4.5 × Sex + 0.91 × (Height - 152.4)",
        "formula": "45.5 + 4.5 * sex + 0.91 * (ht - 152.4)",
        "unit": "kg",
        "interpretation": "Used to calculate: Tidal volume (6-8 mL/kg IBW), Drug dosing, and Nutrition.",
        "reference": "Devine (1974)."
    },
    "Parkland Formula": {
        "description": "Calculates total fluid requirements for burn resuscitation in the first 24 hours.",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 70"},
            {"key": "tbsa", "label": "TBSA (%)", "placeholder": "e.g., 30"}
        ],
        "formula_text": "Total 24h Fluid = 4 mL × Weight × %TBSA (Ringer's Lactate)",
        "formula": "4 * wt * tbsa",
        "unit": "mL",
        "interpretation": "Give 50% in the FIRST 8 HOURS (from time of burn).\nGive 50% in the NEXT 16 HOURS.\nTarget urine output: 0.5-1 mL/kg/h.",
        "reference": "Baxter & Shires (1968)."
    },
    "qSOFA Score": {
        "description": "Quick SOFA score for rapid identification of sepsis at the bedside.",
        "fields": [
            {"key": "rr", "label": "Resp Rate (≥ 22 = 1, else 0)", "placeholder": "0 or 1"},
            {"key": "sbp", "label": "SBP (≤ 100 = 1, else 0)", "placeholder": "0 or 1"},
            {"key": "mental", "label": "Altered Mentation (1=Yes, 0=No)", "placeholder": "0 or 1"}
        ],
        "formula_text": "qSOFA = RR ≥ 22 + SBP ≤ 100 + Altered Mentation",
        "formula": "rr + sbp + mental",
        "unit": "/3",
        "interpretation": "Score ≥ 2: High risk of poor outcome. Further assessment needed for sepsis.\nScore < 2: Sepsis still possible (qSOFA does not rule it out).",
        "reference": "Sepsis-3 Consensus (Singer et al., 2016)."
    },
    "CURB-65 Score": {
        "description": "Severity score for community-acquired pneumonia to guide admission decisions.",
        "fields": [
            {"key": "c", "label": "Confusion (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "u", "label": "Urea > 7 mmol/L (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "r", "label": "RR ≥ 30/min (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "b", "label": "BP (SBP<90 or DBP≤60) (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "a", "label": "Age ≥ 65 (1=Yes, 0=No)", "placeholder": "0 or 1"}
        ],
        "formula_text": "CURB-65 = C + U + R + B + Age (each scored 0 or 1)",
        "formula": "c + u + r + b + a",
        "unit": "/5",
        "interpretation": "0-1: Low risk (outpatient).\n2: Moderate risk (consider admission).\n3-5: High risk (admit, consider ICU if 4-5).",
        "reference": "Lim et al. (2003). BTS Guidelines."
    },
    "Glasgow Coma Scale (GCS)": {
        "description": "Standardized scale to assess level of consciousness after acute brain injury.",
        "fields": [
            {"key": "eye", "label": "Eye Opening (1-4)", "placeholder": "e.g., 4"},
            {"key": "verbal", "label": "Verbal Response (1-5)", "placeholder": "e.g., 5"},
            {"key": "motor", "label": "Motor Response (1-6)", "placeholder": "e.g., 6"}
        ],
        "formula_text": "GCS = Eye + Verbal + Motor",
        "formula": "eye + verbal + motor",
        "unit": "/15",
        "interpretation": "Severe: 3-8 (Consider intubation if ≤ 8).\nModerate: 9-13.\nMild: 14-15.",
        "reference": "Teasdale & Jennett (1974)."
    },
    "Holliday-Segar Maintenance Fluids": {
        "description": "Calculates daily maintenance fluid requirements for children.",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 15"}
        ],
        "formula_text": "4 mL/kg for first 10 kg, 2 mL/kg for next 10 kg, 1 mL/kg thereafter.",
        "formula": "(4 * wt) if wt <= 10 else (40 + 2 * (wt - 10)) if wt <= 20 else (60 + 1 * (wt - 20))",
        "unit": "mL/day",
        "interpretation": "Divide by 24 for hourly rate (mL/hr).\nFor adolescents (>50 kg), use adult maintenance rates.",
        "reference": "Holliday & Segar (1957)."
    },
    "Free Water Deficit": {
        "description": "Calculates the free water deficit to guide correction of hypernatremia.",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 70"},
            {"key": "na", "label": "Serum Sodium (Na+)", "placeholder": "e.g., 160"},
            {"key": "sex", "label": "Total Body Water (0.6=Male, 0.5=Female)", "placeholder": "0.6 or 0.5"}
        ],
        "formula_text": "Deficit = TBW_factor × Weight × (Na / 140 - 1)",
        "formula": "sex * wt * (na / 140.0 - 1.0)",
        "unit": "L",
        "interpretation": "Represents the amount of fluid needed to restore normal sodium (140).\nCorrect slowly (max 10 mEq/L per day) to avoid cerebral edema.",
        "reference": "Standard nephrology formula."
    },
    "Bicarbonate Deficit": {
        "description": "Estimates the bicarbonate deficit in severe metabolic acidosis.",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 70"},
            {"key": "hco3", "label": "Serum Bicarbonate (mEq/L)", "placeholder": "e.g., 10"}
        ],
        "formula_text": "Deficit = 0.5 × Weight × (24 - HCO3)",
        "formula": "0.5 * wt * (24 - hco3)",
        "unit": "mEq",
        "interpretation": "Note: Routine bicarbonate use is not recommended in most cases (e.g., DKA).\nConsider only in severe acidosis (pH < 7.1) or hyperkalemia.",
        "reference": "Standard acid-base formula."
    },
    "FENa (Fractional Excretion of Sodium)": {
        "description": "Helps differentiate pre-renal azotemia from intrinsic renal failure (ATN).",
        "fields": [
            {"key": "sna", "label": "Serum Sodium (mEq/L)", "placeholder": "e.g., 140"},
            {"key": "scr", "label": "Serum Creatinine (mg/dL)", "placeholder": "e.g., 2.0"},
            {"key": "una", "label": "Urine Sodium (mEq/L)", "placeholder": "e.g., 20"},
            {"key": "ucr", "label": "Urine Creatinine (mg/dL)", "placeholder": "e.g., 100"}
        ],
        "formula_text": "FENa = (Urine Na × Serum Cr) / (Serum Na × Urine Cr) × 100",
        "formula": "(una * scr) / (sna * ucr) * 100.0",
        "unit": "%",
        "interpretation": "< 1%: Pre-renal (e.g., dehydration, heart failure).\n> 2%: Intrinsic renal (e.g., ATN).\nNote: Unreliable in patients on diuretics (use FEUrea instead).",
        "reference": "Espinel (1976)."
    },
    "Wells Score for DVT": {
        "description": "Clinical prediction rule for the probability of deep vein thrombosis (DVT).",
        "fields": [
            {"key": "cancer", "label": "Active cancer (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "paralysis", "label": "Paralysis/paresis (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "bed", "label": "Bedridden >3 days (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "tenderness", "label": "Tenderness along deep veins (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "swelling", "label": "Entire leg swollen (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "calf", "label": "Calf swelling >3 cm (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "edema", "label": "Pitting edema (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "veins", "label": "Collateral superficial veins (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "prev", "label": "Previous DVT (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "alt", "label": "Alternative diagnosis as likely (-2=Yes, 0=No)", "placeholder": "-2 or 0"}
        ],
        "formula_text": "Sum of scores (Alternative diagnosis = -2)",
        "formula": "cancer + paralysis + bed + tenderness + swelling + calf + edema + veins + prev + alt",
        "unit": "points",
        "interpretation": "≤ 0: Low probability.\n1-2: Moderate probability.\n≥ 3: High probability.\nUse with D-dimer and Ultrasound.",
        "reference": "Wells et al. (1997)."
    },
    "Wells Score for PE": {
        "description": "Clinical prediction rule for the probability of pulmonary embolism (PE).",
        "fields": [
            {"key": "dvt", "label": "Clinical signs of DVT (3=Yes, 0=No)", "placeholder": "3 or 0"},
            {"key": "pe", "label": "PE is #1 diagnosis (1.5=Yes, 0=No)", "placeholder": "1.5 or 0"},
            {"key": "hr", "label": "HR > 100 bpm (1.5=Yes, 0=No)", "placeholder": "1.5 or 0"},
            {"key": "immob", "label": "Immobilization/Surgery (1.5=Yes, 0=No)", "placeholder": "1.5 or 0"},
            {"key": "prev", "label": "Previous PE/DVT (1.5=Yes, 0=No)", "placeholder": "1.5 or 0"},
            {"key": "hemo", "label": "Hemoptysis (1=Yes, 0=No)", "placeholder": "1 or 0"},
            {"key": "malig", "label": "Malignancy (1=Yes, 0=No)", "placeholder": "1 or 0"}
        ],
        "formula_text": "Sum of weighted scores",
        "formula": "dvt + pe + hr + immob + prev + hemo + malig",
        "unit": "points",
        "interpretation": "< 2: Low probability.\n2-6: Moderate probability.\n> 6: High probability.\nUse with D-dimer and CTPA.",
        "reference": "Wells et al. (2000)."
    },
    "CHA2DS2-VASc Score": {
        "description": "Estimates stroke risk in patients with atrial fibrillation to guide anticoagulation.",
        "fields": [
            {"key": "chf", "label": "Congestive Heart Failure (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "htn", "label": "Hypertension (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "age75", "label": "Age ≥ 75 (2=Yes, 0=No)", "placeholder": "2 or 0"},
            {"key": "dm", "label": "Diabetes Mellitus (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "stroke", "label": "Prior Stroke/TIA (2=Yes, 0=No)", "placeholder": "2 or 0"},
            {"key": "vasc", "label": "Vascular Disease (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "age65", "label": "Age 65-74 (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "female", "label": "Sex Category (Female=1, Male=0)", "placeholder": "0 or 1"}
        ],
        "formula_text": "Sum of scores (Age≥75 and Stroke = 2 points each)",
        "formula": "chf + htn + age75 + dm + stroke + vasc + age65 + female",
        "unit": "points",
        "interpretation": "0 (Male) / 1 (Female): Low risk.\n1 (Male) / 2 (Female): Consider anticoagulation.\n≥ 2 (Male) / ≥ 3 (Female): Oral anticoagulation recommended.",
        "reference": "Lip et al. (2010). ESC Guidelines."
    },
    "HAS-BLED Score": {
        "description": "Assesses the risk of major bleeding in patients on anticoagulation for atrial fibrillation.",
        "fields": [
            {"key": "htn", "label": "Uncontrolled Hypertension (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "renal", "label": "Renal disease (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "liver", "label": "Liver disease (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "stroke", "label": "Prior Stroke (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "bleed", "label": "Bleeding history (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "labile", "label": "Labile INR (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "elderly", "label": "Age > 65 (1=Yes, 0=No)", "placeholder": "0 or 1"},
            {"key": "drugs", "label": "Drugs/Alcohol (1=Yes, 0=No)", "placeholder": "0 or 1"}
        ],
        "formula_text": "Sum of scores",
        "formula": "htn + renal + liver + stroke + bleed + labile + elderly + drugs",
        "unit": "points",
        "interpretation": "0-2: Low risk.\n≥ 3: High risk of bleeding (requires caution, but does NOT automatically contraindicate anticoagulation).",
        "reference": "Pisters et al. (2010)."
    },
    "Child-Pugh Score": {
        "description": "Assesses the prognosis and severity of chronic liver disease (cirrhosis).",
        "fields": [
            {"key": "bili", "label": "Bilirubin (<2=1, 2-3=2, >3=3)", "placeholder": "1, 2, or 3"},
            {"key": "alb", "label": "Albumin (>3.5=1, 2.8-3.5=2, <2.8=3)", "placeholder": "1, 2, or 3"},
            {"key": "inr", "label": "INR (<1.7=1, 1.7-2.3=2, >2.3=3)", "placeholder": "1, 2, or 3"},
            {"key": "ascites", "label": "Ascites (None=1, Mild=2, Severe=3)", "placeholder": "1, 2, or 3"},
            {"key": "encep", "label": "Encephalopathy (None=1, Mild=2, Severe=3)", "placeholder": "1, 2, or 3"}
        ],
        "formula_text": "Sum of scores (range 5-15)",
        "formula": "bili + alb + inr + ascites + encep",
        "unit": "points",
        "interpretation": "5-6: Class A (well-compensated).\n7-9: Class B (significant functional compromise).\n10-15: Class C (decompensated, poor prognosis).",
        "reference": "Child & Turcotte (1964); Pugh et al. (1973)."
    }
}