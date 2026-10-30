# data_surgical.py

SURGICAL_DATA = {
    "Surgical & Trauma": {
        "General Surgery - Acute Abdomen": [
            "Acute Abdomen and Surgical Peritonitis",
            "Acute Appendicitis and Perforated Appendix",
            "Acute Intestinal Obstruction",
            "Incarcerated and Strangulated Hernia",
            "Perforated Peptic Ulcer",
            "Acute Gastrointestinal Bleeding",
            "Acute Mesenteric Ischemia",
            "Sigmoid and Cecal Volvulus",
            "Acute Colonic Pseudo-Obstruction",
            "Toxic Megacolon and Fulminant Colitis",
            "Intra-Abdominal Abscess and Postoperative Sepsis",
            "Esophageal Perforation",
            "Esophageal Food Bolus Impaction",
            "Testicular Torsion and Acute Scrotum",
            "Acute Urinary Retention",
            "Acute Gastric Dilatation and Gastric Ischemia",
            "Acute Ischemic Colitis"
        ],
        "Hepatobiliary & Pancreatic": [
            "Acute Pancreatitis and Complications",
            "Acute Cholecystitis and Acute Cholangitis",
            "Gallbladder Perforation and Complicated Cholecystitis",
            "Infected Pancreatic Necrosis and Pancreatic Abscess",
            "Acute Liver Failure Requiring Emergency Transplant Evaluation",
            "Acute Cholangitis with Septic Shock"
        ],
        "Vascular Surgery": [
            "Ruptured Abdominal Aortic Aneurysm",
            "Acute Limb Ischemia",
            "Acute Mesenteric Venous Thrombosis"
        ],
        "Trauma Surgery": [
            "Abdominal Trauma and Solid Organ Injury",
            "Penetrating Abdominal Trauma",
            "Chest Trauma and Tension Pneumothorax",
            "Open Fractures and Limb-Threatening Injuries",
            "Acute Compartment Syndrome",
            "Complex Soft-Tissue Defects and Extensive Skin Loss",
            "Massive Hemothorax",
            "Flail Chest and Severe Chest Wall Injury",
            "Cardiac Tamponade Following Chest Trauma",
            "Acute Surgical Bleeding and Hemorrhagic Shock"
        ],
        "Surgical Infection": [
            "Necrotizing Soft Tissue Infection",
            "Fournier Gangrene and Perineal Sepsis",
            "Descending Necrotizing Mediastinitis"
        ],
        "Postoperative & Perioperative Complications": [
            "Anastomotic Leak Following Gastrointestinal Surgery",
            "Postoperative Bowel Obstruction and Prolonged Ileus",
            "Postoperative Hemorrhage and Hematoma",
            "Abdominal Wound Dehiscence and Evisceration",
            "Stoma Complications: Ischemia, Retraction, Prolapse, and Obstruction",
            "Postoperative Sepsis and Septic Shock",
            "Acute Abdominal Compartment Syndrome",
            "Suspected Iatrogenic Intra-abdominal Organ Injury",
            "Postoperative Respiratory Deterioration",
            "Retained Surgical Foreign Body",
            "Acute Abdominal Compartment Syndrome After Major Resuscitation"
        ],
        "Colorectal Surgery": [
            "Acute Perianal and Perirectal Abscess"
        ],
        "Burns & Environmental": [
            "Major Burns and Burn Shock",
            "Inhalation Injury and Airway Burns",
            "Electrical Burns and High-Voltage Electrical Injury",
            "Chemical Burns and Emergency Decontamination"
        ],
        "Thoracic Surgery": [
            "Empyema Requiring Urgent Drainage"
        ]
    }
}

SURGICAL_TOPICS = {}

# ==================== GENERAL SURGERY - ACUTE ABDOMEN ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Abdomen and Surgical Peritonitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute abdomen is a sudden or rapidly progressive abdominal condition that may require urgent surgical evaluation or intervention.\n"
     "Peritonitis is inflammation of the peritoneum, commonly caused by perforation, leakage of GI contents, ischemia, or intra-abdominal infection.\n\n"
     "[color=#991B1B]Red flags:[/color]\n"
     "• Severe, sudden-onset, or rapidly worsening abdominal pain.\n"
     "• Involuntary guarding, rigidity, or rebound tenderness.\n"
     "• Abdominal distension with persistent vomiting or inability to pass stool/flatus.\n"
     "• Fever, tachycardia, hypotension, altered mental status, or oliguria.\n"
     "• GI bleeding or signs of bowel ischemia.\n"
     "• Pain out of proportion to physical examination.\n\n"
     "[color=#1E3A8A]Differential:[/color] Perforated peptic ulcer, appendicitis, obstruction/strangulation, mesenteric ischemia, pancreatitis, cholecystitis/cholangitis, ruptured AAA, ectopic pregnancy, trauma, gastroenteritis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment: identify shock, respiratory compromise, altered consciousness, sepsis.\n"
     "• Provide supplemental oxygen for hypoxemia.\n"
     "• Call the surgical team early for generalized peritonitis, suspected perforation, bowel ischemia, strangulation, or hemodynamic instability.\n"
     "• Do not delay surgical consultation while waiting for imaging or labs.\n"
     "• Keep patient nil by mouth (NPO).\n"
     "• Establish two large-bore IV cannulas in shock, major bleeding, or suspected laparotomy.\n"
     "• Fluid resuscitation: isotonic crystalloid (e.g., Lactated Ringer's or 0.9% NaCl). In hypoperfusion, give 500 mL bolus and reassess.\n"
     "• Provide timely analgesia (opioids titrated).\n"
     "• Start IV antibiotics promptly when peritonitis, perforation, complicated intra-abdominal infection, or sepsis is suspected.\n"
     "• Consider urinary catheter (shock/critically ill) and NG tube (persistent vomiting, distension, obstruction)."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Bedside:[/color] Vital signs, glucose, ECG (if indicated), pregnancy test, bedside ultrasound.\n\n"
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, LFTs/bilirubin, lipase, blood gas/lactate, CRP, coagulation, group & screen/crossmatch, blood cultures (if sepsis), urinalysis.\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT abdomen/pelvis with IV contrast: preferred in many stable adults when diagnosis uncertain or serious cause suspected.\n"
     "• Ultrasound: useful for biliary disease, AAA, free fluid, pelvic/pregnancy conditions.\n"
     "• Plain radiographs: may show obstruction/free air, but normal does not exclude surgical emergency.\n"
     "• [color=#991B1B]In unstable patient with peritonitis or time-critical emergency, resuscitation and urgent surgery take priority over CT.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Crystalloid Fluids[/color]\n"
     "• Adult hypoperfusion: 500 mL IV isotonic crystalloid initial bolus, then reassess.\n"
     "• Monitor BP, pulse, capillary refill, mental status, lung exam, urine output. Avoid repeated large-volume boluses without reassessment.\n\n"
     "[color=#1E3A8A]2. Analgesia: Fentanyl[/color]\n"
     "• Adult: 25–50 mcg IV slowly, titrated to pain and response. Use lower doses in frail/elderly/unstable.\n"
     "• Monitor respiratory rate, SpO2, BP, consciousness.\n\n"
     "[color=#1E3A8A]3. Alternative Analgesia: Paracetamol[/color]\n"
     "• Adult: 1 g IV over ~15 min. Adjust for low body weight, liver disease, malnutrition.\n\n"
     "[color=#1E3A8A]4. Empiric Antibiotics (Example)[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (for selected community-acquired infections).\n"
     "• Broader coverage may be needed for septic shock, healthcare-associated infection, or resistant organisms."),
    ("05 — SURGICAL MANAGEMENT", "info", 
     "Urgent operative assessment indicated for:\n"
     "• Generalized peritonitis.\n"
     "• GI perforation with contamination.\n"
     "• Strangulated/ischemic bowel, necrosis, suspected mesenteric ischemia.\n"
     "• Uncontrolled intra-abdominal bleeding.\n"
     "• Intra-abdominal infection requiring urgent source control.\n\n"
     "Procedures: laparotomy or laparoscopy, repair of perforation, bowel resection, drainage, control of bleeding.\n"
     "Consider damage-control surgery in profoundly deranged patients."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate OR/emergency surgical pathway: generalized peritonitis, suspected perforation, bowel ischemia, strangulation, uncontrolled bleeding, clinical deterioration.\n"
     "• ICU/high-dependency: persistent shock, vasopressor requirement, respiratory failure, severe sepsis, major organ dysfunction.\n"
     "• Admit for observation, further investigations, or specialist review.\n"
     "• Discharge only when dangerous cause excluded, symptoms controlled, stable, and clear follow-up arranged."),
    ("REFERENCES", "info", "WSES Guidelines on intra-abdominal emergencies; Surviving Sepsis Campaign; ACR Appropriateness Criteria; NICE Sepsis Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Appendicitis and Perforated Appendix")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute appendicitis is inflammation of the vermiform appendix. Delayed treatment may lead to perforation, abscess, peritonitis, and sepsis.\n"
     "• Periumbilical pain migrating to right lower quadrant.\n"
     "• Anorexia, nausea, vomiting.\n"
     "• RLQ tenderness, sometimes guarding. Fever, tachycardia. Pain aggravated by movement/coughing.\n\n"
     "[color=#991B1B]Complicated appendicitis:[/color] Generalized tenderness/rigidity, persistent fever/systemic toxicity, hypotension, altered mental status, oliguria, imaging evidence of perforation/abscess.\n\n"
     "[color=#1E3A8A]Differential:[/color] Ectopic pregnancy, ovarian torsion, PID, mesenteric adenitis, gastroenteritis, terminal ileitis/Crohn's, ureteric stone/UTI, Meckel's diverticulitis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment; identify shock or sepsis.\n"
     "• Keep NPO. Establish IV access and obtain blood samples.\n"
     "• Provide appropriate analgesia and antiemetics.\n"
     "• Give isotonic IV fluids if dehydrated or hypoperfused.\n"
     "• Request early general surgical assessment.\n"
     "• Obtain pregnancy test when pregnancy is possible.\n"
     "• Start appropriate antibiotics when complicated appendicitis is suspected or surgery is planned.\n"
     "• In generalized peritonitis or septic shock, initiate resuscitation and antibiotics promptly while arranging urgent source control."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC with differential, CRP, electrolytes/urea/creatinine, LFTs (if indicated), urinalysis, pregnancy test, venous blood gas/lactate (if sepsis/hypoperfusion), blood cultures (if severe sepsis, without delaying antibiotics).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• Ultrasound: useful in children, pregnancy, selected patients.\n"
     "• CT abdomen/pelvis with IV contrast: commonly preferred in nonpregnant adults when diagnosis uncertain or complications suspected.\n"
     "• MRI: option during pregnancy when ultrasound inconclusive.\n"
     "• [color=#991B1B]Normal early WBC/CRP does not exclude appendicitis.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluids[/color]\n"
     "• If hypoperfusion: initial 500 mL isotonic crystalloid bolus, then reassess. Repeat per response, comorbidities, losses.\n\n"
     "[color=#1E3A8A]2. Analgesia: Paracetamol[/color]\n"
     "• Adult: 1 g IV or orally. Adjust for low body weight, liver disease, malnutrition.\n\n"
     "[color=#1E3A8A]3. Analgesia: Fentanyl[/color]\n"
     "• Adult: 25–50 mcg IV slowly, titrated in monitored setting.\n\n"
     "[color=#1E3A8A]4. Antibiotics for Appendicitis Requiring Surgery[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours.\n"
     "• Administer before incision. Review allergies, renal/hepatic function, local resistance.\n"
     "• After uncomplicated appendectomy with adequate source control, postoperative antibiotics generally not required.\n"
     "• Complicated appendicitis requires antibiotics after source control; duration per clinical response and local guidance."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Uncomplicated Appendicitis[/color]\n"
     "• Laparoscopic appendectomy is standard definitive treatment where available.\n"
     "• Selected patients may be offered antibiotics-first treatment after surgical assessment (when imaging confirms uncomplicated disease, no appendicolith, no perforation). Explain risk of failure/recurrence.\n\n"
     "[color=#1E3A8A]Perforated Appendicitis[/color]\n"
     "• Generalized peritonitis or uncontrolled sepsis: urgent operative assessment and source control.\n"
     "• Localized abscess/phlegmon: antibiotics, with image-guided drainage when appropriate. Interval appendectomy considered selectively."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Confirmed appendicitis suitable for operative management.\n"
     "• Perforation with generalized peritonitis.\n"
     "• Clinical deterioration or uncontrolled infection.\n"
     "• Failure of nonoperative management.\n"
     "• Complications requiring source control."),
    ("07 — DISPOSITION", "warning", 
     "• Admit for surgery, IV antibiotics, or observation for complications.\n"
     "• ICU for septic shock or organ failure.\n"
     "• Discharge only when safe nonoperative plan established, symptoms controlled, and follow-up/return precautions clear."),
    ("REFERENCES", "info", "WSES Jerusalem Guidelines; SAGES Guidelines; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Intestinal Obstruction")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute intestinal obstruction is partial or complete blockage of small or large bowel. Strangulation, ischemia, and perforation are life-threatening.\n"
     "• Causes: Postoperative adhesions, incarcerated/strangulated hernia, colorectal cancer, volvulus, intussusception, inflammatory strictures, fecal impaction.\n"
     "• Colicky abdominal pain, vomiting (early/prominent in small bowel), distension, constipation/inability to pass flatus.\n"
     "• High-pitched bowel sounds early, reduced in advanced disease.\n\n"
     "[color=#991B1B]Red flags for strangulation/ischemia:[/color] Continuous severe pain, localized/generalized peritonitis, fever/tachycardia/hypotension/acidosis, bloody stool, elevated lactate (early normal does not exclude), CT findings of closed-loop/reduced enhancement/pneumatosis/free air."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment and treatment of shock.\n"
     "• Keep NPO. Insert IV access and begin isotonic fluids as indicated.\n"
     "• Request urgent surgical assessment.\n"
     "• Correct electrolyte disturbances.\n"
     "• Consider NG tube for persistent vomiting, marked distension, or significant obstruction.\n"
     "• Monitor urine output in seriously ill or requiring substantial fluid resuscitation.\n"
     "• Provide analgesia and antiemetics.\n"
     "• Start broad-spectrum IV antibiotics when strangulation, ischemia, perforation, or sepsis suspected.\n"
     "• [color=#991B1B]Do NOT administer laxatives or bowel preparations when mechanical obstruction or perforation suspected.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, venous blood gas/lactate (if ischemia/shock), CRP, LFTs (if indicated), group & screen/crossmatch (if surgery likely), coagulation (severe illness/pre-op).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT abdomen/pelvis with IV contrast: preferred in many adults to identify transition point, cause, closed-loop, ischemia, perforation. Do not delay surgery if clear peritonitis or profound instability.\n"
     "• Abdominal radiography: may show dilated loops/air-fluid levels. Normal does not exclude obstruction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluid Resuscitation[/color]\n"
     "• Adult hypoperfusion: 500 mL isotonic crystalloid, then reassess. Further replacement depends on BP, perfusion, vomiting, NG losses, urine output, comorbidities.\n\n"
     "[color=#1E3A8A]2. Electrolyte Replacement[/color]\n"
     "• Replace potassium, magnesium, etc. per measured values and protocols. Check renal function and urine output before K+ replacement. Never give concentrated KCl IV push.\n\n"
     "[color=#1E3A8A]3. Antiemetic: Ondansetron[/color]\n"
     "• Adult: 4 mg IV slowly. Caution with prolonged QT, hypokalemia, hypomagnesemia.\n\n"
     "[color=#1E3A8A]4. Antibiotics for Suspected Strangulation/Perforation[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (selected community-acquired). Broader for healthcare-associated or septic shock."),
    ("05 — NONOPERATIVE MANAGEMENT", "info", 
     "Trial of nonoperative treatment may be appropriate for selected adhesive SBO without peritonitis, strangulation, ischemia, or perforation.\n"
     "• NPO, IV fluids/electrolytes, NG decompression, repeated abdominal exams/vitals, surgical reassessment if worsening.\n"
     "• Water-soluble contrast protocols may assist assessment in selected adhesive obstructions under local protocol."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Peritonitis or suspected perforation.\n"
     "• Strangulation, ischemia, or closed-loop obstruction.\n"
     "• Incarcerated hernia causing obstruction.\n"
     "• Clinical deterioration despite resuscitation.\n"
     "• Failure of appropriate nonoperative trial.\n"
     "• Obstruction caused by lesion requiring operative treatment."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with confirmed mechanical obstruction.\n"
     "• ICU for shock, severe sepsis, or organ failure.\n"
     "• Discharge only when obstruction excluded or safe resolution and follow-up plan established."),
    ("REFERENCES", "info", "WSES Bologna Guidelines; ACR Appropriateness Criteria; WSES Bowel Ischemia Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Incarcerated and Strangulated Hernia")] = [
    ("01 — RECOGNIZE", "info", 
     "Incarcerated hernia contains tissue that cannot be reduced. Strangulated hernia has compromised blood supply, may progress to bowel necrosis, perforation, septic shock.\n"
     "• Types: Inguinal, femoral, umbilical, incisional, other abdominal wall hernias.\n"
     "• Painful, tender, irreducible swelling. Increasing pain/swelling. Nausea, vomiting, distension, obstipation. Skin erythema/discoloration.\n"
     "• Fever, tachycardia, systemic toxicity.\n\n"
     "[color=#991B1B]Features suggesting strangulation:[/color] Severe continuous pain, marked tenderness/skin changes, peritonitis, obstruction with systemic deterioration, elevated lactate or CT evidence of compromised bowel perfusion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment. Keep NPO.\n"
     "• Establish IV access and obtain blood samples.\n"
     "• Provide analgesia and IV fluids when indicated.\n"
     "• Request urgent surgical assessment.\n"
     "• [color=#991B1B]Do NOT repeatedly attempt forceful manual reduction.[/color]\n"
     "• If strangulation, peritonitis, or bowel ischemia suspected: proceed toward urgent operative management without delaying for unnecessary imaging.\n"
     "• Give antibiotics when bowel compromise, perforation, or operative contamination suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/urea/creatinine, venous blood gas/lactate (if ischemia/shock), group & screen/crossmatch (if emergency surgery likely).\n"
     "• CT abdomen/pelvis with IV contrast in selected stable patients when diagnosis or extent of obstruction unclear.\n"
     "• Ultrasound may help assess selected hernias when expertise available.\n"
     "• [color=#991B1B]Imaging is not required before surgery when strangulation is clinically evident and delay would be dangerous.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Analgesia: Fentanyl[/color]\n"
     "• Adult: 25–50 mcg IV slowly, titrated in monitored environment.\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Adult hypoperfusion: initial 500 mL isotonic crystalloid bolus, reassess. Tailor to cardiac/renal function.\n\n"
     "[color=#1E3A8A]3. Perioperative Antibiotics[/color]\n"
     "• Cefazolin 2 g IV before incision for clean hernia repair (3 g if ≥120 kg per prophylaxis protocol).\n"
     "• If strangulation with suspected bowel necrosis/contamination: use therapeutic antibiotic regimen for intra-abdominal infection."),
    ("05 — MANUAL REDUCTION", "info", 
     "Consider only in selected patients with acutely irreducible hernia when there are NO clinical features of strangulation, ischemia, or peritonitis, and an experienced clinician judges it appropriate.\n"
     "• Provide monitored analgesia. Use gentle, sustained pressure (not forceful).\n"
     "• Stop immediately if pain worsens or reduction unsuccessful.\n"
     "• Arrange surgical assessment after reduction (complications can persist despite apparent disappearance).\n"
     "• [color=#991B1B]Do NOT attempt manual reduction when strangulation suspected (may return nonviable bowel to abdomen and mask continuing ischemia).[/color]"),
    ("06 — SURGICAL MANAGEMENT", "warning", 
     "Urgent surgery indicated for:\n"
     "• Suspected strangulation.\n"
     "• Peritonitis or bowel ischemia.\n"
     "• Obstruction caused by irreducible hernia.\n"
     "• Failed or inappropriate manual reduction.\n"
     "• Clinical deterioration.\n\n"
     "Operative management: reduction, assessment of bowel viability, bowel resection if necessary, hernia repair. Choice of mesh/technique depends on contamination, tissue condition, operative findings."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with suspected strangulation, obstruction, or emergency operative repair.\n"
     "• Monitor closely after successful manual reduction and obtain surgical review.\n"
     "• ICU care may be needed after bowel resection, severe sepsis, or hemodynamic instability."),
    ("REFERENCES", "info", "WSES Guidelines for emergency repair of complicated abdominal wall hernias; HerniaSurge Guidelines; Surgical Infection Society Guidance.")
]

# ==================== HEPATOBILIARY & PANCREATIC ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Pancreatitis and Complications")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute pancreatitis is acute inflammation of the pancreas. Common causes: gallstones, alcohol; others: hypertriglyceridemia, medications, metabolic/procedural.\n"
     "• Severe epigastric pain radiating to back. Nausea, vomiting. Epigastric tenderness. Distension/ileus. Tachycardia, dehydration.\n"
     "• Severe: hypoxemia, hypotension, AKI, shock.\n\n"
     "[color=#991B1B]Features of severe disease:[/color] Persistent organ failure, hypotension/shock, hypoxemia/respiratory failure, oliguria/AKI, altered mental status, infected necrosis/complication."),
    ("02 — DIAGNOSTIC CRITERIA", "info", 
     "Diagnosis requires at least 2 of 3:\n"
     "• Characteristic abdominal pain.\n"
     "• Serum lipase or amylase ≥ 3 times upper limit of normal.\n"
     "• Characteristic imaging findings.\n"
     "• Serum lipase generally preferred to amylase."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment. Identify shock, respiratory failure, organ dysfunction.\n"
     "• Establish IV access and obtain labs.\n"
     "• Give appropriately monitored isotonic crystalloid resuscitation.\n"
     "• Provide adequate analgesia and antiemetics.\n"
     "• Assess severity and arrange admission when indicated.\n"
     "• Start oral feeding early as tolerated in mild disease (do not keep every patient NPO for prolonged periods).\n"
     "• Investigate cause: gallstones, alcohol, hypertriglyceridemia.\n"
     "• [color=#991B1B]Do NOT prescribe prophylactic antibiotics for uncomplicated acute pancreatitis or sterile pancreatic necrosis.[/color]"),
    ("04 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, lipase, LFTs/bilirubin, glucose, calcium, triglycerides, CRP, blood gas/lactate (severe illness).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• RUQ ultrasound: first-line for gallstones/biliary dilatation.\n"
     "• CT abdomen with IV contrast: not routinely immediately when diagnosis clear and improving. Consider when diagnosis uncertain, deteriorating, or complications suspected. Contrast-enhanced CT more informative for necrosis after early phase.\n"
     "• MRCP or EUS: when CBD stone suspected but not demonstrated on initial imaging."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Lactated Ringer's Solution[/color]\n"
     "• Moderately aggressive, individualized fluid therapy.\n"
     "• If hypovolemia: initial bolus ~10 mL/kg, then reassess. In patients without shock, lower initial rate may be appropriate; avoid routine large-volume resuscitation without frequent reassessment.\n"
     "• Monitor BP, pulse, urine output, BUN, creatinine, hematocrit, oxygenation, signs of overload.\n\n"
     "[color=#1E3A8A]2. Analgesia: Fentanyl[/color]\n"
     "• Adult: 25–50 mcg IV slowly, titrated to pain in monitored setting.\n\n"
     "[color=#1E3A8A]3. Antiemetic: Ondansetron[/color]\n"
     "• Adult: 4 mg IV slowly or orally.\n\n"
     "[color=#1E3A8A]4. Antibiotics[/color]\n"
     "• Do NOT use prophylactic antibiotics in uncomplicated pancreatitis or sterile necrosis.\n"
     "• When infection suspected: obtain cultures, assess for cholangitis/infected necrosis, select antibiotics per source/severity/local resistance. Antibiotics do not treat sterile inflammation."),
    ("06 — NUTRITION & COMPLICATIONS", "info", 
     "[color=#1E3A8A]Nutrition[/color]\n"
     "• Mild: begin oral feeding early as tolerated (low-fat solid diet when tolerated; prolonged clear-liquid progression not essential).\n"
     "• Unable to eat: enteral nutrition preferred over parenteral when feasible.\n\n"
     "[color=#1E3A8A]Gallstone Pancreatitis[/color]\n"
     "• Arrange biliary assessment. Urgent ERCP if cholangitis or persistent biliary obstruction requiring intervention. Routine urgent ERCP not indicated without cholangitis/ongoing obstruction.\n"
     "• Cholecystectomy during same admission generally recommended for mild gallstone pancreatitis when fit for surgery. Severe disease/collections may require delayed surgery.\n\n"
     "[color=#1E3A8A]Infected Pancreatic Necrosis[/color]\n"
     "• Suspect with clinical deterioration, sepsis, compatible imaging. Use antibiotics when infection suspected/established.\n"
     "• Drainage/debridement may be required; delayed, step-up approach preferred when feasible. Immediate surgery not routinely required for every case of necrosis."),
    ("07 — SURGICAL/INTERVENTIONAL INDICATIONS", "warning", 
     "• Gallstone pancreatitis requiring definitive cholecystectomy.\n"
     "• Cholangitis or persistent biliary obstruction requiring ERCP/drainage.\n"
     "• Infected necrosis requiring drainage/debridement.\n"
     "• Complications requiring intervention (symptomatic/infected collections).\n"
     "• Abdominal compartment syndrome or other life-threatening complication requiring specialist management."),
    ("08 — DISPOSITION", "warning", 
     "• Admit for significant pain, vomiting, dehydration, systemic inflammation, or diagnostic uncertainty.\n"
     "• ICU for persistent organ failure, shock, respiratory failure, or severe metabolic disturbance.\n"
     "• Discharge after clinical improvement, adequate oral intake, controlled pain, and safe plan for underlying cause."),
    ("REFERENCES", "info", "ACG Clinical Guideline; AGA Guidance; Revised Atlanta Classification; WSES Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Cholecystitis and Acute Cholangitis")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]A. Acute Cholecystitis[/color]\n"
     "• Inflammation of gallbladder, most commonly cystic duct obstruction by gallstone.\n"
     "• Persistent RUQ pain, tenderness, positive Murphy's sign, fever, nausea, vomiting, leukocytosis.\n"
     "• Complicated: Gangrene/perforation, pericholecystic abscess, emphysematous cholecystitis, generalized peritonitis/sepsis.\n\n"
     "[color=#1E3A8A]B. Acute Cholangitis[/color]\n"
     "• Infection of biliary tree, usually with biliary obstruction. Can rapidly progress to sepsis/septic shock.\n"
     "• RUQ pain, fever/chills, jaundice (Charcot's triad; absence does not exclude).\n"
     "• Severe: hypotension, altered mental status, oliguria/AKI, respiratory failure, coagulopathy, organ dysfunction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE assessment. Identify sepsis, shock, organ dysfunction.\n"
     "• Keep NPO initially when urgent intervention likely.\n"
     "• Establish IV access and obtain labs.\n"
     "• Provide analgesia, antiemetics, fluids per clinical need.\n"
     "• Request early surgical assessment for acute cholecystitis.\n"
     "• Request urgent gastroenterology/endoscopy support for suspected cholangitis and biliary obstruction.\n"
     "• Start IV antibiotics promptly when cholangitis, complicated cholecystitis, or sepsis suspected.\n"
     "• In septic shock: initiate sepsis management and arrange urgent source control without waiting for all investigations."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, CRP, bilirubin, ALT/AST/ALP/GGT, electrolytes/urea/creatinine, lipase (gallstone pancreatitis), blood cultures (suspected cholangitis/severe infection), lactate/blood gas (shock/hypoperfusion), coagulation (severe illness/pre-intervention).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• RUQ ultrasound: first-line for acute cholecystitis (gallstones, wall thickening, pericholecystic fluid, sonographic Murphy's, duct dilatation).\n"
     "• MRCP or EUS: when CBD stone suspected and ultrasound inconclusive.\n"
     "• CT abdomen: complications or alternative diagnoses.\n"
     "• HIDA scan: when diagnosis uncertain after initial imaging and available."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluids[/color]\n"
     "• Adult hypoperfusion: initial 500 mL isotonic crystalloid bolus, then reassess. Further fluid per hemodynamics, losses, renal function, comorbidities.\n\n"
     "[color=#1E3A8A]2. Analgesia: Paracetamol[/color]\n"
     "• Adult: 1 g IV or orally. Adjust for liver disease, low body weight, malnutrition, total daily exposure.\n\n"
     "[color=#1E3A8A]3. Analgesia: Fentanyl[/color]\n"
     "• Adult: 25–50 mcg IV slowly, titrated in monitored setting.\n\n"
     "[color=#1E3A8A]4. Antibiotics (Community-Acquired Biliary Infection)[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (when additional anaerobic coverage indicated).\n"
     "• Start promptly for suspected cholangitis or complicated cholecystitis.\n"
     "• Narrow/adjust when microbiology and source-control status known.\n"
     "• Severe cholangitis, healthcare-associated infection, septic shock, resistant organisms may require broader regimen. Antibiotics do not replace drainage of obstructed infected biliary system."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Acute Cholecystitis[/color]\n"
     "• Early laparoscopic cholecystectomy preferred for most suitable patients. Perioperative antibiotics per severity/local guidance.\n"
     "• If not fit for surgery and gallbladder remains uncontrolled source: consider gallbladder drainage and specialist review.\n\n"
     "[color=#1E3A8A]Acute Cholangitis[/color]\n"
     "• Resuscitation and antibiotics essential, but biliary decompression often decisive.\n"
     "• ERCP generally preferred method of drainage when available/appropriate.\n"
     "• If ERCP unavailable/unsuccessful: alternative drainage or surgical options per local expertise.\n"
     "• Severe cholangitis with shock requires urgent drainage after initial resuscitation; do not delay source control unnecessarily."),
    ("06 — SURGICAL/INTERVENTIONAL INDICATIONS", "warning", 
     "• Acute cholecystitis suitable for early cholecystectomy.\n"
     "• Gallbladder gangrene, perforation, or abscess.\n"
     "• Failure of conservative treatment.\n"
     "• Acute cholangitis requiring biliary decompression.\n"
     "• Persistent CBD obstruction or stones requiring intervention.\n"
     "• Uncontrolled sepsis requiring source control."),
    ("07 — DISPOSITION", "warning", 
     "• Admit: confirmed acute cholecystitis requiring IV treatment/surgery, suspected cholangitis, persistent pain/vomiting/jaundice/systemic inflammation.\n"
     "• ICU/high-dependency: septic shock, persistent hypotension, respiratory failure, AKI, other organ dysfunction.\n"
     "• Discharge only selected stable patients after appropriate assessment and documented definitive treatment/follow-up plan."),
    ("REFERENCES", "info", "Tokyo Guidelines; WSES Guidelines for Acute Calculous Cholecystitis; ASGE Guidance; ACG Guidance.")
]


