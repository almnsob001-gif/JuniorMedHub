# data_ent.py

ENT_DATA = {
    "ENT Emergencies": {
        "Otology (Ear & Hearing)": [
            "Acute Mastoiditis",
            "Sudden Sensorineural Hearing Loss",
            "Necrotizing Otitis Externa",
            "Ear Canal Foreign Body and Button Battery",
            "Temporal Bone Fracture",
            "Acute Otitis Media with Intracranial Complications",
            "Spontaneous or Traumatic Ear Bleeding",
            "Acute Vertigo with Neurological Red Flags"
        ],
        "Rhinology (Nose & Sinuses)": [
            "Epistaxis (Nosebleed)",
            "Nasal Septal Hematoma",
            "Orbital Cellulitis and Orbital Abscess",
            "Complicated Acute Bacterial Sinusitis",
            "Acute Invasive Fungal Rhinosinusitis",
            "Nasal Foreign Body and Nasal Button Battery",
            "Cerebrospinal Fluid Rhinorrhea and Otorrhea",
            "Severe Epistaxis Refractory to Initial Treatment"
        ],
        "Pharyngology & Deep Neck Infections": [
            "Peritonsillar Abscess (Quinsy)",
            "Retropharyngeal Abscess",
            "Ludwig's Angina",
            "Parapharyngeal Abscess"
        ],
        "Laryngology & Upper Airway": [
            "Epiglottitis",
            "Foreign Body in Upper Airway",
            "Laryngeal Trauma",
            "Angioedema Affecting the Upper Airway",
            "Acute Laryngeal Edema and Stridor",
            "Tracheostomy Emergency",
            "Acute Complications of Tracheostomy"
        ],
        "Head, Neck & Esophageal Emergencies": [
            "Esophageal Food Bolus Impaction",
            "Caustic Injury of the Upper Aerodigestive Tract",
            "Facial Nerve Injury in ENT Emergencies"
        ]
    }
}

ENT_TOPICS = {}

ENT_TOPICS[("ENT Emergencies", "Epistaxis (Nosebleed)")] = [
    ("01 — DEFINITION", "info", "Bleeding from the nasal cavity, commonly from the anterior septum (Kiesselbach plexus). Posterior bleeding may be severe and difficult to control."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Visible nasal bleeding.\n"
     "• Blood dripping into the throat, especially with posterior bleeding.\n"
     "• Dizziness, pallor, tachycardia, or hypotension in significant hemorrhage."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and hemodynamic stability.\n"
     "• Sit the patient upright and lean forward.\n"
     "• Apply firm continuous pressure to the soft part of the nose for 10–15 minutes.\n"
     "• Suction blood from the mouth if necessary and safe.\n"
     "• Establish IV access and obtain CBC, coagulation tests, and blood grouping/crossmatch when bleeding is severe."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. TOPICAL VASOCONSTRICTOR[/color]\n"
     "• Oxymetazoline 0.05%: 2 sprays into the affected nostril; follow local protocol.\n"
     "• Apply with nasal compression. Reassess bleeding and vital signs.\n\n"
     "[color=#1E3A8A]B. CAUTERIZATION AND NASAL PACKING[/color]\n"
     "• If bleeding point is visible, topical anesthetic and cauterization by a trained clinician.\n"
     "• If bleeding persists, anterior nasal packing may be required.\n"
     "• Suspected posterior epistaxis requires urgent ENT assessment and admission."),
    ("05 — WARNINGS", "danger", 
     "• Use vasoconstrictors cautiously in patients with significant cardiovascular disease. Avoid prolonged use.\n"
     "• Avoid blind or traumatic instrumentation.\n"
     "• Do not remove anticoagulants permanently without assessing indication and bleeding severity."),
    ("06 — DISPOSITION", "warning", 
     "• Discharge if bleeding is controlled and patient is stable.\n"
     "• Admit or urgently refer for persistent bleeding, posterior epistaxis, significant blood loss, or need for posterior packing."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Lean forward; do not tilt the head backward.\n"
     "• Persistent bleeding despite appropriate compression requires escalation.\n"
     "• Recurrent unilateral bleeding warrants ENT assessment."),
    ("REFERENCES", "info", "AAO-HNSF: Nosebleed Clinical Practice Guideline.")
]

ENT_TOPICS[("ENT Emergencies", "Peritonsillar Abscess (Quinsy)")] = [
    ("01 — DEFINITION", "info", "A collection of pus between the tonsillar capsule and surrounding tissues, usually developing as a complication of tonsillitis."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Severe unilateral sore throat.\n"
     "• Fever and painful swallowing.\n"
     "• Trismus.\n"
     "• Muffled 'hot potato' voice.\n"
     "• Unilateral peritonsillar swelling and uvular deviation.\n"
     "• Drooling or inability to swallow in severe cases."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway and ability to handle secretions.\n"
     "• Keep NPO if drainage or anesthesia may be required.\n"
     "• Provide analgesia and IV fluids if oral intake is inadequate.\n"
     "• Obtain urgent ENT assessment.\n"
     "• Suspected airway compromise requires immediate senior airway support."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. DRAINAGE[/color]\n"
     "• Needle aspiration or incision and drainage by a trained clinician.\n"
     "• Obtain pus culture when indicated.\n\n"
     "[color=#1E3A8A]B. ANTIBIOTICS[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours.\n"
     "• Alternative: amoxicillin-clavulanate 875/125 mg PO every 12 hours.\n"
     "• Penicillin allergy: select alternative per local resistance.\n"
     "• Cover streptococci and oral anaerobes."),
    ("05 — WARNINGS", "danger", 
     "• Do not attempt drainage without appropriate training, equipment, and airway support.\n"
     "• Antibiotics alone may be insufficient when a drainable abscess is present."),
    ("06 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Severe tonsillitis.\n"
     "• Peritonsillar cellulitis.\n"
     "• Retropharyngeal or parapharyngeal abscess.\n"
     "• Epiglottitis."),
    ("07 — DISPOSITION", "warning", 
     "• Admit for airway concerns, sepsis, dehydration, inability to swallow, or failed outpatient treatment.\n"
     "• Discharge after successful treatment when airway is safe and oral intake is adequate."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Trismus and unilateral swelling strongly suggest quinsy.\n"
     "• Drooling, respiratory distress, or inability to handle secretions are emergency warning signs."),
    ("REFERENCES", "info", "Merck Manual Professional Edition: Peritonsillar Abscess.")
]

ENT_TOPICS[("ENT Emergencies", "Epiglottitis")] = [
    ("01 — DEFINITION", "info", "Acute inflammation and swelling of the epiglottis and adjacent supraglottic structures, potentially causing rapid, life-threatening airway obstruction."),
    ("02 — CAUSES", "info", 
     "• Haemophilus influenzae type b (Hib).\n"
     "• Streptococcus species.\n"
     "• Other bacterial pathogens."),
    ("03 — CLINICAL PRESENTATION", "info", 
     "• Sudden severe sore throat and fever.\n"
     "• Dysphagia and drooling.\n"
     "• Muffled voice.\n"
     "• Stridor and respiratory distress.\n"
     "• Tripod positioning and toxic appearance."),
    ("04 — IMMEDIATE ACTIONS", "success", 
     "• Recognize possible impending airway obstruction.\n"
     "• Keep the patient calm and in their preferred position.\n"
     "• Call senior anesthesia, ENT, and critical care teams immediately.\n"
     "• Provide oxygen in the least distressing manner.\n"
     "• Prepare for controlled airway management in an appropriate setting."),
    ("05 — WARNINGS", "danger", 
     "• Do not force the patient supine.\n"
     "• Do not use a tongue depressor to inspect the throat.\n"
     "• Do not perform unnecessary procedures that may precipitate complete obstruction.\n"
     "• Do not delay airway stabilization to obtain imaging, blood tests, or cultures."),
    ("06 — TREATMENT", "info", 
     "[color=#1E3A8A]A. AIRWAY MANAGEMENT[/color]\n"
     "• Secure the airway when clinically indicated, with the most experienced clinician.\n"
     "• Have a difficult-airway and emergency surgical-airway plan.\n\n"
     "[color=#1E3A8A]B. IV ANTIBIOTICS[/color]\n"
     "• Ceftriaxone 2 g IV every 24 hours (Adults).\n"
     "• Ceftriaxone 50 mg/kg IV every 24 hours (Pediatrics).\n"
     "• Obtain cultures when feasible without delaying antibiotics or airway stabilization."),
    ("07 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Viral croup.\n"
     "• Bacterial tracheitis.\n"
     "• Retropharyngeal abscess.\n"
     "• Foreign body aspiration.\n"
     "• Angioedema."),
    ("08 — DISPOSITION", "warning", 
     "• Hospital admission is required.\n"
     "• ICU-level care is indicated for airway compromise, significant respiratory distress, or need for airway protection."),
    ("09 — CLINICAL PEARLS", "info", 
     "• Drooling, dysphagia, severe sore throat, and toxic appearance should raise suspicion.\n"
     "• Stridor may be a late sign of severe obstruction."),
    ("REFERENCES", "info", "Merck Manual Professional Edition: Epiglottitis.")
]

