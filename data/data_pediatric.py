# data_pediatric.py

PEDIATRIC_DATA = {
    "Pediatric Emergencies": {
        "Respiratory & Airway": [
            "Acute Asthma Exacerbation", "Bronchiolitis", 
            "Community-Acquired Pneumonia", "Acute Croup (Laryngotracheitis)", 
            "Life-Threatening Wheeze and Respiratory Failure", 
            "Foreign-Body Aspiration", "Epiglottitis and Bacterial Tracheitis",
            "Anaphylaxis"
        ],
        "Cardiovascular & Shock": [
            "Pediatric Sepsis and Septic Shock", "Pediatric Cardiac Arrest", 
            "Pediatric Shock", "Acute Rheumatic Fever and Rheumatic Carditis"
        ],
        "Neurological Emergencies": [
            "Febrile Seizure", "Pediatric Status Epilepticus", 
            "Meningitis and Encephalitis", "Pediatric Head Injury"
        ],
        "Gastrointestinal & Surgical": [
            "Acute Gastroenteritis and Dehydration", "Acute Appendicitis", 
            "Intussusception", "Foreign-Body and Caustic Ingestion"
        ],
        "Renal & Genitourinary": [
            "Urinary Tract Infection and Pyelonephritis", 
            "Acute Kidney Injury (AKI) in Children", "Pediatric Hyperkalemia",
            "Acute Scrotum and Testicular Torsion"
        ],
        "Endocrine & Metabolic": [
            "Diabetic Ketoacidosis (DKA)", "Pediatric Hypoglycemia"
        ],
        "Infectious Diseases & Fever": [
            "Febrile Infant (0-90 Days)", "Acute Otitis Media and Mastoiditis", 
            "Snakebite and Scorpion Sting", "Kawasaki Disease and MIS-C", 
            "Severe Malaria in Children"
        ],
        "Trauma, Toxins & Environmental": [
            "Acute Poisoning and Drug Overdose", "Pediatric Burns and Scalds", 
            "Pediatric Trauma and Fractures", "Drowning and Submersion Injury", 
            "Electrical Injury and Lightning Strike"
        ],
        "Hematology & Oncology": [
            "Sickle Cell Emergencies", "Severe Anemia and Acute Hemolytic Crisis"
        ],
        "Neonatal Emergencies": [
            "Neonatal Resuscitation at Birth", "Neonatal Respiratory Distress and Failure",
            "Neonatal Shock and Poor Perfusion", "Neonatal Hypothermia and Temperature Instability",
            "Neonatal Bradycardia and Cardiac Arrest", "Early-Onset and Late-Onset Neonatal Sepsis",
            "Neonatal Meningitis", "Neonatal Pneumonia", 
            "Neonatal Omphalitis and Umbilical Sepsis", "Neonatal Septic Shock",
            "Neonatal Hypoglycemia", "Neonatal Seizures", 
            "Severe Neonatal Hyperbilirubinemia", "Neonatal Apnea and Respiratory Failure",
            "Neonatal Necrotizing Enterocolitis (NEC)", "Neonatal Hypernatremic Dehydration",
            "Neonatal Pneumothorax and Tension Pneumothorax", 
            "Critical Congenital Heart Disease and Duct-Dependent Shock",
            "Neonatal Hypoxic-Ischemic Encephalopathy (HIE)", 
            "Neonatal Bilious Vomiting and Intestinal Obstruction"
        ]
    }
}
PEDIATRIC_TOPICS = {}

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Gastroenteritis and Dehydration")] = [
    ("01 — RECOGNIZE", "info", 
     "• Acute diarrhea, with or without vomiting, abdominal cramps, and fever.\n"
     "• Assess hydration using mental status, thirst, mucous membranes, tears, eyes, skin turgor, capillary refill, pulse quality, and urine output.\n"
     "• Severe dehydration or shock may present with lethargy, weak pulses, prolonged capillary refill, cool extremities, and reduced urine output.\n"
     "• Consider sepsis, surgical abdomen, DKA, and other causes if the presentation is atypical.\n"
     "• Bloody diarrhea, bilious vomiting, severe localized abdominal pain, or abdominal distension requires further assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status, and bedside glucose if the child is severely ill.\n"
     "• Determine weight, hydration status, duration of symptoms, urine output, and ability to drink.\n"
     "• Start oral rehydration solution (ORS) if the child is alert and can drink.\n"
     "• Establish IV or intraosseous access if shock is present or oral/enteral rehydration is unsafe or unsuccessful.\n"
     "• Continue breastfeeding.\n"
     "• Avoid routine antibiotics and antidiarrheal drugs."),
    ("03 — INVESTIGATIONS", "info", 
     "• No routine laboratory tests are needed in uncomplicated gastroenteritis with no significant dehydration.\n"
     "• Check glucose, electrolytes, urea, and creatinine if severe dehydration, shock, altered mental status, or IV therapy is required.\n"
     "• Blood gas and lactate may be appropriate in severe shock or suspected metabolic acidosis.\n"
     "• Stool testing is indicated selectively for bloody diarrhea, suspected outbreaks, immunocompromise, persistent symptoms, or when results will change management."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Oral rehydration therapy[/color]\n"
     "• For some dehydration, give ORS approximately 75 mL/kg over 4 hours, then reassess and replace ongoing losses.\n"
     "• Give small, frequent amounts using a spoon, cup, or oral syringe.\n"
     "• Replace ongoing watery stool losses with additional ORS.\n"
     "• Do not use plain water alone to replace substantial gastrointestinal losses.\n\n"
     "[color=#1E3A8A]IV fluid resuscitation for shock[/color]\n"
     "• If shock is present, give isotonic crystalloid, commonly 10–20 mL/kg IV, then reassess immediately.\n"
     "• Repeat only when clinically indicated and according to the pediatric shock protocol.\n"
     "• Do not automatically give repeated large boluses without reassessment.\n\n"
     "[color=#1E3A8A]Zinc supplementation[/color]\n"
     "• < 6 months: 10 mg orally once daily.\n"
     "• ≥ 6 months: 20 mg orally once daily.\n"
     "• Duration: 10–14 days.\n\n"
     "[color=#1E3A8A]Antibiotics and antiemetics[/color]\n"
     "• Antibiotics are not routinely indicated for uncomplicated watery diarrhea.\n"
     "• Ondansetron may be considered in selected children with vomiting that prevents ORS.\n"
     "• Avoid routine loperamide in children."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge only when hydration is adequate, oral intake is tolerated, and caregivers understand ORS use and warning signs.\n"
     "• Admit children with shock, severe dehydration, significant electrolyte abnormalities, altered mental status, failed rehydration, or a concerning alternative diagnosis."),
    ("REFERENCES", "info", "WHO. Pocket Book of Hospital Care for Children; WHO. Diarrhoeal disease.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Asthma Exacerbation")] = [
    ("01 — RECOGNIZE", "info", 
     "• Wheezing, cough, breathlessness, chest tightness, and prolonged expiration.\n"
     "• Assess speech, feeding, respiratory rate, accessory muscle use, air entry, oxygen saturation, and mental status.\n"
     "• Severe signs include marked work of breathing, inability to speak or feed normally, exhaustion, cyanosis, or poor air entry.\n"
     "• A silent chest, altered consciousness, or respiratory exhaustion indicates impending respiratory failure.\n"
     "• Consider anaphylaxis, foreign-body aspiration, bronchiolitis, pneumonia, and other causes of wheeze."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and oxygen saturation.\n"
     "• Position the child comfortably and minimize distress.\n"
     "• Give inhaled salbutamol promptly.\n"
     "• Add ipratropium for moderate-to-severe exacerbations according to the local protocol.\n"
     "• Give systemic corticosteroids early for moderate-to-severe attacks.\n"
     "• Escalate immediately for poor air entry, exhaustion, altered mental status, or inadequate response."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Salbutamol (albuterol)[/color]\n"
     "• MDI with spacer: 4–10 puffs (100 mcg/puff), one puff at a time, repeated every 20 minutes during the first hour.\n"
     "• Nebulized: 2.5 mg (smaller children) or 5 mg (larger children), repeated according to protocol.\n\n"
     "[color=#1E3A8A]Ipratropium bromide[/color]\n"
     "• Nebulized: 250 mcg (smaller children) or 500 mcg (larger children), repeated during initial treatment.\n\n"
     "[color=#1E3A8A]Systemic corticosteroid[/color]\n"
     "• Prednisolone orally: 1–2 mg/kg once daily (max local dose) for 3–5 days.\n\n"
     "[color=#1E3A8A]Magnesium sulfate (severe refractory)[/color]\n"
     "• IV: 25–50 mg/kg (max 2 g) over ~20 minutes."),
    ("04 — WARNINGS", "danger", 
     "• Excessive beta-agonist exposure may cause tachycardia, tremor, hypokalemia, and lactic acidosis.\n"
     "• Deterioration or poor air entry despite treatment requires urgent escalation.\n"
     "• Steroids do not provide immediate bronchodilation; continue inhaled bronchodilator treatment as indicated.\n"
     "• Rapid IV magnesium administration can cause hypotension."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge only after sustained clinical improvement, stable oxygenation, and an appropriate home treatment and follow-up plan.\n"
     "• Admit for persistent distress, frequent bronchodilator requirement, hypoxemia, or significant risk factors.\n"
     "• ICU referral is indicated for impending respiratory failure."),
    ("REFERENCES", "info", "WHO; Children's Acute Transport Service (CATS).")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Bronchiolitis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Usually affects infants under 2 years, especially those under 12 months.\n"
     "• Coryza followed by cough, tachypnea, crackles, wheeze, and increased work of breathing.\n"
     "• Feeding difficulty, dehydration, apnea, or hypoxemia may occur.\n"
     "• Severe disease is more likely in very young infants, premature infants, and children with significant cardiopulmonary disease or immunodeficiency."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, respiratory effort, oxygen saturation, feeding, hydration, and apnea history.\n"
     "• Clear nasal secretions gently when they interfere with breathing or feeding.\n"
     "• Provide oxygen for persistent hypoxemia according to age and local guideline thresholds.\n"
     "• Support feeding with small frequent feeds if safe.\n"
     "• Use nasogastric or IV fluids if oral intake is inadequate.\n"
     "• Escalate urgently for apnea, exhaustion, severe respiratory distress, or altered consciousness."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Oxygen therapy[/color]\n"
     "• Give supplemental oxygen for persistent hypoxemia according to local policy.\n"
     "• Do not use oxygen saturation alone to determine severity; work of breathing, apnea, and feeding are also important.\n\n"
     "[color=#1E3A8A]Hydration and feeding[/color]\n"
     "• Continue breastfeeding and age-appropriate feeds when safe.\n"
     "• If oral intake is inadequate, use nasogastric or IV fluids.\n"
     "• Avoid forcing oral feeds in a child with significant respiratory distress.\n\n"
     "[color=#1E3A8A]Nasal secretion management[/color]\n"
     "• Use gentle superficial nasal suction when secretions impair breathing or feeding.\n"
     "• Avoid routine deep suctioning because it can cause trauma.\n\n"
     "[color=#1E3A8A]Treatments generally NOT recommended routinely[/color]\n"
     "• Salbutamol, corticosteroids, antibiotics (unless bacterial infection suspected), nebulized adrenaline, or chest physiotherapy."),
    ("04 — DISPOSITION", "warning", 
     "• Discharge when breathing is stable, oxygenation meets local criteria, feeding and hydration are adequate, and caregivers understand warning signs.\n"
     "• Admit for apnea, persistent hypoxemia, significant respiratory distress, dehydration, or inability to feed."),
    ("REFERENCES", "info", "WHO; NICE. Bronchiolitis in children.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Community-Acquired Pneumonia")] = [
    ("01 — RECOGNIZE", "info", 
     "• Fever, cough, tachypnea, chest indrawing, crackles, or reduced air entry.\n"
     "• Hypoxemia, grunting, cyanosis, inability to drink, lethargy, or exhaustion suggest severe disease.\n"
     "• Consider viral pneumonia, bacterial pneumonia, aspiration, pleural effusion, and tuberculosis where relevant.\n"
     "• Infants may present with poor feeding, apnea, temperature instability, or nonspecific deterioration."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, oxygen saturation, respiratory rate, work of breathing, hydration, and mental status.\n"
     "• Give oxygen for hypoxemia according to the local protocol.\n"
     "• Check bedside glucose in severely ill infants.\n"
     "• Obtain IV access if shock, severe dehydration, or inability to tolerate oral treatment.\n"
     "• If sepsis is suspected, obtain cultures when feasible and start appropriate antibiotics promptly."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotic treatment[/color]\n"
     "• Uncomplicated outpatient: Oral amoxicillin 40–45 mg/kg per dose every 12 hours (subject to local guideline).\n"
     "• Severe pneumonia requiring admission: IV ampicillin, benzylpenicillin, or ceftriaxone according to severity and local guidance.\n"
     "• Do not give antibiotics routinely for clearly viral illness.\n\n"
     "[color=#1E3A8A]Fever and pain control[/color]\n"
     "• Paracetamol 10–15 mg/kg orally every 4–6 hours (within local max).\n"
     "• Ibuprofen may be considered in age-eligible, adequately hydrated children."),
    ("04 — WARNINGS", "danger", 
     "• Persistent hypoxemia, exhaustion, apnea, or altered consciousness requires urgent escalation.\n"
     "• Neonates and young infants require age-specific sepsis/pneumonia protocols.\n"
     "• Suspected empyema or necrotizing pneumonia requires specialist review."),
    ("05 — DISPOSITION", "warning", 
     "• Outpatient care may be appropriate when the child is clinically stable and caregivers can provide safe follow-up.\n"
     "• Admit for hypoxemia, severe respiratory distress, dehydration, or complications."),
    ("REFERENCES", "info", "WHO; NICE. Pneumonia: diagnosis and management.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Febrile Seizure")] = [
    ("01 — RECOGNIZE", "info", 
     "• Usually occurs in children aged 6 months to 5 years with fever and no evidence of CNS infection.\n"
     "• Simple: generalized, lasts < 15 minutes, occurs only once in 24 hours.\n"
     "• Complex features: focal onset, duration ≥ 15 minutes, or recurrence within 24 hours.\n"
     "• A seizure lasting 5 minutes or longer should be treated as an emergency.\n"
     "• Consider meningitis, encephalitis, hypoglycemia, electrolyte disturbance, poisoning, and epilepsy."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Protect the child from injury and place in a safe lateral position.\n"
     "• Do not restrain the child or place objects in the mouth.\n"
     "• Assess ABCs, oxygen saturation, and bedside glucose.\n"
     "• If the seizure continues for 5 minutes or longer, administer a first-line benzodiazepine.\n"
     "• Obtain urgent senior pediatric assessment for prolonged seizures, focal features, or persistent altered consciousness."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]First-line for ongoing seizure[/color]\n"
     "• IV lorazepam: 0.1 mg/kg IV (max 4 mg per dose); may repeat once if seizure continues.\n"
     "• If IV access unavailable: buccal/intranasal midazolam or rectal diazepam using validated protocol.\n\n"
     "[color=#1E3A8A]Hypoglycemia treatment[/color]\n"
     "• If hypoglycemia is confirmed/suspected: IV dextrose (e.g., 10% dextrose 2.5 mL/kg IV), followed by reassessment.\n\n"
     "[color=#1E3A8A]Treat the underlying cause of fever[/color]\n"
     "• Use paracetamol for discomfort (not to prevent febrile seizure recurrence).\n"
     "• Routine long-term antiepileptic medication is NOT recommended after a typical simple febrile seizure."),
    ("04 — WARNINGS", "danger", 
     "• Repeated benzodiazepine doses increase the risk of respiratory depression.\n"
     "• Do not delay treatment of an ongoing prolonged seizure while attempting difficult IV access."),
    ("05 — DISPOSITION", "warning", 
     "• A child with a simple febrile seizure may be discharged after full recovery and assessment of the fever source.\n"
     "• Admit or obtain specialist review for complex seizures, prolonged postictal state, or suspected CNS infection.\n"
     "• Explain seizure first aid and provide clear return precautions."),
    ("REFERENCES", "info", "WHO ETAT; Children's Acute Transport Service (CATS).")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Croup (Laryngotracheitis)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Usually affects children aged 6 months to 6 years.\n"
     "• Barking cough, hoarseness, inspiratory stridor, symptoms often worse at night.\n"
     "• Assess stridor at rest, chest retractions, air entry, oxygen saturation, agitation, and mental status.\n"
     "• Severe features: marked retractions, persistent stridor at rest, reduced air entry, exhaustion, cyanosis.\n"
     "• Consider epiglottitis, bacterial tracheitis, foreign-body aspiration, and anaphylaxis if atypical or toxic."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Keep the child calm with a caregiver; minimize distress and unnecessary examination.\n"
     "• Assess airway, breathing, oxygen saturation, and mental status.\n"
     "• Give dexamethasone for symptomatic croup.\n"
     "• Give nebulized epinephrine for moderate-to-severe croup.\n"
     "• Call an experienced airway clinician early if severe obstruction is suspected.\n"
     "• If respiratory failure is imminent, move to a resuscitation area and prepare for controlled airway management."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Dexamethasone[/color]\n"
     "• 0.15–0.6 mg/kg orally as a single dose (max local limit). Many protocols use 0.6 mg/kg for severe croup.\n"
     "• IM/IV administration may be used when oral route is not feasible.\n\n"
     "[color=#1E3A8A]Nebulized epinephrine (adrenaline)[/color]\n"
     "• Epinephrine 1 mg/mL: 0.5 mL/kg by nebulization (max 5 mL).\n"
     "• OR Racemic epinephrine 2.25%: 0.5 mL nebulized, diluted with normal saline according to protocol.\n"
     "• Observe for at least 2–3 hours after the last dose because symptoms may recur."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay nebulized epinephrine or airway support in severe obstruction while waiting for the corticosteroid effect.\n"
     "• Never administer the nebulized croup dose by IV or IM injection.\n"
     "• A child with decreasing stridor but worsening air entry or consciousness may be deteriorating."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge only when there is no stridor at rest, minimal work of breathing, adequate oral intake, and no recurrence during observation.\n"
     "• Admit for recurrent symptoms after epinephrine, persistent stridor at rest, oxygen requirement, or poor access to emergency care."),
    ("REFERENCES", "info", "Canadian Paediatric Society; Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Anaphylaxis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden onset of illness with airway, breathing, or circulation compromise, usually after exposure to a potential allergen.\n"
     "• Findings may include urticaria, angioedema, wheeze, stridor, vomiting, abdominal pain, hypotension, collapse, or altered consciousness.\n"
     "• Skin signs may be absent in severe anaphylaxis.\n"
     "• Do not wait for a rash or laboratory confirmation when anaphylaxis is clinically suspected."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for emergency assistance and assess ABCs.\n"
     "• Give IM epinephrine immediately into the mid-anterolateral thigh.\n"
     "• Lay the child flat with legs elevated when tolerated; allow position of comfort if severe respiratory distress. Do not allow standing or walking suddenly.\n"
     "• Give high-flow oxygen for significant respiratory or circulatory compromise.\n"
     "• Repeat IM epinephrine after 5 minutes if problems persist."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IM epinephrine (First-line)[/color]\n"
     "• 0.01 mg/kg IM (1 mg/mL solution). Max single dose usually 0.3 mg (smaller children) to 0.5 mg (adolescents).\n"
     "• Repeat every 5 minutes if needed.\n\n"
     "[color=#1E3A8A]Oxygen and IV crystalloid[/color]\n"
     "• Give oxygen for compromise.\n"
     "• For shock: isotonic crystalloid 10–20 mL/kg IV/IO, then reassess.\n\n"
     "[color=#1E3A8A]Refractory anaphylaxis[/color]\n"
     "• Titrated IV epinephrine infusion under pediatric resuscitation protocol and experienced supervision.\n\n"
     "[color=#1E3A8A]Adjuncts[/color]\n"
     "• H1 antihistamine for skin symptoms after stabilization.\n"
     "• Inhaled bronchodilator for persistent wheeze after epinephrine."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay epinephrine while giving antihistamines, corticosteroids, or IV fluids.\n"
     "• Do not give IV epinephrine boluses for routine anaphylaxis; infusion is reserved for refractory cases.\n"
     "• Corticosteroids are not first-line treatment and have no established immediate lifesaving effect."),
    ("05 — DISPOSITION", "warning", 
     "• Observe after stabilization according to severity and risk of biphasic reaction.\n"
     "• Prolonged observation or admission is appropriate after severe reactions, repeated epinephrine, or hypotension.\n"
     "• Arrange an epinephrine auto-injector, caregiver education, and allergy specialist follow-up."),
    ("REFERENCES", "info", "World Allergy Organization; Resuscitation Council UK.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Sepsis and Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "• Suspect in a child with possible infection and acute organ dysfunction.\n"
     "• Early findings: tachycardia, tachypnea, fever/hypothermia, altered behavior, poor feeding, reduced urine output, delayed capillary refill.\n"
     "• Shock may present with weak pulses, cool/mottled extremities, altered consciousness, or hypotension (late sign)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and activate the pediatric sepsis pathway.\n"
     "• Give oxygen and support ventilation as needed.\n"
     "• Check bedside glucose and obtain IV/IO access.\n"
     "• Obtain blood cultures if this does not meaningfully delay antibiotics.\n"
     "• Give prompt IV antibiotics for suspected septic shock (ideally within 1 hour).\n"
     "• Assess perfusion and decide on fluid boluses."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IV fluid resuscitation[/color]\n"
     "• In a setting with ICU capability: isotonic crystalloid 10–20 mL/kg IV/IO over a short period, then reassess.\n"
     "• Further boluses up to 40–60 mL/kg in the first hour in selected children.\n"
     "• In settings without ICU capability: use a more conservative protocol.\n\n"
     "[color=#1E3A8A]Empiric IV antibiotics[/color]\n"
     "• Ceftriaxone 50–75 mg/kg IV every 24 hours (for many children beyond neonatal period) under local guidance.\n"
     "• Neonates require a dedicated neonatal sepsis regimen.\n\n"
     "[color=#1E3A8A]Vasoactive support[/color]\n"
     "• If shock persists despite initial treatment: start epinephrine or norepinephrine infusion under critical-care guidance."),
    ("04 — WARNINGS", "danger", 
     "• Do not automatically administer maximum fluid volume to every child.\n"
     "• Children with myocarditis, severe anemia, or signs of fluid overload require modified management.\n"
     "• Avoid delaying antibiotics for imaging or difficult sampling in a deteriorating child."),
    ("05 — DISPOSITION", "warning", 
     "• Suspected septic shock requires immediate resuscitation and admission to a high-acuity setting.\n"
     "• ICU referral is indicated for persistent shock, respiratory failure, or need for vasoactive support."),
    ("REFERENCES", "info", "Surviving Sepsis Campaign; WHO.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Febrile Infant (0-90 Days)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Fever in a young infant may be the only sign of a serious bacterial infection.\n"
     "• A documented temperature ≥ 38.0°C in an infant < 3 months requires urgent clinical assessment.\n"
     "• Look for poor feeding, lethargy, irritability, apnea, temperature instability, respiratory distress.\n"
     "• Serious causes include bacteremia, UTI, meningitis, and neonatal sepsis.\n"
     "• A well appearance does not exclude serious bacterial infection, especially in neonates."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temperature, heart rate, respiratory rate, perfusion, feeding, and mental status.\n"
     "• Check bedside glucose if unwell.\n"
     "• Obtain weight and establish IV access if unwell.\n"
     "• Obtain urine testing and cultures using an appropriate collection method.\n"
     "• Give prompt empiric parenteral antibiotics when indicated; do not delay in an unstable infant."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Stabilization[/color]\n"
     "• Treat hypoglycemia using the neonatal/young-infant glucose protocol.\n"
     "• If shock is present: carefully reassessed isotonic crystalloid boluses (commonly 10 mL/kg initially).\n\n"
     "[color=#1E3A8A]Empiric parenteral antibiotics[/color]\n"
     "• Select regimen by exact age, gestational age, clinical appearance, and local protocol.\n"
     "• Neonatal regimens commonly use ampicillin + gentamicin for selected presentations.\n"
     "• Ceftriaxone has important restrictions in neonates (hyperbilirubinemia/calcium interactions).\n\n"
     "[color=#1E3A8A]Lumbar puncture[/color]\n"
     "• Perform when indicated and safe. If unstable, stabilize and begin antibiotics before LP."),
    ("04 — WARNINGS", "danger", 
     "• Young infants can deteriorate rapidly and may not show typical signs of infection.\n"
     "• Avoid routine large-volume boluses without reassessment.\n"
     "• Do not delay antibiotics in an unstable infant while attempting lumbar puncture."),
    ("05 — DISPOSITION", "warning", 
     "• Neonates with fever generally require hospital admission and a neonatal sepsis evaluation.\n"
     "• Infants aged 29–90 days require risk stratification under a validated local pathway."),
    ("REFERENCES", "info", "NICE. Fever in under 5s; AAP.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Life-Threatening Wheeze and Respiratory Failure")] = [
    ("01 — RECOGNIZE", "info", 
     "• Severe wheezing or respiratory distress with marked retractions, poor air entry, inability to speak or feed, cyanosis, exhaustion, or altered consciousness.\n"
     "• A silent chest or decreasing respiratory effort in a distressed child may indicate impending respiratory arrest.\n"
     "• Normal or rising carbon dioxide in a previously hyperventilating child may indicate fatigue and ventilatory failure.\n"
     "• Do not assume all wheezing is asthma, particularly during a first episode."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Move the child to a resuscitation area and call senior pediatric and airway support.\n"
     "• Assess ABCs, oxygen saturation, mental status, and air entry.\n"
     "• Give oxygen for hypoxemia and initiate inhaled bronchodilator therapy if bronchospasm is likely.\n"
     "• If anaphylaxis is suspected, give IM epinephrine immediately rather than treating with bronchodilators alone.\n"
     "• Prepare bag-mask ventilation and advanced airway equipment if exhaustion develops."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Inhaled salbutamol[/color]\n"
     "• MDI with spacer: 4–10 puffs, repeated every 20 minutes.\n"
     "• Nebulized: 2.5 mg (smaller children) or 5 mg (larger children).\n\n"
     "[color=#1E3A8A]Ipratropium bromide[/color]\n"
     "• 250 mcg (smaller) or 500 mcg (larger), repeated according to protocol.\n\n"
     "[color=#1E3A8A]Systemic corticosteroid[/color]\n"
     "• Prednisolone 1–2 mg/kg once daily or IV equivalent.\n\n"
     "[color=#1E3A8A]IV magnesium sulfate[/color]\n"
     "• 25–50 mg/kg IV (max 2 g) over 20 minutes for severe refractory asthma.\n\n"
     "[color=#1E3A8A]Respiratory support[/color]\n"
     "• Bag-mask ventilation if inadequate ventilation. Intubation by experienced clinician when indicated."),
    ("04 — WARNINGS", "danger", 
     "• A silent chest, worsening exhaustion, or altered consciousness is not an indication to simply continue repeated nebulization without escalation.\n"
     "• Rapid IV magnesium infusion can cause hypotension.\n"
     "• Positive-pressure ventilation and intubation in severe asthma carry risks (air trapping/hypotension); use experienced support."),
    ("05 — DISPOSITION", "warning", 
     "• All children with impending respiratory failure require emergency admission and pediatric critical-care assessment.\n"
     "• Admit severe attacks requiring frequent bronchodilators, oxygen, IV magnesium, or ongoing respiratory support."),
    ("REFERENCES", "info", "GINA; Royal Children's Hospital Melbourne; CATS.")
]