# ==================== BATCH 2 (TOPICS 7-16) ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Perforated Peptic Ulcer")] = [
    ("01 — RECOGNIZE", "info", 
     "Perforated peptic ulcer is a full-thickness defect in the stomach or duodenal wall that allows GI contents to enter the peritoneal cavity, causing chemical peritonitis followed by bacterial contamination and potentially septic shock.\n"
     "• Sudden severe epigastric pain that may rapidly become generalized.\n"
     "• Abdominal guarding, rigidity, and rebound tenderness. Reduced or absent bowel sounds.\n"
     "• Tachycardia, fever, hypotension, or altered mental status in advanced disease.\n"
     "• Risk factors: NSAIDs, aspirin, previous PUD, H. pylori, older age, comorbidities."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and identify shock.\n"
     "• Keep the patient nil by mouth.\n"
     "• Establish two large-bore IV lines in patients with shock or likely emergency surgery.\n"
     "• Begin isotonic crystalloid resuscitation with frequent reassessment.\n"
     "• Request immediate general surgical review.\n"
     "• Administer IV broad-spectrum antibiotics promptly.\n"
     "• Start IV proton pump inhibitor therapy according to local protocol.\n"
     "• Provide analgesia and antiemetics.\n"
     "• Consider nasogastric decompression in significant vomiting or gastric distension.\n"
     "• Prepare for emergency operative source control."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, LFTs, lipase, venous blood gas/lactate, coagulation, group & crossmatch, blood cultures.\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT abdomen/pelvis with IV contrast: preferred in many stable patients when perforation suspected. May show free air, fluid, site of perforation.\n"
     "• Erect chest radiograph: may show free subdiaphragmatic air when CT unavailable. Normal does not exclude perforation.\n"
     "• [color=#991B1B]Do NOT delay urgent surgical management for imaging in an unstable patient with convincing generalized peritonitis.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluid Resuscitation[/color]\n"
     "• Adult hypoperfusion: initial 500 mL isotonic crystalloid bolus, then reassess. Repeat per response and comorbidities.\n\n"
     "[color=#1E3A8A]2. Antibiotics[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (selected adults).\n"
     "• Severe sepsis, healthcare-associated infection, or resistant organisms may require broader coverage.\n\n"
     "[color=#1E3A8A]3. IV Proton Pump Inhibitor[/color]\n"
     "• Pantoprazole 40 mg IV every 24 hours (commonly used initial regimen). Higher-dose regimens may be selected by the treating team.\n"
     "• [color=#991B1B]PPI therapy does not close a perforation and must not delay surgery.[/color]\n\n"
     "[color=#1E3A8A]4. Analgesia[/color]\n"
     "• Titrated IV analgesia appropriate to severity and hemodynamic status. [color=#991B1B]Avoid NSAIDs.[/color]"),
    ("05 — SURGICAL MANAGEMENT", "info", 
     "Urgent operative repair is generally required for perforation with peritonitis or ongoing leakage.\n"
     "• Laparoscopic or open exploration.\n"
     "• Closure of the perforation, often with an omental patch.\n"
     "• Peritoneal lavage and source control.\n"
     "• More extensive surgery in selected cases.\n"
     "• Nonoperative management reserved for highly selected patients with sealed perforation and no generalized peritonitis under close surgical supervision."),
    ("06 — POSTOPERATIVE CARE", "info", 
     "• Continue antibiotics according to source-control adequacy and clinical response.\n"
     "• Provide PPI therapy.\n"
     "• Test for H. pylori and eradicate if present.\n"
     "• Avoid NSAIDs where possible and review ulcerogenic medications.\n"
     "• Monitor for leakage, abscess, sepsis, and postoperative ileus."),
    ("07 — DISPOSITION", "warning", 
     "• Emergency surgical admission.\n"
     "• ICU care for shock, organ dysfunction, or major postoperative complications.\n"
     "• Discharge only after clinical stabilization, adequate recovery, and documented ulcer-prevention plan."),
    ("REFERENCES", "info", "WSES Guidelines for perforated/bleeding peptic ulcer; ACG Guidance; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Gastrointestinal Bleeding")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute GI bleeding may arise from upper or lower GI tract. Severe bleeding can cause hemorrhagic shock and death.\n\n"
     "[color=#1E3A8A]Upper GI bleeding:[/color] Hematemesis or coffee-ground vomitus, melena, hematochezia (massive upper GI). Causes: PUD, varices, erosive gastritis, Mallory-Weiss tears.\n\n"
     "[color=#1E3A8A]Lower GI bleeding:[/color] Bright red or maroon rectal bleeding. Causes: diverticular bleeding, angiodysplasia, colorectal lesions, ischemic colitis, IBD.\n\n"
     "[color=#991B1B]Severe bleeding:[/color] Hypotension, tachycardia, syncope, altered mental status, cold extremities, poor perfusion, oliguria, ongoing large-volume bleeding."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Assess airway protection (massive hematemesis/reduced consciousness).\n"
     "• Establish two large-bore IV lines in significant bleeding.\n"
     "• Send CBC, coagulation, renal function, LFTs, type & crossmatch.\n"
     "• Begin resuscitation and activate major hemorrhage protocol when indicated.\n"
     "• Hold anticoagulants/antiplatelet drugs temporarily when clinically appropriate; assess need for reversal.\n"
     "• Arrange urgent gastroenterology or surgical consultation.\n"
     "• Consider IV PPI for suspected upper GI bleeding.\n"
     "• In suspected variceal bleeding: initiate vasoactive therapy and antibiotics promptly."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC and serial Hb, platelets, PT/INR, aPTT, urea/creatinine/electrolytes, LFTs, group & crossmatch, lactate/blood gas, medication review.\n\n"
     "[color=#1E3A8A]Risk Assessment:[/color] Glasgow-Blatchford Score (assists but must not override clinical evidence of shock/ongoing bleeding).\n\n"
     "[color=#1E3A8A]Endoscopy/Imaging:[/color]\n"
     "• Upper GI endoscopy after initial resuscitation (urgently in unstable severe bleeding; generally within 24 hours for admitted patients).\n"
     "• CT angiography for ongoing significant lower GI bleeding when actively bleeding.\n"
     "• Colonoscopy per clinical stability and suspected source."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Blood Component Therapy[/color]\n"
     "• Restrictive red-cell transfusion threshold around Hb 7 g/dL in many hemodynamically stable adults. Higher threshold may be appropriate for cardiovascular disease or ongoing ischemia.\n"
     "• In exsanguinating hemorrhage or shock, do NOT wait for Hb to fall below a numerical threshold before initiating blood resuscitation.\n\n"
     "[color=#1E3A8A]2. IV Proton Pump Inhibitor[/color]\n"
     "• IV pantoprazole for suspected nonvariceal upper GI bleeding per local protocol. High-dose PPI particularly relevant after endoscopic treatment of high-risk ulcer bleeding.\n\n"
     "[color=#1E3A8A]3. Suspected Variceal Bleeding: Octreotide[/color]\n"
     "• Adult: 50 mcg IV bolus, followed by 50 mcg/hour IV infusion when variceal hemorrhage suspected.\n"
     "• Adjunct, not a substitute for urgent endoscopic management.\n\n"
     "[color=#1E3A8A]4. Antibiotics for Suspected Variceal Bleeding in Cirrhosis[/color]\n"
     "• Ceftriaxone 1 g IV every 24 hours (commonly used in selected patients with cirrhosis and acute variceal hemorrhage)."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Nonvariceal Upper GI Bleeding[/color]\n"
     "• Endoscopic hemostasis for high-risk bleeding lesions. PPI therapy after appropriate endoscopic management. IR or surgery when bleeding cannot be controlled endoscopically.\n\n"
     "[color=#1E3A8A]Variceal Bleeding[/color]\n"
     "• Vasoactive therapy and antibiotics. Urgent endoscopy with appropriate variceal therapy. Specialist escalation for uncontrolled bleeding.\n\n"
     "[color=#1E3A8A]Severe Lower GI Bleeding[/color]\n"
     "• CT angiography and possible angiographic embolization in appropriate patients. Colonoscopy or surgery according to source, clinical stability, and treatment response."),
    ("06 — SURGICAL/INTERVENTIONAL INDICATIONS", "warning", 
     "• Persistent bleeding despite endoscopic treatment.\n"
     "• Hemodynamic instability despite resuscitation.\n"
     "• Bleeding requiring embolization or operative control.\n"
     "• Perforation or another associated surgical pathology."),
    ("07 — DISPOSITION", "warning", 
     "• Admit for significant bleeding, anemia, comorbidity, or need for intervention.\n"
     "• ICU for shock, airway compromise, massive transfusion, or organ dysfunction.\n"
     "• Outpatient management only for carefully selected low-risk patients after formal assessment."),
    ("REFERENCES", "info", "ACG Guidelines (upper & lower GI bleeding); Baveno VII; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Mesenteric Ischemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute mesenteric ischemia is an abrupt reduction in intestinal blood supply that may progress to bowel infarction, perforation, sepsis, and death.\n"
     "• Causes: Arterial embolism (AF), acute arterial thrombosis (atherosclerosis), mesenteric venous thrombosis, nonocclusive mesenteric ischemia (shock/vasoconstriction).\n"
     "• Sudden severe abdominal pain (often out of proportion to early physical findings). Nausea, vomiting, diarrhea.\n"
     "• Occult/overt GI bleeding. Later guarding, rigidity, peritonitis.\n"
     "• Shock or multiorgan dysfunction in advanced disease.\n"
     "• [color=#991B1B]A normal early lactate does not exclude mesenteric ischemia.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and resuscitate shock.\n"
     "• Request immediate surgical and vascular/interventional specialist assessment.\n"
     "• Keep the patient NPO.\n"
     "• Establish large-bore IV access and obtain urgent laboratory samples.\n"
     "• Arrange urgent CT angiography of the abdomen and pelvis when feasible.\n"
     "• Start broad-spectrum IV antibiotics (bowel ischemia can rapidly lead to bacterial translocation and sepsis).\n"
     "• Consider IV unfractionated heparin when arterial/venous thrombosis suspected and no contraindication, following urgent specialist assessment.\n"
     "• Do not delay intervention in a patient with peritonitis or strong evidence of bowel necrosis."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, venous/arterial blood gas and lactate, coagulation, group & crossmatch, LFTs, glucose, blood cultures (sepsis, without delaying antibiotics).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT angiography: preferred urgent investigation in suspected acute mesenteric ischemia. Identifies arterial/venous occlusion, bowel-wall abnormalities, associated complications.\n"
     "• [color=#991B1B]Do NOT rely on plain abdominal radiographs or a normal early lactate to exclude the diagnosis.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Resuscitation[/color]\n"
     "• Adult hypoperfusion: begin with 500 mL isotonic crystalloid and reassess. Further fluid guided by perfusion, losses, cardiac function, clinical response.\n\n"
     "[color=#1E3A8A]2. Broad-Spectrum Antibiotics[/color]\n"
     "• Example: Piperacillin–tazobactam 4.5 g IV, with subsequent dosing/interval determined by renal function, severity, and institutional protocol.\n\n"
     "[color=#1E3A8A]3. Anticoagulation: Unfractionated Heparin[/color]\n"
     "• When indicated for suspected arterial/venous thrombosis: use institution's therapeutic IV heparin nomogram. Monitor aPTT or anti-Xa. Monitor CBC, platelets, bleeding.\n"
     "• Coordinate with surgical team if emergency laparotomy required."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Arterial Occlusion[/color]\n"
     "• Endovascular revascularization or open embolectomy/thrombectomy. Resect nonviable bowel. Reassess viability and consider planned second-look operation.\n\n"
     "[color=#1E3A8A]Mesenteric Venous Thrombosis[/color]\n"
     "• Therapeutic anticoagulation is a mainstay when no contraindication. Surgery if peritonitis or bowel infarction develops.\n\n"
     "[color=#1E3A8A]Nonocclusive Mesenteric Ischemia[/color]\n"
     "• Correct precipitating low-flow state. Optimize cardiac output and perfusion. Reduce precipitating vasoconstrictors when feasible. Consider targeted intra-arterial vasodilator therapy in selected cases. Operate if bowel necrosis or peritonitis develops."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Peritonitis.\n"
     "• Suspected bowel infarction or perforation.\n"
     "• Clinical deterioration despite resuscitation.\n"
     "• Need for operative revascularization or bowel resection.\n"
     "• Uncertain bowel viability requiring direct assessment."),
    ("07 — DISPOSITION", "warning", 
     "• Emergency admission to a center capable of urgent vascular, endovascular, and abdominal surgical intervention.\n"
     "• ICU care for shock, metabolic acidosis, bowel resection, or organ failure."),
    ("REFERENCES", "info", "WSES Guidelines for acute mesenteric ischemia; ESVS Guidance; ACR Appropriateness Criteria.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Ruptured Abdominal Aortic Aneurysm")] = [
    ("01 — RECOGNIZE", "info", 
     "A ruptured abdominal aortic aneurysm (rAAA) is a life-threatening vascular emergency involving rupture of a dilated abdominal aorta with potentially massive internal hemorrhage.\n"
     "• Sudden severe abdominal, back, flank, or groin pain. Syncope or collapse. Hypotension or shock.\n"
     "• A pulsatile abdominal mass may be present but is not required for diagnosis.\n"
     "• Older age, smoking, hypertension, known aneurysm increase suspicion.\n"
     "• [color=#991B1B]The classic triad of abdominal pain, hypotension, and pulsatile mass is often incomplete.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate the emergency vascular surgery pathway immediately.\n"
     "• Perform ABCDE assessment and establish large-bore IV access.\n"
     "• Keep the patient NPO. Obtain blood samples and activate major hemorrhage protocol when indicated.\n"
     "• Prioritize blood products and avoid excessive crystalloid administration.\n"
     "• Use bedside aortic ultrasound if immediately available and it does not delay definitive care.\n"
     "• Do NOT transport a profoundly unstable patient to CT when clinical picture strongly supports rupture and vascular team is ready to intervene.\n"
     "• Prepare for emergency endovascular or open repair."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Bedside:[/color] Continuous ECG, SpO2, BP monitoring. Bedside aortic ultrasound (can identify aneurysm but cannot reliably exclude rupture). Focused ultrasound may identify free fluid.\n\n"
     "[color=#1E3A8A]Laboratory:[/color] CBC, blood group & crossmatch, coagulation, electrolytes/renal function, blood gas/lactate, fibrinogen.\n\n"
     "[color=#1E3A8A]Imaging:[/color] CT angiography: appropriate for patients sufficiently stable for scanning when it will guide repair. Defines aneurysm anatomy and suitability for EVAR."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Blood Product Resuscitation[/color]\n"
     "• Activate institutional major hemorrhage protocol for significant shock.\n"
     "• Transfuse blood components according to clinical status, ongoing blood loss, and protocol rather than waiting for a specific Hb threshold.\n"
     "• Monitor BP, perfusion, temperature, calcium, coagulation, fibrinogen, transfusion reactions. Use active warming.\n"
     "• [color=#991B1B]Excessive crystalloid can worsen dilutional coagulopathy and tissue edema.[/color]\n\n"
     "[color=#1E3A8A]2. Permissive Hypotension (Selected Patients)[/color]\n"
     "• In selected patients without TBI or another condition requiring higher perfusion pressure, a restricted resuscitation strategy may be used to avoid increasing hemorrhage before aortic control.\n"
     "• Target determined by vascular and anesthesia teams.\n"
     "• [color=#991B1B]Not appropriate for every patient. Significant coronary, cerebral, or other organ ischemia may alter the target.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Carefully titrated IV analgesia according to hemodynamic condition and institutional emergency protocol."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Endovascular Aneurysm Repair (EVAR)[/color]\n"
     "• Preferred when anatomy is suitable and an experienced team and equipment are immediately available. Requires rapid coordination among vascular surgery, anesthesia, imaging, and operating team.\n\n"
     "[color=#1E3A8A]Open Repair[/color]\n"
     "• Required when EVAR is unsuitable, unavailable, or cannot be delivered quickly enough."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate transfer to a vascular operating or endovascular suite.\n"
     "• Postoperative ICU care usually required.\n"
     "• Do NOT manage suspected rupture as an outpatient condition."),
    ("REFERENCES", "info", "ESVS Guidelines on abdominal aorto-iliac aneurysms; SVS Practice Guidelines; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Abdominal Trauma and Solid Organ Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Abdominal trauma may cause injury to liver, spleen, kidneys, pancreas, bowel, mesentery, major vessels, and pelvic organs. Injuries may be blunt or penetrating. Internal hemorrhage and hollow-viscus injury can be initially occult.\n"
     "• Mechanisms: RTCs, falls, blunt impact/crush, stab/firearm, high-energy trauma.\n"
     "• Abdominal pain, tenderness, distension. Bruising, seat-belt marks, penetrating wounds.\n"
     "• Hypotension, tachycardia, pallor, altered mental status. Hematuria. Peritonitis or signs of ongoing hemorrhage.\n"
     "• [color=#991B1B]A normal initial abdominal examination or hemoglobin does not exclude serious injury.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow the trauma ABCDE approach. Control external hemorrhage; protect airway.\n"
     "• Activate trauma team and major hemorrhage protocol for suspected severe bleeding.\n"
     "• Establish large-bore IV access or IO access if necessary. Obtain blood samples including type & crossmatch.\n"
     "• Use bedside eFAST in appropriate trauma patients.\n"
     "• Perform urgent operative evaluation in hemodynamically unstable patients with suspected intra-abdominal hemorrhage.\n"
     "• Give tranexamic acid when indicated by major trauma protocol and within recommended time window.\n"
     "• Prevent hypothermia and correct coagulopathy. Reassess repeatedly."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, blood group & crossmatch, blood gas/lactate, coagulation/fibrinogen, electrolytes/renal function/glucose, urinalysis, pregnancy testing when applicable.\n\n"
     "[color=#1E3A8A]eFAST:[/color] Helps identify free intraperitoneal fluid, pericardial fluid, selected thoracic findings. Negative does not exclude bowel, mesenteric, retroperitoneal, or solid-organ injury.\n\n"
     "[color=#1E3A8A]CT Abdomen/Pelvis with IV Contrast:[/color] Preferred in hemodynamically stable patients with significant blunt abdominal trauma. Do NOT delay laparotomy for CT in an unstable patient with a clear indication for operative hemorrhage control."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Hemorrhage Resuscitation[/color]\n"
     "• Use blood products and major hemorrhage protocol when significant ongoing bleeding or hemorrhagic shock suspected.\n"
     "• Avoid relying on large volumes of crystalloid as sole resuscitation strategy.\n"
     "• Prevent hypothermia, acidosis, and coagulopathy. Definitive hemorrhage control must occur promptly.\n\n"
     "[color=#1E3A8A]2. Tranexamic Acid (TXA)[/color]\n"
     "• For eligible adults with significant traumatic hemorrhage: 1 g IV over 10 minutes followed by 1 g IV over 8 hours.\n"
     "• Administer as early as possible and within 3 hours of injury.\n"
     "• [color=#991B1B]Do not administer routinely to every trauma patient. Do not initiate beyond recommended window unless specialist protocol indicates.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Titrated analgesia according to injury severity and hemodynamic stability."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Nonoperative Management[/color]\n"
     "• Selected hemodynamically stable patients with solid-organ injuries when: no peritonitis, appropriate monitoring/serial examination available, blood products/IR/emergency surgery accessible if deterioration occurs.\n\n"
     "[color=#1E3A8A]Angioembolization[/color]\n"
     "• May be appropriate for selected solid-organ injuries with active bleeding or vascular injury, particularly in stable patients or selected responders.\n\n"
     "[color=#1E3A8A]Operative Management[/color]\n"
     "• Emergency laparotomy for hemodynamic instability with suspected intra-abdominal bleeding, peritonitis, bowel perforation, or uncontrolled hemorrhage.\n"
     "• Damage-control surgery may be necessary in profoundly deranged patients."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Hemodynamic instability due to suspected intra-abdominal hemorrhage.\n"
     "• Generalized peritonitis.\n"
     "• Suspected hollow-viscus perforation.\n"
     "• Uncontrolled bleeding not amenable to other definitive methods.\n"
     "• Clinical deterioration during nonoperative management."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with significant solid-organ injury for appropriate monitoring.\n"
     "• ICU care for shock, major transfusion, severe associated injuries, or organ dysfunction.\n"
     "• Discharge only when injury-specific criteria are met and follow-up instructions are clear."),
    ("REFERENCES", "info", "ATLS; WSES Guidelines on blunt/penetrating abdominal trauma; EAST Practice Management Guidelines; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Penetrating Abdominal Trauma")] = [
    ("01 — RECOGNIZE", "info", 
     "Penetrating abdominal trauma occurs when an object breaches the abdominal wall, potentially injuring bowel, solid organs, mesentery, major vessels, diaphragm, or retroperitoneal structures.\n"
     "• Mechanisms: Stab wounds, firearm injuries, impalement, penetrating fragments.\n"
     "• Abdominal wound with or without visible tissue protrusion. Abdominal pain, tenderness, distension.\n"
     "• External hemorrhage. Hypotension, tachycardia, pallor, altered mental status.\n"
     "• Evisceration, peritonitis, or signs of shock.\n\n"
     "[color=#991B1B]Red Flags:[/color] Hemodynamic instability, generalized peritonitis, evisceration, impalement with object in place, active hemorrhage, suspected major vascular/hollow-viscus injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate trauma team and perform ABCDE assessment.\n"
     "• Control external bleeding with direct pressure when appropriate.\n"
     "• [color=#991B1B]Do NOT remove an impaled object in the ED; stabilize it and arrange controlled removal.[/color]\n"
     "• Cover eviscerated abdominal contents with sterile saline-moistened dressings and a protective covering. Do NOT push organs back into the abdomen.\n"
     "• Keep patient NPO. Establish large-bore IV/IO access. Obtain blood samples and activate major hemorrhage protocol if indicated.\n"
     "• Prevent hypothermia. Request immediate surgical assessment.\n"
     "• Administer antibiotics when bowel injury or operative contamination is suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, blood group & crossmatch, blood gas/lactate, coagulation/fibrinogen, electrolytes/renal function, urinalysis.\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• eFAST: useful for rapidly assessing free fluid in selected trauma patients. Negative result does not exclude significant abdominal injury.\n"
     "• CT abdomen/pelvis with IV contrast: appropriate for selected hemodynamically stable patients. Helps define trajectory and identify organ, vascular, or bowel injury.\n"
     "• [color=#991B1B]Imaging must NOT delay laparotomy in an unstable patient with peritonitis or clear evidence of uncontrolled intra-abdominal hemorrhage.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Blood Product Resuscitation[/color]\n"
     "• Activate local major hemorrhage protocol for significant bleeding or hemorrhagic shock. Use blood components according to clinical status and institutional protocol.\n\n"
     "[color=#1E3A8A]2. Tranexamic Acid[/color]\n"
     "• For eligible adults with significant traumatic hemorrhage: 1 g IV over 10 minutes followed by 1 g IV over 8 hours. Administer as early as possible and within 3 hours of injury.\n\n"
     "[color=#1E3A8A]3. Antibiotics for Suspected Hollow-Viscus Injury[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours.\n"
     "• Severe contamination, shock, or healthcare-associated infection may require broader coverage."),
    ("05 — SURGICAL MANAGEMENT", "info", 
     "Immediate operative management generally indicated for:\n"
     "• Hemodynamic instability attributable to abdominal hemorrhage.\n"
     "• Generalized peritonitis.\n"
     "• Evisceration with other indications for exploration.\n"
     "• Uncontrolled bleeding.\n"
     "• Clear evidence of major hollow-viscus or vascular injury.\n\n"
     "Selected stable patients without peritonitis may undergo CT-guided evaluation and selective nonoperative management under experienced trauma surgical supervision."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected significant intra-abdominal injury.\n"
     "• ICU care for shock, major transfusion, or organ dysfunction.\n"
     "• Discharge only after an appropriate observation or evaluation pathway establishes that significant injury is unlikely."),
    ("REFERENCES", "info", "ATLS; EAST Guidelines for penetrating abdominal trauma; WSES Guidelines on blunt/penetrating bowel injury.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Chest Trauma and Tension Pneumothorax")] = [
    ("01 — RECOGNIZE", "info", 
     "Chest trauma may cause life-threatening injury to lungs, pleura, heart, great vessels, and chest wall.\n"
     "A tension pneumothorax occurs when air accumulates under pressure in the pleural space, impairing ventilation and venous return and causing obstructive shock.\n"
     "• Mechanisms: Blunt chest trauma, penetrating injuries, rib fractures, high-energy RTCs, positive-pressure ventilation in a patient with pneumothorax.\n"
     "• Chest pain and dyspnea. Tachypnea, hypoxemia, respiratory distress. Reduced/absent breath sounds on affected side. Asymmetric chest movement.\n"
     "• Hypotension and tachycardia in tension pneumothorax.\n"
     "• Tracheal deviation may occur late and is not required for diagnosis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Administer oxygen for hypoxemia/respiratory distress.\n"
     "• Expose and inspect chest while preventing hypothermia.\n"
     "• [color=#991B1B]If tension pneumothorax is clinically suspected in an unstable patient, decompress immediately; do NOT wait for imaging.[/color]\n"
     "• Arrange definitive pleural drainage after emergency decompression.\n"
     "• Request urgent trauma and thoracic surgical assessment for major chest injury.\n"
     "• Evaluate for associated hemothorax, cardiac tamponade, flail chest, and great-vessel injury."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Bedside:[/color] Continuous SpO2 and ECG monitoring. eFAST or lung ultrasound when available. Chest radiograph in stable patients when appropriate.\n\n"
     "[color=#1E3A8A]CT Chest:[/color] Consider in stable patients with significant trauma, suspected occult pneumothorax, vascular injury, or complex chest-wall injury.\n\n"
     "[color=#991B1B]In a clinically unstable patient with suspected tension pneumothorax, imaging must NOT delay decompression.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Emergency Decompression of Tension Pneumothorax[/color]\n"
     "• Indication: Suspected tension pneumothorax causing respiratory or hemodynamic compromise.\n"
     "• Perform immediate decompression using an accepted institutional technique (finger thoracostomy by trained clinician or needle decompression when appropriate).\n"
     "• In adults, 4th or 5th intercostal space in anterior-to-midaxillary region is commonly used for decompression.\n"
     "• Follow emergency decompression with definitive tube thoracostomy when indicated.\n"
     "• [color=#991B1B]This is a lifesaving invasive procedure requiring appropriate training.[/color]\n\n"
     "[color=#1E3A8A]2. Tube Thoracostomy[/color]\n"
     "• Indications: Significant traumatic pneumothorax, hemothorax, persistent air leak.\n"
     "• Insert appropriately sized chest drain using institution's trauma procedure. Connect to designated drainage system and verify function.\n"
     "• [color=#991B1B]Do not clamp a chest drain routinely in a patient with an active air leak.[/color]"),
    ("05 — ADDITIONAL CHEST TRAUMA MANAGEMENT", "info", 
     "[color=#1E3A8A]Open Pneumothorax[/color]\n"
     "• Apply an appropriate vented chest seal or locally recommended dressing. Monitor for evolving tension physiology. Arrange definitive chest drainage away from the wound.\n\n"
     "[color=#1E3A8A]Flail Chest[/color]\n"
     "• Provide adequate analgesia, oxygen, respiratory monitoring. Escalate ventilatory support for respiratory failure. Consider regional analgesia and specialist assessment.\n\n"
     "[color=#1E3A8A]Massive Hemothorax[/color]\n"
     "• Initiate blood product resuscitation and urgent chest drainage. Obtain immediate surgical evaluation for ongoing major intrathoracic bleeding."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients requiring chest drainage or significant respiratory support.\n"
     "• ICU care for respiratory failure, shock, major chest trauma, or associated organ injury.\n"
     "• Transfer to trauma center when major thoracic or vascular expertise is unavailable."),
    ("REFERENCES", "info", "ATLS; EAST Guidelines on traumatic hemothorax/pneumothorax; WSES–AAST Thoracic Trauma Guidelines.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Open Fractures and Limb-Threatening Injuries")] = [
    ("01 — RECOGNIZE", "info", 
     "An open fracture is a fracture associated with a wound that communicates with the fracture or fracture hematoma. Carries risks of contamination, infection, neurovascular injury, and compartment syndrome.\n"
     "• Open wound near suspected fracture. Visible bone or deep tissue injury. Deformity, swelling, or bleeding.\n"
     "• Reduced distal pulses or abnormal capillary refill. Sensory loss, weakness, or severe pain. Contamination with soil, water, or foreign material.\n\n"
     "[color=#991B1B]Limb-Threatening Features:[/color] Absent distal pulse or acute ischemia, uncontrolled hemorrhage, progressive neurologic deficit, compartment syndrome, extensive soft-tissue destruction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and control life-threatening hemorrhage.\n"
     "• Document mechanism, time of injury, contamination, and neurovascular status.\n"
     "• Cover wound with sterile dressing. Do NOT repeatedly probe the wound or perform unnecessary bedside exploration.\n"
     "• Give IV antibiotics as early as possible. Check tetanus immunization status and provide prophylaxis when indicated.\n"
     "• Immobilize the limb in an appropriate splint. Reassess and document distal pulses, sensation, movement, capillary refill after splinting.\n"
     "• Request urgent orthopedic and vascular assessment for severe injuries. Arrange urgent operative debridement when indicated."),
    ("03 — INVESTIGATIONS", "info", 
     "• Plain radiographs including the joint above and below the injury when appropriate.\n"
     "• CBC and metabolic studies in significant trauma. Group & crossmatch for major bleeding or likely surgery.\n"
     "• CT angiography when vascular injury suspected and patient stable enough for imaging.\n"
     "• [color=#991B1B]Do NOT delay urgent revascularization or hemorrhage control for imaging when a limb is critically ischemic or the patient is unstable.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Antibiotics[/color]\n"
     "• Selected adult open fractures: cefazolin 2 g IV (3 g if ≥120 kg per local prophylaxis protocol).\n"
     "• Additional coverage for severe contamination, high-grade injury, or special exposures per current institutional open-fracture protocol.\n"
     "• Administer as soon as possible after recognizing open fracture. [color=#991B1B]Do NOT delay antibiotics while awaiting radiographs.[/color]\n\n"
     "[color=#1E3A8A]2. Analgesia[/color]\n"
     "• Titrated IV analgesia according to injury severity and hemodynamic status.\n"
     "• [color=#991B1B]Severe escalating pain may indicate compartment syndrome and requires urgent reassessment rather than analgesia alone.[/color]\n\n"
     "[color=#1E3A8A]3. Tetanus Prophylaxis[/color]\n"
     "• Administer tetanus-containing vaccine and, when indicated, tetanus immune globulin according to immunization history and national guidance."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Urgent orthopedic evaluation.\n"
     "• Operative irrigation and debridement according to injury severity and local guidance.\n"
     "• Fracture stabilization. Vascular repair or revascularization when required.\n"
     "• Soft-tissue coverage and reconstruction planning.\n"
     "• Repeated neurovascular assessment and surveillance for compartment syndrome."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Open fracture requiring operative debridement.\n"
     "• Vascular compromise or uncontrolled hemorrhage.\n"
     "• Compartment syndrome.\n"
     "• Severe contamination, tissue loss, or associated injury requiring specialist intervention."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with significant open fractures.\n"
     "• Urgent transfer to appropriate trauma center if orthopedic, vascular, or reconstructive expertise unavailable.\n"
     "• ICU care for major polytrauma, shock, or associated organ failure."),
    ("REFERENCES", "info", "ATLS; BOAST Open Fractures; NICE Guidance on Complex Fractures.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Compartment Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute compartment syndrome occurs when pressure rises within a closed fascial compartment, reducing tissue perfusion and potentially causing irreversible muscle and nerve injury. It is a surgical emergency.\n"
     "• Causes: Fractures (tibial shaft/forearm), crush injury, reperfusion after prolonged ischemia, tight casts/dressings/external compression, vascular injury, severe burns, bleeding into compartment.\n"
     "• Severe pain disproportionate to apparent injury. Pain aggravated by passive stretch of affected muscles.\n"
     "• Increasing swelling or tense compartments. Paresthesia or altered sensation. Weakness or paralysis in advanced disease.\n"
     "• [color=#991B1B]Normal distal pulses do not exclude compartment syndrome. Pulselessness and paralysis are late findings.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Recognize possibility early and call surgical team immediately.\n"
     "• Remove or loosen constrictive dressings and casts while maintaining appropriate stabilization.\n"
     "• Keep limb at heart level rather than markedly elevated above the heart.\n"
     "• Provide appropriate analgesia without allowing pain relief to delay reassessment.\n"
     "• Document pain, passive-stretch response, sensation, movement, distal perfusion.\n"
     "• Obtain urgent surgical assessment for possible fasciotomy.\n"
     "• Measure compartment pressures when diagnosis uncertain or examination unreliable, provided this does not delay necessary surgery."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Clinical Examination[/color]\n"
     "• Repeated assessment is essential. Document findings and progression.\n\n"
     "[color=#1E3A8A]Compartment Pressure Measurement[/color]\n"
     "• Consider when examination equivocal, patient unconscious, or reliable assessment impossible. Interpret pressure together with clinical findings.\n"
     "• Commonly used supportive criterion: differential pressure (diastolic BP minus compartment pressure) ≤ 30 mmHg.\n\n"
     "[color=#1E3A8A]Additional Investigations[/color]\n"
     "• CK, renal function, electrolytes, urinalysis when muscle injury/rhabdomyolysis suspected.\n"
     "• Imaging may identify associated fractures or vascular injuries but does not diagnose/exclude compartment syndrome reliably."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Immediate Pressure Relief[/color]\n"
     "• Remove external compression immediately. Maintain limb alignment and reassess perfusion.\n"
     "• [color=#991B1B]Do NOT delay surgical review while waiting for laboratory results or imaging. A normal pulse or temporary improvement in pain does not exclude the diagnosis.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids when Rhabdomyolysis is Present[/color]\n"
     "• Give isotonic crystalloid according to perfusion, urine output, renal function, severity of muscle injury.\n"
     "• Monitor urine output, electrolytes, creatinine, CK, fluid balance.\n"
     "• [color=#991B1B]Fluid therapy does not replace fasciotomy when compartment syndrome is established.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Use appropriately titrated analgesia while urgent assessment proceeds.\n"
     "• [color=#991B1B]Do not attribute escalating pain solely to fracture pain without reassessing for compartment syndrome.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "[color=#1E3A8A]Emergency Fasciotomy[/color]\n"
     "• Indicated when acute compartment syndrome is diagnosed or strongly suspected.\n"
     "• All affected compartments must be adequately decompressed.\n"
     "• Wounds often left open initially and managed with planned reassessment, delayed closure, or skin grafting as appropriate.\n"
     "• Treat underlying fracture, vascular injury, or cause of bleeding."),
    ("06 — COMPLICATIONS", "danger", 
     "• Muscle necrosis.\n"
     "• Permanent nerve injury.\n"
     "• Contractures.\n"
     "• Rhabdomyolysis and acute kidney injury.\n"
     "• Infection and limb loss."),
    ("07 — DISPOSITION", "warning", 
     "• Immediate surgical admission.\n"
     "• Postoperative monitoring for recurrent compartment syndrome, rhabdomyolysis, renal injury, wound complications.\n"
     "• ICU care when severe muscle injury, shock, or organ dysfunction present."),
    ("REFERENCES", "info", "AAOS Clinical Practice Guideline on acute compartment syndrome; BOA Guidance; NICE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Necrotizing Soft Tissue Infection")] = [
    ("01 — RECOGNIZE", "info", 
     "Necrotizing soft tissue infection (NSTI) is a rapidly progressive infection involving fascia and subcutaneous tissue, sometimes extending into muscle. Can cause septic shock, multiorgan failure, and death.\n"
     "• Risk factors: Diabetes mellitus, immunosuppression, chronic kidney/liver disease, recent surgery/trauma/injections/skin wounds, peripheral vascular disease. Can occur without recognized risk factors.\n"
     "• Severe pain disproportionate to visible skin changes. Rapidly spreading swelling or erythema. Edema extending beyond visible erythema.\n"
     "• Fever, tachycardia, hypotension, altered mental status. Bullae, ecchymosis, skin anesthesia, or necrosis in advanced disease. Crepitus may occur but is not required.\n"
     "• [color=#991B1B]Early skin findings may be subtle. A low LRINEC score or nondiagnostic imaging must NOT be used to exclude NSTI when clinical suspicion is high.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and identify septic shock.\n"
     "• Request immediate surgical assessment.\n"
     "• Begin sepsis resuscitation and administer broad-spectrum IV antibiotics promptly.\n"
     "• Keep patient NPO and prepare for urgent operative exploration.\n"
     "• Obtain blood cultures and tissue cultures when feasible without delaying antibiotics or surgery.\n"
     "• Check glucose, electrolytes, renal function, lactate, coagulation. Provide analgesia and monitor closely.\n"
     "• [color=#991B1B]Do NOT delay surgery for CT or MRI when clinical diagnosis is strongly suspected.[/color]\n"
     "• Involve ICU, infectious diseases, and relevant surgical specialists early."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, CRP, glucose, CK (if muscle involvement/rhabdomyolysis), lactate/blood gas, coagulation, blood cultures, deep tissue cultures (obtained during surgery).\n\n"
     "[color=#1E3A8A]Imaging:[/color] CT may show fascial edema, fluid, gas, or deep collections. MRI may define tissue involvement in selected stable patients. [color=#991B1B]Neither test reliably excludes early NSTI.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Broad-Spectrum IV Antibiotics[/color]\n"
     "• Example: Piperacillin–tazobactam 4.5 g IV per severe-infection dosing protocol.\n"
     "• Vancomycin using appropriate weight-based regimen and therapeutic monitoring.\n"
     "• Clindamycin 900 mg IV every 8 hours may be added when toxin-mediated infection (Group A strep or clostridial) suspected.\n"
     "• Adjust for renal function, body weight, allergy, microbiology, local resistance.\n"
     "• [color=#991B1B]Antibiotics alone are inadequate treatment for established NSTI.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluid Resuscitation[/color]\n"
     "• For sepsis-induced hypoperfusion: initial crystalloid bolus, followed by reassessment. Individualize in septic shock using perfusion findings and response to treatment.\n\n"
     "[color=#1E3A8A]3. Vasopressor Support: Norepinephrine[/color]\n"
     "• Generally first-line vasopressor in adult septic shock. Start and titrate per institutional protocol, commonly targeting initial MAP ~65 mmHg.\n"
     "• Continuous BP and ECG monitoring required. Monitor peripheral perfusion, urine output, lactate.\n"
     "• [color=#991B1B]Do NOT delay vasopressor treatment in persistent shock while waiting for central venous access when local protocols permit safe peripheral initiation.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "[color=#1E3A8A]Emergency Exploration and Debridement[/color]\n"
     "• Immediate operative exploration required when NSTI strongly suspected.\n"
     "• Remove all clearly necrotic tissue. Obtain deep tissue specimens for microbiology.\n"
     "• Reassess tissue viability and plan repeat exploration, often within 24 hours or earlier if deterioration.\n"
     "• Reconstructive surgery and wound closure considered after infection control.\n\n"
     "[color=#1E3A8A]Additional Management[/color]\n"
     "• Control hyperglycemia. Treat organ dysfunction. Consider tetanus prophylaxis for relevant wounds.\n"
     "• Hyperbaric oxygen is not a substitute for urgent surgery and should never delay debridement."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Strong clinical suspicion of NSTI.\n"
     "• Rapid progression despite treatment.\n"
     "• Skin necrosis, bullae, deep fascial involvement, or systemic toxicity.\n"
     "• Suspected clostridial myonecrosis.\n"
     "• Failure of initial debridement requiring further source control."),
    ("07 — DISPOSITION", "warning", 
     "• Emergency surgical admission.\n"
     "• ICU care for shock, organ failure, extensive debridement, or ventilatory support.\n"
     "• Continue multidisciplinary care until infection controlled and organ function stabilizes."),
    ("REFERENCES", "info", "IDSA Skin and Soft Tissue Infection Guidelines; Surviving Sepsis Campaign; WSES Guidance on NSTI.")
]


# ==================== BATCH 3 (TOPICS 17-26) ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Limb Ischemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute limb ischemia (ALI) is a sudden reduction in limb perfusion that threatens tissue viability. Most commonly caused by arterial embolism or thrombosis.\n"
     "• Causes: Cardiac embolism (AF), acute thrombosis of atherosclerotic artery, thrombosis of stent/graft, arterial trauma/dissection, hypercoagulable states.\n"
     "• The six Ps: Pain, Pallor, Pulselessness, Paresthesia, Paralysis, Poikilothermia (cold limb).\n"
     "• Threatened limb features: Sensory loss (especially beyond toes/fingers), new muscle weakness/paralysis, absent arterial Doppler signals, severe pain with cold pale limb.\n"
     "• [color=#991B1B]Motor weakness indicates an immediately threatened limb and requires emergency revascularization assessment.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and identify shock or associated trauma.\n"
     "• Obtain immediate vascular surgical consultation.\n"
     "• Document time of onset, pain, sensory function, motor function, temperature, capillary refill, and Doppler signals.\n"
     "• Establish IV access and provide appropriate analgesia.\n"
     "• Start IV unfractionated heparin promptly when ALI is suspected unless contraindicated, per protocol.\n"
     "• Obtain urgent vascular imaging when it will guide treatment without delaying revascularization.\n"
     "• Keep patient NPO when intervention likely.\n"
     "• Do NOT apply compression, elevate limb excessively, or expose to direct heat."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC and platelets, electrolytes/urea/creatinine, coagulation profile, group & crossmatch (if intervention likely), CK/potassium/renal function (if muscle ischemia or reperfusion injury suspected), lactate/blood gas (severe ischemia).\n\n"
     "[color=#1E3A8A]Vascular Assessment:[/color] Handheld arterial and venous Doppler signals. Duplex ultrasound when immediately available. CT angiography for anatomical planning in suitable patients. Catheter angiography in selected patients undergoing endovascular intervention.\n\n"
     "[color=#991B1B]Imaging must NOT delay revascularization when the limb is immediately threatened.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Unfractionated Heparin[/color]\n"
     "• Commonly used initial regimen: IV bolus of 70–80 units/kg, followed by infusion of approximately 15–18 units/kg/hour. Use institution's therapeutic anticoagulation protocol; some patients require modified dosing.\n"
     "• Monitor aPTT or anti-Xa per protocol. Check platelet count and assess for bleeding.\n"
     "• [color=#991B1B]Avoid or modify anticoagulation when there is active major bleeding or another contraindication.[/color]\n\n"
     "[color=#1E3A8A]2. Analgesia[/color]\n"
     "• Titrated analgesia appropriate to pain severity and hemodynamic status.\n"
     "• Pain relief must NOT delay vascular assessment or revascularization.\n\n"
     "[color=#1E3A8A]3. Reperfusion and Metabolic Management[/color]\n"
     "• Prepare for urgent revascularization. Monitor potassium, acid-base status, renal function, and CK in patients with significant ischemia.\n"
     "• [color=#991B1B]Reperfusion can cause hyperkalemia, acidosis, rhabdomyolysis, renal injury, and compartment syndrome.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "Depending on anatomy, limb viability, and local expertise:\n"
     "• Surgical embolectomy or thrombectomy.\n"
     "• Endovascular thrombectomy or thrombolysis in selected patients.\n"
     "• Angioplasty or stenting.\n"
     "• Bypass surgery.\n"
     "• Amputation when the limb is irreversibly ischemic and nonviable."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate vascular surgical admission.\n"
     "• ICU or high-dependency care for severe ischemia, reperfusion injury, major intervention, or organ dysfunction."),
    ("REFERENCES", "info", "ESVS Clinical Practice Guidelines on Acute Limb Ischaemia; ACC/AHA PAD Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Testicular Torsion and Acute Scrotum")] = [
    ("01 — RECOGNIZE", "info", 
     "Testicular torsion occurs when the spermatic cord twists, compromising testicular blood flow. It is a time-critical surgical emergency.\n"
     "• Sudden severe unilateral testicular pain. Nausea or vomiting.\n"
     "• High-riding or horizontal testicular position. Scrotal swelling and tenderness.\n"
     "• Absent cremasteric reflex may support diagnosis but is not sufficiently reliable to exclude torsion when present.\n"
     "• Abdominal or groin pain may occur, particularly in children.\n"
     "• Differential: Epididymitis/orchitis, torsion of testicular appendage, incarcerated hernia, trauma, tumor with hemorrhage/infarction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess pain, onset, and associated symptoms immediately.\n"
     "• Request urgent urological or surgical consultation.\n"
     "• Keep patient NPO. Provide analgesia and antiemetics.\n"
     "• Arrange urgent surgical exploration when torsion is strongly suspected.\n"
     "• [color=#991B1B]Do NOT delay surgery for ultrasound when clinical suspicion is high.[/color]\n"
     "• Consider Doppler ultrasound when diagnosis is uncertain and imaging immediately available without delaying specialist assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical assessment is central.\n"
     "• Urinalysis may help identify alternative diagnoses but does not exclude torsion.\n"
     "• Doppler ultrasound can assess testicular perfusion in uncertain cases.\n"
     "• Laboratory tests should not delay definitive management."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Select appropriate analgesia according to age, weight, pain severity, and hemodynamic status.\n"
     "• Analgesia must NOT delay emergency surgical assessment.\n\n"
     "[color=#1E3A8A]Manual Detorsion[/color]\n"
     "• May be attempted by trained clinician while arranging urgent surgery if immediate operative treatment not available.\n"
     "• Continue to arrange emergency surgical exploration even if pain improves.\n"
     "• [color=#991B1B]Manual detorsion may be incomplete/fail. Symptom relief does not prove perfusion restored. Not a substitute for definitive surgical management.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Emergency scrotal exploration.\n"
     "• Detorsion and assessment of testicular viability.\n"
     "• Orchidopexy when appropriate.\n"
     "• Management of nonviable testis according to operative findings and specialist judgment.\n"
     "• Fixation of contralateral testis commonly performed (risk of bilateral anatomical predisposition)."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate emergency surgical/urological management.\n"
     "• Do NOT discharge a patient with unresolved suspicion of torsion."),
    ("REFERENCES", "info", "EAU Guidelines on Paediatric Urology and Acute Scrotum; AUA Educational Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Fournier Gangrene and Perineal Sepsis")] = [
    ("01 — RECOGNIZE", "info", 
     "Fournier gangrene is a rapidly progressive necrotizing infection of the perineal, genital, or perianal fascia. Can spread rapidly and cause septic shock.\n"
     "• Risk factors: Diabetes, immunosuppression, obesity, CKD, perianal abscess/anorectal infection, genitourinary infection/recent instrumentation, recent perineal surgery/trauma.\n"
     "• Severe perineal/genital/perianal pain. Swelling and erythema. Pain disproportionate to visible skin findings.\n"
     "• Fever, tachycardia, hypotension, altered mental status. Bullae, skin discoloration, necrosis, crepitus in advanced disease.\n"
     "• [color=#991B1B]Absence of crepitus or gas on imaging does NOT exclude Fournier gangrene.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and identify septic shock.\n"
     "• Call general surgery and urology immediately; involve other relevant specialists per suspected source.\n"
     "• Begin IV fluid resuscitation and sepsis management.\n"
     "• Administer broad-spectrum IV antibiotics promptly.\n"
     "• Keep patient NPO and prepare for urgent operative debridement.\n"
     "• Obtain blood cultures and lab tests when feasible without delaying treatment.\n"
     "• Control hyperglycemia and correct metabolic abnormalities.\n"
     "• [color=#991B1B]Do NOT delay surgery for CT when clinical suspicion is high.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, glucose, CRP, lactate/blood gas, coagulation profile, CK (muscle involvement suspected), blood cultures, deep tissue cultures during surgery.\n\n"
     "[color=#1E3A8A]Imaging:[/color] CT may help define extent in stable patients. Imaging cannot reliably exclude early disease. Do NOT delay operative source control for imaging in a deteriorating patient."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Broad-Spectrum IV Antibiotics[/color]\n"
     "• Example: Piperacillin–tazobactam 4.5 g IV per severe-infection dosing protocol.\n"
     "• Vancomycin using appropriate weight-based regimen and therapeutic monitoring.\n"
     "• Clindamycin 900 mg IV every 8 hours may be added when toxin-mediated infection suspected.\n"
     "• Adjust for renal function, allergy, cultures, local resistance. Narrow when results available.\n"
     "• [color=#991B1B]Antibiotics do NOT replace urgent surgical debridement.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluid Resuscitation[/color]\n"
     "• Adult sepsis-induced hypoperfusion: begin isotonic crystalloid resuscitation and reassess frequently. Further fluid depends on perfusion, cardiac function, urine output, clinical response.\n\n"
     "[color=#1E3A8A]3. Vasopressor Support: Norepinephrine[/color]\n"
     "• First-line vasopressor for adult septic shock when indicated. Titrate per institutional protocol, commonly targeting initial MAP ~65 mmHg.\n"
     "• Continuous BP and ECG monitoring. Monitor perfusion, urine output, response to source control.\n"
     "• [color=#991B1B]Vasopressors do NOT replace antibiotics and surgery.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Emergency exploration and extensive debridement of necrotic tissue.\n"
     "• Drainage of associated abscesses.\n"
     "• Repeated operative assessment and debridement when necessary.\n"
     "• Management of underlying anorectal, genitourinary, or skin source.\n"
     "• Urinary or fecal diversion may be considered selectively according to extent of disease and specialist assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency surgical admission.\n"
     "• ICU care for shock, extensive tissue destruction, organ failure, or repeated operations.\n"
     "• Continue multidisciplinary care until infection controlled."),
    ("REFERENCES", "info", "IDSA Skin and Soft Tissue Infection Guidelines; WSES Guidance on NSTI; EAU Urological Infections Guidance; Surviving Sepsis Campaign.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Urinary Retention")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute urinary retention is the sudden inability to pass urine despite a full bladder. May cause severe pain and can be associated with obstruction, infection, renal impairment, or neurological disease.\n"
     "• Causes: Benign prostatic enlargement, urethral stricture, medication effects (anticholinergics, sympathomimetics), constipation, prostatitis/UTI, blood clots obstructing outflow, neurological disorders (including spinal cord compression).\n"
     "• Painful suprapubic distension. Inability to pass urine. Frequent small-volume voiding or overflow incontinence. Agitation/discomfort. Renal impairment in prolonged obstruction.\n\n"
     "[color=#991B1B]Red Flags:[/color] Fever/hypotension/urosepsis, AKI, hematuria with clots, new leg weakness/saddle anesthesia/bowel dysfunction (cauda equina), suspected urethral injury after pelvic trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and identify sepsis or hemodynamic instability.\n"
     "• Examine abdomen and assess bladder distension. Obtain bladder ultrasound/scanning when available.\n"
     "• Establish IV access and obtain lab tests if systemically unwell or renal impairment suspected.\n"
     "• Provide appropriate analgesia.\n"
     "• Arrange urinary drainage when indicated and safe.\n"
     "• [color=#991B1B]Do NOT attempt blind urethral catheterization when urethral injury is suspected.[/color]\n"
     "• Request urgent urological assessment for difficult catheterization, suspected urethral injury, clot retention, or associated complications."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bladder scan or bedside ultrasound.\n"
     "• Urinalysis and urine culture when infection suspected.\n"
     "• Creatinine, urea, and electrolytes.\n"
     "• CBC and blood cultures in suspected sepsis.\n"
     "• Renal ultrasound when hydronephrosis or upper urinary tract obstruction suspected.\n"
     "• Additional neurological assessment and imaging if spinal cord/cauda equina pathology suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Bladder Decompression[/color]\n"
     "• Urethral catheterization is commonly used when no suspicion of urethral injury and no contraindication. Use appropriate catheter size and aseptic technique.\n"
     "• If catheterization difficult/unsuccessful, stop repeated traumatic attempts and seek specialist assistance.\n"
     "• Record drained volume. Monitor urine output, pain relief, hematuria, renal function, electrolytes. Monitor for post-obstructive diuresis.\n"
     "• [color=#991B1B]Blood at urethral meatus, pelvic trauma, perineal bruising, or suspected urethral disruption requires specialist evaluation before urethral catheterization. Do NOT force a catheter against resistance.[/color]\n\n"
     "[color=#1E3A8A]2. Alpha Blocker (When Appropriate)[/color]\n"
     "• Selected adults with suspected BPO: Tamsulosin 0.4 mg orally once daily per local protocol.\n"
     "• Review BP, dizziness, falls risk, concurrent antihypertensives.\n"
     "• [color=#991B1B]Tamsulosin does NOT replace urgent bladder drainage. Not appropriate for every cause of urinary retention.[/color]\n\n"
     "[color=#1E3A8A]3. Antibiotics[/color]\n"
     "• Do NOT prescribe antibiotics routinely for uncomplicated urinary retention without evidence of infection.\n"
     "• If UTI/urosepsis suspected, choose antibiotic per severity, culture, renal function, local resistance."),
    ("05 — COMPLICATIONS", "danger", 
     "• Post-obstructive diuresis.\n"
     "• Hematuria.\n"
     "• Acute kidney injury.\n"
     "• Electrolyte disturbances.\n"
     "• Urosepsis.\n"
     "• Recurrent retention."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with renal impairment, sepsis, significant hematuria, major electrolyte disturbances, or neurological red flags.\n"
     "• Arrange urgent specialist review when catheterization fails or a dangerous underlying cause suspected.\n"
     "• Discharge only when drainage adequate, patient clinically stable, and clear catheter-care/follow-up plan arranged."),
    ("REFERENCES", "info", "EAU Guidelines on Non-neurogenic Male LUTS; NICE Guidance; EAU Urological Infections Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Sigmoid and Cecal Volvulus")] = [
    ("01 — RECOGNIZE", "info", 
     "Volvulus is twisting of a bowel segment around its mesentery, causing obstruction and potentially compromising blood supply. Can progress to bowel ischemia, necrosis, perforation, and septic shock.\n"
     "• Types: Sigmoid volvulus, cecal volvulus.\n"
     "• Risk factors: Chronic constipation, older age/institutionalization, neurological disease/impaired mobility, previous abdominal surgery/adhesions, anatomical predisposition (redundant sigmoid).\n"
     "• Abdominal distension. Colicky or persistent abdominal pain. Constipation and inability to pass flatus. Nausea/vomiting. Tympanitic abdomen.\n"
     "• Fever, peritonitis, or shock when ischemia/perforation develops."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Keep patient NPO.\n"
     "• Establish IV access and correct dehydration/electrolyte disturbances.\n"
     "• Request urgent surgical assessment.\n"
     "• Consider NG decompression for persistent vomiting or significant distension.\n"
     "• Start broad-spectrum antibiotics when ischemia, perforation, or sepsis suspected.\n"
     "• Arrange urgent imaging in stable patients.\n"
     "• [color=#991B1B]Do NOT attempt endoscopic decompression when there are signs of peritonitis, perforation, or suspected bowel necrosis.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, lactate/blood gas (ischemia/shock), CRP, group & crossmatch (if surgery likely).\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT abdomen/pelvis: helps identify transition point, twisted mesentery, bowel dilation, ischemia, perforation.\n"
     "• Abdominal radiograph: may show characteristic bowel dilation (coffee-bean appearance in sigmoid volvulus). Cannot reliably exclude ischemia/perforation."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluids[/color]\n"
     "• Adult hypoperfusion: initial 500 mL isotonic crystalloid bolus, then reassess. Replace ongoing vomiting/decompression losses.\n\n"
     "[color=#1E3A8A]2. Antibiotics when Ischemia/Perforation Suspected[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (selected adults).\n"
     "• Broader for severe healthcare-associated infection or septic shock."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Sigmoid Volvulus without Ischemia/Perforation[/color]\n"
     "• Endoscopic detorsion and decompression may be attempted by experienced team. Observe for clinical improvement and bowel viability.\n"
     "• Definitive sigmoid colectomy generally recommended because recurrence after decompression alone is common.\n\n"
     "[color=#1E3A8A]Cecal Volvulus[/color]\n"
     "• Operative management generally recommended. Procedure depends on bowel viability and operative findings; may include resection of affected segment.\n"
     "• Endoscopic decompression generally NOT recommended (limited success, significant perforation risk)."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Peritonitis.\n"
     "• Suspected ischemia or necrosis.\n"
     "• Perforation.\n"
     "• Failed endoscopic detorsion.\n"
     "• Cecal volvulus requiring definitive treatment.\n"
     "• Recurrent sigmoid volvulus requiring definitive surgery."),
    ("07 — DISPOSITION", "warning", 
     "• Admit all patients with confirmed volvulus.\n"
     "• ICU care for shock, bowel necrosis, perforation, or major postoperative complications.\n"
     "• Ensure definitive recurrence-prevention plan after successful decompression."),
    ("REFERENCES", "info", "WSES Guidance on Sigmoid Volvulus; ASGE Guidance; WSES Emergency Colorectal Surgery Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Colonic Pseudo-Obstruction")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute colonic pseudo-obstruction (Ogilvie syndrome) is marked colonic dilation without a mechanical obstructing lesion. Often occurs in hospitalized, postoperative, or severely ill patients.\n"
     "• Risk factors: Major surgery/trauma/severe medical illness, electrolyte abnormalities (hypokalemia), opioids/anticholinergics, neurological disorders/immobility, severe infection/critical illness.\n"
     "• Progressive abdominal distension. Abdominal discomfort/pain. Nausea/vomiting. Constipation/reduced passage of stool/flatus.\n"
     "• Fever, localized tenderness, guarding, or shock may indicate ischemia or perforation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and identify peritonitis or shock.\n"
     "• Keep patient NPO initially if significant distension, vomiting, or procedural intervention likely.\n"
     "• Review medications and discontinue contributing agents where possible.\n"
     "• Correct potassium, magnesium, and other electrolyte abnormalities. Provide IV fluids per volume status.\n"
     "• Obtain urgent surgical assessment.\n"
     "• Evaluate for mechanical obstruction, ischemia, and perforation before pharmacological decompression.\n"
     "• Monitor abdominal findings and vital signs serially."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, magnesium/potassium, lactate/blood gas (ischemia/deterioration), CRP.\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• Abdominal radiograph to assess colonic dilation and follow progression.\n"
     "• CT abdomen/pelvis (often with IV contrast) to exclude mechanical obstruction and identify complications.\n"
     "• Assess cecal diameter and duration of dilation. Risk rises with marked dilation (particularly ≥12 cm) and prolonged distension."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Conservative Management[/color]\n"
     "• Indications: Hemodynamically stable without peritonitis, ischemia, or perforation.\n"
     "• Bowel rest, IV fluids/electrolyte correction, stop/reduce opioids/anticholinergics, mobilization, NG decompression (significant vomiting), rectal tube decompression (selected).\n"
     "• Serial abdominal examination and imaging as indicated. Track abdominal circumference/distension, pain, stool/flatus, vitals, urine output, cecal diameter.\n"
     "• [color=#991B1B]Do NOT continue conservative management when patient deteriorates or bowel ischemia/perforation suspected.[/color]\n\n"
     "[color=#1E3A8A]2. Neostigmine[/color]\n"
     "• Indications: Persistent clinically significant pseudo-obstruction despite appropriate conservative therapy, after mechanical obstruction and perforation excluded. Requires specialist decision and continuous monitoring.\n"
     "• Dose: Neostigmine 2 mg IV administered slowly over ~3–5 minutes. Repeat dosing depends on response and local protocol.\n"
     "• Continuous ECG and SpO2 monitoring. Frequent BP and HR assessment. Have atropine immediately available for clinically significant bradycardia. Ensure staff/equipment for resuscitation.\n"
     "• [color=#991B1B]Avoid in significant bradycardia, uncontrolled asthma/bronchospasm, suspected mechanical obstruction, and suspected bowel perforation.[/color]\n\n"
     "[color=#1E3A8A]3. Colonoscopic Decompression[/color]\n"
     "• Indications: Failure/contraindication to neostigmine, or when specialist assessment favors endoscopic decompression.\n"
     "• Performed by experienced endoscopy team. Decompression tube placement may reduce recurrence. Monitor for perforation and clinical recurrence.\n"
     "• [color=#991B1B]Avoid or use extreme caution when perforation or bowel ischemia suspected.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Perforation or bowel necrosis.\n"
     "• Peritonitis.\n"
     "• Clinical deterioration despite appropriate treatment.\n"
     "• Failure of nonoperative and endoscopic management in a patient requiring operative intervention."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for monitoring and treatment.\n"
     "• Escalate to ICU for shock, respiratory compromise from massive distension, or major complications."),
    ("REFERENCES", "info", "ASGE Guidance; ASCRS Clinical Practice Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Toxic Megacolon and Fulminant Colitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Toxic megacolon is acute colonic dilation associated with severe colitis and systemic toxicity. Can cause perforation, hemorrhage, shock, and multiorgan failure.\n"
     "• Causes: Severe ulcerative colitis, Crohn colitis, C. difficile infection, other infectious colitides, ischemic/drug-associated colitis.\n"
     "• Severe diarrhea (may be bloody). Abdominal pain and distension. Fever, tachycardia, dehydration. Hypotension/altered mental status. Reduced bowel sounds, guarding, rebound tenderness in advanced disease.\n"
     "• Diagnostic concern: Colonic dilation (commonly >6 cm on imaging) combined with systemic toxicity and severe colitis. Diagnosis requires clinical and radiological assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and assess for shock.\n"
     "• Call general surgery and gastroenterology urgently.\n"
     "• Keep patient NPO initially if severe disease or surgery possible.\n"
     "• Establish IV access and begin appropriate fluid resuscitation.\n"
     "• Obtain CBC, electrolytes, renal function, inflammatory markers, lactate when indicated.\n"
     "• Send stool testing for C. difficile and other pathogens as appropriate.\n"
     "• Stop antidiarrheal agents, opioids, anticholinergics, and other drugs that impair colonic motility when clinically feasible.\n"
     "• [color=#991B1B]Avoid colonoscopy and bowel preparation in suspected toxic megacolon because of perforation risk.[/color]\n"
     "• Perform serial abdominal examinations and monitor for deterioration."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC and differential.\n"
     "• Electrolytes, urea, and creatinine.\n"
     "• CRP and albumin.\n"
     "• Lactate and blood gas if severe illness suspected.\n"
     "• Stool testing for C. difficile and relevant enteric pathogens.\n"
     "• Blood cultures in systemic toxicity or suspected sepsis.\n"
     "• Abdominal radiograph or CT to evaluate dilation and complications.\n"
     "• [color=#991B1B]Avoid delaying surgery for imaging when perforation or peritonitis is clinically evident.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Fluid and Electrolyte Replacement[/color]\n"
     "• Isotonic crystalloid, with boluses guided by perfusion and repeated reassessment.\n"
     "• Monitor BP, pulse, urine output, electrolytes, renal function, respiratory status.\n"
     "• Tailor fluids to cardiac/renal function; avoid unmonitored fluid loading.\n\n"
     "[color=#1E3A8A]2. Suspected C. difficile-Associated Fulminant Colitis[/color]\n"
     "• Vancomycin 500 mg orally or via NG tube every 6 hours.\n"
     "• Add Metronidazole 500 mg IV every 8 hours.\n"
     "• If ileus present, rectal vancomycin may be required under specialist direction.\n"
     "• [color=#991B1B]Treatment must follow current local infectious disease guidance. Fulminant disease requires early surgical consultation; antibiotics must NOT delay surgery when indicated.[/color]\n\n"
     "[color=#1E3A8A]3. Severe IBD-Associated Colitis[/color]\n"
     "• IV corticosteroids may be indicated for acute severe ulcerative colitis after appropriate specialist assessment and evaluation for infection.\n"
     "• Infectious causes (particularly C. difficile) should be investigated and treated when present.\n"
     "• Rescue therapy and colectomy decisions require urgent gastroenterology and surgical coordination.\n"
     "• [color=#991B1B]Do NOT start immunosuppression indiscriminately before considering infection and perforation.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "Urgent operative management may be required for:\n"
     "• Perforation or generalized peritonitis.\n"
     "• Uncontrolled hemorrhage.\n"
     "• Worsening systemic toxicity or shock.\n"
     "• Progressive colonic dilation or clinical deterioration despite appropriate medical treatment.\n"
     "• Failure of intensive medical treatment in severe colitis.\n\n"
     "The operation depends on underlying cause and condition of the colon; subtotal colectomy with end ileostomy is commonly considered in fulminant ulcerative colitis with life-threatening complications."),
    ("06 — DISPOSITION", "warning", 
     "• Admit to hospital; ICU care often required in severe systemic toxicity.\n"
     "• Conduct frequent multidisciplinary reassessment.\n"
     "• Do NOT delay operative intervention when complications or failure of treatment are evident."),
    ("REFERENCES", "info", "ACG Clinical Guidelines on C. difficile; ASCRS Clinical Practice Guidelines on Ulcerative Colitis; BSG Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Esophageal Perforation")] = [
    ("01 — RECOGNIZE", "info", 
     "Esophageal perforation is a life-threatening emergency that can cause mediastinitis, pleural infection, sepsis, and shock.\n"
     "• Causes: Forceful vomiting (Boerhaave syndrome), iatrogenic injury during endoscopy/instrumentation, foreign body ingestion, trauma, caustic injury/underlying esophageal disease.\n"
     "• Sudden severe chest, neck, or upper abdominal pain. Pain after forceful vomiting. Dysphagia/odynophagia.\n"
     "• Fever, tachycardia, respiratory distress. Subcutaneous emphysema/crepitus. Pleural effusion, pneumomediastinum, pneumothorax. Shock/sepsis in advanced cases.\n"
     "• [color=#991B1B]The classic triad of vomiting, chest pain, and subcutaneous emphysema is not always present.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and treat respiratory/circulatory compromise.\n"
     "• Keep patient strictly NPO.\n"
     "• Obtain urgent thoracic or upper GI surgical consultation.\n"
     "• Establish IV access and begin resuscitation when indicated.\n"
     "• Start broad-spectrum IV antibiotics covering oral flora and anaerobes.\n"
     "• Consider IV PPI therapy as directed by specialist team.\n"
     "• [color=#991B1B]Avoid blind nasogastric tube insertion; placement should be directed by treating specialist when needed.[/color]\n"
     "• Arrange urgent imaging and definitive source control."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, CRP, lactate, blood gas as clinically indicated.\n"
     "• Blood cultures if sepsis suspected.\n"
     "• CT chest and upper abdomen with appropriate contrast protocol.\n"
     "• Water-soluble contrast esophagography may be used when appropriate.\n"
     "• Endoscopy may be useful in selected cases but should be planned by experienced specialist (instrumentation can worsen injury)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Broad-Spectrum IV Antibiotics[/color]\n"
     "• Example: Piperacillin–tazobactam 4.5 g IV per severe-infection protocol.\n"
     "• Alternative regimens depend on allergy history, renal function, likely organisms, local resistance.\n"
     "• [color=#991B1B]Antibiotics alone are insufficient when ongoing leakage or uncontrolled contamination requires source control.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids and Shock Management[/color]\n"
     "• Isotonic crystalloid in boluses guided by hemodynamic status and reassessment.\n"
     "• Monitor BP, HR, urine output, lactate, respiratory status. Escalate to vasopressors and critical care when shock persists.\n"
     "• Avoid excessive fluid in patients with respiratory compromise or cardiac dysfunction."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "Management depends on site, cause, time since perforation, contamination, and clinical stability. Options:\n"
     "• Endoscopic closure or stenting in selected cases.\n"
     "• Surgical repair and drainage.\n"
     "• Drainage of mediastinal or pleural collections.\n"
     "• Resection or diversion in selected severe injuries.\n"
     "• Carefully selected nonoperative management only when specialist criteria met and close monitoring available."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Free leak with significant contamination.\n"
     "• Hemodynamic instability or uncontrolled sepsis.\n"
     "• Large or non-contained perforation.\n"
     "• Failed endoscopic or conservative management.\n"
     "• Necrotic esophageal tissue or associated major injury."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent admission to a center with appropriate thoracic or upper GI surgical expertise.\n"
     "• ICU care for shock, respiratory failure, or severe mediastinal/pleural contamination."),
    ("REFERENCES", "info", "WSES Guidance on Esophageal Emergencies; ESGE Guidance on Iatrogenic Perforation; STS/Specialist Thoracic Surgery Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Intra-Abdominal Abscess and Postoperative Sepsis")] = [
    ("01 — RECOGNIZE", "info", 
     "An intra-abdominal abscess is a localized collection of infected fluid or pus. May occur after appendicitis, diverticulitis, bowel perforation, pancreatitis, trauma, or abdominal surgery.\n"
     "• Risk factors: Recent abdominal surgery, anastomotic leak, perforated viscus, inadequate source control during previous procedure, immunosuppression/diabetes, complicated appendicitis/diverticulitis.\n"
     "• Persistent/recurrent fever. Abdominal pain or localized tenderness. Tachycardia and malaise. Ileus, nausea, poor oral intake. Leukocytosis/raised inflammatory markers.\n"
     "• Hypotension, altered mental status, oliguria, elevated lactate in severe sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and identify sepsis or shock.\n"
     "• Obtain IV access and assess perfusion. Send lab tests and blood cultures when indicated.\n"
     "• Begin appropriate IV antibiotics promptly in sepsis or when serious intra-abdominal infection suspected.\n"
     "• Obtain urgent surgical assessment. Arrange imaging to identify collection and potential source.\n"
     "• Plan drainage or surgery when source control needed.\n"
     "• [color=#991B1B]Reassess frequently; do not rely on antibiotics alone for a drainable collection.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, LFTs when indicated, CRP, lactate/blood gas in severe illness, blood cultures in sepsis, culture of drained pus/intra-abdominal specimens.\n\n"
     "[color=#1E3A8A]Imaging:[/color]\n"
     "• CT abdomen/pelvis with IV contrast: often preferred in stable adult to locate abscess, identify leak, guide drainage.\n"
     "• Ultrasound: useful for selected superficial/accessible collections and when CT unsuitable."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Empiric IV Antibiotics[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (selected community-acquired).\n"
     "• Piperacillin–tazobactam may be appropriate for more severe infection or broader coverage.\n"
     "• Start promptly in sepsis. Adjust to renal function, allergy, source, cultures, local resistance. Review daily and narrow when possible.\n"
     "• [color=#991B1B]These are example adult regimens, not universal prescriptions. Healthcare-associated infection, resistant organisms, severe allergy, or renal impairment may require a different regimen. Antibiotic duration depends on adequacy of source control and clinical response.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluid Resuscitation[/color]\n"
     "• Isotonic crystalloid for hypoperfusion, with repeated reassessment.\n"
     "• In adult sepsis-induced hypoperfusion or septic shock, initial fluid resuscitation may approach 30 mL/kg within first 3 hours, but must be individualized and reassessed frequently.\n"
     "• Avoid automatic large-volume fluid administration without reassessment, particularly in cardiac/renal dysfunction.\n\n"
     "[color=#1E3A8A]3. Percutaneous Drainage[/color]\n"
     "• Indications: Well-defined collection safely accessible by interventional radiology or appropriately trained specialist.\n"
     "• Obtain specimens for culture. Monitor drain output, fever, pain, inflammatory markers, clinical response. Re-image/reassess if improvement does not occur.\n"
     "• [color=#991B1B]Not every collection is safely drainable percutaneously. Persistent sepsis may indicate undrained collection, ongoing leakage, resistant infection, or inadequate source control.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Generalized peritonitis.\n"
     "• Free perforation or ongoing gastrointestinal leakage.\n"
     "• Collections unsuitable for percutaneous drainage.\n"
     "• Failed drainage or persistent infection.\n"
     "• Hemodynamic instability or clinical deterioration requiring urgent source control."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with significant intra-abdominal infection.\n"
     "• ICU care for septic shock or organ dysfunction.\n"
     "• Document a source-control plan and reassess need for further drainage or surgery."),
    ("REFERENCES", "info", "Surgical Infection Society Guidelines; WSES Guidance on Intra-abdominal Infections; Surviving Sepsis Campaign.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Esophageal Food Bolus Impaction")] = [
    ("01 — RECOGNIZE", "info", 
     "Esophageal food bolus impaction occurs when food becomes lodged in the esophagus. Complete obstruction can prevent patient from swallowing saliva and may cause aspiration.\n"
     "• Sudden dysphagia during a meal. Sensation of food stuck in chest/throat. Regurgitation of liquids/food.\n"
     "• Drooling or inability to swallow saliva. Gagging, coughing, aspiration. Retrosternal discomfort/pain.\n\n"
     "[color=#991B1B]Red Flags:[/color] Inability to handle secretions, respiratory distress/suspected aspiration, sharp foreign body/bone ingestion, severe chest/neck pain, fever, crepitus, signs of perforation, suspected caustic ingestion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation.\n"
     "• If respiratory distress or airway compromise present, initiate emergency airway management as appropriate.\n"
     "• Keep patient NPO. Sit upright when clinically appropriate and keep suction available if secretions cannot be managed.\n"
     "• Request urgent gastroenterology/endoscopy consultation.\n"
     "• [color=#991B1B]Complete obstruction with inability to swallow saliva requires emergent endoscopic management.[/color]\n"
     "• Do NOT force oral fluids, food, or tablets. Do NOT induce vomiting. Avoid blind attempts to push bolus down."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical assessment of airway and ability to handle secretions.\n"
     "• Chest/neck radiographs when radiopaque foreign body or complication suspected.\n"
     "• CT when perforation, sharp foreign body injury, or another complication suspected.\n"
     "• Endoscopy is main diagnostic and therapeutic procedure for persistent impaction.\n"
     "• Investigate underlying cause after resolution (esophageal stricture, Schatzki ring, eosinophilic esophagitis, malignancy when appropriate)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Endoscopic Removal or Advancement[/color]\n"
     "• Indications: Complete obstruction or inability to handle secretions = emergent intervention. Other persistent food bolus impactions: urgent endoscopic treatment per specialist assessment.\n"
     "• Procedure: Flexible endoscopy by trained clinician. Removal or careful advancement of bolus. Evaluate for mucosal injury, stricture, or underlying lesion.\n"
     "• Airway protection and sedation planning depend on aspiration risk and patient stability.\n"
     "• [color=#991B1B]Do NOT delay emergent endoscopy in complete obstruction. Avoid forceful advancement and blind instrumentation.[/color]\n\n"
     "[color=#1E3A8A]2. Pharmacological Measures[/color]\n"
     "• Selected agents (e.g., IV glucagon) have sometimes been used while arranging definitive care, but efficacy is inconsistent.\n"
     "• If specialist/local protocol elects glucagon: commonly cited adult dose 1 mg IV once.\n"
     "• Monitor nausea, vomiting, glucose, airway status.\n"
     "• [color=#991B1B]Glucagon must NOT delay endoscopy. Avoid relying on it in complete obstruction or when patient cannot handle secretions. Do NOT administer oral effervescent agents/fluids to patient with complete obstruction (aspiration risk).[/color]"),
    ("05 — AFTER RESOLUTION", "info", 
     "• Assess for mucosal injury or perforation.\n"
     "• Arrange evaluation for underlying esophageal disorder.\n"
     "• Biopsy for eosinophilic esophagitis when appropriate and safe.\n"
     "• Provide follow-up for recurrent dysphagia or food impaction."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or observe patients with complications, persistent symptoms, significant mucosal injury, aspiration, or suspected perforation.\n"
     "• Discharge only after successful resolution, adequate swallowing assessment, and clear follow-up plan."),
    ("REFERENCES", "info", "ASGE Guidance on Ingested Foreign Bodies and Food Impactions; ESGE Clinical Guidelines.")
]


# ==================== BATCH 4 (TOPICS 27-36) ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Gastric Dilatation and Gastric Ischemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute gastric dilatation is marked enlargement of the stomach due to retained gas, fluid, or food. Severe distension can impair gastric blood flow, cause necrosis or perforation, and compromise ventilation.\n"
     "• Causes: Gastric outlet obstruction, postoperative ileus, severe eating disorders/binge eating, neurological impairment/critical illness, medications impairing GI motility, gastric volvulus/mechanical obstruction.\n"
     "• Marked upper abdominal distension. Epigastric pain/pressure. Nausea/vomiting (may be absent if outlet obstructed). Respiratory distress from diaphragmatic elevation.\n"
     "• Tachycardia, hypotension, shock in severe cases. Hematemesis, peritonitis, or severe persistent pain may indicate ischemia/perforation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Assess respiratory compromise, shock, peritonitis.\n"
     "• Keep patient NPO. Establish IV access and obtain urgent surgical assessment.\n"
     "• Insert NG tube for decompression when appropriate and safe.\n"
     "• [color=#991B1B]Do NOT force NG tube insertion if gastric volvulus, esophageal injury, or another contraindication suspected.[/color]\n"
     "• Correct fluid/electrolyte abnormalities. Arrange urgent imaging in stable patient.\n"
     "• Escalate immediately if decompression fails or ischemia/perforation suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/urea/creatinine, lactate/blood gas (ischemia/shock), LFTs/lipase when indicated.\n"
     "• Abdominal radiograph as initial assessment.\n"
     "• CT abdomen/pelvis with IV contrast when appropriate to identify obstruction, volvulus, ischemia, or perforation.\n"
     "• Endoscopy or contrast studies in selected patients after specialist assessment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Gastric Decompression[/color]\n"
     "• NG decompression commonly first intervention. Record volume/character of aspirated contents. Confirm tube position per policy.\n"
     "• Monitor distension, pain, vomiting, respiratory status, fluid balance, electrolyte losses. Replace significant ongoing losses.\n"
     "• [color=#991B1B]Failure to decompress, worsening pain, bloody aspirate, peritonitis, or hemodynamic instability requires urgent reassessment for ischemia, volvulus, or perforation.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Isotonic crystalloid guided by volume status/response. Boluses for hypoperfusion, reassess frequently.\n\n"
     "[color=#1E3A8A]3. Antibiotics when Ischemia/Perforation Suspected[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours.\n"
     "• [color=#991B1B]Antibiotics do NOT replace urgent operative source control.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Gastric ischemia or necrosis.\n"
     "• Perforation or peritonitis.\n"
     "• Gastric volvulus requiring intervention.\n"
     "• Persistent mechanical obstruction.\n"
     "• Failure of decompression with clinical deterioration."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for monitoring and treatment.\n"
     "• ICU for shock, respiratory compromise, gastric necrosis, or major surgery."),
    ("REFERENCES", "info", "WSES Guidance; ACR Guidance; Local Protocols.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Gallbladder Perforation and Complicated Cholecystitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Gallbladder perforation is a complication of acute cholecystitis that can cause localized abscess, biliary peritonitis, or generalized sepsis.\n"
     "• Risk factors: Delayed treatment of acute cholecystitis, older age, diabetes, immunosuppression, severe systemic illness, gangrenous cholecystitis.\n"
     "• RUQ pain/tenderness. Fever and leukocytosis. Persistent/worsening pain despite treatment.\n"
     "• Generalized abdominal tenderness/guarding. Hypotension, confusion, other signs of sepsis.\n"
     "• Localized mass may suggest pericholecystic abscess."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Keep patient NPO.\n"
     "• Obtain IV access and lab tests. Start appropriate IV fluids if hypovolemia/hypoperfusion.\n"
     "• Request urgent general surgical assessment.\n"
     "• Start IV antibiotics when complicated cholecystitis or sepsis suspected.\n"
     "• Arrange urgent imaging without delaying surgery in patient with generalized peritonitis or instability.\n"
     "• Assess for biliary obstruction and cholangitis."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Laboratory:[/color] CBC, electrolytes/urea/creatinine, bilirubin/ALT/AST/ALP/GGT, CRP, lactate/blood gas in severe illness, blood cultures in sepsis.\n\n"
     "[color=#1E3A8A]Imaging:[/color] Ultrasound (initial test for gallbladder inflammation/gallstones). CT abdomen (perforation, abscess, gas, adjacent inflammatory changes). HIDA/MRCP in selected uncertain cases."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IV Antibiotics[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours.\n"
     "• Broader (e.g., piperacillin–tazobactam) for severe infection, healthcare-associated infection, or selected high-risk patients.\n"
     "• [color=#991B1B]Antibiotics alone are insufficient when perforation or uncontrolled biliary contamination requires source control.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Isotonic crystalloid according to perfusion/volume status, reassessing after each bolus.\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Appropriate titrated analgesic based on severity/contraindications/hemodynamic status.\n"
     "• [color=#991B1B]Analgesia must NOT delay surgical source control.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Urgent cholecystectomy when appropriate and feasible.\n"
     "• Percutaneous gallbladder drainage may be considered for selected high-risk patients who cannot safely undergo immediate surgery.\n"
     "• Drainage of pericholecystic or intra-abdominal abscess when indicated.\n"
     "• Bile duct evaluation and drainage if concomitant obstruction/cholangitis suspected."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Free perforation with biliary peritonitis.\n"
     "• Gangrenous cholecystitis.\n"
     "• Uncontrolled sepsis.\n"
     "• Persistent infection despite appropriate treatment.\n"
     "• Abscess or another complication requiring source control."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with suspected perforation or complicated cholecystitis.\n"
     "• ICU care for shock or organ dysfunction.\n"
     "• Reassess source control and antibiotic response frequently."),
    ("REFERENCES", "info", "Tokyo Guidelines; WSES Guidelines for Acute Calculous Cholecystitis; Surgical Infection Society Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Infected Pancreatic Necrosis and Pancreatic Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute pancreatitis can cause pancreatic or peripancreatic necrosis. Infection of necrotic tissue may lead to sepsis, persistent organ failure, and death.\n"
     "• Severe persistent epigastric pain (radiating to back). Nausea/vomiting. Fever/worsening systemic inflammatory response.\n"
     "• Persistent organ dysfunction. Deterioration after initial improvement.\n"
     "• Gas within pancreatic/peripancreatic collection on CT can suggest infection, although its absence does not exclude infection.\n"
     "• Risk factors: Severe acute pancreatitis, extensive pancreatic necrosis, prolonged critical illness, delayed/inadequate management of complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and identify shock or organ failure.\n"
     "• Involve general surgery, gastroenterology, interventional radiology, and ICU teams early.\n"
     "• Establish IV access and obtain lab tests. Provide goal-directed fluid therapy.\n"
     "• Provide analgesia and nutritional support as appropriate.\n"
     "• Evaluate for infected necrosis, other sources of infection, alternative causes of deterioration.\n"
     "• Obtain blood cultures when sepsis suspected.\n"
     "• [color=#991B1B]Do NOT prescribe prophylactic antibiotics solely because sterile pancreatic necrosis is present.[/color]\n"
     "• Plan drainage or debridement with specialist teams when indicated."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/urea/creatinine, LFTs, glucose/calcium, CRP, lactate/blood gas in severe illness, blood cultures if infection/sepsis suspected.\n"
     "• Contrast-enhanced CT when clinically appropriate to define necrosis and collections. Interpret in relation to time course and clinical findings."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Antibiotics for Suspected/Confirmed Infected Necrosis[/color]\n"
     "• Indicated when infected necrosis or another bacterial infection suspected/confirmed. Choose agents that penetrate pancreatic necrotic tissue and cover likely organisms per local guidance.\n"
     "• Example: Piperacillin–tazobactam may be appropriate in selected patients.\n"
     "• [color=#991B1B]Routine prophylactic antibiotics NOT recommended for sterile necrosis. Antibiotics do NOT replace drainage or debridement when source control required.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluid Therapy[/color]\n"
     "• Isotonic crystalloid with frequent reassessment. Avoid indiscriminate aggressive fluid loading (particularly after early resuscitation or with respiratory/cardiac/renal dysfunction).\n\n"
     "[color=#1E3A8A]3. Analgesia and Nutritional Support[/color]\n"
     "• Appropriate analgesia. Enteral nutrition generally preferred when oral intake not adequate. Use NG/NJ feeding when appropriate.\n"
     "• Avoid unnecessary prolonged fasting when enteral feeding feasible and safe."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Step-Up Approach[/color]\n"
     "• Initial antibiotics and supportive care when infection suspected.\n"
     "• Endoscopic or percutaneous drainage when intervention required and anatomically feasible.\n"
     "• Minimally invasive necrosectomy for patients who do not improve after drainage when indicated.\n"
     "• Open surgery reserved for selected cases (failure of less invasive methods or other surgical emergencies).\n"
     "• When stable, intervention often delayed until necrosis better organized (commonly ~4 weeks). Earlier intervention may be necessary in selected deteriorating patients."),
    ("06 — SURGICAL/INTERVENTIONAL INDICATIONS", "warning", 
     "• Confirmed or strongly suspected infected necrosis with clinical deterioration.\n"
     "• Persistent sepsis despite appropriate medical management.\n"
     "• Symptomatic or enlarging collections causing obstruction or other complications.\n"
     "• Abdominal compartment syndrome or another associated surgical emergency.\n"
     "• Failure of a less invasive step-up strategy."),
    ("07 — DISPOSITION", "warning", 
     "• Admit severe or complicated cases to a specialist center.\n"
     "• ICU care for persistent organ failure or shock.\n"
     "• Multidisciplinary follow-up is essential."),
    ("REFERENCES", "info", "ACG Guidelines on Acute Pancreatitis; AGA Guidance on Pancreatic Necrosis; WSES Guidelines on Severe Acute Pancreatitis.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Anastomotic Leak Following Gastrointestinal Surgery")] = [
    ("01 — RECOGNIZE", "info", 
     "An anastomotic leak occurs when a surgically created connection between GI segments fails, allowing enteric contents to escape. Can cause intra-abdominal infection, peritonitis, septic shock.\n"
     "• Risk factors: Poor tissue perfusion, malnutrition/hypoalbuminemia, diabetes, smoking, immunosuppression/corticosteroid exposure, emergency surgery/severe contamination, tension on anastomosis, technical/vascular complications.\n"
     "• Persistent tachycardia. Fever or increasing abdominal pain. Ileus/failure to recover bowel function.\n"
     "• Purulent or enteric drain output. Increasing inflammatory markers. Hypotension, oliguria, confusion, elevated lactate. Peritonitis in major leak.\n"
     "• [color=#991B1B]Tachycardia and unexplained clinical deterioration after GI surgery may be early warning signs even before dramatic abdominal findings appear.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Notify operating surgeon and general surgery team urgently.\n"
     "• Keep patient NPO. Establish IV access and obtain blood tests.\n"
     "• Begin sepsis resuscitation when indicated. Start broad-spectrum IV antibiotics promptly when leak-associated infection suspected.\n"
     "• Obtain blood cultures if no delay. Arrange CT imaging in stable patient when it will help determine source/management.\n"
     "• [color=#991B1B]Do NOT delay operative exploration for imaging when generalized peritonitis or instability strongly suggests an uncontrolled leak.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/renal function/LFTs/CRP, lactate/blood gas in severe illness, blood cultures when sepsis suspected, culture of drain fluid/operative specimens.\n"
     "• CT abdomen/pelvis with IV contrast when appropriate. Water-soluble enteric contrast may be considered according to location/local protocol.\n"
     "• [color=#991B1B]A negative scan does not fully exclude a leak when clinical suspicion remains high.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Broad-Spectrum IV Antibiotics[/color]\n"
     "• Piperacillin–tazobactam 4.5 g IV per local severe-infection protocol. Alternatives depend on severity, allergy, renal function, local resistance, suspected source.\n"
     "• [color=#991B1B]Antibiotics alone are not adequate for an uncontrolled leak or generalized peritonitis.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids and Shock Management[/color]\n"
     "• Isotonic crystalloid for hypoperfusion with repeated reassessment. In adult sepsis-induced hypoperfusion, initial volume approaching 30 mL/kg within 3 hours may be considered, individualized.\n"
     "• Escalate to vasopressors and ICU support if shock persists despite appropriate resuscitation.\n\n"
     "[color=#1E3A8A]3. Source Control[/color]\n"
     "• Options: Percutaneous drainage (localized collection), endoscopic treatment (selected anastomoses), surgical exploration/washout/repair/revision/diversion/takedown.\n"
     "• Choice depends on hemodynamic stability, degree of contamination, anatomy, operating surgeon's assessment."),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Generalized peritonitis.\n"
     "• Hemodynamic instability or uncontrolled sepsis.\n"
     "• Major leak with free contamination.\n"
     "• Failed percutaneous or endoscopic management.\n"
     "• Persistent clinical deterioration despite treatment."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent admission under surgical team.\n"
     "• ICU care for shock, respiratory failure, or multiorgan dysfunction.\n"
     "• Continue reassessment until source control and clinical improvement established."),
    ("REFERENCES", "info", "Surgical Infection Society Guidance; WSES Guidance on Postoperative Intra-abdominal Infection; Surviving Sepsis Campaign.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Postoperative Bowel Obstruction and Prolonged Ileus")] = [
    ("01 — RECOGNIZE", "info", 
     "Postoperative ileus is temporary impairment of coordinated GI motility after surgery. Mechanical bowel obstruction is a physical blockage and may require urgent intervention.\n"
     "• Ileus causes: Major abdominal surgery, opioids/anticholinergics, hypokalemia/electrolyte disturbances, sepsis/inflammation/intra-abdominal collections, excessive fluid administration/severe systemic illness.\n"
     "• Mechanical obstruction causes: Adhesions, internal/external hernia, anastomotic narrowing, volvulus, early postoperative technical complications.\n"
     "• Abdominal distension, nausea/vomiting, failure to pass flatus/stool, reduced oral intake, abdominal pain.\n"
     "• [color=#991B1B]Fever, tachycardia, focal tenderness, guarding, or rising lactate may indicate strangulation, ischemia, leak, or another complication.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment. Review operation, postoperative day, medications, bowel-function progression.\n"
     "• Keep patient NPO if significant obstruction or vomiting suspected.\n"
     "• Establish IV access and correct fluid/electrolyte deficits. Request surgical review.\n"
     "• Insert NG tube when persistent vomiting or marked distension warrants decompression.\n"
     "• Review opioids/anticholinergics and reduce when clinically feasible.\n"
     "• Assess for anastomotic leak, abscess, ischemia, other postoperative complications.\n"
     "• [color=#991B1B]Do NOT assume that all postoperative distension is benign ileus.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/urea/creatinine, magnesium, CRP when indicated, lactate/blood gas if ischemia/sepsis suspected.\n"
     "• CT abdomen/pelvis with IV contrast when appropriate (transition point, closed-loop obstruction, ischemia, collection, leak).\n"
     "• Plain abdominal radiography may show bowel dilation but is less definitive."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Supportive Management (Uncomplicated Ileus)[/color]\n"
     "• Correct dehydration/electrolyte abnormalities. Encourage early mobilization when safe.\n"
     "• Minimize opioids and motility-inhibiting medications when feasible. Provide appropriate analgesia/antiemetics.\n"
     "• NG decompression for selected patients with significant vomiting/distension. Resume oral intake per clinical recovery/surgical team assessment.\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Isotonic crystalloid according to volume status/ongoing losses. Replace measured NG losses when clinically indicated. Avoid unmonitored fluid overload.\n\n"
     "[color=#1E3A8A]3. Antiemetics[/color]\n"
     "• Select according to age, comorbidities, QT interval risk, other medications. For selected adults, ondansetron 4 mg IV may be used per protocol.\n"
     "• [color=#991B1B]Antiemetics do NOT treat mechanical obstruction and must not delay surgical assessment.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT (MECHANICAL OBSTRUCTION)", "info", 
     "• Selected adhesive small-bowel obstructions may be managed nonoperatively under close surgical supervision when no evidence of ischemia, strangulation, or peritonitis.\n"
     "• Management: Bowel rest, IV fluids, NG decompression, selected contrast protocols.\n"
     "• Surgery required when obstruction is complicated, fails appropriate conservative management, or results from a cause requiring operative correction."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Peritonitis.\n"
     "• Suspected strangulation, ischemia, or perforation.\n"
     "• Closed-loop obstruction.\n"
     "• Clinical deterioration or persistent obstruction despite an appropriate monitored trial of conservative management.\n"
     "• Anastomotic or other postoperative complications requiring source control."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with suspected mechanical obstruction or significant postoperative ileus.\n"
     "• ICU care for shock, organ dysfunction, or major postoperative complications.\n"
     "• Discharge only after clinical improvement, adequate hydration, appropriate oral-intake plan, and clear follow-up."),
    ("REFERENCES", "info", "WSES Guidance on Adhesive SBO; ERAS Society Recommendations; ACR Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Postoperative Hemorrhage and Hematoma")] = [
    ("01 — RECOGNIZE", "info", 
     "Postoperative hemorrhage is bleeding occurring after surgery. May be external, concealed within a body cavity, or present as a wound/organ-space hematoma. Significant bleeding can rapidly progress to hemorrhagic shock.\n"
     "• Causes: Inadequate surgical hemostasis, slipped ligature/vascular injury, coagulopathy/thrombocytopenia, anticoagulant/antiplatelet medication, anastomotic bleeding, vascular graft/organ injury, bleeding from drain site/operative wound.\n"
     "• Persistent tachycardia. Hypotension or narrowing pulse pressure. Pallor, diaphoresis, delayed cap refill.\n"
     "• Increasing wound/drain blood loss. Abdominal distension or increasing pain. Falling hemoglobin (early Hb may initially remain normal). Oliguria, confusion, elevated lactate in severe hemorrhage."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate local major hemorrhage protocol when significant bleeding suspected.\n"
     "• Perform ABCDE assessment and provide oxygen when indicated by hypoxemia/critical illness.\n"
     "• Call operating surgeon and anesthesia/critical care team urgently.\n"
     "• Establish two large-bore IV lines or appropriate rapid-access alternatives.\n"
     "• Send CBC, coagulation, fibrinogen, blood gas, lactate, electrolytes, group/crossmatch.\n"
     "• Apply direct pressure to accessible external bleeding.\n"
     "• Begin blood component resuscitation when indicated by hemorrhage severity/local protocol.\n"
     "• Identify anticoagulants and reverse their effects when indicated.\n"
     "• [color=#991B1B]Do NOT delay operative control for imaging in an unstable patient with suspected ongoing internal bleeding.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC with serial hemoglobin. PT/INR, aPTT, fibrinogen, platelet count.\n"
     "• Blood gas and lactate. Electrolytes, renal function, ionized calcium during major hemorrhage.\n"
     "• Group and crossmatch. Bedside ultrasound or CT angiography in selected stable patients.\n"
     "• Evaluate drains, wound sites, abdominal findings, operative records."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Blood Component Resuscitation[/color]\n"
     "• Indications: Major ongoing hemorrhage or hemorrhagic shock. Use local major hemorrhage protocol when criteria met.\n"
     "• Monitor temperature, ECG, BP, oxygenation, urine output, hemoglobin, coagulation, fibrinogen, ionized calcium. Warm patient and blood products when appropriate.\n"
     "• [color=#991B1B]Do NOT rely on a single hemoglobin value to exclude severe acute blood loss. Avoid excessive crystalloid when blood products and definitive hemorrhage control required.[/color]\n\n"
     "[color=#1E3A8A]2. Tranexamic Acid[/color]\n"
     "• Consider in selected patients with significant hemorrhage when indicated by bleeding context/local protocol.\n"
     "• For selected adult trauma with significant bleeding: 1 g IV over 10 minutes, followed by 1 g IV over 8 hours, ideally within 3 hours of injury.\n"
     "• [color=#991B1B]This trauma regimen should NOT automatically be applied to every postoperative bleed. Avoid rapid IV administration (can cause hypotension). TXA does NOT replace surgical hemostasis.[/color]\n\n"
     "[color=#1E3A8A]3. Anticoagulant Reversal[/color]\n"
     "• Identify anticoagulant, last dose, renal function, severity of bleeding. Use appropriate reversal strategy per local guidance.\n"
     "• [color=#991B1B]Reversal carries thrombotic risk; select according to clinical situation and drug involved.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Return to operating room when bleeding ongoing or surgical control needed.\n"
     "• Interventional radiology embolization may be appropriate for selected arterial bleeding in stable patients.\n"
     "• Correct hypothermia, acidosis, hypocalcemia, coagulopathy.\n"
     "• Review anticoagulant/antiplatelet therapy after hemostasis achieved."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Hemodynamic instability with suspected ongoing internal bleeding.\n"
     "• Persistent blood loss despite resuscitation.\n"
     "• Expanding hematoma causing organ or airway compression.\n"
     "• Suspected major vascular injury.\n"
     "• Bleeding requiring direct operative control."),
    ("07 — DISPOSITION", "warning", 
     "• Admit and monitor patients with significant postoperative bleeding.\n"
     "• ICU care for shock, massive transfusion, coagulopathy, or organ dysfunction."),
    ("REFERENCES", "info", "ESVS/Specialty Guidance on Perioperative Bleeding; European Guideline on Major Bleeding/Coagulopathy; NICE Blood Transfusion Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Abdominal Wound Dehiscence and Evisceration")] = [
    ("01 — RECOGNIZE", "info", 
     "Wound dehiscence is separation of a surgical wound. Fascial dehiscence is a serious complication because abdominal contents may protrude through the wound. Evisceration is the protrusion of abdominal viscera through a disrupted wound.\n"
     "• Risk factors: Surgical-site infection, poor nutrition/hypoalbuminemia, obesity, diabetes, smoking, chronic corticosteroid use/immunosuppression, increased intra-abdominal pressure (coughing/vomiting/ileus), poor tissue quality/technical failure.\n"
     "• Sudden serosanguineous discharge. Feeling of wound opening/tearing sensation. Visible separation of wound edges.\n"
     "• Protruding bowel or omentum. Abdominal pain, fever, signs of infection."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call operating surgeon immediately.\n"
     "• Assess ABCDE and treat associated shock/sepsis. Keep patient NPO.\n"
     "• Position patient comfortably, often supine with knees slightly flexed (reduce abdominal wall tension).\n"
     "• If viscera exposed, cover with sterile dressings moistened with warm sterile saline.\n"
     "• [color=#991B1B]Do NOT push exposed organs back into the abdomen. Avoid pressure on protruding viscera.[/color]\n"
     "• Establish IV access and prepare for urgent operative management.\n"
     "• Administer antibiotics when infection, contamination, or emergency surgery warrants them."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/renal function/glucose, coagulation, group/crossmatch if surgery likely.\n"
     "• Lactate and blood cultures if sepsis suspected.\n"
     "• Imaging only when patient stable and diagnosis/associated intra-abdominal complication uncertain.\n"
     "• [color=#991B1B]Imaging must NOT delay surgery when evisceration or major fascial disruption is evident.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Wound Protection[/color]\n"
     "• Cover exposed viscera with sterile saline-moistened dressings. Maintain warm environment and minimize contamination.\n"
     "• Prepare for urgent surgical exploration.\n"
     "• [color=#991B1B]Never apply dry gauze directly to exposed bowel. Never attempt forceful reduction of eviscerated organs at the bedside.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Isotonic crystalloid guided by perfusion and repeated reassessment.\n"
     "• [color=#991B1B]Escalate to blood products when hemorrhage present; crystalloid alone is inadequate for major blood loss.[/color]\n\n"
     "[color=#1E3A8A]3. Antibiotics when Indicated[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours + Metronidazole 500 mg IV every 8 hours (selected contaminated intra-abdominal situations).\n"
     "• Broader therapy may be required per severity, contamination, healthcare exposure, local resistance."),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Urgent operative exploration for fascial dehiscence with evisceration.\n"
     "• Assess bowel viability and associated intra-abdominal infection.\n"
     "• Repair fascial disruption when feasible.\n"
     "• Use individualized closure strategy when contamination/edema/tissue quality prevents safe primary closure.\n"
     "• Treat associated infection, ileus, or increased intra-abdominal pressure."),
    ("06 — SURGICAL INDICATIONS", "warning", 
     "• Evisceration.\n"
     "• Complete fascial disruption.\n"
     "• Bowel compromise or suspected intra-abdominal infection.\n"
     "• Wound dehiscence associated with uncontrolled bleeding or sepsis."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent surgical admission.\n"
     "• ICU care when associated with shock, major contamination, or significant organ dysfunction."),
    ("REFERENCES", "info", "WSES Guidance; ACS Educational Resources; Local Protocols.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Stoma Complications: Ischemia, Retraction, Prolapse, and Obstruction")] = [
    ("01 — RECOGNIZE", "info", 
     "A stoma complication may threaten bowel viability, cause obstruction, impair appliance fitting, or lead to fluid/electrolyte loss.\n\n"
     "[color=#1E3A8A]Major complications:[/color]\n"
     "• Ischemia/Necrosis: Dusky, purple, gray, or black stoma. Loss of normal mucosal appearance. Reduced bleeding on gentle specialist assessment. Associated abdominal pain/systemic deterioration.\n"
     "• Retraction: Stoma lies below skin level. Leakage and skin irritation. Difficulty maintaining appliance seal.\n"
     "• Prolapse: Excessive protrusion of bowel through stoma. Edema, appliance difficulty, or obstruction. Darkening/severe pain suggests compromised perfusion.\n"
     "• Outlet Obstruction: Reduced/absent output. Abdominal distension, cramping, nausea, vomiting."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and identify shock, dehydration, or peritonitis.\n"
     "• Inspect stoma and surrounding skin. Establish IV access if dehydrated/vomiting/systemically unwell.\n"
     "• Measure stoma output and replace significant fluid losses.\n"
     "• Request urgent surgical and stoma-care specialist assessment.\n"
     "• Keep patient NPO when obstruction, ischemia, or surgery suspected.\n"
     "• [color=#991B1B]Do NOT force instruments or tubes through a stoma. Escalate immediately for suspected ischemia, strangulation, perforation, or complete obstruction.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes/urea/creatinine, magnesium (high output/fluid loss).\n"
     "• Lactate/blood gas if ischemia/shock suspected.\n"
     "• CT abdomen/pelvis for suspected obstruction, internal hernia, intra-abdominal complication.\n"
     "• Direct specialist assessment of stoma viability and depth of ischemia."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Fluid and Electrolyte Replacement[/color]\n"
     "• Indications: High-output ileostomy, vomiting, dehydration, AKI.\n"
     "• Oral rehydration solution when patient can safely drink; IV isotonic crystalloid for significant dehydration/hypoperfusion with reassessment.\n"
     "• Monitor BP, pulse, urine output, renal function, Na+, K+, Mg2+.\n"
     "• [color=#991B1B]High-output stomas can cause rapid sodium/fluid depletion. Replace losses according to measured output and labs.[/color]\n\n"
     "[color=#1E3A8A]2. Stoma Prolapse[/color]\n"
     "• If viable/uncomplicated, trained clinician may attempt gentle reduction using appropriate technique. Edema reduction measures only under clinical supervision.\n"
     "• [color=#991B1B]Do NOT attempt forceful reduction. Painful, irreducible, discolored, or ischemic prolapse requires urgent surgical assessment.[/color]\n\n"
     "[color=#1E3A8A]3. Stoma Ischemia/Necrosis[/color]\n"
     "• Urgent surgical assessment to determine depth/extent of ischemia. Superficial mucosal discoloration may sometimes be observed under specialist guidance. Deep necrosis extending below fascial level usually requires urgent operative management.\n"
     "• [color=#991B1B]Do NOT rely on external color alone when depth of ischemia uncertain.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Deep stoma necrosis.\n"
     "• Strangulation or compromised bowel viability.\n"
     "• Complete obstruction or failure of conservative management.\n"
     "• Irreducible prolapse with ischemia.\n"
     "• Retraction causing severe dysfunction or complications not manageable conservatively.\n"
     "• Associated intra-abdominal pathology."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with ischemia, obstruction, severe dehydration, or systemic illness.\n"
     "• Arrange stoma nurse follow-up for stable appliance or skin problems."),
    ("REFERENCES", "info", "ASCRS Clinical Practice Resources; ACPGBI Guidance; Local Protocols.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Perianal and Perirectal Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "An anorectal abscess is a localized collection of pus near the anus or rectum. Delayed drainage can lead to sepsis, tissue extension, or fistula formation.\n"
     "• Types: Perianal, intersphincteric, ischioanal, supralevator.\n"
     "• Risk factors: Anal gland obstruction/infection, diabetes, Crohn disease, immunosuppression, previous anorectal abscess/fistula.\n"
     "• Perianal pain (worse sitting/defecating). Localized swelling/erythema/fluctuance. Fever/malaise.\n"
     "• Deep abscess may cause severe rectal/pelvic pain without obvious external swelling. Urinary retention may occur with deep pelvic inflammation.\n"
     "• [color=#991B1B]Severe pain out of proportion, rapidly spreading erythema, bullae, or skin necrosis raises concern for necrotizing infection.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and look for sepsis.\n"
     "• Examine perianal region with appropriate consent, analgesia, and chaperone.\n"
     "• Obtain urgent surgical assessment.\n"
     "• Keep patient NPO when urgent drainage/anesthesia likely. Provide analgesia.\n"
     "• Obtain lab tests in systemic illness, diabetes, or immunocompromise.\n"
     "• Arrange urgent drainage; antibiotics alone are usually insufficient for a drainable abscess.\n"
     "• [color=#991B1B]If Fournier gangrene suspected, activate the emergency necrotizing-infection pathway.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC/inflammatory markers when indicated. Glucose/renal function in diabetes/systemic illness.\n"
     "• Lactate/blood cultures when sepsis suspected.\n"
     "• CT or MRI for deep, complex, recurrent, or clinically occult abscesses when imaging will guide management.\n"
     "• Superficial, obvious abscesses usually do not require imaging before drainage."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Analgesia[/color]\n"
     "• Choose appropriate analgesic based on severity, renal function, allergies, comorbidities.\n"
     "• [color=#991B1B]Severe or escalating pain may indicate deep collection or necrotizing infection and requires reassessment.[/color]\n\n"
     "[color=#1E3A8A]2. Antibiotics when Indicated[/color]\n"
     "• Indications: Sepsis/systemic infection, significant surrounding cellulitis, immunocompromise, selected high-risk comorbidities, specific indications determined by surgeon.\n"
     "• Example: Amoxicillin–clavulanate may be appropriate in selected cases when local guidance supports. IV broad-spectrum needed for severe infection/sepsis per local protocols.\n"
     "• [color=#991B1B]Routine antibiotics do NOT replace incision and drainage of an established abscess.[/color]\n\n"
     "[color=#1E3A8A]3. Incision and Drainage[/color]\n"
     "• Drainage is primary treatment for most anorectal abscesses. Approach depends on location/complexity. Deep/complex abscesses may require drainage under anesthesia.\n"
     "• Monitor pain, fever, drainage, wound healing, recurrence. Consider fistula evaluation if symptoms persist/recur.\n"
     "• [color=#991B1B]Avoid blind probing for a fistula during acute drainage because it can injure the sphincter complex.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Established anorectal abscess requiring drainage.\n"
     "• Deep collection.\n"
     "• Sepsis or clinical deterioration.\n"
     "• Suspected necrotizing infection.\n"
     "• Failure of initial treatment or recurrent disease."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with sepsis, extensive infection, deep abscess, immunocompromise, or need for operative drainage.\n"
     "• Outpatient management may be appropriate after drainage in selected stable patients with reliable follow-up."),
    ("REFERENCES", "info", "ASCRS Clinical Practice Guidelines on Anorectal Abscess/Fistula; ACPGBI Guidance; IDSA Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Liver Failure Requiring Emergency Transplant Evaluation")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute liver failure is a rapidly developing severe liver injury with impaired synthetic function and hepatic encephalopathy in a patient without established cirrhosis. Can cause cerebral edema, hypoglycemia, coagulopathy, renal failure, multiorgan dysfunction.\n"
     "• Causes: Paracetamol toxicity, viral hepatitis, drug-induced liver injury, autoimmune hepatitis, ischemic hepatitis, metabolic/toxin-related disorders, pregnancy-associated liver disease.\n"
     "• Jaundice. Confusion/drowsiness/altered mental status. Hypoglycemia. Coagulopathy (elevated INR). Nausea/vomiting/RUQ discomfort. Renal dysfunction. Lactic acidosis/hemodynamic instability in severe disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform ABCDE assessment and check bedside glucose immediately.\n"
     "• Contact hepatology and a liver-transplant center urgently when acute liver failure suspected.\n"
     "• Establish IV access and obtain comprehensive lab investigations.\n"
     "• Correct hypoglycemia promptly. Assess airway protection and encephalopathy severity.\n"
     "• Identify and treat possible paracetamol toxicity without waiting for all confirmatory results when clinically indicated.\n"
     "• Stop potentially hepatotoxic drugs and review recent medications/exposures.\n"
     "• Avoid unnecessary invasive procedures (coagulopathy). Monitor for cerebral edema, renal failure, infection, shock.\n"
     "• [color=#991B1B]Do NOT delay transfer to a specialist center while awaiting progression of encephalopathy or worsening INR.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, glucose, electrolytes, urea, creatinine, AST/ALT/bilirubin/ALP/albumin, PT/INR and fibrinogen, blood gas/lactate.\n"
     "• Paracetamol level when relevant. Viral hepatitis studies. Autoimmune markers and other etiological investigations as indicated.\n"
     "• Blood cultures if infection suspected. Ammonia may help in selected cases but should not replace clinical assessment.\n"
     "• Abdominal ultrasound with Doppler to assess hepatic/portal vasculature when appropriate."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. N-Acetylcysteine (NAC) for Suspected Paracetamol Toxicity[/color]\n"
     "• Use validated IV NAC protocol, commonly three-infusion regimen delivering total 300 mg/kg over ~21 hours. Continue/extend according to paracetamol concentration, INR, liver tests, clinical status, specialist advice.\n"
     "• [color=#991B1B]Do NOT delay NAC in clinically significant suspected paracetamol overdose while awaiting test results. Dosing protocols may differ by product/jurisdiction; use local validated protocol.[/color]\n\n"
     "[color=#1E3A8A]2. IV Dextrose for Hypoglycemia[/color]\n"
     "• Treat per institutional adult hypoglycemia protocol and bedside glucose. Recheck promptly and provide ongoing support if recurrent.\n"
     "• [color=#991B1B]Avoid relying on a single corrected glucose measurement; recurrent hypoglycemia can occur in severe liver failure.[/color]\n\n"
     "[color=#1E3A8A]3. Vitamin K when Deficiency Possible[/color]\n"
     "• Consider when deficiency or impaired absorption is plausible, as directed by treating team. Failure of INR to improve does not exclude severe hepatic synthetic failure.\n"
     "• [color=#991B1B]Do NOT assume all coagulopathy in acute liver failure is caused by vitamin K deficiency.[/color]\n\n"
     "[color=#1E3A8A]4. General Critical Care[/color]\n"
     "• Maintain oxygenation/hemodynamic stability. Avoid hypoglycemia, treat electrolyte abnormalities. Assess RRT needs when indicated. Avoid sedatives/meds that obscure neuro assessment when possible. Manage suspected cerebral edema and severe encephalopathy with specialist ICU guidance.\n"
     "• [color=#991B1B]Do NOT routinely correct INR with plasma solely to normalize lab value in absence of bleeding/planned invasive procedure; use specialist guidance.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Immediate specialist hepatology and transplant-center evaluation.\n"
     "• Cause-specific therapy, including NAC where indicated.\n"
     "• ICU monitoring for encephalopathy, cerebral edema risk, shock, renal failure, severe metabolic abnormalities.\n"
     "• Liver transplantation assessment when spontaneous recovery is unlikely."),
    ("06 — SURGICAL/TRANSPLANT INDICATIONS", "warning", 
     "• Fulminant hepatic failure with poor prognostic features.\n"
     "• Progressive encephalopathy or worsening synthetic dysfunction.\n"
     "• Severe metabolic instability or multiorgan failure.\n"
     "• Fulfillment of specialist transplant criteria."),
    ("07 — DISPOSITION", "warning", 
     "• Acute liver failure requires urgent hospital admission and early discussion with a transplant-capable center.\n"
     "• Do NOT manage established acute liver failure as a routine outpatient condition."),
    ("REFERENCES", "info", "AASLD Guidance; EASL Clinical Practice Guidelines; ACMT Guidance.")
]


