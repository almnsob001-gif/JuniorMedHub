# data_obgyn.py

OBGYN_DATA = {
    "Obstetric & Gynecological": {
        "Obstetric Hemorrhage & Shock": [
            "Postpartum Hemorrhage (PPH)", "Placental Abruption", 
            "Placenta Previa with Major Bleeding", "Uterine Rupture", 
            "Retained Placenta", "Amniotic Fluid Embolism (AFE)", 
            "Severe Vaginal/Cervical Laceration", "Acute Obstetric Hemorrhagic Shock"
        ],
        "Hypertensive Disorders": [
            "Severe Preeclampsia and Eclampsia", "HELLP Syndrome", 
            "Postpartum Headache: Stroke, CVST, and Hemorrhage"
        ],
        "Early Pregnancy & Ectopic": [
            "Ruptured Ectopic Pregnancy", "Miscarriage with Hemorrhage", 
            "Septic Miscarriage", "Hyperemesis Gravidarum", 
            "Ovarian Torsion in Pregnancy"
        ],
        "Labor & Delivery Emergencies": [
            "Umbilical Cord Prolapse", "Shoulder Dystocia", 
            "Preterm Prelabor Rupture of Membranes (PPROM)", 
            "Preterm Labor", "Breech Presentation and Complicated Delivery", 
            "Multiple Pregnancy with Complications"
        ],
        "Maternal Critical Care": [
            "Maternal Sepsis and Septic Shock", "Maternal Cardiac Arrest", 
            "Pulmonary Embolism in Pregnancy and Postpartum", 
            "Trauma in Pregnancy", "Postpartum Venous Thromboembolism", 
            "Peripartum Cardiomyopathy", "Acute Fatty Liver of Pregnancy (AFLP)", 
            "Peripartum Aortic Dissection", "Pregnancy-Associated AKI", 
            "Severe Hypoglycemia and DKA"
        ],
        "Gynecologic Emergencies": [
            "Ovarian Torsion", "Acute Heavy Uterine Bleeding", 
            "Pelvic Inflammatory Disease (PID) with Sepsis", 
            "Ruptured Hemorrhagic Ovarian Cyst", "Tubo-Ovarian Abscess (TOA)", 
            "Uterine Arteriovenous Malformation (AVM)", 
            "Ovarian Hyperstimulation Syndrome (OHSS)", "Postpartum Endometritis"
        ]
    }
}

OBGYN_TOPICS = {}

