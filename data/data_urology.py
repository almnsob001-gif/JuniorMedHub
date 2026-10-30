# data_urology.py

UROLOGY_DATA = {
    "Urology Emergencies": {
        "Scrotal & Testicular Emergencies": [
            "Testicular Torsion",
            "Testicular Rupture",
            "Acute Scrotal Pain: Differential Diagnosis",
            "Acute Epididymo-Orchitis"
        ],
        "Penile Emergencies": [
            "Ischemic Priapism",
            "Paraphimosis",
            "Penile Fracture"
        ],
        "Urinary Retention & Obstruction": [
            "Acute Urinary Retention",
            "Acute Urinary Retention with High-Risk Complications",
            "Acute Obstructive Uropathy",
            "Post-Obstructive Diuresis",
            "Difficult Urethral Catheterization",
            "Postrenal Acute Kidney Injury"
        ],
        "Urinary Tract Infection & Sepsis": [
            "Urosepsis and Septic Shock",
            "Acute Pyelonephritis with Complications",
            "Emphysematous Pyelonephritis",
            "Renal or Perinephric Abscess",
            "Acute Bacterial Prostatitis",
            "Obstructed Infected Kidney",
            "Infected Ureteric Stone"
        ],
        "Urolithiasis & Renal Colic": [
            "Acute Ureteric Colic",
            "Renal Colic in Pregnancy"
        ],
        "Hematuria": [
            "Gross Hematuria with Clot Retention",
            "Gross Hematuria Without Clot Retention"
        ],
        "Trauma & Iatrogenic Injury": [
            "Renal Trauma",
            "Bladder Trauma and Rupture",
            "Urethral Injury",
            "Iatrogenic Ureteric Injury"
        ],
        "Soft Tissue & Other Emergencies": [
            "Fournier's Gangrene",
            "General Safety Checklist"
        ]
    }
}

UROLOGY_TOPICS = {}