ENT_TOPICS[("ENT Emergencies", "Retropharyngeal Abscess")] = [
    ("01 — DEFINITION", "info", "A deep neck space infection involving the retropharyngeal tissues, occurring predominantly in young children but also possible in adults."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Fever and sore throat.\n"
     "• Dysphagia or drooling.\n"
     "• Neck stiffness, pain, or limited neck movement.\n"
     "• Muffled voice.\n"
     "• Posterior pharyngeal wall swelling.\n"
     "• Stridor or respiratory distress in severe cases."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway and ability to handle secretions.\n"
     "• Keep the patient NPO.\n"
     "• Obtain urgent ENT and pediatric/anesthesia support.\n"
     "• Establish IV access and provide fluids.\n"
     "• Avoid unnecessary throat manipulation in a child with airway symptoms."),
    ("04 — INVESTIGATIONS", "info", 
     "• CBC and CRP.\n"
     "• Contrast-enhanced CT of the neck when stable.\n"
     "• Blood cultures in suspected sepsis.\n"
     "• Do not delay airway management for imaging."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV ANTIBIOTICS[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours (Adults).\n"
     "• Ampicillin-sulbactam 50 mg/kg/dose IV every 6 hours (Pediatrics).\n"
     "• Alternative: Ceftriaxone plus metronidazole.\n"
     "• Cover streptococci, oral anaerobes, and S. aureus.\n\n"
     "[color=#1E3A8A]B. DRAINAGE[/color]\n"
     "• Indications: Airway compromise, sepsis, large/mature abscess, failure to improve with antibiotics."),
    ("06 — WARNINGS", "danger", 
     "• A threatened airway requires immediate management. Do not wait for antibiotic response."),
    ("07 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Epiglottitis.\n"
     "• Peritonsillar abscess.\n"
     "• Bacterial cervical lymphadenitis.\n"
     "• Meningitis.\n"
     "• Foreign body."),
    ("08 — DISPOSITION", "warning", 
     "• Hospital admission for IV antibiotics and observation.\n"
     "• ICU care for airway compromise or severe sepsis."),
    ("09 — CLINICAL PEARLS", "info", 
     "• Neck stiffness with fever and dysphagia in a child is concerning.\n"
     "• Airway obstruction and mediastinal spread are important complications."),
    ("REFERENCES", "info", "Merck Manual Professional Edition: Deep Neck Infections.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Mastoiditis")] = [
    ("01 — DEFINITION", "info", "Acute infection of the mastoid air cells, usually following acute otitis media. It can progress to bone destruction, subperiosteal abscess, or intracranial complications."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Fever and ear pain.\n"
     "• Recent or current acute otitis media.\n"
     "• Postauricular erythema, swelling, and tenderness.\n"
     "• Protrusion of the pinna.\n"
     "• Otorrhea or hearing impairment.\n"
     "• Severe headache, vomiting, meningism, or neurological signs."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs and signs of sepsis.\n"
     "• Perform otoscopy and examine the postauricular region.\n"
     "• Obtain urgent ENT assessment.\n"
     "• Establish IV access and provide analgesia and fluids.\n"
     "• Admit patients with suspected acute mastoiditis."),
    ("04 — INVESTIGATIONS", "info", 
     "• CBC and CRP.\n"
     "• Blood cultures if febrile or septic.\n"
     "• Culture ear discharge when available.\n"
     "• CT temporal bone if complications or diagnostic uncertainty.\n"
     "• MRI if intracranial complications suspected."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV ANTIBIOTICS[/color]\n"
     "• Ceftriaxone 50 mg/kg IV every 24 hours (Pediatrics).\n"
     "• Ceftriaxone 1–2 g IV every 24 hours (Adults).\n"
     "• Adjust antibiotics to culture results and specialist advice.\n\n"
     "[color=#1E3A8A]B. SOURCE CONTROL[/color]\n"
     "• ENT may perform myringotomy or tympanostomy.\n"
     "• Mastoidectomy or drainage may be required for abscess or failure of medical therapy."),
    ("06 — WARNINGS", "danger", 
     "• Do not delay ENT review when postauricular swelling or pinna displacement is present."),
    ("07 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Uncomplicated acute otitis media.\n"
     "• Otitis externa.\n"
     "• Postauricular cellulitis."),
    ("08 — DISPOSITION", "warning", 
     "• Hospital admission and urgent ENT involvement.\n"
     "• ICU or tertiary referral for sepsis or suspected intracranial spread."),
    ("09 — CLINICAL PEARLS", "info", 
     "• Postauricular swelling and protrusion of the pinna are key findings.\n"
     "• Meningitis, venous sinus thrombosis, and intracranial abscess are serious complications."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne: Acute Otitis Media and Mastoiditis.")
]

ENT_TOPICS[("ENT Emergencies", "Sudden Sensorineural Hearing Loss")] = [
    ("01 — DEFINITION", "info", "Sudden sensorineural hearing loss is a rapid decline in hearing, typically developing within 72 hours. It is an otologic emergency requiring prompt assessment and treatment consideration."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Sudden unilateral hearing loss, sometimes bilateral.\n"
     "• Tinnitus or a feeling of ear fullness.\n"
     "• Vertigo may occur.\n"
     "• Otoscopy may be normal.\n\n"
     "[color=#991B1B]RED FLAGS: Hearing loss with facial weakness, diplopia, ataxia, or other focal neurological signs. Bilateral sudden hearing loss.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Establish the onset and progression of hearing loss.\n"
     "• Perform otoscopy to exclude wax, effusion, and conductive causes.\n"
     "• Perform bedside hearing assessment and tuning-fork tests.\n"
     "• Arrange urgent ENT assessment and audiometry.\n"
     "• Evaluate urgently for stroke if neurological symptoms are present."),
    ("04 — INVESTIGATIONS", "info", 
     "• Pure-tone audiometry as soon as possible.\n"
     "• MRI of internal auditory canals/brain when indicated.\n"
     "• Routine head CT is not recommended for typical idiopathic SSNHL."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. CORTICOSTEROIDS[/color]\n"
     "• Prednisone/prednisolone ~1 mg/kg PO daily (max 60 mg/day) for 7–14 days.\n"
     "• Consider within 2 weeks of symptom onset.\n"
     "• Monitor blood glucose, blood pressure, mood, GI symptoms.\n"
     "• ENT may consider intratympanic steroid therapy if incomplete recovery."),
    ("06 — WARNINGS", "danger", 
     "• Treatment benefit is not guaranteed.\n"
     "• Do not delay urgent ENT referral while waiting for routine investigations."),
    ("07 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Cerumen impaction.\n"
     "• Otitis media with effusion.\n"
     "• Ear trauma or barotrauma.\n"
     "• Ménière disease.\n"
     "• Vestibular schwannoma.\n"
     "• Posterior circulation stroke."),
    ("08 — DISPOSITION", "warning", 
     "• Urgent ENT assessment, ideally the same day or within 24 hours.\n"
     "• Emergency neurological assessment for focal deficits."),
    ("09 — CLINICAL PEARLS", "info", 
     "• A normal otoscopic examination does not exclude SSNHL.\n"
     "• Early audiometry and timely treatment assessment are important.\n"
     "• Routine antivirals, thrombolytics, and head CT are not recommended."),
    ("REFERENCES", "info", "AAO-HNSF: Clinical Practice Guideline — Sudden Hearing Loss.")
]

ENT_TOPICS[("ENT Emergencies", "Nasal Septal Hematoma")] = [
    ("01 — DEFINITION", "info", "A collection of blood between the nasal septal cartilage and its mucoperichondrium, usually following nasal trauma. Delayed treatment can cause cartilage necrosis, septal abscess, and permanent nasal deformity."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Recent nasal trauma.\n"
     "• Nasal obstruction, often bilateral.\n"
     "• Pain and tenderness.\n"
     "• Soft, boggy swelling of the nasal septum.\n"
     "• Persistent obstruction despite apparent improvement in external swelling."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Ask about trauma and timing.\n"
     "• Examine the septum using appropriate illumination.\n"
     "• Arrange urgent ENT assessment.\n"
     "• Assess for associated facial fractures, significant bleeding, or head injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. URGENT DRAINAGE[/color]\n"
     "• Prompt incision and drainage by a trained clinician.\n"
     "• ENT may place a drain, quilting sutures, or packing to prevent re-accumulation.\n\n"
     "[color=#1E3A8A]B. ANTIBIOTICS[/color]\n"
     "• May be prescribed after drainage according to local ENT protocol."),
    ("05 — WARNINGS", "danger", 
     "• A suspected septal hematoma requires urgent drainage; do not manage it with observation or antibiotics alone."),
    ("06 — INVESTIGATIONS", "info", 
     "• Diagnosis is primarily clinical.\n"
     "• CT is not routinely required for isolated septal hematoma."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent ENT review and drainage.\n"
     "• Admit or escalate care for septal abscess or associated major facial trauma."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Always inspect the nasal septum after significant nasal trauma.\n"
     "• Early treatment prevents cartilage necrosis and saddle-nose deformity."),
    ("REFERENCES", "info", "Merck Manual Professional Edition: Nasal Fractures.")
]

ENT_TOPICS[("ENT Emergencies", "Foreign Body in Upper Airway")] = [
    ("01 — DEFINITION", "info", "Partial or complete airway obstruction caused by an aspirated object. Complete obstruction is immediately life-threatening."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Sudden choking or coughing.\n"
     "• Inability to speak or cry effectively.\n"
     "• Weak or absent cough.\n"
     "• Stridor, wheezing, or reduced air entry.\n"
     "• Cyanosis or loss of consciousness."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "[color=#1E3A8A]SEVERE OBSTRUCTION — ADULTS AND CHILDREN >1 YEAR[/color]\n"
     "• If can cough effectively, encourage coughing.\n"
     "• If unable to cough/speak/breathe: back blows followed by abdominal thrusts.\n"
     "• Use chest thrusts in pregnancy or if abdominal not feasible.\n"
     "• If unresponsive, begin CPR.\n\n"
     "[color=#1E3A8A]INFANTS UNDER 1 YEAR[/color]\n"
     "• 5 back blows and 5 chest thrusts.\n"
     "• Do NOT perform abdominal thrusts in infants.\n"
     "• If unresponsive, begin infant CPR."),
    ("04 — WARNINGS", "danger", 
     "• Do not perform blind finger sweeps. Remove an object only when it is visible and safely graspable."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Urgent airway and ENT/anesthesia support for persistent obstruction.\n"
     "• Direct laryngoscopy or bronchoscopy may be required."),
    ("06 — INVESTIGATIONS", "info", 
     "• Imaging depends on suspected object and location.\n"
     "• A normal chest X-ray does not exclude a radiolucent foreign body."),
    ("07 — DISPOSITION", "warning", 
     "• Emergency resuscitation for severe obstruction.\n"
     "• Urgent specialist assessment for suspected retained airway foreign bodies."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Sudden choking with unilateral wheeze suggests aspiration.\n"
     "• Button batteries and sharp objects require urgent specialist assessment.\n"
     "• Do not delay life-saving airway maneuvers for imaging."),
    ("REFERENCES", "info", "Resuscitation Council UK: Adult and Paediatric BLS Guidelines.")
]

ENT_TOPICS[("ENT Emergencies", "Ludwig's Angina")] = [
    ("01 — DEFINITION", "info", "A rapidly progressive cellulitis of the submandibular, sublingual, and submental spaces, commonly originating from an odontogenic infection. Tongue elevation and floor-of-mouth swelling can cause life-threatening airway obstruction."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Dental pain or recent dental infection.\n"
     "• Painful, firm swelling beneath the jaw.\n"
     "• Floor-of-mouth induration and tongue elevation.\n"
     "• Dysphagia, drooling, and muffled voice.\n"
     "• Fever and systemic toxicity.\n"
     "• Respiratory distress or stridor.\n\n"
     "[color=#991B1B]RED FLAGS: Rapidly progressive swelling, inability to swallow secretions, tongue elevation, stridor, hypoxemia.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess the airway immediately.\n"
     "• Call ENT, anesthesia, and oral/maxillofacial surgery urgently.\n"
     "• Keep NPO and upright if tolerated.\n"
     "• Provide oxygen and monitoring.\n"
     "• Establish IV access and initiate sepsis management.\n"
     "• Prepare for early definitive airway management."),
    ("04 — WARNINGS", "danger", 
     "• Do not delay airway protection for CT imaging.\n"
     "• Sedation or routine induction in an unstable patient may precipitate complete airway obstruction."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV ANTIBIOTICS[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours.\n"
     "• Alternative: Ceftriaxone plus metronidazole.\n"
     "• Cover oral streptococci and anaerobes.\n\n"
     "[color=#1E3A8A]B. SOURCE CONTROL[/color]\n"
     "• Drainage of infected spaces when indicated.\n"
     "• Definitive treatment of the dental source."),
    ("06 — INVESTIGATIONS", "info", 
     "• CBC, CRP, renal function, blood cultures.\n"
     "• Contrast-enhanced CT of the neck in stable patients."),
    ("07 — DISPOSITION", "warning", 
     "• Hospital admission is required.\n"
     "• ICU care for airway compromise or sepsis."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Ludwig's angina may obstruct the airway before a discrete abscess develops.\n"
     "• Early airway planning and IV antibiotics are essential."),
    ("REFERENCES", "info", "Merck Manual Professional Edition: Deep Neck Infections.")
]

ENT_TOPICS[("ENT Emergencies", "Tracheostomy Emergency")] = [
    ("01 — DEFINITION", "info", "An acute problem involving a tracheostomy tube or stoma, including obstruction, displacement, accidental decannulation, bleeding, or respiratory deterioration."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Respiratory distress or desaturation.\n"
     "• Difficulty passing a suction catheter.\n"
     "• Reduced or absent airflow through the tube.\n"
     "• Absent or abnormal capnography waveform.\n"
     "• Tube displacement or accidental decannulation.\n"
     "• Bleeding from the tube or stoma."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Call resuscitation team and experienced airway support.\n"
     "• Apply high-concentration oxygen to both the face AND the tracheostomy stoma.\n"
     "• Remove any speaking valve or cap.\n"
     "• Remove a removable inner cannula and check for obstruction.\n"
     "• Attempt gentle suction if trained.\n"
     "• If tube is nonfunctional, remove promptly according to emergency algorithm."),
    ("04 — WARNINGS", "danger", 
     "• Do not repeatedly attempt ventilation through a tube confirmed blocked or displaced.\n"
     "• Avoid blind reinsertion, particularly through an immature stoma."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. BLOCKED TRACHEOSTOMY[/color]\n"
     "• Remove inner cannula.\n"
     "• Attempt suction.\n"
     "• If obstructed, remove nonfunctional tube.\n"
     "• Oxygenate through face or stoma.\n\n"
     "[color=#1E3A8A]B. DISPLACED TUBE[/color]\n"
     "• Assess upper airway patency.\n"
     "• Reinsertion only by trained clinician to avoid false passage.\n\n"
     "[color=#1E3A8A]C. BLEEDING[/color]\n"
     "• Minor bleeding: evaluate for trauma/infection.\n"
     "• Significant/pulsatile bleeding: major vascular complication, requires immediate surgical management."),
    ("06 — MONITORING", "info", 
     "• Continuous SpO2 and cardiorespiratory monitoring.\n"
     "• Waveform capnography when available.\n"
     "• Reassess chest movement, airflow, consciousness."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent ICU or specialist airway management for obstruction, displacement, or major bleeding."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Oxygenation takes priority over attempts to save the tube.\n"
     "• A blocked or displaced tube should not be left in place.\n"
     "• Total laryngectomy patients must be ventilated through the neck stoma (no connection to upper airway)."),
    ("REFERENCES", "info", "National Tracheostomy Safety Project (NTSP); OpenAnesthesia.")
]


# ==================== NEW ENT TOPICS (11-20) ====================

ENT_TOPICS[("ENT Emergencies", "Orbital Cellulitis and Orbital Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "Fever, eyelid swelling, erythema, and significant ocular pain.\n"
     "• Painful or restricted extraocular movements.\n"
     "• Proptosis, diplopia, or chemosis.\n"
     "• Reduced visual acuity, impaired color vision, or a relative afferent pupillary defect.\n"
     "• Recent acute sinusitis, particularly ethmoid sinusitis.\n"
     "• Severe headache, altered mental status, or cranial nerve abnormalities may indicate intracranial extension.\n\n"
     "[color=#991B1B]PRESEPTAL CELLULITIS:[/color] Eyelid inflammation without proptosis, impaired vision, or painful/restricted eye movements.\n"
     "[color=#991B1B]ORBITAL CELLULITIS:[/color] Infection posterior to the orbital septum; a vision-threatening emergency."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, temperature, mental status, and sepsis indicators.\n"
     "• Document baseline visual acuity in each eye, pupils, color vision if feasible, ocular movements, and proptosis.\n"
     "• Obtain immediate ophthalmology and ENT consultation.\n"
     "• Start IV antibiotics promptly when orbital cellulitis is suspected; do not delay treatment for imaging.\n"
     "• Keep the patient fasting if urgent surgery is possible.\n"
     "• Escalate immediately for deteriorating vision, rapidly progressive proptosis, ophthalmoplegia, or neurological abnormalities."),
    ("03 — INVESTIGATIONS", "info", 
     "• Contrast-enhanced CT of the orbits and paranasal sinuses.\n"
     "• MRI brain and orbits if intracranial extension, cavernous sinus thrombosis, or another intracranial complication is suspected.\n"
     "• CBC, CRP, renal function, electrolytes, and blood cultures if febrile or systemically unwell.\n"
     "• Culture material obtained during surgical drainage when available.\n"
     "• Consider glucose and HbA1c if diabetes is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Empiric IV Antibiotics — Adults[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours.\n"
     "• Alternative broad-spectrum: Ceftriaxone 2 g IV every 24 hours (some intracranial infections require 2 g every 12 hours).\n"
     "• Add Metronidazole 500 mg IV every 8 hours when anaerobic coverage is indicated (abscess or intracranial extension).\n"
     "• Add Vancomycin (weight-based, renal adjusted, therapeutic monitoring) if MRSA coverage is indicated.\n\n"
     "[color=#1E3A8A]2. Definitive Management[/color]\n"
     "• Urgent surgical drainage may be necessary for an orbital abscess, visual compromise, deterioration despite antibiotics, or selected large abscesses.\n"
     "• Drain associated infected sinuses when indicated by ENT.\n"
     "• Modify antibiotics according to cultures and clinical response."),
    ("05 — WARNINGS", "danger", 
     "• Adjust dosing in renal impairment. Regimens may be insufficient when MRSA risk or other resistant organisms require additional coverage.\n"
     "• Ceftriaxone alone does not provide reliable MRSA or anaerobic coverage.\n"
     "• Rapid vancomycin infusion can cause an infusion reaction. Avoid unmonitored dosing, especially in renal impairment."),
    ("06 — DISPOSITION", "warning", 
     "• Admit all suspected orbital cellulitis cases for urgent specialist assessment and IV treatment.\n"
     "• Consider a higher-acuity setting for visual deterioration, sepsis, intracranial extension, or rapidly progressive disease.\n"
     "• Discharge only when a specialist confirms that the condition is preseptal rather than orbital and outpatient treatment is appropriate."),
    ("REFERENCES", "info", "AAO Orbital Cellulitis Guidance; IDSA Guidance; Local ENT/Ophthalmology Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Complicated Acute Bacterial Sinusitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Persistent or worsening nasal obstruction, purulent nasal discharge, facial pain, or fever.\n"
     "• Severe frontal headache, forehead swelling, or focal frontal bone tenderness.\n"
     "• Periorbital swelling, proptosis, diplopia, or reduced visual acuity.\n"
     "• Meningism, altered mental status, focal neurological deficits, or seizures.\n"
     "• Severe systemic illness or deterioration after initial improvement.\n\n"
     "[color=#991B1B]RED FLAGS:[/color] Orbital signs, neurological symptoms, forehead swelling, or suspected intracranial infection require emergency evaluation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, circulation, mental status, visual function, and sepsis.\n"
     "• Obtain urgent ENT review; involve ophthalmology or neurosurgery if orbital or intracranial complications are suspected.\n"
     "• Start IV antibiotics promptly when complicated bacterial infection is suspected.\n"
     "• Do not delay antibiotics in an unstable patient while waiting for imaging or specialist arrival.\n"
     "• Keep fasting if operative drainage may be required."),
    ("03 — INVESTIGATIONS", "info", 
     "• Contrast-enhanced CT of the paranasal sinuses and orbits when orbital complications are suspected.\n"
     "• Contrast-enhanced CT or MRI of the brain when intracranial extension is suspected; MRI is particularly useful for intracranial soft-tissue complications.\n"
     "• CBC, CRP, renal function, electrolytes, and blood cultures in severe systemic illness.\n"
     "• Obtain cultures from surgically drained collections where feasible.\n"
     "• Consider glucose testing in severe or recurrent infection."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Empiric IV Antibiotics — Adults[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours.\n"
     "• Alternative for severe/intracranial: Ceftriaxone 2 g IV every 12–24 hours (meningitis regimen for intracranial infection).\n"
     "• Add Metronidazole 500 mg IV every 8 hours when anaerobic coverage is indicated.\n"
     "• Add Vancomycin if MRSA coverage is indicated (weight-based, renal adjusted).\n\n"
     "[color=#1E3A8A]2. Definitive Management[/color]\n"
     "• Drain orbital, subperiosteal, or intracranial collections when indicated.\n"
     "• ENT may perform endoscopic sinus surgery for source control.\n"
     "• Neurosurgical drainage may be required for selected intracranial abscesses.\n"
     "• Tailor antimicrobial therapy to cultures, imaging, clinical response, and specialist recommendations.\n"
     "• Pott's puffy tumor (frontal bone osteomyelitis with forehead swelling) requires urgent specialist management and assessment for intracranial spread."),
    ("05 — WARNINGS", "danger", 
     "• Consider alternative or additional coverage for resistant organisms, intracranial infection, or specific exposure risks.\n"
     "• Do not use ceftriaxone alone when anaerobic or MRSA coverage is indicated.\n"
     "• Intracranial infection requires a dedicated specialist-directed regimen; do not assume every sinusitis case requires metronidazole."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected orbital or intracranial complications.\n"
     "• Escalate to critical care for shock, airway compromise, or severe neurological deterioration.\n"
     "• Outpatient treatment is appropriate only for uncomplicated sinusitis after red flags have been excluded."),
    ("REFERENCES", "info", "AAO-HNS Adult Sinusitis Guidance; IDSA Acute Bacterial Rhinosinusitis Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Invasive Fungal Rhinosinusitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Rapidly progressive facial pain, nasal congestion, fever, or facial swelling.\n"
     "• Black, pale, or necrotic nasal mucosa may occur but is not always present.\n"
     "• Facial numbness, palatal necrosis, proptosis, ophthalmoplegia, or visual loss.\n"
     "• Severe headache, altered mental status, or focal neurological findings.\n"
     "• Major risk factors: uncontrolled diabetes, DKA, neutropenia, hematologic malignancy, transplantation, significant immunosuppression.\n\n"
     "[color=#991B1B]CRITICAL POINT:[/color] Early mucosal appearance may be deceptively normal. Do not wait for black eschar before suspecting invasive fungal disease in a high-risk patient."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as a time-critical emergency.\n"
     "• Contact ENT, infectious diseases, ophthalmology, and the relevant medical team immediately.\n"
     "• Assess and correct diabetic ketoacidosis, hyperglycemia, neutropenia, and other reversible risk factors.\n"
     "• Arrange urgent nasal endoscopy and tissue biopsy.\n"
     "• Start appropriate antifungal treatment when suspicion is high; do not wait for final culture results.\n"
     "• Arrange urgent surgical debridement when indicated.\n"
     "• Evaluate for orbital and intracranial extension."),
    ("03 — INVESTIGATIONS", "info", 
     "• Urgent nasal endoscopy with biopsy for histopathology and fungal studies.\n"
     "• Contrast-enhanced MRI of the face, orbits, and brain where feasible to assess soft-tissue and intracranial involvement.\n"
     "• CT of the sinuses to evaluate bony anatomy and associated sinus disease.\n"
     "• CBC with differential, renal function, electrolytes, glucose, ketones, and acid-base status when indicated.\n"
     "• Blood cultures if febrile or systemically unwell; negative blood cultures do not exclude invasive fungal infection."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Liposomal Amphotericin B[/color]\n"
     "• Dose: 5 mg/kg IV every 24 hours for mucormycosis; higher dosing (often 10 mg/kg/day) may be considered for CNS involvement under specialist direction.\n"
     "• Monitor creatinine, potassium, magnesium, fluid status, and liver function. Replace electrolytes when indicated.\n\n"
     "[color=#1E3A8A]2. Control Underlying Metabolic Abnormalities[/color]\n"
     "• Follow the relevant DKA or hyperglycemic emergency protocol for insulin, IV fluids, and electrolyte replacement.\n\n"
     "[color=#1E3A8A]3. Definitive Management[/color]\n"
     "• Urgent endoscopic surgical debridement of necrotic tissue; repeat procedures may be required.\n"
     "• Histopathology and culture guide diagnosis and ongoing therapy.\n"
     "• Reverse immunosuppression when feasible.\n"
     "• Continue antifungal treatment until clinical and radiological response and reversal of risk factors are achieved."),
    ("05 — WARNINGS", "danger", 
     "• Formulations are not dose-interchangeable. Amphotericin B can cause nephrotoxicity, hypokalemia, hypomagnesemia, and infusion reactions.\n"
     "• Correcting hyperglycemia alone is not adequate treatment for invasive fungal disease."),
    ("06 — DISPOSITION", "warning", 
     "• Admit urgently; these patients generally require inpatient multidisciplinary care.\n"
     "• ICU care may be necessary for DKA, sepsis, major neurological involvement, or extensive disease.\n"
     "• Do not discharge a patient with credible suspicion of acute invasive fungal rhinosinusitis for routine outpatient follow-up."),
    ("REFERENCES", "info", "ECMM/MSG Global Guideline for Mucormycosis; IDSA Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Necrotizing Otitis Externa")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe, persistent ear pain, often worse at night and disproportionate to routine otitis externa.\n"
     "• Purulent otorrhea and granulation tissue in the external auditory canal.\n"
     "• Commonly occurs in older adults with diabetes or in immunocompromised patients.\n"
     "• Facial nerve palsy, dysphagia, hoarseness, or other cranial neuropathies suggest skull-base involvement.\n"
     "• Persistent symptoms despite standard topical treatment raise suspicion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for sepsis, cranial neuropathies, and spread beyond the external auditory canal.\n"
     "• Obtain urgent ENT review.\n"
     "• Check glucose and assess diabetes control.\n"
     "• Obtain appropriate cultures before antibiotics when feasible, provided this does not delay treatment in a severely ill patient.\n"
     "• Avoid traumatic canal manipulation and repeated blind instrumentation.\n"
     "• Begin systemic antipseudomonal treatment when invasive disease is suspected, guided by specialist and local resistance patterns."),
    ("03 — INVESTIGATIONS", "info", 
     "• Ear canal examination and culture of discharge or granulation tissue.\n"
     "• CBC, CRP/ESR, renal function, and glucose.\n"
     "• CT of the temporal bone for bony erosion and anatomical assessment.\n"
     "• MRI when soft-tissue, skull-base, cranial nerve, or intracranial extension is suspected.\n"
     "• Consider biopsy if malignancy or an alternative diagnosis is possible."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Systemic Antipseudomonal Antibiotics[/color]\n"
     "• Option A: Cefepime 2 g IV every 8–12 hours (adjust for renal function).\n"
     "• Option B: Ceftazidime 2 g IV every 8 hours (renal adjustment).\n"
     "• Option C: Piperacillin-tazobactam 4.5 g IV every 6–8 hours (adjust for renal function).\n\n"
     "[color=#1E3A8A]2. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed (max daily limit).\n\n"
     "[color=#1E3A8A]3. Definitive Management[/color]\n"
     "• Obtain cultures and tailor systemic antimicrobial therapy.\n"
     "• Provide careful aural toilet by trained staff.\n"
     "• Optimize glycemic control and address immunosuppression.\n"
     "• Imaging and serial clinical assessment guide treatment duration; prolonged systemic therapy is often required.\n"
     "• Surgery is reserved for selected cases (diagnostic uncertainty, abscess, or non-response)."),
    ("05 — WARNINGS", "danger", 
     "• Renal impairment increases the risk of cefepime-associated neurotoxicity. Adjust the dose accordingly.\n"
     "• Select according to local susceptibility data; resistance may make ceftazidime inappropriate.\n"
     "• Broad-spectrum therapy should be narrowed when cultures permit."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with cranial neuropathy, skull-base involvement, sepsis, severe uncontrolled pain, or inability to manage safely as an outpatient.\n"
     "• Outpatient treatment may be considered only for selected stable patients with reliable specialist follow-up and a clear antimicrobial plan."),
    ("REFERENCES", "info", "UK Specialist Guidance on Necrotizing Otitis Externa; IDSA Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Ear Canal Foreign Body and Button Battery")] = [
    ("01 — RECOGNIZE", "info", 
     "Ear pain, foreign-body sensation, reduced hearing, bleeding, or otorrhea.\n"
     "• Visible object in the external auditory canal.\n"
     "• Button battery may cause rapid tissue necrosis, liquefaction, and perforation.\n"
     "• Suspect tympanic membrane injury if there is bleeding, severe pain, sudden hearing loss, or vertigo.\n"
     "• In children, ask about possible insertion of button batteries, paired magnets, or sharp objects."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Identify the object, its location, and the duration of impaction.\n"
     "• Button battery in the ear: urgent removal is required. Do not wait for symptoms.\n"
     "• Urgently refer to ENT if a battery, paired magnets, sharp object, deeply impacted object, or object adjacent to the tympanic membrane is present.\n"
     "• Do not irrigate a button battery, magnet, vegetable matter, or other object that may swell or react with water.\n"
     "• Avoid repeated blind attempts; stop if the object is pushed deeper, bleeding occurs, or the patient cannot remain still.\n"
     "• Do not use potentially ototoxic drops if tympanic membrane perforation is suspected unless specifically directed by a clinician."),
    ("03 — INVESTIGATIONS", "info", 
     "• Otoscopy, ideally documenting the object and canal condition before and after removal.\n"
     "• Assess hearing symptoms and examine the tympanic membrane after removal when possible.\n"
     "• Formal hearing assessment if persistent hearing loss, suspected tympanic injury, or other auditory symptoms are present.\n"
     "• Imaging is not routinely required for a straightforward visible foreign body but may be necessary for suspected complications or an unidentifiable object."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Removal of a Non-Hazardous Foreign Body[/color]\n"
     "• Select method based on object type, location, shape, and patient cooperation. Options include forceps, a suitable hook, suction, or irrigation only when appropriate.\n"
     "• Use direct visualization. A single well-planned attempt is preferable to repeated unsuccessful attempts. Re-examine the canal and tympanic membrane after removal.\n\n"
     "[color=#1E3A8A]2. Button Battery[/color]\n"
     "• Immediate removal by a clinician with suitable equipment and expertise. Arrange urgent ENT assistance if removal cannot be performed safely.\n"
     "• After removal, assess canal skin, tympanic membrane integrity, bleeding, hearing, and signs of chemical injury. ENT follow-up may be required even if the battery is removed promptly.\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed (max daily limit)."),
    ("05 — WARNINGS", "danger", 
     "• Never irrigate the ear with a button battery in place. Do not apply ear drops or other substances as a substitute for removal.\n"
     "• Analgesia must not delay urgent battery removal or ENT referral.\n"
     "• Avoid irrigation if the tympanic membrane may be perforated, the object is a battery or magnet, or the object is hygroscopic or likely to swell."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate ENT assessment for a button battery, paired magnets, sharp object, tympanic membrane injury, significant bleeding, or failed removal.\n"
     "• Discharge may be appropriate after uncomplicated removal when the canal and tympanic membrane are satisfactory and no significant symptoms remain.\n"
     "• Provide clear return precautions for worsening pain, discharge, fever, vertigo, or hearing loss."),
    ("REFERENCES", "info", "AAO-HNS Ear Foreign-Body Management Principles; Pediatric Button Battery Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Nasal Foreign Body and Nasal Button Battery")] = [
    ("01 — RECOGNIZE", "info", 
     "Unilateral foul-smelling nasal discharge, nasal obstruction, epistaxis, or localized pain, particularly in children.\n"
     "• Visible foreign body in one nostril.\n"
     "• Button battery or paired magnets may cause rapid mucosal necrosis, septal perforation, and permanent tissue damage.\n"
     "• Fever, facial swelling, severe pain, or purulent discharge may indicate secondary infection or tissue injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess breathing and determine whether the object is confined to the nose or may have been aspirated.\n"
     "• Identify the object, location, duration, and whether paired magnets or a battery may be present.\n"
     "• A nasal button battery requires immediate removal. Do not delay for routine imaging or outpatient follow-up.\n"
     "• Obtain urgent ENT assistance for batteries, paired magnets, posteriorly located objects, significant bleeding, or failed removal.\n"
     "• Do not irrigate the nose or push the object posteriorly.\n"
     "• Avoid repeated unsuccessful attempts, which may cause bleeding, aspiration, or deeper impaction."),
    ("03 — INVESTIGATIONS", "info", 
     "• Anterior rhinoscopy or nasal endoscopy when available.\n"
     "• Imaging is not routinely required for a visible uncomplicated foreign body.\n"
     "• Consider imaging if the object is not identified, complications are suspected, or an unusual radiopaque object may be present.\n"
     "• Evaluate for aspiration if there is coughing, choking, wheezing, or respiratory distress."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Removal of a Non-Hazardous Foreign Body[/color]\n"
     "• A trained clinician may use direct-vision forceps, suction, a suitable hook, or a positive-pressure technique in carefully selected cooperative patients.\n"
     "• Use direct visualization and an appropriate technique for the object's shape and location. Confirm complete removal and reassess the nasal mucosa.\n\n"
     "[color=#1E3A8A]2. Nasal Button Battery or Paired Magnets[/color]\n"
     "• Immediate removal by an appropriately trained clinician; obtain urgent ENT support if safe removal is not straightforward.\n"
     "• After removal, assess mucosal injury, septal damage, bleeding, and possible retained fragments. Arrange ENT follow-up because tissue injury may progress after removal.\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed in adults (max daily limit)."),
    ("05 — WARNINGS", "danger", 
     "• Do not irrigate, delay removal, or attempt repeated blind extraction. Button batteries can cause severe injury within a short time.\n"
     "• Avoid blind instrumentation and repeated attempts. Do not use positive-pressure techniques for a button battery, paired magnets, or an object with a high aspiration risk."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent ENT assessment for batteries, paired magnets, significant injury, or failed removal.\n"
     "• Discharge after uncomplicated removal may be appropriate when bleeding is controlled and no complication is suspected.\n"
     "• Return immediately for fever, increasing pain, persistent bleeding, foul discharge, or breathing difficulty."),
    ("REFERENCES", "info", "AAO-HNS Nasal Foreign-Body Management Principles; Pediatric Button Battery Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Laryngeal Trauma")] = [
    ("01 — RECOGNIZE", "info", 
     "Blunt or penetrating injury to the anterior neck.\n"
     "• Hoarseness, dysphonia, aphonia, or painful swallowing.\n"
     "• Stridor, dyspnea, hemoptysis, or subcutaneous emphysema.\n"
     "• Neck swelling, tenderness over the larynx, or palpable structural abnormality.\n"
     "• Respiratory distress or progressive voice change may indicate evolving airway obstruction.\n\n"
     "[color=#991B1B]CRITICAL POINT:[/color] A patient who initially appears stable can deteriorate as laryngeal edema and hematoma progress."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma priorities and assess airway, breathing, and circulation.\n"
     "• Call ENT and anesthesia early if laryngeal injury is suspected.\n"
     "• Provide oxygen and continuous monitoring.\n"
     "• Keep the patient fasting and prepare difficult-airway equipment.\n"
     "• Avoid unnecessary manipulation of the neck and avoid blind airway instrumentation.\n"
     "• If airway obstruction is imminent, secure the airway with the most appropriate expert-led technique; emergency front-of-neck access may be required.\n"
     "• Control external bleeding without compromising the airway."),
    ("03 — INVESTIGATIONS", "info", 
     "• Flexible nasolaryngoscopy in a stable patient when performed by an appropriately trained clinician.\n"
     "• CT of the neck with contrast in a stable patient when structural injury or associated vascular injury is suspected.\n"
     "• CT angiography if the mechanism or findings suggest blunt cerebrovascular injury.\n"
     "• Assess for associated cervical spine, esophageal, tracheal, and vascular injuries.\n"
     "• Do not send an unstable patient to CT before airway stabilization."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Oxygen and Airway Preparation[/color]\n"
     "• Provide supplemental oxygen and titrate to maintain adequate oxygenation.\n"
     "• Ensure oxygen delivery, suction, bag-mask ventilation, difficult-airway equipment, and emergency front-of-neck airway equipment are immediately available.\n\n"
     "[color=#1E3A8A]2. Airway Intervention[/color]\n"
     "• Indication: Progressive stridor, respiratory fatigue, severe airway narrowing, rapidly expanding hematoma, or inability to maintain oxygenation.\n"
     "• ENT and anesthesia should plan the airway according to the injury pattern. Maintain spontaneous ventilation when appropriate and avoid repeated traumatic attempts.\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally or by an appropriate non-oral route every 6–8 hours as needed in adults."),
    ("05 — WARNINGS", "danger", 
     "• Normal oxygen saturation does not exclude impending upper-airway obstruction.\n"
     "• Blind intubation or repeated attempts may worsen a disrupted larynx and create a false passage.\n"
     "• Avoid excessive sedation or analgesia that may obscure deterioration in an evolving airway emergency."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected significant laryngeal injury for specialist observation.\n"
     "• ICU or high-dependency care is appropriate for airway compromise, progressive edema, significant structural injury, or an artificial airway.\n"
     "• Discharge only after specialist assessment confirms a low risk of delayed airway deterioration."),
    ("REFERENCES", "info", "ATLS Principles; ENT/Difficult-Airway Management Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Temporal Bone Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Head trauma followed by bleeding from the ear or hemotympanum.\n"
     "• Hearing loss, tinnitus, vertigo, or nystagmus.\n"
     "• Facial nerve weakness.\n"
     "• Clear fluid draining from the ear or nose, suggesting possible cerebrospinal fluid (CSF) leakage.\n"
     "• Battle sign, hemotympanum, or other evidence of skull-base fracture.\n"
     "• Altered mental status, seizures, or focal neurological deficits may indicate associated intracranial injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma priorities and stabilize airway, breathing, and circulation.\n"
     "• Assess Glasgow Coma Scale, pupils, cranial nerves, and facial nerve function.\n"
     "• Protect the cervical spine until injury is excluded according to trauma protocols.\n"
     "• Do not irrigate the ear or insert instruments into a potentially injured canal.\n"
     "• If CSF leakage is suspected, avoid nasal instrumentation and unnecessary ear manipulation.\n"
     "• Obtain urgent trauma and ENT assessment; involve neurosurgery when indicated."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT head according to head injury criteria.\n"
     "• High-resolution CT of the temporal bones when fracture characterization will affect management.\n"
     "• Document facial nerve function as early as possible.\n"
     "• Audiometry when the patient is stable and able to cooperate.\n"
     "• Assess suspected CSF leakage with appropriate laboratory testing (e.g., beta-2 transferrin).\n"
     "• Evaluate for associated vascular injury if indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Initial Trauma Management[/color]\n"
     "• Oxygen and fluid resuscitation according to the patient's physiological needs and trauma protocol.\n"
     "• Monitor neurological status, vital signs, and evidence of ongoing bleeding or deterioration.\n\n"
     "[color=#1E3A8A]2. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally or by an appropriate alternative route every 6–8 hours as needed.\n\n"
     "[color=#1E3A8A]3. Antibiotics[/color]\n"
     "• Do NOT prescribe routine prophylactic antibiotics solely because a temporal bone fracture or CSF leak is suspected. If meningitis, contaminated open injury, or another infection is suspected, initiate the appropriate emergency protocol.\n\n"
     "[color=#1E3A8A]4. Definitive Management[/color]\n"
     "• Most uncomplicated fractures are managed conservatively with observation and follow-up.\n"
     "• Persistent CSF leakage requires specialist management; selected cases may require surgical repair.\n"
     "• Facial nerve paralysis requires early ENT evaluation.\n"
     "• Persistent conductive hearing loss may require later assessment and possible surgery."),
    ("05 — WARNINGS", "danger", 
     "• Avoid hypotension and hypoxia in traumatic brain injury. Do not delay stabilization for detailed ear examination.\n"
     "• Analgesia must not obscure serial neurological assessment.\n"
     "• Routine prophylaxis for a CSF leak is not universally recommended."),
    ("06 — DISPOSITION", "warning", 
     "• Admit according to head injury severity, neurological findings, CSF leakage, facial nerve dysfunction, and associated injuries.\n"
     "• Urgent escalation for deteriorating consciousness, new focal deficits, meningism, worsening vertigo, or progressive facial weakness.\n"
     "• Arrange ENT and audiology follow-up after discharge."),
    ("REFERENCES", "info", "ATLS Principles; NICE Head Injury Guidance; ENT/Skull-Base Trauma Guidance.")
]

ENT_TOPICS[("ENT Emergencies", "Cerebrospinal Fluid Rhinorrhea and Otorrhea")] = [
    ("01 — RECOGNIZE", "info", 
     "Persistent clear, watery nasal or ear drainage after head trauma or skull-base surgery.\n"
     "• Drainage may increase with certain positional changes.\n"
     "• A salty or metallic taste may accompany CSF rhinorrhea.\n"
     "• Associated skull-base fracture, hemotympanum, or neurological injury increases suspicion.\n"
     "• Fever, neck stiffness, severe headache, photophobia, or altered mental status may indicate meningitis.\n\n"
     "[color=#991B1B]CRITICAL POINT:[/color] Clear drainage is not diagnostic by itself. Confirm the diagnosis with appropriate testing where possible."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess trauma severity, neurological status, and signs of meningitis.\n"
     "• Contact ENT and neurosurgery when traumatic or postoperative CSF leakage is suspected.\n"
     "• Avoid nasal packing, nasal instrumentation, and unnecessary manipulation of the ear.\n"
     "• Advise the patient not to blow the nose forcefully or perform Valsalva maneuvers.\n"
     "• Elevate the head if clinically appropriate and not contraindicated by other injuries.\n"
     "• If meningitis is suspected, obtain appropriate cultures promptly when feasible and initiate emergency empiric antimicrobial treatment without unsafe delay."),
    ("03 — INVESTIGATIONS", "info", 
     "• Beta-2 transferrin or beta-trace protein testing of drainage where available.\n"
     "• CT of the skull base and relevant sinuses to identify a bony defect.\n"
     "• MRI or specialized cisternographic imaging when the leak site remains uncertain.\n"
     "• CT head and broader trauma imaging according to the injury mechanism and clinical findings.\n"
     "• If meningitis is suspected, perform blood cultures and the appropriate infection work-up. Lumbar puncture must be considered only after assessing contraindications."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Conservative Measures[/color]\n"
     "• No medication is required solely to stop an uncomplicated CSF leak; management depends on the cause and associated injuries.\n"
     "• Monitor neurological status, fever, meningism, leak volume, and persistence of drainage.\n\n"
     "[color=#1E3A8A]2. Suspected Bacterial Meningitis[/color]\n"
     "• Start the local adult bacterial meningitis regimen immediately when clinically suspected. Common empiric component: ceftriaxone 2 g IV every 12 hours; additional agents (vancomycin, ampicillin) may be required depending on resistance patterns, age, immune status, and local guidelines.\n\n"
     "[color=#1E3A8A]3. Definitive Management[/color]\n"
     "• Many acute traumatic leaks are initially observed under specialist supervision.\n"
     "• Persistent leaks, recurrent meningitis, large defects, or selected high-risk injuries may require endoscopic or open surgical repair.\n"
     "• Antibiotics are used to treat suspected or confirmed infection; routine prophylactic antibiotics for every CSF leak are not universally recommended."),
    ("05 — WARNINGS", "danger", 
     "• Conservative management is not appropriate for every leak. Deterioration, infection, significant skull-base injury, or persistent leakage requires urgent specialist reassessment.\n"
     "• This is not a complete universal meningitis regimen. Do not delay treatment for imaging or lumbar puncture when doing so would be unsafe."),
    ("06 — DISPOSITION", "warning", 
     "• Suspected traumatic or postoperative CSF leakage generally requires urgent specialist assessment.\n"
     "• Admit patients with significant trauma, persistent leakage, neurological abnormalities, fever, or suspected meningitis.\n"
     "• Escalate immediately for altered mental status, seizures, severe headache, neck stiffness, or haemodynamic instability."),
    ("REFERENCES", "info", "NICE Head Injury Guidance; ENT/Neurosurgical Skull-Base Leak Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Parapharyngeal Abscess")] = [
    ("01 — RECOGNIZE", "info", 
     "Fever, severe sore throat, unilateral neck pain, or swelling.\n"
     "• Trismus, dysphagia, odynophagia, or muffled voice.\n"
     "• Medial displacement of the tonsil or lateral pharyngeal wall bulging.\n"
     "• Neck stiffness or painful limitation of movement.\n"
     "• Stridor, drooling, respiratory distress, or inability to handle secretions indicates possible airway compromise.\n"
     "• Sepsis, cranial neuropathy, or swelling along the sternocleidomastoid region may indicate vascular or deep-space extension."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, sepsis, and ability to handle secretions.\n"
     "• Contact ENT and anesthesia urgently if airway compromise is possible.\n"
     "• Keep the patient fasting.\n"
     "• Avoid unnecessary pharyngeal examination or sedation in a patient with a threatened airway.\n"
     "• Establish IV access and start empiric IV antibiotics promptly.\n"
     "• Obtain urgent imaging in a stable patient; do not delay airway stabilization for CT.\n"
     "• Consider associated internal jugular vein thrombosis or mediastinal spread if clinically suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• Contrast-enhanced CT of the neck in a stable patient to identify the abscess and its extent.\n"
     "• CBC, CRP, renal function, electrolytes, and blood cultures if septic or systemically unwell.\n"
     "• Culture material obtained during drainage.\n"
     "• CT of the chest if descending mediastinal infection is suspected.\n"
     "• Additional vascular imaging if internal jugular vein thrombosis or carotid involvement is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Empiric IV Antibiotics — Adults[/color]\n"
     "• Ampicillin-sulbactam 3 g IV every 6 hours (renal adjusted).\n"
     "• Alternative: Piperacillin-tazobactam 4.5 g IV every 6–8 hours (adjust for renal function).\n"
     "• Add Vancomycin if MRSA coverage is indicated (weight-based, therapeutic monitoring).\n\n"
     "[color=#1E3A8A]2. Airway Management[/color]\n"
     "• Prepare suction, oxygen, difficult-airway equipment, and emergency surgical-airway equipment.\n"
     "• Secure the airway early if obstruction is progressing.\n\n"
     "[color=#1E3A8A]3. Definitive Management[/color]\n"
     "• Drainage is often required for a confirmed abscess, especially when large, associated with airway compromise, or not responding to IV antibiotics.\n"
     "• ENT determines the safest drainage approach.\n"
     "• Treat the primary source (tonsillar or dental infection).\n"
     "• Monitor for internal jugular vein thrombosis, carotid complications, sepsis, and descending mediastinitis.\n"
     "• Tailor antibiotics to culture results and clinical response."),
    ("05 — WARNINGS", "danger", 
     "• Broader or alternative coverage may be needed according to local resistance patterns, previous antibiotics, allergy history, or complications.\n"
     "• Sedation or repeated pharyngeal manipulation may precipitate complete obstruction. Do not delay definitive airway management when indicated.\n"
     "• Do not add vancomycin routinely without an indication. Adjust for renal impairment."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected parapharyngeal abscess for IV therapy and specialist assessment.\n"
     "• ICU or high-dependency care is appropriate for airway compromise, severe sepsis, or major complications.\n"
     "• Do not discharge a patient with suspected deep neck-space abscess without an appropriate specialist plan."),
    ("REFERENCES", "info", "ENT Deep Neck Space Infection Guidance; IDSA Antimicrobial Stewardship Guidance; Local Protocols.")
]


# ==================== NEW ENT TOPICS (21-30) ====================

ENT_TOPICS[("ENT Emergencies", "Angioedema Affecting the Upper Airway")] = [
    ("01 — RECOGNIZE", "info", 
     "Rapid swelling of the lips, tongue, floor of mouth, soft palate, or pharynx.\n"
     "• Hoarseness, voice change, dysphagia, drooling, stridor, or respiratory distress.\n"
     "• Urticaria, itching, wheezing, or hypotension suggest histamine-mediated anaphylaxis.\n"
     "• ACE inhibitor use or a history of hereditary angioedema may suggest bradykinin-mediated disease.\n"
     "• [color=#991B1B]Absence of urticaria does not exclude a life-threatening reaction.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and progression of swelling.\n"
     "• Call anesthesia and ENT early if tongue, floor-of-mouth, or laryngeal involvement is suspected.\n"
     "• Give IM epinephrine immediately if anaphylaxis is suspected.\n"
     "• Provide oxygen, monitoring, IV access, and resuscitation as indicated.\n"
     "• Prepare for early expert airway management if voice changes, stridor, progressive tongue swelling, or respiratory distress develops.\n"
     "• Stop a suspected causative drug, such as an ACE inhibitor.\n"
     "• Do not delay airway intervention while waiting for medications to work."),
    ("03 — INVESTIGATIONS", "info", 
     "• Diagnosis is primarily clinical during the emergency.\n"
     "• Check glucose and other investigations according to the patient's condition.\n"
     "• In suspected hereditary or recurrent bradykinin-mediated angioedema, consider C4 and C1-inhibitor testing after stabilization.\n"
     "• Serum tryptase may help support anaphylaxis retrospectively when obtained at an appropriate time, but treatment must not wait for results."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. IM Epinephrine for Suspected Anaphylaxis[/color]\n"
     "• Adult dose: 0.5 mg IM (1 mg/mL preparation) into anterolateral thigh. Repeat after ~5 minutes if airway, breathing, or circulation problems persist.\n"
     "• [color=#991B1B]Do NOT give the 1 mg/mL preparation as an IV bolus for routine anaphylaxis treatment.[/color]\n\n"
     "[color=#1E3A8A]2. IV Crystalloid for Anaphylactic Shock[/color]\n"
     "• Adult initial bolus commonly 500–1,000 mL of isotonic crystalloid, reassessing after each bolus; larger volumes may be required.\n\n"
     "[color=#1E3A8A]3. Antihistamine for Skin Symptoms[/color]\n"
     "• Cetirizine 10 mg orally in a stable adult who can swallow safely. Use only as an adjunct after immediate airway and circulatory threats are addressed.\n"
     "• [color=#991B1B]Antihistamines do NOT treat laryngeal edema or shock and must never delay epinephrine in anaphylaxis.[/color]\n\n"
     "[color=#1E3A8A]4. Corticosteroids[/color]\n"
     "• Steroids are NOT routine first-line treatment for anaphylaxis and do not reliably prevent biphasic reactions. Use only as an adjunct when clinically indicated.\n\n"
     "[color=#1E3A8A]5. Bradykinin-Mediated Angioedema[/color]\n"
     "• For suspected hereditary angioedema, use an approved disease-specific treatment where available (e.g., C1-inhibitor concentrate or icatibant) according to local protocol.\n"
     "• [color=#991B1B]Epinephrine, antihistamines, and steroids may have little or no effect in bradykinin-mediated angioedema. Airway management remains the priority.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Secure the airway early if swelling is progressive or laryngeal involvement is suspected.\n"
     "• Discontinue the causative ACE inhibitor permanently when implicated.\n"
     "• Arrange allergy/immunology evaluation for recurrent or unexplained attacks.\n"
     "• Provide an anaphylaxis action plan and appropriate auto-injector prescription when indicated.\n"
     "• Refer suspected hereditary angioedema for specialist confirmation and prevention planning."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with tongue, pharyngeal, or laryngeal involvement or any airway symptoms.\n"
     "• ICU or high-dependency care may be required for progressive edema or an artificial airway.\n"
     "• Discharge only after appropriate observation and resolution of risk, with clear return precautions and follow-up."),
    ("REFERENCES", "info", "World Allergy Organization Anaphylaxis Guidance; Resuscitation Council UK Anaphylaxis Guidance; Hereditary Angioedema Specialist Guidance.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Laryngeal Edema and Stridor")] = [
    ("01 — RECOGNIZE", "info", 
     "Inspiratory stridor, hoarseness, voice change, or a barking cough.\n"
     "• Increased work of breathing, suprasternal retractions, or difficulty speaking.\n"
     "• Drooling or inability to swallow secretions.\n"
     "• Causes include anaphylaxis, infection, thermal or chemical injury, post-extubation edema, and laryngeal trauma.\n"
     "• [color=#991B1B]Agitation, exhaustion, reduced air entry, cyanosis, or altered mental status are signs of impending respiratory failure.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and the severity of obstruction.\n"
     "• Call anesthesia and ENT urgently for severe or progressive symptoms.\n"
     "• Keep the patient in the position of comfort; avoid unnecessary agitation.\n"
     "• Provide oxygen and continuous monitoring.\n"
     "• Prepare difficult-airway equipment and emergency front-of-neck access equipment.\n"
     "• Treat the cause immediately, such as IM epinephrine for anaphylaxis.\n"
     "• Do not delay airway stabilization for imaging or diagnostic procedures in an unstable patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical assessment is primary in a threatened airway.\n"
     "• Flexible nasolaryngoscopy may be useful in a stable patient when performed by a trained clinician.\n"
     "• Blood gas testing may help assess respiratory failure but must not delay treatment.\n"
     "• Imaging is considered only when the airway is stable and the result will affect management.\n"
     "• Investigate the underlying cause after stabilization."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Oxygen and Monitoring[/color]\n"
     "• Titrate oxygen to clinical need and oxygenation target; use high-concentration oxygen during severe respiratory compromise.\n"
     "• Monitor respiratory effort, stridor, mental status, heart rate, and oxygen saturation continuously.\n"
     "• [color=#991B1B]A normal oxygen saturation early in the course does not exclude critical upper-airway obstruction.[/color]\n\n"
     "[color=#1E3A8A]2. Nebulized Epinephrine for Selected Upper-Airway Edema[/color]\n"
     "• For selected cases of significant upper-airway edema: epinephrine 5 mg nebulized (using appropriate 1 mg/mL solution) under local emergency protocol.\n"
     "• [color=#991B1B]Nebulized epinephrine is a temporizing measure, not a substitute for definitive airway management. If anaphylaxis is suspected, give IM epinephrine as first-line treatment.[/color]\n\n"
     "[color=#1E3A8A]3. Corticosteroids for Selected Inflammatory or Post-Extubation Edema[/color]\n"
     "• Dose and agent depend on cause and local protocol; steroids are not a universal treatment for all causes of stridor. Do not rely on them to rescue a patient with impending airway obstruction."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Secure the airway with an expert-led plan if obstruction is severe or progressive.\n"
     "• Use cause-specific treatment for anaphylaxis, infection, trauma, or post-extubation edema.\n"
     "• Consider heliox only as a temporary adjunct in selected settings; it does not correct a critically narrowed airway.\n"
     "• Reassess after treatment because edema may recur or progress."),
    ("06 — DISPOSITION", "warning", 
     "• Admit any patient with persistent stridor, significant laryngeal edema, or a need for nebulized epinephrine and close observation.\n"
     "• ICU care is indicated for respiratory failure, progressive obstruction, or a secured airway requiring intensive monitoring.\n"
     "• Discharge only after specialist assessment confirms that the airway is stable and the underlying cause has been addressed."),
    ("REFERENCES", "info", "Difficult Airway Society Emergency Airway Guidance; Resuscitation Council UK Anaphylaxis Guidance; Local ENT/Anesthesia Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Esophageal Food Bolus Impaction")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden dysphagia during a meal, often involving meat or another solid food.\n"
     "• Sensation of food stuck in the throat or chest.\n"
     "• Regurgitation, drooling, or inability to swallow saliva.\n"
     "• Complete obstruction is suggested by inability to handle secretions.\n"
     "• Stridor, choking, or respiratory distress suggests possible airway involvement or aspiration."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, and ability to manage secretions.\n"
     "• Keep the patient fasting.\n"
     "• Obtain urgent gastroenterology or endoscopy consultation.\n"
     "• Arrange emergent endoscopy when the patient cannot handle secretions or has complete obstruction.\n"
     "• Do not induce vomiting or blindly push the bolus down.\n"
     "• Avoid giving oral food, drink, or tablets to a patient with complete obstruction.\n"
     "• Consider airway protection when aspiration risk is high."),
    ("03 — INVESTIGATIONS", "info", 
     "• Diagnosis is often clinical.\n"
     "• Plain radiographs may help when a radiopaque foreign body or perforation is suspected, but a normal radiograph does not exclude food impaction.\n"
     "• CT is appropriate if perforation, a sharp object, or another complication is suspected.\n"
     "• Endoscopy is both diagnostic and therapeutic.\n"
     "• After resolution, assess for underlying esophageal disease (stricture, Schatzki ring, eosinophilic esophagitis)."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Endoscopic Removal[/color]\n"
     "• Indication: Complete obstruction, inability to handle secretions, or persistent impaction.\n"
     "• Perform urgent endoscopic removal or advancement under direct visualization according to specialist judgment.\n"
     "• [color=#991B1B]Do NOT delay emergency endoscopy in complete obstruction to try medications or imaging.[/color]\n\n"
     "[color=#1E3A8A]2. Glucagon — Selected Cases Only[/color]\n"
     "• Some protocols use glucagon 1 mg IV once in a stable patient while endoscopy is being arranged.\n"
     "• [color=#991B1B]Evidence of benefit is limited. Avoid relying on glucagon in complete obstruction, and use caution because it can cause nausea and vomiting, increasing aspiration risk.[/color]\n\n"
     "[color=#1E3A8A]3. Acid Suppression After Assessment[/color]\n"
     "• A proton pump inhibitor may be prescribed when reflux or esophagitis is suspected after the obstruction is resolved.\n"
     "• [color=#991B1B]Acid suppression does not remove an impacted bolus and must not delay endoscopy.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Remove or safely advance the bolus endoscopically.\n"
     "• Assess for mucosal injury and perforation.\n"
     "• Arrange investigation of underlying esophageal disease, including biopsies for eosinophilic esophagitis when appropriate.\n"
     "• Provide dietary advice and follow-up according to the identified cause."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or observe patients with complete obstruction, aspiration, significant mucosal injury, or suspected perforation.\n"
     "• Discharge may be appropriate after successful resolution if the patient can swallow safely and there is no complication.\n"
     "• Return immediately for chest or neck pain, fever, dyspnea, or inability to swallow."),
    ("REFERENCES", "info", "ASGE Management of Ingested Foreign Bodies and Food Impactions; ESGE Foreign Body and Food Bolus Management Guidance; Local Emergency Endoscopy Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Caustic Injury of the Upper Aerodigestive Tract")] = [
    ("01 — RECOGNIZE", "info", 
     "History of ingestion or exposure to acids, alkalis, or corrosive household or industrial products.\n"
     "• Oral burns, drooling, dysphagia, odynophagia, vomiting, or chest/abdominal pain.\n"
     "• Hoarseness, stridor, respiratory distress, or neck swelling may indicate airway injury.\n"
     "• [color=#991B1B]Severe injury may occur even without obvious oral burns.[/color]\n"
     "• Hematemesis, severe pain, shock, or signs of perforation suggest a complicated injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and the nature and timing of exposure.\n"
     "• Contact poison control or a toxicology service where available, along with ENT and gastroenterology.\n"
     "• Give oxygen and prepare for early expert airway management if edema or respiratory symptoms are progressing.\n"
     "• Keep the patient fasting.\n"
     "• Remove contaminated clothing and irrigate exposed skin or eyes with copious water when relevant.\n"
     "• Do NOT induce vomiting.\n"
     "• Do NOT attempt chemical neutralization with another substance.\n"
     "• Do NOT administer activated charcoal routinely for corrosive ingestion.\n"
     "• Do NOT force oral fluids in a patient with dysphagia, drooling, or possible airway injury."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, blood gas, lactate, and other tests guided by severity.\n"
     "• Chest and abdominal imaging when perforation or thoracic complications are suspected.\n"
     "• CT of the neck or chest may be indicated in severe cases or when deep injury is suspected.\n"
     "• Endoscopy is commonly considered within the first 12–24 hours in patients with significant ingestion, according to specialist assessment and local protocols.\n"
     "• Avoid endoscopy when suspected perforation or instability makes it unsafe until the specialist team determines the appropriate approach."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Airway Support[/color]\n"
     "• Oxygen according to the patient's respiratory status and oxygenation target.\n"
     "• Prepare suction, difficult-airway equipment, and emergency surgical-airway equipment.\n"
     "• [color=#991B1B]Progressive edema may make later intubation difficult. Seek early expert assistance; do not delay a necessary airway intervention.[/color]\n\n"
     "[color=#1E3A8A]2. IV Fluids[/color]\n"
     "• Use isotonic crystalloid according to haemodynamic status; in shock, administer reassessed boluses according to the adult resuscitation protocol.\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Select analgesia according to severity, haemodynamic status, and organ function; paracetamol may be appropriate in selected stable patients.\n"
     "• [color=#991B1B]Avoid oral medications in patients unable to swallow safely. Avoid masking worsening pain without reassessment.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Consult ENT and gastroenterology early for suspected significant injury.\n"
     "• Manage airway injury and esophageal or gastric injury according to specialist assessment.\n"
     "• Surgery may be required for perforation, necrosis, or severe transmural injury.\n"
     "• Steroids and prophylactic antibiotics are NOT routine for every caustic ingestion; use only for a specific indication.\n"
     "• Arrange nutritional support and follow-up for strictures or delayed complications."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with airway symptoms, significant ingestion, persistent vomiting, severe pain, abnormal investigations, or suspected deep injury.\n"
     "• ICU care may be needed for airway compromise, shock, or major tissue injury.\n"
     "• Discharge only after specialist assessment establishes low risk and a safe follow-up plan."),
    ("REFERENCES", "info", "WSES Esophageal Emergencies Guidance; AACT/Poison-Control Guidance; Local Toxicology/ENT/Gastroenterology Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Facial Nerve Injury in ENT Emergencies")] = [
    ("01 — RECOGNIZE", "info", 
     "New unilateral facial weakness involving the forehead, eye closure, and mouth.\n"
     "• Facial weakness following temporal bone trauma, otitis media, mastoiditis, or ear surgery.\n"
     "• Associated hearing loss, vertigo, otorrhea, or severe ear pain.\n"
     "• Vesicles around the ear or in the external auditory canal may suggest Ramsay Hunt syndrome.\n"
     "• [color=#991B1B]Forehead sparing, limb weakness, speech disturbance, or other focal neurological findings may indicate a central lesion such as stroke.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Establish the time of onset and assess for stroke symptoms.\n"
     "• Activate the local stroke pathway when stroke is suspected; do not assume every facial palsy is peripheral.\n"
     "• Assess airway and swallowing if multiple cranial nerves are involved.\n"
     "• Examine the ear and document facial nerve function.\n"
     "• In traumatic cases, follow head injury and cervical spine protocols.\n"
     "• Protect the cornea immediately if eye closure is incomplete.\n"
     "• Obtain urgent ENT review for facial weakness associated with trauma, invasive infection, or other otologic disease."),
    ("03 — INVESTIGATIONS", "info", 
     "• Full neurological examination, including forehead movement, eye closure, and lower facial movement.\n"
     "• CT head and/or temporal bone imaging when trauma or structural injury is suspected.\n"
     "• MRI when central pathology, tumor, or selected inflammatory disease is suspected.\n"
     "• Otoscopy and hearing assessment.\n"
     "• Glucose testing and other investigations guided by the suspected cause.\n"
     "• Electrodiagnostic testing may be considered by specialists in selected severe traumatic cases."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Corneal Protection[/color]\n"
     "• Use preservative-free lubricating eye drops frequently while awake; use lubricating eye ointment at night when needed.\n"
     "• Ensure the eye remains lubricated and closes safely; consider gentle eyelid taping at night when appropriate.\n"
     "• [color=#991B1B]Incomplete eye closure can cause corneal abrasion and vision loss. Arrange urgent ophthalmology review for eye pain, redness, photophobia, or visual changes.[/color]\n\n"
     "[color=#1E3A8A]2. Corticosteroids for Eligible Acute Bell's Palsy[/color]\n"
     "• For adults with clinically diagnosed Bell's palsy: prednisolone 50–60 mg orally once daily for 5 days, then taper over next 5 days, per local guidance. Start early, ideally within 72 hours of onset.\n"
     "• [color=#991B1B]This regimen is for selected Bell's palsy cases, not a universal treatment for facial weakness caused by trauma, stroke, or invasive ear infection. Exclude serious alternative causes.[/color]\n\n"
     "[color=#1E3A8A]3. Antiviral Therapy in Selected Cases[/color]\n"
     "• Antivirals may be considered with corticosteroids in severe Bell's palsy or suspected Ramsay Hunt syndrome; drug selection and dosing follow local protocol and renal function.\n"
     "• [color=#991B1B]Antivirals are not a substitute for corticosteroids in eligible Bell's palsy and should not delay urgent evaluation of other causes.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat the underlying cause, including trauma, otologic infection, or herpes zoster when diagnosed.\n"
     "• Facial palsy after temporal bone trauma requires urgent specialist assessment; management depends on onset, severity, imaging, and nerve function.\n"
     "• Arrange eye care and facial nerve follow-up.\n"
     "• Consider facial rehabilitation for persistent weakness.\n"
     "• Reassess patients with progressive weakness, recurrent palsy, bilateral symptoms, or failure to improve."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or urgently refer patients with traumatic facial palsy, multiple cranial neuropathies, suspected invasive infection, or associated neurological deficits.\n"
     "• Activate emergency stroke care when central neurological signs are present.\n"
     "• Stable isolated Bell's palsy may be managed as an outpatient after appropriate assessment, eye protection, and follow-up."),
    ("REFERENCES", "info", "AAO-HNS Bell's Palsy Clinical Practice Guideline; NICE Stroke/TIA Guidance; ENT/Temporal Bone Trauma Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Otitis Media with Intracranial Complications")] = [
    ("01 — RECOGNIZE", "info", 
     "Ear pain, fever, reduced hearing, and a bulging tympanic membrane may indicate acute otitis media.\n"
     "• Severe or persistent headache, neck stiffness, photophobia, altered mental status, or seizures may indicate meningitis.\n"
     "• Persistent fever, vomiting, focal neurological deficits, or reduced consciousness may indicate intracranial abscess.\n"
     "• Postauricular swelling, erythema, tenderness, or protrusion of the pinna suggests mastoiditis.\n"
     "• Papilledema, diplopia, or worsening headache may indicate raised intracranial pressure or venous sinus thrombosis.\n"
     "• Clinical deterioration despite antibiotics raises concern for an invasive complication."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, neurological status, and sepsis.\n"
     "• Obtain urgent ENT and appropriate infectious diseases or neurosurgical consultation.\n"
     "• Establish IV access and obtain blood cultures when feasible without delaying treatment.\n"
     "• Start emergency IV antibiotics when meningitis, intracranial abscess, or another serious bacterial complication is suspected.\n"
     "• Perform urgent neuroimaging when indicated; stabilize the patient first if unstable.\n"
     "• Keep the patient fasting if surgery or drainage may be required.\n"
     "• Do NOT perform lumbar puncture when contraindicated, including suspected mass effect or significant raised intracranial pressure."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, CRP, renal function, electrolytes, glucose, and blood cultures when systemically unwell.\n"
     "• Contrast-enhanced CT of the temporal bones and relevant intracranial structures.\n"
     "• MRI brain with contrast when intracranial abscess, venous sinus thrombosis, or other intracranial extension is suspected.\n"
     "• CT or MR venography if venous sinus thrombosis is suspected.\n"
     "• Ear examination and culture of discharge when useful.\n"
     "• Lumbar puncture only if meningitis is suspected, it is clinically indicated, and there are no contraindications."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Empiric IV Antibiotics for Suspected Bacterial Meningitis[/color]\n"
     "• Common adult component: ceftriaxone 2 g IV every 12 hours. Additional agents (vancomycin, ampicillin) may be required according to local resistance patterns, age, immune status, and suspected source.\n"
     "• [color=#991B1B]This is not a complete universal regimen. Suspected meningitis or intracranial infection requires immediate clinician-directed treatment; do not delay for imaging or lumbar puncture when unsafe.[/color]\n\n"
     "[color=#1E3A8A]2. Additional Anaerobic Coverage[/color]\n"
     "• Metronidazole 500 mg IV every 8 hours may be used when anaerobic coverage is indicated (e.g., selected intracranial abscess regimens).\n"
     "• [color=#991B1B]Antibiotic combinations depend on suspected pathogen, intracranial complication, and local protocol. Do not use metronidazole automatically for every case of otitis media.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia and Supportive Care[/color]\n"
     "• Paracetamol 500–1,000 mg orally or by appropriate alternative route every 6–8 hours as needed.\n"
     "• [color=#991B1B]Analgesia must not obscure clinical deterioration or delay definitive treatment.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• ENT may perform myringotomy or tympanostomy when indicated for drainage and microbiological sampling.\n"
     "• Mastoidectomy may be necessary for coalescent mastoiditis or failure of appropriate treatment.\n"
     "• Intracranial abscess may require neurosurgical drainage.\n"
     "• Manage venous sinus thrombosis with specialist input; anticoagulation decisions must be individualized.\n"
     "• Narrow antibiotic therapy according to cultures, imaging, and clinical response."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected intracranial complications.\n"
     "• ICU care may be required for shock, reduced consciousness, seizures, or respiratory compromise.\n"
     "• Arrange ENT and infectious diseases follow-up after stabilization."),
    ("REFERENCES", "info", "NICE Otitis Media and Related Infection Guidance; ENT Guidance on Acute Mastoiditis/Intracranial Complications; Local Meningitis/Sepsis Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Complications of Tracheostomy")] = [
    ("01 — RECOGNIZE", "info", 
     "Respiratory distress, desaturation, increased work of breathing, or inability to pass a suction catheter.\n"
     "• A blocked tube may present with reduced airflow, high airway pressures, or ineffective ventilation.\n"
     "• Displacement or accidental decannulation may cause rapid respiratory deterioration.\n"
     "• Bleeding may be minor or may indicate a life-threatening tracheo-innominate artery fistula.\n"
     "• Subcutaneous emphysema, neck swelling, or surgical emphysema may suggest false passage or airway injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call for help immediately and identify whether the patient has a tracheostomy or a total laryngectomy.\n"
     "• Give oxygen to the face and the stoma as appropriate while assessing the patient's anatomy and airflow.\n"
     "• Remove any speaking valve or cap.\n"
     "• Remove the inner cannula if present and assess whether airflow improves.\n"
     "• Attempt suction only if appropriate and do not force a catheter through resistance.\n"
     "• If the tube is blocked or displaced, follow the local emergency tracheostomy algorithm.\n"
     "• If the patient is deteriorating and ventilation through the tube is ineffective, trained clinicians may need to remove the tube and provide oxygenation through the appropriate route.\n"
     "• For a total laryngectomy, the stoma is the only route to the lungs; face-mask ventilation will not oxygenate the patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical assessment and immediate response to airway maneuvers take priority.\n"
     "• Check oxygen saturation, ECG, capnography when available, and respiratory effort.\n"
     "• Obtain blood gas analysis if respiratory failure is suspected and this will not delay stabilization.\n"
     "• Chest radiography or bronchoscopy may be needed after stabilization to assess tube position, obstruction, or complications.\n"
     "• Investigate significant bleeding urgently with ENT and surgical teams."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Blocked Tracheostomy Tube[/color]\n"
     "• Remove inner cannula if present, assess airflow, and follow emergency tracheostomy algorithm.\n"
     "• Ensure suction, oxygen, bag-mask equipment, spare tracheostomy tubes (same size and one size smaller), and emergency airway equipment are available.\n"
     "• [color=#991B1B]Do not repeatedly force a suction catheter or ventilation through a suspected blocked or displaced tube.[/color]\n\n"
     "[color=#1E3A8A]2. Displaced or Accidentally Removed Tracheostomy Tube[/color]\n"
     "• Call ENT and anesthesia immediately. Management depends on whether the stoma is mature and whether the upper airway is patent.\n"
     "• [color=#991B1B]Blind reinsertion into an immature or difficult stoma can create a false passage and cause fatal airway obstruction. Do not delay oxygenation while attempting repeated replacement.[/color]\n\n"
     "[color=#1E3A8A]3. Significant Bleeding or Suspected Tracheo-Innominate Fistula[/color]\n"
     "• Treat brisk or pulsatile bleeding as a life-threatening emergency. Call ENT, anesthesia, and surgical team immediately.\n"
     "• [color=#991B1B]A small sentinel bleed may precede catastrophic hemorrhage. Do not dismiss new tracheostomy bleeding as minor without urgent assessment.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Correct tube position or replace the tube under appropriate conditions.\n"
     "• Treat the underlying cause (mucus plugging, infection, airway narrowing).\n"
     "• Arrange bronchoscopy or surgical assessment when indicated.\n"
     "• Investigate significant bleeding urgently for vascular injury.\n"
     "• Review humidification, suctioning, tube care, and emergency equipment after stabilization."),
    ("06 — DISPOSITION", "warning", 
     "• Any significant obstruction, displacement, respiratory compromise, or bleeding requires urgent specialist assessment.\n"
     "• Admit patients with unresolved complications or a need for airway intervention.\n"
     "• Ensure caregivers and staff have appropriate training and an emergency tracheostomy plan."),
    ("REFERENCES", "info", "National Tracheostomy Safety Project Emergency Algorithms; Difficult Airway Society Guidance; Local Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Spontaneous or Traumatic Ear Bleeding")] = [
    ("01 — RECOGNIZE", "info", 
     "Blood in the external auditory canal or bleeding from the ear.\n"
     "• Causes include canal trauma, foreign body injury, tympanic membrane perforation, infection, and temporal bone fracture.\n"
     "• Ear bleeding after significant head trauma may indicate a skull-base or temporal bone injury.\n"
     "• Associated hearing loss, vertigo, facial weakness, clear fluid leakage, or neurological deficits increases concern for serious injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and neurological status if trauma is possible.\n"
     "• Control external bleeding gently without inserting material deeply into the ear canal.\n"
     "• Do NOT irrigate the ear or perform blind instrumentation.\n"
     "• Avoid ear drops when tympanic membrane perforation is suspected unless directed by an appropriate clinician.\n"
     "• Obtain urgent ENT assessment for significant bleeding, hearing loss, vertigo, facial weakness, or suspected skull fracture.\n"
     "• Follow the local head injury pathway after significant trauma."),
    ("03 — INVESTIGATIONS", "info", 
     "• Otoscopy when safe and appropriate.\n"
     "• Neurological examination and assessment of facial nerve function.\n"
     "• CT head and temporal bone imaging according to trauma severity and suspected fracture.\n"
     "• Audiometry when the patient is stable and hearing symptoms persist.\n"
     "• Consider investigation for a coagulation disorder or medication-related bleeding when clinically indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Minor External Canal Injury[/color]\n"
     "• Apply gentle external pressure only where safe and visible; do not pack the canal blindly.\n"
     "• [color=#991B1B]Deep packing or blind instrumentation may worsen injury or damage the tympanic membrane.[/color]\n\n"
     "[color=#1E3A8A]2. Suspected Temporal Bone Fracture[/color]\n"
     "• Follow trauma resuscitation and arrange urgent ENT and trauma assessment.\n"
     "• [color=#991B1B]Do not irrigate or manipulate the ear in suspected skull-base injury.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally or by appropriate alternative route every 6–8 hours as needed.\n"
     "• [color=#991B1B]Avoid delaying investigation of significant trauma or neurological symptoms while treating pain.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat the source of bleeding.\n"
     "• Manage tympanic membrane perforation, canal laceration, infection, or temporal bone fracture according to ENT findings.\n"
     "• Consider specialist-selected topical treatment if infection or canal injury requires it.\n"
     "• Arrange hearing assessment when hearing loss or persistent symptoms are present."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate evaluation for bleeding after significant head trauma, facial nerve weakness, vertigo, CSF leakage, or significant hearing loss.\n"
     "• Minor superficial injuries may be managed as an outpatient after examination confirms no serious injury.\n"
     "• Return urgently for recurrent bleeding, worsening pain, fever, dizziness, or new neurological symptoms."),
    ("REFERENCES", "info", "NICE Head Injury Guidance; ENT Guidance on External Auditory Canal/Tympanic Membrane Injury; Local Trauma Protocols.")
]

ENT_TOPICS[("ENT Emergencies", "Acute Vertigo with Neurological Red Flags")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden-onset vertigo, imbalance, nausea, vomiting, or difficulty walking.\n"
     "• Central warning signs: diplopia, dysarthria, dysphagia, limb weakness, sensory loss, severe truncal ataxia, or new cranial nerve deficits.\n"
     "• New severe headache or neck pain may indicate posterior circulation stroke or arterial dissection.\n"
     "• Sudden hearing loss with acute vestibular symptoms may indicate an inner-ear disorder or a vascular event.\n"
     "• Continuous acute vestibular symptoms in a patient with vascular risk factors require careful assessment.\n"
     "• [color=#991B1B]CRITICAL POINT: Posterior circulation stroke may present predominantly with vertigo and imbalance, even without obvious limb weakness.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, glucose, and neurological status.\n"
     "• Establish the exact onset or last-known-well time.\n"
     "• Activate the local stroke pathway when stroke is suspected.\n"
     "• Do not assume symptoms are benign because the patient is young or has no obvious limb weakness.\n"
     "• Avoid walking an unstable patient without assistance.\n"
     "• Use HINTS examination only in the appropriate patient with an acute vestibular syndrome and only when performed by a trained clinician.\n"
     "• Do not use a reassuring or incomplete HINTS examination to rule out stroke when examiner expertise is lacking."),
    ("03 — INVESTIGATIONS", "info", 
     "• Full neurological examination, including eye movements, cranial nerves, coordination, gait when safe, and hearing.\n"
     "• Point-of-care glucose.\n"
     "• Brain imaging according to stroke pathway; MRI with DWI is more sensitive than non-contrast CT for many posterior fossa infarctions.\n"
     "• CT angiography or MR angiography when vertebrobasilar occlusion or arterial dissection is suspected.\n"
     "• ECG and laboratory investigations according to suspected cause.\n"
     "• [color=#991B1B]A normal early CT does not reliably exclude posterior circulation ischemic stroke.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Suspected Posterior Circulation Stroke[/color]\n"
     "• Activate stroke team and arrange urgent imaging and reperfusion eligibility assessment.\n"
     "• [color=#991B1B]Do not delay stroke evaluation to administer vestibular suppressants or antiemetics. Thrombolysis or thrombectomy eligibility must be determined by the stroke team.[/color]\n\n"
     "[color=#1E3A8A]2. Antiemetic for Severe Nausea or Vomiting[/color]\n"
     "• Ondansetron 4 mg orally, orally disintegrating, or IV as appropriate; repeat dosing per local protocol.\n"
     "• [color=#991B1B]Review QT-prolonging drugs, electrolyte abnormalities, and significant cardiac risk. Antiemetics do not treat stroke or establish the cause of vertigo.[/color]\n\n"
     "[color=#1E3A8A]3. Short-Term Vestibular Symptom Relief[/color]\n"
     "• Medication choice depends on cause and comorbidities; routine prolonged vestibular suppressant treatment is not recommended for every case.\n"
     "• [color=#991B1B]Sedation can worsen falls and obscure neurological reassessment. Do not let symptom relief delay stroke evaluation.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat confirmed stroke according to stroke pathway.\n"
     "• Peripheral vestibular disorders require cause-specific management (e.g., repositioning maneuvers for confirmed BPPV).\n"
     "• Consider urgent ENT or audiology assessment for sudden sensorineural hearing loss accompanying vertigo.\n"
     "• Provide vestibular rehabilitation when appropriate.\n"
     "• Reassess patients with persistent, progressive, or atypical symptoms."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or manage through stroke pathway when central pathology is suspected.\n"
     "• Do not discharge a patient with new neurological deficits, inability to walk safely, or unexplained acute vestibular syndrome without adequate evaluation.\n"
     "• Outpatient care may be appropriate for a confidently diagnosed benign peripheral disorder with no red flags and safe mobility."),
    ("REFERENCES", "info", "AHA/ASA Acute Ischemic Stroke Guidance; NICE Stroke/TIA Guidance; GRACE-3 Guideline for Acute Dizziness/Vertigo.")
]

ENT_TOPICS[("ENT Emergencies", "Severe Epistaxis Refractory to Initial Treatment")] = [
    ("01 — RECOGNIZE", "info", 
     "Persistent nasal bleeding despite correct compression and initial treatment.\n"
     "• Suspected posterior bleeding, especially with blood in the oropharynx and no visible anterior source.\n"
     "• Haemodynamic instability, syncope, tachycardia, hypotension, or signs of significant blood loss.\n"
     "• Anticoagulant or antiplatelet use, coagulopathy, or significant comorbid disease.\n"
     "• Airway compromise from heavy bleeding or aspiration."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and haemodynamic stability.\n"
     "• Sit the patient forward if conscious and appropriate; instruct them to spit out blood rather than swallow it.\n"
     "• Apply firm continuous compression to the soft part of the nose for 10–15 minutes without repeatedly releasing pressure to check.\n"
     "• Use suction when needed to clear blood and allow safe assessment.\n"
     "• Establish IV access and obtain blood tests when bleeding is severe or the patient is unstable.\n"
     "• Call ENT urgently for persistent bleeding, suspected posterior epistaxis, or failed initial treatment.\n"
     "• Protect the airway if bleeding is massive or the patient cannot handle secretions.\n"
     "• Do not delay resuscitation for local procedures in an unstable patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC and platelet count in significant or recurrent bleeding.\n"
     "• Coagulation studies when anticoagulant use, liver disease, or a bleeding disorder is suspected.\n"
     "• Group and screen or crossmatch if substantial blood loss or transfusion is possible.\n"
     "• Review anticoagulants, antiplatelets, hypertension, trauma, and other contributing factors.\n"
     "• Imaging is not routinely required for uncomplicated epistaxis but may be indicated when a tumor, vascular lesion, or trauma is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Topical Vasoconstrictor[/color]\n"
     "• A locally approved topical oxymetazoline preparation may be used according to its product instructions and local epistaxis protocol.\n"
     "• [color=#991B1B]Avoid excessive or repeated use. Consider cardiovascular contraindications and local guidance.[/color]\n\n"
     "[color=#1E3A8A]2. Topical Tranexamic Acid[/color]\n"
     "• Some emergency protocols use topical tranexamic acid, commonly 500 mg in 5 mL applied to the bleeding site using an appropriate delivery method.\n"
     "• [color=#991B1B]Evidence and practice vary. Topical tranexamic acid must not delay packing, airway management, or definitive ENT treatment when required.[/color]\n\n"
     "[color=#1E3A8A]3. Nasal Packing[/color]\n"
     "• Indication: Persistent bleeding when a source cannot be controlled with initial measures, or when directed by the treating clinician.\n"
     "• [color=#991B1B]Posterior packing can cause significant discomfort, hypoxia, and other complications; it generally requires admission and specialist oversight. Do not blindly pack a suspected major facial or skull-base injury.[/color]\n\n"
     "[color=#1E3A8A]4. Resuscitation for Significant Blood Loss[/color]\n"
     "• Use isotonic crystalloid as an initial bridge when indicated, with blood products for major haemorrhage according to the local protocol.\n"
     "• [color=#991B1B]Crystalloid alone is inadequate for uncontrolled major haemorrhage. Prioritize definitive bleeding control and appropriate blood-product resuscitation.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• ENT may perform endoscopic cautery or surgical arterial control.\n"
     "• Endovascular embolization may be considered when bleeding persists or surgery is unsuitable.\n"
     "• Correct reversible coagulopathy when clinically indicated.\n"
     "• Review antithrombotic therapy individually; do not automatically discontinue essential anticoagulants without considering thrombotic risk.\n"
     "• Identify and treat an underlying cause, including trauma, vascular lesions, or neoplasia when suspected."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with posterior packing, significant blood loss, haemodynamic instability, or ongoing bleeding.\n"
     "• Escalate to ICU or a high-dependency setting when airway protection, major transfusion, or close haemodynamic monitoring is needed.\n"
     "• Discharge only when bleeding is controlled, the patient is stable, and follow-up and return precautions are clear."),
    ("REFERENCES", "info", "AAO-HNS Nosebleed (Epistaxis) Clinical Practice Guideline; NICE Blood Transfusion/Emergency Bleeding Guidance; Local ENT/Major Haemorrhage Protocols.")
]