# ==================== BATCH 3 & 4 (TOPICS 11-20) ====================

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Foreign-Body Aspiration")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden coughing, choking, gagging, or respiratory distress during eating or play.\n"
     "• Persistent cough, unilateral wheeze, asymmetric air entry, or unexplained respiratory symptoms.\n"
     "• Complete obstruction may cause inability to cry, speak, cough effectively, or breathe.\n"
     "• Cyanosis, reduced consciousness, and collapse are late signs.\n"
     "• A normal chest X-ray does not exclude aspiration."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway patency, breathing, circulation, mental status, and SpO2.\n"
     "• If effective cough, encourage coughing and observe closely. Do not perform blind finger sweeps.\n"
     "• Infants < 1 year (severe obstruction): 5 back blows followed by 5 chest thrusts.\n"
     "• Children > 1 year (severe obstruction): Abdominal thrusts per age-appropriate algorithm.\n"
     "• If unresponsive, begin pediatric CPR. Remove object only if clearly visible and safe.\n"
     "• Arrange urgent airway specialist assessment if aspiration is suspected, even if symptoms improve."),
    ("03 — TREATMENT", "info", 
     "• Follow the age-specific pediatric basic life support choking algorithm.\n"
     "• Do not use abdominal thrusts in infants < 1 year.\n"
     "• Keep the child under observation and obtain urgent pediatric, ENT, or respiratory specialist review.\n"
     "• Rigid bronchoscopy is commonly used for removal of airway foreign bodies by an experienced team.\n"
     "• Provide oxygen and respiratory support. Do not delay airway management for imaging in an unstable child."),
    ("04 — WARNINGS", "danger", 
     "• Persistent cough or unilateral wheeze after a choking event requires further evaluation, even if the child appears well.\n"
     "• Do not discharge a child with significant suspicion of a retained foreign body without a specialist plan.\n"
     "• Deterioration requires immediate airway support and emergency escalation."),
    ("05 — DISPOSITION", "warning", 
     "• Admit or transfer urgently for suspected retained airway foreign body, ongoing symptoms, hypoxemia, or distress.\n"
     "• Discharge only when a retained foreign body is considered unlikely and appropriate follow-up is arranged."),
    ("REFERENCES", "info", "Resuscitation Council UK; Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Urinary Tract Infection and Pyelonephritis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Infants: fever, poor feeding, vomiting, irritability, lethargy.\n"
     "• Older children: dysuria, frequency, urgency, new incontinence, suprapubic pain, hematuria.\n"
     "• Fever with flank pain or systemic illness suggests upper UTI or pyelonephritis.\n"
     "• Consider sepsis in an unwell child, especially infants."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temperature, perfusion, hydration, urine output, and mental status.\n"
     "• Obtain a properly collected urine sample for urinalysis and culture before antibiotics when feasible.\n"
     "• Do not delay antibiotics in a septic or unstable child while attempting urine collection.\n"
     "• Establish IV access and initiate sepsis management if shock is suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis: leukocyte esterase, nitrites, and microscopy.\n"
     "• Urine culture before treatment. Avoid relying on bag specimens to confirm UTI (contamination).\n"
     "• CBC, renal function, electrolytes, blood culture, and inflammatory markers if systemically ill.\n"
     "• Renal/bladder ultrasound in selected children (age < 6 months, atypical, recurrent)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Oral antibiotics (Stable children)[/color]\n"
     "• Cephalexin 25 mg/kg per dose orally every 8 hours (subject to local max).\n"
     "• For febrile UTI/pyelonephritis: choose an agent with appropriate renal tissue penetration.\n\n"
     "[color=#1E3A8A]IV antibiotics (Severe illness)[/color]\n"
     "• Ceftriaxone 50 mg/kg IV every 24 hours (for children beyond neonatal period) per local guidance.\n"
     "• Neonates require a separate neonatal infection regimen.\n"
     "• Switch to oral therapy when improving and tolerating oral meds.\n\n"
     "[color=#1E3A8A]Supportive care[/color]\n"
     "• Encourage oral fluids. Paracetamol 10–15 mg/kg orally every 4–6 hours as needed."),
    ("05 — WARNINGS", "danger", 
     "• Infants < 3 months with suspected UTI and fever require urgent hospital assessment.\n"
     "• Suspected urosepsis requires prompt resuscitation and empiric antibiotics.\n"
     "• Persistent fever or failure to improve may indicate obstruction, renal abscess, or resistance."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for young infants, sepsis, dehydration, persistent vomiting, or suspected obstruction.\n"
     "• Outpatient care may be suitable for a stable child who tolerates oral therapy with reliable follow-up."),
    ("REFERENCES", "info", "NICE. Urinary tract infection in under 16s.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Otitis Media and Mastoiditis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Acute otitis media: ear pain, fever, irritability, bulging tympanic membrane.\n"
     "• Mastoiditis: postauricular pain, erythema, swelling, tenderness, or outward displacement of the pinna.\n"
     "• Severe headache, neck stiffness, facial weakness, vertigo, or altered mental status raises concern for complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess temperature, hydration, pain severity, and signs of systemic illness.\n"
     "• Examine both ears and the mastoid region. Perform neurological exam if complications suspected.\n"
     "• Provide appropriate analgesia early.\n"
     "• If mastoiditis or an intracranial complication is suspected, arrange urgent hospital assessment and ENT review.\n"
     "• Do not delay emergency referral for imaging in an unstable child."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Pain and fever control[/color]\n"
     "• Paracetamol 10–15 mg/kg orally every 4–6 hours as needed.\n"
     "• Ibuprofen may be used in age-eligible, adequately hydrated children.\n\n"
     "[color=#1E3A8A]Antibiotics for acute otitis media[/color]\n"
     "• Many uncomplicated cases can be managed with observation/delayed prescription.\n"
     "• When indicated: Amoxicillin 80–90 mg/kg/day orally divided into 2 doses (subject to local max).\n\n"
     "[color=#1E3A8A]Suspected mastoiditis[/color]\n"
     "• Admit urgently and start IV antibiotics according to local ENT guidance.\n"
     "• Urgent ENT consultation; drainage or mastoid surgery may be required."),
    ("04 — WARNINGS", "danger", 
     "• Postauricular swelling or erythema with displacement of the pinna is a red flag for mastoiditis.\n"
     "• Facial palsy, severe headache, meningism, persistent vomiting, or altered consciousness requires emergency escalation.\n"
     "• Reassess children who worsen or fail to improve within 48–72 hours."),
    ("05 — DISPOSITION", "warning", 
     "• Uncomplicated cases may be treated as outpatients with pain control and safety-net advice.\n"
     "• Admit urgently for suspected mastoiditis, intracranial complications, or severe systemic illness."),
    ("REFERENCES", "info", "NICE. Otitis media (acute); Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Status Epilepticus")] = [
    ("01 — RECOGNIZE", "info", 
     "• A convulsive seizure lasting ≥ 5 minutes, or recurrent seizures without recovery of consciousness.\n"
     "• Assess airway, respiratory effort, SpO2, circulation, temperature, and consciousness.\n"
     "• Consider hypoglycemia, electrolyte disturbance, CNS infection, trauma, poisoning, and epilepsy."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for help and start the pediatric resuscitation pathway.\n"
     "• Protect from injury; do not restrain or place objects in the mouth.\n"
     "• Position safely, provide oxygen, prepare suction and bag-mask ventilation.\n"
     "• Check bedside glucose immediately and treat hypoglycemia if present.\n"
     "• Give a benzodiazepine promptly for an ongoing seizure ≥ 5 minutes.\n"
     "• Avoid giving > 2 appropriately timed benzodiazepine doses in total before escalation to second-line treatment."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]First-line: IV lorazepam[/color]\n"
     "• 0.1 mg/kg IV per dose; maximum 4 mg per dose. May repeat once.\n"
     "• If no IV access: buccal/intranasal midazolam or rectal diazepam (weight-based).\n\n"
     "[color=#1E3A8A]Second-line antiseizure treatment[/color]\n"
     "• If seizures persist: Levetiracetam 40–60 mg/kg IV (max 4.5 g).\n"
     "• Alternatives: Fosphenytoin/phenytoin or valproate (selected per contraindications).\n\n"
     "[color=#1E3A8A]Refractory status epilepticus[/color]\n"
     "• Call pediatric critical care and neurology. May require anesthetic infusions and airway control.\n\n"
     "[color=#1E3A8A]Treat underlying cause[/color]\n"
     "• IV dextrose for hypoglycemia. Correct electrolyte abnormalities. Treat CNS infection."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay first-line treatment for IV access; use an appropriate non-IV route.\n"
     "• Repeated benzodiazepine doses increase the risk of respiratory depression.\n"
     "• Phenytoin/fosphenytoin can cause hypotension and arrhythmias.\n"
     "• Persistent altered consciousness after apparent seizure cessation requires urgent reassessment."),
    ("05 — DISPOSITION", "warning", 
     "• Ongoing status epilepticus requires resuscitation-level care and urgent critical-care involvement.\n"
     "• Admit children with prolonged seizures, recurrent seizures, or respiratory compromise."),
    ("REFERENCES", "info", "American Epilepsy Society; Local pediatric protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Meningitis and Encephalitis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Fever, severe headache, neck stiffness, photophobia, vomiting, or altered mental status.\n"
     "• Infants: poor feeding, irritability, lethargy, temperature instability, apnea, bulging fontanelle.\n"
     "• Seizures, focal deficits, or behavioral change raise concern for encephalitis or complicated CNS infection.\n"
     "• A non-blanching rash with fever may indicate meningococcal disease (emergency).\n"
     "• Absence of neck stiffness does not exclude meningitis, especially in infants."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, mental status, temperature, and bedside glucose.\n"
     "• Activate sepsis pathway if shock is suspected.\n"
     "• Start empiric IV antibiotics urgently when bacterial meningitis is suspected.\n"
     "• Do not wait for imaging or lumbar puncture in an unstable child.\n"
     "• Use infection-control precautions if meningococcal disease is suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• Blood cultures, CBC, inflammatory markers, glucose, electrolytes, renal function.\n"
     "• Lumbar puncture (LP) for CSF studies when clinically safe. Check serum glucose near time of LP.\n"
     "• Do not routinely delay LP for CT; imaging is reserved for focal signs, reduced consciousness, or suspected mass effect.\n"
     "• Consider MRI, EEG, and pathogen-specific testing if encephalitis is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV antibiotics (Bacterial meningitis)[/color]\n"
     "• Selection/dosing depend on age and local resistance.\n"
     "• Often Ceftriaxone + Vancomycin for children beyond neonatal period (if resistant pneumococcus is a concern).\n"
     "• Neonates require a dedicated neonatal regimen.\n\n"
     "[color=#1E3A8A]Possible encephalitis[/color]\n"
     "• Start IV acyclovir promptly when HSV encephalitis is suspected. Adjust for renal function.\n\n"
     "[color=#1E3A8A]Supportive management[/color]\n"
     "• Support airway, ventilation, perfusion, and glucose. Treat seizures promptly."),
    ("05 — WARNINGS", "danger", 
     "• Suspected bacterial meningitis is a time-critical emergency; do not delay antibiotics for CT or LP.\n"
     "• Do not perform LP in an unstable child or when signs suggest significant risk.\n"
     "• Ceftriaxone has important restrictions in neonates (hyperbilirubinemia/calcium).\n"
     "• A normal early examination or absence of rash does not reliably exclude serious CNS infection."),
    ("06 — DISPOSITION", "warning", 
     "• Admit all children with suspected bacterial meningitis or encephalitis for urgent inpatient treatment.\n"
     "• Obtain critical-care support for shock, airway compromise, or markedly reduced consciousness."),
    ("REFERENCES", "info", "NICE. Meningitis (bacterial) and meningococcal disease; WHO.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Appendicitis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Abdominal pain migrating to the right lower quadrant. Anorexia, nausea, vomiting, fever.\n"
     "• Right lower quadrant tenderness, guarding, rebound tenderness.\n"
     "• Younger children may have nonspecific symptoms, diffuse pain, or delayed presentation.\n"
     "• Perforation may present with generalized tenderness, rigidity, or shock."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, hydration, pain severity.\n"
     "• Keep the child nil by mouth when strongly suspected.\n"
     "• Establish IV access if dehydrated, systemically unwell, or likely to require surgery.\n"
     "• Provide appropriate analgesia and antiemetic treatment.\n"
     "• Request early pediatric surgical assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC and inflammatory markers (cannot independently exclude appendicitis).\n"
     "• Urinalysis (to rule out urinary causes).\n"
     "• Abdominal ultrasound is generally the preferred initial imaging in children.\n"
     "• MRI or CT may be considered if ultrasound is inconclusive.\n"
     "• Imaging must not delay urgent surgical assessment in a child with peritonitis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 10–15 mg/kg orally/IV. IV opioid for severe pain using pediatric weight-based protocol.\n"
     "• Adequate analgesia should not be withheld because appendicitis is suspected.\n\n"
     "[color=#1E3A8A]IV fluid therapy[/color]\n"
     "• If hypovolemic/shock: isotonic crystalloid 10–20 mL/kg IV, followed by reassessment.\n\n"
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• For suspected complicated appendicitis/perforation: IV antibiotics covering enteric gram-negatives and anaerobes per local guidance."),
    ("05 — WARNINGS", "danger", 
     "• Severe or increasing pain, generalized guarding, or signs of shock require immediate surgical reassessment.\n"
     "• Antibiotics do not replace urgent surgical assessment when source control is required."),
    ("06 — DISPOSITION", "warning", 
     "• Refer urgently to pediatric surgery.\n"
     "• Admit for confirmed appendicitis, peritonitis, perforation, or systemic illness."),
    ("REFERENCES", "info", "IDSA 2024 Guidelines; Local pediatric surgical guidelines.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Intussusception")] = [
    ("01 — RECOGNIZE", "info", 
     "• Most common in infants/young children (3 months to 2 years).\n"
     "• Intermittent episodes of severe colicky abdominal pain/distress, often with pallor.\n"
     "• Vomiting, poor feeding, or unexplained lethargy may be the main presentation.\n"
     "• Child may appear well between painful episodes. Sausage-shaped mass occasionally palpable.\n"
     "• Bloody/mucus-containing stool (red currant jelly) is a late sign.\n"
     "• Classic triad (pain, mass, bloody stool) is often absent."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, hydration, abdominal tenderness, mental status.\n"
     "• Establish IV access, keep the child nil by mouth.\n"
     "• Provide appropriate analgesia and antiemetic treatment.\n"
     "• If shock: pediatric resuscitation with isotonic crystalloid boluses.\n"
     "• Request urgent pediatric surgical and radiology consultation."),
    ("03 — INVESTIGATIONS", "info", 
     "• Abdominal ultrasound is the preferred initial investigation (target/doughnut sign).\n"
     "• A normal X-ray does not exclude intussusception. X-ray is useful if obstruction/perforation suspected.\n"
     "• Check glucose, electrolytes, renal function, CBC, blood gas if significantly unwell."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid resuscitation[/color]\n"
     "• For shock: isotonic crystalloid 10–20 mL/kg IV, with reassessment.\n\n"
     "[color=#1E3A8A]Enema reduction[/color]\n"
     "• Pneumatic or hydrostatic enema reduction may be attempted in an equipped center when stable and no perforation/peritonitis.\n"
     "• Monitor closely during and after. Surgical reduction may be required if nonoperative fails.\n"
     "• Contraindicated in suspected bowel perforation, peritonitis, or unstable child."),
    ("05 — WARNINGS", "danger", 
     "• Enema reduction is contraindicated in suspected bowel perforation, peritonitis, or an unstable child.\n"
     "• Recurrent abdominal pain, vomiting, pallor, or lethargy after reduction requires immediate reassessment (recurrence can occur)."),
    ("06 — DISPOSITION", "warning", 
     "• All suspected cases require urgent pediatric surgical discussion.\n"
     "• Admit or transfer urgently when confirmed or strongly suspected."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; Perth Children's Hospital.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Diabetic Ketoacidosis (DKA)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Polyuria, polydipsia, weight loss, fatigue, vomiting, abdominal pain, dehydration.\n"
     "• Kussmaul breathing, fruity/acetone breath odor. Severe disease: reduced consciousness, shock, coma.\n"
     "• Criteria: hyperglycemia (>11 mmol/L), venous pH <7.3 or bicarb <18, beta-hydroxybutyrate ≥3 mmol/L or significant ketonuria."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, hydration, respiratory pattern, neurological status.\n"
     "• Measure bedside glucose and blood ketones immediately.\n"
     "• Obtain IV access, send venous blood gas, electrolytes, urea, creatinine.\n"
     "• Start carefully calculated IV fluid therapy according to pediatric DKA protocol.\n"
     "• Perform frequent neurological assessments (cerebral injury is a critical complication)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IV fluid replacement[/color]\n"
     "• Begin with isotonic crystalloid 10–20 mL/kg over 20–30 min if indicated, followed by reassessment.\n"
     "• Calculate maintenance and deficit using the pediatric DKA pathway. Do not use unmonitored adult regimens.\n\n"
     "[color=#1E3A8A]IV insulin infusion[/color]\n"
     "• Regular insulin 0.05–0.1 units/kg/hour according to protocol.\n"
     "• Begin insulin typically at least 1 hour after fluids have started.\n"
     "• Never give an IV insulin bolus for routine pediatric DKA.\n"
     "• Add dextrose-containing fluid as glucose falls, while continuing insulin to suppress ketogenesis.\n\n"
     "[color=#1E3A8A]Potassium replacement[/color]\n"
     "• Depends on serum K+, renal function, urine output. Never give concentrated KCl IV push.\n\n"
     "[color=#1E3A8A]Sodium bicarbonate[/color]\n"
     "• Routine use is NOT recommended. Consider exceptional use only under specialist direction."),
    ("04 — WARNINGS", "danger", 
     "• Cerebral injury is a potentially fatal complication. Headache, worsening irritability, decreasing consciousness, bradycardia, or new neurological signs require immediate escalation.\n"
     "• Do not start insulin if potassium is dangerously low.\n"
     "• Children with DKA have total-body potassium depletion even if initial serum K+ is normal/elevated."),
    ("05 — DISPOSITION", "warning", 
     "• All children with DKA require hospital admission and protocol-based monitoring.\n"
     "• Severe DKA, altered consciousness, or shock requires urgent pediatric intensive care assessment."),
    ("REFERENCES", "info", "ISPAD Guidelines; Royal Children's Hospital Melbourne; CPS.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Hypoglycemia")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sweating, tremor, pallor, tachycardia, irritability, hunger, behavioral change.\n"
     "• Severe: confusion, seizures, reduced consciousness, coma.\n"
     "• Infants: poor feeding, lethargy, apnea, hypothermia, or seizures.\n"
     "• Confirm low glucose promptly, but do not delay emergency treatment in a symptomatic child."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, circulation, and bedside glucose.\n"
     "• Conscious and can swallow safely: rapid-acting oral glucose.\n"
     "• Seizures, reduced consciousness, or cannot swallow: IV dextrose.\n"
     "• Recheck glucose promptly after treatment and repeat if hypoglycemia persists.\n"
     "• Identify and treat the underlying cause (consider critical sample before glucose if recurrent/unexplained, without delaying treatment)."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Oral glucose (Conscious child)[/color]\n"
     "• ~0.3 g/kg of rapid-acting oral glucose (commonly up to 15 g per treatment).\n"
     "• Recheck glucose after 10–15 min. Repeat if low. Provide meal/longer-acting carb once corrected.\n\n"
     "[color=#1E3A8A]IV dextrose (Severe/Symptomatic)[/color]\n"
     "• 10% dextrose 2.5 mL/kg IV (equivalent to 0.25 g/kg glucose).\n"
     "• Recheck glucose after 10–15 min. If recurrent, commence controlled dextrose infusion.\n\n"
     "[color=#1E3A8A]Glucagon (If IV unavailable)[/color]\n"
     "• Use age/weight-appropriate glucagon per product labeling. Give carbohydrate once awake.\n"
     "• May be less effective if hepatic glycogen stores are depleted (e.g., prolonged fasting)."),
    ("04 — WARNINGS", "danger", 
     "• Never give oral glucose, drinks, or food to a child who cannot protect their airway.\n"
     "• Avoid unnecessary concentrated dextrose through a peripheral line (extravasation injury)."),
    ("05 — DISPOSITION", "warning", 
     "• Admit or observe severe, recurrent, unexplained, or treatment-resistant hypoglycemia.\n"
     "• Admission indicated if ongoing dextrose infusion is required or serious underlying illness suspected."),
    ("REFERENCES", "info", "ISPAD Guidelines; Local pediatric protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Poisoning and Drug Overdose")] = [
    ("01 — RECOGNIZE", "info", 
     "• Consider poisoning in a child with unexplained altered consciousness, vomiting, seizures, abnormal behavior, respiratory depression, or metabolic acidosis.\n"
     "• Obtain history: substance, amount, time, route, co-ingestants.\n"
     "• Examine for toxidromes (opioid, anticholinergic, sympathomimetic, sedative, cholinergic).\n"
     "• A normal initial exam does not exclude delayed toxicity."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and treat airway obstruction, respiratory failure, shock, and seizures immediately.\n"
     "• Check bedside glucose in every child with altered consciousness.\n"
     "• Remove contaminated clothing and irrigate exposed skin/eyes.\n"
     "• Identify substance and contact a poison information service/toxicology.\n"
     "• Do not induce vomiting. Do not administer activated charcoal routinely without assessing airway safety and timing."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside glucose, ECG, vital signs, neurological assessment.\n"
     "• Electrolytes, renal function, blood gas, lactate when indicated.\n"
     "• Targeted tests: paracetamol level, salicylate level, ethanol level, etc.\n"
     "• Consider anion gap, osmolal gap for toxic alcohols.\n"
     "• Urine drug screens have limitations; do not use to exclude poisoning."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Stabilization[/color]\n"
     "• Treatment depends on substance. Correct hypoglycemia, treat seizures, support airway/shock.\n\n"
     "[color=#1E3A8A]Activated charcoal[/color]\n"
     "• Single dose 1 g/kg orally (up to local max). Consider only after toxicology consult.\n"
     "• Most useful for adsorbable substances early (usually within 1 hour).\n"
     "• Do not use in unprotected airway, bowel obstruction, or corrosives/alcohols.\n\n"
     "[color=#1E3A8A]Naloxone (Opioid toxicity)[/color]\n"
     "• Pediatric weight-based regimen. Priority is reversal of respiratory depression, not necessarily full awakening.\n\n"
     "[color=#1E3A8A]Substance-specific antidotes[/color]\n"
     "• Paracetamol: N-acetylcysteine per nomogram.\n"
     "• Organophosphate: Atropine and oxime.\n"
     "• Methanol/Ethylene glycol: Fomepizole/ethanol, possible dialysis.\n"
     "• Iron: Chelation if indicated."),
    ("05 — WARNINGS", "danger", 
     "• Respiratory depression, seizures, hypotension, severe metabolic acidosis, arrhythmias, or reduced consciousness require resuscitation-level care.\n"
     "• Some substances cause delayed deterioration despite an initially normal exam.\n"
     "• Consider safeguarding assessment when intentional ingestion, neglect, or inconsistent history is suspected."),
    ("06 — DISPOSITION", "warning", 
     "• Admit significant symptoms, abnormal ECG, altered consciousness, or high-risk substances.\n"
     "• Discharge only when substance-appropriate observation is complete and child is clinically stable."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; WHO; Local poison service.")
]


# ==================== BATCH 5 & 6 (TOPICS 21-30) ====================

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Head Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Head injury ranges from minor scalp trauma to traumatic brain injury (TBI), intracranial hemorrhage, skull fracture, and secondary brain injury caused by hypoxia or hypotension.\n\n"
     "[color=#1E3A8A]Assess for:[/color]\n"
     "• Loss of consciousness, confusion, amnesia, or abnormal behavior.\n"
     "• Persistent or worsening headache, repeated vomiting, seizure.\n"
     "• Reduced GCS, abnormal pupils, or focal neurological deficit.\n"
     "• Signs of skull fracture: palpable depression, hemotympanum, periorbital bruising, Battle sign, or CSF leakage.\n"
     "• Scalp hematoma (large or non-frontal in an infant).\n"
     "• Possible non-accidental injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Apply an ABCDE approach and assess the pediatric GCS.\n"
     "• Protect the cervical spine.\n"
     "• Prevent secondary brain injury: Correct hypoxemia immediately, treat hypotension promptly, avoid hypoglycemia, maintain normothermia.\n"
     "• Check bedside blood glucose in altered consciousness or seizures.\n"
     "• Seek urgent neurosurgical or pediatric critical-care advice for deteriorating consciousness, suspected intracranial bleeding, or signs of raised ICP."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]CT head without contrast[/color]\n"
     "• NICE recommends CT within 1 hour for high-risk features (suspected NAI, post-traumatic seizure, GCS < 14 on initial or < 15 at 2 hours, suspected skull fracture, focal deficit, large scalp injury in < 1yo).\n"
     "• Intermediate-risk factors may require urgent CT or structured observation (≥ 4 hours).\n\n"
     "[color=#1E3A8A]Other tests[/color]\n"
     "• Blood glucose immediately. CBC, coagulation, crossmatch if significant trauma.\n"
     "• Do not use skull radiographs as a substitute for CT."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Airway and breathing[/color]\n"
     "• Oxygen: titrate to age-appropriate SpO2. Avoid hypoxia and hypotension.\n"
     "• Aim for normocapnia. Do not routinely hyperventilate.\n\n"
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 15 mg/kg orally every 4–6 hours. Opioids may be needed for severe pain (titrate carefully).\n\n"
     "[color=#1E3A8A]Suspected raised ICP / herniation[/color]\n"
     "• Elevate head ~30 degrees, keep neck midline.\n"
     "• Prevent hypoxia, hypotension, fever, and seizures.\n"
     "• Hyperosmolar therapy may be required under critical-care protocol.\n"
     "• Avoid routine corticosteroids for TBI."),
    ("05 — WARNINGS", "danger", 
     "• A normal initial appearance does not exclude intracranial injury.\n"
     "• Infants may deteriorate without clear verbal symptoms.\n"
     "• Any neurological deterioration, new seizure, repeated vomiting, unequal pupils, or falling GCS requires immediate reassessment.\n"
     "• Consider safeguarding assessment if abuse is possible."),
    ("06 — DISPOSITION", "warning", 
     "• Discharge only if returned to normal state, no concerning features, tolerating oral intake, reliable supervision, and written head-injury precautions given.\n"
     "• Admit or transfer for abnormal imaging, persistent symptoms, reduced GCS, or suspected abuse."),
    ("REFERENCES", "info", "NICE NG232; NICE NG41.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Burns and Scalds")] = [
    ("01 — RECOGNIZE", "info", 
     "Assess burn mechanism, time, depth, total body surface area (TBSA), and associated trauma.\n"
     "• Superficial: red, painful, dry (not included in TBSA fluid calc).\n"
     "• Partial-thickness: blistering, moist, significant pain.\n"
     "• Full-thickness: leathery, pale/brown/charred, reduced sensation.\n"
     "• Inhalation injury: facial/neck burns, hoarseness, stridor, soot, respiratory distress.\n"
     "• Circumferential burns: may compromise perfusion/chest expansion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop burning process and remove from source.\n"
     "• ABCDE assessment; treat associated trauma first.\n"
     "• Cool thermal burn with cool running water for 20 minutes (ideally within 3 hours).\n"
     "• Remove clothing/jewelry unless adherent. Prevent hypothermia (cool the burn, not the child).\n"
     "• Cover loosely with clean non-adherent dressing or clean film (lengthwise, never circumferentially).\n"
     "• Give early analgesia and obtain IV/IO access for major burns.\n"
     "• Arrange early specialist consult for inhalation, major, electrical, chemical, or special-area burns."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 15 mg/kg orally every 4–6 hours. IV morphine 0.05–0.1 mg/kg IV slowly for severe pain.\n\n"
     "[color=#1E3A8A]IV fluid resuscitation[/color]\n"
     "• Indicated for burns > 10% TBSA (or earlier if shock).\n"
     "• Modified Parkland: 3 mL × weight (kg) × %TBSA over 24 hours (half in first 8 hours from injury).\n"
     "• Add maintenance fluids (with glucose as appropriate).\n"
     "• Monitor urine output (target ~1 mL/kg/hour).\n"
     "• Avoid excessive fluids (worsens edema).\n\n"
     "[color=#1E3A8A]Airway / inhalation[/color]\n"
     "• High-concentration oxygen. Early expert airway assessment; consider early intubation if progressive edema or stridor."),
    ("04 — WARNINGS", "danger", 
     "• Children are vulnerable to hypothermia and fluid overload.\n"
     "• Do not calculate TBSA using superficial erythema alone.\n"
     "• Chemical eye burns require immediate prolonged irrigation.\n"
     "• Electrical injuries may cause deep tissue damage despite small skin lesions.\n"
     "• Consider non-accidental injury if history/pattern is concerning."),
    ("05 — DISPOSITION", "warning", 
     "• Refer/transfer urgently for airway injury, major/full-thickness burns, circumferential burns, electrical/chemical burns, special areas, or suspected abuse.\n"
     "• Small uncomplicated burns may be outpatient after assessment, pain control, dressing, tetanus review, and follow-up."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; NICE NG39.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Trauma and Fractures")] = [
    ("01 — RECOGNIZE", "info", 
     "Trauma may involve isolated limb injury or multisystem injury. Children can mask significant blood loss until deterioration.\n"
     "• High-energy mechanism, airway compromise, chest/abdominal tenderness, altered consciousness.\n"
     "• Deformity, swelling, open wound, severe pain, inability to use limb.\n"
     "• Distal neurovascular compromise: absent/weak pulse, delayed cap refill, cool limb, numbness.\n"
     "• Compartment syndrome: escalating pain, pain with passive stretch, tense swelling.\n"
     "• Possible non-accidental injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Structured pediatric trauma primary survey (ABCDE with cervical spine protection).\n"
     "• Control external hemorrhage. Tourniquet for life-threatening limb bleeding.\n"
     "• Treat shock promptly. Judicious isotonic crystalloid while arranging blood products.\n"
     "• Immobilize fractures in position found (unless reduction needed for perfusion).\n"
     "• Document neurovascular findings before/after splinting.\n"
     "• Urgent orthopedic/trauma consult for open fractures, neurovascular compromise, or suspected compartment syndrome."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Pain control[/color]\n"
     "• Paracetamol 15 mg/kg, Ibuprofen 10 mg/kg (if appropriate).\n"
     "• Severe pain: IV morphine 0.05–0.1 mg/kg slowly.\n\n"
     "[color=#1E3A8A]Open fracture[/color]\n"
     "• Sterile dressing. Do not probe or push bone back in.\n"
     "• IV antibiotics as early as possible. Check tetanus status.\n\n"
     "[color=#1E3A8A]Neurovascular compromise / Compartment syndrome[/color]\n"
     "• Remove constricting items, reassess splints.\n"
     "• Urgent reduction if displaced fracture compromises perfusion.\n"
     "• Suspected compartment syndrome = surgical emergency. Keep limb at heart level, remove constrictions. Do not delay for pressure measurements if clinically convincing.\n\n"
     "[color=#1E3A8A]Hemorrhagic shock[/color]\n"
     "• Control bleeding, activate major hemorrhage pathway. Blood products early. Avoid large crystalloid boluses."),
    ("04 — WARNINGS", "danger", 
     "• Children maintain BP until late shock; do not rely on hypotension alone.\n"
     "• Preserved pulses do not exclude compartment syndrome.\n"
     "• Severe pain, pain on passive stretch, or rapidly increasing swelling requires immediate evaluation.\n"
     "• Do not discharge with unresolved neurovascular abnormalities."),
    ("05 — DISPOSITION", "warning", 
     "• Admit/transfer for open/unstable fractures, neurovascular compromise, compartment syndrome, significant trauma, or suspected abuse.\n"
     "• Discharge only after adequate assessment, satisfactory neurovascular findings, and clear follow-up."),
    ("REFERENCES", "info", "NICE NG39; Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Foreign-Body and Caustic Ingestion")] = [
    ("01 — RECOGNIZE", "info", 
     "• Foreign-body: May be asymptomatic or cause drooling, dysphagia, vomiting, chest/abdominal pain, or respiratory distress.\n"
     "• [color=#991B1B]High-risk:[/color] Button batteries (especially esophagus), multiple magnets, sharp objects, large objects, objects causing airway symptoms.\n"
     "• [color=#991B1B]Caustic ingestion:[/color] Strong acids/alkalis. Drooling, painful swallowing, oral burns, vomiting, stridor. Absence of oral burns does NOT exclude esophageal injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation. Follow choking algorithm if complete obstruction.\n"
     "• Keep NPO if urgent endoscopy/airway intervention may be required.\n"
     "• Identify object/product, time, amount, symptoms. Bring packaging.\n"
     "• Contact pediatric surgery/gastro/ENT/toxicology early.\n"
     "• Do NOT induce vomiting. Do NOT give activated charcoal or attempt chemical neutralization for caustics."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Foreign body[/color]\n"
     "• X-rays (neck, chest, abdomen) to locate radiopaque objects.\n"
     "• Button batteries: double-rim/halo appearance.\n"
     "• Normal X-rays do not exclude radiolucent objects.\n\n"
     "[color=#1E3A8A]Caustic ingestion[/color]\n"
     "• Assess airway and signs of perforation.\n"
     "• Chest/abdominal imaging if perforation suspected.\n"
     "• Endoscopy timing determined urgently with specialists."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Esophageal button battery[/color]\n"
     "• Time-critical emergency. Urgent specialist consult and emergent removal.\n"
     "• Honey may be considered (≥12 months) under poison-center protocol while arranging transport (do not delay definitive care).\n\n"
     "[color=#1E3A8A]Magnets and sharp objects[/color]\n"
     "• Multiple magnets/magnet + metal = urgent specialist assessment (risk of necrosis/fistula).\n"
     "• Sharp objects in esophagus/stomach = urgent endoscopic evaluation.\n\n"
     "[color=#1E3A8A]Caustic ingestion[/color]\n"
     "• Protect airway, assess for progressive edema/stridor.\n"
     "• Do not induce vomiting, perform blind lavage, or attempt neutralization.\n"
     "• No universal antidote; supportive care and early specialist assessment.\n"
     "• Avoid blind NG tube placement."),
    ("05 — WARNINGS", "danger", 
     "• Any esophageal button battery is an emergency.\n"
     "• Multiple magnets are high risk even if initially well.\n"
     "• Persistent drooling, inability to swallow, stridor, severe pain, or peritonitis requires emergency escalation."),
    ("06 — DISPOSITION", "warning", 
     "• Admit/transfer for esophageal batteries, multiple magnets, sharp objects, symptomatic caustic ingestion, or suspected perforation.\n"
     "• Discharge after low-risk blunt object only if no symptoms and safe follow-up."),
    ("REFERENCES", "info", "NASPGHAN; National Capital Poison Center; Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Sickle Cell Emergencies")] = [
    ("01 — RECOGNIZE", "info", 
     "• [color=#1E3A8A]Vaso-occlusive crisis:[/color] Acute pain (bones, limbs, back, chest, abdomen). Assess for fever, hypoxemia, focal neuro symptoms, abdominal enlargement.\n"
     "• [color=#1E3A8A]Acute chest syndrome (ACS):[/color] New pulmonary infiltrate + fever and/or respiratory symptoms. May deteriorate rapidly.\n"
     "• [color=#1E3A8A]Other:[/color] Stroke, splenic sequestration (sudden splenomegaly, pallor, shock), aplastic crisis, sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE, vital signs, pain severity, SpO2, hydration, neuro status.\n"
     "• Treat fever urgently; do not assume uncomplicated crisis.\n"
     "• Prompt analgesia for severe pain (within 30–60 min).\n"
     "• Give oxygen for hypoxemia (not routine if normoxic).\n"
     "• Contact hematology/pediatric team early for ACS, stroke, sequestration, sepsis."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Vaso-occlusive pain[/color]\n"
     "• Paracetamol 15 mg/kg, Ibuprofen 10 mg/kg (if appropriate).\n"
     "• Severe pain: IV morphine 0.05–0.1 mg/kg slowly, reassess and titrate.\n"
     "• Encourage oral fluids. IV fluid only if needed (avoid overload).\n\n"
     "[color=#1E3A8A]Acute chest syndrome[/color]\n"
     "• Admit, oxygen, monitor closely, analgesia without excessive sedation.\n"
     "• Incentive spirometry when awake.\n"
     "• Empiric antibiotics: Ceftriaxone 50–75 mg/kg IV every 24 hours + Azithromycin per local protocol.\n"
     "• Discuss transfusion with hematology for hypoxemia or deterioration.\n\n"
     "[color=#1E3A8A]Fever/Sepsis[/color]\n"
     "• Obtain cultures, but start IV antibiotics promptly per sickle cell fever pathway.\n\n"
     "[color=#1E3A8A]Stroke / Sequestration[/color]\n"
     "• Stroke: Activate stroke pathway, urgent imaging, specialist-directed exchange transfusion.\n"
     "• Sequestration: Urgent CBC/crossmatch, treat shock, urgent transfusion (careful of hyperviscosity)."),
    ("04 — WARNINGS", "danger", 
     "• Fever, respiratory symptoms, hypoxemia, neurological deficit, rapidly enlarging spleen, or severe pallor are NOT uncomplicated pain crises.\n"
     "• ACS can progress rapidly.\n"
     "• Avoid dehydration and excessive IV fluid.\n"
     "• Do not transfuse routinely for uncomplicated pain crisis."),
    ("05 — DISPOSITION", "warning", 
     "• Admit urgently for ACS, stroke, sequestration, aplastic crisis, sepsis, hypoxemia, uncontrolled pain, or inability to maintain intake.\n"
     "• Outpatient only if clinically stable, serious complications excluded, pain controlled, and reliable follow-up."),
    ("REFERENCES", "info", "WHO 2026; CDC; NHLBI.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Kidney Injury (AKI) in Children")] = [
    ("01 — RECOGNIZE", "info", 
     "Abrupt decline in kidney function leading to fluid overload, electrolyte disturbances, acidosis, uremia.\n"
     "• Causes: Prerenal (dehydration, hemorrhage, sepsis), Intrinsic (ATN, glomerulonephritis, HUS), Postrenal (obstruction).\n"
     "• Features: Reduced urine output/anuria, dehydration/poor perfusion, edema, hypertension, vomiting, lethargy, hyperkalemia, acidosis.\n"
     "• KDIGO criteria: Creatinine ↑ ≥ 0.3 mg/dL in 48h, or ↑ to ≥ 1.5x baseline in 7 days, or UO < 0.5 mL/kg/h for ≥ 6h."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE, perfusion, BP, hydration. Record strict fluid intake/output, weigh child.\n"
     "• Check glucose, electrolytes, urea, creatinine, blood gas.\n"
     "• Stop/withhold nephrotoxic meds, review doses.\n"
     "• Treat cause: shock, sepsis, dehydration, obstruction.\n"
     "• Urgent nephrology consult for severe AKI, anuria, refractory electrolyte abnormalities, or overload."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid management[/color]\n"
     "• If hypovolemic/shock: Isotonic crystalloid 10 mL/kg IV, reassess.\n"
     "• Once perfused, calculate maintenance carefully.\n"
     "• In oliguric/anuric AKI, avoid routine fluid loading (risk of pulmonary edema).\n\n"
     "[color=#1E3A8A]Medications[/color]\n"
     "• Adjust renal doses. Avoid NSAIDs.\n"
     "• Loop diuretics (e.g., Furosemide 1 mg/kg IV) for fluid overload (do not use just to convert oliguria).\n\n"
     "[color=#1E3A8A]Renal Replacement Therapy (RRT)[/color]\n"
     "• Indications: Refractory hyperkalemia, severe acidosis, fluid overload with respiratory compromise, uremic complications."),
    ("04 — WARNINGS", "danger", 
     "• Repeated fluid boluses can cause pulmonary edema in oliguric AKI.\n"
     "• A normal initial creatinine does not exclude evolving AKI.\n"
     "• Investigate urinary obstruction promptly."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for significant AKI, persistent oliguria, electrolyte/acid-base abnormalities, fluid overload, or suspected intrinsic renal disease.\n"
     "• Transfer to center with pediatric critical care/RRT if refractory complications."),
    ("REFERENCES", "info", "NICE NG148; KDIGO.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Hyperkalemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Can cause fatal conduction abnormalities, arrhythmias, cardiac arrest.\n"
     "• Thresholds: Mild 5.5–6.0, Moderate 6.1–7.0, Severe > 7.0 mmol/L (Neonates have different ranges). Treat clinical context and ECG.\n"
     "• ECG: Tall peaked T waves, PR prolongation, loss of P waves, QRS widening, sine wave.\n"
     "• Causes: AKI, dehydration, acidosis, tumor lysis, rhabdomyolysis, adrenal insufficiency, pseudohyperkalemia (hemolysis)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• ABCDE, immediate 12-lead ECG, continuous cardiac monitoring.\n"
     "• IV access, urgent labs (K+, glucose, renal, blood gas).\n"
     "• If severe/ECG changes, start emergency treatment without waiting for repeat labs.\n"
     "• Stop K+ administration and review medications."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Stabilize cardiac membrane (if ECG changes)[/color]\n"
     "• Calcium gluconate 10%: 0.5 mL/kg IV (max 20 mL) over 5–10 min under ECG monitoring. (Calcium chloride 10% may be preferred in arrest, but is more injurious if extravasated).\n\n"
     "[color=#1E3A8A]2. Shift K+ into cells[/color]\n"
     "• Insulin/Glucose: Regular insulin 0.1 unit/kg IV (max 10 units) + Glucose 0.5 g/kg IV. Monitor glucose closely for ≥ 4–6 hours.\n"
     "• Nebulized Salbutamol: 2.5 mg (smaller) or 5 mg (larger) as adjunct.\n\n"
     "[color=#1E3A8A]3. Remove K+ from body[/color]\n"
     "• Treat cause (AKI, shock, acidosis). Consider potassium binders or urgent dialysis for refractory cases."),
    ("04 — WARNINGS", "danger", 
     "• Severe hyperkalemia is an emergency even if child appears well.\n"
     "• Do not delay treatment for repeat testing when ECG is abnormal or K+ is critically high.\n"
     "• Calcium does not lower K+. Insulin/glucose shifts K+ temporarily. Watch for rebound and hypoglycemia."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for moderate/severe hyperkalemia, ECG abnormalities, AKI, or acidosis.\n"
     "• Transfer urgently for refractory hyperkalemia or need for dialysis."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; AHA PALS 2025.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Drowning and Submersion Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Respiratory impairment from submersion/immersion. May result in hypoxemia, respiratory failure, cardiac arrest, brain injury.\n"
     "• Cough, tachypnea, distress, hypoxemia. Altered consciousness, seizures, arrest. Hypothermia.\n"
     "• Prognosis depends on submersion duration, need for CPR, neuro state, oxygenation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure rescuer safety. Remove from water.\n"
     "• If unresponsive/not breathing normally: Activate emergency support, begin CPR (including rescue breaths). Use AED as soon as available.\n"
     "• Provide oxygen/ventilation for hypoxemia.\n"
     "• If trauma suspected, use spinal precautions (do not delay airway/resus).\n"
     "• Remove wet clothing, dry, prevent heat loss."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Oxygenation/Ventilation[/color]\n"
     "• Supplemental oxygen. Bag-mask if inadequate breathing. Intubation/mechanical ventilation for respiratory failure.\n"
     "• Lung-protective ventilation strategies.\n"
     "• Do not delay ventilation to drain water. Abdominal thrusts not recommended for water removal.\n\n"
     "[color=#1E3A8A]CPR / Hypothermia[/color]\n"
     "• High-quality pediatric CPR, AED. Treat hypoxia as major reversible cause.\n"
     "• Remove wet clothing, insulate, active rewarming per protocol.\n\n"
     "[color=#1E3A8A]Antibiotics/Steroids[/color]\n"
     "• Do NOT prescribe prophylactic antibiotics routinely.\n"
     "• Corticosteroids NOT routinely recommended."),
    ("04 — WARNINGS", "danger", 
     "• Respiratory deterioration can occur after initial event.\n"
     "• Do not assume safe because child coughed up water or initially appeared well.\n"
     "• Consider hypothermia, trauma, intoxication, seizure, or underlying event."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for persistent cough, distress, abnormal SpO2, altered mental status, hypothermia, or need for resus.\n"
     "• Discharge after observation ONLY if completely asymptomatic, normal vitals/SpO2, reassuring exam."),
    ("REFERENCES", "info", "AHA BLS 2025; Resuscitation Council UK 2025.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Cardiac Arrest")] = [
    ("01 — RECOGNIZE", "info", 
     "Frequently preceded by respiratory failure or shock.\n"
     "• Unresponsive, not breathing normally/gasping, no definite pulse (check ≤ 10 sec).\n"
     "• If pulse present but HR < 60/min with poor perfusion despite oxygenation/ventilation → start compressions."),
    ("02 — HIGH-QUALITY CPR", "info", 
     "• Rate: 100–120/min.\n"
     "• Depth: ≥ 1/3 AP diameter (~4 cm infant, 5 cm child). Allow full recoil, minimize interruptions.\n"
     "• Infants: 2-thumb encircling or 1-hand heel (avoid 2-finger).\n"
     "• Single rescuer: 30:2. Two rescuers: 15:2 (before advanced airway).\n"
     "• Advanced airway: Continuous compressions + 20–30 breaths/min. Use capnography."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Epinephrine[/color]\n"
     "• IV/IO: 0.01 mg/kg (0.1 mg/mL concentration / 1:10,000) = 0.1 mL/kg. Max 1 mg.\n"
     "• Repeat every 3–5 minutes.\n\n"
     "[color=#1E3A8A]Defibrillation (VF/pVT)[/color]\n"
     "• 1st: 2 J/kg. 2nd: 4 J/kg. Subsequent: ≥ 4 J/kg (max 10 J/kg or adult dose).\n"
     "• Resume CPR immediately after shock.\n\n"
     "[color=#1E3A8A]Antiarrhythmics[/color]\n"
     "• Amiodarone 5 mg/kg IV/IO bolus (or Lidocaine) for refractory VF/pVT.\n\n"
     "[color=#1E3A8A]Bradycardia with poor perfusion[/color]\n"
     "• Support airway/oxygen/ventilation. If HR < 60 with compromise, start CPR. Consider epinephrine/atropine."),
    ("04 — WARNINGS", "danger", 
     "• Incorrect epinephrine concentration can cause fatal dosing errors. (0.1 mg/mL vs 1 mg/mL).\n"
     "• Avoid excessive ventilation and long pauses in compressions.\n"
     "• Routine sodium bicarbonate and calcium are NOT recommended unless specific indication (e.g., hyperkalemia)."),
    ("05 — DISPOSITION", "warning", 
     "• All children with ROSC require urgent pediatric critical care and cause evaluation."),
    ("REFERENCES", "info", "AHA/AAP PALS 2025; AHA/AAP BLS 2025.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Pediatric Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Inadequate tissue perfusion. Children maintain BP until late deterioration; hypotension is a late sign.\n"
     "• Types: Hypovolemic (dehydration, hemorrhage), Distributive (sepsis, anaphylaxis), Cardiogenic (myocarditis, arrhythmia), Obstructive (tension pneumothorax, tamponade).\n"
     "• Features: Tachycardia, prolonged cap refill, cool/mottled extremities, weak pulses, altered mental status, reduced UO, acidosis. Warm/bounding pulses in distributive."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call senior/critical care. ABCDE, oxygen.\n"
     "• IV access (IO if delayed). Check glucose, treat hypoglycemia.\n"
     "• Identify shock type and treat cause in parallel.\n"
     "• Isotonic crystalloid in carefully reassessed aliquots when indicated.\n"
     "• Start vasoactive support early if shock persists or fluids are unsafe."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid Resuscitation[/color]\n"
     "• Initial bolus: 10 mL/kg IV isotonic crystalloid, then reassess.\n"
     "• Septic shock: repeated 10–20 mL/kg aliquots per protocol.\n"
     "• Hemorrhagic: blood products early; avoid large crystalloid.\n"
     "• Stop boluses if signs of overload (pulmonary edema, hepatomegaly).\n\n"
     "[color=#1E3A8A]Vasoactive Support[/color]\n"
     "• Epinephrine or Norepinephrine infusion: start 0.05–0.1 mcg/kg/min, titrate to response.\n"
     "• Use standardized concentrations and pump library.\n\n"
     "[color=#1E3A8A]Treat underlying cause[/color]\n"
     "• Septic: Cultures (if no delay), broad-spectrum IV antibiotics, source control.\n"
     "• Anaphylactic: IM epinephrine.\n"
     "• Hemorrhagic: Control bleeding, activate hemorrhage pathway.\n"
     "• Cardiogenic: Cardiology consult, avoid repeated fluid boluses, use inotropes.\n"
     "• Obstructive: Urgent relief (e.g., needle decompression for pneumothorax)."),
    ("04 — WARNINGS", "danger", 
     "• A normal blood pressure does not exclude shock in children.\n"
     "• Reassess after every intervention. Shock evolves rapidly.\n"
     "• Do not treat every shock state identically (e.g., fluid loading can worsen cardiogenic/obstructive shock)."),
    ("05 — DISPOSITION", "warning", 
     "• Shock requires emergency resuscitation, admission, and usually critical care.\n"
     "• Transfer urgently if child needs ventilation, vasoactive infusions, blood products, or monitoring beyond local capacity."),
    ("REFERENCES", "info", "AHA/AAP PALS 2025; Royal Children's Hospital Melbourne; NICE NG254.")
]


# ==================== BATCH 7 & 8 (TOPICS 31-40) ====================

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Scrotum and Testicular Torsion")] = [
    ("01 — RECOGNIZE", "info", 
     "Testicular torsion is a time-critical surgical emergency caused by twisting of the spermatic cord, compromising testicular blood supply. Salvage is most likely with rapid detorsion, ideally within 4–6 hours.\n"
     "• Sudden unilateral scrotal/testicular pain. Nausea/vomiting.\n"
     "• Swelling, erythema, high-riding or horizontal testis.\n"
     "• Absent/abnormal cremasteric reflex (presence does not exclude).\n"
     "• In neonates: painless swelling, discoloration, or firm testis.\n"
     "• [color=#1E3A8A]Differential:[/color] Torsion of appendix testis, epididymitis, incarcerated hernia, trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess pain, vital signs, onset/duration.\n"
     "• Contact surgery/urology immediately if torsion suspected.\n"
     "• Keep NPO, establish IV access if surgery likely.\n"
     "• Provide analgesia and antiemetic.\n"
     "• Do not delay surgical consultation or transfer for imaging when suspicion is high."),
    ("03 — INVESTIGATIONS", "info", 
     "• Doppler ultrasound: May help if diagnosis uncertain and immediately available. Preserved flow does NOT completely exclude torsion. Imaging must NOT delay surgery.\n"
     "• Urinalysis/culture: May help if infection suspected but do not exclude torsion.\n"
     "• Blood tests: Not routinely required, should not delay surgery."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 15 mg/kg orally every 4–6 hours.\n"
     "• Severe pain: titrated IV morphine 0.05–0.1 mg/kg slowly.\n\n"
     "[color=#1E3A8A]Definitive management[/color]\n"
     "• Urgent surgical exploration and detorsion + fixation (affected and contralateral testes).\n"
     "• Manual detorsion: May be attempted by experienced clinician while arranging surgery. Temporizing only; does NOT remove need for surgery."),
    ("05 — WARNINGS", "danger", 
     "• Time to detorsion is critical. Do not wait for next morning or delayed ultrasound.\n"
     "• Abdominal pain/vomiting may be main presentation in younger children.\n"
     "• A delayed presentation still requires urgent assessment.\n"
     "• Intermittent pain may indicate intermittent torsion."),
    ("06 — DISPOSITION", "warning", 
     "• All suspected cases require emergency surgical assessment.\n"
     "• Discharge only after torsion and other urgent causes are excluded with clear follow-up."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; EAU Paediatric Urology Guidelines.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Hyperbilirubinemia and Jaundice")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe unconjugated hyperbilirubinemia can cause acute bilirubin encephalopathy and kernicterus. Jaundice in the first 24 hours is particularly concerning.\n"
     "• Assess age in hours, gestational age, birth weight.\n"
     "• Risk factors: Hemolysis (blood group incompatibility, positive DAT, G6PD, bruising), sepsis, prematurity.\n"
     "• Pale stools/dark urine suggests conjugated hyperbilirubinemia (hepatobiliary disease).\n"
     "• [color=#991B1B]Acute bilirubin encephalopathy:[/color] Poor feeding, lethargy, abnormal tone, high-pitched cry, hypertonia, arching, retrocollis, opisthotonus, apnea, seizures."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temp, feeding, hydration, neuro state.\n"
     "• Establish exact age in hours.\n"
     "• Obtain urgent bilirubin for jaundice < 24 hours or unwell infant.\n"
     "• Use validated treatment-threshold chart (gestational age, hours, risk factors).\n"
     "• Start phototherapy promptly at threshold.\n"
     "• Contact neonatology urgently for rapid rise, near-exchange thresholds, neuro signs, or suspected hemolysis."),
    ("03 — INVESTIGATIONS", "info", 
     "• Total serum bilirubin (TSB). Transcutaneous for screening only.\n"
     "• Direct/conjugated bilirubin if prolonged jaundice or pale stools/dark urine.\n"
     "• Maternal/infant blood groups, DAT if hemolysis possible.\n"
     "• CBC, reticulocyte count, blood film, G6PD testing.\n"
     "• Sepsis investigations if clinically indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Phototherapy[/color]\n"
     "• Indications: TSB at/above threshold for age and risk factors.\n"
     "• Use effective medical equipment, expose max skin, protect eyes, maintain temp/hydration. Repeat TSB per protocol.\n"
     "• Do not use sunlight as a substitute.\n\n"
     "[color=#1E3A8A]Exchange transfusion[/color]\n"
     "• Indications: TSB at/above exchange threshold, or signs of encephalopathy (emergency).\n"
     "• Intensive phototherapy while preparing. Urgent neonatology consult/transfer.\n\n"
     "[color=#1E3A8A]Feeding/hydration[/color]\n"
     "• Support frequent effective feeding. Avoid routine water/glucose water."),
    ("05 — WARNINGS", "danger", 
     "• Jaundice < 24 hours requires urgent assessment.\n"
     "• Lethargy, abnormal tone, high-pitched cry, arching, apnea, or seizures are emergency features.\n"
     "• Visual inspection alone cannot reliably quantify bilirubin.\n"
     "• Prolonged jaundice, pale stools, dark urine requires assessment for cholestasis."),
    ("06 — DISPOSITION", "warning", 
     "• Admit/transfer for severe hyperbilirubinemia, rapid rise, neuro signs, sepsis, dehydration, or possible exchange transfusion."),
    ("REFERENCES", "info", "AAP Clinical Practice Guideline 2022; NICE CG98.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Seizures")] = [
    ("01 — RECOGNIZE", "info", 
     "Can be subtle: eye deviation, repetitive oral movements, cycling limb movements, apnea, autonomic changes, stereotyped motor activity. Clinical observation alone may not distinguish from nonepileptic movements.\n"
     "• Causes: HIE, intracranial hemorrhage/stroke, hypoglycemia, hypocalcemia/magnesemia, meningitis/sepsis, metabolic disorders."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize ABCs. Position safely, oxygen/ventilation, monitor ECG/SpO2/temp.\n"
     "• Check bedside glucose immediately; correct hypoglycemia without delay.\n"
     "• Establish IV access. Obtain urgent neonatal support.\n"
     "• Look for and correct electrolyte disturbances, treat suspected infection.\n"
     "• Use EEG/aEEG to confirm seizures and monitor response if available."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bedside glucose, electrolytes (Ca, Mg), blood gas, renal function.\n"
     "• CBC, blood culture if sepsis/meningitis suspected. LP when safe.\n"
     "• Cranial ultrasound/MRI based on suspected cause. EEG (video)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hypoglycemia[/color]\n"
     "• 10% dextrose 2 mL/kg IV (0.2 g/kg), followed by infusion. Recheck glucose promptly.\n\n"
     "[color=#1E3A8A]First-line: Phenobarbital[/color]\n"
     "• Loading dose: 20 mg/kg IV slowly. Additional doses may be considered for persistent seizures per protocol.\n"
     "• Monitor respiratory rate, SpO2, BP, HR, consciousness. Ensure airway/ventilation support is available (risk of respiratory depression).\n\n"
     "[color=#1E3A8A]Persistent seizures[/color]\n"
     "• Reassess glucose/electrolytes/oxygenation. Seek neonatology/neurology guidance for 2nd-line (levetiracetam, phenytoin). Consider pyridoxine in refractory cases."),
    ("05 — WARNINGS", "danger", 
     "• Treat the cause as well as the seizure.\n"
     "• Neonatal seizures may be electrographic without clinical movements.\n"
     "• Do not delay glucose measurement/correction.\n"
     "• Avoid empiric repeated antiseizure doses without reassessment and monitoring."),
    ("06 — DISPOSITION", "warning", 
     "• All neonates with suspected seizures require urgent hospital evaluation and usually admission to a neonatal unit with continuous monitoring."),
    ("REFERENCES", "info", "ILAE Neonatal Seizures Recommendations; WHO Guidelines.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Snakebite and Scorpion Sting")] = [
    ("01 — RECOGNIZE", "info", 
     "Children may develop severe systemic toxicity from a smaller venom dose relative to body weight.\n"
     "• [color=#1E3A8A]Snakebite:[/color] Fang marks, swelling, bruising, spontaneous bleeding, ptosis, weakness, shock, dark urine.\n"
     "• [color=#1E3A8A]Scorpion sting:[/color] Severe local pain, agitation, sweating, salivation, abnormal eye movements, tachycardia/bradycardia, muscle jerking, pulmonary edema."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure scene safety. Move away from animal.\n"
     "• Assess ABCs, provide respiratory/circulatory support.\n"
     "• Keep child calm, immobilize affected limb. Remove rings/constricting items.\n"
     "• Mark edge of swelling and record time.\n"
     "• Contact poison center/toxicology. Arrange urgent transfer for systemic symptoms.\n"
     "• Do not delay transfer for home remedies."),
    ("03 — INVESTIGATIONS", "info", 
     "• Snakebite: CBC, platelets, PT/INR, aPTT, fibrinogen, renal function, urinalysis, crossmatch if bleeding.\n"
     "• Scorpion: Continuous ECG, glucose, electrolytes, blood gas, cardiac biomarkers, chest imaging/echo if severe."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]First Aid[/color]\n"
     "• Immobilize limb, minimize movement. Clean wound, provide tetanus prophylaxis.\n"
     "• [color=#991B1B]Do NOT:[/color] Apply tight tourniquet, cut/suck wound, apply ice, burn, or use electric shock.\n\n"
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 15 mg/kg. Avoid NSAIDs if coagulopathy/bleeding/renal injury.\n\n"
     "[color=#1E3A8A]Antivenom[/color]\n"
     "• Indications: Systemic envenomation, significant coagulopathy, neurotoxicity, shock.\n"
     "• Children often require the SAME dose as adults (venom dose not proportional to weight). Follow product instructions and regional toxicology guidance.\n"
     "• Administer in a setting capable of treating anaphylaxis. Monitor for hypersensitivity.\n\n"
     "[color=#1E3A8A]Severe Scorpion[/color]\n"
     "• Supportive respiratory/cardiovascular care. Contact regional toxicology for species-specific antivenom."),
    ("05 — WARNINGS", "danger", 
     "• Children can deteriorate rapidly. Progressive weakness, ptosis, respiratory distress, bleeding, or shock requires urgent escalation.\n"
     "• Do not rely on fang marks or local pain severity to predict systemic toxicity.\n"
     "• Antivenom can cause severe acute hypersensitivity reactions. Be prepared to manage anaphylaxis."),
    ("06 — DISPOSITION", "warning", 
     "• Admit children with systemic symptoms, abnormal coagulation, progressive swelling, neurotoxicity, or antivenom treatment."),
    ("REFERENCES", "info", "WHO Snakebite Guidelines; WHO Scorpion Stings.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Electrical Injury and Lightning Strike")] = [
    ("01 — RECOGNIZE", "info", 
     "External skin lesions may underestimate internal damage.\n"
     "• Risk factors: High-voltage exposure, lightning strike, LOC/arrest, chest-crossing current, tetany, deep burns, dark urine, associated trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Ensure source is disconnected before touching patient. Do not approach downed lines.\n"
     "• Activate emergency services, use scene safety.\n"
     "• Assess responsiveness, breathing, pulse. Begin CPR/AED if arrest.\n"
     "• Oxygen/ventilation when indicated.\n"
     "• Assess burns, trauma, spinal injury. Obtain IV access.\n"
     "• Arrange urgent transfer for high-voltage, lightning, cardiac symptoms, LOC, or major burns."),
    ("03 — INVESTIGATIONS", "info", 
     "• 12-lead ECG for significant injury, cardiac symptoms, LOC, high-voltage, lightning.\n"
     "• Continuous cardiac monitoring for abnormal ECG or significant symptoms.\n"
     "• CBC, electrolytes, renal function, blood gas, CK, urinalysis (rhabdomyolysis).\n"
     "• Imaging for fractures/head injury based on mechanism."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Cardiac arrest/arrhythmia[/color]\n"
     "• Follow pediatric BLS/PALS. Defibrillate shockable rhythms.\n\n"
     "[color=#1E3A8A]Burns/Soft-tissue[/color]\n"
     "• Cover burns, prevent hypothermia. Assess entry/exit wounds. Early surgical consult.\n\n"
     "[color=#1E3A8A]Rhabdomyolysis/Renal protection[/color]\n"
     "• IV isotonic fluids individualized to perfusion/urine output. Monitor CK, electrolytes, renal function. Treat hyperkalemia."),
    ("05 — WARNINGS", "danger", 
     "• High-voltage/lightning can cause serious internal injury despite minimal external burns.\n"
     "• Delayed weakness, numbness, compartment syndrome, or renal injury may develop.\n"
     "• Do not touch patient until source is safe."),
    ("06 — DISPOSITION", "warning", 
     "• Admit/transfer for high-voltage, lightning, arrest, abnormal ECG, LOC, significant burns, rhabdomyolysis, or major trauma."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; AHA BLS.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Kawasaki Disease and MIS-C")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Kawasaki Disease (KD):[/color] Usually < 5 years. Persistent fever ≥ 5 days, bilateral non-purulent conjunctival injection, red/cracked lips/strawberry tongue, polymorphous rash, redness/swelling of hands/feet (later peeling), cervical lymphadenopathy. Major concern: coronary artery aneurysm.\n"
     "[color=#1E3A8A]MIS-C:[/color] Persistent fever + systemic inflammation + multisystem involvement (abdominal pain, rash, conjunctivitis, hypotension/shock, cardiac dysfunction). Consider recent SARS-CoV-2."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion. Continuous monitoring (ECG, SpO2, BP).\n"
     "• Obtain urgent pediatric and cardiology consultation.\n"
     "• If shock: carefully reassessed fluid boluses, early vasoactive support.\n"
     "• Obtain cultures and start empiric antibiotics promptly if bacterial sepsis cannot be excluded.\n"
     "• Arrange echocardiography."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, CRP, ESR, electrolytes, renal/liver function, albumin, urinalysis.\n"
     "• Blood cultures. ECG and echocardiography.\n"
     "• Troponin and BNP/NT-proBNP if myocarditis suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Kawasaki Disease[/color]\n"
     "• IVIG 2 g/kg IV as single infusion (standard initial). Do not delay for day 5 if strongly suspected.\n"
     "• Aspirin: Used with IVIG under specialist direction (acute phase varies). Low-dose antiplatelet continued after acute phase when indicated. (Avoid unsupervised aspirin in viral illness - Reye syndrome).\n\n"
     "[color=#1E3A8A]MIS-C[/color]\n"
     "• IVIG commonly 2 g/kg. Corticosteroids commonly used (e.g., Methylprednisolone 1–2 mg/kg/day IV).\n"
     "• Monitor BP, fluid balance, cardiac function, thrombosis risk."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay KD treatment while waiting for day 5 of fever when strongly suspected.\n"
     "• Exclude or treat dangerous infectious mimics (sepsis, toxic shock).\n"
     "• Avoid excessive IVIG volume in myocardial dysfunction."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for specialist assessment and cardiac evaluation. ICU for shock, significant dysfunction, or rapid deterioration."),
    ("REFERENCES", "info", "CDC Kawasaki Disease; CDC MIS-C.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Severe Malaria in Children")] = [
    ("01 — RECOGNIZE", "info", 
     "Fever in child living in/returning from endemic area + any of:\n"
     "• Altered consciousness/coma, repeated seizures.\n"
     "• Respiratory distress, deep breathing, acidosis.\n"
     "• Shock, poor perfusion. Severe anemia/hemoglobinuria. Hypoglycemia. AKI. Jaundice. Bleeding.\n"
     "• [color=#991B1B]Important:[/color] A negative rapid diagnostic test does not always exclude malaria if suspicion is high."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE. Check bedside glucose immediately; correct hypoglycemia.\n"
     "• Obtain IV/IO access. Monitor ECG, SpO2, temp, BP, mental status, urine output.\n"
     "• Obtain urgent malaria testing (thick/thin films).\n"
     "• Treat seizures/respiratory failure promptly.\n"
     "• Avoid routine large fluid boluses (vulnerable to fluid overload). Give fluids according to perfusion/losses.\n"
     "• Contact pediatric/infectious disease team urgently."),
    ("03 — INVESTIGATIONS", "info", 
     "• Rapid test and thick/thin smear (parasite density).\n"
     "• CBC, bedside glucose, electrolytes, renal/liver function, bilirubin.\n"
     "• Blood gas/lactate. Blood group/crossmatch if severe anemia. Blood cultures if sepsis possible."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Artesunate (First-Line)[/color]\n"
     "• WHO: < 20 kg = 3 mg/kg/dose; ≥ 20 kg = 2.4 mg/kg/dose. Give at 0, 12, 24 hours, then daily.\n"
     "• Once tolerating oral meds, complete with full oral ACT (Artemisinin-based combination therapy).\n"
     "• Artesunate alone is NOT the complete treatment course.\n\n"
     "[color=#1E3A8A]Hypoglycemia[/color]\n"
     "• 10% dextrose 2.5 mL/kg IV. Recheck glucose promptly and frequently.\n\n"
     "[color=#1E3A8A]Supportive[/color]\n"
     "• Treat seizures (status epilepticus protocol). Support ventilation. Manage severe anemia/AKI."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay antimalarial treatment while awaiting nonessential tests.\n"
     "• Do not use oral treatment alone for severe malaria.\n"
     "• Hypoglycemia may recur, particularly during quinine treatment."),
    ("06 — DISPOSITION", "warning", 
     "• All children with severe malaria require hospital admission and close monitoring.\n"
     "• ICU-level care for coma, recurrent seizures, shock, respiratory failure, or major organ dysfunction."),
    ("REFERENCES", "info", "WHO Guidelines for Malaria; CDC Treatment of Severe Malaria.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Acute Rheumatic Fever and Rheumatic Carditis")] = [
    ("01 — RECOGNIZE", "info", 
     "Usually school-aged. Develops 1–5 weeks after GAS pharyngitis.\n"
     "• Migratory polyarthritis (large joints).\n"
     "• Carditis: Tachycardia out of proportion, new murmur, cardiomegaly, heart failure, pericardial involvement.\n"
     "• Sydenham chorea (involuntary movements, emotional lability).\n"
     "• Erythema marginatum, subcutaneous nodules."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, signs of heart failure.\n"
     "• Obtain ECG and urgent echocardiography.\n"
     "• Treat acute heart failure per pediatric protocol.\n"
     "• Seek pediatric and cardiology consultation.\n"
     "• Consider infective endocarditis, septic arthritis, JIA, myocarditis."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, ESR, CRP.\n"
     "• ECG (PR interval). Echocardiography with Doppler.\n"
     "• Evidence of preceding strep: throat culture, ASO or anti-DNase B.\n"
     "• Apply revised Jones criteria (taking local risk into account)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Eradication of GAS[/color]\n"
     "• Benzathine benzylpenicillin G IM single dose: < 27 kg = 600,000 units IM; ≥ 27 kg = 1.2 million units IM.\n"
     "• [color=#991B1B]Never administer IV.[/color] Clarify penicillin allergy.\n\n"
     "[color=#1E3A8A]Anti-inflammatory (Arthritis)[/color]\n"
     "• Aspirin or other anti-inflammatory under specialist supervision.\n\n"
     "[color=#1E3A8A]Carditis/Heart Failure[/color]\n"
     "• Admit. Manage pulmonary edema/heart failure per pediatric cardiac protocol.\n\n"
     "[color=#1E3A8A]Secondary Prophylaxis[/color]\n"
     "• Long-term antibiotic prophylaxis required to reduce recurrence."),
    ("05 — WARNINGS", "danger", 
     "• Benzathine penicillin G must never be administered intravenously.\n"
     "• Do not assume resolution of joint symptoms means carditis has resolved.\n"
     "• Avoid unsupervised aspirin in suspected viral illness (Reye syndrome)."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for suspected carditis, heart failure, severe arthritis, chorea, or diagnostic uncertainty.\n"
     "• Establish documented secondary prophylaxis plan before discharge."),
    ("REFERENCES", "info", "WHO Guideline; CDC Acute Rheumatic Fever.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Epiglottitis and Bacterial Tracheitis")] = [
    ("01 — RECOGNIZE", "info", 
     "[color=#1E3A8A]Epiglottitis:[/color] Sudden fever, severe sore throat, toxic appearance, drooling, muffled voice, tripod positioning, respiratory distress, stridor (critical obstruction).\n"
     "[color=#1E3A8A]Bacterial Tracheitis:[/color] High fever, toxic, cough, stridor, distress. May follow viral URI/croup. Thick purulent secretions. Poor response to usual croup therapy is a warning."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call most experienced airway clinician, anesthetist, and pediatric/ENT team immediately.\n"
     "• Keep child calm, in position of comfort. Provide oxygen minimizing distress.\n"
     "• Do NOT force child to lie flat or open mouth for exam.\n"
     "• Avoid tongue-depressor exam, throat swabs, IV attempts, or imaging that may agitate before safe airway plan.\n"
     "• Prepare for controlled airway management."),
    ("03 — INVESTIGATIONS", "info", 
     "• Prioritize clinical assessment and airway safety over diagnostic tests.\n"
     "• Once airway is secure: CBC, inflammatory markers, blood cultures, airway cultures.\n"
     "• Imaging only if it will not delay or jeopardize airway management."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Airway Management[/color]\n"
     "• Airway meds/induction agents selected by experienced airway team. Secure airway in controlled setting.\n"
     "• Plan for difficult ventilation and emergency surgical-airway contingencies.\n\n"
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Suspected epiglottitis: IV ceftriaxone or cefotaxime (e.g., Ceftriaxone 50 mg/kg IV every 24 hours).\n"
     "• Add anti-staphylococcal coverage for tracheitis/MRSA suspected.\n\n"
     "[color=#1E3A8A]Adjunctive[/color]\n"
     "• Nebulized epinephrine may temporarily reduce edema (do not delay airway management). Corticosteroids per team protocol."),
    ("05 — WARNINGS", "danger", 
     "• Sedation or examination that causes agitation can precipitate complete airway obstruction.\n"
     "• Antibiotics do not replace airway stabilization.\n"
     "• Do not delay treatment for imaging or cultures in a critically ill child."),
    ("06 — DISPOSITION", "warning", 
     "• Suspected epiglottitis requires emergency specialist assessment and usually hospital admission.\n"
     "• Airway compromise/tracheitis/intubation requires ICU-level monitoring."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; CDC Haemophilus influenzae.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Severe Anemia and Acute Hemolytic Crisis")] = [
    ("01 — RECOGNIZE", "info", 
     "• Marked pallor, fatigue, weakness, dizziness, syncope.\n"
     "• Tachycardia, tachypnea, flow murmur. Severe: altered consciousness, shock, distress, heart failure.\n"
     "• Acute hemolysis: jaundice, dark urine, sudden fall in Hb.\n"
     "• Splenic sequestration: sudden pallor, abdominal distension, splenomegaly, shock.\n"
     "• Consider malaria, nutritional deficiency, hemoglobinopathies, G6PD, autoimmune hemolysis, marrow suppression, acute blood loss."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, mental status. Continuous monitoring in unstable patients.\n"
     "• Check bedside glucose. Obtain urgent CBC.\n"
     "• Assess for bleeding, jaundice, splenomegaly, heart failure.\n"
     "• Send blood group and crossmatch early.\n"
     "• Treat shock according to cause (avoid indiscriminate fluid boluses due to overload risk).\n"
     "• Investigate/treat malaria promptly. Contact hematology for suspected hemolytic crisis."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC with indices/platelets. Reticulocyte count, blood film.\n"
     "• Blood group, antibody screen, crossmatch.\n"
     "• Bilirubin, LDH, renal function, electrolytes, urinalysis. DAT if immune hemolysis.\n"
     "• Malaria test/smear. Iron studies, Hb electrophoresis, G6PD testing based on timing/cause."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Packed Red Blood Cell Transfusion[/color]\n"
     "• Guided by Hb, symptoms, hemodynamics, ongoing loss.\n"
     "• Initial PRBC volume commonly 10 mL/kg, followed by reassessment. Use local protocol.\n"
     "• Children with chronic severe anemia are vulnerable to overload. Avoid rapid/excessive transfusion.\n\n"
     "[color=#1E3A8A]Treat Underlying Cause[/color]\n"
     "• Iron deficiency: Oral iron 3–6 mg/kg/day elemental iron after stabilization.\n"
     "• Malaria: Prompt antimalarial testing/treatment.\n"
     "• Acute hemolysis: Stop suspected causative med. Maintain renal perfusion.\n"
     "• Splenic sequestration: Emergency hematology assessment and carefully managed transfusion."),
    ("05 — WARNINGS", "danger", 
     "• Stop transfusion immediately and initiate transfusion-reaction protocol if serious reaction suspected.\n"
     "• Do not delay lifesaving transfusion in a child with life-threatening anemia and instability.\n"
     "• In sickle cell disease, avoid excessive hemoglobin elevation; consult protocol."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for instability, respiratory distress, heart failure, acute hemolysis, sequestration, active bleeding, severe malaria, or need for urgent transfusion."),
    ("REFERENCES", "info", "AAP Iron Deficiency; WHO Manual for Health Care of Children; WHO Malaria.")
]


# ==================== NEONATAL EMERGENCIES (TOPICS 1-10) ====================

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Resuscitation at Birth")] = [
    ("01 — RECOGNIZE", "info", 
     "Neonatal resuscitation is required when a newborn fails to establish effective spontaneous breathing or has persistent bradycardia after birth.\n"
     "• Assess: Gestational age, muscle tone, spontaneous breathing/crying, heart rate, respiratory effort.\n"
     "• Apnea or gasping. Heart rate < 100 bpm. Persistent cyanosis/hypoxemia. Poor respiratory effort.\n"
     "• Heart rate < 60 bpm despite effective ventilation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for neonatal resuscitation assistance.\n"
     "• Provide warmth and maintain temperature.\n"
     "• Position head in neutral/slightly extended position. Dry and provide gentle tactile stimulation.\n"
     "• Clear airway only if obstruction is suspected; routine suctioning not recommended.\n"
     "• Assess heart rate and breathing promptly.\n"
     "• Begin positive-pressure ventilation (PPV) within first 60 seconds if apnea, gasping, or HR < 100/min.\n"
     "• Attach preductal pulse oximeter (right hand/wrist) and ECG monitoring."),
    ("03 — TREATMENT: PPV", "info", 
     "[color=#1E3A8A]Indication:[/color] Apnea, gasping, or HR < 100/min despite initial steps.\n"
     "• Provide 30–60 inflations/min. Initial peak inflation pressure commonly 20–30 cm H2O.\n"
     "• Assess heart rate response and chest movement.\n"
     "• If HR does not improve, correct mask seal, head position, airway obstruction, and ventilation technique.\n"
     "• [color=#991B1B]Effective ventilation is the most important intervention. Do NOT proceed to chest compressions before ensuring ventilation is effective.[/color]"),
    ("04 — TREATMENT: Oxygen", "info", 
     "• Term/late-preterm: begin with 21% oxygen.\n"
     "• Preterm: select initial concentration per gestational age and protocol.\n"
     "• Titrate using preductal pulse oximetry.\n"
     "• Target preductal SpO2: 1 min (60-65%), 2 min (65-70%), 3 min (70-75%), 4 min (75-80%), 5 min (80-85%), 10 min (85-95%).\n"
     "• Avoid unnecessary hyperoxia."),
    ("05 — TREATMENT: Compressions & Epinephrine", "info", 
     "[color=#1E3A8A]Chest Compressions[/color]\n"
     "• Indication: HR < 60/min after at least 30 seconds of effective ventilation.\n"
     "• Two-thumb encircling-hands technique. Lower third of sternum.\n"
     "• 3:1 ratio (90 compressions, 30 ventilations/min). Increase O2 to 100%.\n\n"
     "[color=#1E3A8A]Epinephrine[/color]\n"
     "• Indication: HR < 60/min despite optimized ventilation and compressions.\n"
     "• IV/Umbilical dose: 0.01–0.03 mg/kg (0.1–0.3 mL/kg of 0.1 mg/mL solution).\n"
     "• Endotracheal route (if vascular access pending): 0.05–0.1 mg/kg.\n"
     "• Repeat every 3–5 minutes if HR < 60/min.\n"
     "• [color=#991B1B]Do NOT confuse 0.1 mg/mL with 1 mg/mL epinephrine (tenfold error).[/color]\n\n"
     "[color=#1E3A8A]Volume Expansion[/color]\n"
     "• Suspected blood loss/hypovolemia: 0.9% NaCl or blood products, 10 mL/kg cautiously."),
    ("06 — DISPOSITION", "warning", 
     "• Newborns requiring prolonged ventilation, chest compressions, epinephrine, or advanced resuscitation require close post-resuscitation monitoring and NICU care."),
    ("REFERENCES", "info", "AHA/AAP Neonatal Resuscitation Guidelines (2025).")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Respiratory Distress and Failure")] = [
    ("01 — RECOGNIZE", "info", 
     "May result from RDS, TTN, pneumonia, meconium aspiration, pneumothorax, CHD, or PPHN.\n"
     "• RR > 60/min. Grunting. Nasal flaring. Chest retractions. Central cyanosis. Apnea.\n"
     "• Persistent hypoxemia. Poor feeding, lethargy, temperature instability.\n"
     "• Impending failure: Apnea/gasping, worsening hypoxemia, exhaustion, bradycardia, altered consciousness."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and temperature. Position airway appropriately.\n"
     "• Continuous pulse oximetry and cardiorespiratory monitoring. Check bedside glucose.\n"
     "• Provide oxygen when indicated, titrate to target.\n"
     "• Initiate CPAP in a spontaneously breathing infant with appropriate indications.\n"
     "• Begin assisted ventilation for apnea, gasping, or inadequate ventilation.\n"
     "• Consider pneumothorax, sepsis, CHD, metabolic disease if deteriorating."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Supplemental Oxygen[/color]\n"
     "• Use lowest concentration to achieve target (e.g., 90–94% in many preterm infants post-stabilization).\n\n"
     "[color=#1E3A8A]B. CPAP[/color]\n"
     "• Starting pressure ~5–6 cm H2O. Appropriately fitted interface. Monitor work of breathing, O2 requirement, blood gas, abdominal distension.\n"
     "• Not appropriate as sole support for apneic infant or severe failure.\n\n"
     "[color=#1E3A8A]C. Positive-Pressure Ventilation[/color]\n"
     "• For apnea, gasping, or inadequate effort. Monitor chest movement, HR, SpO2.\n\n"
     "[color=#1E3A8A]D. Surfactant Therapy[/color]\n"
     "• For preterm RDS. Administer via approved airway technique by trained personnel.\n\n"
     "[color=#1E3A8A]E. Investigate and Treat Cause[/color]\n"
     "• Suspected infection: cultures and empiric antibiotics. Pneumothorax: urgent decompression if tension. CHD: urgent cardiac assessment."),
    ("04 — DISPOSITION", "warning", 
     "• Admit infants with persistent distress, O2 requirement, apnea, suspected infection, or need for CPAP/ventilation to NICU."),
    ("REFERENCES", "info", "WHO Recommendations; AHA/AAP Guidelines (2025).")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Shock and Poor Perfusion")] = [
    ("01 — RECOGNIZE", "info", 
     "Inadequate tissue perfusion. Hypotension is a late finding.\n"
     "• Causes: Sepsis, hypovolemia/blood loss, myocardial dysfunction, PPHN, duct-dependent CHD, pneumothorax.\n"
     "• Prolonged cap refill. Weak pulses. Cool/mottled extremities. Tachycardia/bradycardia.\n"
     "• Reduced urine output. Lethargy/poor feeding. Metabolic acidosis/elevated lactate. Hypotension (late)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for neonatal/critical care assistance. Assess ABCs, temperature.\n"
     "• Provide respiratory support and oxygen. Obtain IV/umbilical venous access.\n"
     "• Check glucose immediately. Obtain blood gas, lactate, cultures, relevant labs.\n"
     "• Start empiric antibiotics promptly if sepsis suspected.\n"
     "• Assess shock type (hypovolemia, sepsis, cardiac, obstructive) before repeated fluid boluses.\n"
     "• Arrange urgent echocardiography if cardiac dysfunction/duct-dependent disease possible."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Fluid Resuscitation[/color]\n"
     "• Suspected hypovolemic shock: cautious initial bolus 10 mL/kg, immediate reassessment.\n"
     "• Repeat only if evidence of ongoing fluid-responsive shock and no fluid overload/cardiac failure.\n"
     "• [color=#991B1B]Repeated boluses may worsen respiratory failure or myocardial dysfunction.[/color]\n\n"
     "[color=#1E3A8A]B. Suspected Septic Shock[/color]\n"
     "• Blood cultures if no delay. Appropriate IV antibiotics per local guidance. Do NOT delay in unstable infant.\n\n"
     "[color=#1E3A8A]C. Vasoactive Support[/color]\n"
     "• If perfusion inadequate after initial management, initiate specialist-directed vasoactive therapy (Epinephrine, Dopamine, etc., per shock phenotype and local protocol).\n"
     "• Monitor ECG, BP, perfusion, urine output, glucose, lactate, extravasation risk.\n\n"
     "[color=#1E3A8A]D. Correct Reversible Causes[/color]\n"
     "• Hypoglycemia, blood loss/anemia, pneumothorax, duct-dependent CHD."),
    ("04 — DISPOSITION", "warning", 
     "• All suspected shock require urgent hospital management. Persistent shock, vasoactive support, severe acidosis, or organ dysfunction requires NICU."),
    ("REFERENCES", "info", "WHO Guidance; Local NICU Guidelines.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Hypothermia and Temperature Instability")] = [
    ("01 — RECOGNIZE", "info", 
     "Neonates (especially preterm/LBW) lose heat rapidly.\n"
     "• Normal: 36.5–37.5°C. Cold stress: < 36.5°C. Moderate: 32.0–35.9°C. Severe: < 32.0°C.\n"
     "• Cold skin/low temp. Poor feeding. Lethargy/weak cry. Respiratory distress/apnea. Hypoglycemia. Bradycardia. Poor perfusion/acidosis.\n"
     "• Temperature instability may be a sign of sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Confirm temperature with neonatal thermometer. Assess ABCs and glucose.\n"
     "• Remove wet clothing, dry infant. Begin controlled rewarming.\n"
     "• Use radiant warmer or incubator. Monitor temperature frequently.\n"
     "• Investigate for infection, hypoglycemia, respiratory disease."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Thermal Support[/color]\n"
     "• Target 36.5–37.5°C. Radiant warmer for rapid access; incubator for ongoing control.\n"
     "• Preterm immediately after birth: plastic wrap/bag without prior drying + head cover per protocol.\n"
     "• [color=#991B1B]Do NOT use direct high-temperature heat sources, hot-water bottles, or uncontrolled heating.[/color]\n\n"
     "[color=#1E3A8A]B. Glucose Management[/color]\n"
     "• Check glucose promptly, treat hypoglycemia per protocol.\n\n"
     "[color=#1E3A8A]C. Evaluate for Sepsis[/color]\n"
     "• Consider infection with hypothermia + poor feeding/respiratory distress/lethargy/apnea. Obtain cultures, start empiric antibiotics if indicated.\n\n"
     "[color=#1E3A8A]D. Rewarming in Severe Hypothermia[/color]\n"
     "• Controlled rewarming with continuous monitoring. Manage apnea, bradycardia, hypoglycemia, shock. Requires specialist neonatal care."),
    ("04 — DISPOSITION", "warning", 
     "• Admit for persistent hypothermia, hypoglycemia, respiratory symptoms, poor feeding, suspected infection, or abnormal perfusion. Preterm/LBW may need ongoing incubator care."),
    ("REFERENCES", "info", "WHO Recommendations for Newborn Thermal Care.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Bradycardia and Cardiac Arrest")] = [
    ("01 — RECOGNIZE", "info", 
     "Neonatal bradycardia may result from hypoxia, hypothermia, respiratory failure, sepsis, metabolic abnormalities, CHD, or medications.\n"
     "• HR below expected range. Apnea/inadequate breathing. Cyanosis/hypoxemia. Poor perfusion/weak pulses.\n"
     "• Altered responsiveness. Cardiac arrest with absent effective circulation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for resuscitation assistance. Assess ABCs and temperature.\n"
     "• Provide effective ventilation for apnea/inadequate breathing. Attach ECG and SpO2.\n"
     "• Check glucose and consider reversible causes.\n"
     "• Follow appropriate neonatal resuscitation or pediatric life support algorithm based on age and setting."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Bradycardia During Resuscitation at Birth[/color]\n"
     "• Apnea/gasping/HR < 100: Provide effective PPV.\n"
     "• HR < 60 despite 30s effective ventilation: Initiate coordinated chest compressions.\n"
     "• HR < 60 after ~60s of compressions + ventilation: Administer epinephrine per neonatal algorithm (0.01–0.03 mg/kg IV/umbilical of 0.1 mg/mL solution).\n\n"
     "[color=#1E3A8A]B. Bradycardia After Initial Birth Transition[/color]\n"
     "• Support oxygenation/ventilation. Treat hypoxemia, hypothermia, hypoglycemia, sepsis, electrolytes.\n"
     "• Urgent neonatal/pediatric critical care support.\n"
     "• Cardiopulmonary arrest/persistent severe bradycardia with poor perfusion: Use age-appropriate resuscitation algorithm.\n"
     "• [color=#991B1B]Do NOT automatically apply delivery-room 3:1 algorithm to an older neonate who deteriorated later. Follow appropriate protocol.[/color]\n\n"
     "[color=#1E3A8A]C. Treat Underlying Cause[/color]\n"
     "• Hypoxemia, hypothermia, hypoglycemia, hyperkalemia, CHD, sepsis."),
    ("04 — DISPOSITION", "warning", 
     "• Persistent bradycardia, cardiac arrest, significant O2 requirement, or hemodynamic instability requires NICU/appropriate critical care."),
    ("REFERENCES", "info", "AHA/AAP Neonatal Resuscitation Guidelines (2025).")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Early-Onset and Late-Onset Neonatal Sepsis")] = [
    ("01 — RECOGNIZE", "info", 
     "Potentially life-threatening systemic infection. Signs may be subtle/nonspecific.\n"
     "• EOS: First 72 hours (some use 48h). Risk factors: maternal GBS, intra-amniotic infection, maternal fever, prolonged ROM, prematurity.\n"
     "• LOS: After early period. Risk factors: prematurity, prolonged hospitalization, central lines, mechanical ventilation, parenteral nutrition.\n"
     "• Indicators: Temp instability, poor feeding, vomiting, lethargy, apnea, grunting, tachypnea, tachycardia/bradycardia, poor perfusion, abdominal distension, jaundice, seizures, hypo/hyperglycemia.\n"
     "• [color=#991B1B]Normal temp, CBC, or initial CRP does NOT exclude neonatal sepsis.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temperature, neuro status. Provide O2/respiratory support.\n"
     "• Establish IV access (IO if urgent). Check bedside glucose, correct hypoglycemia.\n"
     "• Obtain blood culture before antibiotics if no meaningful delay.\n"
     "• Obtain CBC, CRP/PCT per protocol, blood gas, lactate, glucose, electrolytes, renal function.\n"
     "• Start empiric IV antibiotics promptly (ideally within 1 hour).\n"
     "• Assess for meningitis, pneumonia, UTI, omphalitis, NEC. Monitor vitals, perfusion, urine output."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric Antibiotics: EOS[/color]\n"
     "• Common regimen: IV benzylpenicillin + gentamicin (or ampicillin + gentamicin).\n"
     "• Benzylpenicillin sodium: 25 mg/kg IV every 12 hours (NICE; interval shortened if severely ill).\n"
     "• Gentamicin: 5 mg/kg IV starting dose (NICE); subsequent intervals based on GA, postnatal age, renal function, TDM.\n"
     "• [color=#991B1B]Confirm exact penicillin formulation/units. Do not confuse benzylpenicillin with benzathine penicillin. Never assume same gentamicin interval for all neonates.[/color]\n\n"
     "[color=#1E3A8A]Empiric Antibiotics: LOS[/color]\n"
     "• Hospital-acquired: Base on unit antibiogram, previous cultures, device exposure (e.g., flucloxacillin + gentamicin). Modify for MRSA/resistant Gram-negatives.\n"
     "• Community-presenting: Use locally recommended regimen (may differ from hospital-acquired).\n"
     "• Meningitis/NEC: Use regimen covering suspected diagnosis (additional anaerobic coverage for NEC).\n\n"
     "[color=#1E3A8A]Supportive Treatment[/color]\n"
     "• Normothermia, correct glucose/electrolytes, respiratory support, cautious fluids, vasoactive support if shock persists.\n"
     "• Review cultures daily; narrow/adjust/stop antibiotics when justified."),
    ("04 — DISPOSITION", "warning", 
     "• Admit any neonate with suspected systemic infection for urgent assessment/monitored treatment.\n"
     "• Transfer to NICU for apnea, respiratory failure, shock, seizures, significant metabolic abnormalities.\n"
     "• Antibiotic duration depends on cultures, course, site. Do not use single duration for every case."),
    ("REFERENCES", "info", "NICE NG195 (2026); Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Meningitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Emergency because deterioration can be rapid and long-term neuro complications possible.\n"
     "• Poor feeding, lethargy, irritability, reduced responsiveness. Temp instability.\n"
     "• Apnea, respiratory distress, unexplained bradycardia. Seizures/abnormal movements.\n"
     "• Bulging fontanelle (not always present). Abnormal tone, weak cry, persistent vomiting.\n"
     "• Signs of sepsis/shock. Organisms: GBS, E. coli, Listeria, healthcare-associated. Consider HSV.\n"
     "• Consider neonatal HSV when seizures, vesicular lesions, hepatitis, encephalitis, or compatible maternal history."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize ABCs. Check glucose immediately, treat hypoglycemia.\n"
     "• Obtain blood culture and appropriate blood tests.\n"
     "• Perform lumbar puncture if safe and no delay to antibiotics.\n"
     "• Start empiric IV antibiotics urgently.\n"
     "• Treat seizures promptly (neonatal protocol).\n"
     "• Consider HSV investigations and empiric acyclovir when indicated.\n"
     "• [color=#991B1B]Do NOT perform LP immediately if uncontrolled seizures, significant cardiorespiratory instability, shock requiring stabilization. Stabilize first, do NOT delay antibiotics.[/color]"),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Must cover likely neonatal pathogens and achieve adequate CSF penetration.\n"
     "• NICE recommends IV amoxicillin + cefotaxime for suspected meningitis in neonatal-unit patients when pathogen unknown.\n"
     "• Use meningitis-specific doses from local formulary (do NOT substitute routine sepsis dose).\n"
     "• [color=#991B1B]Do NOT use ceftriaxone routinely in neonates without checking contraindications (hyperbilirubinemia, IV calcium exposure). Cefotaxime often preferred.[/color]\n\n"
     "[color=#1E3A8A]Organism-Directed Treatment[/color]\n"
     "• Adjust antibiotics when CSF/blood cultures identify pathogen. Obtain microbiology advice for resistant organisms. Treatment usually prolonged.\n\n"
     "[color=#1E3A8A]Seizures and Raised ICP[/color]\n"
     "• Treat seizures (neonatal protocol). Maintain oxygenation, glucose, temp, electrolytes. Avoid routine fluid restriction without assessment. Seek urgent advice for raised ICP."),
    ("04 — DISPOSITION", "warning", 
     "• Admit to neonatal unit; intensive care for seizures, shock, apnea, respiratory failure, reduced consciousness.\n"
     "• Arrange hearing assessment and neurodevelopmental follow-up after confirmed meningitis."),
    ("REFERENCES", "info", "NICE NG195; NICE NG240.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Pneumonia")] = [
    ("01 — RECOGNIZE", "info", 
     "May occur early after birth or later (hospital/community). Can coexist with neonatal sepsis.\n"
     "• Tachypnea, grunting, nasal flaring, chest recession. Apnea/cyanosis. Increasing O2 requirement.\n"
     "• Poor feeding, lethargy, temp instability. Crackles/reduced air entry.\n"
     "• Poor perfusion/hypotension in severe infection.\n"
     "• Differentials: RDS, TTN, meconium aspiration, pneumothorax, PPHN, CHD."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temperature. Monitor SpO2 and cardiorespiratory status.\n"
     "• Provide O2, CPAP, or ventilation per severity and local guidance.\n"
     "• Check glucose, obtain blood gas if significant distress.\n"
     "• Obtain blood culture before antibiotics if feasible without delay.\n"
     "• Start empiric IV antibiotics per EOS/LOS guidance.\n"
     "• Assess for pneumothorax and other causes of sudden deterioration."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Respiratory Support[/color]\n"
     "• Oxygen: Titrate to target saturation specified by neonatal unit. Avoid hypoxemia/hyperoxia.\n"
     "• CPAP/Ventilation: Settings per gestation, weight, lung mechanics, oxygenation, blood gas. Monitor SpO2, effort, apnea, blood gas, hemodynamics.\n"
     "• [color=#991B1B]Sudden deterioration requires immediate assessment for pneumothorax, tube displacement, or equipment failure.[/color]\n\n"
     "[color=#1E3A8A]Antibiotic Treatment[/color]\n"
     "• Use local neonatal sepsis regimen (EOS vs LOS, local resistance).\n"
     "• EOS example: benzylpenicillin + gentamicin. LOS: base on unit antibiogram.\n"
     "• Review cultures/clinical response to avoid unnecessarily broad/prolonged treatment.\n\n"
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Maintain normothermia, glucose, fluids/nutrition. Treat associated sepsis/shock. Consider surfactant only for appropriate indication (e.g., coexisting RDS)."),
    ("04 — DISPOSITION", "warning", 
     "• Admit for monitored neonatal care. Escalate to intensive care for increasing respiratory support, recurrent apnea, severe acidosis, shock, or persistent hypoxemia.\n"
     "• Determine antibiotic duration from cultures/clinical progress, not radiographic findings alone."),
    ("REFERENCES", "info", "NICE NG195; Royal Children's Hospital Melbourne.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Omphalitis and Umbilical Sepsis")] = [
    ("01 — RECOGNIZE", "info", 
     "Infection of umbilical stump and surrounding tissues. May progress rapidly to bacteremia, septic shock, or necrotizing soft-tissue infection.\n"
     "• Redness extending onto surrounding abdominal skin. Warmth, swelling, tenderness around umbilicus.\n"
     "• Purulent/foul-smelling discharge. Induration, skin discoloration, blistering, necrosis.\n"
     "• Fever/hypothermia, poor feeding, lethargy, respiratory instability.\n"
     "• [color=#991B1B]Red flags:[/color] Rapidly spreading erythema, severe swelling/pain out of proportion, crepitus, bullae, dusky skin, necrosis, abdominal distension, poor perfusion, altered responsiveness. Requires urgent surgical assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temp, perfusion, glucose. Inspect umbilicus/surrounding skin carefully.\n"
     "• Obtain blood culture before antibiotics if no delay. Obtain sample of purulent discharge for culture.\n"
     "• Start IV antibiotics promptly.\n"
     "• Assess for systemic sepsis, abdominal wall involvement, abscess, necrotizing infection.\n"
     "• Obtain urgent surgical consult for rapid progression, necrosis, crepitus, or suspected deep infection.\n"
     "• Monitor closely for deterioration."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IV Antibiotic Therapy[/color]\n"
     "• Cover Staph aureus, streptococci, relevant Gram-negatives. Select per severity, local resistance, formulary.\n"
     "• Add MRSA-active treatment if risk factors/local epidemiology warrant.\n"
     "• Modify based on culture/clinical response.\n"
     "• [color=#991B1B]Do NOT use topical treatment or oral antibiotics alone for clinically significant omphalitis.[/color]\n\n"
     "[color=#1E3A8A]Local Care[/color]\n"
     "• Clean technique, keep area clean/dry. Avoid unprescribed powders, herbal preparations, caustic substances.\n"
     "• Do NOT squeeze or probe stump. Follow neonatal unit infection-control protocol."),
    ("04 — DISPOSITION", "warning", 
     "• Admit neonates with suspected omphalitis for urgent medical assessment and usually parenteral antibiotics.\n"
     "• Intensive care may be required for shock, organ dysfunction, or rapidly progressive infection.\n"
     "• Obtain surgical review for suspected abscess, necrotizing infection, or deep extension."),
    ("REFERENCES", "info", "Botswana Neonatal Guidelines; NICE NG195.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Circulatory and cellular dysfunction due to infection. Hypotension may be late.\n"
     "• Prolonged cap refill. Cool/mottled extremities or warm vasodilated extremities. Weak pulses.\n"
     "• Tachycardia/bradycardia. Reduced urine output. Lethargy/altered responsiveness/seizures.\n"
     "• Metabolic acidosis/elevated lactate. Hypotension (advanced)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call NICU team and activate local sepsis/shock pathway.\n"
     "• Assess airway/breathing; provide O2/respiratory support.\n"
     "• Establish IV/emergency IO access. Check glucose, blood gas, lactate, electrolytes, perfusion.\n"
     "• Obtain blood culture if no delay.\n"
     "• Give empiric IV antibiotics urgently (ideally within 1 hour).\n"
     "• Assess fluid responsiveness/cardiac dysfunction/pulmonary edema.\n"
     "• Administer carefully titrated isotonic crystalloid boluses only when indicated, reassess after each.\n"
     "• Start vasoactive support promptly when shock persists or fluids unsafe/ineffective."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Select per suspected source, EOS/LOS, local antibiogram, previous cultures. Use meningitis-specific treatment if suspected. Reassess/tailor when microbiology available.\n"
     "• [color=#991B1B]Shock is not a reason to use unverified doses. Confirm high-risk medication calculations with another clinician.[/color]\n\n"
     "[color=#1E3A8A]Fluid Resuscitation[/color]\n"
     "• If hypovolemia/fluid responsiveness suspected: cautious 10 mL/kg bolus under specialist guidance. Reassess after every bolus.\n"
     "• [color=#991B1B]Do NOT automatically give repeated large-volume boluses. Preterm and myocardial dysfunction particularly vulnerable to overload.[/color]\n\n"
     "[color=#1E3A8A]Vasoactive Support[/color]\n"
     "• Persistent poor perfusion/hypotension despite initial treatment. Early treatment may be required if further fluid unsafe.\n"
     "• Epinephrine or norepinephrine per shock phenotype and specialist guidance. Use neonatal weight-based infusion protocol.\n"
     "• Monitor ECG, BP, cap refill, pulses, lactate, urine output, glucose, perfusion. Titrate per protocol.\n"
     "• [color=#991B1B]Never administer continuous vasoactive infusion without verified concentration and pump calculation.[/color]\n\n"
     "[color=#1E3A8A]Additional Supportive Care[/color]\n"
     "• Correct glucose/electrolytes, maintain temp, treat respiratory failure/apnea. Consider hydrocortisone only for refractory shock after specialist assessment.\n"
     "• Identify/control source (infected catheters, surgical pathology)."),
    ("04 — DISPOSITION", "warning", 
     "• All neonates with septic shock require immediate NICU and continuous monitoring.\n"
     "• Urgent transfer to higher-level NICU if advanced support unavailable."),
    ("REFERENCES", "info", "NICE NG195; Local NICU Protocols.")
]


# ==================== NEONATAL EMERGENCIES (TOPICS 11-20) ====================

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Hypoglycemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Jitteriness, tremors, poor feeding, lethargy, hypotonia, apnea, cyanosis, seizures, or altered consciousness.\n"
     "• Risk factors: prematurity, small/large for gestational age, infant of diabetic mother, hypothermia, sepsis, perinatal stress.\n"
     "• Symptoms may be absent despite low glucose."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and check bedside blood glucose immediately.\n"
     "• Treat symptomatic or severely low glucose without waiting for lab confirmation.\n"
     "• Obtain lab confirmation when feasible, but do NOT delay treatment.\n"
     "• Check temperature and assess for sepsis or other causes.\n"
     "• Recheck glucose after treatment according to neonatal protocol."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Asymptomatic infant who can feed[/color]\n"
     "• Feed promptly with breast milk or appropriate alternative per local pathway.\n"
     "• Buccal 40% dextrose gel, 0.5 mL/kg (200 mg/kg), may be used in eligible infants.\n"
     "• Recheck glucose at protocol-defined interval (commonly ~30 minutes after intervention).\n\n"
     "[color=#1E3A8A]B. Symptomatic or severe hypoglycemia[/color]\n"
     "• 10% dextrose IV, 2 mL/kg (200 mg/kg) as initial bolus when indicated by neonatal protocol.\n"
     "• Start continuous glucose infusion (initial GIR ~5–8 mg/kg/min; individual requirements vary).\n"
     "• Recheck glucose ~30 minutes after treatment or as directed. Adjust GIR per serial measurements.\n"
     "• Monitor IV access, fluid volume, electrolytes."),
    ("04 — WARNINGS", "danger", 
     "• Do not rely on feeding or gel alone for an infant with seizures, apnea, impaired consciousness, or other severe symptoms.\n"
     "• Avoid excessive or repeated dextrose boluses without reassessment.\n"
     "• Persistent/recurrent hypoglycemia requires investigation for hyperinsulinism, endocrine disease, or inborn error of metabolism."),
    ("05 — DISPOSITION", "warning", 
     "• Admit infants requiring IV glucose or with recurrent, severe, or symptomatic hypoglycemia.\n"
     "• Ensure stable glucose during an appropriate feeding interval before discharge."),
    ("REFERENCES", "info", "British Association of Perinatal Medicine; Local neonatal hypoglycemia protocol.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Seizures")] = [
    ("01 — RECOGNIZE", "info", 
     "Repetitive focal clonic movements, tonic posturing, abnormal eye deviation, oral automatisms, or stereotyped autonomic changes.\n"
     "• Many neonatal seizures are subtle or electrographic-only.\n"
     "• Common causes: HIE, stroke, intracranial hemorrhage, infection, hypoglycemia, electrolyte disturbances, or metabolic disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation. Check glucose immediately and correct hypoglycemia.\n"
     "• Monitor ECG, SpO2, temperature, BP. Obtain IV access.\n"
     "• Treat prolonged or recurrent seizures promptly.\n"
     "• Arrange continuous EEG monitoring when available. Investigate underlying cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Correct Reversible Causes[/color]\n"
     "• Correct glucose and clinically significant calcium, sodium, or magnesium abnormalities per neonatal protocols.\n"
     "• Treat suspected meningitis/sepsis promptly. Consider pyridoxine-dependent epilepsy in refractory seizures under specialist supervision.\n\n"
     "[color=#1E3A8A]Phenobarbital (First-Line)[/color]\n"
     "• Loading dose: 20 mg/kg IV.\n"
     "• Additional loading doses may be considered under specialist direction if seizures persist.\n"
     "• Administer slowly by IV infusion. Monitor respiratory rate, SpO2, BP, cardiac status.\n"
     "• Prepare for respiratory support (respiratory depression/hypotension may occur)."),
    ("04 — WARNINGS", "danger", 
     "• Confirm total loading dose before giving additional doses.\n"
     "• Persistent seizures require reassessment and specialist-directed second-line treatment."),
    ("05 — DISPOSITION", "warning", 
     "• Urgent NICU assessment. Monitor for recurrent seizures and medication-related respiratory depression.\n"
     "• Arrange neurological follow-up for infants with significant seizures or brain injury."),
    ("REFERENCES", "info", "ILAE Neonatal Seizure Recommendations; Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Severe Neonatal Hyperbilirubinemia")] = [
    ("01 — RECOGNIZE", "info", 
     "Jaundice in the first 24 hours is pathological until evaluated.\n"
     "• Rapidly increasing jaundice, extending to legs, poor feeding, lethargy, abnormal tone.\n"
     "• Risk factors: prematurity, hemolysis, G6PD deficiency, bruising, inadequate milk intake, infection.\n"
     "• Severe bilirubin elevation can cause acute bilirubin encephalopathy and permanent neurological injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Measure total serum bilirubin urgently; do NOT rely on visual assessment alone.\n"
     "• Record exact age in hours, gestational age, and neurotoxicity risk factors.\n"
     "• Check maternal/infant blood groups and DAT when indicated.\n"
     "• Assess feeding, hydration, temperature, neurological status.\n"
     "• Start intensive phototherapy when age/gestation-specific threshold reached.\n"
     "• Obtain urgent neonatal specialist advice if bilirubin approaches exchange threshold or neuro signs present."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Intensive Phototherapy[/color]\n"
     "• Use intensive blue-light phototherapy with irradiance and exposed surface area meeting local standard.\n"
     "• Treatment threshold must be selected using applicable guideline chart for gestational age, postnatal age in hours, and risk factors.\n"
     "• Maximize skin exposure while protecting eyes. Monitor temp, hydration, feeding, serial bilirubin.\n"
     "• Continue breastfeeding or provide appropriate feeding support.\n\n"
     "[color=#1E3A8A]Exchange Transfusion[/color]\n"
     "• Indication: Bilirubin at/above applicable exchange threshold, or signs of acute bilirubin encephalopathy requiring emergency management.\n"
     "• Urgent NICU/experienced neonatal team involvement. Prepare compatible blood products. Monitor cardiorespiratory status, glucose, electrolytes, calcium, bilirubin per protocol."),
    ("04 — WARNINGS", "danger", 
     "• Do not use one bilirubin cutoff for all newborns. Treatment thresholds vary substantially with age in hours, gestational age, and risk factors.\n"
     "• Do not delay escalation when severe bilirubin encephalopathy is suspected."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for intensive phototherapy or exchange transfusion.\n"
     "• Arrange follow-up bilirubin testing and developmental/hearing assessment when clinically indicated."),
    ("REFERENCES", "info", "AAP Clinical Practice Guideline (2022); Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Apnea and Respiratory Failure")] = [
    ("01 — RECOGNIZE", "info", 
     "Apnea commonly defined as cessation of breathing for ~20 seconds, or shorter pause with bradycardia, cyanosis, or desaturation.\n"
     "• Grunting, nasal flaring, chest recession, tachypnea, poor air entry, increasing O2 requirement.\n"
     "• Causes: prematurity, infection, hypoglycemia, temperature instability, RDS, airway obstruction, seizures, pneumothorax."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway position, breathing, HR, SpO2. Position airway and provide gentle stimulation.\n"
     "• If apnea/ineffective breathing persists, provide effective PPV.\n"
     "• Reassess HR and chest movement; correct mask leak/airway obstruction.\n"
     "• Check glucose and temperature. Investigate infection and other reversible causes.\n"
     "• Escalate to CPAP or mechanical ventilation when indicated."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Positive-Pressure Ventilation[/color]\n"
     "• Indication: Apnea, gasping, ineffective breathing with clinical deterioration.\n"
     "• Use neonatal ventilation device/mask. Confirm effective chest movement and rising HR.\n\n"
     "[color=#1E3A8A]B. Caffeine for Apnea of Prematurity[/color]\n"
     "• Caffeine citrate: Loading dose 20 mg/kg, followed by 5–10 mg/kg once daily per protocol.\n"
     "• Verify dose is expressed as caffeine citrate, not caffeine base.\n"
     "• Administer by IV or enteral route. Monitor apnea frequency, HR, feeding tolerance."),
    ("04 — WARNINGS", "danger", 
     "• Oxygen alone does not correct apnea when ventilation is inadequate.\n"
     "• Caffeine does not replace urgent ventilation in an infant with ongoing apnea or respiratory failure.\n"
     "• Dosing/monitoring may differ in extremely premature or critically ill infants."),
    ("05 — DISPOSITION", "warning", 
     "• Recurrent apnea, bradycardia, or desaturation requires monitored neonatal care.\n"
     "• Respiratory failure, need for ventilation, or suspected sepsis requires urgent NICU assessment."),
    ("REFERENCES", "info", "AHA/AAP Neonatal Resuscitation Guidelines (2025); Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Necrotizing Enterocolitis (NEC)")] = [
    ("01 — RECOGNIZE", "info", 
     "Abdominal distension, feeding intolerance, bilious vomiting, or bloody stools.\n"
     "• Lethargy, temperature instability, apnea, bradycardia, poor perfusion.\n"
     "• Abdominal tenderness, discoloration, palpable mass. Most common in premature/VLBW infants.\n"
     "• [color=#991B1B]Red flags:[/color] Rapid abdominal enlargement, abdominal wall erythema, shock, severe metabolic acidosis, thrombocytopenia, persistent deterioration.\n"
     "• Pneumoperitoneum suggests intestinal perforation and is a surgical emergency."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stop enteral feeds immediately. Obtain urgent neonatal and pediatric surgical consultation.\n"
     "• Establish IV access, assess ABCs/perfusion. Insert orogastric/nasogastric tube for decompression.\n"
     "• Obtain blood cultures and lab investigations.\n"
     "• Start IV antibiotics covering Gram-positive, Gram-negative, and (when indicated) anaerobic organisms.\n"
     "• Correct hypoglycemia, electrolyte abnormalities, and shock. Monitor abdominal findings closely."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Bowel Rest and Decompression[/color]\n"
     "• Keep infant NPO. Decompress stomach with correctly placed OGT/NGT.\n"
     "• Provide IV fluids and nutritional support per neonatal/surgical guidance.\n"
     "• Monitor abdominal girth, tenderness, stool, urine output, glucose, electrolytes, perfusion.\n\n"
     "[color=#1E3A8A]B. IV Antibiotics[/color]\n"
     "• Use neonatal NEC antibiotic protocol; selection/duration depend on disease stage, local resistance, cultures, surgical findings.\n"
     "• [color=#991B1B]Do not use adult intra-abdominal infection regimen without neonatal dose verification.[/color]\n\n"
     "[color=#1E3A8A]C. Surgical Management[/color]\n"
     "• Indications: Pneumoperitoneum or suspected perforation, progressive deterioration despite medical treatment, abdominal wall discoloration, peritonitis, necrotic bowel."),
    ("04 — WARNINGS", "danger", 
     "• A normal initial radiograph does not exclude evolving NEC.\n"
     "• Suspected perforation or clinical deterioration requires immediate surgical reassessment."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to NICU. Continue close neonatal and surgical reassessment.\n"
     "• Restart feeds only after clinical improvement and individualized neonatal/surgical plan."),
    ("REFERENCES", "info", "APSA NEC Resources; Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Hypernatremic Dehydration")] = [
    ("01 — RECOGNIZE", "info", 
     "Poor feeding, excessive weight loss, reduced urine output, lethargy, irritability, weak cry.\n"
     "• Dry mucous membranes, fever, tachycardia, poor perfusion.\n"
     "• Severe: seizures, altered consciousness, intracranial hemorrhage, shock.\n"
     "• Causes: inadequate milk intake, ineffective breastfeeding, excessive insensible water loss, GI fluid loss.\n"
     "• Hypernatremia defined as serum sodium > 145 mmol/L.\n"
     "• [color=#991B1B]Clinical signs may underestimate degree of water deficit in neonatal hypernatremia.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, neuro status, temperature. Check bedside glucose immediately.\n"
     "• Obtain weight and compare with birth/previous weights.\n"
     "• Establish IV access if significant dehydration/instability. Obtain serum sodium, K+, Cl-, HCO3-, urea, creatinine, glucose, osmolality.\n"
     "• Assess urine output and ongoing losses.\n"
     "• If shock present, restore circulation cautiously with isotonic crystalloid and reassess frequently.\n"
     "• Correct sodium abnormality gradually with neonatal specialist-directed fluid plan."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Initial Circulatory Stabilization[/color]\n"
     "• If shock/severe intravascular depletion: 0.9% NaCl in cautious 10 mL/kg aliquots under specialist supervision. Reassess perfusion after each.\n"
     "• Once circulation restored, calculate remaining deficit and maintenance requirements.\n\n"
     "[color=#1E3A8A]B. Controlled Sodium Correction[/color]\n"
     "• Usual maximum sodium reduction ~0.5 mmol/L/hour and 10–12 mmol/L in 24 hours.\n"
     "• Calculate maintenance fluid, estimated deficit, and ongoing losses separately.\n"
     "• Check sodium frequently (every 2–4 hours initially in severe cases or during active correction).\n"
     "• Monitor glucose, K+, renal function, urine output, weight, neuro status."),
    ("04 — WARNINGS", "danger", 
     "• Avoid rapid correction of hypernatremia (can cause cerebral edema and seizures).\n"
     "• Do not attempt to normalize sodium rapidly.\n"
     "• Seizures or neurological deterioration during correction require urgent reassessment."),
    ("05 — DISPOSITION", "warning", 
     "• Admit infants with significant hypernatremia for monitored treatment.\n"
     "• Severe hypernatremia, shock, seizures, or renal impairment requires urgent NICU.\n"
     "• Assess feeding technique and establish safe feeding plan before discharge."),
    ("REFERENCES", "info", "NICE Neonatal Fluid/Electrolyte Guidance; Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Pneumothorax and Tension Pneumothorax")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden deterioration in SpO2 or ventilation. Increasing respiratory distress, cyanosis, apnea.\n"
     "• Reduced/absent breath sounds on one side may be present. Unequal chest movement or sudden cardiovascular compromise.\n"
     "• Tension pneumothorax: severe hypoxemia, bradycardia, hypotension, cardiac arrest.\n"
     "• Risk factors: PPV, RDS, meconium aspiration, underlying lung disease.\n"
     "• [color=#991B1B]A critically unstable infant with suspected tension pneumothorax requires immediate treatment; do NOT wait for radiographic confirmation.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for neonatal resuscitation and senior assistance. Assess airway, breathing, circulation, ventilation equipment.\n"
     "• Give oxygen and provide effective ventilation if needed.\n"
     "• If tension pneumothorax strongly suspected with cardiovascular/respiratory collapse: perform emergency decompression per neonatal emergency protocol.\n"
     "• Arrange definitive pleural drainage when indicated.\n"
     "• Obtain chest imaging after stabilization if no delay. Reassess for recurrence and underlying cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Emergency Decompression for Tension[/color]\n"
     "• Indication: Suspected tension pneumothorax with severe respiratory/cardiovascular compromise.\n"
     "• Appropriately trained clinician should immediately decompress affected hemithorax using approved neonatal technique/equipment.\n"
     "• Follow local protocol for anatomical site, catheter/needle selection, decompression method. Arrange chest drain insertion when indicated.\n\n"
     "[color=#1E3A8A]B. Stable Pneumothorax[/color]\n"
     "• Small, clinically stable pneumothoraces may be managed with close observation and respiratory support per specialist advice.\n"
     "• Larger pneumothoraces, worsening distress, or persistent air leaks may require pleural drainage."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay emergency decompression for imaging in a collapsing infant.\n"
     "• Incorrect placement can injure lung, heart, or blood vessels. Requires appropriate training.\n"
     "• Avoid unnecessary positive-pressure escalation without assessing for worsening air leak."),
    ("05 — DISPOSITION", "warning", 
     "• Tension pneumothorax or any infant requiring pleural drainage requires intensive neonatal monitoring.\n"
     "• Transfer to higher-level unit if drainage, ventilation, or continuous monitoring unavailable."),
    ("REFERENCES", "info", "AHA/AAP Neonatal Resuscitation Guidelines (2025); Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Critical Congenital Heart Disease and Duct-Dependent Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Duct-dependent congenital heart disease may become life-threatening as ductus arteriosus constricts during first days of life.\n"
     "• Cyanosis not improving as expected with oxygen. Poor feeding, tachypnea, lethargy, diaphoresis during feeding.\n"
     "• Weak femoral pulses or difference between upper/lower-limb pulses. Poor perfusion, metabolic acidosis, oliguria, shock.\n"
     "• Differential preductal and postductal SpO2 may occur.\n"
     "• Duct-dependent systemic: HLHS, critical aortic stenosis, interrupted aortic arch. Duct-dependent pulmonary: pulmonary atresia, critical pulmonary stenosis. TGA may cause profound cyanosis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, perfusion, BP, temperature.\n"
     "• Measure preductal SpO2 (right hand) and postductal SpO2 (foot).\n"
     "• Obtain IV access; check glucose, blood gas, lactate, electrolytes, renal function.\n"
     "• Contact NICU and pediatric cardiology urgently. Obtain urgent echocardiography when available.\n"
     "• If duct-dependent circulation strongly suspected in deteriorating neonate: initiate PGE1 under emergency specialist guidance without waiting for echo when delay dangerous.\n"
     "• Treat shock cautiously; avoid indiscriminate fluid boluses. Arrange urgent transfer to cardiac-capable center."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Prostaglandin E1 (Alprostadil)[/color]\n"
     "• Indication: Suspected duct-dependent CHD when maintaining ductal patency essential.\n"
     "• Initial infusion range: 0.01–0.05 mcg/kg/min IV. Titrate per neonatal/cardiology team and protocol.\n"
     "• Give as continuous IV infusion using syringe pump. Monitor HR, BP, SpO2, respiratory effort, temperature, perfusion continuously.\n"
     "• Prepare for assisted ventilation and transfer to intensive care.\n"
     "• [color=#991B1B]Do NOT give as IV bolus. Do NOT stop abruptly in neonate dependent on ductal patency without specialist direction.[/color]\n\n"
     "[color=#1E3A8A]B. Shock Management[/color]\n"
     "• If significant hypovolemia suspected: cautious isotonic crystalloid 10 mL/kg aliquots with immediate reassessment.\n"
     "• Avoid repeated boluses when myocardial dysfunction/fluid overload suspected. Use vasoactive support per shock phenotype."),
    ("04 — WARNINGS", "danger", 
     "• Apnea, hypotension, flushing, and fever may occur with PGE1.\n"
     "• Oxygen alone does not correct duct-dependent systemic obstruction and may not correct cyanosis from complex cardiac physiology.\n"
     "• Avoid delaying prostaglandin or cardiology assessment."),
    ("05 — DISPOSITION", "warning", 
     "• Urgent NICU admission. Transfer to pediatric cardiac center ASAP.\n"
     "• Continue PGE1 infusion and cardiorespiratory monitoring during transfer with personnel capable of managing apnea and deterioration."),
    ("REFERENCES", "info", "AHA Neonatal Cyanosis/CHD Management; Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Hypoxic-Ischemic Encephalopathy (HIE)")] = [
    ("01 — RECOGNIZE", "info", 
     "HIE results from impaired oxygen delivery and blood flow around birth and may cause acute brain injury.\n"
     "• Difficult resuscitation or significant perinatal hypoxic event.\n"
     "• Altered consciousness, lethargy, reduced spontaneous activity. Abnormal tone, weak suck, impaired primitive reflexes.\n"
     "• Clinical or electrographic seizures. Respiratory depression, poor perfusion, metabolic acidosis, multiorgan dysfunction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize ABCs. Review resuscitation history, cord gases, Apgar scores, evidence of perinatal hypoxia.\n"
     "• Check glucose, blood gas, lactate, electrolytes, renal/liver function, coagulation.\n"
     "• Perform structured neuro exam and assess eligibility for therapeutic hypothermia.\n"
     "• Contact NICU urgently. Treat seizures and correct reversible physiological abnormalities.\n"
     "• Arrange EEG/aEEG when available. Do NOT delay specialist consultation while waiting for neuroimaging."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Therapeutic Hypothermia[/color]\n"
     "• Eligibility: Consider for eligible infants (generally ≥36 weeks gestation) with evidence of significant perinatal hypoxia-ischemia and moderate-to-severe encephalopathy. Initiation time-critical, generally within 6 hours after birth.\n"
     "• Target: Core temperature near 33.5°C for 72 hours, followed by controlled rewarming. Use only approved device and protocol in unit capable of continuous monitoring.\n"
     "• Monitor core temperature continuously. Monitor HR, BP, oxygenation, glucose, electrolytes, coagulation, urine output, neuro status. Rewarm slowly per protocol.\n"
     "• [color=#991B1B]Do NOT initiate uncontrolled cooling with ice packs or improvised methods.[/color]\n\n"
     "[color=#1E3A8A]B. Seizure Management[/color]\n"
     "• Treat confirmed/strongly suspected neonatal seizures per protocol. Check/correct glucose, calcium, sodium, magnesium.\n\n"
     "[color=#1E3A8A]C. Multiorgan Support[/color]\n"
     "• Maintain adequate oxygenation/ventilation (avoid hyperoxia/hypocapnia). Maintain glucose/electrolyte stability. Monitor renal, liver, coagulation, hemodynamics."),
    ("04 — WARNINGS", "danger", 
     "• Do not initiate uncontrolled cooling with ice packs or improvised methods.\n"
     "• Do not delay referral of an eligible infant while arranging nonessential tests.\n"
     "• Therapeutic hypothermia not routinely recommended for every infant with mild encephalopathy or outside eligibility criteria; obtain specialist advice."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to NICU.\n"
     "• Arrange neurodevelopmental follow-up, hearing assessment, and early-intervention services per findings and local pathway.\n"
     "• Counsel family using serial examinations, EEG, imaging, and overall clinical course rather than single early finding."),
    ("REFERENCES", "info", "AAP Therapeutic Hypothermia for HIE; Local protocols.")
]