OBGYN_TOPICS[("Obstetric & Gynecological", "Postpartum Hemorrhage (PPH)")] = [
    ("01 — RECOGNITION", "info", 
     "Excessive bleeding after childbirth or any bleeding causing hemodynamic instability.\n\n"
     "• Warning signs: tachycardia, hypotension, pallor, altered mental status, oliguria, cold extremities.\n"
     "• Do not wait for a specific measured blood-loss threshold if the patient is deteriorating.\n"
     "• Consider uterine atony, retained placental tissue, genital tract trauma, and coagulopathy."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call the obstetric, anesthesia, blood bank, and senior emergency teams.\n"
     "• Assess airway, breathing, circulation, and mental status.\n"
     "• Give high-flow oxygen if hypoxemic or critically unstable.\n"
     "• Establish two large-bore IV lines; send CBC, blood group/crossmatch, coagulation profile, fibrinogen, electrolytes, and blood gas/lactate.\n"
     "• Begin warmed isotonic crystalloid while arranging blood products for significant ongoing hemorrhage.\n"
     "• Activate the massive hemorrhage protocol when indicated.\n"
     "• Quantify blood loss and monitor vital signs frequently."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Uterine atony[/color]\n"
     "• Perform uterine massage and assess uterine tone.\n"
     "• Administer oxytocin according to the local PPH protocol.\n"
     "• Inspect for retained tissue and genital tract trauma; do not assume atony is the only cause.\n\n"
     "[color=#1E3A8A]Oxytocin[/color]\n"
     "• Dose: 10 IU IM or a slow IV dose, followed when needed by an infusion according to local protocol.\n"
     "• Administration: Avoid rapid IV bolus because severe hypotension and cardiovascular effects may occur.\n\n"
     "[color=#1E3A8A]Tranexamic acid (TXA)[/color]\n"
     "• Dose: 1 g IV over 10 minutes as soon as possible and within 3 hours of birth. A second 1 g dose may be given if bleeding continues after 30 minutes.\n"
     "• Administration: Give early alongside standard PPH treatment.\n\n"
     "[color=#1E3A8A]Additional measures[/color]\n"
     "• Consider additional uterotonics according to contraindications (Ergometrine avoided in hypertension; Carboprost avoided in asthma).\n"
     "• Consider uterine balloon tamponade, operative intervention, embolization, and blood component therapy if bleeding persists."),
    ("04 — WARNINGS", "danger", 
     "• Persistent hemorrhage or shock requires urgent escalation; do not delay surgery while repeatedly trying medications.\n"
     "• Consider coagulopathy, retained placenta, uterine rupture, and genital tract lacerations.\n"
     "• Do not delay definitive hemorrhage control while administering TXA."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for monitoring after significant PPH.\n"
     "• Escalate to operating theatre, higher-level care, or ICU according to hemodynamic status and ongoing blood loss."),
    ("REFERENCES", "info", "WHO PPH Guidelines, 2025; FIGO recommendations.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Severe Preeclampsia and Eclampsia")] = [
    ("01 — RECOGNITION", "info", 
     "• New hypertension after 20 weeks of pregnancy with proteinuria or evidence of maternal organ dysfunction.\n"
     "• Severe-range blood pressure: systolic ≥160 mmHg or diastolic ≥110 mmHg.\n"
     "• Severe features: persistent headache, visual disturbance, epigastric/RUQ pain, pulmonary edema, thrombocytopenia, renal impairment, or elevated liver enzymes.\n"
     "• Eclampsia is a new-onset seizure associated with preeclampsia when another cause is not more likely."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call obstetrics, anesthesia, and neonatal teams as appropriate.\n"
     "• Position laterally during a seizure; protect from injury and maintain the airway.\n"
     "• Do not restrain the patient or place objects in the mouth.\n"
     "• Assess oxygenation, circulation, blood pressure, and neurological status.\n"
     "• Establish IV access; obtain CBC/platelets, renal and liver function, urine protein assessment.\n"
     "• Assess fetal status when maternal stabilization permits."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Magnesium sulfate for eclampsia/seizure prophylaxis[/color]\n"
     "• Dose: 4–6 g loading dose over 15–30 minutes, followed by 1–2 g/hour.\n"
     "• Monitoring: Monitor respiratory rate, SpO2, deep tendon reflexes, urine output, and consciousness. Keep calcium gluconate available.\n\n"
     "[color=#1E3A8A]Acute severe hypertension[/color]\n"
     "• Treat persistent BP ≥160 systolic or ≥110 diastolic urgently.\n"
     "• Options: IV labetalol, IV hydralazine, or immediate-release oral nifedipine.\n"
     "• Recheck BP frequently and avoid uncontrolled, excessive reduction.\n"
     "• Do not administer nifedipine sublingually.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Stabilize the mother first.\n"
     "• Delivery is the definitive treatment. Timing and mode depend on gestational age, maternal/fetal condition."),
    ("04 — WARNINGS", "danger", 
     "• Magnesium toxicity can cause loss of reflexes, respiratory depression, and cardiac arrest. Use particular caution in renal impairment.\n"
     "• Persistent severe hypertension, recurrent seizures, pulmonary edema, altered consciousness, or suspected stroke requires immediate senior and critical-care involvement.\n"
     "• Do not delay treatment of severe hypertension while waiting for laboratory results."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to an obstetric unit with appropriate monitoring; ICU/high-dependency care may be required.\n"
     "• Arrange maternal and fetal surveillance and delivery planning."),
    ("REFERENCES", "info", "ACOG guidance; NICE guideline NG133.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Ruptured Ectopic Pregnancy")] = [
    ("01 — RECOGNITION", "info", 
     "• Pregnancy with abdominal or pelvic pain, vaginal bleeding, syncope, shoulder-tip pain, or hemodynamic instability.\n"
     "• Risk of rupture exists even when the pregnancy test or initial ultrasound findings are inconclusive.\n"
     "• Consider ectopic pregnancy in any reproductive-age patient with possible pregnancy and abdominal pain or bleeding."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and hemodynamic status; call gynecology and anesthesia urgently if rupture is suspected.\n"
     "• Establish two large-bore IV lines in an unstable patient.\n"
     "• Send CBC, blood group/crossmatch, quantitative beta-hCG.\n"
     "• Perform urgent pelvic ultrasound when available, but do not delay resuscitation or surgery in an unstable patient.\n"
     "• Arrange blood products and urgent operative assessment when internal bleeding is suspected."),
    ("03 — TREATMENT", "info", 
     "• Hemodynamic instability or suspected rupture: urgent surgical management is generally required.\n"
     "• Provide blood products and resuscitation according to the hemorrhage protocol.\n"
     "• Provide appropriate analgesia and antiemetics while avoiding delays to definitive care.\n\n"
     "[color=#1E3A8A]Methotrexate[/color]\n"
     "• Reserved for carefully selected, stable, unruptured ectopic pregnancies with appropriate follow-up and no contraindications.\n"
     "• NOT appropriate for suspected rupture or hemodynamic instability.\n"
     "• Selection, dose, beta-hCG monitoring, and follow-up must follow a gynecology protocol."),
    ("04 — WARNINGS", "danger", 
     "• A normal or nondiagnostic early ultrasound does not exclude ectopic pregnancy.\n"
     "• Do not discharge a patient with concerning symptoms without a safe, documented follow-up plan.\n"
     "• Syncope, shock, peritoneal signs, or significant free fluid require emergency escalation."),
    ("05 — DISPOSITION", "warning", 
     "• Suspected rupture: emergency gynecological surgical management.\n"
     "• Stable confirmed ectopic pregnancy: specialist-led decision between expectant, medical, and surgical management."),
    ("REFERENCES", "info", "RCOG; NICE guidance on ectopic pregnancy and miscarriage.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Placental Abruption")] = [
    ("01 — RECOGNITION", "info", 
     "• Premature separation of the placenta from the uterine wall.\n"
     "• May present with painful vaginal bleeding, abdominal or back pain, uterine tenderness, frequent contractions, or fetal compromise.\n"
     "• Bleeding may be concealed; visible blood loss may underestimate severity.\n"
     "• Consider coagulopathy in severe cases."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call obstetrics, anesthesia, and neonatal teams.\n"
     "• Assess maternal ABCs and hemodynamic status.\n"
     "• Establish IV access; send CBC, blood group/crossmatch, coagulation profile, and fibrinogen.\n"
     "• Monitor maternal vital signs and fetal heart rate when permitted.\n"
     "• Arrange ultrasound, but remember that a normal scan does not exclude abruption.\n"
     "• Avoid digital vaginal examination until placenta previa has been excluded."),
    ("03 — TREATMENT", "info", 
     "• Stabilize the mother and treat hemorrhagic shock promptly.\n"
     "• Use blood products and activate the major hemorrhage protocol when indicated.\n"
     "• Delivery urgency and mode depend on maternal stability, fetal status, gestational age, and obstetric findings.\n"
     "• Continuous fetal monitoring is indicated when appropriate.\n"
     "• If disseminated intravascular coagulation is suspected, involve senior obstetrics, anesthesia, hematology, and critical care."),
    ("04 — WARNINGS", "danger", 
     "• Do not estimate severity solely from visible vaginal bleeding.\n"
     "• Maternal shock, persistent abdominal pain, uterine rigidity, fetal bradycardia, or coagulopathy requires urgent escalation.\n"
     "• Do not delay necessary delivery in a deteriorating mother or fetus."),
    ("05 — DISPOSITION", "warning", 
     "• Hospital admission and obstetric-led monitoring are required for suspected significant abruption.\n"
     "• Severe hemorrhage or instability requires emergency delivery planning and possible ICU care."),
    ("REFERENCES", "info", "RCOG; NICE guidance on intrapartum care.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Placenta Previa with Major Bleeding")] = [
    ("01 — RECOGNITION", "info", 
     "• Painless, bright-red vaginal bleeding in the second half of pregnancy.\n"
     "• May cause maternal shock or fetal compromise.\n"
     "• Placenta previa is diagnosed by ultrasound."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call obstetrics, anesthesia, and neonatal teams.\n"
     "• Assess maternal circulation and quantify bleeding.\n"
     "• Establish IV access; obtain CBC, blood group/crossmatch, and coagulation studies.\n"
     "• Monitor maternal vital signs and fetal status.\n"
     "• Arrange ultrasound to determine placental location."),
    ("03 — TREATMENT", "info", 
     "• Stabilize maternal circulation and prepare blood products for major bleeding.\n"
     "• Delivery is required when bleeding is severe, maternal/fetal status is compromised, or obstetric assessment indicates it.\n"
     "• Cesarean delivery is usually required when the placenta covers the cervical os.\n"
     "• Give antenatal corticosteroids when indicated by gestational age, without delaying emergency delivery."),
    ("04 — WARNINGS", "danger", 
     "• Do NOT perform a digital vaginal examination until placenta previa has been excluded.\n"
     "• Do not delay resuscitation or delivery in an unstable patient.\n"
     "• Consider placenta accreta spectrum in patients with relevant risk factors."),
    ("05 — DISPOSITION", "warning", 
     "• Significant bleeding requires hospital admission and obstetric management.\n"
     "• Arrange delivery in a facility with blood products, anesthesia, and neonatal support."),
    ("REFERENCES", "info", "RCOG; NICE guidance on intrapartum care.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Umbilical Cord Prolapse")] = [
    ("01 — RECOGNITION", "info", 
     "• The umbilical cord descends through the cervix alongside or ahead of the presenting fetal part after membrane rupture.\n"
     "• Suspect when sudden fetal bradycardia or severe variable decelerations occur after rupture of membranes.\n"
     "• The cord may be visible or palpable on vaginal examination."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for an immediate obstetric emergency response and prepare for urgent birth.\n"
     "• Confirm fetal heart rate.\n"
     "• If the cord is felt or seen, elevate the presenting fetal part manually to relieve cord compression.\n"
     "• Position the mother knee-chest or in a head-down lateral position.\n"
     "• Minimize handling of the exposed cord; do not attempt to push it back into the uterus.\n"
     "• Maintain elevation of the presenting part during transfer to theatre."),
    ("03 — TREATMENT", "info", 
     "• Expedite delivery, usually by emergency cesarean section unless vaginal birth is immediately achievable and safer.\n"
     "• Consider bladder filling or other decompression maneuvers under trained obstetric direction.\n"
     "• Tocolysis may be considered by the obstetric team in selected cases if delay is unavoidable."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay delivery for nonessential investigations.\n"
     "• Avoid excessive manipulation of the cord because vasospasm may worsen fetal compromise.\n"
     "• If fetal death has been confirmed, the senior obstetric team should guide management."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate obstetric-led emergency delivery and neonatal resuscitation readiness."),
    ("REFERENCES", "info", "RCOG; NICE guidance on intrapartum care.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Shoulder Dystocia")] = [
    ("01 — RECOGNITION", "info", 
     "• The fetal head delivers but the shoulders do not deliver with routine gentle traction.\n"
     "• May be indicated by the 'turtle sign' (head retracts against the perineum).\n"
     "• This is an obstetric emergency requiring coordinated action."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Declare shoulder dystocia clearly and call for help.\n"
     "• Note the time of head delivery.\n"
     "• Ask the mother to stop pushing briefly while the team prepares maneuvers.\n"
     "• Do not apply fundal pressure.\n"
     "• Avoid excessive traction on the fetal head or neck."),
    ("03 — TREATMENT", "info", 
     "• First-line maneuver: McRoberts position (maternal hips flexed toward the abdomen).\n"
     "• Apply suprapubic pressure as directed by a trained clinician.\n"
     "• If unresolved, proceed through the institutional algorithm (internal rotational maneuvers or delivery of the posterior arm).\n"
     "• Consider all-fours positioning when clinically feasible.\n"
     "• Prepare neonatal resuscitation and assess the mother for PPH and genital tract injury."),
    ("04 — WARNINGS", "danger", 
     "• Fundal pressure is contraindicated because it may worsen impaction and cause injury.\n"
     "• Do not use excessive traction.\n"
     "• Record the sequence and timing of maneuvers and the personnel involved."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate neonatal assessment for brachial plexus injury, fracture, or hypoxia.\n"
     "• Maternal assessment for postpartum hemorrhage and perineal trauma."),
    ("REFERENCES", "info", "ACOG Practice Bulletin; RCOG guidance.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Uterine Rupture")] = [
    ("01 — RECOGNITION", "info", 
     "• Sudden severe abdominal pain, abnormal fetal heart rate, vaginal bleeding, maternal shock, loss of fetal station, or cessation of contractions.\n"
     "• Risk is increased with a uterine scar, but rupture can occur without a known scar.\n"
     "• Fetal heart rate abnormality may be the earliest sign."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call obstetrics, anesthesia, operating theatre, blood bank, and neonatal teams immediately.\n"
     "• Begin ABC resuscitation and establish large-bore IV access.\n"
     "• Send CBC, coagulation profile, and blood group/crossmatch.\n"
     "• Prepare for emergency laparotomy and delivery.\n"
     "• Monitor fetal heart rate if feasible without delaying surgery."),
    ("03 — TREATMENT", "info", 
     "• Definitive treatment is urgent surgical exploration and delivery.\n"
     "• Resuscitate with blood products and other fluids according to the degree of hemorrhage.\n"
     "• Surgical repair versus hysterectomy depends on the extent of rupture, bleeding, maternal condition, and fertility considerations.\n"
     "• Administer antibiotics according to surgical and obstetric protocol."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay surgery for imaging when clinical suspicion is high and the patient is unstable.\n"
     "• Maternal shock can progress rapidly; concealed intra-abdominal bleeding may be substantial.\n"
     "• Ensure neonatal resuscitation support is available."),
    ("05 — DISPOSITION", "warning", 
     "• Emergency operative management followed by close postoperative monitoring; ICU care may be required."),
    ("REFERENCES", "info", "ACOG; RCOG guidance on birth after previous cesarean.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Maternal Sepsis and Septic Shock")] = [
    ("01 — RECOGNITION", "info", 
     "• Suspect infection in a pregnant or recently postpartum patient with deterioration, fever or hypothermia, tachycardia, tachypnea, hypotension, altered mental status, oliguria, or elevated lactate.\n"
     "• Sources: endometritis, retained products, urinary infection, pyelonephritis, wound infection, pneumonia, septic abortion.\n"
     "• Sepsis may occur without fever."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Recognize and treat suspected maternal sepsis as an emergency.\n"
     "• Call obstetrics, anesthesia/critical care, and microbiology support.\n"
     "• Obtain cultures before antibiotics if this causes no meaningful delay.\n"
     "• Measure lactate and assess renal function, CBC, coagulation.\n"
     "• Give IV broad-spectrum antibiotics promptly, ideally within 1 hour.\n"
     "• Give IV crystalloid for hypoperfusion, reassessing frequently.\n"
     "• Identify and control the source urgently."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• Select broad-spectrum IV therapy according to the suspected source, severity, allergies, and local resistance.\n"
     "• Do not delay antibiotics in a critically ill patient while waiting for cultures.\n\n"
     "[color=#1E3A8A]Fluids and vasopressors[/color]\n"
     "• Use isotonic crystalloid with repeated reassessment of perfusion.\n"
     "• If hypotension persists despite fluids, initiate vasopressor therapy (norepinephrine is commonly first-line).\n"
     "• Monitor for pulmonary edema, particularly in patients with preeclampsia or cardiac disease."),
    ("04 — WARNINGS", "danger", 
     "• Do not rely on fever or a single screening score to exclude sepsis.\n"
     "• Persistent hypotension, rising lactate, oliguria, altered consciousness, or respiratory failure requires urgent critical-care escalation.\n"
     "• Source control is essential; antibiotics alone may not be sufficient."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to hospital; shock or organ dysfunction requires high-dependency or ICU care.\n"
     "• Continue reassessment and narrow antibiotics when clinically appropriate."),
    ("REFERENCES", "info", "Society for Maternal-Fetal Medicine; Surviving Sepsis Campaign.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Ovarian Torsion")] = [
    ("01 — RECOGNITION", "info", 
     "• Sudden unilateral lower abdominal or pelvic pain, often with nausea and vomiting.\n"
     "• Pain may be intermittent if torsion twists and untwists.\n"
     "• Risk factors include an ovarian mass or enlarged ovary, but torsion can occur without a known mass.\n"
     "• Normal Doppler flow does not reliably exclude torsion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs, abdominal findings, and severity of pain.\n"
     "• Consider pregnancy testing in reproductive-age patients.\n"
     "• Obtain CBC, urinalysis, and other investigations guided by the differential.\n"
     "• Arrange urgent gynecological review and pelvic ultrasound.\n"
     "• Provide appropriate analgesia and antiemetics."),
    ("03 — TREATMENT", "info", 
     "• Suspected ovarian torsion requires urgent gynecological assessment.\n"
     "• Definitive treatment is usually urgent laparoscopy with detorsion and ovarian preservation when feasible.\n"
     "• The decision to remove an ovary depends on specialist intraoperative assessment.\n"
     "• Do not delay specialist assessment solely to obtain additional imaging when clinical suspicion is high."),
    ("04 — WARNINGS", "danger", 
     "• Normal Doppler flow does not rule out torsion.\n"
     "• Delay may result in ovarian ischemia and loss of ovarian function.\n"
     "• Consider other emergencies, including ectopic pregnancy, appendicitis, and ruptured ovarian cyst."),
    ("05 — DISPOSITION", "warning", 
     "• Urgent gynecological evaluation; suspected torsion generally requires hospital-based surgical assessment."),
    ("REFERENCES", "info", "ACOG guidance on adnexal torsion in adolescents.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Retained Placenta")] = [
    ("01 — RECOGNITION", "info", 
     "• Placenta has not been delivered within the expected third-stage timeframe.\n"
     "• Prolonged third stage is commonly >30 minutes with active management or >60 minutes with physiological management.\n"
     "• Earlier intervention is required if significant bleeding or maternal instability occurs.\n"
     "• Consider placenta accreta spectrum when the placenta does not separate."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call the obstetric team and assess maternal vital signs and blood loss.\n"
     "• Establish IV access and obtain CBC and blood group/crossmatch if bleeding is significant.\n"
     "• Empty the bladder if appropriate.\n"
     "• Assess for postpartum hemorrhage and initiate the PPH protocol if indicated.\n"
     "• Prepare analgesia/anesthesia and an appropriate setting for manual removal."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Controlled cord traction[/color]\n"
     "• Perform only by a trained clinician, with appropriate uterine countertraction.\n"
     "• Do not pull forcefully on the cord.\n\n"
     "[color=#1E3A8A]Manual removal[/color]\n"
     "• Indication: retained placenta requiring removal, particularly with bleeding.\n"
     "• Must be performed by a trained obstetric clinician with adequate anesthesia/analgesia.\n"
     "• Provide prophylactic antibiotics according to local protocol."),
    ("04 — WARNINGS", "danger", 
     "• Do not perform uterine exploration or manual removal without appropriate anesthesia and trained personnel.\n"
     "• Avoid forceful traction because it can cause uterine inversion or cord rupture.\n"
     "• Suspected placenta accreta requires senior obstetric involvement; forcible separation can cause catastrophic hemorrhage."),
    ("05 — DISPOSITION", "warning", 
     "• Continue postpartum monitoring for bleeding, uterine tone, and infection.\n"
     "• Escalate to theatre and blood product support when necessary."),
    ("REFERENCES", "info", "WHO PPH Guidelines 2025; NICE NG235.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Postpartum Endometritis")] = [
    ("01 — RECOGNITION", "info", 
     "• Postpartum fever, uterine tenderness, lower abdominal pain, and foul-smelling lochia.\n"
     "• May occur after vaginal birth or cesarean delivery.\n"
     "• Severe disease may progress to sepsis and septic shock.\n"
     "• Consider retained products, wound infection, urinary infection, and other causes."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, temperature, blood pressure, pulse, respiratory rate, mental status, and urine output.\n"
     "• Obtain CBC, renal function, and lactate if systemic illness is suspected.\n"
     "• Obtain blood cultures in severe illness before antibiotics if this does not delay treatment.\n"
     "• Perform abdominal and pelvic examination; assess the cesarean wound.\n"
     "• Consider pelvic ultrasound if retained products or an abscess is suspected."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric IV antibiotics[/color]\n"
     "• Commonly used regimen: clindamycin 900 mg IV every 8 hours plus gentamicin (weight-based).\n"
     "• Alternative regimens may be appropriate depending on local resistance patterns.\n\n"
     "[color=#1E3A8A]Supportive care[/color]\n"
     "• Give IV fluids if hypovolemic, with repeated reassessment.\n"
     "• Provide analgesia and antipyretics.\n"
     "• Investigate and manage retained products, abscess, or another source requiring source control."),
    ("04 — WARNINGS", "danger", 
     "• Suspected sepsis or shock requires immediate broad-spectrum IV antibiotics and escalation.\n"
     "• Failure to improve should prompt reassessment for retained products, pelvic abscess, or resistant organisms.\n"
     "• Antibiotic selection must account for renal function and local resistance patterns."),
    ("05 — DISPOSITION", "warning", 
     "• Admit for IV treatment and reassessment.\n"
     "• Consider higher-level care for organ dysfunction, shock, or failure to improve."),
    ("REFERENCES", "info", "WHO; NICE guidance on sepsis and postpartum care.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "HELLP Syndrome")] = [
    ("01 — RECOGNITION", "info", 
     "• HELLP refers to: Hemolysis, Elevated Liver enzymes, Low Platelet count.\n"
     "• Clinical features: epigastric or RUQ pain, nausea, vomiting, malaise, headache, hypertension, and proteinuria. Hypertension or proteinuria may occasionally be absent."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Urgent obstetric, anesthesia, and senior medical review.\n"
     "• Assess ABCs, blood pressure, neurological status, bleeding, and fetal condition.\n"
     "• Obtain CBC with platelets, blood film, LDH, bilirubin, AST/ALT, creatinine, coagulation profile, and blood group/crossmatch.\n"
     "• Assess for DIC, liver hematoma, renal injury, and pulmonary edema.\n"
     "• Monitor fetal status according to gestational age."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Maternal stabilization[/color]\n"
     "• Treat severe hypertension urgently using a pregnancy-appropriate protocol.\n"
     "• Give magnesium sulfate for seizure prophylaxis when indicated.\n"
     "• Monitor fluid balance carefully and avoid unnecessary fluid loading.\n"
     "• Correct significant blood loss or coagulopathy with appropriate blood components.\n\n"
     "[color=#1E3A8A]Definitive management[/color]\n"
     "• Delivery is the definitive treatment.\n"
     "• Do not delay necessary delivery solely to complete corticosteroids when maternal/fetal condition requires urgent intervention."),
    ("04 — WARNINGS", "danger", 
     "• HELLP can progress rapidly to DIC, hepatic hematoma or rupture, renal failure, placental abruption, and maternal death.\n"
     "• Persistent right upper quadrant pain, hypotension, falling hemoglobin, or worsening coagulopathy requires immediate escalation.\n"
     "• Continue monitoring after delivery because complications may persist or worsen."),
    ("05 — DISPOSITION", "warning", 
     "• Manage in a hospital with obstetric, anesthesia, blood bank, and neonatal support.\n"
     "• ICU or high-dependency care may be required."),
    ("REFERENCES", "info", "ACOG; NICE NG133.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Preterm Prelabor Rupture of Membranes (PPROM)")] = [
    ("01 — RECOGNITION", "info", 
     "• Rupture of membranes before labor and before 37 weeks of gestation.\n"
     "• Presentation: gush or persistent leakage of fluid.\n"
     "• Major complications include ascending infection, cord prolapse, placental abruption, and preterm birth."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Establish gestational age and assess maternal and fetal condition.\n"
     "• Check maternal temperature, pulse, blood pressure, uterine tenderness, and fetal heart rate.\n"
     "• Perform a sterile speculum examination to look for pooling of amniotic fluid.\n"
     "• Avoid routine digital vaginal examinations.\n"
     "• Assess for labor, bleeding, cord prolapse, and signs of intra-amniotic infection."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Expectant management[/color]\n"
     "• If mother and fetus are stable and there is no infection, expectant management may be appropriate.\n\n"
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• RCOG recommends erythromycin for up to 10 days or until established labor.\n"
     "• Avoid amoxicillin-clavulanate for latency prophylaxis.\n\n"
     "[color=#1E3A8A]Antenatal corticosteroids[/color]\n"
     "• Betamethasone 12 mg IM every 24 hours for 2 doses, or dexamethasone 6 mg IM every 12 hours for 4 doses.\n\n"
     "[color=#1E3A8A]Magnesium sulfate[/color]\n"
     "• Consider fetal neuroprotection when early preterm birth is imminent."),
    ("04 — WARNINGS", "danger", 
     "• Suspected intra-amniotic infection, maternal sepsis, significant abruption, cord prolapse, or fetal compromise may require prompt delivery.\n"
     "• Tocolysis is not routinely recommended in PPROM."),
    ("05 — DISPOSITION", "warning", 
     "• Obstetric assessment and a documented plan for inpatient or selected outpatient care are required.\n"
     "• Arrange neonatal consultation when preterm delivery is possible."),
    ("REFERENCES", "info", "RCOG Green-top Guideline No. 73; NICE NG25.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Preterm Labor")] = [
    ("01 — RECOGNITION", "info", 
     "• Regular uterine contractions with cervical change before 37 completed weeks.\n"
     "• Symptoms: pelvic pressure, backache, menstrual-like cramps, or increased vaginal discharge.\n"
     "• Exclude PPROM, infection, placental abruption, and other causes."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Establish gestational age and assess maternal vital signs.\n"
     "• Assess fetal heart rate and uterine contractions.\n"
     "• Evaluate membrane status and signs of infection or bleeding.\n"
     "• Use sterile speculum examination and appropriate cervical assessment.\n"
     "• Avoid digital examination when PPROM or placenta previa is suspected.\n"
     "• Consult obstetrics and neonatal services if early delivery is possible."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Antenatal corticosteroids[/color]\n"
     "• Betamethasone 12 mg IM, repeated after 24 hours (2 doses); or dexamethasone 6 mg IM every 12 hours for 4 doses.\n\n"
     "[color=#1E3A8A]Tocolysis[/color]\n"
     "• Nifedipine may be used in selected patients to delay birth briefly.\n"
     "• Avoid tocolysis when delivery is required for maternal/fetal indications.\n\n"
     "[color=#1E3A8A]Magnesium sulfate[/color]\n"
     "• Consider for fetal neuroprotection when preterm birth is imminent.\n\n"
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• Do not give antibiotics routinely unless there is a specific indication."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay necessary delivery for corticosteroids or transfer when the mother or fetus is deteriorating.\n"
     "• Assess for infection, abruption, and fetal compromise before attempting to delay labor.\n"
     "• Nifedipine may cause hypotension; monitor blood pressure."),
    ("05 — DISPOSITION", "warning", 
     "• Admit or transfer according to gestational age, cervical findings, and neonatal capability."),
    ("REFERENCES", "info", "NICE NG25; WHO recommendations.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Maternal Cardiac Arrest")] = [
    ("01 — RECOGNITION", "info", 
     "• Unresponsive patient with absent normal breathing and no signs of circulation.\n"
     "• In pregnancy, aortocaval compression may reduce venous return and resuscitation effectiveness.\n"
     "• Consider reversible causes: hemorrhage, thromboembolism, eclampsia, sepsis, amniotic fluid embolism, cardiac disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate the maternal cardiac arrest response and call resuscitation, obstetric, anesthesia, and neonatal teams.\n"
     "• Start high-quality CPR immediately.\n"
     "• Use standard adult cardiac arrest algorithms, including prompt defibrillation.\n"
     "• Manually displace the uterus to the patient's left.\n"
     "• Ensure IV/IO access and standard resuscitation medications.\n"
     "• Identify and treat reversible causes."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]CPR and defibrillation[/color]\n"
     "• Perform chest compressions at standard adult depth and rate.\n"
     "• Pregnancy is not a reason to delay defibrillation.\n"
     "• Do not withhold indicated resuscitation medications solely because the patient is pregnant.\n\n"
     "[color=#1E3A8A]Resuscitative delivery[/color]\n"
     "• If the uterus is large enough to cause aortocaval compression and ROSC is not achieved promptly, prepare for resuscitative delivery.\n"
     "• Preparation should begin immediately; do not wait for prolonged unsuccessful CPR.\n"
     "• Follow the current institutional maternal cardiac arrest algorithm."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay CPR, defibrillation, or resuscitative delivery while waiting for ultrasound.\n"
     "• Standard adult resuscitation medications and defibrillation protocols remain applicable.\n"
     "• Consider hemorrhage and pulmonary embolism as important reversible causes."),
    ("05 — DISPOSITION", "warning", 
     "• After ROSC, transfer to an appropriate critical-care setting.\n"
     "• Continue evaluation and treatment of the cause of arrest."),
    ("REFERENCES", "info", "American Heart Association (AHA) guidance.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Miscarriage with Hemorrhage")] = [
    ("01 — RECOGNITION", "info", 
     "• Early pregnancy bleeding with abdominal cramps and passage of tissue.\n"
     "• Severe bleeding may cause tachycardia, hypotension, syncope, or shock.\n"
     "• Confirm pregnancy location when possible; ectopic pregnancy must be considered.\n"
     "• Assess for incomplete miscarriage and retained products."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, bleeding severity, and mental status.\n"
     "• Establish IV access and obtain CBC, blood group/Rh status, and crossmatch if bleeding is significant.\n"
     "• Perform pregnancy testing and ultrasound when appropriate.\n"
     "• Provide analgesia and resuscitation as indicated.\n"
     "• Seek urgent gynecological review for hemodynamic instability or heavy bleeding."),
    ("03 — TREATMENT", "info", 
     "• Hemodynamic instability or uncontrolled bleeding requires emergency resuscitation and urgent gynecological intervention.\n"
     "• Options for stable patients may include expectant, medical, or surgical management.\n"
     "• Surgical evacuation may be necessary for persistent heavy bleeding, infection, or retained tissue.\n"
     "• Provide anti-D prophylaxis when indicated by local Rh-negative guidance."),
    ("04 — WARNINGS", "danger", 
     "• Do not assume all early pregnancy bleeding represents miscarriage; exclude ectopic pregnancy.\n"
     "• Fever, foul discharge, severe pain, syncope, or persistent heavy bleeding requires urgent reassessment.\n"
     "• Ensure follow-up confirms resolution."),
    ("05 — DISPOSITION", "warning", 
     "• Unstable patients require emergency hospital management.\n"
     "• Stable patients may be managed according to a documented gynecology plan."),
    ("REFERENCES", "info", "NICE; RCOG guidance on early pregnancy loss.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Septic Miscarriage")] = [
    ("01 — RECOGNITION", "info", 
     "• Pregnancy loss or attempted termination accompanied by fever, pelvic pain, uterine tenderness, foul discharge, or systemic illness.\n"
     "• May progress rapidly to septic shock, DIC, renal failure, and multiorgan dysfunction.\n"
     "• Consider retained infected products of conception."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as a time-critical emergency.\n"
     "• Call gynecology, anesthesia/critical care, and the operating theatre team.\n"
     "• Assess ABCs, mental status, vital signs, urine output, and perfusion.\n"
     "• Obtain CBC, renal/liver function, coagulation profile, lactate, blood cultures, and crossmatch.\n"
     "• Start broad-spectrum IV antibiotics promptly.\n"
     "• Arrange urgent assessment for uterine evacuation."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• Start broad-spectrum IV coverage against gram-positive, gram-negative, and anaerobic organisms (e.g., clindamycin + gentamicin).\n"
     "• Adjust antibiotic selection for allergy history, renal function, and microbiology.\n\n"
     "[color=#1E3A8A]Source control[/color]\n"
     "• Urgent uterine evacuation is generally required for infected retained products.\n"
     "• Perform under appropriate specialist supervision with resuscitation support.\n\n"
     "[color=#1E3A8A]Septic shock[/color]\n"
     "• Give IV fluids with frequent reassessment.\n"
     "• If hypotension persists, use vasopressors in a monitored setting.\n"
     "• Treat DIC and organ dysfunction with specialist support."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay antibiotics or source control in a critically ill patient.\n"
     "• Consider uterine perforation, hemorrhage, and toxic shock in severe cases.\n"
     "• Avoid managing septic miscarriage as uncomplicated miscarriage."),
    ("05 — DISPOSITION", "warning", 
     "• Hospital admission is required.\n"
     "• Shock, DIC, organ dysfunction, or severe infection requires critical-care management."),
    ("REFERENCES", "info", "WHO; Surviving Sepsis Campaign.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Acute Heavy Uterine Bleeding")] = [
    ("01 — RECOGNITION", "info", 
     "• Excessive uterine bleeding requiring immediate intervention to prevent hemodynamic compromise.\n"
     "• Consider pregnancy-related bleeding first in anyone who could be pregnant.\n"
     "• Causes in nonpregnant patients: anovulation, fibroids, adenomyosis, coagulopathy, medication effects, endometrial pathology."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, bleeding rate, and symptoms of anemia or shock.\n"
     "• Establish IV access and obtain CBC, pregnancy test, blood group/crossmatch if severe, and coagulation tests.\n"
     "• Assess medication history, including anticoagulants.\n"
     "• Arrange pelvic examination and ultrasound according to clinical stability."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemodynamic instability[/color]\n"
     "• Begin resuscitation and arrange urgent gynecological assessment.\n"
     "• Use blood products when clinically indicated.\n\n"
     "[color=#1E3A8A]Medical treatment (Stable patients)[/color]\n"
     "• Tranexamic acid may be considered when not contraindicated.\n"
     "• Hormonal treatment (combined oral contraceptives or progestin therapy) may be appropriate.\n"
     "• IV estrogen is reserved for selected patients under specialist protocol.\n\n"
     "[color=#1E3A8A]Procedural treatment[/color]\n"
     "• If bleeding remains uncontrolled, consider uterine tamponade or surgical management."),
    ("04 — WARNINGS", "danger", 
     "• Exclude pregnancy and pregnancy-related complications before treating as nonpregnant abnormal uterine bleeding.\n"
     "• Estrogen-containing treatment may be contraindicated in patients with thromboembolic risks.\n"
     "• Persistent bleeding requires investigation for structural disease, coagulopathy, and malignancy."),
    ("05 — DISPOSITION", "warning", 
     "• Admit unstable patients or those with severe ongoing bleeding or significant anemia.\n"
     "• Stable patients require a documented treatment and follow-up plan."),
    ("REFERENCES", "info", "ACOG; NICE guidance on heavy menstrual bleeding.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Pelvic Inflammatory Disease (PID) with Sepsis")] = [
    ("01 — RECOGNITION", "info", 
     "• Lower abdominal or pelvic pain, cervical motion tenderness, uterine/adnexal tenderness, fever, or abnormal vaginal discharge.\n"
     "• Severe disease may be associated with tubo-ovarian abscess, peritonitis, or sepsis.\n"
     "• Consider ectopic pregnancy, appendicitis, ovarian torsion, and other surgical emergencies."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, pain severity, and signs of peritonitis or shock.\n"
     "• Perform pregnancy testing.\n"
     "• Obtain CBC, renal function, inflammatory markers, and cultures.\n"
     "• Collect gonorrhea/chlamydia nucleic acid amplification tests.\n"
     "• Arrange pelvic ultrasound when abscess, ectopic pregnancy, or torsion is suspected.\n"
     "• Initiate sepsis management promptly if systemic illness is present."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics[/color]\n"
     "• Hospitalize patients with severe illness, sepsis, suspected tubo-ovarian abscess, pregnancy, or inability to tolerate oral therapy.\n"
     "• Use broad-spectrum IV antibiotics covering gonorrhea, chlamydia, anaerobes (e.g., ceftriaxone plus doxycycline and metronidazole).\n"
     "• Modify treatment according to cultures and clinical response.\n\n"
     "[color=#1E3A8A]Supportive care and source control[/color]\n"
     "• Give IV fluids if hypoperfusion is present.\n"
     "• Provide analgesia and antiemetics.\n"
     "• A tubo-ovarian abscess may require image-guided drainage or surgery if rupture is suspected."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay surgical assessment when appendicitis, ectopic pregnancy, torsion, or abscess rupture is possible.\n"
     "• Suspected sepsis requires immediate treatment and source assessment.\n"
     "• Arrange partner evaluation and treatment to reduce reinfection."),
    ("05 — DISPOSITION", "warning", 
     "• Admit severe cases and reassess frequently.\n"
     "• Ensure clinical improvement before transition to oral therapy.\n"
     "• Arrange follow-up and completion of the recommended antibiotic course."),
    ("REFERENCES", "info", "CDC STI Treatment Guidelines; Surviving Sepsis Campaign.")
]


# ==================== ADDITIONAL TOPICS (21-30) ====================

OBGYN_TOPICS[("Obstetric & Gynecological", "Hyperemesis Gravidarum")] = [
    ("01 — RECOGNITION", "info", 
     "Severe nausea and vomiting during pregnancy with inability to maintain adequate oral intake.\n"
     "• Dehydration, tachycardia, orthostatic hypotension, oliguria, electrolyte disturbances, weight loss.\n"
     "• Assess for hypokalemia, hyponatremia, metabolic alkalosis or acidosis, and AKI.\n"
     "• Consider alternatives: gastroenteritis, pancreatitis, hepatitis, DKA, UTI, bowel obstruction.\n"
     "• Prolonged vomiting increases the risk of thiamine deficiency and Wernicke encephalopathy."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, mental status, hydration, and urine output.\n"
     "• Record vital signs, weight, and fluid balance.\n"
     "• Obtain CBC, electrolytes, urea, creatinine, glucose, and LFTs.\n"
     "• Check urinalysis/urine culture, blood gas, ketones.\n"
     "• Admit severe dehydration, significant electrolyte abnormalities, inability to tolerate oral fluids, or renal impairment."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]IV fluid replacement[/color]\n"
     "• Isotonic saline (0.9% NaCl) for initial volume replacement.\n"
     "• Replace potassium carefully after checking renal function and urine output. Never give concentrated KCl IV push.\n\n"
     "[color=#1E3A8A]Thiamine[/color]\n"
     "• Give thiamine (e.g., 100 mg IV daily) before dextrose-containing fluids in patients with prolonged vomiting/malnutrition.\n"
     "• Suspected Wernicke encephalopathy requires higher-dose IV treatment.\n\n"
     "[color=#1E3A8A]Antiemetic therapy[/color]\n"
     "• Pregnancy-appropriate antiemetics (doxylamine/pyridoxine, cyclizine, promethazine, metoclopramide, or ondansetron).\n"
     "• Caution: Metoclopramide (extrapyramidal reactions), Ondansetron (QT prolongation)."),
    ("04 — WARNINGS", "danger", 
     "• Dextrose given to a thiamine-deficient patient may precipitate Wernicke encephalopathy.\n"
     "• Confusion, ataxia, abnormal eye movements, or altered consciousness may indicate Wernicke's.\n"
     "• Persistent tachycardia, hypotension, oliguria, or rising creatinine requires urgent escalation."),
    ("05 — DISPOSITION", "warning", 
     "• Discharge only when symptoms are controlled and oral fluids tolerated.\n"
     "• Admit severe or complicated cases."),
    ("REFERENCES", "info", "RCOG Green-top Guideline No. 69; NICE guidance.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Breech Presentation and Complicated Delivery")] = [
    ("01 — RECOGNITION", "info", 
     "The fetal buttocks or feet present first instead of the head.\n"
     "• Complications: cord prolapse, head entrapment, fetal hypoxia, birth trauma.\n"
     "• Assess presentation, gestational age, labor progress, membrane status, and fetal heart rate."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain urgent obstetric review when breech is identified in labor.\n"
     "• Confirm presentation by ultrasound if it does not delay management.\n"
     "• Prepare an experienced obstetric clinician, anesthesia, neonatal resuscitation, and theatre.\n"
     "• Assess for cord prolapse following membrane rupture."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Delivery planning[/color]\n"
     "• Cesarean is often recommended for term breech unless criteria for safe vaginal birth are met.\n"
     "• Planned vaginal breech birth requires an established protocol and expertise.\n\n"
     "[color=#1E3A8A]Complicated vaginal breech delivery[/color]\n"
     "• Call for senior obstetric assistance immediately.\n"
     "• Avoid pulling on the fetus or uncontrolled traction.\n"
     "• If aftercoming head is delayed, use the locally approved maneuver promptly."),
    ("04 — WARNINGS", "danger", 
     "• Footling breech carries an increased risk of cord prolapse.\n"
     "• Do not use routine traction to deliver the fetal trunk or head.\n"
     "• Avoid attempting an unfamiliar breech maneuver without training."),
    ("05 — DISPOSITION", "warning", 
     "• Refer to an obstetric unit with surgical, anesthesia, and neonatal support.\n"
     "• Assess newborn for hypoxia or trauma."),
    ("REFERENCES", "info", "RCOG; NICE guidance on intrapartum care.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Multiple Pregnancy with Complications")] = [
    ("01 — RECOGNITION", "info", 
     "Twins or higher-order multiples complicated by labor, fetal distress, malpresentation, cord prolapse, or delayed delivery of subsequent baby.\n"
     "• The second twin may change presentation after delivery of the first.\n"
     "• Risks: PPH, prematurity, intertwin delivery complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call senior obstetric, anesthesia, and neonatal teams.\n"
     "• Confirm number of fetuses, presentations, and placental configuration.\n"
     "• Establish IV access and assess hemorrhage risk.\n"
     "• Prepare for delivery in a setting with immediate cesarean capability.\n"
     "• Ensure neonatal resuscitation equipment for each newborn."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Delivery of the first twin[/color]\n"
     "• Manage according to presentation and fetal condition.\n"
     "• Reassess the lie, presentation, and heart rate of the remaining fetus.\n\n"
     "[color=#1E3A8A]Complications involving the second twin[/color]\n"
     "• Internal podalic version, breech extraction, or emergency cesarean may be needed by trained clinicians.\n\n"
     "[color=#1E3A8A]PPH prevention[/color]\n"
     "• Assess uterine tone and blood loss after delivery. Use institutional PPH protocol."),
    ("04 — WARNINGS", "danger", 
     "• Do not assume the second twin will remain in the same presentation.\n"
     "• Avoid delays when fetal heart rate abnormalities persist.\n"
     "• Multiple pregnancy increases PPH risk; maintain readiness for active management."),
    ("05 — DISPOSITION", "warning", 
     "• Delivery should occur in a facility with appropriate obstetric, anesthesia, and neonatal support."),
    ("REFERENCES", "info", "NICE guidance on twin and triplet pregnancy.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Amniotic Fluid Embolism (AFE)")] = [
    ("01 — RECOGNITION", "info", 
     "Rare, sudden, life-threatening syndrome during labor, delivery, or shortly after birth.\n"
     "• Abrupt hypoxemia, hypotension, cardiac arrest, altered consciousness, or severe coagulopathy.\n"
     "• DIC and massive hemorrhage may develop rapidly.\n"
     "• AFE is a clinical diagnosis of exclusion; no single definitive diagnostic test."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate maternal cardiac arrest or emergency response.\n"
     "• Call obstetrics, anesthesia, critical care, blood bank, and neonatal teams.\n"
     "• Provide high-quality CPR immediately if cardiac arrest occurs.\n"
     "• Give oxygen, secure airway, establish IV/IO access.\n"
     "• Send CBC, coagulation, fibrinogen, blood gas, crossmatch.\n"
     "• Activate massive transfusion protocol for severe hemorrhage/coagulopathy."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Cardiorespiratory support[/color]\n"
     "• Standard advanced life support algorithms. For arrest in pregnancy, use manual left uterine displacement.\n"
     "• Pregnancy is not a reason to withhold defibrillation.\n\n"
     "[color=#1E3A8A]Hemodynamic support[/color]\n"
     "• IV fluids judiciously. Vasopressors or inotropes per shock phenotype.\n"
     "• Consider echocardiography to assess ventricular function.\n\n"
     "[color=#1E3A8A]Coagulopathy and hemorrhage[/color]\n"
     "• Activate major hemorrhage protocol. Replace blood components based on clinical bleeding and tests."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay resuscitation while attempting to confirm AFE.\n"
     "• AFE may cause both cardiovascular collapse and profound coagulopathy.\n"
     "• Avoid indiscriminate fluid loading when cardiac dysfunction is present."),
    ("05 — DISPOSITION", "warning", 
     "• Immediate critical-care management.\n"
     "• Monitor for recurrent shock, DIC, renal injury, and PPH."),
    ("REFERENCES", "info", "AHA Guidelines; SMFM guidance; Standard major obstetric hemorrhage protocols.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Pulmonary Embolism in Pregnancy and Postpartum")] = [
    ("01 — RECOGNITION", "info", 
     "Suspect PE with sudden dyspnea, pleuritic chest pain, tachycardia, unexplained hypoxemia, syncope, hemoptysis, or hypotension.\n"
     "• Risk is increased during pregnancy and especially postpartum.\n"
     "• Hemodynamic instability may indicate high-risk PE."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, SpO2, BP, HR, and mental status.\n"
     "• Give oxygen and ventilatory support if required.\n"
     "• Obtain ECG and chest radiography.\n"
     "• Use a validated pregnancy-adapted diagnostic pathway.\n"
     "• If unstable, prioritize resuscitation and urgent senior assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Compression ultrasonography for suspected DVT.\n"
     "• CTPA or V/Q imaging for suspected PE.\n"
     "• D-dimer only within a validated pregnancy pathway; not alone to exclude PE.\n"
     "• Echocardiography may help assess right ventricular dysfunction in unstable patients."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Anticoagulation[/color]\n"
     "• LMWH is commonly preferred (e.g., Enoxaparin 1 mg/kg SC every 12 hours).\n"
     "• Coordinate with labor, delivery, and neuraxial anesthesia.\n\n"
     "[color=#1E3A8A]High-risk PE with shock[/color]\n"
     "• Activate multidisciplinary emergency response.\n"
     "• Consider systemic thrombolysis or catheter-based/surgical reperfusion for life-threatening PE.\n"
     "• Use unfractionated heparin when rapid adjustment or reversal is needed."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay life-saving resuscitation in an unstable patient for imaging.\n"
     "• Consider postpartum hemorrhage and recent surgery when selecting anticoagulation/thrombolysis.\n"
     "• Do not exclude PE solely because the patient is young or has no leg symptoms."),
    ("06 — DISPOSITION", "warning", 
     "• Confirmed PE requires hospital management and a pregnancy/postpartum-specific plan.\n"
     "• Hemodynamic instability requires urgent higher-level care."),
    ("REFERENCES", "info", "2025 ESC Guidelines; Local pregnancy-associated VTE protocols.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Trauma in Pregnancy")] = [
    ("01 — RECOGNITION", "info", 
     "Trauma from RTC, falls, assault, or penetrating injuries.\n"
     "• Maternal injuries can cause placental abruption, fetomaternal hemorrhage, uterine rupture, preterm labor.\n"
     "• Maternal shock may be present before obvious hypotension (increased blood volume).\n"
     "• Significant abruption may occur without visible vaginal bleeding."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]Primary survey[/color]\n"
     "• Activate trauma team and involve obstetrics early. Assess ABCDE.\n"
     "• Protect cervical spine. Control external hemorrhage and establish large-bore IV access.\n"
     "• Send CBC, crossmatch, coagulation, fibrinogen, blood gas.\n\n"
     "[color=#1E3A8A]Positioning[/color]\n"
     "• Avoid prolonged supine positioning. Use manual left uterine displacement.\n\n"
     "[color=#1E3A8A]Obstetric assessment[/color]\n"
     "• Establish gestational age, assess fetal heart rate, abdominal pain, contractions, bleeding.\n"
     "• Do not use a normal scan to exclude placental abruption."),
    ("03 — INVESTIGATIONS", "info", 
     "• Perform indicated trauma imaging (X-ray/CT); do not withhold necessary imaging due to pregnancy.\n"
     "• Consider fetomaternal hemorrhage testing (especially in Rh-negative patients)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage and shock[/color]\n"
     "• Control bleeding source and use blood products.\n"
     "• Give isotonic crystalloid judiciously.\n\n"
     "[color=#1E3A8A]Rh-negative patients[/color]\n"
     "• Assess need for anti-D immunoglobulin after abdominal trauma.\n\n"
     "[color=#1E3A8A]Delivery[/color]\n"
     "• Delivery is not automatically indicated solely because trauma occurred.\n"
     "• If maternal cardiac arrest occurs, follow the maternal cardiac arrest algorithm."),
    ("05 — WARNINGS", "danger", 
     "• Maternal resuscitation takes priority over fetal investigations.\n"
     "• Do not delay indicated CT or surgery because of pregnancy.\n"
     "• Absence of vaginal bleeding does not exclude placental abruption."),
    ("06 — DISPOSITION", "warning", 
     "• Admit significant trauma, abnormal maternal observations, or abnormal fetal assessment."),
    ("REFERENCES", "info", "EAST Guidelines; ACOG guidance on diagnostic imaging.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Postpartum Venous Thromboembolism")] = [
    ("01 — RECOGNITION", "info", 
     "Pregnancy and postpartum increase VTE risk.\n"
     "• DVT: unilateral leg swelling, pain, warmth.\n"
     "• PE: sudden dyspnea, chest pain, tachycardia, hypoxemia, syncope, shock.\n"
     "• Risk factors: previous VTE, thrombophilia, cesarean, immobility, obesity, infection, hemorrhage."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, SpO2, and hemodynamic stability.\n"
     "• If PE suspected, assess severity immediately.\n"
     "• If DVT suspected, arrange urgent compression ultrasonography.\n"
     "• Check medication history, recent delivery details, neuraxial anesthesia timing, and bleeding risk."),
    ("03 — INVESTIGATIONS", "info", 
     "• Compression duplex ultrasonography for DVT.\n"
     "• CTPA or V/Q imaging for PE.\n"
     "• D-dimer should not be used in isolation to exclude postpartum VTE.\n"
     "• Consider pelvic venous imaging for suspected iliac/pelvic vein thrombosis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Therapeutic anticoagulation[/color]\n"
     "• Enoxaparin 1 mg/kg SC every 12 hours (adjust for renal function).\n"
     "• Unfractionated heparin preferred in unstable patients or severe renal impairment.\n"
     "• Coordinate with recent neuraxial anesthesia and postpartum hemorrhage risk.\n\n"
     "[color=#1E3A8A]Duration[/color]\n"
     "• Generally at least 3 months total and at least 6 weeks postpartum."),
    ("05 — WARNINGS", "danger", 
     "• Do not start anticoagulation without assessing active bleeding.\n"
     "• Suspected PE with shock requires emergency resuscitation and consideration of reperfusion.\n"
     "• Direct oral anticoagulants are generally not preferred during breastfeeding."),
    ("06 — DISPOSITION", "warning", 
     "• Confirmed VTE requires a documented anticoagulation and follow-up plan.\n"
     "• PE with hemodynamic instability requires urgent higher-level care."),
    ("REFERENCES", "info", "RCOG Green-top Guidelines 37a and 37b; ASH guidelines.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Peripartum Cardiomyopathy")] = [
    ("01 — RECOGNITION", "info", 
     "Heart failure due to LV systolic dysfunction occurring toward the end of pregnancy or in months following delivery.\n"
     "• Symptoms: progressive dyspnea, orthopnea, PND, cough, fatigue, edema.\n"
     "• Severe cases: pulmonary edema, hypotension, arrhythmias, cardiogenic shock.\n"
     "• Distinguish from common pregnancy-related breathlessness and edema."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, SpO2, respiratory effort, BP, perfusion, and mental status.\n"
     "• Sit upright, give oxygen, provide ventilatory support if required.\n"
     "• Obtain ECG, CBC, electrolytes, renal function, troponin, BNP/NT-proBNP.\n"
     "• Arrange urgent echocardiography.\n"
     "• Involve cardiology, obstetrics, and critical care early."),
    ("03 — INVESTIGATIONS", "info", 
     "• ECG and continuous cardiac monitoring.\n"
     "• Echocardiography (LVEF, chamber size, RV function, valvular disease).\n"
     "• Chest radiography when indicated.\n"
     "• Consider PE, ACS, preeclampsia-associated pulmonary edema, myocarditis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Acute pulmonary edema (adequate BP)[/color]\n"
     "• Oxygen, noninvasive ventilation for distress.\n"
     "• IV loop diuretic for congestion (monitor renal function/electrolytes).\n\n"
     "[color=#1E3A8A]Cardiogenic shock[/color]\n"
     "• Activate critical-care and cardiology support.\n"
     "• Use vasopressors or inotropes per shock phenotype.\n\n"
     "[color=#1E3A8A]Long-term treatment[/color]\n"
     "• During pregnancy: avoid ACE inhibitors, ARBs, ARNIs, and MRAs.\n"
     "• After delivery: optimize guideline-directed therapy per hemodynamics and breastfeeding."),
    ("05 — WARNINGS", "danger", 
     "• New orthopnea, hypoxemia, pulmonary crackles, or rapid deterioration requires urgent evaluation.\n"
     "• Do not assume dyspnea or edema is physiological in late pregnancy/postpartum.\n"
     "• Excessive fluid administration may worsen pulmonary edema."),
    ("06 — DISPOSITION", "warning", 
     "• Admit suspected acute heart failure for urgent evaluation.\n"
     "• ICU or coronary care for pulmonary edema, shock, or severe ventricular dysfunction."),
    ("REFERENCES", "info", "ESC Guidelines; AHA scientific guidance.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Postpartum Headache: Stroke, CVST, and Hemorrhage")] = [
    ("01 — RECOGNITION", "info", 
     "Postpartum headache may result from primary headache, post-dural puncture, preeclampsia, CVST, ischemic stroke, ICH, RCVS, or pituitary apoplexy.\n"
     "• [color=#991B1B]Red flags: thunderclap onset, severe/progressive headache, seizure, focal deficit, altered consciousness, fever, visual disturbance, severe hypertension.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, BP, temperature, SpO2, glucose, neurological status.\n"
     "• Perform focused neurological examination.\n"
     "• Activate stroke pathway immediately for focal deficits.\n"
     "• Treat seizures and severe hypertension according to protocols.\n"
     "• Do not attribute severe/atypical headache to epidural/spinal procedure without excluding dangerous causes."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, platelets, electrolytes, renal function, LFTs, urine protein.\n"
     "• Urgent noncontrast CT head for suspected ICH.\n"
     "• MRI brain and MR venography for suspected CVST.\n"
     "• Lumbar puncture only after appropriate assessment and exclusion of contraindications."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Suspected postpartum preeclampsia/eclampsia[/color]\n"
     "• Treat severe BP (≥160/110) urgently.\n"
     "• Magnesium sulfate for eclampsia/seizure prophylaxis (4–6 g load, then 1–2 g/hr).\n\n"
     "[color=#1E3A8A]Suspected stroke or ICH[/color]\n"
     "• Activate stroke/neurosurgical pathway.\n"
     "• Maintain oxygenation, avoid hypotension, control BP per protocol.\n\n"
     "[color=#1E3A8A]Suspected CVST[/color]\n"
     "• Urgent neuroimaging with venous imaging. Therapeutic heparin is generally standard for confirmed CVST."),
    ("05 — WARNINGS", "danger", 
     "• Thunderclap headache, focal deficit, seizure, altered consciousness, or severe hypertension is an emergency.\n"
     "• A normal initial examination does not reliably exclude CVST.\n"
     "• Do not delay emergency neuroimaging in a patient with red flags."),
    ("06 — DISPOSITION", "warning", 
     "• Admit suspected stroke, CVST, ICH, eclampsia, or other serious secondary headache."),
    ("REFERENCES", "info", "AHA/ASA guidance; ACOG guidance on postpartum preeclampsia.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Acute Fatty Liver of Pregnancy (AFLP)")] = [
    ("01 — RECOGNITION", "info", 
     "Rare, potentially life-threatening pregnancy-associated liver disease, usually in the third trimester or early postpartum.\n"
     "• Symptoms: nausea, vomiting, abdominal pain, malaise, jaundice, polydipsia, altered mental status.\n"
     "• Severe: hypoglycemia, coagulopathy, renal impairment, encephalopathy, multiorgan failure.\n"
     "• Differentiate from HELLP, viral hepatitis, drug-induced liver injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Urgent obstetric, hepatology, anesthesia, and critical-care review.\n"
     "• Assess ABCs, consciousness, BP, perfusion, glucose, and bleeding signs.\n"
     "• Check bedside glucose immediately and repeat frequently.\n"
     "• Obtain CBC, LFTs, bilirubin, renal function, coagulation, fibrinogen, blood gas, lactate, crossmatch."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Maternal stabilization[/color]\n"
     "• Correct hypoglycemia promptly using IV glucose.\n"
     "• Correct dehydration and electrolytes cautiously.\n"
     "• Treat coagulopathy with blood components when indicated.\n"
     "• Manage encephalopathy, renal failure, and other organ dysfunction with critical-care support.\n\n"
     "[color=#1E3A8A]Definitive management[/color]\n"
     "• Prompt delivery is the definitive treatment once AFLP is diagnosed/suspected.\n"
     "• Do not delay delivery solely to normalize all lab values if deteriorating."),
    ("04 — WARNINGS", "danger", 
     "• AFLP can progress rapidly to acute liver failure, severe hypoglycemia, DIC, and maternal death.\n"
     "• A single normal glucose or coagulation result does not exclude evolving disease.\n"
     "• Avoid unnecessary invasive procedures when coagulopathy is present."),
    ("05 — DISPOSITION", "warning", 
     "• Manage in a hospital with obstetric, anesthesia, blood bank, and critical-care support.\n"
     "• ICU care often required. Continue close postpartum monitoring."),
    ("REFERENCES", "info", "EASL Guidelines; FIGO guidance on liver disease in pregnancy.")
]


