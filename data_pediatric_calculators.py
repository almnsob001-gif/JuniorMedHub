# ==============================================================================
# ملف حاسبات الأطفال (Pediatric Calculators) - النسخة المصححة
# ==============================================================================

PEDIATRIC_CALCULATORS_DATA = {
    "Pediatric Calculators": {
        "General": [
            "Pediatric Weight Estimation (APLS)",
            "Pediatric ETT Size (Uncuffed)", "Pediatric ETT Size (Cuffed)", "Pediatric ETT Depth",
            "Pediatric Defibrillation Energy (First)", "Pediatric Defibrillation Energy (Subsequent)",
            "Pediatric Epinephrine (Cardiac Arrest)", "Pediatric Adrenaline IM (Anaphylaxis)",
            "Pediatric Fluid Bolus", "Pediatric Tidal Volume (Lung Protective)",
            "Pediatric Creatinine Clearance (Schwartz)", "Pediatric Vancomycin Dose",
            "Pediatric Fluid Deficit", "Pediatric Parkland Formula", "Pediatric Maintenance Fluids"
        ]
    }
}

PEDIATRIC_CALCULATOR_DEFINITIONS = {
    "Pediatric Weight Estimation (APLS)": {
        "description": "Estimates weight in children aged 1-10 years using the APLS formula.",
        "fields": [{"key": "age", "label": "Age (years, 1-10)", "placeholder": "e.g., 5"}],
        "formula_text": "Weight = (Age + 4) × 2", "formula": "(age + 4) * 2", "unit": "kg",
        "interpretation": "Useful in emergencies when weight is unknown.\nFor children < 1 year, use standard growth charts.",
        "reference": "APLS Guidelines."
    },
    "Pediatric ETT Size (Uncuffed)": {
        "description": "Estimates uncuffed endotracheal tube size for children.",
        "fields": [{"key": "age", "label": "Age (years)", "placeholder": "e.g., 5"}],
        "formula_text": "Size = (Age / 4) + 4", "formula": "(age / 4) + 4", "unit": "mm",
        "interpretation": "Uncuffed ETT (internal diameter in mm).",
        "reference": "APLS Guidelines."
    },
    "Pediatric ETT Size (Cuffed)": {
        "description": "Estimates cuffed endotracheal tube size for children.",
        "fields": [{"key": "age", "label": "Age (years)", "placeholder": "e.g., 5"}],
        "formula_text": "Size = (Age / 4) + 3.5", "formula": "(age / 4) + 3.5", "unit": "mm",
        "interpretation": "Cuffed ETT (internal diameter in mm).",
        "reference": "APLS Guidelines."
    },
    "Pediatric ETT Depth": {
        "description": "Estimates oral ETT insertion depth at the lip.",
        "fields": [{"key": "ett", "label": "ETT Size (mm)", "placeholder": "e.g., 5.0"}],
        "formula_text": "Depth (cm) = ETT Size × 3", "formula": "ett * 3", "unit": "cm",
        "interpretation": "Depth at lip (cm). Confirm with capnography and chest auscultation.",
        "reference": "APLS Guidelines."
    },
    "Pediatric Defibrillation Energy (First)": {
        "description": "First shock energy for pediatric defibrillation.",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Energy = 2 J/kg", "formula": "2 * wt", "unit": "J",
        "interpretation": "First defibrillation dose: 2 J/kg.",
        "reference": "AHA 2025 PALS Guidelines."
    },
    "Pediatric Defibrillation Energy (Subsequent)": {
        "description": "Subsequent shock energy for pediatric defibrillation.",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Energy = 4 J/kg (max 10 J/kg or adult dose, capped at 360 J)",
        "formula": "min(4 * wt, 360)",
        "unit": "J",
        "interpretation": "Second and subsequent shocks: 4 J/kg (max 10 J/kg or adult dose).\nCapped at 360 J (standard adult maximum).",
        "reference": "AHA 2025 PALS Guidelines."
    },
    "Pediatric Epinephrine (Cardiac Arrest)": {
        "description": "Epinephrine dose for pediatric cardiac arrest (IV/IO).",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Dose = 0.01 mg/kg (max 1 mg)", "formula": "min(0.01 * wt, 1)", "unit": "mg",
        "interpretation": "Give 1:10,000 concentration. Repeat every 3-5 mins.\nVolume in mL = Dose × 10 (since 1:10,000 = 0.1 mg/mL).",
        "reference": "AHA 2025 PALS Guidelines."
    },
    "Pediatric Adrenaline IM (Anaphylaxis)": {
        "description": "IM adrenaline dose for pediatric anaphylaxis.",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Dose = 0.01 mg/kg (max 0.5 mg)", "formula": "min(0.01 * wt, 0.5)", "unit": "mg",
        "interpretation": "Use 1:1000 concentration (1 mg/mL).\nVolume in mL = Dose (since 1:1000 = 1 mg/mL).\nAlternative age-based: <6mo 150 mcg, 6mo-6yr 150 mcg, 6-12yr 300 mcg, >12yr 500 mcg.",
        "reference": "Resuscitation Council UK."
    },
    "Pediatric Fluid Bolus": {
        "description": "Standard fluid bolus for pediatric resuscitation.",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Volume = 20 mL/kg (10 mL/kg if cardiac)", "formula": "20 * wt", "unit": "mL",
        "interpretation": "Use 10 mL/kg in cardiac or renal disease or DKA (without shock).\nReassess after each bolus.",
        "reference": "APLS; Surviving Sepsis Pediatric Guidelines."
    },
    "Pediatric Tidal Volume (Lung Protective)": {
        "description": "Tidal volume for mechanical ventilation in children.",
        "fields": [{"key": "wt", "label": "Ideal Body Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Vt = 6 mL/kg IBW", "formula": "6 * wt", "unit": "mL",
        "interpretation": "Lung-protective: 6 mL/kg IBW (range 5-8).\nUse Ideal Body Weight, not actual.",
        "reference": "PALICC-2; ARDSNet."
    },
    "Pediatric Creatinine Clearance (Schwartz)": {
        "description": "Estimates GFR in children using the bedside Schwartz formula.",
        "fields": [
            {"key": "ht", "label": "Height (cm)", "placeholder": "e.g., 100"},
            {"key": "cr", "label": "Serum Creatinine (mg/dL)", "placeholder": "e.g., 0.5"}
        ],
        "formula_text": "eGFR = (0.413 × Height) / Creatinine", "formula": "(0.413 * ht) / cr", "unit": "mL/min/1.73m²",
        "interpretation": "Bedside Schwartz formula (2009).\nValid for children 1-16 years.",
        "reference": "Schwartz et al. (2009)."
    },
    "Pediatric Vancomycin Dose": {
        "description": "Standard vancomycin dose for pediatric severe infections (max 750 mg/dose).",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"}],
        "formula_text": "Dose = 15 mg/kg per dose (max 750 mg/dose)",
        "formula": "min(15 * wt, 750)",
        "unit": "mg",
        "interpretation": "Typical: 15 mg/kg q6h (max 750 mg/dose).\nAdjust per renal function and levels.\nConsider 60-80 mg/kg/day divided q6h for severe MRSA.",
        "reference": "IDSA; PIDS Guidelines."
    },
    "Pediatric Fluid Deficit": {
        "description": "Calculates fluid deficit in pediatric dehydration.",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 10"},
            {"key": "pct", "label": "Dehydration (%)", "placeholder": "e.g., 5"}
        ],
        "formula_text": "Deficit = Weight × %Dehydration × 10", "formula": "wt * pct * 10", "unit": "mL",
        "interpretation": "Give as 0.9% NaCl (or per protocol) over 24-48 hours.\nAdd maintenance fluids separately.",
        "reference": "WHO; NICE Guidelines."
    },
    "Pediatric Parkland Formula": {
        "description": "Burn fluid resuscitation for children (per 24 hours).",
        "fields": [
            {"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 20"},
            {"key": "tbsa", "label": "TBSA (%)", "placeholder": "e.g., 20"}
        ],
        "formula_text": "Total = 4 × Weight × %TBSA (Ringer's Lactate)", "formula": "4 * wt * tbsa", "unit": "mL",
        "interpretation": "Give 50% in first 8h, 50% in next 16h.\nFor children, also add maintenance fluids (Holliday-Segar).",
        "reference": "Baxter & Shires; ABA Guidelines."
    },
    "Pediatric Maintenance Fluids": {
        "description": "Daily maintenance fluid (Holliday-Segar formula).",
        "fields": [{"key": "wt", "label": "Weight (kg)", "placeholder": "e.g., 15"}],
        "formula_text": "4 mL/kg (first 10 kg) + 2 mL/kg (next 10 kg) + 1 mL/kg (>20 kg)",
        "formula": "(4 * wt) if wt <= 10 else (40 + 2 * (wt - 10)) if wt <= 20 else (60 + 1 * (wt - 20))",
        "unit": "mL/day",
        "interpretation": "Divide by 24 for hourly rate.\nMaximum 100 mL/hour in most children.",
        "reference": "Holliday & Segar (1957)."
    }
}