PEDIATRIC_TOPICS[("Pediatric Emergencies", "Neonatal Bilious Vomiting and Intestinal Obstruction")] = [
    ("01 — RECOGNIZE", "info", 
     "Bilious vomiting in a neonate is a surgical emergency until intestinal obstruction has been excluded.\n"
     "• Green, bile-stained vomiting. Abdominal distension or tenderness.\n"
     "• Failure to pass meconium or abnormal stool passage. Poor feeding, dehydration, lethargy, shock.\n"
     "• Blood in stool, abdominal discoloration, systemic deterioration may indicate bowel ischemia or NEC.\n"
     "• Causes: Malrotation with midgut volvulus, intestinal atresia/stenosis, Hirschsprung, meconium ileus, NEC, other congenital/acquired obstruction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat green bilious vomiting as emergency; obtain immediate pediatric surgical consultation.\n"
     "• Stop all oral/enteral feeds. Assess ABCs, perfusion, hydration, glucose.\n"
     "• Establish IV access, obtain blood tests. Insert orogastric/nasogastric tube for decompression per protocol.\n"
     "• Provide isotonic IV fluids when indicated, with reassessment.\n"
     "• Obtain urgent abdominal imaging guided by surgical team.\n"
     "• Start antibiotics if ischemia, perforation, NEC, or sepsis suspected. Arrange urgent transfer to pediatric surgical center if required."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Stabilization and Gastric Decompression[/color]\n"
     "• Keep infant NPO. Use appropriately sized OGT/NGT for decompression.\n"
     "• Provide IV maintenance fluid and replace deficits/ongoing losses per neonatal guidance.\n"
     "• Correct hypoglycemia and clinically important electrolyte abnormalities.\n"
     "• Monitor abdominal girth, vomiting, tube output, perfusion, urine output, glucose, serial blood gases when indicated.\n\n"
     "[color=#1E3A8A]B. Antibiotics[/color]\n"
     "• Indication: Suspected bowel ischemia, perforation, NEC, or systemic infection.\n"
     "• Use neonatal intra-abdominal infection or NEC protocol selected by treating team.\n\n"
     "[color=#1E3A8A]C. Definitive Management[/color]\n"
     "• Malrotation with suspected volvulus: urgent surgical evaluation and often emergency operation.\n"
     "• Atresia and other mechanical obstructions: pediatric surgical management."),
    ("04 — WARNINGS", "danger", 
     "• Do not give feeds, oral fluids, or laxatives while obstruction suspected.\n"
     "• Do not delay surgical consultation while waiting for complete investigation panel.\n"
     "• Antibiotics do not correct mechanical obstruction or replace urgent surgery when volvulus or ischemic bowel suspected."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to neonatal unit with immediate pediatric surgical involvement.\n"
     "• Transfer urgently to center with neonatal surgery if unavailable locally.\n"
     "• Document color of vomit, onset, abdominal findings, meconium passage, fluid management, surgical communication."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne; APSA Resources; Local protocols.")
]