# ==================== ADDITIONAL TOPICS (31-40) ====================

OBGYN_TOPICS[("Obstetric & Gynecological", "Ruptured Hemorrhagic Ovarian Cyst")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden unilateral pelvic or lower abdominal pain.\n"
     "• Pain may occur during exercise or intercourse.\n"
     "• Guarding, rebound tenderness, dizziness, syncope, or shoulder-tip pain if significant intraperitoneal bleeding occurs.\n"
     "• Tachycardia, hypotension, pallor, or falling hemoglobin suggest major hemorrhage.\n"
     "• Always exclude ectopic pregnancy in any reproductive-age patient with pelvic pain or bleeding."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, mental status, and vital signs.\n"
     "• Obtain two large-bore IV lines if significant bleeding or instability is suspected.\n"
     "• Keep the patient nil by mouth and urgently involve gynecology.\n"
     "• Send CBC, blood group and crossmatch, coagulation profile, renal function, and serum or urine β-hCG.\n"
     "• Perform bedside ultrasound if available; do not delay surgery for imaging in a patient with suspected life-threatening intra-abdominal hemorrhage.\n"
     "• Activate the major hemorrhage protocol if indicated."),
    ("03 — INVESTIGATIONS", "info", 
     "• Transvaginal pelvic ultrasound: ovarian cyst, free pelvic fluid, and possible hemoperitoneum.\n"
     "• Serial hemoglobin/hematocrit; an initial normal hemoglobin does not exclude acute blood loss.\n"
     "• Quantitative β-hCG to help exclude ectopic pregnancy.\n"
     "• CT is generally not the first-line investigation when pregnancy is possible."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol 1 g orally or IV every 6–8 hours as needed; maximum 4 g/day in a healthy adult.\n"
     "• If severe pain persists, titrated IV opioid analgesia may be used according to local protocols.\n"
     "• Avoid NSAIDs when significant bleeding, renal impairment, or a bleeding disorder is suspected.\n\n"
     "[color=#1E3A8A]IV fluids and blood products[/color]\n"
     "• If hypotensive, give isotonic crystalloid in reassessed boluses, commonly 250–500 mL in adults.\n"
     "• If major hemorrhage is suspected, use emergency-release blood or crossmatched blood according to the institutional major hemorrhage protocol.\n\n"
     "[color=#1E3A8A]Definitive management[/color]\n"
     "• Stable, improving patient: monitored observation, serial vital signs and hemoglobin.\n"
     "• Hemodynamic instability, ongoing bleeding, worsening hemoperitoneum: urgent laparoscopy or laparotomy.\n"
     "• Aim for ovarian-sparing cyst treatment when feasible and safe."),
    ("05 — WARNINGS", "danger", 
     "• Analgesia must not delay evaluation for ectopic pregnancy, torsion, or hemorrhagic shock.\n"
     "• Persistent instability requires urgent operative hemorrhage control; fluids alone do not treat the bleeding source."),
    ("06 — DISPOSITION", "warning", 
     "• Admit if significant hemoperitoneum, falling hemoglobin, uncontrolled pain, or diagnostic uncertainty is present.\n"
     "• Discharge only after adequate reassessment, stable vital signs, controlled pain, and a safe follow-up plan."),
    ("REFERENCES", "info", "ACOG; NICE. Ectopic pregnancy and miscarriage.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Tubo-Ovarian Abscess (TOA)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Lower abdominal or pelvic pain, fever, and cervical motion or adnexal tenderness.\n"
     "• Vaginal discharge, dyspareunia, nausea, or vomiting may occur.\n"
     "• A pelvic mass or complex adnexal collection on ultrasound supports the diagnosis.\n"
     "• Rupture may cause generalized peritonitis, sepsis, and shock.\n"
     "• Differential diagnoses include ectopic pregnancy, appendicitis, ovarian torsion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for sepsis, shock, peritonitis, and pregnancy.\n"
     "• Obtain IV access; send CBC, renal and liver function, lactate if severely ill, blood cultures if sepsis is suspected, and β-hCG.\n"
     "• Obtain vaginal/cervical testing for gonorrhea and chlamydia when appropriate.\n"
     "• Perform pelvic ultrasound and involve gynecology.\n"
     "• Hospitalize patients with suspected TOA; pregnancy, severe illness, inability to tolerate oral treatment, or inability to exclude a surgical emergency are additional reasons for inpatient care."),
    ("03 — INVESTIGATIONS", "info", 
     "• Transvaginal ultrasound, usually with Doppler when indicated.\n"
     "• CBC, CRP, renal function, pregnancy test, and microbiological testing.\n"
     "• CT or MRI may be considered when the diagnosis remains uncertain."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]First-line inpatient antimicrobial regimen[/color]\n"
     "• Ceftriaxone 1 g IV every 24 hours.\n"
     "• PLUS doxycycline 100 mg orally or IV every 12 hours.\n"
     "• PLUS metronidazole 500 mg orally or IV every 12 hours.\n"
     "• Continue IV therapy until clinical improvement, then transition to oral doxycycline 100 mg twice daily plus metronidazole 500 mg twice daily to complete 14 days.\n\n"
     "[color=#1E3A8A]Alternative inpatient regimens[/color]\n"
     "• Option A: Ampicillin–sulbactam 3 g IV every 6 hours PLUS doxycycline 100 mg.\n"
     "• Option B: Clindamycin 900 mg IV every 8 hours PLUS gentamicin.\n\n"
     "[color=#1E3A8A]Drainage or surgery[/color]\n"
     "• Consider image-guided drainage or operative drainage if the abscess is large, ruptured, associated with sepsis, or not improving with appropriate antibiotics."),
    ("05 — WARNINGS", "danger", 
     "• Doxycycline is generally avoided during pregnancy; if pregnancy is possible or confirmed, obtain urgent specialist advice and select a pregnancy-appropriate regimen.\n"
     "• Suspected rupture, generalized peritonitis, or hemodynamic instability requires urgent surgical assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for inpatient treatment and observation for more than 24 hours.\n"
     "• Lack of clinical improvement within 48–72 hours requires reassessment of the diagnosis and need for drainage."),
    ("REFERENCES", "info", "CDC. Pelvic Inflammatory Disease: STI Treatment Guidelines.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Ovarian Torsion in Pregnancy")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden severe unilateral pelvic or lower abdominal pain, often with nausea and vomiting.\n"
     "• Pain may be intermittent if torsion is partial or intermittent.\n"
     "• Adnexal tenderness or a known ovarian/adnexal mass may be present.\n"
     "• Ovarian torsion is a time-critical surgical emergency because delayed treatment can cause ovarian ischemia and loss."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Urgent OB/GYN consultation.\n"
     "• Assess hemodynamic stability and perform abdominal examination.\n"
     "• Keep nil by mouth; establish IV access and provide pregnancy-appropriate analgesia.\n"
     "• Confirm gestational age and assess fetal status when appropriate.\n"
     "• Arrange urgent pelvic ultrasound; do not delay surgery when clinical suspicion remains high."),
    ("03 — INVESTIGATIONS", "info", 
     "• Transvaginal or transabdominal ultrasound with Doppler.\n"
     "• Preserved Doppler blood flow does not exclude torsion.\n"
     "• Definitive diagnosis may be made at surgery."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia and stabilization[/color]\n"
     "• Paracetamol 1 g orally or IV every 6–8 hours as needed; maximum 4 g/day.\n"
     "• For severe pain, use carefully titrated IV opioid analgesia under monitoring.\n\n"
     "[color=#1E3A8A]Definitive treatment[/color]\n"
     "• Urgent laparoscopy is generally preferred when feasible; laparotomy may be required depending on gestational age, anatomy, or instability.\n"
     "• Detorsion and ovarian preservation are preferred when technically feasible, even when the ovary initially appears dark or congested."),
    ("05 — WARNINGS", "danger", 
     "• Analgesia and imaging must not delay urgent gynecologic intervention when torsion is strongly suspected."),
    ("06 — DISPOSITION", "warning", 
     "• Admit and arrange urgent operative evaluation.\n"
     "• Monitor postoperative pain, bleeding, infection, and pregnancy status."),
    ("REFERENCES", "info", "ACOG. Evaluation and Management of Adnexal Masses.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Uterine AVM with Severe Bleeding")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden, recurrent, or profuse vaginal bleeding.\n"
     "• May occur after pregnancy, miscarriage, uterine instrumentation, or uterine surgery.\n"
     "• Severe cases may cause tachycardia, hypotension, syncope, and hemorrhagic shock.\n"
     "• Doppler ultrasound may show prominent serpiginous vessels with high-velocity, low-resistance flow."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs and activate the major hemorrhage protocol if indicated.\n"
     "• Establish two large-bore IV lines; send CBC, coagulation profile, fibrinogen, blood group and crossmatch, and β-hCG.\n"
     "• Urgent gynecology and interventional radiology consultation.\n"
     "• Avoid blind uterine curettage or instrumentation until a high-flow vascular lesion has been assessed."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, coagulation studies, fibrinogen, renal function, and β-hCG.\n"
     "• Transvaginal ultrasound with color and spectral Doppler.\n"
     "• CT angiography or MRI may be considered in selected stable patients.\n"
     "• Angiography may confirm the lesion and enable treatment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage resuscitation[/color]\n"
     "• Give isotonic crystalloid in reassessed 250–500 mL adult boluses if hypotensive while blood products are arranged.\n"
     "• Use emergency-release or crossmatched blood and component therapy according to the major hemorrhage protocol.\n\n"
     "[color=#1E3A8A]Definitive treatment[/color]\n"
     "• Uterine artery embolization is often the preferred uterus-preserving intervention for significant bleeding.\n"
     "• Surgical management may be required for uncontrolled life-threatening hemorrhage or failed embolization."),
    ("05 — WARNINGS", "danger", 
     "• Avoid blind curettage or uterine instrumentation when AVM is suspected.\n"
     "• Tranexamic acid and uterotonics are not definitive treatment for a uterine AVM."),
    ("06 — DISPOSITION", "warning", 
     "• Admit all patients with significant bleeding or suspected high-flow uterine vascular lesions."),
    ("REFERENCES", "info", "ACOG; NICE.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Severe Vaginal/Cervical Laceration")] = [
    ("01 — RECOGNIZE", "info", 
     "• Persistent vaginal bleeding after vaginal birth, miscarriage, instrumentation, or pelvic trauma.\n"
     "• Bleeding may be brisk despite a firm, well-contracted uterus.\n"
     "• Cervical or upper vaginal lacerations can cause severe concealed or ongoing blood loss.\n"
     "• Assess for perineal injury, expanding vulvovaginal hematoma, urinary tract injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call senior obstetric/gynecologic help and anesthesia if bleeding is significant.\n"
     "• Assess ABCs, vital signs, mental status, and estimated blood loss.\n"
     "• Establish two large-bore IV lines; send CBC, coagulation profile, fibrinogen, and blood group/crossmatch.\n"
     "• Assess uterine tone and placental completeness; do not assume atony is the cause.\n"
     "• If the source cannot be adequately visualized, move promptly to an operating theatre for examination under anesthesia."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage resuscitation[/color]\n"
     "• If hypotensive, give reassessed 250–500 mL adult boluses of isotonic crystalloid while arranging blood products.\n"
     "• For major blood loss, transfuse blood components according to the local obstetric major hemorrhage protocol.\n\n"
     "[color=#1E3A8A]Repair of cervical or vaginal laceration[/color]\n"
     "• Use local anesthetic or regional/general anesthesia according to injury extent.\n"
     "• Repair under direct visualization, securing bleeding vessels and closing the laceration with appropriate absorbable sutures.\n"
     "• Deep cervical or upper vaginal injuries may require an operating theatre and experienced surgeon.\n"
     "• Reassess hemostasis after repair; inspect for expanding hematoma."),
    ("04 — WARNINGS", "danger", 
     "• Do not place blind deep sutures where the bladder, ureters, or rectum may be injured.\n"
     "• Persistent bleeding after repair requires immediate reassessment for an unrecognized higher injury, hematoma, or coagulopathy."),
    ("05 — DISPOSITION", "warning", 
     "• Admit and observe patients with significant lacerations, substantial blood loss, operative repair, or suspected associated injury."),
    ("REFERENCES", "info", "ACOG; WHO; NICE.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Ovarian Hyperstimulation Syndrome (OHSS)")] = [
    ("01 — RECOGNIZE", "info", 
     "• Usually occurs after ovarian stimulation during fertility treatment.\n"
     "• Abdominal distension, pelvic pain, nausea, vomiting, and rapid weight gain.\n"
     "• Severe disease may cause ascites, pleural effusion, oliguria, hemoconcentration, electrolyte abnormalities, AKI, and VTE.\n"
     "• Red flags: dyspnea, chest pain, syncope, severe abdominal pain, reduced urine output, or unilateral leg swelling."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, SpO2, and hemodynamic status.\n"
     "• Determine severity and involve the fertility specialist and gynecology team.\n"
     "• Measure weight, abdominal girth, fluid intake/output, and urine output.\n"
     "• Evaluate for pregnancy, ectopic, ovarian torsion, hemorrhage, and PE when clinically indicated.\n"
     "• Admit patients with severe symptoms, significant ascites, respiratory compromise, oliguria, or suspected thrombosis."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC and hematocrit.\n"
     "• Electrolytes, urea, creatinine, liver function, albumin, and coagulation studies.\n"
     "• Pregnancy test or quantitative β-hCG.\n"
     "• Pelvic ultrasound to assess ovarian enlargement and ascites.\n"
     "• Chest imaging and PE investigations if respiratory symptoms."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid management[/color]\n"
     "• For clinically significant intravascular depletion, give isotonic crystalloid in small, reassessed boluses.\n"
     "• Avoid automatic large-volume fluid administration in patients with substantial ascites or pleural effusion.\n\n"
     "[color=#1E3A8A]Analgesia and antiemetics[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed.\n"
     "• For persistent vomiting, use a pregnancy-appropriate antiemetic.\n"
     "• Avoid NSAIDs when renal impairment, dehydration, or significant intravascular depletion is present.\n\n"
     "[color=#1E3A8A]Thromboprophylaxis[/color]\n"
     "• In hospitalized patients with severe OHSS, consider LMWH prophylaxis according to body weight, renal function, and bleeding risk."),
    ("05 — WARNINGS", "danger", 
     "• OHSS causes fluid shift into third spaces; excessive IV fluid may worsen ascites and respiratory compromise.\n"
     "• Severe or increasing pain requires assessment for ovarian torsion, cyst rupture, or another acute abdomen.\n"
     "• Suspected PE or DVT requires urgent diagnostic evaluation and treatment."),
    ("06 — DISPOSITION", "warning", 
     "• Mild disease: outpatient care only if oral intake, pain control, urine output, and follow-up are adequate.\n"
     "• Moderate or severe disease: specialist review and often admission."),
    ("REFERENCES", "info", "RCOG; ASRM.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Acute Obstetric Hemorrhagic Shock")] = [
    ("01 — RECOGNIZE", "info", 
     "• Significant bleeding during pregnancy, delivery, or the postpartum period.\n"
     "• Tachycardia, pallor, cold extremities, delayed capillary refill, altered mental status, oliguria, or hypotension.\n"
     "• Hypotension can be a late sign; do not wait for it before initiating treatment.\n"
     "• Consider concealed bleeding when visible blood loss appears insufficient to explain the patient's condition."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate the obstetric major hemorrhage protocol and call senior obstetrics, anesthesia, blood bank, and theatre teams.\n"
     "• Perform ABC assessment and provide oxygen for hypoxemia.\n"
     "• Establish two large-bore IV lines; send CBC, blood group/crossmatch, PT/INR, aPTT, fibrinogen, blood gas, lactate, and ionized calcium.\n"
     "• Start rapid hemorrhage resuscitation and identify the bleeding source simultaneously.\n"
     "• Keep the patient warm and prepare for definitive hemorrhage control."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Blood products and resuscitation[/color]\n"
     "• Activate the local massive transfusion protocol.\n"
     "• Give emergency-release blood or crossmatched red cells and balanced blood components.\n"
     "• Use isotonic crystalloid only as a bridge while blood products and hemorrhage control are arranged.\n\n"
     "[color=#1E3A8A]Tranexamic acid for postpartum hemorrhage[/color]\n"
     "• If postpartum hemorrhage is diagnosed, give tranexamic acid 1 g IV over 10 minutes as soon as possible and within 3 hours of birth.\n"
     "• If bleeding continues after 30 minutes, a second 1 g IV dose may be given.\n\n"
     "[color=#1E3A8A]Cause-directed hemorrhage control[/color]\n"
     "• Uterine atony: uterine massage, oxytocin, and additional uterotonics.\n"
     "• Retained placental tissue: urgent obstetric assessment and removal.\n"
     "• Genital tract trauma: prompt inspection and repair.\n"
     "• Uterine rupture or uncontrolled intra-abdominal bleeding: emergency surgery."),
    ("04 — WARNINGS", "danger", 
     "• Do not rely on a single initial hemoglobin to estimate acute blood loss.\n"
     "• Excessive crystalloid can worsen dilutional coagulopathy and tissue edema.\n"
     "• Do not delay standard postpartum hemorrhage measures while giving tranexamic acid."),
    ("05 — DISPOSITION", "warning", 
     "• All patients with hemorrhagic shock require resuscitation in a monitored setting and urgent definitive treatment.\n"
     "• Transfer to ICU or high-dependency care when ongoing organ support is present."),
    ("REFERENCES", "info", "WHO; FIGO; RCOG.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Peripartum Aortic Dissection")] = [
    ("01 — RECOGNIZE", "info", 
     "• Sudden severe chest, back, neck, or abdominal pain, sometimes described as tearing or ripping.\n"
     "• Syncope, collapse, hypotension, pulse deficit, unequal arm blood pressures, new aortic regurgitation murmur, or focal neurological deficit.\n"
     "• May mimic pulmonary embolism, acute coronary syndrome, or musculoskeletal pain.\n"
     "• Pregnancy and the early postpartum period increase risk, especially with hypertension or connective tissue disorders."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate emergency, cardiothoracic/vascular surgery, anesthesia, and obstetric teams immediately.\n"
     "• Assess ABCs, continuous ECG, blood pressure, SpO2, and neurological status.\n"
     "• Measure blood pressure in both arms when feasible without delaying treatment.\n"
     "• Obtain urgent definitive aortic imaging; CT angiography is commonly used when appropriate.\n"
     "• Do not delay specialist management for a normal ECG or troponin."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Anti-impulse therapy[/color]\n"
     "• IV esmolol: 500 microgram/kg loading dose over 1 minute, followed by 50 microgram/kg/min infusion; titrate to response.\n"
     "• If beta-blockers are contraindicated, IV diltiazem may be considered.\n"
     "• A vasodilator such as nicardipine may be added if BP remains elevated after adequate heart-rate control.\n"
     "• Target: HR 60-80/min and systolic BP <120 mmHg (or lowest pressure maintaining organ perfusion).\n\n"
     "[color=#1E3A8A]Definitive management[/color]\n"
     "• Type A dissection generally requires emergency cardiac surgery.\n"
     "• Type B dissection requires urgent specialist management.\n"
     "• Delivery timing and mode must be coordinated with cardiothoracic surgery, obstetrics, and anesthesia."),
    ("04 — WARNINGS", "danger", 
     "• Do not initiate aggressive blood-pressure reduction in profound hypotension or shock without specialist direction.\n"
     "• Avoid vasodilator monotherapy before adequate heart-rate control because reflex tachycardia may increase aortic wall stress."),
    ("05 — DISPOSITION", "warning", 
     "• Admit to ICU or an equivalent high-acuity setting.\n"
     "• Immediate transfer to a center with cardiothoracic/vascular surgery capability when needed."),
    ("REFERENCES", "info", "2022 ACC/AHA Guideline for Aortic Disease; ESC Guidelines.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Pregnancy-Associated AKI")] = [
    ("01 — RECOGNIZE", "info", 
     "• Rising serum creatinine, oliguria, or anuria during pregnancy or postpartum.\n"
     "• Causes include hypovolemia, hemorrhage, sepsis, preeclampsia/HELLP, AFLP, thrombotic microangiopathy, urinary obstruction, and drug toxicity.\n"
     "• Pregnancy normally lowers serum creatinine; a value that appears only mildly elevated by nonpregnant reference ranges may be clinically important.\n"
     "• Evaluate for life-threatening hyperkalemia, pulmonary edema, severe acidosis, and uremic complications."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCs, vital signs, volume status, and urine output.\n"
     "• Review pregnancy/postpartum status, bleeding, sepsis, hypertension, medications, and nephrotoxic exposures.\n"
     "• Establish IV access and obtain CBC, electrolytes, urea, creatinine, bicarbonate, liver function, urinalysis.\n"
     "• Perform ECG urgently if hyperkalemia is suspected or confirmed.\n"
     "• Involve obstetrics and nephrology early for severe, rapidly progressive, or unexplained AKI."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]Volume and perfusion management[/color]\n"
     "• If hypovolemia is likely, give isotonic crystalloid in carefully reassessed 250–500 mL adult boluses.\n"
     "• If the patient is euvolemic or fluid overloaded, do not give repeated fluid boluses without evidence of fluid responsiveness.\n\n"
     "[color=#1E3A8A]Hyperkalemia with ECG changes or severe elevation[/color]\n"
     "• IV calcium gluconate 10% solution, commonly 10 mL IV over 5–10 minutes, for cardiac membrane stabilization.\n"
     "• Insulin with glucose, nebulized salbutamol, and other potassium-lowering measures should follow the emergency hyperkalemia protocol.\n\n"
     "[color=#1E3A8A]Treat the underlying cause[/color]\n"
     "• Hemorrhage: control bleeding and restore perfusion.\n"
     "• Sepsis: early appropriate antibiotics and source control.\n"
     "• Preeclampsia/HELLP: urgent obstetric management and delivery when indicated.\n"
     "• Obstruction: urgent relief of urinary tract obstruction."),
    ("04 — WARNINGS", "danger", 
     "• Oliguria alone does not prove that more fluid is needed.\n"
     "• Pulmonary edema and severe preeclampsia require careful fluid management.\n"
     "• IV calcium stabilizes the myocardium but does not lower serum potassium."),
    ("05 — DISPOSITION", "warning", 
     "• Admit patients with significant, progressive, or unexplained AKI.\n"
     "• ICU care is indicated for severe electrolyte disturbance, pulmonary edema, shock, or severe acidosis."),
    ("REFERENCES", "info", "NICE. Acute kidney injury; KDIGO Guidelines.")
]