UROLOGY_TOPICS[("Urology Emergencies", "Testicular Torsion")] = [
    ("01 — RECOGNITION", "info", 
     "Testicular torsion is twisting of the spermatic cord, compromising testicular blood flow. It is a time-critical surgical emergency.\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Sudden, severe unilateral scrotal pain.\n"
     "• Nausea and vomiting.\n"
     "• High-riding or horizontally oriented testis.\n"
     "• Swelling and testicular tenderness.\n"
     "• Absent cremasteric reflex may be present.\n\n"
     "[color=#991B1B]IMPORTANT: Torsion can occur in neonates, children, adolescents, and adults. A preserved cremasteric reflex or atypical presentation does not reliably exclude torsion.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Request immediate urological or surgical review.\n"
     "• Keep the patient nil by mouth.\n"
     "• Establish IV access and provide analgesia.\n"
     "• Document symptom onset, testicular position, swelling, and examination findings.\n"
     "• Prepare for emergency scrotal exploration.\n"
     "• Do not delay surgery for imaging when clinical suspicion is high."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical examination.\n"
     "• Doppler ultrasound if immediately available and diagnosis remains uncertain, provided it does not delay surgical assessment.\n"
     "• Urinalysis when alternative diagnoses are considered; a normal urinalysis does not exclude torsion."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive treatment:[/color] Emergency surgical exploration, detorsion, assessment of viability, and orchidopexy. The contralateral testis is generally fixed during the same operation.\n\n"
     "[color=#1E3A8A]Dose:[/color]\n"
     "• Paracetamol: 1 g orally or IV in an adult, usually every 6 hours as needed.\n"
     "• Severe pain may require titrated IV opioid analgesia under appropriate monitoring.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Monitor pain, vital signs, and response to analgesia.\n"
     "• Keep the patient fasting and document the time of symptom onset and referral.\n"
     "• Manual detorsion may be attempted by a trained clinician if surgery is delayed, but it must never delay definitive surgery."),
    ("05 — WARNINGS", "danger", 
     "• Do not wait for the testis to become discolored or for the ultrasound result if suspicion is high.\n"
     "• Testicular salvage is best when treatment occurs within approximately 4–6 hours, but late presentation is still an emergency.\n"
     "• Pain relief after manual detorsion does not eliminate the need for surgery."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate surgical management. Admit for operative treatment and postoperative assessment."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Time is testicular tissue.\n"
     "• Differential diagnosis includes epididymo-orchitis, torsion of the appendix testis, incarcerated hernia, and testicular trauma.\n"
     "• A normal Doppler study should not override strong clinical suspicion."),
    ("REFERENCES", "info", "EAU Guidelines on Paediatric Urology, Acute Scrotum; Royal Children's Hospital.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Fournier's Gangrene")] = [
    ("01 — RECOGNITION", "info", 
     "Fournier's gangrene is a rapidly progressive necrotizing infection of the perineum, perianal region, and external genitalia. It may cause septic shock and death.\n\n"
     "[color=#1E3A8A]Risk factors:[/color] Diabetes mellitus, immunosuppression, recent urological procedures, perianal/urinary/genital infections.\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Severe genital or perineal pain (sometimes disproportionate to visible findings).\n"
     "• Swelling, erythema, dusky discoloration, or skin necrosis.\n"
     "• Crepitus or foul-smelling discharge in advanced disease.\n"
     "• Fever, tachycardia, hypotension, or altered mental status."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call urology and general surgery immediately.\n"
     "• Activate the sepsis pathway and assess for shock.\n"
     "• Establish IV access, obtain cultures when feasible, and begin broad-spectrum IV antibiotics promptly.\n"
     "• Resuscitate with appropriate IV fluids and vasopressors when indicated.\n"
     "• Arrange emergency operative debridement.\n"
     "• Involve ICU, anesthesia, and other surgical teams as required."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, glucose, blood gas, lactate, coagulation profile, and blood cultures.\n"
     "• Cultures from operative tissue and drainage.\n"
     "• CT may help define extent in a stable patient, but imaging must not delay surgery."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric adult antibiotic example:[/color]\n"
     "• Piperacillin–tazobactam 4.5 g IV every 6–8 hours.\n"
     "• Add vancomycin when MRSA coverage is indicated (15–20 mg/kg IV initial dose).\n"
     "• Add clindamycin 900 mg IV every 8 hours when toxin suppression is indicated.\n"
     "*(These are example components, not a universal regimen).*\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Give antibiotics immediately and document administration time.\n"
     "• Monitor BP, lactate, urine output, renal function, glucose, and resuscitation response.\n"
     "• Perform urgent surgical debridement; repeated debridement may be required."),
    ("05 — WARNINGS", "danger", 
     "• Antibiotics alone are insufficient.\n"
     "• Do not delay surgery for CT, laboratory scores, or complete culture results.\n"
     "• Visible skin changes may underestimate deep tissue destruction.\n"
     "• Avoid relying on the absence of fever or crepitus to exclude the diagnosis."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency surgery and hospital admission. ICU care is required for shock, organ dysfunction, or severe disease."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Severe pain with subtle genital or perineal skin findings should raise suspicion.\n"
     "• Early source control is critical.\n"
     "• Assess for urinary, anorectal, and cutaneous sources."),
    ("REFERENCES", "info", "EAU Guidelines on Urological Infections; Emergency Care Institute NSW.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Obstructed Infected Kidney")] = [
    ("01 — RECOGNITION", "info", 
     "An infected, obstructed urinary collecting system (Obstructive Pyelonephritis / Infected Hydronephrosis) is a urological emergency. It may progress rapidly to urosepsis, septic shock, and acute kidney injury.\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Fever, chills, flank pain, or costovertebral-angle tenderness.\n"
     "• Dysuria or urinary frequency may be present.\n"
     "• Nausea and vomiting.\n"
     "• Hypotension, tachycardia, confusion, or oliguria in severe infection.\n"
     "• Risk increased with ureteric stones, strictures, tumors, pregnancy."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call urology immediately.\n"
     "• Assess for sepsis and initiate resuscitation when indicated.\n"
     "• Obtain urine and blood cultures when feasible.\n"
     "• Start IV antibiotics promptly.\n"
     "• Arrange urgent decompression with a ureteric stent or percutaneous nephrostomy.\n"
     "• Do not delay drainage in a septic/deteriorating patient while waiting for definitive stone treatment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture.\n"
     "• CBC, creatinine, electrolytes, lactate, and blood cultures.\n"
     "• Renal ultrasound to identify hydronephrosis.\n"
     "• Non-contrast CT for suspected ureteric stone when appropriate."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics (Adult examples):[/color]\n"
     "• Ceftriaxone 1–2 g IV every 24 hours.\n"
     "• Piperacillin–tazobactam 4.5 g IV every 6–8 hours for severe infection or broader coverage.\n"
     "• Adjust dosing for renal impairment.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Monitor BP, urine output, lactate, renal function, and response.\n"
     "• Arrange urgent ureteric stenting or nephrostomy for decompression.\n"
     "• Delay definitive stone removal until sepsis has resolved and infection is controlled."),
    ("05 — WARNINGS", "danger", 
     "• Antibiotics alone cannot reliably treat infection behind a persistent obstruction.\n"
     "• Do not discharge a patient with sepsis and an obstructed collecting system.\n"
     "• Anuria, bilateral obstruction, or obstruction of a solitary functioning kidney requires urgent specialist intervention."),
    ("06 — DISPOSITION", "warning", 
     "• Admit urgently. Septic patients may require ICU care. Transfer to a center capable of urgent urinary drainage if unavailable locally."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Sepsis plus obstruction requires antibiotics AND source control.\n"
     "• Ureteric stenting and nephrostomy are accepted decompression methods.\n"
     "• Reassess renal function after drainage."),
    ("REFERENCES", "info", "EAU Guidelines on Urolithiasis; EAU Guidelines on Urological Infections.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Urinary Retention")] = [
    ("01 — RECOGNITION", "info", 
     "Acute urinary retention is the sudden inability to empty the bladder, often with painful bladder distension.\n\n"
     "[color=#1E3A8A]Common causes:[/color] Benign prostatic enlargement, urethral stricture, stones/clots, medications (anticholinergics/opioids), constipation, postoperative retention, neurological disease.\n\n"
     "[color=#1E3A8A]Clinical features:[/color] Inability to pass urine, suprapubic pain, palpable/ultrasound-confirmed distended bladder, overflow dribbling."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs and abdominal findings.\n"
     "• Perform a bladder scan when available.\n"
     "• Relieve retention by urethral catheterization if there is no suspicion of urethral injury.\n"
     "• If catheterization fails, stop repeated traumatic attempts and seek urological assistance.\n"
     "• Investigate the cause and assess renal function, infection, and post-obstructive diuresis risk."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bladder scan and post-void residual.\n"
     "• Urinalysis and urine culture if infection suspected.\n"
     "• Creatinine, electrolytes, and glucose.\n"
     "• Renal/bladder ultrasound if renal impairment suspected.\n"
     "• Neurological examination if spinal cord/cauda equina pathology is possible."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Bladder drainage:[/color]\n"
     "• Insert an appropriately sized urethral catheter using aseptic technique.\n"
     "• If contraindicated/unsuccessful, urgent urological assessment for alternative drainage (e.g., suprapubic catheter).\n\n"
     "[color=#1E3A8A]Medication:[/color]\n"
     "• For BPH: Tamsulosin 0.4 mg orally once daily may be initiated.\n"
     "• A trial without catheter may be considered after at least 3 days of alpha-blocker therapy.\n\n"
     "[color=#1E3A8A]Monitoring:[/color]\n"
     "• Record volume and appearance of drained urine.\n"
     "• Monitor urine output, fluid balance, BP, renal function, and electrolytes.\n"
     "• Watch for post-obstructive diuresis."),
    ("05 — WARNINGS", "danger", 
     "• Blood at the urethral meatus after trauma, perineal bruising, or suspected urethral disruption requires evaluation before blind catheterization.\n"
     "• Do not force a catheter against resistance.\n"
     "• Sudden decompression is generally acceptable; monitor for hematuria, hypotension, and post-obstructive diuresis.\n"
     "• New urinary retention with saddle anesthesia or leg weakness is a possible cauda equina emergency."),
    ("06 — DISPOSITION", "warning", 
     "• Depends on cause, renal function, infection, and follow-up safety. Admit for sepsis, AKI, significant electrolyte abnormalities, suspected neurological disease."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Relieving the obstruction is the first priority.\n"
     "• Alpha-blockers improve the chance of a successful trial without catheter in BPH.\n"
     "• Persistent retention requires evaluation of the underlying cause."),
    ("REFERENCES", "info", "American Urological Association, BPH Guideline.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Ischemic Priapism")] = [
    ("01 — RECOGNITION", "info", 
     "Ischemic priapism is a painful, prolonged erection caused by impaired venous outflow and trapped blood within the corpora cavernosa. It is a urological emergency (risk of permanent erectile dysfunction).\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Erection lasting four hours or longer.\n"
     "• Painful, rigid corpora cavernosa.\n"
     "• The glans may remain relatively soft.\n"
     "• History of sickle cell disease, hematologic malignancy, or causative drugs."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain immediate urological consultation.\n"
     "• Establish IV access and provide analgesia.\n"
     "• Record duration, pain, relevant medications, and medical history.\n"
     "• Do not delay definitive treatment while attempting oral remedies.\n"
     "• Assess for sickle cell disease or another underlying cause without delaying penile treatment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical assessment.\n"
     "• Cavernosal blood gas when diagnosis is uncertain (ischemic shows hypoxic, hypercarbic, acidotic blood).\n"
     "• CBC and targeted investigations for sickle cell disease or other causes."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive initial treatment:[/color]\n"
     "• Corporal aspiration (with or without saline irrigation), followed by intracavernosal phenylephrine.\n"
     "• Surgical shunting may be required if conservative treatment fails.\n\n"
     "[color=#1E3A8A]Phenylephrine — specialist-administered:[/color]\n"
     "• Concentration: 100–500 micrograms/mL.\n"
     "• Typical adult dose: 100–500 micrograms injected intracavernosally, repeated every 3–5 minutes.\n"
     "• Max total dose of 1 mg within one hour (follow local protocol).\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Must be performed by a trained clinician.\n"
     "• Monitor BP, heart rate, and ECG.\n"
     "• Reassess penile rigidity and pain after each step.\n"
     "• Escalate to surgical management promptly if erection persists."),
    ("05 — WARNINGS", "danger", 
     "• Oral medication or observation alone is not adequate.\n"
     "• Phenylephrine can cause severe hypertension, arrhythmias, and cardiovascular complications.\n"
     "• Dilution errors can cause serious cardiovascular harm. Never inject undiluted concentrate.\n"
     "• Do not delay urology consultation."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent urological treatment and observation until detumescence and clinical stability. Admit when ongoing treatment or complications are suspected."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Ischemic priapism is usually painful with rigid corpora.\n"
     "• Non-ischemic priapism is often less painful and follows trauma.\n"
     "• The longer ischemia persists, the greater the risk of erectile dysfunction."),
    ("REFERENCES", "info", "AUA/SMSNA, Diagnosis and Management of Priapism.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Paraphimosis")] = [
    ("01 — RECOGNITION", "info", 
     "Paraphimosis occurs when a retracted foreskin becomes trapped behind the glans penis, producing a constricting ring and progressive edema. It can compromise blood flow and cause tissue necrosis.\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Retracted foreskin that cannot be brought forward.\n"
     "• Painful swelling of the glans and foreskin.\n"
     "• A tight constricting band behind the glans.\n"
     "• Dusky or dark discoloration in severe cases."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess glans color, sensation, swelling, and perfusion.\n"
     "• Provide analgesia and explain the procedure.\n"
     "• Obtain urgent urological help if reduction is difficult or ischemia is suspected.\n"
     "• Attempt prompt manual reduction if appropriate and performed by a trained clinician."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Manual reduction:[/color]\n"
     "• Apply gentle, sustained compression to reduce edema, then move the foreskin forward over the glans.\n"
     "• Provide adequate analgesia; local anesthesia or penile block may be considered.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Reassess pain, swelling, color, and perfusion after reduction.\n"
     "• If manual reduction fails, urgent surgical intervention may be needed (dorsal slit or circumcision)."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay reduction when perfusion is threatened.\n"
     "• Avoid repeated forceful attempts that may cause tissue injury.\n"
     "• Dusky, blue, or black discoloration, severe pain, or impaired perfusion requires immediate urological intervention."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge may be appropriate after successful reduction if glans is well perfused, pain is controlled, and follow-up is arranged. Failed reduction or ischemia requires specialist care."),
    ("06 — CLINICAL PEARLS", "info", 
     "• Always return the foreskin to its normal position after examination or catheterization.\n"
     "• Explain recurrence prevention and the need for urological follow-up if phimosis is present."),
    ("REFERENCES", "info", "EAU Guidelines on Paediatric Urology; NHS.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Gross Hematuria with Clot Retention")] = [
    ("01 — RECOGNITION", "info", 
     "Gross hematuria with clot retention is visible urinary bleeding that causes obstruction of bladder outflow by blood clots. It may lead to painful distension, acute retention, anemia, or hemodynamic instability.\n\n"
     "[color=#1E3A8A]Possible causes:[/color] Bladder/prostate bleeding, malignancy, infection, stones, recent instrumentation, trauma, or anticoagulants."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess hemodynamic stability and control life-threatening bleeding.\n"
     "• Establish IV access and obtain blood tests and crossmatch.\n"
     "• Request urgent urological review.\n"
     "• If no suspected urethral injury, insert a large-bore three-way urinary catheter.\n"
     "• Perform manual clot evacuation and continuous bladder irrigation according to protocol.\n"
     "• Arrange urgent cystoscopy or operative clot evacuation if obstruction persists."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, renal function, electrolytes, coagulation studies, and type/crossmatch.\n"
     "• Urinalysis and urine culture.\n"
     "• Review anticoagulants and antiplatelet drugs.\n"
     "• Imaging and cystoscopy based on clinical stability."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Bladder drainage:[/color]\n"
     "• A three-way Foley catheter (commonly 22–24 French in adults) may be required for clot evacuation and continuous irrigation.\n"
     "• Use sterile 0.9% sodium chloride for bladder irrigation.\n"
     "• Adjust irrigation to maintain drainage free of obstructing clots; monitor input and output carefully.\n\n"
     "[color=#1E3A8A]Monitoring:[/color]\n"
     "• Monitor vital signs, pain, urine color, clot burden, urine output, hemoglobin, and renal function.\n"
     "• Document irrigation volume and drainage volume separately.\n"
     "• Arrange cystoscopy or operative intervention if bleeding persists."),
    ("05 — WARNINGS", "danger", 
     "• Do not force a catheter in suspected urethral trauma.\n"
     "• Never allow continuous irrigation to continue against an obstructed outflow catheter; bladder overdistension and rupture may occur.\n"
     "• Anticoagulant reversal must be individualized and balanced against thrombosis risk."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with clot retention, ongoing significant bleeding, anemia, renal impairment, or need for continuous irrigation/operative intervention."),
    ("07 — CLINICAL PEARLS", "info", 
     "• A three-way catheter allows simultaneous drainage and irrigation.\n"
     "• Continuous irrigation is safe only when outflow remains patent.\n"
     "• Do not confuse total drainage volume with actual urine output."),
    ("REFERENCES", "info", "StatPearls; AUA Urologic Emergencies.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Urethral Injury")] = [
    ("01 — RECOGNITION", "info", 
     "Urethral injury may occur after pelvic fractures, straddle injuries, penetrating trauma, or instrumentation. Failure to recognize it can worsen damage (strictures, incontinence).\n\n"
     "[color=#991B1B]Warning features:[/color]\n"
     "• Blood at the urethral meatus.\n"
     "• Inability to urinate after trauma.\n"
     "• Perineal or scrotal bruising.\n"
     "• Pelvic fracture with urinary symptoms.\n"
     "• Difficulty passing a catheter after traumatic injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform the trauma primary survey and control life-threatening bleeding.\n"
     "• Contact urology or trauma surgery urgently.\n"
     "• If urethral injury is suspected, avoid blind urethral catheterization.\n"
     "• Perform retrograde urethrography in appropriate patients.\n"
     "• Arrange bladder drainage through a specialist-directed approach if required."),
    ("03 — INVESTIGATIONS", "info", 
     "• Retrograde urethrogram in suspected urethral injury.\n"
     "• CT and other trauma imaging based on associated injuries.\n"
     "• Urinalysis and renal function.\n"
     "• Assess for associated bladder, pelvic, rectal, and vascular injuries."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Initial management:[/color]\n"
     "• Stabilize associated injuries.\n"
     "• Avoid repeated attempts at urethral catheterization.\n"
     "• Urinary diversion may require a suprapubic catheter placed by a trained clinician.\n"
     "• Selected partial injuries may be managed with specialist-directed catheter placement or endoscopic realignment."),
    ("05 — WARNINGS", "danger", 
     "• Blood at the meatus after pelvic trauma is a major warning sign.\n"
     "• Do not blindly pass a Foley catheter when urethral disruption is suspected.\n"
     "• In life-threatening circumstances, urinary drainage decisions must be made urgently without delaying resuscitation."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or transfer for specialist evaluation. Pelvic fracture-associated injury generally requires coordinated trauma and urology care."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Urethral injury should be considered in pelvic fractures with blood at the meatus or inability to void.\n"
     "• A single traumatic catheterization attempt may worsen a partial injury.\n"
     "• Long-term follow-up is important because strictures may develop later."),
    ("REFERENCES", "info", "AUA Urotrauma Guideline; EAU Guidelines on Urological Trauma.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Testicular Rupture")] = [
    ("01 — RECOGNITION", "info", 
     "Testicular rupture is disruption of the tunica albuginea after blunt or penetrating scrotal trauma. Delayed treatment can lead to testicular loss.\n\n"
     "[color=#1E3A8A]Clinical features:[/color]\n"
     "• Severe scrotal pain after trauma.\n"
     "• Rapid swelling and bruising.\n"
     "• Nausea or vomiting.\n"
     "• Difficulty palpating the testis due to swelling.\n"
     "• Hematocele or abnormal testicular contour."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess trauma mechanism and associated injuries.\n"
     "• Provide analgesia and scrotal support.\n"
     "• Request urgent urological assessment.\n"
     "• Obtain urgent scrotal ultrasound with Doppler.\n"
     "• Keep the patient fasting if surgical exploration is likely.\n"
     "• Do not delay exploration when rupture is strongly suspected or imaging is inconclusive."),
    ("03 — INVESTIGATIONS", "info", 
     "• Scrotal ultrasound with Doppler.\n"
     "• CBC and other trauma investigations.\n"
     "• Assess testicular perfusion and contour.\n"
     "• Evaluate for associated penile, urethral, pelvic, or abdominal injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive treatment:[/color]\n"
     "• Urgent surgical exploration when rupture is diagnosed or strongly suspected.\n"
     "• Debridement of nonviable tissue and repair of the tunica albuginea.\n"
     "• Orchiectomy may be necessary if the testis is nonviable.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Prepare for urgent surgery and anesthesia assessment.\n"
     "• Maintain scrotal support while awaiting definitive care.\n"
     "• Monitor pain, swelling, skin condition, and vital signs."),
    ("05 — WARNINGS", "danger", 
     "• Do not assume that severe scrotal swelling is only a hematoma.\n"
     "• A negative or equivocal ultrasound does not exclude rupture when clinical suspicion remains high.\n"
     "• Do not delay surgical review while waiting for repeat imaging if the testis may be threatened."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent urological management. Confirmed rupture generally requires operative exploration and admission."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Early repair improves the chance of testicular preservation.\n"
     "• Ultrasound is useful, but clinical judgment and specialist assessment remain essential.\n"
     "• Consider safeguarding concerns in children when the injury mechanism is unclear."),
    ("REFERENCES", "info", "EAU Guidelines on Urological Trauma; AUA Urotrauma Guideline.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Penile Fracture")] = [
    ("01 — RECOGNITION", "info", 
     "Penile fracture is rupture of the tunica albuginea of an erect corpus cavernosum, usually due to bending trauma during sexual activity.\n\n"
     "[color=#1E3A8A]Typical features:[/color]\n"
     "• Sudden cracking or popping sound.\n"
     "• Immediate loss of erection.\n"
     "• Acute penile pain.\n"
     "• Rapid swelling and bruising.\n"
     "• Penile deviation or deformity.\n\n"
     "[color=#1E3A8A]Associated urethral injury may present with:[/color] Blood at meatus, gross hematuria, difficulty urinating."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Contact urology urgently.\n"
     "• Keep the patient nil by mouth.\n"
     "• Provide analgesia.\n"
     "• Document mechanism, timing, swelling, deformity, and urinary symptoms.\n"
     "• Assess for associated urethral injury.\n"
     "• Prepare for prompt surgical exploration and repair."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical diagnosis is often sufficient when history and findings are typical.\n"
     "• Ultrasound or MRI may be considered when diagnosis is uncertain.\n"
     "• Retrograde urethrography or urethroscopy may be required if urethral injury is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive treatment:[/color]\n"
     "• Prompt surgical exploration and repair of the tunica albuginea.\n"
     "• Evaluate and manage associated urethral injury during the operative assessment.\n\n"
     "[color=#1E3A8A]Monitoring:[/color]\n"
     "• Monitor pain, swelling, urinary function, and vital signs.\n"
     "• Postoperative follow-up should assess healing, penile curvature, erectile function, and urethral symptoms."),
    ("05 — WARNINGS", "danger", 
     "• Do not manage a convincing penile fracture with ice and observation alone.\n"
     "• Do not delay surgical consultation for imaging when the clinical diagnosis is clear.\n"
     "• Blood at the meatus, hematuria, or urinary retention increases concern for urethral injury."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent urological admission or operative management. Prompt repair, ideally within 24 hours, reduces the risk of long-term complications."),
    ("07 — CLINICAL PEARLS", "info", 
     "• A sudden pop followed by immediate detumescence and bruising is highly suggestive.\n"
     "• Early repair is associated with better functional outcomes.\n"
     "• Exclude associated urethral injury."),
    ("REFERENCES", "info", "EAU Guidelines on Urological Trauma; British Association of Urological Surgeons.")
]

UROLOGY_TOPICS[("Urology Emergencies", "General Safety Checklist")] = [
    ("01 — GENERAL UROLOGICAL EMERGENCY SAFETY CHECKLIST", "warning", 
     "• Identify time-critical diagnoses early: testicular torsion, Fournier’s gangrene, infected urinary obstruction, ischemic priapism, and traumatic urinary tract injuries.\n"
     "• Contact urology or surgery early and document the time of referral.\n"
     "• Do not delay surgery, drainage, or revascularization for unnecessary imaging.\n"
     "• In suspected urethral trauma, avoid blind catheterization.\n"
     "• Verify medication allergies, weight-based dosing, renal adjustment, and drug concentrations.\n"
     "• Reassess vital signs, urine output, pain, perfusion, and response to treatment.\n"
     "• Arrange appropriate admission, transfer, and follow-up.")
]


# ==================== NEW UROLOGY TOPICS (12-21) ====================

UROLOGY_TOPICS[("Urology Emergencies", "Gross Hematuria with Clot Retention")] = [
    ("01 — RECOGNIZE", "info", 
     "Visible blood in urine, sometimes with large clots. Suprapubic pain, bladder distension, urgency, or inability to pass urine. Reduced urine output despite a distended bladder.\n"
     "• Tachycardia, hypotension, pallor, or syncope may indicate significant blood loss.\n"
     "• Causes: bladder/renal tumors, stones, infection, trauma, anticoagulants, recent urological procedures, radiation cystitis.\n"
     "• [color=#991B1B]Red urine is not always hematuria; consider hemoglobinuria, myoglobinuria, medication-related discoloration.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, and hemodynamic stability.\n"
     "• Establish IV access; use two large-bore IV cannulas if significant bleeding or shock suspected.\n"
     "• Monitor BP, HR, SpO2, urine output, mental status.\n"
     "• Obtain CBC, renal function, electrolytes, coagulation when indicated, and group/type and screen or crossmatch if significant bleeding.\n"
     "• Assess for bladder distension and clot retention using examination and bladder ultrasound.\n"
     "• Obtain urgent urology consultation for clot retention, ongoing heavy bleeding, hemodynamic instability, or suspected malignancy/trauma."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC (Hb and platelets), urea, creatinine, electrolytes, urinalysis, urine culture.\n"
     "• PT/INR and aPTT when anticoagulation/coagulopathy relevant.\n"
     "• Bladder ultrasound or bladder scan to assess retention.\n"
     "• CT urography or other upper tract imaging after stabilization, depending on renal function and suspected cause.\n"
     "• Cystoscopy may be required for persistent bleeding, clot evacuation, diagnosis, or definitive treatment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Bladder Decompression and Clot Evacuation[/color]\n"
     "• Indication: Significant clot retention or inability to drain bladder.\n"
     "• Equipment: Large-bore three-way urinary catheter (commonly 22–24 Fr in adults), sterile irrigation fluid, closed continuous bladder irrigation system.\n"
     "• If urethral injury suspected: do NOT attempt blind catheterization; obtain urgent specialist assessment.\n"
     "• If no urethral injury: insert large-bore three-way catheter. Gently irrigate with sterile 0.9% NaCl to remove clots. Start continuous bladder irrigation once cleared, adjusted to maintain light-pink urine.\n"
     "• Record irrigation input and actual urine output separately. Net urine output = total drainage minus irrigation volume.\n"
     "• [color=#991B1B]Never force irrigation against resistance or continue when outflow is blocked; excessive pressure may injure bladder.[/color]\n\n"
     "[color=#1E3A8A]Hemodynamic Support[/color]\n"
     "• If shock present: follow local hemorrhage/resuscitation protocol. Give IV isotonic crystalloid judiciously; transfuse blood products per clinical status, Hb, ongoing bleeding, comorbidities, local guidance.\n"
     "• Review anticoagulants/antiplatelet agents. Reversal only when clinically indicated, considering drug, indication, severity, thrombotic risk.\n"
     "• [color=#991B1B]Do NOT routinely use tranexamic acid for undifferentiated gross hematuria without specialist guidance (urinary tract clot obstruction may worsen).[/color]\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Identify and treat underlying cause. Cystoscopic clot evacuation and endoscopic control of bleeding may be necessary. Arrange appropriate evaluation for malignancy when indicated. Treat infection when confirmed/strongly suspected. Coordinate anticoagulation management with prescribing team."),
    ("05 — WARNINGS", "danger", 
     "• If catheter cannot be inserted safely, irrigation does not restore drainage, or bleeding remains severe → urgent urological intervention may be required for cystoscopic clot evacuation and hemostasis."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or arrange urgent specialist management if: Clot retention/inability to maintain catheter drainage. Hemodynamic instability, significant anemia, or ongoing heavy bleeding. AKI, suspected obstruction, or significant infection. Recent significant urinary tract trauma/procedure with ongoing bleeding.\n"
     "• Discharge only after bleeding and drainage adequately controlled, patient stable, and timely follow-up/return precautions established."),
    ("REFERENCES", "info", "EAU Guidelines on Urological Trauma and Non-neurogenic Male LUTS; AUA Hematuria Resources; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Renal Trauma")] = [
    ("01 — RECOGNIZE", "info", 
     "Blunt or penetrating trauma to the flank, abdomen, lower chest, or back.\n"
     "• Hematuria may be present but its absence does NOT exclude serious renal injury.\n"
     "• Flank tenderness, bruising, abdominal pain, or penetrating wound along renal trajectory.\n"
     "• Hypotension, tachycardia, pallor, or altered mental status may indicate major hemorrhage.\n"
     "• Associated injuries to liver, spleen, bowel, pancreas, ribs, or spine are common in high-energy trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow the trauma primary survey: ABCDE. Control external hemorrhage and initiate appropriate resuscitation.\n"
     "• Obtain large-bore IV access and blood samples (CBC, renal function, electrolytes, urinalysis, type and crossmatch when indicated).\n"
     "• Activate major hemorrhage protocol if severe bleeding or shock suspected.\n"
     "• Assess for associated abdominal, thoracic, pelvic, and spinal injuries.\n"
     "• Contact trauma surgery and urology early for suspected high-grade injury, ongoing bleeding, urinary extravasation, or a solitary functioning kidney."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]Imaging[/color]\n"
     "• Stable/stabilized patient: Contrast-enhanced CT abdomen/pelvis with appropriate delayed/excretory phase when renal collecting-system or ureteric injury suspected.\n"
     "• CT findings may include renal contusion, laceration, hematoma, devascularization, active contrast extravasation, collecting-system injury, or vascular injury.\n"
     "• Unstable patient: Do NOT delay life-saving hemorrhage control to obtain CT. Use bedside trauma ultrasound as adjunct; negative FAST does NOT exclude retroperitoneal renal injury.\n\n"
     "[color=#1E3A8A]Laboratory[/color]\n"
     "• CBC and serial Hb when bleeding suspected. Creatinine and electrolytes. Urinalysis. Coagulation studies and blood group/crossmatch when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage and Resuscitation[/color]\n"
     "• Use trauma resuscitation principles and blood products when clinically indicated. Avoid delaying definitive hemorrhage control in persistent shock.\n\n"
     "[color=#1E3A8A]Nonoperative Management[/color]\n"
     "• Indication: Most blunt renal injuries in hemodynamically stable patients, depending on CT grade and associated injuries. Admit for observation. Serial abdominal exams, vital signs, Hb. Monitor urine output, renal function. Analgesia. Avoid unnecessary nephrotoxic medications. Bed rest/activity restrictions individualized according to injury grade/clinical course.\n\n"
     "[color=#1E3A8A]Angioembolization[/color]\n"
     "• Indication: Selected stable/stabilized patients with active arterial bleeding, pseudoaneurysm, or AV fistula. Arrange urgent IR assessment. Selective angioembolization can control bleeding while preserving viable renal tissue.\n\n"
     "[color=#1E3A8A]Operative Management[/color]\n"
     "• Indication: Persistent hemodynamic instability attributable to renal bleeding, major vascular injury, or injuries requiring operative exploration. Urgent trauma and urological surgical management required. Nephrectomy may occasionally be necessary for uncontrollable life-threatening hemorrhage; renal preservation preferred when safely achievable."),
    ("05 — WARNINGS", "danger", 
     "• Do NOT use presence/absence of hematuria alone to determine injury severity.\n"
     "• A normal initial Hb does not exclude acute major hemorrhage.\n"
     "• A negative FAST does not exclude retroperitoneal bleeding.\n"
     "• Avoid delaying intervention for CT in persistently unstable patient."),
    ("06 — DISPOSITION", "warning", 
     "• Unstable patients require immediate trauma-level resuscitation and hemorrhage control.\n"
     "• High-grade injuries generally require admission and specialist monitoring.\n"
     "• Discharge after minor injury requires stable observations, controlled pain, adequate oral intake, clear follow-up/return precautions."),
    ("REFERENCES", "info", "AUA Urotrauma Guideline; EAU Urological Trauma Guidelines; ATLS.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Bladder Trauma and Rupture")] = [
    ("01 — RECOGNIZE", "info", 
     "Pelvic fracture, blunt lower abdominal trauma, penetrating injury, or trauma with a full bladder.\n"
     "• Gross hematuria, suprapubic pain, abdominal distension, or inability to void. Reduced urine output despite adequate fluid administration.\n"
     "• Urinary ascites, unexplained elevation of serum creatinine, or peritonitis may occur with intraperitoneal rupture.\n"
     "• Consider iatrogenic injury after pelvic surgery or instrumentation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma primary survey and treat shock immediately.\n"
     "• Assess for pelvic fracture, abdominal injury, and associated urethral injury.\n"
     "• Obtain CBC, renal function, electrolytes, urinalysis, and blood group/crossmatch when indicated.\n"
     "• [color=#991B1B]Avoid blind urethral catheterization if urethral injury is suspected.[/color]\n"
     "• Contact trauma surgery and urology early when bladder rupture suspected.\n"
     "• Arrange appropriate bladder imaging after stabilization."),
    ("03 — INVESTIGATIONS", "info", 
     "[color=#1E3A8A]CT Cystography or Conventional Retrograde Cystography[/color]\n"
     "• Properly performed retrograde cystography is the key diagnostic test when bladder rupture suspected. CT cystography commonly used in trauma centers.\n"
     "• Bladder must be adequately filled retrogradely with contrast per radiology protocol; routine IV contrast CT alone may miss a bladder rupture.\n"
     "• Gross hematuria with pelvic fracture is a major indication for bladder imaging.\n"
     "• Additional indications: gross hematuria after trauma without pelvic fracture, inability to void, or other strong clinical evidence.\n\n"
     "[color=#1E3A8A]Laboratory[/color]\n"
     "• CBC, creatinine, electrolytes, urinalysis. Monitor serial Hb and renal function."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Extraperitoneal Bladder Rupture[/color]\n"
     "• Many uncomplicated extraperitoneal ruptures can be managed with continuous bladder drainage.\n"
     "• Insert urethral catheter only when urethral injury excluded or safe placement confirmed by experienced clinician.\n"
     "• Maintain closed urinary drainage per urology instructions. Monitor urine output, hematuria, infection, abdominal findings, renal function.\n"
     "• Follow-up cystography generally performed before catheter removal.\n"
     "• Consider surgery when: bladder-neck involvement, bone fragments penetrating bladder, associated rectal/vaginal injury, bladder-wall entrapment or another indication for abdominal surgery, or complicated/failing rupture.\n\n"
     "[color=#1E3A8A]Intraperitoneal Bladder Rupture[/color]\n"
     "• Usually requires urgent surgical repair. Arrange urgent urological and trauma surgical management. Provide resuscitation, analgesia, perioperative antibiotics per local protocol. Repair bladder defect and establish postoperative urinary drainage. Assess associated intra-abdominal injuries."),
    ("05 — WARNINGS", "danger", 
     "• Intraperitoneal bladder rupture can cause urinary peritonitis, sepsis, and metabolic abnormalities.\n"
     "• Do NOT assume that a pelvic fracture alone proves bladder rupture.\n"
     "• Do NOT rely on routine IV contrast CT without appropriate cystographic bladder filling to exclude rupture.\n"
     "• Avoid blind catheterization when urethral injury suspected."),
    ("06 — DISPOSITION", "warning", 
     "• Suspected/confirmed rupture requires urgent urological assessment and usually hospital admission.\n"
     "• Discharge with a catheter should occur only under documented specialist plan with catheter-care instructions and follow-up."),
    ("REFERENCES", "info", "AUA Urotrauma Guideline; EAU Urological Trauma Guidelines; ATLS.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Ureteric Colic")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden severe unilateral flank pain, often radiating to groin. Restlessness, nausea, vomiting, microscopic or visible hematuria. Patients may be unable to find a comfortable position.\n"
     "• Fever, rigors, hypotension, or systemic toxicity suggest infection and possible obstructed infected urinary system.\n"
     "• Reduced urine output, anuria, solitary kidney, bilateral obstruction, pregnancy, or known renal impairment increases urgency."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, pain severity, hydration, and evidence of sepsis.\n"
     "• Provide prompt analgesia and antiemetic therapy when indicated.\n"
     "• Obtain urinalysis, renal function, electrolytes, and pregnancy testing when relevant. Obtain urine culture if infection suspected.\n"
     "• Assess for red flags: fever, sepsis, anuria, AKI, solitary kidney, bilateral obstruction, uncontrolled pain/vomiting.\n"
     "• Arrange urgent urology assessment for infected obstruction, anuria, deteriorating renal function, or refractory symptoms."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis (blood, leukocytes, nitrites). Urine culture when infection suspected.\n"
     "• Creatinine, urea, electrolytes. CBC and inflammatory markers when infection/complications suspected.\n"
     "• Non-contrast CT kidneys/ureters/bladder is highly accurate in most nonpregnant adults when imaging indicated.\n"
     "• Ultrasound preferred initially in pregnancy; may be appropriate in selected younger patients or when radiation avoidance important.\n"
     "• Evaluate for alternative diagnoses if presentation atypical."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]First-Line Analgesia: NSAID[/color]\n"
     "• Example: Diclofenac 50 mg orally or 75 mg IM when appropriate; follow formulation-specific max dose and local protocol.\n"
     "• Avoid or use specialist guidance in significant renal impairment, active GI bleeding/ulceration, severe dehydration, NSAID allergy, relevant pregnancy stages.\n"
     "• Do NOT combine multiple NSAIDs. [color=#991B1B]NSAIDs may worsen kidney injury in dehydration or obstructive renal impairment. Select alternative when contraindicated.[/color]\n\n"
     "[color=#1E3A8A]Alternative Analgesia: Paracetamol[/color]\n"
     "• Adults commonly 500–1,000 mg orally or IV per formulation/local protocol. Respect maximum daily dose (lower limit in liver disease, low body weight, malnutrition, heavy alcohol use).\n\n"
     "[color=#1E3A8A]Antiemetic Treatment[/color]\n"
     "• For persistent nausea/vomiting. Select agent/dose according to age, pregnancy status, QT risk, concurrent meds, local protocol.\n\n"
     "[color=#1E3A8A]Medical Expulsive Therapy[/color]\n"
     "• Example: Tamsulosin 0.4 mg orally once daily in selected adults. Consider primarily for appropriately selected distal ureteric stones when stone size/location make spontaneous passage less likely but conservative management remains safe.\n"
     "• [color=#991B1B]Not a substitute for urgent decompression of infected obstruction or threatened renal function. Counsel about dizziness, orthostatic hypotension, possible ejaculatory adverse effects.[/color]\n\n"
     "[color=#1E3A8A]Infected Obstructed System[/color]\n"
     "• Treat as urological emergency. Start appropriate IV antibiotics promptly per local resistance patterns and sepsis protocols. Arrange urgent decompression with ureteric stent or percutaneous nephrostomy. Definitive stone removal generally delayed until infection controlled."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Base management on stone size, location, obstruction, symptoms, renal function, likelihood of spontaneous passage.\n"
     "• Options: observation, medical expulsive therapy in selected cases, ureteroscopy, shock-wave lithotripsy, percutaneous procedures.\n"
     "• Provide clear follow-up to confirm stone passage/resolution of obstruction. Analyze retrieved stones when appropriate and assess recurrent stone risk."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or arrange urgent urology management if: Fever/sepsis with suspected obstruction. Anuria, bilateral obstruction, solitary kidney with obstruction, or AKI. Pain/vomiting uncontrolled. Significant dehydration or inability to maintain oral intake. Pregnancy with concerning symptoms or complicated obstruction.\n"
     "• Discharge may be appropriate for stable patients with controlled symptoms, preserved renal function, no evidence of infection/high-risk obstruction, and reliable follow-up."),
    ("REFERENCES", "info", "EAU Urolithiasis Guidelines; NICE Renal and Ureteric Stones; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Urosepsis and Septic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "Suspected UTI with systemic illness or organ dysfunction. Fever/hypothermia, tachycardia, tachypnea, hypotension, confusion, oliguria, mottled skin.\n"
     "• Flank pain, dysuria, urinary frequency, suprapubic pain, CVA tenderness may be present. Older adults/immunocompromised may have few local urinary symptoms.\n"
     "• Consider obstructing ureteric stones, hydronephrosis, urinary retention, infected catheters, renal/perinephric abscess, recent urological procedures.\n"
     "• Septic shock suggested by persistent circulatory failure despite initial fluid resuscitation and may require vasopressors."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate local sepsis pathway; assess ABCDE. Give oxygen when hypoxemic; support ventilation as required.\n"
     "• Establish IV access; monitor BP, HR, RR, SpO2, temperature, mental status, urine output. Measure serum lactate when sepsis with hypoperfusion/shock suspected.\n"
     "• Obtain blood cultures and urine culture before antibiotics when no clinically significant delay.\n"
     "• [color=#991B1B]Start empiric IV antibiotics promptly, ideally within 1 hour for septic shock or high likelihood of sepsis, per local protocol.[/color]\n"
     "• Assess urgently for urinary obstruction and other sources requiring source control.\n"
     "• Request early critical care and urology input in shock, organ dysfunction, or suspected obstructed infection."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, urea, creatinine, LFTs, glucose.\n"
     "• Serum lactate with repeat measurement when initially elevated or perfusion remains impaired.\n"
     "• Blood cultures and urine culture. Urinalysis. Coagulation when indicated.\n"
     "• Renal and bladder ultrasound to identify hydronephrosis/retention.\n"
     "• CT abdomen/pelvis when needed to assess stones, obstruction, abscess, emphysematous infection, or another complicated source."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Selection depends on severity, likely source, prior cultures, recent antibiotic exposure, healthcare-associated infection, renal function, allergies, local resistance, risk of resistant organisms.\n"
     "• Example: Ceftriaxone 1–2 g IV every 24 hours for susceptible community-acquired urinary infection; severe sepsis may require upper end of range per local guidance.\n"
     "• [color=#991B1B]Ceftriaxone alone may be inadequate in healthcare-associated infection, suspected Pseudomonas, resistant organisms, or certain complicated infections. Select broader therapy when clinically indicated per local protocols.[/color]\n\n"
     "[color=#1E3A8A]IV Fluid Resuscitation[/color]\n"
     "• For sepsis-induced hypoperfusion or septic shock: balanced crystalloid or 0.9% NaCl per protocol. Initial volume ~30 mL/kg within first 3 hours is guideline-based starting point, NOT inflexible requirement.\n"
     "• Give fluid in reassessed boluses, particularly in HF, renal failure, or risk of fluid overload. Reassess BP, capillary refill, mental status, lung findings, urine output. Stop/reduce fluids if overload develops.\n\n"
     "[color=#1E3A8A]Vasopressor: Norepinephrine[/color]\n"
     "• For persistent hypotension despite appropriate initial fluid resuscitation, or earlier when profound shock requires it.\n"
     "• Start per local critical-care protocol, commonly 0.05–0.1 mcg/kg/min IV, titrate to perfusion targets. Prefer central venous catheter for ongoing infusion, but well-sited peripheral IV may be used temporarily in emergency with frequent site checks per local protocol.\n"
     "• Titrate to MAP target ~65 mmHg in most adults, individualized. Monitor BP continuously, rhythm, peripheral perfusion, urine output, lactate trend, IV site for extravasation.\n"
     "• [color=#991B1B]Norepinephrine is a high-alert medication. Verify concentration, dose units, and pump settings independently per local safety policy.[/color]\n\n"
     "[color=#1E3A8A]Source Control: Obstructed Infected Urinary System[/color]\n"
     "• Infected obstruction requires urgent drainage (ureteric stent or percutaneous nephrostomy). Antibiotics alone NOT sufficient when infected collecting system remains obstructed. Coordinate urgent decompression with urology/IR. Delay definitive stone removal until infection adequately controlled."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Tailor antimicrobial therapy to cultures, susceptibility, source, renal function, clinical response. Remove/replace infected urinary catheter when indicated. Drain obstructed systems/abscesses when required. Assess for additional sources/complications. Review antimicrobial duration and step-down therapy based on source control and response."),
    ("06 — DISPOSITION", "warning", 
     "• ICU or high-dependency care for: Persistent hypotension/vasopressor requirement. Altered mental status/respiratory failure. Rising lactate/persistent hypoperfusion. Significant AKI/other organ dysfunction. Need for urgent source control with ongoing instability.\n"
     "• [color=#991B1B]Patients with uncomplicated infection should NOT be labeled as having sepsis solely because of fever or positive urine test; diagnosis depends on overall clinical assessment and evidence of organ dysfunction.[/color]"),
    ("REFERENCES", "info", "Surviving Sepsis Campaign (2021); EAU Urological Infections/Urolithiasis Guidelines; SCCM Sepsis Resources; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Epididymo-Orchitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Unilateral scrotal pain and swelling, often developing over hours or days. Epididymal tenderness, scrotal erythema, possible fever.\n"
     "• Dysuria, urinary frequency, urethral discharge, or recent urinary instrumentation may be present.\n"
     "• Consider sexually transmitted pathogens in sexually active patients; urinary pathogens in older patients or those with urinary tract abnormalities.\n"
     "• [color=#991B1B]Testicular torsion must be excluded urgently[/color], especially with sudden severe pain, nausea, vomiting, high-riding testis, or absent cremasteric reflex."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, pain severity, systemic toxicity.\n"
     "• Perform focused abdominal, inguinal, genital, scrotal examination with appropriate consent and chaperone.\n"
     "• [color=#991B1B]If torsion strongly suspected: obtain immediate urological/surgical assessment; do NOT delay exploration for imaging.[/color]\n"
     "• Provide analgesia and scrotal support.\n"
     "• Obtain urine testing and STI testing when indicated.\n"
     "• Arrange urgent ultrasound with Doppler when diagnosis uncertain and imaging will not delay necessary intervention."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture.\n"
     "• First-catch urine NAAT for Chlamydia trachomatis and Neisseria gonorrhoeae when STI possible.\n"
     "• CBC and inflammatory markers when systemic infection suspected.\n"
     "• Scrotal ultrasound with Doppler when torsion, abscess, or uncertain diagnosis remains a concern.\n"
     "• Evaluate for urinary obstruction or structural urinary disease when suggested."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Rest and scrotal elevation/support. Wrapped cold packs intermittently if helpful (avoid direct ice contact). Appropriate analgesia. Encourage hydration according to status.\n\n"
     "[color=#1E3A8A]Antibiotic Therapy[/color]\n"
     "• Select treatment according to likely pathogen, STI risk, local resistance, allergies, local guidelines.\n"
     "• Example (Suspected STI): Ceftriaxone 500 mg IM once + Doxycycline 100 mg orally twice daily for 10 days. For patients ≥150 kg, some guidelines recommend ceftriaxone 1 g IM once.\n"
     "• Obtain appropriate STI specimens without unnecessarily delaying treatment. Counsel regarding adherence, adverse effects, partner evaluation, temporary abstinence from sexual activity until treatment completed and partners treated, per local guidance. Reassess if no improvement within 72 hours.\n"
     "• [color=#991B1B]This regimen is NOT suitable for every cause. Suspected enteric pathogens, gonorrhea resistance, severe infection, and local recommendations may require a different regimen.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Tailor antimicrobial treatment to culture/STI results. Evaluate sexual partners and arrange testing/treatment when STI identified/suspected. Consider abscess, infarction, torsion, or another diagnosis when clinical course atypical. Persistent swelling after treatment requires reassessment."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or obtain urgent specialist review for severe systemic illness, abscess, suspected infarction, inability to tolerate oral therapy, immunocompromise with significant infection, or unresolved concern for torsion."),
    ("REFERENCES", "info", "CDC STI Treatment Guidelines—Epididymitis; EAU Urological Infections Guidelines; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Difficult Urethral Catheterization")] = [
    ("01 — RECOGNIZE", "info", 
     "Inability to pass a urinary catheter despite appropriate initial attempts. Resistance, severe pain, urethral bleeding, or catheter coiling.\n"
     "• Potential causes: prostatic enlargement, urethral stricture, bladder-neck contracture, false passage, previous urethral surgery, urethral trauma.\n"
     "• [color=#991B1B]Repeated unsuccessful attempts increase risk of urethral injury, bleeding, and false passage formation.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Confirm indication for catheterization; consider whether catheter necessary.\n"
     "• Assess for urinary retention using bladder examination/ultrasound.\n"
     "• Ask about previous urethral stricture, prostate surgery, difficult catheterization, recent trauma.\n"
     "• [color=#991B1B]If pelvic trauma, blood at urethral meatus, perineal bruising, or suspected urethral injury: STOP blind catheterization and obtain urgent urological assessment.[/color]\n"
     "• Use adequate analgesia, appropriate positioning, sterile technique, generous sterile lubricant/anesthetic gel when suitable.\n"
     "• Stop if significant resistance or bleeding occurs; do NOT force catheter."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bladder scan to confirm retention and estimate bladder volume.\n"
     "• Renal function and electrolytes when retention prolonged/severe/associated with suspected renal impairment.\n"
     "• Retrograde urethrography when urethral injury suspected.\n"
     "• Flexible cystoscopy or specialist-directed imaging may be needed to assess strictures/other anatomical obstruction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Initial Catheterization Attempt[/color]\n"
     "• Use appropriately sized catheter selected according to anatomy/clinical indication. Ensure adequate lubrication and gentle technique.\n"
     "• Experienced clinician may consider different catheter type when prostatic obstruction/stricture suspected, provided urethral injury not suspected. Do NOT repeatedly attempt different catheters without clear plan.\n\n"
     "[color=#1E3A8A]Local Anesthetic Gel[/color]\n"
     "• Example: Lidocaine urethral gel, using product-specific adult dose and maximum allowable amount. Check concentration, dose, allergy history, product instructions. Use sterile single-use gel when available.\n"
     "• Instill gently according to product instructions and allow sufficient time for local anesthesia. Observe for discomfort, bleeding, or signs of local injury.\n"
     "• [color=#991B1B]Lidocaine toxicity is possible with excessive dosing/absorption. Account for other lidocaine products already administered.[/color]\n\n"
     "[color=#1E3A8A]Failed Catheterization[/color]\n"
     "• Stop further blind attempts after persistent resistance, significant pain, or bleeding.\n"
     "• Obtain urgent urological assistance for guidewire-assisted placement or flexible cystoscopic catheterization.\n"
     "• If urgent bladder drainage essential and urethral access unsafe/impossible: suprapubic catheterization may be required by trained clinician after assessment of contraindications/anatomy."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat underlying cause (urethral stricture, prostatic obstruction, bladder-neck contracture).\n"
     "• Document attempts, catheter type/size, resistance encountered, bleeding, and final drainage method.\n"
     "• Arrange follow-up when stricture or other structural abnormality suspected."),
    ("06 — DISPOSITION", "warning", 
     "• Patients with persistent retention, renal impairment, infection, urethral injury, or failed drainage need urgent specialist assessment.\n"
     "• Discharge with catheter should include documented drainage plan, catheter-care instructions, and follow-up."),
    ("REFERENCES", "info", "EAU Urological Trauma/Male LUTS Guidelines; AUA Urethral Stricture Guideline; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Obstructive Uropathy")] = [
    ("01 — RECOGNIZE", "info", 
     "Obstruction of urine flow at kidney, ureter, bladder outlet, or urethra.\n"
     "• Flank pain, reduced urine output, urinary retention, or anuria.\n"
     "• Bilateral obstruction or obstruction of a solitary functioning kidney can rapidly impair renal function.\n"
     "• Causes: stones, prostatic enlargement, urethral stricture, tumors, blood clots, external compression.\n"
     "• Fever, rigors, hypotension, or confusion in an obstructed patient suggests infected urinary system and requires emergency management."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess hemodynamic stability, pain, fever, urine output, signs of sepsis.\n"
     "• Measure bladder volume when lower urinary tract obstruction possible.\n"
     "• Obtain IV access and blood tests if severe obstruction, dehydration, infection, or AKI suspected. Record fluid intake and urine output.\n"
     "• Arrange urgent imaging and urology consultation for anuria, bilateral obstruction, solitary kidney obstruction, deteriorating renal function, or suspected infected obstruction.\n"
     "• [color=#991B1B]Do NOT delay drainage of an infected obstructed system while waiting for definitive stone treatment.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Urea, creatinine, electrolytes, glucose. CBC and inflammatory markers when infection suspected. Urinalysis and urine culture.\n"
     "• Renal and bladder ultrasound to identify hydronephrosis and retention.\n"
     "• CT imaging when needed to identify site and cause of obstruction.\n"
     "• ECG when severe hyperkalemia suspected/confirmed."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Lower Urinary Tract Obstruction[/color]\n"
     "• Bladder decompression usually required when acute urinary retention confirmed. Use urethral catheterization only when safe; suspected urethral injury requires specialist assessment. If urethral catheterization fails/contraindicated: urgent urological assessment for alternative drainage.\n\n"
     "[color=#1E3A8A]Upper Urinary Tract Obstruction[/color]\n"
     "• Arrange urgent urological drainage when obstruction threatens renal function, causes anuria, or is associated with infection.\n"
     "• Options: ureteric stent or percutaneous nephrostomy, selected according to anatomy, availability, clinical circumstances. Definitive treatment of stones/tumors/strictures follows stabilization and appropriate assessment.\n\n"
     "[color=#1E3A8A]Hyperkalemia[/color]\n"
     "• For confirmed/strongly suspected clinically significant hyperkalemia, particularly with ECG changes. Obtain ECG and urgent potassium when possible without delaying treatment of life-threatening arrhythmia.\n"
     "• Give IV calcium for cardiac membrane stabilization when indicated by ECG changes/severe hyperkalemia, per local emergency protocol. Use insulin with glucose and other potassium-lowering measures per institutional pathway. Monitor glucose, potassium, ECG, renal function. Obtain urgent nephrology/critical care input for refractory hyperkalemia or severe renal failure.\n"
     "• [color=#991B1B]Calcium stabilizes myocardium but does NOT remove potassium from body. Repeat potassium and glucose measurements are essential.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Relieve obstruction. Treat underlying cause. Monitor renal recovery and complications. Consider nephrology input if renal impairment persists after drainage or if dialysis indications develop."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with anuria, bilateral obstruction, obstruction of solitary functioning kidney, AKI, significant electrolyte disturbance, infected obstruction, or need for urgent intervention."),
    ("REFERENCES", "info", "EAU Urolithiasis/Urological Infections Guidelines; NICE AKI Guidance; KDIGO AKI Guideline; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Post-Obstructive Diuresis")] = [
    ("01 — RECOGNIZE", "info", 
     "High urine output after relief of urinary obstruction, commonly after catheterization for prolonged retention or drainage of bilateral obstruction.\n"
     "• Commonly used clinical definition: urine output >200 mL/hour for two consecutive hours or >3 L in 24 hours.\n"
     "• Patient may develop thirst, dizziness, hypotension, dehydration, weakness.\n"
     "• Electrolyte abnormalities may include hypokalemia, sodium disturbances, magnesium abnormalities.\n"
     "• Distinguish transient physiologic diuresis from persistent pathologic diuresis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Measure and document urine output hourly in high-risk patients. Record fluid intake, vital signs, clinical volume status.\n"
     "• Obtain serum sodium, potassium, bicarbonate, urea, creatinine, magnesium when significant diuresis present.\n"
     "• Assess for orthostatic symptoms, hypotension, dehydration.\n"
     "• [color=#991B1B]Do NOT automatically clamp urinary catheter or stop bladder drainage solely because large volume has drained.[/color]\n"
     "• Admit or closely observe patients with persistent high output, significant electrolyte abnormalities, renal impairment, or hemodynamic instability."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial electrolytes and renal function; frequency depends on urine output/clinical severity.\n"
     "• Urine osmolality and urine electrolytes may help evaluate persistent/unexplained diuresis.\n"
     "• ECG if significant potassium abnormalities suspected.\n"
     "• Monitor daily weight and fluid balance in patients with ongoing diuresis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid Replacement[/color]\n"
     "• Principle: Replace losses according to hemodynamic status, oral tolerance, laboratory findings, ongoing urine output rather than fixed volume for every patient.\n"
     "• Encourage oral fluids when patient alert, stable, able to drink safely. Use IV crystalloid when oral intake inadequate or significant hypovolemia present.\n"
     "• In stable patient with ongoing post-obstructive diuresis, commonly used starting strategy: replace approximately 50–75% of preceding urine output, then adjust according to volume status and electrolytes.\n"
     "• [color=#991B1B]This is NOT a universal formula; avoid both inadequate replacement and excessive fluid administration. In shock, follow resuscitation protocol rather than routine post-obstructive replacement strategy.[/color]\n\n"
     "[color=#1E3A8A]Electrolyte Correction[/color]\n"
     "• Replace potassium, magnesium, other electrolytes according to measured deficits and local protocols. Correct sodium abnormalities carefully, following established limits for rate of correction.\n"
     "• Reassess electrolytes frequently when losses substantial or replacement being given.\n"
     "• [color=#991B1B]Excessive replacement can perpetuate diuresis and cause fluid overload. Inadequate replacement can lead to hypovolemia, hypotension, and AKI.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Continue monitoring until urine output declines and volume status/electrolytes stabilize. Investigate persistent diuresis for ongoing tubular dysfunction or another cause. Plan trial without catheter or definitive management of underlying obstruction only when clinically appropriate."),
    ("06 — DISPOSITION", "warning", 
     "• Patients with persistent marked diuresis, hypotension, significant sodium/potassium abnormalities, or impaired renal function require hospital observation or admission."),
    ("REFERENCES", "info", "NICE AKI Guidance; KDIGO AKI Guideline; Standard urology/nephrology references; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Pyelonephritis with Complications")] = [
    ("01 — RECOGNIZE", "info", 
     "Fever, rigors, flank pain, CVA tenderness, nausea, vomiting. Dysuria, urinary frequency, urgency may accompany upper urinary tract symptoms.\n"
     "• Complicated infection more likely with urinary obstruction, stones, structural abnormalities, pregnancy, immunosuppression, diabetes, renal impairment, or recent instrumentation.\n"
     "• Persistent fever or clinical deterioration despite appropriate antibiotics raises concern for renal abscess, perinephric abscess, obstruction, or resistant pathogens.\n"
     "• Confusion, hypotension, tachypnea, oliguria, or elevated lactate may indicate sepsis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for sepsis, shock, dehydration, AKI.\n"
     "• Obtain IV access and start resuscitation when clinically indicated.\n"
     "• Obtain urinalysis and urine culture before antibiotics when this does not significantly delay treatment.\n"
     "• Obtain blood cultures when sepsis, severe systemic illness, or bacteremia suspected.\n"
     "• Start empiric antibiotics promptly, guided by severity, prior microbiology, allergies, renal function, local resistance patterns.\n"
     "• Assess for obstruction and arrange urgent imaging when clinically indicated.\n"
     "• Seek urgent urology input if infected obstruction or drainable abscess suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture with susceptibility testing.\n"
     "• CBC, renal function, electrolytes, inflammatory markers.\n"
     "• Blood cultures and lactate in suspected sepsis.\n"
     "• Renal ultrasound to assess hydronephrosis/obstruction.\n"
     "• CT abdomen/pelvis when complicated infection, abscess, emphysematous infection, obstruction, or poor response to treatment suspected.\n"
     "• In pregnancy, choose imaging and antibiotics according to pregnancy-specific guidance."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric Antibiotic Therapy[/color]\n"
     "• Choose according to illness severity, local antibiograms, prior cultures, recent antibiotic use, allergy history, pregnancy status, renal function.\n"
     "• Example: Ceftriaxone 1–2 g IV every 24 hours for appropriate susceptible infections; severe illness may require regimen selected under local sepsis guidance.\n"
     "• [color=#991B1B]Ceftriaxone may not provide adequate coverage for all resistant/healthcare-associated pathogens. Critically ill patients may require broader empiric therapy selected according to local guidance.[/color]\n\n"
     "[color=#1E3A8A]Supportive Care[/color]\n"
     "• Appropriate analgesia and antiemetics. Replace fluids according to clinical volume status. Monitor urine output and renal function. Avoid nephrotoxic medications where possible in AKI.\n\n"
     "[color=#1E3A8A]Renal or Perinephric Abscess[/color]\n"
     "• Obtain specialist assessment and appropriate imaging. Continue antibiotics directed by likely pathogens and culture results. Drainage may be required depending on abscess size, location, clinical response, patient stability.\n\n"
     "[color=#1E3A8A]Infected Obstruction[/color]\n"
     "• Treat as emergency requiring antibiotics and urgent urinary drainage. Ureteric stent or percutaneous nephrostomy may be needed. Antibiotics alone NOT sufficient when infected collecting system remains obstructed."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Adjust antibiotics according to cultures, clinical response, renal function. Identify and correct urinary obstruction when present. Evaluate for abscess or resistant organisms if patient fails to improve as expected. Determine duration/route of antibiotic treatment according to pathogen, severity, source control, local guidelines."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for sepsis, hemodynamic instability, persistent vomiting, significant dehydration, AKI, pregnancy with systemic illness, suspected obstruction/abscess, or inability to take oral medication.\n"
     "• Outpatient management appropriate only for selected stable patients who can tolerate oral treatment and have reliable follow-up and clear return precautions."),
    ("REFERENCES", "info", "EAU Urological Infections Guidelines; NICE Pyelonephritis; Surviving Sepsis Campaign; Local protocols.")
]


# ==================== NEW UROLOGY TOPICS (22-31) ====================

UROLOGY_TOPICS[("Urology Emergencies", "Acute Scrotal Pain: Differential Diagnosis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute scrotal pain is a time-sensitive presentation. Testicular torsion must be considered first because delayed treatment can result in testicular loss.\n"
     "Important differential diagnoses include:\n"
     "• Testicular torsion.\n"
     "• Epididymitis and epididymo-orchitis.\n"
     "• Testicular rupture or blunt scrotal trauma.\n"
     "• Incarcerated or strangulated inguinal hernia.\n"
     "• Testicular appendage torsion.\n"
     "• Scrotal abscess or severe soft-tissue infection.\n"
     "• Referred pain from ureteric stones or other abdominal pathology.\n\n"
     "Clinical clues:\n"
     "• Sudden severe unilateral pain, nausea, vomiting, or a high-riding testis suggests torsion.\n"
     "• Gradually progressive pain, epididymal tenderness, dysuria, or fever may suggest epididymitis.\n"
     "• Trauma with marked swelling, bruising, or an abnormal testicular contour raises concern for rupture.\n"
     "• An irreducible painful groin mass with vomiting suggests an incarcerated or strangulated hernia."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, pain severity, and signs of shock or systemic infection.\n"
     "• Obtain a focused abdominal, inguinal, and genital examination with consent and a chaperone.\n"
     "• Establish the time of symptom onset and ask about trauma, urinary symptoms, sexual history when relevant, and previous episodes.\n"
     "• Provide prompt analgesia.\n"
     "• Request immediate urological or surgical assessment if torsion, testicular rupture, strangulated hernia, or a necrotizing infection is suspected.\n"
     "• Arrange Doppler ultrasound if the diagnosis is uncertain and imaging will not delay urgent surgical management."),
    ("03 — INVESTIGATIONS", "info", 
     "• Scrotal ultrasound with color Doppler when clinically appropriate.\n"
     "• Urinalysis and urine culture if urinary infection is suspected.\n"
     "• STI nucleic acid amplification testing when epididymitis due to a sexually transmitted infection is possible.\n"
     "• CBC, renal function, inflammatory markers, and blood cultures when systemic infection or significant trauma is suspected.\n"
     "• Additional abdominal or pelvic imaging if a referred cause or associated injury is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Select age-appropriate analgesic according to pain severity, contraindications, renal function, and local protocol.\n"
     "• Provide prompt pain relief without delaying surgical assessment.\n"
     "• Reassess pain, vital signs, and response to treatment.\n\n"
     "[color=#1E3A8A]Suspected Testicular Torsion[/color]\n"
     "• Treat as surgical emergency.\n"
     "• Obtain immediate urological consultation and prepare for surgical exploration when indicated.\n"
     "• Do not wait for laboratory results or ultrasound if clinical suspicion is high.\n"
     "• Manual detorsion may be attempted by a trained clinician while arranging surgery, but it must not delay operative management.\n\n"
     "[color=#1E3A8A]Suspected Epididymo-Orchitis[/color]\n"
     "• Obtain appropriate urine and STI testing.\n"
     "• Start empiric antibiotics according to suspected pathogen and local guidelines.\n"
     "• Reassess if diagnosis is uncertain or symptoms fail to improve.\n\n"
     "[color=#1E3A8A]Suspected Traumatic Testicular Injury[/color]\n"
     "• Provide analgesia and scrotal support.\n"
     "• Obtain urgent Doppler ultrasound if this does not delay necessary surgery.\n"
     "• Suspected testicular rupture requires urgent urological assessment and often surgical exploration."),
    ("05 — WARNINGS", "danger", 
     "• A normal or equivocal ultrasound does not reliably exclude torsion when clinical suspicion remains high. Preserve the testis by prioritizing timely surgical assessment."),
    ("06 — DEFINITIVE MANAGEMENT", "info", 
     "• Torsion: urgent surgical detorsion and orchiopexy, with management of the contralateral testis according to surgical practice.\n"
     "• Rupture: surgical exploration and repair when indicated.\n"
     "• Epididymo-orchitis: pathogen-directed antimicrobial therapy and follow-up.\n"
     "• Hernia: urgent surgical management if incarcerated or strangulated."),
    ("07 — DISPOSITION", "warning", 
     "• Any patient with suspected torsion, rupture, strangulated hernia, or necrotizing infection requires immediate specialist evaluation.\n"
     "• Discharge only after time-critical diagnoses reasonably excluded and clear treatment/follow-up plan established."),
    ("REFERENCES", "info", "EAU Paediatric Urology/Urological Infections Guidelines; AUA Acute Scrotum Resources; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Infected Ureteric Stone")] = [
    ("01 — RECOGNIZE", "info", 
     "Flank pain or renal colic with fever, rigors, or systemic illness.\n"
     "• Urinalysis may show pyuria, bacteriuria, or hematuria.\n"
     "• Hydronephrosis may be present on ultrasound or CT.\n"
     "• Hypotension, tachycardia, altered mental status, oliguria, or elevated lactate suggests severe infection or sepsis.\n"
     "• A patient may have significant obstruction even if urine output is initially preserved."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for sepsis and hemodynamic instability.\n"
     "• Establish IV access and obtain CBC, renal function, electrolytes, lactate when indicated, blood cultures, and urine culture.\n"
     "• Start empiric IV antibiotics promptly according to local resistance patterns and sepsis guidance.\n"
     "• Provide analgesia and appropriate fluid resuscitation based on clinical status.\n"
     "• Arrange urgent urology consultation for drainage.\n"
     "• Do not delay source control while waiting for definitive stone treatment or for a complete diagnostic workup in an unstable patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture.\n"
     "• Blood cultures in patients with systemic illness or suspected sepsis.\n"
     "• CBC, creatinine, urea, electrolytes, and lactate when indicated.\n"
     "• Renal ultrasound to identify hydronephrosis.\n"
     "• Non-contrast CT kidneys/ureters/bladder in suitable patients to define stone location and size; contrast-enhanced imaging may be needed when complications or alternative diagnoses suspected.\n"
     "• Monitor urine output and renal function."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Choose treatment according to severity, likely organisms, previous cultures, recent antibiotic exposure, allergy history, renal function, and local resistance patterns.\n"
     "• Example: Ceftriaxone 1–2 g IV every 24 hours for susceptible infections, according to local protocol.\n"
     "• [color=#991B1B]Ceftriaxone may be inadequate for resistant or healthcare-associated pathogens. Severe sepsis may require broader empiric coverage based on local antibiogram.[/color]\n\n"
     "[color=#1E3A8A]Urgent Urinary Drainage[/color]\n"
     "• Indication: Infected obstructed collecting system.\n"
     "• Options: Retrograde ureteric stent. Percutaneous nephrostomy.\n"
     "• Arrange urgent decompression by urology or interventional radiology. Monitor hemodynamics, urine output, renal function, response to antibiotics. Obtain cultures from drained system when appropriate.\n"
     "• [color=#991B1B]Antibiotics alone are NOT adequate source control for an infected obstructed kidney.[/color]\n\n"
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Use appropriate analgesic based on pain severity, renal function, contraindications. Avoid NSAIDs or use cautiously when significant AKI or dehydration present."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Stabilize the infection and achieve drainage first.\n"
     "• Delay definitive ureteroscopy or other stone-removal procedures until infection is controlled.\n"
     "• Tailor antibiotics to culture results and clinical response.\n"
     "• Establish a plan for subsequent stone removal and assessment of underlying cause."),
    ("06 — DISPOSITION", "warning", 
     "• Admission required for infected obstruction, systemic illness, AKI, or need for urgent drainage.\n"
     "• Patients with shock or organ dysfunction may require critical care."),
    ("REFERENCES", "info", "EAU Urolithiasis/Urological Infections Guidelines; Surviving Sepsis Campaign; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Bacterial Prostatitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute fever, chills, malaise, dysuria, urinary frequency, urgency. Pelvic, perineal, rectal, or lower back pain.\n"
     "• A tender prostate may be found on gentle rectal examination when clinically appropriate.\n"
     "• Acute urinary retention can occur.\n"
     "• Severe disease may progress to bacteremia, sepsis, or prostatic abscess.\n"
     "• Risk factors: urinary instrumentation, bladder outlet obstruction, recent catheterization, UTI."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, sepsis features, hydration, ability to pass urine.\n"
     "• Obtain urinalysis and urine culture before antibiotics when feasible without delaying treatment.\n"
     "• Obtain blood cultures when febrile with systemic illness or suspected sepsis.\n"
     "• Check renal function and electrolytes if retention, dehydration, or severe illness present.\n"
     "• [color=#991B1B]Avoid vigorous prostate massage because it can precipitate bacteremia.[/color]\n"
     "• Assess urgently for urinary retention and obtain urology input if drainage needed."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture.\n"
     "• CBC, renal function, electrolytes, inflammatory markers when indicated.\n"
     "• Blood cultures if systemic infection suspected.\n"
     "• Bladder scan if retention suspected.\n"
     "• Imaging with CT, MRI, or transrectal ultrasound may be needed if prostatic abscess suspected or patient fails to improve.\n"
     "• [color=#991B1B]PSA is NOT useful for diagnosing acute bacterial prostatitis because it may be transiently elevated during acute inflammation.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotic Therapy[/color]\n"
     "• Select according to illness severity, likely organisms, previous cultures, local resistance, allergy, renal function.\n"
     "• Stable patient suitable for oral treatment: Use appropriate oral antibiotic with prostatic penetration, per local guidelines and culture results. Fluoroquinolones or trimethoprim-based regimens may be options in selected patients when susceptibility and safety considerations support use.\n"
     "• Severely ill patient or suspected sepsis: Start IV antibiotics promptly per local severe urinary infection or sepsis guidance. Examples include ceftriaxone or broader-spectrum beta-lactams when indicated by severity and local resistance.\n"
     "• Review culture results and de-escalate when appropriate. Monitor temperature, symptoms, renal function, signs of complications. Duration commonly measured in weeks per local guidance.\n"
     "• [color=#991B1B]Fluoroquinolones have important potential adverse effects and resistance limitations. Do NOT prescribe empirically without considering local guidance, patient-specific contraindications, and susceptibility data.[/color]\n\n"
     "[color=#1E3A8A]Analgesia and Supportive Care[/color]\n"
     "• Appropriate analgesia and antipyretics. Maintain hydration according to volume status. Avoid unnecessary urethral instrumentation.\n\n"
     "[color=#1E3A8A]Acute Urinary Retention[/color]\n"
     "• Obtain urgent urological advice regarding bladder drainage.\n"
     "• Urethral catheterization may be difficult or undesirable in some cases; route should be selected by experienced clinician. Suprapubic drainage may be considered when urethral catheterization unsuitable or unsafe."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Tailor antimicrobial therapy to microbiology and response.\n"
     "• Evaluate persistent fever or symptoms for abscess or obstruction.\n"
     "• Drain prostatic abscess when indicated.\n"
     "• Address associated bladder outlet obstruction after acute infection controlled."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with sepsis, hypotension, significant dehydration, urinary retention requiring complex drainage, vomiting preventing oral treatment, suspected abscess, or major comorbidity requiring inpatient care."),
    ("REFERENCES", "info", "EAU Urological Infections Guidelines; NICE Prostatitis (Acute); Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Postrenal Acute Kidney Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute rise in serum creatinine due to impaired urinary drainage.\n"
     "• Oliguria or anuria may occur, but urine output can remain relatively preserved in partial obstruction.\n"
     "• Bilateral obstruction, bladder outlet obstruction, or obstruction of a solitary functioning kidney is particularly concerning.\n"
     "• Symptoms may include suprapubic fullness, flank pain, urinary hesitancy, weak stream, or overflow incontinence.\n"
     "• Hyperkalemia, metabolic acidosis, pulmonary edema, confusion, or uremic symptoms may indicate severe complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, vital signs, volume status.\n"
     "• Measure urine output and obtain urgent bladder scan when lower urinary tract obstruction possible.\n"
     "• Obtain blood tests: creatinine, urea, sodium, potassium, bicarbonate, glucose.\n"
     "• Obtain ECG urgently if hyperkalemia suspected/confirmed.\n"
     "• Review nephrotoxic medications and temporarily withhold relevant agents when clinically appropriate.\n"
     "• Arrange urgent urinary decompression when obstruction confirmed/strongly suspected and threatening renal function.\n"
     "• Seek urgent nephrology or critical care input for severe hyperkalemia, refractory acidosis, pulmonary edema, or other indications for renal replacement therapy."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial creatinine and electrolytes.\n"
     "• Urinalysis and urine culture if infection suspected.\n"
     "• Bladder scan and renal ultrasound to assess retention and hydronephrosis.\n"
     "• CT imaging when cause/level of obstruction remains unclear.\n"
     "• ECG for significant potassium abnormalities. Blood gas when severe acidosis/critical illness suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Relieve the Obstruction[/color]\n"
     "• Bladder outlet obstruction may require catheter drainage when urethral catheterization safe. Suspected urethral injury or failed catheterization requires specialist assessment.\n"
     "• Upper tract obstruction may require ureteric stent or percutaneous nephrostomy.\n"
     "• Infected obstruction requires antibiotics and urgent drainage.\n\n"
     "[color=#1E3A8A]Hyperkalemia Management[/color]\n"
     "• For severe hyperkalemia or hyperkalemia with ECG changes: emergency treatment. Give IV calcium for cardiac membrane stabilization when indicated. Administer insulin with glucose and other potassium-shifting/removal therapies per local emergency protocol.\n"
     "• Monitor ECG, glucose, potassium, renal function, response to treatment. Consider dialysis for refractory hyperkalemia or other established indications.\n"
     "• [color=#991B1B]Calcium does NOT lower serum potassium. Insulin can cause delayed hypoglycemia, so glucose monitoring is essential.[/color]\n\n"
     "[color=#1E3A8A]Fluid and Electrolyte Management[/color]\n"
     "• Correct hypovolemia if present, but do NOT give routine large-volume fluids to an oliguric patient without assessing volume status. Treat pulmonary edema and electrolyte disturbances per standard emergency protocols.\n"
     "• Monitor fluid balance closely after decompression because post-obstructive diuresis may develop."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat underlying cause (stones, prostatic obstruction, stricture, clot retention, malignancy).\n"
     "• Monitor for renal recovery after drainage. Seek nephrology input if kidney function does not improve or complications persist.\n"
     "• Review medications and arrange follow-up renal function testing."),
    ("06 — DISPOSITION", "warning", 
     "• Admission generally indicated for significant postrenal AKI, bilateral obstruction, solitary kidney obstruction, anuria, hyperkalemia, severe acidosis, infection, or need for urgent drainage."),
    ("REFERENCES", "info", "KDIGO AKI Guideline; NICE AKI Guidance; EAU Urolithiasis/Male LUTS Guidelines; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Iatrogenic Ureteric Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Possible injury after pelvic, colorectal, gynecological, vascular, or urological surgery.\n"
     "• Unexplained flank pain, fever, ileus, abdominal distension, or sepsis after an operation.\n"
     "• Urinary leakage from a surgical drain or wound.\n"
     "• Hydronephrosis, urinoma, reduced renal function, or persistent urinary leak.\n"
     "• Injury may be recognized during surgery or present hours to days later.\n"
     "• [color=#991B1B]Hematuria may be absent, so its absence does not exclude ureteric injury.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess hemodynamic stability, abdominal findings, urine output, evidence of sepsis.\n"
     "• Review operative report and timing of symptoms.\n"
     "• Obtain CBC, renal function, electrolytes, urine studies when indicated.\n"
     "• Contact operating surgical team and urology promptly.\n"
     "• Treat sepsis and resuscitate if clinically indicated.\n"
     "• Arrange appropriate imaging to identify site and extent of injury."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT urography with delayed excretory-phase imaging when patient stable and contrast imaging appropriate.\n"
     "• Retrograde pyelography may be used by urology to define injury and facilitate stent placement.\n"
     "• Ultrasound can identify hydronephrosis or fluid collection but may not fully characterize injury.\n"
     "• Check creatinine and monitor urine output.\n"
     "• Analyze drained fluid for creatinine when urinary leakage suspected and this will help establish diagnosis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Urinary Diversion[/color]\n"
     "• Options: Retrograde ureteric stenting, percutaneous nephrostomy, or another specialist-selected drainage strategy.\n"
     "• Indication: Obstruction, urinary leakage, or ureteric injury requiring diversion.\n"
     "• Arrange urgent urology and, when necessary, interventional radiology involvement. Monitor temperature, urine output, renal function, signs of infection. Drain significant infected/symptomatic urinoma when indicated. Start antibiotics when infection suspected/confirmed per local protocols.\n\n"
     "[color=#1E3A8A]Operative Repair[/color]\n"
     "• Indication: Complete transection, major devascularization, uncontrolled leakage, or injury not amenable to endoscopic/percutaneous management.\n"
     "• Repair depends on injury location, extent, tissue viability, patient's condition. Options include ureteric reimplantation, ureteroureterostomy, or more complex reconstruction.\n"
     "• In unstable patients, initial drainage and stabilization may precede definitive reconstruction."),
    ("05 — WARNINGS", "danger", 
     "• Delayed diagnosis can result in urinoma, sepsis, fistula, obstruction, and loss of renal function.\n"
     "• Normal urine output does NOT exclude unilateral ureteric injury.\n"
     "• Do NOT rely on routine abdominal CT without appropriate delayed excretory imaging when ureteric injury suspected."),
    ("06 — DEFINITIVE MANAGEMENT", "info", 
     "• Establish urinary drainage and control infection. Perform definitive repair/reconstruction when appropriate.\n"
     "• Arrange follow-up imaging and renal function assessment to identify persistent obstruction or stricture."),
    ("07 — DISPOSITION", "warning", 
     "• Suspected iatrogenic ureteric injury requires urgent specialist assessment.\n"
     "• Patients with sepsis, major urinary leakage, obstruction, or significant renal impairment generally require admission."),
    ("REFERENCES", "info", "EAU Urological Trauma Guidelines; AUA Urotrauma Guideline; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Gross Hematuria Without Clot Retention")] = [
    ("01 — RECOGNIZE", "info", 
     "Visible blood in urine, with or without dysuria, flank pain, or urinary frequency.\n"
     "• Possible causes: UTI, stones, malignancy, renal disease, trauma, recent instrumentation, anticoagulant-associated bleeding.\n"
     "• [color=#991B1B]Painless visible hematuria, especially in older adults or smokers, requires evaluation for urinary tract malignancy.[/color]\n"
     "• Clots, reduced urine output, suprapubic distension, or inability to void suggest evolving clot retention.\n"
     "• Hypotension, tachycardia, syncope, or pallor may indicate significant blood loss."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, hemodynamic stability, urine output, presence of clots or retention.\n"
     "• Establish IV access if bleeding heavy or patient unstable.\n"
     "• Obtain CBC, renal function, electrolytes, urinalysis, urine culture when infection suspected.\n"
     "• Check coagulation studies when anticoagulation, liver disease, or bleeding disorder relevant.\n"
     "• Obtain blood group and crossmatch if significant bleeding or transfusion may be required.\n"
     "• Seek urgent urological assessment for persistent heavy bleeding, falling hemoglobin, obstruction, trauma, or suspected malignancy."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis with microscopy to confirm red blood cells and assess proteinuria or infection.\n"
     "• Urine culture if infection suspected.\n"
     "• CBC and serial hemoglobin when ongoing bleeding significant.\n"
     "• Creatinine and electrolytes. Coagulation studies when indicated.\n"
     "• Renal and bladder ultrasound or CT imaging according to suspected cause and clinical stability.\n"
     "• Cystoscopy and upper urinary tract evaluation are often required for unexplained visible hematuria, even if bleeding resolves."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Initial Management[/color]\n"
     "• Provide analgesia when required. Treat confirmed/strongly suspected infection per local guidelines. Correct clinically significant coagulopathy when indicated.\n"
     "• Review anticoagulants/antiplatelet agents with prescribing team; interruption/reversal depends on bleeding severity, drug, indication, thrombotic risk.\n"
     "• Monitor urine output and watch for clot formation/retention.\n\n"
     "[color=#1E3A8A]Significant Ongoing Bleeding[/color]\n"
     "• Resuscitate patients with hemodynamic instability per local hemorrhage protocol. Transfuse according to clinical status, Hb, ongoing blood loss, local transfusion guidance.\n"
     "• If clots develop with impaired drainage, follow emergency pathway for clot retention and urgent urological management."),
    ("05 — WARNINGS", "danger", 
     "• Do NOT attribute visible hematuria solely to anticoagulant use without evaluating for underlying urinary tract cause.\n"
     "• Do NOT delay resuscitation in patient with hemorrhagic shock.\n"
     "• Avoid routine tranexamic acid for undifferentiated urinary bleeding without specialist guidance (urinary clot obstruction may occur)."),
    ("06 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat underlying cause. Arrange urological assessment for unexplained visible hematuria.\n"
     "• Consider nephrology assessment if findings suggest glomerular disease (significant proteinuria, dysmorphic red cells, red-cell casts)."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with hemodynamic instability, significant anemia, ongoing heavy bleeding, AKI, clot retention, or suspected serious underlying pathology.\n"
     "• Stable patients may be discharged only with reliable and timely investigation plan and clear return precautions."),
    ("REFERENCES", "info", "AUA Hematuria Resources; EAU Urological Cancers/Urolithiasis Guidelines; NICE Suspected Cancer Referral; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Renal Colic in Pregnancy")] = [
    ("01 — RECOGNIZE", "info", 
     "Flank pain, often radiating toward groin, with nausea or vomiting.\n"
     "• Hematuria may occur but its absence does not exclude a stone.\n"
     "• Physiological hydronephrosis of pregnancy can complicate ultrasound interpretation.\n"
     "• Fever, rigors, hypotension, or systemic illness may indicate infected obstructed system.\n"
     "• Differential diagnoses: pyelonephritis, obstetric emergencies, appendicitis, ovarian pathology, musculoskeletal pain."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess maternal vital signs, pain, hydration, sepsis features.\n"
     "• Assess gestational age and involve obstetric care when clinically indicated.\n"
     "• Obtain urinalysis, urine culture, CBC, renal function, electrolytes.\n"
     "• Provide pregnancy-appropriate analgesia and antiemetics.\n"
     "• Arrange renal and bladder ultrasound as first-line imaging.\n"
     "• Obtain urgent urology and obstetric input if infection, renal impairment, persistent pain, vomiting, or suspected obstruction."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture. CBC, creatinine, electrolytes.\n"
     "• Renal and bladder ultrasound; Doppler or transvaginal ultrasound may be helpful in selected cases.\n"
     "• MRI without gadolinium may be considered when ultrasound inconclusive and additional imaging needed.\n"
     "• Low-dose non-contrast CT may occasionally be justified when diagnosis remains uncertain and result will materially change management; requires individualized risk-benefit assessment and specialist input."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol generally preferred initial analgesic when appropriate. Severe pain may require short course of opioid under supervised care.\n"
     "• [color=#991B1B]NSAIDs should generally be avoided during pregnancy unless specialist determines use appropriate; particularly problematic from 20 weeks onward and contraindicated in third trimester under standard regulatory guidance.[/color]\n\n"
     "[color=#1E3A8A]Hydration and Antiemetics[/color]\n"
     "• Correct dehydration if present; forced fluid loading does not reliably expel a stone and may worsen discomfort. Select antiemetics using pregnancy-specific guidance and consider QT risk and concurrent medication.\n\n"
     "[color=#1E3A8A]Infected Obstruction or Threatened Renal Function[/color]\n"
     "• Start pregnancy-appropriate IV antibiotics promptly when infection suspected. Arrange urgent urinary drainage by ureteric stent or percutaneous nephrostomy when indicated. Coordinate care among urology, obstetrics, anesthesia, radiology.\n"
     "• [color=#991B1B]Do NOT delay necessary source control because of pregnancy.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Many uncomplicated stones can initially be managed conservatively with close monitoring. Persistent obstruction, uncontrolled symptoms, or complications may require ureteroscopy or temporary drainage.\n"
     "• Select procedures and imaging according to gestational age, clinical urgency, local expertise."),
    ("06 — WARNINGS", "danger", 
     "• Fever or sepsis with urinary obstruction is an emergency.\n"
     "• Do NOT assume hydronephrosis is caused by a stone; physiological dilatation is common during pregnancy.\n"
     "• Avoid medications with pregnancy-related risks unless clinical benefit and safety assessed."),
    ("07 — DISPOSITION", "warning", 
     "• Admit patients with infection, AKI, uncontrolled pain/vomiting, significant obstruction, or obstetric concerns.\n"
     "• Outpatient care requires stable maternal status, controlled symptoms, no evidence of infection/threatened renal function, and reliable follow-up."),
    ("REFERENCES", "info", "EAU Urolithiasis Guidelines; ACOG Diagnostic Imaging During Pregnancy; NICE Renal/Ureteric Stones; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Renal or Perinephric Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "Persistent fever, flank pain, and malaise despite treatment for urinary infection.\n"
     "• Nausea, vomiting, CVA tenderness, or systemic toxicity.\n"
     "• Risk factors: diabetes, urinary obstruction, stones, immunosuppression, recent urinary instrumentation.\n"
     "• Renal abscess involves renal parenchyma; perinephric abscess extends into surrounding space.\n"
     "• Severe cases may progress to sepsis or septic shock."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs and sepsis-related organ dysfunction.\n"
     "• Establish IV access and obtain CBC, renal function, electrolytes, lactate when indicated, blood cultures, urine culture.\n"
     "• Start empiric IV antibiotics promptly when severe infection suspected.\n"
     "• Assess for urinary obstruction and arrange urgent imaging.\n"
     "• Consult urology and interventional radiology early if collection requiring drainage suspected.\n"
     "• Provide fluids according to volume status and monitor urine output."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urinalysis and urine culture. Blood cultures in systemic illness.\n"
     "• CBC, renal function, electrolytes, inflammatory markers.\n"
     "• Contrast-enhanced CT is often most informative imaging test for renal/perinephric abscess when clinically appropriate.\n"
     "• Ultrasound may identify collection but can be less sensitive for defining extent.\n"
     "• Obtain cultures from drained material when drainage performed."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV Antibiotics[/color]\n"
     "• Choose therapy according to severity, likely organisms, prior cultures, recent antibiotic exposure, local resistance, allergy, renal function. Ceftriaxone may be suitable for selected community-acquired infections; severe illness or resistant-organism risk may require broader therapy per local guidance.\n"
     "• Adjust treatment according to culture results and clinical response. Monitor temperature, hemodynamics, renal function, inflammatory markers, clinical improvement. Reassess promptly if fever or systemic illness persists.\n\n"
     "[color=#1E3A8A]Drainage[/color]\n"
     "• Indications may include: Large/enlarging abscess. Persistent sepsis or failure to improve with appropriate antibiotics. Obstructed infected urinary system. Collection accessible and judged likely to benefit from drainage.\n"
     "• Procedure: Arrange image-guided percutaneous drainage when appropriate. Surgical drainage or other interventions may be required in selected complex cases. Treat any associated urinary obstruction.\n"
     "• [color=#991B1B]There is NO single abscess-size threshold that determines drainage for every patient. Decisions depend on clinical stability, collection characteristics, response to antibiotics, and specialist assessment.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Tailor antibiotics to cultures and susceptibility. Drain collections when indicated. Relieve associated obstruction.\n"
     "• Repeat imaging when clinical course suggests persistent/recurrent infection. Address contributing factors (stones, diabetes, urinary tract abnormalities)."),
    ("06 — DISPOSITION", "warning", 
     "• Hospital admission generally required for confirmed renal/perinephric abscess.\n"
     "• Patients with sepsis, obstruction, or need for drainage require urgent specialist management and may need critical care."),
    ("REFERENCES", "info", "EAU Urological Infections Guidelines; Surviving Sepsis Campaign; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Emphysematous Pyelonephritis")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe upper urinary tract infection associated with gas within renal parenchyma or surrounding tissues.\n"
     "• Most commonly associated with diabetes mellitus or urinary obstruction.\n"
     "• Fever, flank pain, vomiting, confusion, hypotension, signs of sepsis may occur.\n"
     "• Presentation may be nonspecific, particularly in patients with diabetes or impaired immunity.\n"
     "• Severe disease can progress rapidly to shock, AKI, multiorgan dysfunction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate sepsis pathway and assess airway, breathing, circulation, organ dysfunction.\n"
     "• Obtain IV access, CBC, renal function, electrolytes, lactate when indicated, blood cultures, urine culture.\n"
     "• Start broad-spectrum IV antibiotics promptly according to local resistance patterns and severity.\n"
     "• Begin hemodynamic resuscitation with reassessment of fluid responsiveness and signs of overload.\n"
     "• Arrange urgent CT imaging when patient stable enough; CT important for defining gas distribution and associated obstruction.\n"
     "• Request urgent urology and critical care assessment.\n"
     "• Identify and relieve urinary obstruction when present."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, renal function, electrolytes, glucose, lactate.\n"
     "• Blood cultures and urine culture. Urinalysis.\n"
     "• CT abdomen/pelvis to assess gas within kidney, perinephric tissues, collecting system, and to identify obstruction or abscess.\n"
     "• Monitor urine output, BP, lactate, renal function."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Broad-Spectrum IV Antibiotics[/color]\n"
     "• Choose therapy based on severity, likely pathogens, local resistance, previous cultures, allergy, renal function. Severe disease may require antipseudomonal beta-lactam or another broad-spectrum regimen under local sepsis protocol. Consider resistant organisms based on prior healthcare exposure, antibiotic use, local epidemiology.\n"
     "• Adjust doses for renal function where necessary. Review cultures and de-escalate when clinically appropriate.\n\n"
     "[color=#1E3A8A]Resuscitation and Organ Support[/color]\n"
     "• Give IV crystalloid for sepsis-induced hypoperfusion, reassessing frequently. Use vasopressors when hypotension persists despite appropriate resuscitation, following critical-care protocol. Monitor oxygenation, mental status, urine output, lactate, electrolytes. Provide glucose management and support other failing organs.\n\n"
     "[color=#1E3A8A]Source Control[/color]\n"
     "• Arrange urgent decompression of obstructed collecting system. Percutaneous drainage may be required for drainable collection or selected cases of extensive infection.\n"
     "• Nephrectomy may be necessary in selected patients with uncontrolled infection or deterioration despite appropriate treatment and less invasive measures; decision requires specialist assessment."),
    ("05 — WARNINGS", "danger", 
     "• This is a life-threatening infection, NOT a routine outpatient UTI.\n"
     "• Do NOT delay antibiotics or source control in a deteriorating patient.\n"
     "• Imaging and procedures must NOT delay immediate resuscitation in an unstable patient."),
    ("06 — DEFINITIVE MANAGEMENT", "info", 
     "• Combine effective antimicrobial therapy, correction of obstruction, and drainage or surgery when indicated.\n"
     "• Use CT findings, clinical status, renal function, response to treatment to guide further intervention.\n"
     "• Arrange follow-up for renal recovery and control of contributing conditions."),
    ("07 — DISPOSITION", "warning", 
     "• All suspected/confirmed cases require hospital admission.\n"
     "• Patients with shock, organ dysfunction, or need for vasopressor support should be managed in critical care."),
    ("REFERENCES", "info", "EAU Urological Infections Guidelines; Surviving Sepsis Campaign; Local protocols.")
]

UROLOGY_TOPICS[("Urology Emergencies", "Acute Urinary Retention with High-Risk Complications")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden inability to void, often with suprapubic pain and palpable/ultrasound-confirmed distended bladder.\n"
     "• Overflow incontinence may occur, particularly in chronic retention.\n"
     "• Causes: benign prostatic enlargement, urethral stricture, medications, constipation, neurological disease, postoperative retention.\n"
     "• [color=#991B1B]High-risk features: fever/sepsis, AKI, hydronephrosis, gross hematuria with clots, neurological deficits, suspected urethral injury.[/color]\n"
     "• New saddle anesthesia, bilateral leg weakness, or bowel dysfunction raises concern for cauda equina syndrome and requires emergency spinal assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, pain, bladder distension, neurological symptoms.\n"
     "• Confirm retention with bladder scan/ultrasound when available.\n"
     "• Obtain renal function and electrolytes when retention prolonged, severe, recurrent, or associated with systemic illness.\n"
     "• Relieve retention promptly when safe.\n"
     "• [color=#991B1B]If urethral injury suspected, do NOT perform blind urethral catheterization; seek urgent specialist evaluation.[/color]\n"
     "• Monitor urine output and hemodynamic status after decompression, particularly in chronic or high-volume retention."),
    ("03 — INVESTIGATIONS", "info", 
     "• Bladder scan and post-void residual measurement when relevant.\n"
     "• Creatinine, urea, electrolytes, urinalysis. Urine culture if infection suspected.\n"
     "• Renal ultrasound when renal impairment, hydronephrosis, or chronic high-volume retention suspected.\n"
     "• Neurological examination and urgent spinal imaging when cauda equina syndrome or other compressive neurological cause suspected.\n"
     "• Review medications that can contribute to retention (anticholinergics, opioids, sympathomimetics)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Bladder Decompression[/color]\n"
     "• Urethral catheterization commonly initial approach when no contraindication. Use sterile technique and appropriate catheter selection.\n"
     "• If catheterization difficult, stop repeated traumatic attempts and obtain experienced assistance.\n"
     "• Suprapubic catheterization may be required when urethral access unsafe/unsuccessful, according to specialist assessment.\n\n"
     "[color=#1E3A8A]Monitoring After Decompression[/color]\n"
     "• Record initial drained volume and monitor subsequent urine output. Watch for post-obstructive diuresis, hypotension, hematuria, electrolyte abnormalities.\n"
     "• Check renal function/electrolytes when retention prolonged, high-volume, or associated with complications.\n"
     "• [color=#991B1B]Do NOT routinely clamp catheter simply because a large volume drains; manage drainage and monitoring according to clinical status and local protocol.[/color]\n\n"
     "[color=#1E3A8A]Alpha-Blocker Therapy[/color]\n"
     "• Example: Tamsulosin 0.4 mg orally once daily may be used in selected adult men with suspected prostatic outlet obstruction, per local guidance.\n"
     "• Review BP, dizziness, falls risk, interactions, contraindications. Consider as part of plan for supervised trial without catheter, NOT substitute for urgent decompression.\n"
     "• [color=#991B1B]Tamsulosin does NOT provide immediate relief of acute retention. It may cause orthostatic hypotension and dizziness.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat underlying cause. Arrange trial without catheter when clinically appropriate and follow local urology guidance.\n"
     "• Investigate recurrent retention, renal impairment, hydronephrosis, or suspected neurological disease. Review and adjust causative medications when appropriate.\n"
     "• Refer for definitive management of prostatic enlargement, urethral stricture, or other structural obstruction."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or obtain urgent specialist management for AKI, significant electrolyte disturbance, sepsis, hydronephrosis with complications, suspected neurological compression, traumatic urethral injury, or failed drainage.\n"
     "• Stable patients may be discharged with catheter only when appropriate follow-up plan, catheter-care instructions, and return precautions in place."),
    ("REFERENCES", "info", "EAU Male LUTS Guidelines; NICE LUTS in Men; KDIGO AKI Guideline; Local protocols.")
]