# ==================== BATCH 5 (TOPICS 37-46) ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Postoperative Sepsis and Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Suspect postoperative infection in any patient with deterioration after surgery.\n"
     "• Warning signs: fever or hypothermia, tachycardia, tachypnea, hypotension, altered mental status, oliguria, increasing O2 requirement, abdominal pain, or wound discharge.\n"
     "• Possible sources: Anastomotic leak/bowel perforation, intra-abdominal abscess, infected wound/deep SSI, infected catheter, pneumonia, UTI.\n"
     "• Septic shock: sepsis with persistent circulatory failure requiring vasopressors to maintain MAP ≥65 mmHg and lactate >2 mmol/L despite adequate volume resuscitation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate surgical, anesthesia, and critical-care teams.\n"
     "• Assess ABCs, mental status, peripheral perfusion. Give O2 when indicated; prepare for ventilatory support.\n"
     "• Establish two IV lines and monitor ECG, SpO2, BP, temperature, urine output.\n"
     "• Measure lactate, CBC, renal function, electrolytes, LFTs, coagulation, glucose.\n"
     "• Obtain blood cultures and source-specific cultures before antibiotics if no meaningful delay.\n"
     "• Start IV antibiotics promptly (ideally within 1 hour in septic shock).\n"
     "• Give balanced crystalloid in reassessed boluses (initial target ~30 mL/kg within first 3 hours for sepsis-induced hypoperfusion, individualized).\n"
     "• [color=#991B1B]Arrange urgent source control; antibiotics alone are insufficient when an uncontrolled surgically correctable source persists.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, urea, creatinine, LFTs, coagulation, blood gas, lactate.\n"
     "• Blood cultures and cultures from suspected infected sites. Urinalysis/culture when indicated.\n"
     "• Contrast-enhanced CT abdomen/pelvis in sufficiently stable patient when intra-abdominal source suspected.\n"
     "• Bedside ultrasound for free fluid, collections, or biliary pathology.\n"
     "• Chest radiograph or CT when thoracic source suspected.\n"
     "• [color=#991B1B]Do NOT delay operative exploration or essential source control for imaging in a patient with an obvious surgical catastrophe or rapidly worsening instability.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Broad-Spectrum Antibiotics[/color]\n"
     "• Choose empiric therapy according to suspected source, severity, local resistance, recent antibiotic exposure, allergies, renal function.\n"
     "• Example for severe intra-abdominal infection: Piperacillin–tazobactam 4.5 g IV every 6–8 hours (adjust for renal function).\n"
     "• Carbapenem may be appropriate when severe infection with resistant organisms likely; follow local guidelines.\n\n"
     "[color=#1E3A8A]IV Crystalloid Resuscitation[/color]\n"
     "• Reassessed boluses (often 250–500 mL at a time in adults), with repeated assessment. Cumulative initial target near 30 mL/kg may be appropriate for sepsis-induced hypoperfusion, individualized.\n"
     "• Use balanced crystalloid (Lactated Ringer's or Plasma-Lyte) when appropriate.\n"
     "• Monitor MAP, capillary refill, lung findings, O2 requirement, urine output, lactate. Avoid continued fluid loading when pulmonary edema or fluid intolerance develops.\n\n"
     "[color=#1E3A8A]Norepinephrine[/color]\n"
     "• Start IV infusion per local protocol (commonly ~0.05–0.1 mcg/kg/min), titrate to response. Initial MAP target ~65 mmHg, individualized.\n"
     "• Central line preferred for ongoing administration, but initiation through suitable monitored peripheral IV may be appropriate while central access arranged. Monitor BP continuously and inspect IV site.\n"
     "• [color=#991B1B]Extravasation can cause tissue ischemia. Treat suspected extravasation immediately per local protocol.[/color]"),
    ("05 — SOURCE CONTROL", "info", 
     "• Drain accessible abscesses percutaneously when suitable.\n"
     "• Perform urgent surgery for perforation, anastomotic failure, necrotic tissue, uncontrolled contamination, or another source not amenable to less invasive treatment.\n"
     "• Remove infected devices when indicated.\n"
     "• Coordinate with interventional radiology and endoscopy when they can provide timely definitive source control."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with organ dysfunction to high-acuity setting; septic shock generally requires ICU care.\n"
     "• Reassess frequently for ongoing contamination, inadequate source control, worsening lactate, renal injury, respiratory failure.\n"
     "• Review cultures daily and de-escalate antibiotics when appropriate."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign (2021); WSES Guidelines on Intra-abdominal Infections; Surgical Infection Society Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Abdominal Compartment Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "• Intra-abdominal hypertension (IAH): sustained/repeated intra-abdominal pressure (IAP) ≥12 mmHg.\n"
     "• Abdominal compartment syndrome (ACS): sustained IAP >20 mmHg associated with new organ dysfunction or failure.\n"
     "• Risk factors: Major abdominal trauma/surgery, massive fluid resuscitation, severe pancreatitis, intra-abdominal bleeding/edema, bowel obstruction/ileus/distension, large-volume ascites or burns.\n"
     "• Clinical features: Tense/progressively distended abdomen. Increasing airway pressures and worsening ventilation. Oliguria/AKI. Hypotension, reduced venous return, increasing vasopressor requirement. Rising lactate and worsening organ perfusion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Recognize progressive abdominal distension with unexplained respiratory, renal, or circulatory deterioration.\n"
     "• Call surgical and critical-care teams urgently.\n"
     "• Assess and support ABCs.\n"
     "• Measure IAP using standardized bladder-pressure technique. Insert urinary catheter if appropriate and monitor urine output.\n"
     "• Relieve abdominal distension where possible: decompress stomach with NG tube and colon/rectum when indicated and safe.\n"
     "• Optimize analgesia and sedation; consider brief neuromuscular blockade in selected patients while definitive management arranged.\n"
     "• Avoid unnecessary ongoing fluid administration after initial resuscitation; use hemodynamic reassessment to guide further fluids.\n"
     "• [color=#991B1B]Arrange urgent decompressive laparotomy if ACS persists with organ dysfunction despite appropriate nonoperative measures.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial IAP measurements.\n"
     "• CBC, electrolytes, urea, creatinine, blood gas, lactate.\n"
     "• Continuous assessment of urine output, airway pressures, hemodynamics.\n"
     "• Bedside ultrasound or CT to identify ascites, bleeding, obstruction, or another treatable cause when patient stable enough.\n"
     "• [color=#991B1B]Do NOT delay decompression for CT when severe ACS clinically evident and organ failure progressing.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Gastric/Intestinal Decompression[/color]\n"
     "• Correctly positioned NG tube when gastric distension/ileus contributing. Rectal/colonic decompression selected according to cause and procedural safety.\n"
     "• Monitor abdominal girth, IAP, ventilatory mechanics, urine output. Confirm tube position before use.\n"
     "• [color=#991B1B]Avoid blind rectal instrumentation when perforation, severe colitis, or another contraindication suspected.[/color]\n\n"
     "[color=#1E3A8A]Analgesia/Sedation[/color]\n"
     "• Titrated agents per local ICU protocols and patient physiology. Assess sedation depth, BP, respiratory status, abdominal muscle relaxation.\n"
     "• [color=#991B1B]Sedation may improve abdominal wall compliance but does NOT replace definitive decompression when ACS persists.[/color]\n\n"
     "[color=#1E3A8A]Fluid Strategy[/color]\n"
     "• Individualize fluids according to perfusion/hemodynamic assessment; avoid fixed additional fluid target once adequate resuscitation achieved.\n"
     "• Track cumulative fluid balance, lactate, urine output, oxygenation, IAP. Consider specialist-guided fluid removal after hemodynamic stabilization when fluid overload significant.\n"
     "• [color=#991B1B]Do NOT compromise organ perfusion through overly aggressive fluid restriction or diuresis in an unstable patient.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat underlying cause: hemorrhage, bowel obstruction, ileus, ascites, intra-abdominal infection.\n"
     "• Consider percutaneous drainage of significant fluid collections when appropriate.\n"
     "• Urgent decompressive laparotomy indicated for overt ACS with persistent/worsening organ dysfunction despite initial measures.\n"
     "• Temporary abdominal closure and planned reassessment may be required after decompression.\n"
     "• Following laparotomy, monitor for recurrent ACS, fluid loss, hypothermia, abdominal wound complications."),
    ("06 — DISPOSITION", "warning", 
     "• Manage suspected/confirmed ACS in ICU or equivalent high-acuity setting.\n"
     "• Obtain immediate surgical review when organ dysfunction accompanies elevated IAP.\n"
     "• Repeat pressure measurements after interventions and whenever clinical condition worsens."),
    ("REFERENCES", "info", "WSACS Consensus Definitions and Guidelines; WSES Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Suspected Iatrogenic Intra-abdominal Organ Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Consider iatrogenic injury when patient deteriorates during or after operation, endoscopy, or invasive procedure.\n"
     "• Possible injuries: Bowel perforation, major vascular injury/hemorrhage, bile duct injury, bladder/ureteric injury, pancreatic/solid-organ injury.\n"
     "• Warning signs: Unexpected hypotension/tachycardia/falling Hb. Severe/increasing abdominal pain, guarding, rigidity.\n"
     "• Fever, peritonitis, unexplained sepsis. Hematuria, oliguria, rising creatinine, urine leakage. Bile-stained drainage/persistent bilious ascites. Free intraperitoneal air/fluid beyond expected postoperative findings."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Notify operating surgeon and senior surgical team immediately.\n"
     "• Assess ABCs and signs of hemorrhagic shock or peritonitis.\n"
     "• Establish IV access and continuous monitoring. Keep patient NPO.\n"
     "• Send CBC, electrolytes, renal function, blood gas, lactate, coagulation, group-and-crossmatch as indicated.\n"
     "• Begin resuscitation and blood-product replacement when indicated.\n"
     "• Start broad-spectrum IV antibiotics when bowel perforation or intra-abdominal contamination suspected.\n"
     "• Review operative note, procedure details, drains, postoperative trend.\n"
     "• Arrange urgent imaging or operative exploration according to stability and suspected injury."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, renal function, electrolytes, LFTs, coagulation, lactate, blood gas.\n"
     "• Contrast-enhanced CT abdomen/pelvis in stable patients with suspected bowel injury/intra-abdominal collection.\n"
     "• CT urography or other dedicated urinary tract imaging when ureteric injury suspected.\n"
     "• Retrograde cystography or CT cystography when bladder injury suspected.\n"
     "• Ultrasound or CT angiography for selected bleeding concerns.\n"
     "• Cholangiography or other biliary imaging for suspected bile duct injury, in consultation with hepatobiliary team.\n"
     "• [color=#991B1B]Imaging must NOT delay emergency surgery in an unstable patient with suspected uncontrolled bleeding or generalized peritonitis.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Crystalloid and Blood Products[/color]\n"
     "• Small, reassessed crystalloid boluses while arranging definitive treatment. Transfuse blood components according to hemorrhage severity, hemodynamics, labs, local massive transfusion protocol.\n"
     "• Monitor BP, HR, temperature, urine output, lactate, Hb, coagulation, calcium, acid-base. Activate massive transfusion protocol for life-threatening hemorrhage.\n"
     "• [color=#991B1B]Avoid excessive crystalloid in major hemorrhage (worsens dilutional coagulopathy and tissue edema).[/color]\n\n"
     "[color=#1E3A8A]Broad-Spectrum Antibiotics[/color]\n"
     "• Select IV regimen appropriate to suspected injury/contamination; piperacillin–tazobactam is one possible adult option for severe intra-abdominal contamination.\n"
     "• Adjust according to cultures, renal function, operative findings.\n"
     "• [color=#991B1B]Antibiotics do NOT replace repair, drainage, or control of ongoing contamination.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "[color=#1E3A8A]Bowel Perforation[/color]\n"
     "• Urgent surgical exploration and repair or resection. Choice depends on site, extent of injury, contamination, tissue viability, patient stability.\n\n"
     "[color=#1E3A8A]Vascular Injury/Uncontrolled Bleeding[/color]\n"
     "• Immediate operative or endovascular control, depending on vessel, available expertise, patient condition.\n\n"
     "[color=#1E3A8A]Bile Duct Injury[/color]\n"
     "• Early specialist hepatobiliary consultation. Drain collections and control sepsis; definitive reconstruction or endoscopic treatment depends on injury type and timing.\n\n"
     "[color=#1E3A8A]Bladder/Ureteric Injury[/color]\n"
     "• Urgent urology consultation. Bladder drainage, repair, ureteric stenting, or reconstruction depends on injury location and severity."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for close monitoring and specialist care.\n"
     "• Reassess for delayed perforation, ongoing hemorrhage, bile/urine leak, abscess, sepsis.\n"
     "• Document injury, interventions, follow-up plan clearly."),
    ("REFERENCES", "info", "WSES Guidelines on Iatrogenic Perforation/Bowel Injury; EAU Guidelines on Urological Trauma; ATLS.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Major Burns and Burn Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Major burns may cause airway injury, capillary leak, hypovolemia, hypothermia, electrolyte disturbances, multi-organ dysfunction.\n"
     "• Estimate TBSA using Rule of Nines (adults) or Lund–Browder chart (children).\n"
     "• Include partial-thickness and full-thickness burns in TBSA; do NOT include simple superficial erythema.\n"
     "• Consider major burn referral for extensive burns, full-thickness burns, burns involving critical areas, suspected inhalation injury, electrical/chemical burns, or burns with significant associated trauma.\n"
     "• Signs of burn shock: tachycardia, hypotension, poor peripheral perfusion, reduced urine output, rising lactate."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop burning process and ensure scene safety.\n"
     "• Remove hot/contaminated clothing and jewelry unless adherent to skin.\n"
     "• Assess ABCs; consider early airway control if progressive airway edema suspected.\n"
     "• Give supplemental O2 when indicated.\n"
     "• Expose patient sufficiently to assess burns, then cover with clean, dry dressings and prevent hypothermia.\n"
     "• Estimate TBSA and burn depth.\n"
     "• Establish IV access; obtain CBC, electrolytes, renal function, glucose, blood gas, lactate, group-and-crossmatch for major burns.\n"
     "• Start warmed isotonic crystalloid for major burns, titrate to perfusion and urine output.\n"
     "• Give appropriate analgesia and assess for associated trauma.\n"
     "• Contact burn center early for major burns or complex injuries."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, urea, creatinine, glucose, blood gas.\n"
     "• Lactate and carboxyhemoglobin when smoke inhalation or CO exposure suspected.\n"
     "• ECG and cardiac monitoring for electrical injury.\n"
     "• Urinalysis and assessment for myoglobinuria in high-voltage injury or suspected rhabdomyolysis.\n"
     "• Chest imaging when respiratory injury/associated trauma suspected.\n"
     "• [color=#991B1B]Investigations must NOT delay airway stabilization or resuscitation.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Burn Fluid Resuscitation[/color]\n"
     "• For adults with burns ≥20% TBSA, formal IV fluid resuscitation generally required.\n"
     "• Commonly used starting estimate: 2 mL × body weight (kg) × %TBSA over first 24 hours (adult thermal burns), consistent with contemporary approaches. Adjust to local burn-center protocol and clinical response.\n"
     "• Use warmed lactated Ringer's or another protocol-approved isotonic crystalloid. Calculate 24-hour requirement from time of injury, not arrival time.\n"
     "• Give ~half of calculated volume during first 8 hours after burn and remainder over following 16 hours, continuously adjusting to response. Target adult urine output commonly ~0.5 mL/kg/hour.\n"
     "• Monitor BP, mental status, peripheral perfusion, urine output, lactate, electrolytes, signs of fluid overload. Reassess frequently and titrate infusion rather than treating calculated volume as fixed prescription.\n"
     "• [color=#991B1B]Excessive resuscitation can cause pulmonary edema, extremity compartment syndrome, abdominal compartment syndrome. Do NOT delay resuscitation in a shocked patient while calculating exact formula.[/color]\n\n"
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Titrate IV opioid analgesia according to pain severity, hemodynamics, respiratory status, local protocol. Reassess pain, respiratory rate, SpO2, BP, sedation level.\n"
     "• [color=#991B1B]Opioids can cause respiratory depression and hypotension; monitor closely, especially with inhalation injury.[/color]\n\n"
     "[color=#1E3A8A]Wound Care and Tetanus Prevention[/color]\n"
     "• Tetanus prophylaxis depends on vaccination history and wound classification.\n"
     "• Cover burns with clean, dry dressings during initial stabilization. Arrange wound assessment, debridement, definitive dressing care by trained staff.\n"
     "• [color=#991B1B]Do NOT apply ice directly to major burns. Avoid prolonged cooling that can cause hypothermia. Routine systemic antibiotic prophylaxis NOT recommended for uncomplicated burns without specific indication.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Refer major burns early to specialist burn service.\n"
     "• Assess need for escharotomy when circumferential burns compromise ventilation or distal perfusion.\n"
     "• Evaluate for associated trauma, rhabdomyolysis, compartment syndrome.\n"
     "• Provide nutritional support, wound management, infection surveillance, rehabilitation as appropriate."),
    ("06 — DISPOSITION", "warning", 
     "• Admit major burns to burn center or ICU according to severity.\n"
     "• Transfer early when specialist burn care unavailable locally.\n"
     "• Monitor for airway compromise, shock, hypothermia, renal injury, infection, compartment syndrome."),
    ("REFERENCES", "info", "ABA Guidelines for Burn Patient Referral; ABA Burn Shock Resuscitation Guidelines; ISBI Practice Guidelines.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Inhalation Injury and Airway Burns")] = [
    ("01 — RECOGNIZE", "info", 
     "Suspect inhalation injury after exposure to fire in enclosed space, smoke, hot gases, or chemical combustion products.\n"
     "• Warning signs: Facial burns/singed nasal hairs. Soot in mouth/sputum. Hoarseness, stridor, drooling, difficulty swallowing. Progressive facial/oral/neck swelling. Cough, wheeze, hypoxemia, respiratory distress. Confusion, collapse, unexplained lactic acidosis (toxic gas exposure).\n"
     "• Pulse oximetry can appear reassuring in CO poisoning and cannot exclude it.\n"
     "• Cyanide toxicity may occur after enclosed-space fires (altered consciousness, cardiovascular instability, severe unexplained lactic acidosis)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Remove patient from exposure; ensure rescuer safety.\n"
     "• Give 100% O2 immediately when smoke inhalation or CO exposure suspected.\n"
     "• Assess airway patency and look for progressive edema, stridor, voice change, respiratory fatigue.\n"
     "• Arrange early endotracheal intubation when significant progressive airway compromise likely; do NOT wait for complete obstruction.\n"
     "• Assess breathing/circulation, establish IV access, monitor ECG, BP, oxygenation.\n"
     "• Obtain blood gas with co-oximetry, lactate, electrolytes, glucose, other tests guided by exposure.\n"
     "• Evaluate for associated major burns and begin appropriate burn resuscitation.\n"
     "• Contact critical care, anesthesia, burn center early."),
    ("03 — INVESTIGATIONS", "info", 
     "• Arterial/venous blood gas with carboxyhemoglobin and methemoglobin when available.\n"
     "• Lactate and acid-base assessment when cyanide exposure possible.\n"
     "• Chest radiograph as baseline when indicated; early imaging can be normal despite evolving inhalation injury.\n"
     "• Bronchoscopy may help diagnose/grade lower-airway injury in selected patients.\n"
     "• ECG and troponin when significant CO exposure or cardiac symptoms present.\n"
     "• Consider alternative/coexisting causes of respiratory deterioration (aspiration, bronchospasm, pulmonary edema, trauma)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]100% Oxygen[/color]\n"
     "• Deliver highest feasible inspired O2 concentration immediately when CO poisoning or significant smoke inhalation suspected. Use non-rebreather mask with reservoir (spontaneously breathing) or appropriate ventilatory system (intubated).\n"
     "• Continue O2 while urgently evaluating CO exposure. Follow symptoms, blood gas, carboxyhemoglobin per severity and local protocol.\n"
     "• [color=#991B1B]Standard pulse oximetry cannot reliably distinguish oxyhemoglobin from carboxyhemoglobin. A normal SpO2 does NOT exclude CO poisoning.[/color]\n\n"
     "[color=#1E3A8A]Endotracheal Intubation[/color]\n"
     "• Use appropriate rapid-sequence intubation regimen per patient physiology and local airway protocol. Prepare airway equipment, suction, backup devices, rescue plan.\n"
     "• Intubate early when progressive upper-airway edema, stridor, significant respiratory distress, reduced consciousness, or impending airway obstruction present.\n"
     "• Confirm tube placement with waveform capnography and clinical assessment. Monitor ventilation, oxygenation, airway pressures, hemodynamics.\n"
     "• [color=#991B1B]Airway edema can progress rapidly. Delayed intubation may make airway control extremely difficult. Facial burns alone do NOT automatically require intubation; decisions should consider exposure history, symptoms, examination, trajectory.[/color]\n\n"
     "[color=#1E3A8A]Suspected Cyanide Toxicity[/color]\n"
     "• In adults with strong clinical suspicion of severe cyanide poisoning after smoke exposure: hydroxocobalamin commonly 5 g IV; second 5 g dose may be considered per response and local toxicology guidance.\n"
     "• Monitor hemodynamics, acid-base status, lactate trend, clinical response.\n"
     "• [color=#991B1B]Hydroxocobalamin can interfere with certain lab tests and may cause red discoloration of skin/urine. Do NOT give antidotes indiscriminately for minor smoke exposure.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Manage significant inhalation injury in ICU or burn center.\n"
     "• Provide lung-protective ventilation when required.\n"
     "• Treat bronchospasm with inhaled bronchodilators when indicated.\n"
     "• Evaluate for CO poisoning and consider hyperbaric O2 consultation for selected severe cases.\n"
     "• Monitor for delayed pulmonary edema, ARDS, airway casts, secondary infection.\n"
     "• Avoid routine prophylactic systemic antibiotics or corticosteroids unless another specific indication exists."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with significant inhalation injury, airway symptoms, abnormal gas exchange, toxic exposure, or major associated burns.\n"
     "• Transfer to specialist center when advanced airway, burn, or critical-care support required.\n"
     "• Reassess frequently because respiratory findings may worsen over several hours."),
    ("REFERENCES", "info", "ABA Guidelines; CDC CO Poisoning Guidance; WHO Smoke/Toxic Gas Exposure; ISBI Guidelines.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Electrical Burns and High-Voltage Electrical Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Electrical injury may cause deep muscle necrosis, vascular injury, arrhythmias, rhabdomyolysis, AKI, and compartment syndrome despite small external burns.\n"
     "• High-voltage injury generally defined as exposure to ≥1,000 volts.\n"
     "• Assess for: LOC or cardiac arrest. Entry/exit wounds. Deep tissue injury/progressive swelling. Severe muscle pain, weakness, dark urine. Limb ischemia/compartment syndrome. Associated falls, fractures, spinal injury.\n"
     "• Lightning injury can cause cardiac arrest, respiratory arrest, burns, neurologic complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure electrical source disconnected before touching patient.\n"
     "• Follow standard resuscitation; initiate CPR and defibrillation when indicated.\n"
     "• Assess ABCs and possible associated trauma.\n"
     "• Obtain 12-lead ECG and initiate cardiac monitoring for significant exposure.\n"
     "• Establish IV access and assess for rhabdomyolysis/major tissue injury.\n"
     "• Remove jewelry/constrictive items before swelling develops.\n"
     "• Cover burns with clean, dry dressings and prevent hypothermia.\n"
     "• Obtain urgent surgical assessment for high-voltage exposure, deep burns, neurovascular compromise, or suspected compartment syndrome.\n"
     "• Contact burn center early."),
    ("03 — INVESTIGATIONS", "info", 
     "• 12-lead ECG; continuous monitoring when indicated by exposure severity or abnormal findings.\n"
     "• CBC, electrolytes, urea, creatinine, glucose, blood gas when clinically indicated.\n"
     "• Creatine kinase (CK), potassium, calcium, phosphate, urinalysis for suspected muscle injury.\n"
     "• Urine or plasma assessment for myoglobin when available.\n"
     "• ECG monitoring and troponin when cardiac arrest, chest pain, ECG abnormality, or suspected myocardial injury.\n"
     "• Imaging for fractures, spinal injury, or other trauma according to examination.\n"
     "• Serial neurovascular examinations of affected limbs."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Crystalloid for Rhabdomyolysis[/color]\n"
     "• Individualize according to perfusion, urine output, renal function, extent of muscle injury. In adults with significant rhabdomyolysis, starting rate ~200–500 mL/hour may be considered in selected patients, then titrated to response.\n"
     "• Commonly used urine-output target in adults with substantial rhabdomyolysis: ~1–3 mL/kg/hour, generally not exceeding 300 mL/hour without specialist direction.\n"
     "• Monitor urine output, fluid balance, potassium, creatinine, CK, calcium, acid-base. Reassess frequently for pulmonary edema/fluid overload.\n"
     "• [color=#991B1B]Do NOT administer large fluid volumes blindly in anuric patients or those with heart failure. Routine bicarbonate/mannitol NOT recommended for every case; use only for specific indication under appropriate protocol.[/color]\n\n"
     "[color=#1E3A8A]Hyperkalemia Treatment[/color]\n"
     "• If severe hyperkalemia or hyperkalemic ECG changes: IV calcium for myocardial stabilization per local emergency protocol. Insulin with dextrose and nebulized beta-2 agonist may be used to shift potassium intracellularly.\n"
     "• Continuous ECG monitoring. Recheck potassium and glucose after treatment. Arrange urgent renal support when hyperkalemia refractory or associated with severe renal failure.\n"
     "• [color=#991B1B]IV calcium stabilizes myocardium but does NOT lower serum potassium. Insulin can cause delayed hypoglycemia; establish glucose-monitoring plan.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Urgent fasciotomy for confirmed compartment syndrome with compatible clinical findings.\n"
     "• Early debridement of nonviable tissue when indicated.\n"
     "• Escharotomy when circumferential burns compromise perfusion or ventilation.\n"
     "• Vascular repair or other operative treatment for associated injuries.\n"
     "• Amputation may be required for irreversible tissue destruction (decisions by experienced multidisciplinary team)."),
    ("06 — DISPOSITION", "warning", 
     "• Admit high-voltage injuries, significant deep burns, rhabdomyolysis, arrhythmias, neurovascular compromise, or associated major trauma.\n"
     "• Transfer to burn center when specialist management required.\n"
     "• Continue serial assessment because muscle necrosis and compartment syndrome may evolve after initial presentation."),
    ("REFERENCES", "info", "ABA Guidelines; AHA ACLS Guidance; ERC ALS Guidelines; ISBI Guidelines.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Chemical Burns and Emergency Decontamination")] = [
    ("01 — RECOGNIZE", "info", 
     "Chemical burns can result from acids, alkalis, solvents, cement, phenols, industrial chemicals.\n"
     "• Alkali injuries can penetrate deeply and continue damaging tissue after initial exposure.\n"
     "• Important findings: Pain, erythema, blistering, tissue necrosis. Ocular pain, redness, blurred vision, visual loss. Respiratory symptoms following inhalation. Systemic toxicity after absorption of particular chemicals.\n"
     "• Hydrofluoric acid exposure is particularly dangerous (fluoride can cause severe hypocalcemia, hypomagnesemia, hyperkalemia, cardiac arrhythmias).\n"
     "• Dry chemicals may need to be brushed off before irrigation if adding water would trigger hazardous reaction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Protect staff with appropriate PPE. Remove patient from contaminated environment.\n"
     "• Remove contaminated clothing, shoes, watches, jewelry.\n"
     "• Brush off dry chemical powders before irrigation when safe/appropriate.\n"
     "• Irrigate most skin chemical exposures promptly with copious running water.\n"
     "• Begin eye irrigation immediately for ocular exposure; do NOT delay while searching for specialized solution.\n"
     "• Assess airway/breathing after inhalation exposure.\n"
     "• Check vital signs, pain, burn extent, possible systemic toxicity.\n"
     "• Contact poison center, toxicologist, or specialist burn service for chemical-specific guidance.\n"
     "• [color=#991B1B]Avoid neutralizing an acid with an alkali or vice versa; reaction can generate heat and worsen injury.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Identify chemical using container, safety data sheet, or workplace information when available.\n"
     "• Assess burn depth, BSA, involvement of eyes, airway, face.\n"
     "• CBC, electrolytes, renal function, blood gas when significant injury/systemic toxicity suspected.\n"
     "• ECG and electrolytes (including calcium, magnesium, potassium) after suspected hydrofluoric acid exposure.\n"
     "• Ocular pH assessment and visual examination after eye exposure.\n"
     "• Additional investigations according to specific agent and symptoms."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Skin Decontamination[/color]\n"
     "• No fixed drug dose. Irrigate with copious water for prolonged period, commonly at least 20–30 minutes, and longer when required by chemical/persistent symptoms.\n"
     "• Use safe source of running water or appropriate emergency irrigation system. Remove contaminated clothing; prevent contaminated runoff from exposing staff/other body areas.\n"
     "• Begin immediately and continue while checking pain, skin appearance, chemical-specific guidance. Prevent hypothermia during prolonged irrigation.\n"
     "• [color=#991B1B]Some agents have specific decontamination requirements. Consult poison center/chemical safety guidance for reactive substances (elemental metals, agents that react dangerously with water).[/color]\n\n"
     "[color=#1E3A8A]Ocular Chemical Exposure[/color]\n"
     "• Immediate, continuous irrigation; no fixed volume applies to all exposures. Use clean tap water, normal saline, or another suitable irrigation fluid immediately available.\n"
     "• Irrigate continuously and evert eyelids when feasible to remove retained particles. Check ocular pH when available; continue irrigation until pH near physiologic and remains stable after brief pause.\n"
     "• Arrange urgent ophthalmology assessment for significant exposures.\n"
     "• [color=#991B1B]Do NOT delay irrigation to obtain sterile fluid or measure pH first.[/color]\n\n"
     "[color=#1E3A8A]Hydrofluoric Acid Exposure[/color]\n"
     "• Treat as medical emergency. Calcium gluconate may be used topically, by infiltration, or intravenously according to site/severity and specialist-guided protocol.\n"
     "• Obtain urgent toxicology or burn-specialist advice. Monitor ECG and serial calcium, magnesium, potassium. Treat systemic electrolyte abnormalities promptly.\n"
     "• [color=#991B1B]Hydrofluoric acid can cause life-threatening arrhythmias even when skin findings initially appear limited. Avoid blind/excessive local calcium injection (tissue injury).[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Urgent debridement may be required for progressive necrosis or deeply injured tissue.\n"
     "• Ocular burns require urgent ophthalmic evaluation.\n"
     "• Compartment syndrome or limb ischemia requires immediate surgical assessment.\n"
     "• Significant airway injury requires early airway and critical-care involvement."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with extensive burns, deep injury, ocular involvement, systemic toxicity, significant pain requiring monitored treatment, or high-risk chemical exposure.\n"
     "• Arrange burn-center or specialist transfer when appropriate.\n"
     "• Provide clear documentation of chemical, decontamination performed, serial findings."),
    ("REFERENCES", "info", "ABA Guidelines; CDC Chemical Emergencies/Decontamination; NIOSH Emergency Response Database.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Descending Necrotizing Mediastinitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Descending necrotizing mediastinitis is a rapidly progressive, potentially fatal infection spreading from oropharynx/deep neck spaces into mediastinum.\n"
     "• Common sources: Deep neck infection, odontogenic infection, peritonsillar/retropharyngeal infection, cervical trauma/postoperative infection.\n"
     "• Warning signs: Fever, toxic appearance, severe neck/chest pain. Neck swelling, dysphagia, odynophagia, trismus. Dyspnea, tachycardia, hypotension, septic shock. Crepitus/swelling extending into chest.\n"
     "• Early symptoms may be nonspecific; rapid deterioration should raise suspicion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate ENT, thoracic/cardiothoracic surgery, anesthesia, and critical-care teams.\n"
     "• Assess airway early; progressive neck swelling may make later intubation difficult.\n"
     "• Provide O2 and establish IV access with continuous monitoring.\n"
     "• Obtain blood cultures and lab tests without delaying treatment.\n"
     "• Start broad-spectrum IV antibiotics covering oral streptococci, anaerobes, other likely pathogens.\n"
     "• Obtain urgent contrast-enhanced CT of neck/chest when patient stable enough.\n"
     "• [color=#991B1B]Arrange urgent drainage and debridement; antibiotics alone are inadequate for established necrotizing mediastinal infection.[/color]\n"
     "• Resuscitate septic shock according to current sepsis protocols."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal/liver function, coagulation, blood gas, lactate.\n"
     "• Blood cultures and operative tissue/fluid cultures.\n"
     "• Contrast-enhanced CT of neck/chest to identify deep-space infection, mediastinal extension, gas, drainable collections.\n"
     "• Additional imaging based on suspected pleural, pericardial, or vascular complications.\n"
     "• [color=#991B1B]Do NOT delay emergency source control in rapidly deteriorating patient solely to obtain additional imaging.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Broad-Spectrum IV Antibiotics[/color]\n"
     "• Select regimen according to severity, allergy, renal function, local resistance. One possible adult empiric regimen: piperacillin–tazobactam 4.5 g IV every 6–8 hours (dosing/infusion adjusted to local protocols).\n"
     "• Add MRSA coverage (e.g., vancomycin) when epidemiology/clinical risk supports.\n"
     "• If necrotizing soft-tissue infection or toxin-mediated streptococcal disease suspected, specialist-guided addition of protein-synthesis inhibitor may be appropriate.\n"
     "• Administer promptly and obtain cultures when no delay to therapy. Monitor renal function, drug toxicity, culture results. Narrow therapy when possible.\n"
     "• [color=#991B1B]Renal adjustment and local resistance patterns essential. Antibiotics must NOT delay surgical drainage/debridement.[/color]\n\n"
     "[color=#1E3A8A]Septic Shock Support[/color]\n"
     "• Individualized crystalloid resuscitation and norepinephrine when hypotension persists despite appropriate fluid assessment. Typical initial MAP target ~65 mmHg, individualized.\n"
     "• [color=#991B1B]Avoid indiscriminate fluid loading when respiratory compromise or fluid overload developing.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Drain original cervical or odontogenic source.\n"
     "• Perform surgical drainage and debridement of infected mediastinal compartments.\n"
     "• Drain pleural collections or empyema when present.\n"
     "• Repeat operative assessment when infection persists or tissue necrosis progresses.\n"
     "• Coordinate approach with thoracic surgery based on anatomical extent of infection."),
    ("06 — DISPOSITION", "warning", 
     "• ICU admission usually required.\n"
     "• Continue close monitoring for airway compromise, septic shock, pleural infection, pericardial involvement, recurrent mediastinal collections.\n"
     "• Reassess source control early if fever, vasopressor needs, or organ dysfunction persist."),
    ("REFERENCES", "info", "EACTS Guidance; WSES Guidance on Severe Surgical Infections; Surviving Sepsis Campaign.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Empyema Requiring Urgent Drainage")] = [
    ("01 — RECOGNIZE", "info", 
     "Empyema is infected purulent material in pleural space, commonly following pneumonia but also possible after thoracic surgery, trauma, or esophageal perforation.\n"
     "• Suspect in patients with fever, pleuritic chest pain, dyspnea, persistent sepsis, or failure to improve with antibiotics.\n"
     "• Complicated parapneumonic effusion suggested by pleural fluid with low pH, low glucose, positive microbiology, or loculations.\n"
     "• Findings may include reduced breath sounds, dullness to percussion, respiratory distress.\n"
     "• A pleural collection associated with septic shock or respiratory failure requires urgent specialist assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and oxygenation. Give supplemental O2 if indicated.\n"
     "• Establish IV access and monitor vital signs.\n"
     "• Obtain CBC, renal function, electrolytes, blood cultures, lactate if sepsis suspected.\n"
     "• Perform chest ultrasound to identify and characterize pleural fluid.\n"
     "• Start appropriate IV antibiotics promptly when bacterial infection or sepsis suspected.\n"
     "• Arrange diagnostic aspiration and pleural drainage when indicated.\n"
     "• Involve thoracic surgery early for loculated infection, trapped lung, failure of drainage, or ongoing sepsis.\n"
     "• If esophageal perforation or postoperative leak suspected, investigate and control underlying source urgently."),
    ("03 — INVESTIGATIONS", "info", 
     "• Chest radiograph as initial assessment.\n"
     "• Thoracic ultrasound to assess fluid volume, septations, safe drainage site.\n"
     "• Contrast-enhanced CT chest when needed to define loculations, pleural thickening, lung abscess, or another source.\n"
     "• Pleural fluid Gram stain/culture, pH measured appropriately, glucose, LDH, cell count.\n"
     "• Blood cultures when systemic infection suspected.\n"
     "• [color=#991B1B]Avoid delaying drainage in an unstable patient with an obvious infected pleural collection.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Antibiotics[/color]\n"
     "• Choose empiric antibiotics based on community-acquired vs hospital-acquired infection, prior procedures, local resistance, allergy, renal function.\n"
     "• Community-acquired coverage may include beta-lactam/beta-lactamase inhibitor; hospital-acquired may require broader Gram-negative and MRSA coverage per local guidance.\n"
     "• Administer promptly in sepsis. Obtain pleural/blood cultures when feasible. Adjust to microbiology and clinical response.\n"
     "• [color=#991B1B]Antibiotics alone are often insufficient when established pleural pus or complicated infected effusion requires drainage.[/color]\n\n"
     "[color=#1E3A8A]Intercostal Chest Drain[/color]\n"
     "• Use ultrasound-guided site selection when possible. Select suitable small-bore or larger-bore drain based on fluid characteristics, loculations, local thoracic protocols.\n"
     "• Insert using appropriate aseptic technique and procedural expertise. Connect to prescribed drainage system.\n"
     "• Monitor respiratory status, drain output, air leak, pain, imaging response.\n"
     "• [color=#991B1B]Avoid blind insertion when ultrasound guidance available. Drain insertion can cause bleeding, organ injury, malposition; reassess immediately if respiratory/hemodynamic status worsens.[/color]\n\n"
     "[color=#1E3A8A]Intrapleural tPA and DNase[/color]\n"
     "• In selected adults with residual loculated pleural infection despite chest-tube drainage: alteplase (tPA) 10 mg plus DNase 5 mg intrapleurally, twice daily for up to 3 days, following specialist assessment and local protocol.\n"
     "• Assess bleeding risk and anticoagulant use before treatment.\n"
     "• [color=#991B1B]Do NOT use intrapleural fibrinolytic therapy as substitute for urgent surgery when patient has uncontrolled sepsis or requires definitive operative management.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Persistent sepsis or residual collection despite appropriate antibiotics and drainage.\n"
     "• Extensive loculations not adequately drained.\n"
     "• Trapped lung or organized pleural peel.\n"
     "• Failure of less invasive management.\n"
     "• VATS or open decortication may be required, depending on stage, anatomy, patient fitness."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with empyema for antibiotics, drainage, monitoring.\n"
     "• ICU care may be required for respiratory failure or septic shock.\n"
     "• Review imaging, drainage output, cultures, clinical response regularly."),
    ("REFERENCES", "info", "BTS Pleural Disease Guideline (2023); AATS Empyema Management Guidelines; CHEST Guidance on Pleural Infection.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Complex Soft-Tissue Defects and Extensive Skin Loss")] = [
    ("01 — RECOGNIZE", "info", 
     "Extensive skin and soft-tissue loss may follow trauma, burns, infection, degloving injury, surgical complications, or tissue necrosis.\n"
     "• Assess: Defect size, depth, contamination. Exposure of bone, tendon, vessels, nerves, implants. Distal circulation, sensation, motor function. Associated fractures/vascular injury. Evidence of infection/ongoing tissue necrosis.\n"
     "• Major defects may require staged debridement, temporary wound coverage, skin grafting, or flap reconstruction.\n"
     "• Exposed critical structures often cannot be managed by simple dressings or skin grafting alone."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Control life-threatening hemorrhage.\n"
     "• Assess ABCs and associated injuries.\n"
     "• Examine and document distal neurovascular status before and after any intervention.\n"
     "• Cover wound with sterile, nonadherent dressing; use saline-moistened dressings when appropriate for exposed viable tissue.\n"
     "• Prevent hypothermia and treat shock.\n"
     "• Provide analgesia and assess tetanus immunization status.\n"
     "• Administer antibiotics for contaminated open injuries or established infection per local guidelines.\n"
     "• Arrange urgent surgical assessment for exposed vessels, nerves, tendons, bone, implants, or extensive tissue loss.\n"
     "• Coordinate with plastic surgery, orthopedics, vascular surgery, or other specialties according to injured structures."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, glucose, coagulation when clinically indicated.\n"
     "• Group-and-crossmatch for major bleeding or extensive operative injury.\n"
     "• Plain radiographs for suspected fractures or retained foreign bodies.\n"
     "• CT or CT angiography when deep injury or vascular compromise suspected and imaging will not delay necessary treatment.\n"
     "• Wound cultures when infection present; routine superficial swabs of clean wounds may be unhelpful.\n"
     "• Serial neurovascular examinations and documentation of wound progression."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage Control[/color]\n"
     "• Apply firm direct pressure for external bleeding. Use hemostatic dressings or a tourniquet when indicated and available (for life-threatening extremity hemorrhage when direct pressure ineffective/impractical, following training and local protocols).\n"
     "• [color=#991B1B]Do NOT blindly clamp vessels in a deep wound; adjacent nerves and vessels may be damaged.[/color]\n\n"
     "[color=#1E3A8A]Antibiotics for Contaminated/Infected Wounds[/color]\n"
     "• Select antibiotics according to mechanism, contamination, anatomical site, allergy, local protocol.\n"
     "• For major open fractures, follow dedicated open-fracture protocol, including timely antibiotic administration and operative debridement.\n"
     "• [color=#991B1B]Antibiotics do NOT replace irrigation, removal of devitalized tissue, or surgical source control. Routine prolonged antibiotics NOT indicated for every clean soft-tissue defect.[/color]\n\n"
     "[color=#1E3A8A]Wound Coverage and Temporary Management[/color]\n"
     "• Use sterile dressing, appropriate wound-contact layer, temporary coverage system selected by treating surgical team.\n"
     "• Keep exposed structures protected and avoid desiccation of viable tissue.\n"
     "• Negative-pressure wound therapy may be appropriate in selected wounds after adequate debridement and hemostasis.\n"
     "• [color=#991B1B]Negative-pressure therapy is not a substitute for debridement and is unsuitable in some wounds, including certain wounds with exposed major vessels or uncontrolled bleeding.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Perform timely irrigation and debridement of contaminated or devitalized tissue.\n"
     "• Reassess tissue viability when injury zone is evolving.\n"
     "• Restore blood flow when vascular injury present.\n"
     "• Stabilize associated fractures and protect injured tendons, nerves, vessels.\n"
     "• Choose definitive coverage according to wound bed and exposed structures:\n"
     "  - Secondary healing for selected small wounds.\n"
     "  - Skin grafting for suitable vascularized wound beds.\n"
     "  - Local or free-flap reconstruction when critical structures exposed or durable tissue coverage needed.\n"
     "• Plan reconstruction with relevant surgical specialties."),
    ("06 — DISPOSITION", "warning", 
     "• Admit extensive, contaminated, infected, or complex defects requiring operative treatment.\n"
     "• Transfer to center with reconstructive expertise when local capability insufficient.\n"
     "• Arrange follow-up for wound assessment, infection surveillance, rehabilitation, functional recovery."),
    ("REFERENCES", "info", "ATLS; WHO Global Guidelines for Prevention of SSI; Specialist Guidelines for Open Fractures/Complex Wounds.")
]