OBGYN_TOPICS[("Obstetric & Gynecological", "Severe Hypoglycemia and DKA")] = [
    ("01 — RECOGNIZE", "info", 
     "• [color=#991B1B]Severe hypoglycemia:[/color] Blood glucose below 70 mg/dL (3.9 mmol/L) is low; below 54 mg/dL (3.0 mmol/L) is clinically significant. Severe means cognitive impairment requiring assistance.\n"
     "• Symptoms: sweating, tremor, palpitations, confusion, seizures, or coma.\n"
     "• [color=#991B1B]DKA in pregnancy:[/color] Nausea, vomiting, abdominal pain, dehydration, tachypnea, and altered mental status.\n"
     "• DKA may occur at lower glucose concentrations in pregnancy than outside pregnancy (euglycemic DKA)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Check bedside glucose immediately and assess ABCs.\n"
     "• If unconscious or seizing, protect the airway and obtain IV access.\n"
     "• For suspected DKA, obtain blood gas, electrolytes, bicarbonate, renal function, blood ketones, glucose, CBC.\n"
     "• Start maternal resuscitation and urgent obstetric, medical, and critical-care consultation.\n"
     "• Identify and treat the precipitating cause."),
    ("03 — TREATMENT", "info", 
     "[color=#1E3A8A]A. Severe hypoglycemia[/color]\n"
     "• Conscious and can swallow: give 15–20 g fast-acting oral glucose, then recheck glucose after 15 minutes.\n"
     "• Cannot swallow/impaired consciousness: Give 10% dextrose 150–200 mL IV over 10–15 minutes, then reassess.\n"
     "• If IV access unavailable, glucagon 1 mg IM may be used.\n\n"
     "[color=#1E3A8A]B. Diabetic ketoacidosis in pregnancy[/color]\n"
     "• Begin IV isotonic crystalloid, often 500–1,000 mL in the first hour in adults if not fluid overloaded.\n"
     "• Start IV regular insulin according to local DKA protocol, commonly 0.1 unit/kg/hour after assessing potassium.\n"
     "• Add IV dextrose when glucose falls to ~200–250 mg/dL (11.1–13.9 mmol/L).\n"
     "• Potassium replacement must be individualized; withhold insulin temporarily if K+ is severely low."),
    ("04 — WARNINGS", "danger", 
     "• Do not give oral fluids or food to a patient with impaired consciousness or unsafe swallowing.\n"
     "• DKA in pregnancy can be severe at relatively modest glucose levels.\n"
     "• Avoid insulin if potassium is dangerously low until potassium replacement has made treatment safer.\n"
     "• Avoid routine bicarbonate; reserve it for exceptional circumstances."),
    ("05 — DISPOSITION", "warning", 
     "• Severe hypoglycemia with loss of consciousness, seizures, or prolonged drug effect requires monitored care.\n"
     "• DKA in pregnancy requires hospital admission and usually high-dependency or ICU-level monitoring."),
    ("REFERENCES", "info", "ADA Standards of Care; JBDS; NICE.")
]