# ==================== BATCH 6 (TOPICS 47-56) ====================

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Ischemic Colitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute ischemic colitis occurs when colonic blood flow becomes insufficient to meet tissue requirements. Often affects watershed areas (splenic flexure, rectosigmoid junction).\n"
     "• Risk factors: Older age, atherosclerotic vascular disease, hypotension/shock/dehydration/blood loss, heart failure/arrhythmias, vasoconstrictor exposure, recent vascular/major abdominal surgery.\n"
     "• Typical presentation: Sudden crampy abdominal pain. Urgent defecation followed by bloody diarrhea or hematochezia. Abdominal tenderness (usually without severe peritonitis in uncomplicated disease).\n\n"
     "[color=#991B1B]Warning signs of advanced ischemia:[/color] Persistent severe pain, guarding, rebound tenderness, fever, metabolic acidosis, rising lactate, shock, perforation/pneumatosis/portal venous gas on imaging."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and hemodynamic stability.\n"
     "• Keep patient NPO. Establish IV access and begin appropriate isotonic crystalloid resuscitation if hypovolemic.\n"
     "• Obtain CBC, electrolytes, renal function, coagulation, blood gas, lactate.\n"
     "• Perform urgent abdominal examination and involve surgery early if severe disease suspected.\n"
     "• Obtain contrast-enhanced CT abdomen/pelvis when appropriate.\n"
     "• Start broad-spectrum IV antibiotics for moderate/severe disease, systemic toxicity, or suspected transmural injury.\n"
     "• Avoid vasoconstrictors where possible and correct precipitating cause of low perfusion.\n"
     "• Arrange urgent operative assessment for peritonitis, perforation, gangrene, or deterioration."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, urea, creatinine, LFTs, coagulation, lactate.\n"
     "• Blood gas when severe illness or metabolic acidosis suspected.\n"
     "• Contrast-enhanced CT abdomen/pelvis to assess colonic wall thickening, edema, pneumatosis, or complications.\n"
     "• CT angiography if acute mesenteric arterial occlusion or another vascular cause suspected.\n"
     "• Colonoscopy with cautious insufflation may help confirm diagnosis in selected stable patients (usually within 48 hours).\n"
     "• [color=#991B1B]Avoid colonoscopy when peritonitis, perforation, or suspected gangrenous bowel makes procedure unsafe.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Fluid Resuscitation[/color]\n"
     "• Isotonic crystalloid in reassessed boluses according to hemodynamics and fluid tolerance.\n"
     "• Monitor BP, urine output, abdominal findings, renal function, lactate. Correct dehydration/hypotension while avoiding fluid overload.\n"
     "• [color=#991B1B]Persistent pain or worsening acidosis despite resuscitation may indicate ongoing bowel ischemia requiring urgent surgical assessment.[/color]\n\n"
     "[color=#1E3A8A]Broad-Spectrum Antibiotics[/color]\n"
     "• In moderate/severe ischemic colitis, use IV antibiotics covering enteric Gram-negative organisms and anaerobes per local protocols.\n"
     "• One possible adult regimen: Piperacillin–tazobactam 4.5 g IV every 6–8 hours (adjust for renal function).\n"
     "• [color=#991B1B]Antibiotics do NOT restore blood flow or replace surgery when transmural necrosis is present.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "Urgent surgery is indicated when there is:\n"
     "• Generalized peritonitis.\n"
     "• Perforation or gangrenous bowel.\n"
     "• Persistent hemodynamic instability attributable to bowel injury.\n"
     "• Clinical deterioration despite appropriate resuscitation/treatment.\n"
     "• Strong evidence of transmural necrosis.\n\n"
     "Surgical management may involve resection of nonviable colon, with anastomosis or stoma formation depending on stability, contamination, tissue viability."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with clinically significant ischemic colitis for monitoring and treatment.\n"
     "• ICU care for shock, severe acidosis, or organ failure.\n"
     "• Repeat abdominal examinations and laboratory assessment according to severity."),
    ("REFERENCES", "info", "ACG Clinical Guideline on Colon Ischemia; WSES Guidelines on Acute Mesenteric Ischemia.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Mesenteric Venous Thrombosis")] = [
    ("01 — RECOGNIZE", "info", 
     "Mesenteric venous thrombosis causes impaired venous drainage, bowel wall edema, congestion, and potentially intestinal infarction.\n"
     "• Risk factors: Inherited/acquired thrombophilia, malignancy, cirrhosis/portal hypertension, pancreatitis/intra-abdominal inflammation, recent abdominal surgery, estrogen exposure, prior VTE.\n"
     "• Presentation: Abdominal pain (initially exceeds physical exam findings). Nausea/vomiting/diarrhea. GI bleeding in advanced disease. Abdominal distension, peritonitis, or shock when bowel infarction develops."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess hemodynamic stability and signs of bowel ischemia.\n"
     "• Keep patient NPO. Establish IV access and correct dehydration/shock.\n"
     "• Obtain CBC, electrolytes, renal function, coagulation, blood gas, lactate.\n"
     "• Request urgent contrast-enhanced CT with mesenteric venous phase or CT angiography as appropriate.\n"
     "• Involve general surgery and vascular/interventional specialists early.\n"
     "• Start therapeutic anticoagulation promptly when diagnosis established and no contraindication, under treating team's direction.\n"
     "• Start broad-spectrum antibiotics if bowel infarction, perforation, or systemic infection suspected.\n"
     "• Arrange urgent surgery for peritonitis or suspected necrotic bowel."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, urea, creatinine, coagulation, lactate.\n"
     "• Contrast-enhanced CT demonstrating thrombus in superior mesenteric vein or tributaries, bowel edema, mesenteric congestion, or associated portal venous thrombosis.\n"
     "• Assess for bowel hypoenhancement, pneumatosis, portal venous gas, free air.\n"
     "• Thrombophilia evaluation may be considered after stabilization.\n"
     "• [color=#991B1B]A normal lactate does NOT exclude early intestinal ischemia.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Unfractionated Heparin[/color]\n"
     "• Common therapeutic IV regimen in adults: initial bolus 80 units/kg followed by 18 units/kg/hour, adjusted using institutional aPTT or anti-Xa protocol. Bolus dosing may need modification/omission when bleeding risk high or urgent surgery anticipated.\n"
     "• Monitor aPTT/anti-Xa per local protocol, platelet count, hemoglobin, signs of bleeding.\n"
     "• [color=#991B1B]Do NOT start anticoagulation without assessing active bleeding and contraindications. Suspected HIT requires alternative anticoagulant and specialist management.[/color]\n\n"
     "[color=#1E3A8A]IV Fluids and Supportive Care[/color]\n"
     "• Reassessed isotonic crystalloid boluses according to perfusion and fluid tolerance. Monitor hemodynamics, urine output, lactate, renal function, serial abdominal findings.\n"
     "• [color=#991B1B]Resuscitation must NOT delay surgery when bowel necrosis or perforation suspected.[/color]\n\n"
     "[color=#1E3A8A]Antibiotics when Bowel Injury Suspected[/color]\n"
     "• Broad-spectrum IV coverage for enteric Gram-negative organisms and anaerobes per local protocol.\n"
     "• [color=#991B1B]Antibiotics are NOT routinely a substitute for anticoagulation in uncomplicated venous thrombosis.[/color]"),
    ("05 — SURGICAL/INTERVENTIONAL MANAGEMENT", "info", 
     "• Anticoagulation is first-line treatment in many patients without peritonitis or established bowel necrosis.\n"
     "• Urgent laparotomy indicated for peritonitis, perforation, or suspected infarcted bowel.\n"
     "• Resect clearly nonviable intestine while preserving viable bowel where possible.\n"
     "• Endovascular treatment may be considered in selected patients who deteriorate despite anticoagulation but have no indication for immediate laparotomy."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for monitored treatment and serial abdominal examinations.\n"
     "• ICU care for shock, severe bowel ischemia, or organ dysfunction.\n"
     "• Determine duration/long-term choice of anticoagulation according to cause, bleeding risk, specialist advice."),
    ("REFERENCES", "info", "WSES Acute Mesenteric Ischemia Guidelines; ESVS Mesenteric Arterial/Venous Disease Guidelines; ASH VTE Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Massive Hemothorax")] = [
    ("01 — RECOGNIZE", "info", 
     "Hemothorax is blood accumulation in pleural cavity, usually following blunt/penetrating chest trauma. Massive hemothorax can cause hemorrhagic shock and respiratory compromise.\n"
     "• Suspect in trauma patient with: Hypotension, tachycardia, pallor, altered mental status. Respiratory distress, reduced breath sounds on one side. Dullness to percussion on affected side. Chest wall injury/penetrating trauma.\n"
     "• Common sources: Intercostal vessels, lung parenchyma, internal mammary vessels, major intrathoracic vessels."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma resuscitation principles; assess ABCs.\n"
     "• Administer oxygen and support ventilation when required.\n"
     "• Activate major hemorrhage/massive transfusion protocol when indicated.\n"
     "• Establish large-bore IV or IO access.\n"
     "• Begin blood-product resuscitation for major hemorrhage; avoid excessive crystalloid.\n"
     "• Perform bedside eFAST or chest radiography if no delay to treatment.\n"
     "• Insert appropriate chest drain when indicated by trained personnel.\n"
     "• Obtain immediate thoracic/trauma surgical consultation.\n"
     "• Consider emergency thoracotomy in selected patients with traumatic arrest or profound instability per local protocols."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside eFAST for pleural fluid and associated pericardial/abdominal injury.\n"
     "• Portable chest radiograph when appropriate.\n"
     "• CBC, blood gas, lactate, coagulation, fibrinogen, electrolytes, group-and-crossmatch.\n"
     "• CT chest in sufficiently stable patients to identify vascular/associated injuries.\n"
     "• Monitor chest-drain output and hemodynamic response.\n"
     "• [color=#991B1B]Do NOT delay drainage or operative hemorrhage control for CT in unstable patient.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Blood-Product Resuscitation[/color]\n"
     "• Use institutional major hemorrhage protocol for life-threatening bleeding. Balanced component therapy or whole blood may be used per local availability/protocol. Transition to lab/viscoelastic-guided resuscitation as soon as feasible.\n"
     "• Monitor BP, temperature, Hb, lactate, coagulation, fibrinogen, calcium, ongoing blood loss. Replace calcium when clinically indicated. Prevent hypothermia and correct coagulopathy.\n"
     "• [color=#991B1B]Do NOT delay life-saving blood products in uncontrolled hemorrhagic shock while waiting for Hb result. Avoid relying on large crystalloid volumes in major hemorrhage.[/color]\n\n"
     "[color=#1E3A8A]Chest Tube Drainage[/color]\n"
     "• Prepare sterile chest-drain equipment and appropriate monitoring. Select drain size according to injury, clot burden, local trauma protocol.\n"
     "• Insert using appropriate technique and confirm effective drainage. Record immediate and ongoing output.\n"
     "• [color=#991B1B]A chest tube may reveal severity of bleeding but does NOT itself control major vascular injury. Do NOT clamp a chest drain routinely in an actively bleeding patient unless specifically directed.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "Immediate operative assessment required for hemodynamic instability or suspected major intrathoracic bleeding.\n"
     "Common triggers for considering thoracotomy:\n"
     "• Initial chest-tube output around 1,500 mL in an adult.\n"
     "• Ongoing drainage around 200 mL/hour for several hours.\n"
     "• Persistent shock or transfusion requirement despite drainage.\n"
     "• Suspected major vascular or cardiac injury.\n"
     "*(These are guideposts, not absolute thresholds; physiology, bleeding rate, mechanism, local protocols determine urgency).*"),
    ("06 — DISPOSITION", "warning", 
     "• Admit significant hemothorax for monitored care.\n"
     "• ICU care required for persistent shock, respiratory failure, major transfusion, or operative management.\n"
     "• Reassess for retained hemothorax, empyema, persistent air leak, delayed bleeding."),
    ("REFERENCES", "info", "ATLS; EAST Practice Management Guidelines on Hemothorax/Occult Pneumothorax; Western Trauma Association Critical Decisions.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Flail Chest and Severe Chest Wall Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Flail chest typically results from multiple adjacent ribs fractured in at least two places, producing a free-floating segment of chest wall.\n"
     "• Paradoxical movement may be visible, but absence does NOT exclude flail chest.\n"
     "• Respiratory failure often reflects underlying pulmonary contusion, pain-related hypoventilation, and associated injuries rather than chest-wall instability alone.\n"
     "• Look for: Severe chest pain/shallow breathing. Tachypnea, hypoxemia, respiratory fatigue. Reduced breath sounds or associated pneumothorax. Subcutaneous emphysema. Shock suggesting associated bleeding/another major injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma ABCDE approach.\n"
     "• Administer oxygen and monitor SpO2, ECG, BP.\n"
     "• Assess for tension pneumothorax or massive hemothorax and treat immediately when suspected.\n"
     "• Provide effective multimodal analgesia.\n"
     "• Assess for pulmonary contusion, aspiration, associated abdominal/spinal injuries.\n"
     "• Obtain chest imaging after immediate life-threatening conditions addressed.\n"
     "• Use noninvasive or invasive ventilatory support when clinically indicated.\n"
     "• Involve trauma, thoracic surgery, critical care early for severe injury."),
    ("03 — INVESTIGATIONS", "info", 
     "• Chest radiograph for initial assessment.\n"
     "• CT chest in stable patients when defining fracture patterns/associated injuries will alter management.\n"
     "• Blood gas in respiratory failure/significant hypoxemia.\n"
     "• CBC, electrolytes, renal function, lactate according to injury severity.\n"
     "• Continuous oxygenation monitoring and repeated respiratory assessment.\n"
     "• Evaluate for pneumothorax, hemothorax, pulmonary contusion, blunt cardiac injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Multimodal Analgesia[/color]\n"
     "• Patient-specific regimen; options may include paracetamol and carefully titrated opioid analgesia. NSAIDs may be considered when renal function/bleeding risk permit. Regional techniques may be appropriate for selected patients.\n"
     "• Reassess pain, cough effectiveness, RR, sedation, ability to mobilize. Consider epidural, paravertebral, or fascial-plane blocks per expertise/contraindications.\n"
     "• [color=#991B1B]Excessive opioid sedation can worsen hypoventilation. Regional anesthesia requires assessment of anticoagulation, hemodynamic status, procedural risks.[/color]\n\n"
     "[color=#1E3A8A]Oxygen and Ventilatory Support[/color]\n"
     "• Titrate oxygen to appropriate target; aim for adequate oxygenation while avoiding unnecessary hyperoxia. Provide positive-pressure support when indicated by respiratory distress/gas-exchange failure.\n"
     "• Monitor oxygenation, work of breathing, mental status, blood gases, fatigue. Consider NIV only in suitable, cooperative patients without contraindications and with close monitoring.\n"
     "• [color=#991B1B]Do NOT delay intubation in progressive respiratory failure, exhaustion, or inability to protect airway. Positive-pressure ventilation may worsen untreated pneumothorax; assess and treat pneumothorax promptly.[/color]"),
    ("05 — SURGICAL INDICATIONS", "warning", 
     "• Surgical stabilization of rib fractures may be considered in selected patients with flail chest, ventilator dependence, severe chest-wall deformity, or persistent respiratory compromise despite optimal treatment.\n"
     "• Chest drainage required for clinically significant pneumothorax/hemothorax when indicated.\n"
     "• Thoracic surgical intervention may be needed for associated intrathoracic injury."),
    ("06 — DISPOSITION", "warning", 
     "• Admit flail chest or significant multiple rib fractures for close monitoring.\n"
     "• ICU admission appropriate for respiratory failure, severe pulmonary contusion, or need for ventilatory support.\n"
     "• Encourage pulmonary hygiene, mobilization, effective pain control to reduce atelectasis/pneumonia risk."),
    ("REFERENCES", "info", "ATLS; EAST Guidelines on Blunt Thoracic Trauma/Rib Fractures; Chest Wall Injury Society Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Cardiac Tamponade Following Chest Trauma")] = [
    ("01 — RECOGNIZE", "info", 
     "Traumatic cardiac tamponade occurs when blood accumulates in pericardial sac and impairs cardiac filling. Common mechanisms: Penetrating chest injury; less commonly blunt cardiac trauma with myocardial/vascular rupture.\n"
     "• Suspect in trauma patients with: Hypotension, signs of obstructive shock. Tachycardia, elevated JVP, poor perfusion. Penetrating injury in cardiac box. Pericardial fluid on eFAST.\n"
     "• [color=#991B1B]Beck's triad (hypotension, raised JVP, muffled heart sounds) is often incomplete and should NOT be relied upon to exclude tamponade. Absence of pericardial fluid on limited study does NOT exclude all cardiac injury.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate trauma, cardiothoracic/trauma-surgical, anesthesia, and resuscitation teams.\n"
     "• Assess ABCs. Give oxygen and establish IV/IO access.\n"
     "• Perform immediate bedside eFAST when available/appropriate.\n"
     "• Treat associated life-threatening thoracic injuries.\n"
     "• Arrange immediate operative management for suspected traumatic tamponade with instability.\n"
     "• Use blood products when hemorrhage suspected.\n"
     "• Avoid unnecessary delays for CT/advanced imaging in unstable patient.\n"
     "• If traumatic cardiac arrest occurs, follow institution's resuscitative thoracotomy and traumatic-arrest protocol."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside eFAST for pericardial fluid.\n"
     "• ECG and continuous cardiac monitoring.\n"
     "• CBC, blood gas, lactate, coagulation, electrolytes, group-and-crossmatch.\n"
     "• Formal echocardiography in stable patients when further assessment needed.\n"
     "• CT may be appropriate for selected stable patients with suspected blunt cardiac/vascular injury.\n"
     "• [color=#991B1B]Imaging must NOT delay life-saving intervention when tamponade with shock strongly suspected.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Blood-Product Resuscitation[/color]\n"
     "• Use major hemorrhage protocol when significant traumatic bleeding suspected. Arrange emergency blood products through local trauma/transfusion protocol.\n"
     "• Monitor BP, perfusion, lactate, temperature, coagulation, calcium during major transfusion.\n"
     "• [color=#991B1B]Fluid/blood administration alone cannot definitively relieve mechanical cardiac tamponade.[/color]\n\n"
     "[color=#1E3A8A]Emergency Pericardial Decompression[/color]\n"
     "• Prepare for immediate definitive intervention by appropriately trained trauma/cardiothoracic team.\n"
     "• In traumatic tamponade with instability, operative management generally preferred (permits control of bleeding source).\n"
     "• Pericardiocentesis may be considered as temporizing measure in selected circumstances when definitive intervention not immediately available, but may fail when blood is clotted.\n"
     "• [color=#991B1B]Blind pericardiocentesis can cause serious injury and may not control source of traumatic bleeding. Do NOT delay definitive surgery in unstable patient while repeatedly attempting drainage.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Emergency thoracotomy or sternotomy may be required depending on injury mechanism, location, patient condition.\n"
     "• Evacuate pericardial blood and control cardiac/vascular bleeding source.\n"
     "• Repair myocardial injury and address associated thoracic injuries.\n"
     "• In traumatic cardiac arrest, resuscitative thoracotomy is reserved for appropriately selected patients according to mechanism, signs of life, elapsed time, local protocols."),
    ("06 — DISPOSITION", "warning", 
     "• Admit survivors to ICU or cardiothoracic surgical critical-care setting.\n"
     "• Monitor for recurrent tamponade, ongoing hemorrhage, arrhythmias, myocardial dysfunction, coagulopathy.\n"
     "• Arrange definitive cardiac/vascular evaluation based on injury pattern."),
    ("REFERENCES", "info", "ATLS; AHA Resuscitation/Traumatic Cardiac Arrest Guidance; EAST Emergency Resuscitative Thoracotomy Guidelines; ERC Special Circumstances Guidelines.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Postoperative Respiratory Deterioration")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute respiratory deterioration after surgery may result from airway obstruction, residual anesthetic effects, opioid-induced respiratory depression, atelectasis, aspiration, pneumonia, pulmonary edema, PE, pneumothorax, or sepsis.\n"
     "• Warning signs: Increasing RR/work of breathing. Falling SpO2/increasing O2 requirement. Reduced consciousness, shallow breathing, inability to protect airway. Tachycardia, hypotension, cyanosis, exhaustion.\n"
     "• Consider PE when hypoxemia/unexplained tachycardia occurs, particularly after major surgery or immobility.\n"
     "• Consider hemorrhage/intra-abdominal sepsis when respiratory deterioration accompanies hypotension or abdominal findings."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for urgent anesthesia, surgical, and critical-care assessment.\n"
     "• Assess ABCs and mental status. Open/reposition airway; suction secretions when needed.\n"
     "• Administer supplemental O2 and monitor SpO2, ECG, BP.\n"
     "• Assist ventilation with bag-mask device if breathing inadequate.\n"
     "• Check RR, pupil size, medication history, recent opioids/sedatives/neuromuscular-blocking agents.\n"
     "• Obtain blood gas when respiratory failure, hypercapnia, or severe hypoxemia suspected.\n"
     "• Examine for pneumothorax, pulmonary edema, aspiration, signs of hemorrhage/sepsis.\n"
     "• Arrange urgent definitive airway management if patient cannot protect airway or maintain adequate ventilation.\n"
     "• Treat underlying cause without delay."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside glucose and blood gas as clinically indicated.\n"
     "• CBC, electrolytes, renal function, lactate when deterioration significant.\n"
     "• Chest radiograph for suspected atelectasis, aspiration, edema, pneumonia, pneumothorax.\n"
     "• ECG and troponin when cardiac ischemia/myocardial injury suspected.\n"
     "• CTPA when PE suspected and patient stable enough.\n"
     "• Bedside ultrasound/echo when pulmonary edema, cardiac dysfunction, or obstructive shock suspected.\n"
     "• Review anesthetic records, fluid balance, medication chart, operative findings."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Oxygen and Ventilatory Support[/color]\n"
     "• Titrate oxygen to patient's condition. Usual target 94–98%; use 88–92% in patients at risk of hypercapnic respiratory failure unless individualized target indicated.\n"
     "• Select appropriate oxygen device (nasal cannula, face mask, non-rebreather). Prepare bag-mask ventilation and airway equipment when deterioration severe.\n"
     "• Monitor SpO2, respiratory effort, mental status, blood gas when indicated. Escalate to NIV/invasive ventilation according to cause and clinical response.\n"
     "• [color=#991B1B]Oxygen alone does NOT correct hypoventilation or airway obstruction. Do NOT delay intubation in patient with worsening consciousness, exhaustion, or refractory hypoxemia.[/color]\n\n"
     "[color=#1E3A8A]Naloxone for Suspected Opioid-Induced Respiratory Depression[/color]\n"
     "• In adults with opioid-induced respiratory depression, titrate IV naloxone in small doses, commonly starting at 0.04 mg and escalating every 2–3 minutes as needed. In apnea/life-threatening deterioration, use emergency protocol for rapid reversal.\n"
     "• Aim to restore adequate ventilation rather than necessarily causing complete analgesia reversal. Continue respiratory monitoring; provide ventilatory support when necessary.\n"
     "• [color=#991B1B]Naloxone may precipitate severe pain, agitation, withdrawal, sympathetic activation. Its effect may wear off before opioid; recurrent respiratory depression requires continued observation and sometimes repeat dosing or infusion.[/color]\n\n"
     "[color=#1E3A8A]Cause-Directed Treatment[/color]\n"
     "• Bronchospasm: inhaled bronchodilator per severity. Pulmonary edema: respiratory support and treatment of underlying cause. Pneumothorax: urgent decompression when tension suspected. PE: assess severity, initiate anticoagulation/reperfusion when indicated. Aspiration/pneumonia: supportive care, antibiotics when infection suspected/established. Hemorrhage/sepsis: resuscitation and urgent source control."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with persistent oxygen requirement, hypercapnia, respiratory distress, or identified serious cause.\n"
     "• ICU care for invasive ventilation, hemodynamic instability, or rapidly progressive respiratory failure.\n"
     "• Reassess frequently after treatment because postoperative deterioration can recur."),
    ("REFERENCES", "info", "ASA Practice Guidelines for Postanesthetic Care; BTS Oxygen Use Guideline; ERC ALS Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Surgical Bleeding and Hemorrhagic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Surgical bleeding may occur after trauma, abdominal/thoracic surgery, vascular procedures, or GI intervention.\n"
     "• Possible sources: Arterial/venous injury. Postoperative wound/intra-abdominal bleeding. GI hemorrhage. Retroperitoneal hemorrhage. Bleeding related to anticoagulants/coagulopathy.\n"
     "• Early signs: Tachycardia, pallor, anxiety, cool extremities, delayed capillary refill, reduced urine output.\n"
     "• [color=#991B1B]Hypotension is often a late sign; a normal initial Hb does NOT exclude major acute blood loss. Consider hemorrhagic shock when unexplained deterioration following surgery or trauma.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate major hemorrhage protocol when life-threatening bleeding suspected.\n"
     "• Call responsible surgeon, anesthesia team, blood bank, critical-care team.\n"
     "• Control external bleeding with direct pressure, wound packing, or tourniquet for life-threatening extremity bleeding when indicated.\n"
     "• Establish two large-bore IV lines or IO access if necessary.\n"
     "• Obtain CBC, blood gas, lactate, coagulation, fibrinogen, electrolytes, ionized calcium, group-and-crossmatch.\n"
     "• Begin blood-product resuscitation promptly for severe hemorrhage. Prevent hypothermia, monitor for hypocalcemia/coagulopathy.\n"
     "• Identify bleeding source using bedside assessment, imaging in stable patients, or immediate operative exploration when indicated.\n"
     "• [color=#991B1B]Do NOT delay definitive hemorrhage control while waiting for lab results.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, blood gas, lactate, electrolytes, renal function, coagulation, fibrinogen, ionized calcium. Type and crossmatch.\n"
     "• Bedside eFAST for suspected traumatic internal bleeding.\n"
     "• CT angiography in stable patients when it will help identify source/guide embolization.\n"
     "• Review anticoagulants, antiplatelet drugs, recent procedures, operative records.\n"
     "• Repeat lab tests according to ongoing blood loss and resuscitation response."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Blood-Product Resuscitation[/color]\n"
     "• Use local major hemorrhage protocol for life-threatening bleeding. Balanced component therapy/whole blood may be used per local availability/protocol. Transition to lab/viscoelastic-guided treatment when results available.\n"
     "• Activate emergency blood-bank support. Use appropriate identification/compatibility/transfusion procedures. Use blood warmer when indicated.\n"
     "• Monitor BP, perfusion, temperature, lactate, Hb, coagulation, fibrinogen, ionized calcium. Replace calcium when clinically indicated. Monitor for transfusion reactions/complications.\n"
     "• [color=#991B1B]Do NOT rely on initial Hb to exclude major acute blood loss. Avoid excessive crystalloid in uncontrolled hemorrhage.[/color]\n\n"
     "[color=#1E3A8A]Tranexamic Acid (TXA)[/color]\n"
     "• For selected adults with significant traumatic hemorrhage: 1 g IV over 10 minutes, followed by 1 g IV over 8 hours, when indicated by trauma protocol. Most beneficial when started early (generally within 3 hours of injury). Do NOT use routinely for every type of postoperative/GI bleeding without specific indication.\n"
     "• [color=#991B1B]Avoid rapid IV injection (can cause hypotension). TXA does NOT replace surgical/endovascular hemorrhage control.[/color]\n\n"
     "[color=#1E3A8A]Reversal of Anticoagulation[/color]\n"
     "• Select reversal according to anticoagulant, time of last dose, renal function, bleeding severity, local protocol. Examples: Vitamin K + 4F-PCC for life-threatening warfarin-associated bleeding; specific reversal strategies for selected DOACs.\n"
     "• [color=#991B1B]Reversal agents have thrombotic risks and should be used for appropriate indications under emergency protocols.[/color]"),
    ("05 — DEFINITIVE HEMORRHAGE CONTROL", "info", 
     "• Apply direct surgical hemostasis for accessible bleeding.\n"
     "• Perform emergency laparotomy or thoracotomy when indicated by bleeding source and patient condition.\n"
     "• Consider interventional radiology and embolization in selected stable patients.\n"
     "• Correct coagulopathy and hypothermia while controlling source."),
    ("06 — DISPOSITION", "warning", 
     "• Admit significant hemorrhage for monitored care.\n"
     "• ICU admission after major transfusion, persistent shock, emergency surgery, or organ dysfunction.\n"
     "• Reassess for rebleeding, abdominal compartment syndrome, AKI, transfusion-related complications."),
    ("REFERENCES", "info", "ATLS; European Guideline on Management of Major Bleeding/Coagulopathy Following Trauma; ASH Anticoagulant-Associated Bleeding/Reversal Guidance.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Cholangitis with Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute cholangitis is infection of biliary tree, usually associated with obstruction.\n"
     "• Common causes: CBD stones, malignant obstruction, biliary strictures, obstructed biliary stents.\n"
     "• Clinical features: Fever/chills. RUQ/epigastric pain. Jaundice. Hypotension/altered mental status in severe disease.\n"
     "• [color=#991B1B]The classic Charcot triad is not always present. Severe cholangitis may cause septic shock, AKI, coagulopathy, multiorgan dysfunction.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and signs of septic shock. Obtain IV access and continuous monitoring.\n"
     "• Send CBC, renal/liver function, bilirubin, coagulation, blood gas, lactate.\n"
     "• Obtain blood cultures before antibiotics when no delay to treatment.\n"
     "• Start broad-spectrum IV antibiotics promptly.\n"
     "• Begin appropriate fluid resuscitation and vasopressor support if required.\n"
     "• Arrange urgent biliary decompression; severe cholangitis with shock requires emergency specialist intervention.\n"
     "• Contact gastroenterology for ERCP; involve surgery/interventional radiology if ERCP unavailable/unsuccessful.\n"
     "• [color=#991B1B]Do NOT delay drainage for complete diagnostic work-up in a patient with ongoing shock and confirmed/strongly suspected obstructed cholangitis.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, LFTs, bilirubin, coagulation, lactate.\n"
     "• Blood cultures. Ultrasound for biliary dilation/gallstones.\n"
     "• MRCP or CT in selected stable patients when diagnosis/cause unclear.\n"
     "• ERCP may provide both diagnosis and definitive treatment.\n"
     "• Assess for pancreatitis, hepatic abscess, other associated complications when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Broad-Spectrum IV Antibiotics[/color]\n"
     "• Select therapy based on severity, prior biliary procedures, local resistance, allergies, renal function. One possible adult regimen for severe biliary infection: Piperacillin–tazobactam 4.5 g IV every 6–8 hours, adjusted per local guidance. Broader/alternative therapy may be needed for resistant organisms/healthcare-associated infection.\n"
     "• Review blood cultures and bile cultures after drainage. Narrow treatment when microbiology/clinical response permit.\n"
     "• [color=#991B1B]Antibiotics alone are often inadequate when an obstructed biliary system remains infected.[/color]\n\n"
     "[color=#1E3A8A]IV Crystalloid[/color]\n"
     "• Reassessed boluses according to perfusion and fluid tolerance. In sepsis-induced hypoperfusion, initial target near 30 mL/kg within 3 hours may be considered, individualized for cardiac/renal function.\n"
     "• [color=#991B1B]Avoid unmonitored fluid loading in patients developing pulmonary edema/fluid intolerance.[/color]\n\n"
     "[color=#1E3A8A]Norepinephrine for Persistent Shock[/color]\n"
     "• Start/titrate per local vasopressor protocol; typical initial range 0.05–0.1 mcg/kg/min. Common initial MAP target ~65 mmHg.\n"
     "• Monitor BP continuously/very frequently. Inspect IV site and arrange central access when appropriate.\n"
     "• [color=#991B1B]Vasopressors support circulation but do NOT replace urgent biliary drainage.[/color]"),
    ("05 — DEFINITIVE BILIARY DRAINAGE", "info", 
     "• ERCP usually preferred when available/technically feasible. Procedures may include sphincterotomy, stone extraction, biliary stent placement.\n"
     "• If ERCP unavailable/unsuccessful: consider percutaneous transhepatic biliary drainage or operative drainage according to anatomy, expertise, patient condition.\n"
     "• Definitive gallstone management should be planned after stabilization."),
    ("06 — DISPOSITION", "warning", 
     "• Severe cholangitis or septic shock generally requires ICU-level care.\n"
     "• Monitor for renal injury, coagulopathy, persistent obstruction, liver abscess, ongoing sepsis.\n"
     "• Review cultures and antibiotic duration after successful source control."),
    ("REFERENCES", "info", "Tokyo Guidelines 2018; ASGE Cholangitis Endoscopy Guideline; Surviving Sepsis Campaign.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Retained Surgical Foreign Body")] = [
    ("01 — RECOGNIZE", "info", 
     "A retained surgical item may present immediately or months to years after a procedure.\n"
     "• Possible retained materials: Sponges, instruments, needles, fragments of devices.\n"
     "• Clinical presentations: Persistent/unexplained postoperative pain. Fever, abscess, recurrent infection. Bowel obstruction, fistula, perforation. Palpable mass or persistent drainage. Unexpected radiographic findings.\n"
     "• [color=#991B1B]A retained foreign body is NOT the only explanation for postoperative symptoms; evaluate other surgical complications concurrently.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess patient stability and identify any immediate threat from sepsis, hemorrhage, obstruction, perforation.\n"
     "• Notify responsible surgical team and senior hospital leadership per institutional policy.\n"
     "• Review operative report, count documentation, implant records, procedure details.\n"
     "• Perform focused examination and obtain appropriate imaging.\n"
     "• Start resuscitation and antibiotics when infection/sepsis suspected.\n"
     "• Obtain urgent surgical review if item causing obstruction, perforation, bleeding, or uncontrolled infection.\n"
     "• Preserve relevant records and follow institutional patient-safety/disclosure policies.\n"
     "• [color=#991B1B]Avoid blind removal or instrumentation that may worsen injury.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, lactate, blood cultures when infection suspected.\n"
     "• Plain radiography for radiopaque objects or when radiographic surgical count marker present.\n"
     "• CT abdomen/pelvis for suspected retained sponge, abscess, obstruction, fistula, perforation.\n"
     "• Ultrasound may help identify superficial collections or selected foreign bodies.\n"
     "• [color=#991B1B]Imaging choice depends on material, location, suspected complication; some materials are not readily visible on plain radiographs.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics for Associated Infection[/color]\n"
     "• Choose antibiotics according to suspected infection, source, severity, renal function, allergies, local resistance. For severe intra-abdominal infection, broad-spectrum IV regimen may be required.\n"
     "• Obtain cultures when appropriate without delaying urgent treatment. Monitor hemodynamics, renal function, temperature, clinical response.\n"
     "• [color=#991B1B]Antibiotics do NOT remove the foreign body or replace drainage/definitive source control when required.[/color]\n\n"
     "[color=#1E3A8A]Abscess Drainage[/color]\n"
     "• Arrange image-guided drainage or operative drainage depending on anatomy/clinical condition. Send aspirated material for appropriate microbiology.\n"
     "• Monitor drain output, fever, inflammatory markers, clinical improvement.\n"
     "• [color=#991B1B]Avoid percutaneous drainage when it is unsafe or unlikely to control the source; obtain surgical consultation.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Remove retained item when clinically indicated, using approach appropriate to its location/associated risks.\n"
     "• Treat associated abscess, perforation, fistula, obstruction, tissue injury.\n"
     "• Emergency surgery may be necessary for peritonitis, uncontrolled sepsis, or bowel obstruction.\n"
     "• Document event and management transparently according to local law, hospital policy, patient-safety standards."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with infection, obstruction, perforation, or retained item requiring urgent intervention.\n"
     "• Arrange follow-up to confirm source control/resolution of complications.\n"
     "• Conduct structured safety review to identify contributing process failures."),
    ("REFERENCES", "info", "WHO Surgical Safety Checklist/Safe Surgery Guidance; ACS Surgical Patient Safety Statements; National Surgical Safety Policies.")
]

SURGICAL_TOPICS[("Surgical & Trauma", "Acute Abdominal Compartment Syndrome After Major Resuscitation")] = [
    ("01 — RECOGNIZE", "info", 
     "Abdominal compartment syndrome can develop after major trauma, massive fluid resuscitation, severe burns, major abdominal surgery, hemorrhage, or severe pancreatitis. Results from elevated intra-abdominal pressure causing impaired organ perfusion and dysfunction.\n"
     "• Clinical warning signs: Increasing abdominal distension/tense abdomen. Rising airway pressures/worsening oxygenation. Oliguria/AKI. Hypotension or escalating vasopressor requirements. Rising lactate/worsening metabolic acidosis.\n"
     "• [color=#991B1B]Diagnosis requires sustained intra-abdominal pressure >20 mmHg associated with new organ dysfunction or failure.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate surgical and critical-care teams urgently.\n"
     "• Assess ABCs and evidence of progressive organ failure.\n"
     "• Measure intra-abdominal pressure using standardized bladder-pressure technique.\n"
     "• Check urine output, ventilatory mechanics, blood gas, lactate, renal function, fluid balance.\n"
     "• Decompress stomach with NG tube when indicated.\n"
     "• Treat bowel obstruction, ileus, intra-abdominal bleeding, fluid collections contributing to increased pressure.\n"
     "• Avoid unnecessary additional fluid loading after adequate resuscitation.\n"
     "• [color=#991B1B]Arrange urgent decompressive laparotomy if organ dysfunction persists/worsens despite appropriate measures.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial intra-abdominal pressure measurements.\n"
     "• Blood gas, lactate, electrolytes, renal function, CBC.\n"
     "• Continuous monitoring of airway pressures, urine output, hemodynamics.\n"
     "• Bedside ultrasound or CT when patient stable enough and imaging will clarify treatable cause.\n"
     "• [color=#991B1B]Do NOT delay decompression in deteriorating patient with established ACS.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Gastric Decompression[/color]\n"
     "• Prepare correctly sized NG tube and appropriate drainage system. Confirm placement per local protocol. Monitor drainage, abdominal distension, IAP, respiratory mechanics.\n"
     "• [color=#991B1B]Decompression alone is NOT definitive treatment for persistent ACS with organ dysfunction.[/color]\n\n"
     "[color=#1E3A8A]Hemodynamic Support[/color]\n"
     "• Individualize fluid and vasopressor treatment according to perfusion, blood loss, hemodynamic response. Use standardized isotonic fluid/vasopressor preparations.\n"
     "• Monitor MAP, lactate, urine output, renal function, signs of fluid overload. Consider norepinephrine for persistent hypotension per local shock protocol.\n"
     "• [color=#991B1B]Avoid both under-resuscitation and indiscriminate fluid loading; each can worsen organ injury.[/color]"),
    ("05 — DEFINITIVE SURGICAL MANAGEMENT", "info", 
     "• Urgent decompressive laparotomy indicated when overt ACS causes persistent/worsening organ dysfunction despite appropriate initial measures.\n"
     "• Treat underlying cause (bleeding, bowel obstruction, intra-abdominal infection).\n"
     "• Temporary abdominal closure may be required.\n"
     "• Monitor for recurrent compartment syndrome, fluid/protein losses, hypothermia, infection, abdominal wound complications."),
    ("06 — DISPOSITION", "warning", 
     "• Manage confirmed ACS in ICU or equivalent high-acuity care.\n"
     "• Obtain immediate surgical review for rising IAP accompanied by respiratory, renal, or circulatory deterioration.\n"
     "• Repeat pressure measurements after interventions and whenever patient's condition changes."),
    ("REFERENCES", "info", "WSACS Consensus Definitions/Clinical Practice Guidelines; WSES ACS Guidance; Surviving Sepsis Campaign.")
]