# data_orthopedics.py

ORTHOPEDICS_DATA = {
    "Orthopedic Emergencies": {
        "Trauma & General Fractures": [
            "Open Fracture",
            "Traumatic Amputation",
            "Crush Syndrome",
            "General Safety Checklist"
        ],
        "Upper Limb Injuries": [
            "Supracondylar Humerus Fracture in Children",
            "Pediatric Forearm Fracture with Neurovascular Compromise",
            "Humeral Shaft Fracture with Radial Nerve Injury",
            "Clavicle Fracture with Skin or Neurovascular Compromise",
            "Monteggia Fracture-Dislocation",
            "Galeazzi Fracture-Dislocation",
            "Elbow Dislocation",
            "Shoulder Dislocation with Neurovascular Risk",
            "Acute Rotator Cuff Tear After Trauma"
        ],
        "Wrist & Hand Injuries": [
            "Scaphoid Fracture",
            "Distal Radius Fracture with Neurovascular Compromise",
            "Perilunate Dislocation",
            "Acute Hand Compartment Syndrome"
        ],
        "Lower Limb Injuries": [
            "Femoral Shaft Fracture",
            "Femoral Neck Fracture",
            "Hip Dislocation",
            "Hip Dislocation with Associated Fracture",
            "Pelvic Fracture with Hemorrhage",
            "Knee Dislocation and Popliteal Artery Injury",
            "Tibial Plateau Fracture",
            "Patellar Fracture and Extensor Mechanism Disruption",
            "Acute Knee Extensor Mechanism Rupture",
            "Ankle Fracture-Dislocation",
            "Calcaneal Fracture",
            "Achilles Tendon Rupture",
            "Acute Achilles Tendon Avulsion or Insertional Rupture"
        ],
        "Spine Injuries": [
            "Cervical Spine Fracture and Dislocation",
            "Thoracolumbar Spine Fracture",
            "Acute Spinal Cord Injury",
            "Cauda Equina Syndrome",
            "Acute Cauda Equina Syndrome",
            "Acute Osteoporotic Vertebral Compression Fracture"
        ],
        "Vascular & Compartment Emergencies": [
            "Acute Compartment Syndrome",
            "Acute Limb Ischemia"
        ],
        "Orthopedic Infections": [
            "Septic Arthritis",
            "Acute Hematogenous Osteomyelitis",
            "Acute Septic Bursitis"
        ]
    }
}

ORTHOPEDICS_TOPICS = {}

# ==================== ORIGINAL TOPICS (1-11) ====================

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Compartment Syndrome")] = [
    ("01 — RECOGNITION", "info", 
     "Acute compartment syndrome (ACS) is a surgical emergency caused by increased pressure within a closed fascial compartment, compromising tissue perfusion and potentially causing irreversible muscle and nerve necrosis.\n\n"
     "[color=#1E3A8A]Common causes:[/color]\n"
     "• Tibial shaft fractures and forearm fractures.\n"
     "• Crush injuries, reperfusion after ischemia, and major soft-tissue trauma.\n"
     "• Tight casts, dressings, or circumferential burns.\n"
     "• Bleeding in patients receiving anticoagulants."),
    ("02 — CLINICAL FEATURES", "info", 
     "• Severe pain disproportionate to the injury.\n"
     "• Pain on passive stretch of muscles within the affected compartment.\n"
     "• Tense swelling and increasing analgesic requirements.\n"
     "• Paresthesia, reduced sensation, or weakness are concerning later findings.\n\n"
     "[color=#991B1B]IMPORTANT: Normal distal pulses do not exclude compartment syndrome. Pallor, paralysis, and pulselessness are late signs.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Call orthopedics immediately; notify anesthesia and the operating theatre.\n"
     "• Remove or fully release constrictive dressings, casts, and bandages.\n"
     "• Keep the limb at approximately heart level; avoid excessive elevation that may reduce perfusion.\n"
     "• Maintain systemic blood pressure and correct hypotension.\n"
     "• Provide appropriate analgesia without allowing pain relief to replace serial examinations.\n"
     "• Document pain, passive-stretch pain, sensation, motor function, capillary refill, pulses, and Doppler findings.\n"
     "• Prepare for urgent fasciotomy if clinically indicated."),
    ("04 — INVESTIGATIONS", "info", 
     "• Clinical examination is central; do not delay surgery for tests when the diagnosis is clear.\n"
     "• Measure compartment pressures when the examination is equivocal or unreliable (e.g., unconscious/sedated patient).\n"
     "• A diastolic blood pressure minus compartment pressure (delta pressure) of ≤30 mmHg is concerning and supports the diagnosis.\n"
     "• CBC, electrolytes, creatinine, CK, urinalysis for myoglobin, and blood gas/lactate when significant muscle injury or rhabdomyolysis is suspected.\n"
     "• Radiographs for associated fractures."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive treatment:[/color] Emergency surgical fasciotomy with complete decompression of all involved compartments.\n\n"
     "[color=#1E3A8A]Dose:[/color]\n"
     "• There is no medication that reverses established acute compartment syndrome.\n"
     "• Give analgesia according to the local trauma protocol (e.g., IV morphine titrated in small doses, such as 2–4 mg in an adult, with reassessment).\n\n"
     "[color=#1E3A8A]How to prepare:[/color]\n"
     "• Prepare for operative decompression, blood tests, IV access, and possible fracture stabilization.\n"
     "• Treat rhabdomyolysis and electrolyte abnormalities when present.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Repeat and document neurovascular examinations frequently.\n"
     "• Monitor urine output, creatinine, potassium, CK, and acid-base status.\n"
     "• Continue surveillance after fasciotomy; wound management and delayed closure may be necessary."),
    ("06 — WARNINGS", "danger", 
     "• Do not wait for pulselessness or paralysis.\n"
     "• Do not use a normal pulse or a single normal pressure measurement to rule out evolving disease.\n"
     "• Avoid neuraxial or regional techniques that obscure assessment.\n"
     "• Late presentations with irreversible tissue damage require senior surgical assessment; fasciotomy is not automatically beneficial in every late case."),
    ("07 — DISPOSITION", "warning", 
     "• Admit urgently under orthopedics. Confirmed or strongly suspected ACS requires emergency surgical management and postoperative monitoring."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Pain out of proportion and pain on passive stretch are key early clues.\n"
     "• Repeat examinations are essential because findings evolve.\n"
     "• Compartment pressure measurements support, but do not replace, clinical judgment."),
    ("REFERENCES", "info", "AAOS, Management of Acute Compartment Syndrome, 2025; BOAST.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Open Fracture")] = [
    ("01 — RECOGNITION", "info", 
     "An open fracture is a fracture associated with a wound communicating with the fracture or fracture hematoma. Even a small wound may represent an open fracture.\n\n"
     "[color=#1E3A8A]Assess:[/color]\n"
     "• Wound location, contamination, tissue loss, and exposed bone.\n"
     "• Mechanism and energy of injury.\n"
     "• Distal pulses, capillary refill, temperature, sensation, and motor function.\n"
     "• Associated vascular injury, compartment syndrome, and systemic trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform the trauma primary survey and control life-threatening hemorrhage.\n"
     "• Contact orthopedics immediately; involve vascular or plastic surgery when indicated.\n"
     "• Cover the wound with sterile saline-moistened gauze and an appropriate sterile dressing.\n"
     "• Do not repeatedly probe the wound or attempt definitive wound cleaning in the ED.\n"
     "• Realign and splint the limb when appropriate; document neurovascular status before and after manipulation.\n"
     "• Administer IV antibiotics as early as possible, ideally within one hour.\n"
     "• Assess tetanus immunization and provide prophylaxis.\n"
     "• Keep the patient fasting if surgery is likely."),
    ("03 — INVESTIGATIONS", "info", 
     "• Radiographs including the joint above and below the fracture.\n"
     "• CBC, electrolytes, renal function, coagulation profile, and type and crossmatch according to injury severity.\n"
     "• CTA or urgent vascular assessment if vascular injury is suspected; do not delay revascularization for imaging when hard signs are present."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Antibiotics (Adult examples):[/color]\n"
     "• Lower-grade: cefazolin 2 g IV every 8 hours (local protocols may differ).\n"
     "• Severe contamination/high-grade: protocol-specific broader regimen.\n"
     "• Pediatric example: Cefazolin 30 mg/kg IV per dose, commonly every 8 hours.\n\n"
     "[color=#1E3A8A]Administration:[/color]\n"
     "• Give antibiotics promptly and document administration time.\n"
     "• Duration depends on fracture grade, operative findings, contamination, and local protocol.\n\n"
     "[color=#1E3A8A]Surgical management:[/color]\n"
     "• Urgent operative irrigation and debridement.\n"
     "• Stabilization of the fracture.\n"
     "• Early definitive soft-tissue coverage.\n"
     "• Vascular repair or shunting if limb perfusion is compromised."),
    ("05 — WARNINGS", "danger", 
     "• Antibiotics do not replace operative debridement.\n"
     "• Do not delay antibiotics while waiting for radiographs or an orthopedic review.\n"
     "• Do not push exposed bone back into the wound.\n"
     "• Suspected arterial injury requires urgent specialist management."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for urgent orthopedic management. High-energy, contaminated, vascularly compromised injuries require a trauma center."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Any wound near a fracture should be treated as potentially communicating until assessed.\n"
     "• Record neurovascular status before and after splinting or reduction.\n"
     "• Tetanus prophylaxis depends on immunization history and wound characteristics."),
    ("REFERENCES", "info", "NICE, Fractures (Complex): Assessment and Management; NICE, Major Trauma.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Hip Dislocation")] = [
    ("01 — RECOGNITION", "info", 
     "Hip dislocation is an orthopedic emergency because prolonged displacement increases the risk of femoral-head osteonecrosis.\n\n"
     "[color=#1E3A8A]Posterior dislocation:[/color]\n"
     "• Usually follows high-energy trauma.\n"
     "• Hip is often flexed, adducted, and internally rotated.\n"
     "• The limb may appear shortened.\n\n"
     "[color=#1E3A8A]Anterior dislocation:[/color]\n"
     "• Hip may be abducted and externally rotated.\n\n"
     "Assess sciatic nerve function, distal perfusion, associated fractures, and other injuries."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Perform trauma assessment and treat life-threatening injuries first.\n"
     "• Document distal pulses, capillary refill, foot sensation, ankle dorsiflexion, and plantarflexion.\n"
     "• Obtain urgent orthopedic consultation.\n"
     "• Provide analgesia and prepare for controlled reduction with appropriate sedation or anesthesia.\n"
     "• Aim for reduction as soon as safely possible, preferably within six hours.\n"
     "• Obtain pre-reduction radiographs unless an immediately threatened limb requires an exception."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP pelvis and appropriate hip radiographs.\n"
     "• CT after reduction to identify occult fractures, intra-articular fragments, or acetabular injury.\n"
     "• Repeat neurovascular examination after reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Dose:[/color]\n"
     "• Ketamine may be used for procedural sedation. A commonly used IV dissociative dose is 1–1.5 mg/kg, with additional titrated doses according to protocol.\n\n"
     "[color=#1E3A8A]How to prepare:[/color]\n"
     "• Ensure oxygen, suction, bag-mask ventilation, monitoring, IV access, and resuscitation equipment are available before sedation.\n"
     "• Prepare reduction equipment and post-reduction immobilization.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Reduction should be performed by a trained clinician with adequate sedation and muscular relaxation.\n"
     "• Monitor ECG, SpO2, BP, respiratory status, and level of consciousness.\n"
     "• Repeat and document the full neurovascular examination immediately after reduction.\n"
     "• Confirm reduction radiographically and arrange CT when indicated."),
    ("05 — WARNINGS", "danger", 
     "• Do not attempt repeated forceful reductions.\n"
     "• A suspected associated fracture may change the reduction plan; involve orthopedics urgently.\n"
     "• Persistent sciatic nerve deficit or vascular compromise requires immediate reassessment.\n"
     "• Do not discharge before confirming reduction, assessing associated injury, and establishing an orthopedic plan."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic admission or specialist-directed management is generally required. Associated fractures, instability, or failed reduction require operative assessment."),
    ("07 — CLINICAL PEARLS", "info", 
     "• The sciatic nerve is particularly vulnerable in posterior dislocation.\n"
     "• Reduction timing matters; do not allow avoidable delays.\n"
     "• A post-reduction CT may identify injuries missed on plain radiographs."),
    ("REFERENCES", "info", "Emergency Care Institute NSW, Hip Dislocation; NICE, Fractures (Complex).")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Pelvic Fracture with Hemorrhage")] = [
    ("01 — RECOGNITION", "info", 
     "Pelvic fractures may cause life-threatening retroperitoneal hemorrhage, especially after high-energy trauma.\n\n"
     "[color=#1E3A8A]Suspect significant pelvic injury with:[/color]\n"
     "• Hemodynamic instability after blunt trauma.\n"
     "• Pelvic, groin, hip, or lower-back pain.\n"
     "• Perineal bruising, pelvic deformity, or associated lower-limb injuries.\n\n"
     "[color=#991B1B]Do not repeatedly compress or 'spring' the pelvis to test stability.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate the major trauma and hemorrhage protocols.\n"
     "• Follow ABCDE; control external bleeding and establish large-bore IV or intraosseous access.\n"
     "• Apply a pelvic binder at the level of the greater trochanters when an unstable pelvic fracture is suspected.\n"
     "• Activate massive transfusion when indicated; use blood products rather than excessive crystalloid.\n"
     "• Keep the patient warm and correct hypothermia, acidosis, and coagulopathy.\n"
     "• Contact trauma surgery, orthopedics, interventional radiology, and urology.\n"
     "• Do not delay hemorrhage control for CT in a persistently unstable patient."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, blood gas/lactate, electrolytes, coagulation profile, fibrinogen, and type and crossmatch.\n"
     "• FAST/eFAST as part of the trauma assessment.\n"
     "• Pelvic radiograph if needed in an unstable patient.\n"
     "• CT with contrast in patients sufficiently stable for imaging.\n"
     "• Assess for associated abdominal, urinary tract, rectal, and vascular injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage control:[/color]\n"
     "• Pelvic binder at the greater trochanters.\n"
     "• Blood component therapy according to the massive transfusion protocol.\n"
     "• Early tranexamic acid (TXA) may be considered for significant traumatic bleeding within 3 hours: adult dose 1 g IV over 10 minutes, followed by 1 g IV over 8 hours.\n"
     "• Urgent pelvic packing, external fixation, angioembolization, or other operative intervention.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Continuous ECG, BP, SpO2, temperature, urine output, and repeated assessment of perfusion.\n"
     "• Repeat blood gas/lactate, hemoglobin, coagulation studies, and fibrinogen.\n"
     "• Reassess binder position and the need for definitive stabilization."),
    ("05 — WARNINGS", "danger", 
     "• Do not repeatedly manipulate the pelvis.\n"
     "• Do not place the binder over the iliac crests; it should be centered over the greater trochanters.\n"
     "• A normal initial hemoglobin does not exclude major acute hemorrhage.\n"
     "• Avoid routine large-volume crystalloid resuscitation.\n"
     "• Tranexamic acid is not a substitute for hemorrhage control."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate trauma-center management, usually ICU. Persistent shock requires immediate definitive hemorrhage control."),
    ("07 — CLINICAL PEARLS", "info", 
     "• The binder is a temporary stabilization measure, not definitive treatment.\n"
     "• A patient who remains unstable needs a rapid hemorrhage-control pathway.\n"
     "• Consider non-pelvic sources of bleeding even when a pelvic fracture is present."),
    ("REFERENCES", "info", "NICE, Fractures (Complex); Royal Children's Hospital, Pelvic Injury.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Knee Dislocation and Popliteal Artery Injury")] = [
    ("01 — RECOGNITION", "info", 
     "Knee dislocation may spontaneously reduce before arrival. Severe ligament injury, deformity, or a high-energy mechanism should raise suspicion even if the knee appears aligned.\n\n"
     "[color=#991B1B]Critical risk: Popliteal artery injury can cause limb-threatening ischemia.[/color]\n\n"
     "Assess:\n"
     "• Dorsalis pedis and posterior tibial pulses.\n"
     "• Limb temperature, capillary refill, skin color, and Doppler signals.\n"
     "• Common peroneal nerve function (ankle dorsiflexion, sensation over dorsum of foot).\n"
     "• ABI when appropriate."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Activate orthopedic and vascular consultation early.\n"
     "• Document neurovascular status before reduction.\n"
     "• Perform urgent reduction of a dislocated knee by a trained clinician.\n"
     "• Repeat neurovascular examination immediately after reduction.\n"
     "• If hard signs of vascular injury persist, proceed to immediate vascular surgical intervention; do not delay for angiography.\n"
     "• If vascular injury remains possible, obtain urgent CTA.\n"
     "• Immobilize the reduced knee and arrange admission."),
    ("03 — INVESTIGATIONS", "info", 
     "• Knee radiographs before and after reduction when feasible.\n"
     "• ABI and Doppler examination.\n"
     "• CTA for suspected popliteal artery injury when stable.\n"
     "• Serial vascular examinations even when initial findings appear reassuring."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Reduction and stabilization:[/color]\n"
     "• Urgent closed reduction with appropriate analgesia or sedation.\n"
     "• Splint the knee after reduction, commonly in slight flexion.\n"
     "• Vascular repair, thrombectomy, bypass, or temporary shunting may be necessary.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Record pulses, Doppler signals, skin temperature, capillary refill, sensation, and motor function before and after reduction.\n"
     "• Continue serial vascular examinations and monitor for reperfusion injury and compartment syndrome."),
    ("05 — WARNINGS", "danger", 
     "• Palpable pulses alone do not reliably exclude arterial injury.\n"
     "• A normal-looking knee does not rule out a spontaneously reduced dislocation.\n"
     "• Do not delay revascularization for imaging when there are persistent hard signs of arterial injury.\n"
     "• Watch for compartment syndrome after revascularization."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for orthopedic management and appropriate vascular observation or intervention. Confirmed or suspected popliteal artery injury requires urgent vascular surgical management."),
    ("07 — CLINICAL PEARLS", "info", 
     "• A knee dislocation is a vascular emergency until assessed adequately.\n"
     "• Document all pre- and post-reduction findings."),
    ("REFERENCES", "info", "NICE, Fractures (Complex); StatPearls, Knee Dislocation.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Cauda Equina Syndrome")] = [
    ("01 — RECOGNITION", "info", 
     "Cauda equina syndrome is compression or dysfunction of lumbosacral nerve roots and is a time-critical neurological emergency.\n\n"
     "[color=#991B1B]Red flags:[/color]\n"
     "• New urinary retention, difficulty initiating urination, or loss of awareness of bladder filling.\n"
     "• Saddle or perineal sensory disturbance.\n"
     "• New bowel dysfunction or sexual dysfunction.\n"
     "• Bilateral sciatica or progressive bilateral leg weakness.\n"
     "• Reduced anal tone may occur, but a normal examination does not exclude the diagnosis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain immediate spinal/neurosurgical consultation.\n"
     "• Arrange emergency MRI of the lumbosacral spine.\n"
     "• Document the time of symptom onset, bladder/bowel symptoms, perineal sensation, and lower-limb motor/sensory findings.\n"
     "• Perform bladder scan and measure post-void residual when available.\n"
     "• Keep the patient fasting if urgent surgery is possible."),
    ("03 — INVESTIGATIONS", "info", 
     "• Emergency MRI is the preferred investigation.\n"
     "• Bladder scan/post-void residual as an adjunct.\n"
     "• CBC, CRP/ESR, blood cultures if infection or malignancy suspected.\n"
     "• CT may identify bony injury but does not reliably exclude neural compression."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Definitive treatment:[/color]\n"
     "• Emergency surgical decompression when compressive pathology is confirmed and indicated.\n"
     "• Treat the underlying cause (disc herniation, epidural abscess, hematoma, or tumor).\n\n"
     "[color=#1E3A8A]Dose & Administration:[/color]\n"
     "• Analgesia according to local protocol.\n"
     "• If epidural abscess is suspected, obtain blood cultures if this does not delay care; initiate urgent empiric IV antibiotics for sepsis or neurological deterioration.\n"
     "• Prepare for urgent MRI and possible transfer to a center with spinal surgical capability."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay MRI because symptoms are incomplete or the patient can still walk.\n"
     "• A normal rectal examination or low post-void residual does not safely exclude the syndrome.\n"
     "• Do not discharge a patient with unresolved clinical suspicion without an appropriate definitive assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency spinal/neurosurgical evaluation. Admit or transfer urgently when MRI or specialist treatment is unavailable locally."),
    ("07 — CLINICAL PEARLS", "info", 
     "• New urinary dysfunction plus saddle sensory changes is a major warning pattern.\n"
     "• Early recognition and decompression may reduce permanent deficits.\n"
     "• Document findings clearly and time-stamp changes."),
    ("REFERENCES", "info", "NICE, Suspected Neurological Conditions; NICE, Spinal Injury.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Spinal Cord Injury")] = [
    ("01 — RECOGNITION", "info", 
     "Acute traumatic spinal cord injury may cause weakness or paralysis, sensory loss, respiratory impairment, autonomic dysfunction, and neurogenic shock.\n\n"
     "[color=#1E3A8A]Assess:[/color]\n"
     "• Mechanism and spinal pain.\n"
     "• Motor function and sensation in all limbs.\n"
     "• Respiratory effort, cough strength, and diaphragmatic function.\n"
     "• Blood pressure, heart rate, temperature, and signs of neurogenic shock.\n"
     "• Associated head, chest, abdominal, and pelvic injuries."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow ABCDE and control catastrophic hemorrhage.\n"
     "• Maintain spinal motion restriction and manual in-line stabilization during airway procedures.\n"
     "• Prevent hypoxemia and hypotension.\n"
     "• Activate trauma, spinal surgery/neurosurgery, and ICU teams.\n"
     "• Perform and document a structured neurological examination.\n"
     "• Obtain urgent CT; perform MRI after CT when neurological abnormalities suggest injury.\n"
     "• Arrange early transfer to a specialist trauma/spinal center."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT of the relevant spinal region; whole-body CT when indicated.\n"
     "• MRI when spinal cord, ligament, disc, or epidural pathology is suspected.\n"
     "• CBC, electrolytes, blood gas, lactate, coagulation profile, and type and crossmatch.\n"
     "• ECG and cardiac monitoring if neurogenic shock is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Airway and circulation:[/color]\n"
     "• Provide oxygen and ventilatory support as required.\n"
     "• Treat hemorrhagic shock by controlling bleeding.\n"
     "• If neurogenic shock is suspected after hemorrhage is assessed, use specialist-guided vasopressor support.\n\n"
     "[color=#1E3A8A]Hemodynamic management:[/color]\n"
     "• A 2024 AO Spine/Praxis guideline suggests augmenting MAP to at least 75–80 mmHg, avoiding active augmentation above 90–95 mmHg, for approximately 3–7 days.\n\n"
     "[color=#1E3A8A]Dose:[/color]\n"
     "• Norepinephrine may be used in monitored critical care, titrated to the agreed MAP target.\n"
     "• Do not use high-dose methylprednisolone routinely.\n\n"
     "[color=#1E3A8A]Monitoring:[/color]\n"
     "• Continuous ECG and blood pressure monitoring; arterial line where appropriate.\n"
     "• Frequent neurological reassessment and monitoring of respiratory function, temperature, urine output, and electrolytes.\n"
     "• Decompression within 24 hours is recommended when medically feasible."),
    ("05 — WARNINGS", "danger", 
     "• Avoid hypotension and hypoxia.\n"
     "• Do not attribute hypotension to neurogenic shock until hemorrhage and other causes have been assessed.\n"
     "• Avoid unnecessary spinal movement; do not delay life-saving airway or hemorrhage interventions.\n"
     "• Routine high-dose corticosteroids are not recommended."),
    ("06 — DISPOSITION", "warning", 
     "• Admit to a trauma center, usually ICU or a specialist spinal unit."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Neurological deficits can progress due to secondary injury.\n"
     "• Document motor and sensory findings before and after interventions.\n"
     "• Early specialist involvement is essential."),
    ("REFERENCES", "info", "NICE, Spinal Injury; AO Spine/Praxis, Acute Spinal Cord Injury Guidelines.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Septic Arthritis")] = [
    ("01 — RECOGNITION", "info", 
     "Septic arthritis is infection within a joint that can rapidly destroy cartilage and cause sepsis.\n\n"
     "[color=#1E3A8A]Features:[/color]\n"
     "• Acute painful, swollen, warm joint with restricted movement.\n"
     "• Fever may be absent, particularly in older or immunocompromised patients.\n"
     "• Risk factors: prosthetic joints, recent surgery/injection, bacteremia, diabetes, immunosuppression, skin infection."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Urgent orthopedic consultation.\n"
     "• Assess for sepsis and begin resuscitation when indicated.\n"
     "• Obtain urgent joint aspiration for cell count, Gram stain, culture, and crystals.\n"
     "• Obtain blood cultures when febrile or systemically unwell.\n"
     "• In a stable patient, obtain synovial fluid and blood cultures before antibiotics when feasible.\n"
     "• If septic shock is present, do not delay antibiotics for aspiration."),
    ("03 — INVESTIGATIONS", "info", 
     "• Joint aspiration: appearance, leukocyte count/differential, Gram stain, culture, and crystal analysis.\n"
     "• CBC, CRP/ESR, renal function, blood cultures, and lactate.\n"
     "• Ultrasound for effusion and aspiration guidance.\n"
     "• X-ray for baseline assessment; MRI when osteomyelitis or deep infection is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric antibiotics (Adult examples):[/color]\n"
     "• Vancomycin IV (15–20 mg/kg) when MRSA coverage is indicated.\n"
     "• Ceftriaxone 2 g IV every 24 hours for Gram-negative coverage.\n"
     "• Adjust therapy to culture results and local guidelines.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Urgent joint drainage is required in many cases (aspiration, arthroscopy, or open surgery).\n"
     "• Monitor temperature, hemodynamics, pain, range of motion, CRP, renal function, and cultures.\n"
     "• Narrow antibiotics when microbiology results become available."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay antibiotics in sepsis or septic shock.\n"
     "• Crystals in synovial fluid do not exclude concomitant septic arthritis.\n"
     "• A negative Gram stain does not rule out infection.\n"
     "• Prosthetic-joint infection requires urgent specialist management."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for urgent orthopedic assessment, drainage planning, and IV antimicrobial therapy. Sepsis requires an appropriate high-acuity pathway."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Aspiration is central to diagnosis.\n"
     "• The absence of fever does not exclude septic arthritis.\n"
     "• Antibiotics alone are often insufficient without adequate source control."),
    ("REFERENCES", "info", "SANJO Guideline, Septic Arthritis in Native Joints; NICE, Sepsis.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Supracondylar Humerus Fracture in Children")] = [
    ("01 — RECOGNITION", "info", 
     "Supracondylar fracture is a common pediatric elbow injury. Displaced fractures may injure the brachial artery, median/anterior interosseous nerve, radial nerve, or ulnar nerve.\n\n"
     "[color=#1E3A8A]Assess:[/color]\n"
     "• Swelling, deformity, skin tenting, and open wounds.\n"
     "• Radial pulse, capillary refill, hand temperature, and color.\n"
     "• Median/anterior interosseous, radial, and ulnar nerve function.\n"
     "• Pain, passive-stretch pain, and compartment syndrome signs."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide age- and weight-appropriate analgesia.\n"
     "• Contact orthopedics urgently for displaced fractures or any neurovascular abnormality.\n"
     "• Document neurovascular status before and after splinting or reduction.\n"
     "• Immobilize in an above-elbow backslab; avoid excessive elbow flexion.\n"
     "• Obtain AP and lateral radiographs of the distal humerus.\n"
     "• Urgent reduction and fixation are needed for displaced fractures, vascular compromise, open injury, or threatened skin."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral radiographs of the distal humerus.\n"
     "• Repeat neurovascular examination after any intervention.\n"
     "• Doppler or vascular imaging only as directed by the specialist."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia:[/color]\n"
     "• Paracetamol: 15 mg/kg orally per dose, every 4–6 hours as needed.\n"
     "• Ibuprofen: 10 mg/kg orally per dose every 6–8 hours (if appropriate).\n"
     "• IV analgesia may be needed for severe pain.\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Orthopedic reduction and percutaneous pin fixation may be required.\n"
     "• A child with a pulseless, poorly perfused hand needs emergency orthopedic and vascular assessment.\n"
     "• A pulseless but warm, well-perfused hand after reduction may be observed in selected cases under close specialist supervision.\n"
     "• Monitor for compartment syndrome and evolving nerve dysfunction."),
    ("05 — WARNINGS", "danger", 
     "• Do not dismiss a pulseless hand.\n"
     "• Do not apply a tight circumferential cast to a swollen elbow.\n"
     "• Avoid prolonged flexion in a tense, swollen limb.\n"
     "• A normal capillary refill alone does not exclude vascular injury."),
    ("06 — DISPOSITION", "warning", 
     "• Undisplaced fractures may be managed with immobilization and planned follow-up. Displaced fractures, open fractures, vascular compromise, or suspected compartment syndrome require urgent specialist care and often admission."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Assess the anterior interosseous nerve by asking the child to make an 'OK' sign.\n"
     "• Record pulse, perfusion, and nerve function before and after splinting.\n"
     "• Reassess swelling and pain frequently."),
    ("REFERENCES", "info", "Royal Children's Hospital, Supracondylar Fracture of the Humerus; NICE, Fractures (Complex).")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Limb Ischemia")] = [
    ("01 — RECOGNITION", "info", 
     "Acute limb ischemia is a sudden reduction in arterial perfusion, generally with symptoms lasting less than two weeks. It threatens limb viability and requires emergency vascular assessment.\n\n"
     "[color=#1E3A8A]The six Ps:[/color]\n"
     "• Pain.\n"
     "• Pallor.\n"
     "• Pulselessness.\n"
     "• Paresthesia.\n"
     "• Paralysis.\n"
     "• Poikilothermia (cold limb).\n\n"
     "[color=#991B1B]Motor or sensory deficits suggest a threatened limb and increase urgency.[/color]"),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Call vascular surgery immediately.\n"
     "• Rapidly assess limb viability and document sensory and motor function.\n"
     "• Assess arterial and venous Doppler signals.\n"
     "• Establish IV access, provide analgesia, and obtain blood tests.\n"
     "• Start IV unfractionated heparin promptly unless contraindicated.\n"
     "• Do not delay intervention for CTA or other imaging when the limb is immediately threatened."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, electrolytes, renal function, coagulation profile, blood group, and crossmatch.\n"
     "• ECG and assessment for atrial fibrillation or another embolic source.\n"
     "• Bedside Doppler examination.\n"
     "• CTA or duplex ultrasound when appropriate.\n"
     "• Assess for rhabdomyolysis, hyperkalemia, and acidosis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Anticoagulation:[/color]\n"
     "• IV unfractionated heparin is commonly used (e.g., 70–80 units/kg IV bolus followed by approximately 15–18 units/kg/hour, adjusted to aPTT or anti-Xa).\n\n"
     "[color=#1E3A8A]Administration and monitoring:[/color]\n"
     "• Monitor aPTT, hemoglobin, platelets, bleeding, and clinical perfusion.\n"
     "• Definitive treatment may include embolectomy, thrombectomy, bypass, or catheter-directed therapy.\n"
     "• Monitor after reperfusion for compartment syndrome, hyperkalemia, acidosis, and renal injury."),
    ("05 — WARNINGS", "danger", 
     "• Do not anticoagulate automatically when major bleeding or aortic dissection is suspected.\n"
     "• A threatened limb with motor deficit requires immediate revascularization planning.\n"
     "• Do not delay revascularization for imaging when this would jeopardize limb salvage.\n"
     "• Do not assume a palpable pulse excludes evolving ischemia."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency vascular admission or immediate transfer to a facility capable of revascularization."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Neurological deficits indicate a more advanced ischemic threat.\n"
     "• Document the time of onset and serial neurovascular findings.\n"
     "• Reperfusion can itself cause compartment syndrome and systemic metabolic complications."),
    ("REFERENCES", "info", "2024 ACC/AHA Guideline for Lower Extremity Peripheral Artery Disease; NICE, Fractures (Complex).")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "General Safety Checklist")] = [
    ("01 — GENERAL SAFETY CHECKLIST", "warning", 
     "For all orthopedic emergencies:\n\n"
     "• Complete the trauma primary survey before focusing on the fracture.\n"
     "• Document neurovascular status before and after reduction, splinting, or casting.\n"
     "• Escalate immediately for an absent pulse, a cold or pale limb, progressive neurological deficit, severe disproportionate pain, or uncontrolled bleeding.\n"
     "• Do not delay time-critical surgery or revascularization for unnecessary imaging.\n"
     "• Confirm allergies, weight-based dosing, renal function, pregnancy status when relevant, and local antimicrobial protocols.\n"
     "• Record consultation, decisions, reassessments, and transfer arrangements clearly.")
]

# ==================== NEW TOPICS (12-21) ====================

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Femoral Shaft Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "High-energy trauma, commonly road traffic collisions or falls from height. Severe thigh pain, swelling, deformity, inability to bear weight. Affected limb may appear shortened or externally rotated.\n"
     "• Significant occult blood loss can occur into the thigh, causing hemorrhagic shock.\n"
     "• Assess for associated pelvic, chest, abdominal, and other long-bone injuries."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma ABCDE approach.\n"
     "• Control external bleeding and establish IV access when indicated.\n"
     "• Assess distal pulses, capillary refill, skin temperature, sensation, and motor function before and after splinting.\n"
     "• Apply a suitable long-leg splint. Traction splint may be considered for isolated femoral shaft fracture when pelvic/ipsilateral knee injury and other contraindications excluded.\n"
     "• Provide titrated analgesia and monitor vital signs.\n"
     "• Activate major hemorrhage protocol if shock or significant ongoing bleeding suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral radiographs of entire femur, including hip and knee.\n"
     "• Trauma imaging according to mechanism and hemodynamic stability.\n"
     "• CBC, blood group and crossmatch, electrolytes, renal function, coagulation when clinically indicated.\n"
     "• Repeat neurovascular examination and document findings.\n"
     "• Consider associated femoral neck fracture, especially after high-energy trauma."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• IV morphine: commonly 0.05–0.1 mg/kg in carefully titrated doses. IV paracetamol may be used as adjunct.\n\n"
     "[color=#1E3A8A]Hemorrhage Management[/color]\n"
     "• Give isotonic crystalloid judiciously while arranging blood products when major hemorrhage suspected. Use blood-component therapy per institutional major hemorrhage protocol. Consider tranexamic acid for significant traumatic bleeding when indicated and within recommended early treatment window.\n\n"
     "[color=#1E3A8A]Definitive Fracture Management[/color]\n"
     "• Urgent orthopedic consultation. Most adult femoral shaft fractures require operative stabilization, commonly intramedullary nailing. Temporary external fixation may be required in selected patients with severe physiological instability or major soft-tissue injury.\n"
     "• Provide tetanus prophylaxis and antibiotics if open fracture, following open-fracture protocol."),
    ("05 — WARNINGS", "danger", 
     "• Reduce or carefully titrate opioids in patients with shock, respiratory compromise, or reduced consciousness.\n"
     "• Do not assume that a femoral fracture is the only source of shock. Search for associated thoracic, abdominal, pelvic, and other bleeding."),
    ("06 — DISPOSITION", "warning", 
     "• Admit under orthopedics, with trauma or critical-care involvement when indicated.\n"
     "• Escalate urgently for hemodynamic instability, suspected associated vascular injury, open fracture, or evolving compartment syndrome."),
    ("REFERENCES", "info", "ATLS; AO Surgery Reference; Local trauma/orthopedic protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Ankle Fracture-Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe ankle pain, swelling, deformity, or inability to bear weight. Skin tenting, blanching, open wounds, or threatened skin from displaced bone.\n"
     "• Distal pulse reduction, delayed capillary refill, numbness, or weakness may indicate neurovascular compromise.\n"
     "• Look for associated proximal fibular tenderness suggesting Maisonneuve injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess and document distal pulses, capillary refill, sensation, and motor function.\n"
     "• Remove constrictive footwear and assess skin.\n"
     "• Provide analgesia and elevate limb if this does not delay urgent reduction.\n"
     "• Obtain radiographs before reduction if limb is neurovascularly intact and imaging immediately available.\n"
     "• If threatened skin, severe deformity, or neurovascular compromise: perform urgent reduction without delaying for radiographs.\n"
     "• Cover any open wound with sterile dressing and follow open-fracture pathway."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP, lateral, and mortise ankle radiographs when safe and feasible. Examine entire fibula and proximal leg.\n"
     "• CT may be required for complex fractures or operative planning after stabilization.\n"
     "• Repeat and document neurovascular findings after reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Closed Reduction[/color]\n"
     "• Procedural sedation or regional anesthesia selected according to patient condition/expertise/protocol. Ensure monitoring, oxygen, suction, airway equipment, resuscitation drugs available before sedation.\n"
     "• Perform gentle reduction using appropriate technique by trained clinician. Reassess distal perfusion, sensation, movement immediately afterward. Apply well-padded splint. Obtain post-reduction radiographs and repeat neurovascular examinations.\n\n"
     "[color=#1E3A8A]Open Fracture Management[/color]\n"
     "• Administer IV antibiotics as soon as possible per open-fracture protocol. Give tetanus prophylaxis per immunization history. Cover wound with sterile dressing. Arrange urgent orthopedic assessment and operative debridement when indicated."),
    ("05 — WARNINGS", "danger", 
     "• Do not repeatedly attempt forceful reduction.\n"
     "• Persistent vascular compromise, irreducibility, or threatened skin requires immediate orthopedic escalation.\n"
     "• Do not probe wound or perform repeated bedside wound manipulation.\n"
     "• Do not delay antibiotics while waiting for imaging or definitive surgery."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or arrange urgent orthopedic management for fracture-dislocation, open injury, unstable reduction, or neurovascular concern.\n"
     "• Discharge only for selected stable injuries after assessment, with safe immobilization and reliable follow-up."),
    ("REFERENCES", "info", "NICE Complex Fractures; BOAST Ankle Fractures; AO Surgery Reference.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Traumatic Amputation")] = [
    ("01 — RECOGNIZE", "info", 
     "Complete or partial traumatic separation of finger, hand, foot, or limb. Severe bleeding, contamination, crush injury, or associated fractures.\n"
     "• Assess for shock and additional injuries.\n"
     "• A partially attached part may retain some circulation; do not complete amputation at bedside."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow ABCDE and control life-threatening hemorrhage.\n"
     "• Apply firm direct pressure and pressure dressing. Use tourniquet for life-threatening extremity hemorrhage not rapidly controlled with direct pressure, per trauma protocol. Record tourniquet application time and keep visible.\n"
     "• Do not clamp vessels blindly.\n"
     "• Cover stump with sterile dressing and provide analgesia.\n"
     "• Contact orthopedic, vascular, and microsurgical/replantation services early when available."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, blood group and crossmatch, coagulation, electrolytes, blood gas/lactate when indicated.\n"
     "• Radiographs of residual limb and amputated part when they will guide management and will not delay resuscitation.\n"
     "• Assess for crush syndrome, rhabdomyolysis, other traumatic injuries in severe crush or prolonged entrapment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Hemorrhage Control[/color]\n"
     "• Blood products and resuscitation fluids guided by hemodynamic status and major hemorrhage protocol. Tranexamic acid may be considered for significant traumatic hemorrhage when indicated and within early treatment window.\n\n"
     "[color=#1E3A8A]Stump and Amputated-Part Care[/color]\n"
     "• Administer IV antibiotics according to contamination/tissue damage/open-fracture status/allergies/local protocol. Give tetanus prophylaxis as indicated.\n"
     "• Cover stump with sterile dressing after bleeding control. Wrap amputated part in sterile gauze lightly moistened with saline, place in sealed waterproof bag, place that bag in second container with ice and water. Keep tissue cool but do not place directly on ice or immerse directly in water. Label part and send with patient.\n"
     "• Do not freeze part, scrub it, or apply antiseptic directly to it."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay life-saving hemorrhage control to preserve amputated part.\n"
     "• A tourniquet must not be intermittently loosened outside a trained, protocol-directed setting.\n"
     "• Replantation suitability depends on mechanism, ischemia time, tissue condition, patient stability, specialist assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency transfer or admission required for complete amputation, major bleeding, significant crush injury, or possible replantation.\n"
     "• Any unstable patient requires resuscitation and definitive hemorrhage control before nonessential procedures."),
    ("REFERENCES", "info", "ATLS; Stop the Bleed; AAOS Limb Salvage/Amputation Resources; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Shoulder Dislocation with Neurovascular Risk")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute shoulder pain, deformity, restricted movement, inability to use arm. Anterior dislocation common; posterior dislocation may follow seizures/electrical injury and can be missed on single AP radiograph.\n"
     "• Assess axillary nerve function (sensation over lateral deltoid, deltoid contraction when feasible).\n"
     "• Check radial pulse, capillary refill, hand sensation, distal motor function.\n"
     "• Consider associated proximal humerus fracture, brachial plexus injury, or vascular injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and support arm in comfortable position.\n"
     "• Document neurovascular status before any reduction attempt.\n"
     "• Obtain appropriate radiographs before reduction when fracture suspected and patient neurovascularly intact.\n"
     "• Urgent reduction needed when vascular compromise suspected, under appropriately trained clinician and local emergency protocol.\n"
     "• Avoid repeated or forceful reduction attempts."),
    ("03 — INVESTIGATIONS", "info", 
     "• Shoulder radiographs, including views that assess alignment and help identify associated fractures.\n"
     "• Additional imaging if posterior dislocation suspected or radiographs inconclusive.\n"
     "• Vascular imaging and urgent specialist consultation if arterial injury suspected.\n"
     "• Repeat neurovascular examination after reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia and Reduction[/color]\n"
     "• Use analgesia and, where appropriate, procedural sedation or intra-articular local anesthetic per local protocol and patient factors.\n"
     "• If procedural sedation planned, prepare monitoring, oxygen, suction, airway equipment, resuscitation supplies. If intra-articular anesthesia selected, use approved sterile technique and verify maximum safe local-anesthetic dose.\n"
     "• Reduction by trained clinician using gentle, appropriate technique. Stop if unexpected resistance, worsening pain, or concern for fracture.\n"
     "• Reassess distal pulses, capillary refill, sensation, motor function immediately after reduction. Obtain post-reduction radiographs and immobilize shoulder."),
    ("05 — WARNINGS", "danger", 
     "• Do not attempt routine manipulation when associated fracture or complex injury makes it unsafe.\n"
     "• Persistent absent pulse, expanding hematoma, or progressive neurological deficit requires urgent specialist assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Discharge may be considered after successful reduction, satisfactory post-reduction imaging, intact/evaluated neurovascular status, safe follow-up plan.\n"
     "• Admit or transfer for fracture-dislocation, vascular injury, irreducibility, or unresolved neurological deficit."),
    ("REFERENCES", "info", "AAOS Shoulder Dislocation; NICE Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Hematogenous Osteomyelitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Fever, focal bone pain, tenderness, reduced use of affected limb. Children may present with refusal to walk, limp, or refusal to move arm/leg.\n"
     "• Early radiographs may be normal.\n"
     "• Consider associated septic arthritis, especially when pain centered on joint or passive movement severely restricted.\n"
     "• Suspect severe infection in patients with systemic toxicity, hypotension, altered mental status."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for sepsis and initiate local sepsis pathway when indicated.\n"
     "• Obtain blood cultures before antibiotics if this can be done promptly without delaying treatment.\n"
     "• Arrange urgent orthopedic and pediatric/infectious-disease consultation as appropriate.\n"
     "• Provide analgesia and avoid unnecessary weight-bearing on affected limb.\n"
     "• If unstable or septic, start empiric IV antibiotics promptly after cultures when feasible."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, CRP, ESR, renal function, blood cultures.\n"
     "• Plain radiographs to assess for fracture/alternative diagnoses (early osteomyelitis may not be visible).\n"
     "• MRI generally preferred when diagnosis uncertain or extent must be assessed.\n"
     "• Ultrasound may identify joint effusion/superficial collection but does not exclude bone infection.\n"
     "• Aspirate or obtain tissue for culture when feasible, especially if drainage/debridement required."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric Antimicrobial Therapy[/color]\n"
     "• Empiric IV antibiotic choice must cover likely pathogens, particularly Staphylococcus aureus. Add MRSA coverage when local prevalence/patient risk factors/severity/previous colonization warrants.\n"
     "• Pediatric and adult regimens differ; select using age, weight, renal function, allergy history, local resistance, institutional osteomyelitis guideline.\n\n"
     "[color=#1E3A8A]Drainage and Source Control[/color]\n"
     "• Antibiotics alone may be insufficient when drainable abscess, infected joint, or necrotic tissue present.\n"
     "• Urgent surgical drainage/debridement indicated for selected patients with abscess formation, associated septic arthritis, necrotic bone, or failure to respond to appropriate antimicrobial treatment."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay antibiotics in unstable patient to obtain MRI or invasive specimen.\n"
     "• In clinically stable patient, specialist-directed sampling before antibiotics may improve microbiological diagnosis when it can be performed safely and promptly.\n"
     "• A suspected associated septic joint requires urgent evaluation because delayed drainage can cause rapid joint damage."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with systemic toxicity, suspected abscess, inability to tolerate treatment, uncertain diagnosis requiring urgent investigation, or need for IV therapy/surgery.\n"
     "• Selected stable patients may transition to appropriate oral regimen after specialist review and clinical improvement, with reliable follow-up."),
    ("REFERENCES", "info", "PIDS/IDSA Pediatric Osteomyelitis Guideline; IDSA Infectious Diseases Guidelines; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Tibial Plateau Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Knee pain, swelling, inability to bear weight after fall, direct impact, or twisting injury. Large knee effusion or hemarthrosis may be present.\n"
     "• Assess for associated ligament injury, meniscal injury, neurovascular compromise.\n"
     "• High-energy injuries may cause significant soft-tissue damage and acute compartment syndrome.\n"
     "• Consider associated knee dislocation even if joint appears aligned at presentation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma ABCDE approach when injury high energy.\n"
     "• Provide analgesia and immobilize knee in comfortable position. Keep patient non-weight-bearing.\n"
     "• Assess and document distal pulses, capillary refill, foot temperature, sensation, ankle/toe movement.\n"
     "• Perform serial examinations for compartment syndrome.\n"
     "• Obtain urgent orthopedic consultation for displaced fractures, skin compromise, open injury, or neurovascular abnormalities."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral knee radiographs.\n"
     "• CT of knee for fracture configuration and operative planning when indicated.\n"
     "• CT angiography if vascular injury suspected; do not delay emergency vascular management in critically ischemic limb.\n"
     "• CBC, renal function, other trauma investigations according to injury severity.\n"
     "• Repeat neurovascular examination after splinting and any manipulation."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Analgesia[/color]\n"
     "• Paracetamol may be used as adjunct according to age/weight/liver function/local protocol. Opioid analgesia may be required for severe pain, titrated to clinical response.\n"
     "• Apply well-padded knee immobilizer or splint without excessive pressure. Reassess distal perfusion, sensation, movement after immobilization.\n"
     "• Monitor pain, swelling, compartment-syndrome warning signs.\n\n"
     "[color=#1E3A8A]Definitive Fracture Management[/color]\n"
     "• Nonoperative treatment may be suitable for selected stable, minimally displaced fractures after orthopedic assessment. Displaced, unstable, depressed, or intra-articular fractures may require operative fixation.\n"
     "• Open fractures require urgent open-fracture management, including antibiotics, wound coverage, and surgical assessment."),
    ("05 — WARNINGS", "danger", 
     "• Increasing pain, pain with passive stretch, tense swelling, or new neurological deficits require immediate reassessment.\n"
     "• Normal distal pulses do not exclude compartment syndrome."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or urgently refer for displaced fracture, significant swelling, open injury, suspected compartment syndrome, vascular concern, or inability to ensure safe outpatient management.\n"
     "• Maintain non-weight-bearing status until definitive plan established."),
    ("REFERENCES", "info", "AO Surgery Reference; NICE Complex Fractures; Local orthopedic trauma protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Calcaneal Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Heel pain and swelling after fall from height or axial loading injury. Bruising around heel and plantar surface may be prominent. Patient may be unable to bear weight.\n"
     "• Assess skin tension and posterior heel skin viability.\n"
     "• Consider associated thoracolumbar spine fractures and other injuries from same mechanism."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for additional injuries using trauma approach when indicated.\n"
     "• Keep patient non-weight-bearing. Elevate limb and apply well-padded splint.\n"
     "• Perform and document neurovascular assessment.\n"
     "• Urgently refer if open fracture, threatened skin, severe deformity, or neurovascular compromise.\n"
     "• Avoid tight circumferential casts in markedly swollen limb."),
    ("03 — INVESTIGATIONS", "info", 
     "• Lateral and axial calcaneal radiographs when appropriate.\n"
     "• CT for intra-articular fractures and operative planning.\n"
     "• Examine spine and other regions injured by axial loading. Assess for associated foot fractures and soft-tissue injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Pain Control and Immobilization[/color]\n"
     "• Use age- and weight-appropriate analgesia. Titrate opioid analgesia when required for severe pain, following local protocol.\n"
     "• Apply well-padded posterior splint or other suitable immobilization. Elevate limb and monitor swelling, skin condition, pain, distal neurovascular status.\n"
     "• Maintain strict non-weight-bearing.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Management depends on fracture displacement, joint involvement, soft-tissue condition, patient factors. Selected fractures may be managed nonoperatively. Displaced intra-articular fractures or fractures with threatened skin may require urgent specialist intervention.\n"
     "• Delay definitive fixation when necessary to allow soft-tissue swelling to improve, provided limb remains safe."),
    ("05 — WARNINGS", "danger", 
     "• Blanching, pressure necrosis, or skin tenting over heel requires urgent orthopedic assessment.\n"
     "• Do not delay referral when skin is threatened."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic referral for displaced, open, or skin-threatening injuries.\n"
     "• Assess for spinal injury and arrange further imaging when indicated.\n"
     "• Discharge only when injury stable, pain controlled, non-weight-bearing feasible, follow-up reliable."),
    ("REFERENCES", "info", "AO Surgery Reference; NICE Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Elbow Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe elbow pain, deformity, swelling, restricted movement after trauma. Posterior dislocation common.\n"
     "• Assess brachial artery and distal perfusion. Check median, ulnar, and radial nerve function.\n"
     "• Consider associated radial head, coronoid, or distal humeral fractures."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and support arm.\n"
     "• Document pulses, capillary refill, hand temperature, sensation, motor function before reduction.\n"
     "• Obtain radiographs before reduction if no urgent neurovascular/skin threat and imaging immediately available.\n"
     "• Urgent reduction required when vascular compromise or severe skin tension present.\n"
     "• Seek orthopedic help for complex dislocation, associated fracture, open injury, or failed reduction."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral elbow radiographs.\n"
     "• Post-reduction radiographs to confirm alignment and identify fractures.\n"
     "• CT when associated fracture or complex injury suspected.\n"
     "• Vascular imaging and urgent vascular consultation when arterial injury suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Reduction and Analgesia[/color]\n"
     "• Select procedural sedation or appropriate regional/local anesthetic technique according to patient condition/expertise/protocol. Sedative and analgesic doses must be individualized.\n"
     "• Prepare cardiorespiratory monitoring, oxygen, suction, airway equipment, resuscitation supplies before procedural sedation. Ensure trained personnel available.\n"
     "• Reduction by trained clinician gently. Reassess neurovascular function immediately after. Immobilize elbow in appropriate splint. Obtain post-reduction imaging and assess joint stability.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Simple stable dislocations may be managed with brief immobilization followed by supervised early mobilization. Associated fractures, instability, open dislocation, or vascular injury may require surgery.\n"
     "• Avoid unnecessarily prolonged immobilization because elbow stiffness can develop rapidly."),
    ("05 — WARNINGS", "danger", 
     "• Do not make repeated forceful attempts.\n"
     "• Persistent absent pulse, expanding hematoma, progressive neurological deficit, or irreducibility requires urgent specialist intervention."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic assessment for all confirmed dislocations.\n"
     "• Admission or transfer for complex injuries, neurovascular compromise, open injury, or unstable reduction.\n"
     "• Discharge only after satisfactory reduction, imaging, neurovascular reassessment, clear follow-up plan."),
    ("REFERENCES", "info", "AO Surgery Reference; NICE Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Pediatric Forearm Fracture with Neurovascular Compromise")] = [
    ("01 — RECOGNIZE", "info", 
     "Forearm pain, deformity, swelling, reduced use of affected arm. Assess radial and ulnar pulses, capillary refill, hand temperature, finger movement. Test median, anterior interosseous, ulnar, and radial nerve function as age/cooperation allow.\n"
     "• A pale, cold, poorly perfused hand or progressive neurological deficit is an emergency.\n"
     "• Severe pain, tense swelling, pain with passive finger stretch may indicate compartment syndrome."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma stabilization principles.\n"
     "• Provide age- and weight-appropriate analgesia. Remove rings or constrictive items.\n"
     "• Document neurovascular examination before and after any manipulation.\n"
     "• Obtain urgent orthopedic assistance for vascular compromise, open fracture, severe deformity, or suspected compartment syndrome.\n"
     "• If circulation threatened, urgent reduction by trained clinician should not be delayed for routine imaging."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral radiographs of forearm, including wrist and elbow as appropriate.\n"
     "• CBC and other tests only when indicated by major trauma, bleeding, or planned intervention.\n"
     "• Vascular imaging or specialist vascular assessment when arterial injury remains suspected after reduction.\n"
     "• Repeat neurovascular examinations and document changes."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Reduction and Immobilization[/color]\n"
     "• Use appropriate pediatric analgesic regimen based on weight and contraindications. Procedural sedation or anesthesia may be required for reduction and must follow pediatric sedation protocols.\n"
     "• Calculate all medication doses from child's current weight. Verify maximum doses and concentrations. Prepare appropriate pediatric monitoring, oxygen, suction, airway equipment if sedation planned.\n"
     "• Immobilize fracture with appropriately padded splint. If reduction required, perform under suitable analgesia or anesthesia by trained clinician. Reassess circulation, sensation, motor function immediately after reduction and immobilization. Obtain post-reduction radiographs.\n\n"
     "[color=#1E3A8A]Open Fracture Management[/color]\n"
     "• Cover wound with sterile dressing. Administer IV antibiotics promptly according to pediatric open-fracture protocol. Give tetanus prophylaxis when indicated. Arrange urgent orthopedic assessment and operative management when required."),
    ("05 — WARNINGS", "danger", 
     "• A normal pulse does not exclude compartment syndrome or evolving vascular injury.\n"
     "• Increasing pain, pain with passive stretch, tense swelling, or progressive sensory/motor loss requires immediate reassessment.\n"
     "• Do not delay emergency orthopedic intervention for a persistently ischemic hand."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or transfer for neurovascular compromise, open fracture, suspected compartment syndrome, unstable reduction, or need for urgent surgery.\n"
     "• Outpatient care only for selected stable fractures with intact perfusion, adequate immobilization, pain control, reliable follow-up."),
    ("REFERENCES", "info", "BOAST Fractures in Children; NICE Non-Complex Fractures; AO Pediatric Resources; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Crush Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Prolonged compression of muscle after entrapment, building collapse, industrial injury, or severe limb trauma. Muscle pain, swelling, weakness, or dark urine may occur.\n"
     "• Systemic complications: rhabdomyolysis, hyperkalemia, acute kidney injury, metabolic acidosis, shock. Hyperkalemia can cause fatal dysrhythmias.\n"
     "• Crush syndrome may develop even when external injuries appear limited."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma ABCDE approach and activate appropriate rescue/trauma teams.\n"
     "• Establish IV access and cardiac monitoring as early as feasible.\n"
     "• Obtain urgent blood tests, including potassium, creatinine, bicarbonate, calcium, phosphate, creatine kinase. Check ECG promptly when hyperkalemia possible.\n"
     "• Begin isotonic crystalloid resuscitation when indicated, individualized to hemodynamics, urine output, renal function, risk of fluid overload.\n"
     "• Seek urgent critical-care, trauma, and surgical advice.\n"
     "• Do not delay lifesaving rescue or hemorrhage control for laboratory testing."),
    ("03 — INVESTIGATIONS", "info", 
     "• Serial potassium, renal function, bicarbonate, calcium, phosphate, creatine kinase.\n"
     "• Blood gas and lactate when shock or metabolic disturbance suspected.\n"
     "• Urinalysis; heme-positive urine with few red cells may suggest myoglobinuria.\n"
     "• ECG monitoring for hyperkalemic changes.\n"
     "• Assess for associated fractures, vascular injury, compartment syndrome."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Fluid Resuscitation[/color]\n"
     "• Use isotonic crystalloid according to perfusion, hemodynamic status, urine output, renal function, local crush-injury protocol. Do not apply fixed high-volume regimen to every patient, particularly when renal failure or cardiac dysfunction present.\n"
     "• Reassess BP, HR, lung examination, peripheral perfusion, urine output, electrolytes, renal function. Insert urinary catheter when clinically indicated for accurate output monitoring. In adults, urine output targets may be individualized; avoid pursuing target with escalating fluid when patient anuric or developing pulmonary edema.\n\n"
     "[color=#1E3A8A]Hyperkalemia Management[/color]\n"
     "• If hyperkalemia causes ECG changes or is severe, treat immediately per emergency hyperkalemia protocol. IV calcium used to stabilize myocardium when indicated; insulin with glucose and inhaled beta-agonist may be used to shift potassium intracellularly. Select drug doses according to age, renal function, ECG findings, local protocol.\n"
     "• Continuous ECG monitoring required for severe hyperkalemia. Recheck potassium after treatment and monitor glucose frequently after insulin. Arrange definitive potassium removal and renal replacement therapy when indicated.\n\n"
     "[color=#1E3A8A]Limb Assessment and Surgical Management[/color]\n"
     "• Perform serial examinations for compartment syndrome and vascular compromise. Fasciotomy indicated when compartment syndrome diagnosed after urgent surgical assessment; not routinely indicated solely because crush injury occurred.\n"
     "• Debridement or amputation may be necessary for nonviable tissue, uncontrollable infection, or unsalvageable limb. Dialysis may be required for refractory hyperkalemia, severe acidosis, fluid overload, or other standard indications for renal replacement therapy."),
    ("05 — WARNINGS", "danger", 
     "• Excessive fluid administration can cause life-threatening overload.\n"
     "• Routine bicarbonate or mannitol is not recommended for every case of rhabdomyolysis; use only for specific indications under appropriate protocol.\n"
     "• Calcium stabilizes myocardium but does not lower serum potassium. Hyperkalemia treatment is temporizing; potassium must be monitored and definitive management arranged."),
    ("06 — DISPOSITION", "warning", 
     "• Admit patients with suspected crush syndrome for serial laboratory testing and monitoring.\n"
     "• Critical-care admission for shock, severe electrolyte disturbance, dysrhythmias, respiratory compromise, or renal failure.\n"
     "• Arrange urgent nephrology and orthopedic/surgical involvement when indicated."),
    ("REFERENCES", "info", "AAST Rhabdomyolysis Consensus; KDIGO AKI Guideline; Local trauma/hyperkalemia protocols.")
]


# ==================== BATCH 3 (TOPICS 21-30) ====================

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Femoral Neck Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Common in older adults after a low-energy fall; may occur in younger patients after high-energy trauma.\n"
     "• Groin or hip pain, inability to bear weight, pain with passive hip movement.\n"
     "• Affected limb may be shortened and externally rotated in a displaced fracture.\n"
     "• Occult fractures may occur despite initially normal radiographs.\n"
     "• Assess for head injury, other fractures, anticoagulant use, and causes of the fall."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE if major trauma suspected.\n"
     "• Provide timely analgesia and support the affected limb.\n"
     "• Avoid unnecessary movement and repeated attempts to mobilize the patient.\n"
     "• Assess distal neurovascular status.\n"
     "• Obtain urgent orthopedic consultation.\n"
     "• Review anticoagulants, baseline mobility, cognition, frailty, and relevant comorbidities."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP pelvis and lateral hip radiographs.\n"
     "• MRI when clinical suspicion remains high despite negative radiographs; CT may be considered if MRI unavailable/contraindicated.\n"
     "• CBC, electrolytes, renal function, coagulation tests when indicated, blood group/crossmatch if surgery anticipated.\n"
     "• ECG and additional preoperative investigations according to clinical status."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia[/color]\n"
     "• Paracetamol according to age, weight, liver function, local protocol. Carefully titrated opioid analgesia may be required for severe pain. A fascia iliaca or other appropriate regional nerve block may reduce opioid requirements when performed by a trained clinician.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Most confirmed femoral neck fractures require surgical management. Options include internal fixation, hemiarthroplasty, or total hip arthroplasty depending on fracture displacement, patient function, and overall condition.\n"
     "• Optimize dehydration, anemia, electrolyte abnormalities, anticoagulation, and other reversible medical problems without unnecessary surgical delay.\n"
     "• Provide VTE prophylaxis according to bleeding risk and local protocol."),
    ("05 — WARNINGS", "danger", 
     "• NSAIDs may be unsuitable in some older adults due to renal impairment, GI bleeding risk, or anticoagulant use.\n"
     "• Do not delay analgesia while waiting for imaging."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for orthopedic management and coordinated medical assessment.\n"
     "• Aim for surgery on the day of or the day after admission when medically appropriate.\n"
     "• Begin postoperative mobilization and rehabilitation as soon as clinically safe."),
    ("REFERENCES", "info", "NICE Hip Fracture Management; AAOS Hip Fractures in Older Adults; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Hip Dislocation with Associated Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe hip pain and inability to move or bear weight after high-energy trauma.\n"
     "• Posterior dislocation commonly presents with a shortened, flexed, adducted, internally rotated limb.\n"
     "• Anterior dislocation may present with limb externally rotated and abducted.\n"
     "• Assess sciatic nerve function (ankle dorsiflexion, plantarflexion, sensation over foot).\n"
     "• Associated acetabular or femoral head fractures may complicate reduction."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma ABCDE approach.\n"
     "• Document distal pulses, perfusion, and neurological function before intervention.\n"
     "• Provide analgesia and arrange urgent orthopedic consultation.\n"
     "• Obtain pre-reduction radiographs unless immediate limb-threatening emergency requires action without delay.\n"
     "• Arrange urgent reduction by trained clinician, usually under procedural sedation or anesthesia.\n"
     "• Avoid repeated forceful reduction attempts, particularly when associated fracture suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP pelvis and appropriate hip radiographs.\n"
     "• CT after reduction to assess acetabular and femoral head fractures or loose intra-articular fragments.\n"
     "• Additional trauma imaging according to mechanism and clinical findings.\n"
     "• Repeat neurovascular examination after reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Urgent Reduction[/color]\n"
     "• Select procedural sedation or general anesthesia according to patient stability, injury complexity, local protocol. No single sedation regimen is appropriate for every patient.\n"
     "• Perform reduction using appropriate technique by experienced clinician. Reassess neurovascular status immediately after reduction.\n"
     "• Obtain post-reduction radiographs and CT when indicated.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Simple dislocations may be managed with protected mobilization under orthopedic direction. Associated acetabular or femoral head fractures may require operative fixation.\n"
     "• Evaluate for sciatic nerve injury and persistent instability."),
    ("05 — WARNINGS", "danger", 
     "• Hip dislocation is time-critical because delayed reduction increases risk of femoral head avascular necrosis.\n"
     "• Vascular compromise, irreducibility, or suspected fracture-dislocation requires urgent specialist management."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or transfer for orthopedic management.\n"
     "• Discharge only after successful reduction, satisfactory imaging, stable neurovascular findings, and documented orthopedic plan."),
    ("REFERENCES", "info", "AO Surgery Reference; NICE Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Patellar Fracture and Extensor Mechanism Disruption")] = [
    ("01 — RECOGNIZE", "info", 
     "Anterior knee pain and swelling after direct blow or sudden quadriceps contraction. Hemarthrosis and focal patellar tenderness may be present.\n"
     "• Inability to perform straight-leg raise suggests disruption of extensor mechanism, although pain can also limit examination.\n"
     "• Open fractures may communicate with knee joint. Consider associated quadriceps tendon or patellar tendon rupture."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess skin integrity and distal neurovascular status.\n"
     "• Provide analgesia and apply knee immobilizer with knee in extension if appropriate.\n"
     "• Keep patient protected from weight-bearing until fracture assessed.\n"
     "• Obtain urgent orthopedic consultation for open fracture, extensor mechanism disruption, or significant displacement.\n"
     "• Cover open wounds with sterile dressing and initiate open-fracture management."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral knee radiographs; additional views may be useful when tolerated.\n"
     "• CT for complex or comminuted fractures when needed for operative planning.\n"
     "• Ultrasound or MRI may be considered if tendon injury remains uncertain.\n"
     "• CBC and other tests according to trauma severity and operative requirements."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Analgesia[/color]\n"
     "• Use age- and weight-appropriate analgesia based on comorbidities and contraindications. Titrated opioid analgesia may be required for severe pain.\n"
     "• Immobilize knee in extension when appropriate. Reassess skin, swelling, distal perfusion, sensation, pain. Document ability to perform straight-leg raise when pain control permits.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Nondisplaced fractures with intact extensor mechanism may be treated with immobilization and close orthopedic follow-up. Displaced fractures, open fractures, or loss of extensor mechanism commonly require operative treatment."),
    ("05 — WARNINGS", "danger", 
     "• Do not allow an unassessed patient with suspected extensor mechanism disruption to walk unsupported.\n"
     "• Increasing pain or tense swelling requires reassessment for associated compartment syndrome or other injury."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic review for displaced fracture, open injury, or inability to extend knee.\n"
     "• Discharge only for selected stable injuries with secure immobilization plan and reliable follow-up."),
    ("REFERENCES", "info", "AAOS Patellar Fractures; AO Surgery Reference; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Achilles Tendon Rupture")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden posterior ankle pain, often described as being kicked in the back of the leg. A snapping sensation during running, jumping, or sudden acceleration.\n"
     "• Difficulty pushing off or standing on tiptoe.\n"
     "• Palpable tendon gap may be present. Thompson calf-squeeze test may be abnormal, with reduced/absent plantarflexion."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and avoid forced ankle dorsiflexion.\n"
     "• Immobilize ankle in plantarflexion to reduce tension on tendon.\n"
     "• Provide crutches and protect limb from unsupported weight-bearing.\n"
     "• Arrange timely orthopedic assessment. Check skin condition and distal neurovascular status."),
    ("03 — INVESTIGATIONS", "info", 
     "• Diagnosis is often clinical.\n"
     "• Ultrasound can help when examination findings equivocal.\n"
     "• MRI reserved for selected uncertain or complex cases.\n"
     "• Radiographs may be indicated if associated avulsion fracture or other bony injury suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Pain Control[/color]\n"
     "• Paracetamol or another appropriate analgesic according to patient factors and local guidance.\n"
     "• Maintain ankle in plantarflexion using appropriate splint or functional boot. Check skin pressure areas, distal circulation, sensation, comfort. Arrange prompt specialist review to select functional rehabilitation pathway.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Both nonoperative functional rehabilitation and surgical repair may be appropriate, depending on patient factors, tendon gap, activity requirements, specialist assessment. Rehabilitation requires structured protocol with gradual progression of ankle movement/loading.\n"
     "• Assess VTE risk and consider prophylaxis per individual risk and local policy."),
    ("05 — WARNINGS", "danger", 
     "• Do not force ankle into neutral dorsiflexion during initial immobilization.\n"
     "• Avoid unsupported walking until appropriate protection plan in place."),
    ("06 — DISPOSITION", "warning", 
     "• Arrange timely orthopedic or specialist musculoskeletal follow-up.\n"
     "• Urgent referral required for open injury, suspected neurovascular compromise, or associated fracture.\n"
     "• Provide clear instructions on immobilization, mobility aids, return precautions."),
    ("REFERENCES", "info", "AAOS Achilles Tendon Rupture; NICE VTE Prevention; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Osteoporotic Vertebral Compression Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden focal back pain after minor fall, lifting, coughing, or spontaneous onset in patient with osteoporosis. Localized spinal tenderness and pain worsened by movement.\n"
     "• Consider vertebral fracture in older adults and patients with long-term corticosteroid exposure.\n"
     "• [color=#991B1B]Red flags:[/color] Progressive weakness, sensory changes, saddle anesthesia, urinary retention, fecal incontinence, fever, cancer history, significant trauma.\n"
     "• Severe trauma, neurological deficits, or suspected spinal instability requires emergency evaluation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE if significant trauma suspected.\n"
     "• Perform focused neurological examination of lower-limb power, sensation, reflexes, sphincter-related symptoms.\n"
     "• Use spinal precautions when instability suspected after trauma.\n"
     "• Provide analgesia and assist safe movement without unnecessary prolonged bed rest.\n"
     "• Obtain urgent spinal or orthopedic consultation for neurological deficit, suspected instability, or cauda equina symptoms."),
    ("03 — INVESTIGATIONS", "info", 
     "• Spine radiographs or CT depending on mechanism, severity, suspected fracture.\n"
     "• MRI when neurological deficits, concern for spinal cord/nerve compression, suspected malignancy/infection, or uncertainty about fracture acuity.\n"
     "• CBC, renal function, calcium, other tests when secondary causes or alternative diagnoses suspected.\n"
     "• Evaluate bone health and secondary osteoporosis after acute stabilization."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia and Supportive Care[/color]\n"
     "• Paracetamol when appropriate. Short-term opioid analgesia may be considered for severe pain, with cautious titration. Avoid routine prolonged opioid treatment.\n"
     "• Encourage safe mobilization as tolerated after stability assessed. Use brace only when recommended for appropriate indication; prolonged immobilization may worsen deconditioning.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Most uncomplicated compression fractures managed nonoperatively with analgesia, gradual mobilization, osteoporosis treatment.\n"
     "• Specialist evaluation needed for persistent severe pain, progressive deformity, instability, or neurological compromise. Vertebral augmentation procedures reserved for selected patients after specialist assessment."),
    ("05 — WARNINGS", "danger", 
     "• New weakness, saddle anesthesia, urinary retention, or bowel dysfunction requires immediate reassessment for neural compression.\n"
     "• Do not attribute severe back pain automatically to osteoporosis without considering malignancy, infection, other serious causes."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or urgently refer for neurological deficits, unstable fracture, uncontrolled pain, inability to mobilize safely, or suspicion of malignancy/infection.\n"
     "• Arrange follow-up for fracture healing, falls prevention, osteoporosis evaluation."),
    ("REFERENCES", "info", "NICE Spinal Injury; ACR Appropriateness Criteria; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Scaphoid Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Wrist pain after fall on outstretched hand. Tenderness in anatomical snuffbox or over scaphoid tubercle. Pain with axial loading of thumb or wrist movement.\n"
     "• Initial radiographs may be normal despite clinically significant fracture.\n"
     "• Proximal pole fractures have increased risk of avascular necrosis due to scaphoid's blood supply."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Remove rings and assess swelling. Document distal perfusion, sensation, motor function.\n"
     "• Immobilize wrist in thumb-spica splint when scaphoid fracture suspected.\n"
     "• Avoid forceful wrist movement and weight-bearing through affected hand.\n"
     "• Arrange timely fracture-clinic or orthopedic assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Scaphoid-specific wrist radiographs.\n"
     "• If initial radiographs negative but clinical suspicion remains: arrange MRI where available; CT may be used according to local pathways. Repeat radiographs may be considered if advanced imaging unavailable, but should not replace appropriate follow-up.\n"
     "• Reassess for associated distal radius or other carpal fractures."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Analgesia[/color]\n"
     "• Paracetamol according to age, weight, liver function, local guidance. NSAID may be considered when appropriate after assessing renal function, GI risk, contraindications.\n"
     "• Immobilize wrist with well-padded wrist splint that protects suspected fracture. Provide clear instructions to keep splint dry/intact. Reassess swelling, sensation, skin condition, distal perfusion. Arrange definitive imaging and follow-up.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Nondisplaced fractures may be treated with immobilization under specialist guidance. Displaced fractures, proximal pole fractures, instability, or nonunion may require surgical fixation. Follow-up imaging important to confirm healing."),
    ("05 — WARNINGS", "danger", 
     "• Do not dismiss persistent anatomical snuffbox tenderness because initial radiographs are normal.\n"
     "• Increasing pain, numbness, or cold/pale hand requires urgent reassessment."),
    ("06 — DISPOSITION", "warning", 
     "• Discharge may be appropriate with immobilization, adequate analgesia, reliable follow-up.\n"
     "• Refer urgently if neurovascular compromise, open injury, or significant associated trauma."),
    ("REFERENCES", "info", "NICE Non-Complex Fractures; BSSH Scaphoid Fractures; AO Surgery Reference.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Distal Radius Fracture with Neurovascular Compromise")] = [
    ("01 — RECOGNIZE", "info", 
     "Wrist pain, swelling, deformity, reduced hand function after fall.\n"
     "• Check radial pulse, capillary refill, hand temperature, finger movement.\n"
     "• Assess median nerve function (sensation in thumb/index/middle fingers, thumb opposition when possible).\n"
     "• Severe pain, progressive median nerve symptoms, or tense wrist may indicate acute carpal tunnel syndrome.\n"
     "• Open fractures and marked deformity require urgent assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Remove rings and constrictive items. Document neurovascular examination before manipulation.\n"
     "• Provide analgesia and elevate limb if appropriate.\n"
     "• Obtain wrist radiographs if this does not delay treatment of threatened circulation or skin.\n"
     "• Urgent reduction required for markedly displaced fracture with threatened skin or compromised circulation.\n"
     "• Seek urgent orthopedic assistance for persistent ischemia, progressive neurological deficits, open injury, or suspected acute carpal tunnel syndrome."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral wrist radiographs. Include forearm imaging if injury extends proximally or additional fracture suspected.\n"
     "• Post-reduction radiographs to confirm alignment.\n"
     "• CT may be required for complex intra-articular fractures and operative planning."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Reduction and Immobilization[/color]\n"
     "• Use appropriate analgesia, regional anesthesia, or procedural sedation according to patient condition/local protocol.\n"
     "• Perform reduction using appropriate technique by trained clinician. Apply well-padded splint that accommodates swelling. Repeat neurovascular examination immediately after reduction/immobilization. Obtain post-reduction radiographs.\n\n"
     "[color=#1E3A8A]Open Fracture Management[/color]\n"
     "• Cover wound with sterile dressing. Administer IV antibiotics promptly per open-fracture protocol. Assess tetanus immunization status and provide prophylaxis when indicated. Arrange urgent operative assessment when required.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Stable fractures may be managed with immobilization and scheduled radiographic follow-up. Unstable, significantly displaced, or intra-articular fractures may require operative fixation. Acute carpal tunnel syndrome caused by fracture may require urgent decompression."),
    ("05 — WARNINGS", "danger", 
     "• Do not apply a tight circumferential cast to a markedly swollen limb.\n"
     "• Persistent vascular compromise or progressive median nerve deficit after reduction requires immediate orthopedic reassessment.\n"
     "• A palpable pulse does not exclude acute carpal tunnel syndrome."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic review for neurovascular compromise, open fracture, unstable reduction, or progressive median nerve symptoms.\n"
     "• Outpatient management appropriate only when alignment, perfusion, pain control, follow-up arrangements satisfactory."),
    ("REFERENCES", "info", "NICE Non-Complex Fractures; AAOS/ASSH Distal Radius Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Monteggia Fracture-Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Fracture of proximal ulna associated with dislocation of radial head.\n"
     "• Pain, swelling, deformity, reduced movement of elbow and forearm.\n"
     "• Radial head dislocation can be missed if elbow not adequately imaged.\n"
     "• Assess posterior interosseous nerve function (finger and thumb extension).\n"
     "• Pediatric cases may have subtle radiographic findings and require careful assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and support arm.\n"
     "• Document distal pulses, capillary refill, sensation, motor function.\n"
     "• Obtain radiographs of entire forearm, including elbow and wrist.\n"
     "• Apply well-padded splint and avoid repeated manipulation.\n"
     "• Arrange urgent orthopedic assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral radiographs of forearm, elbow, wrist as indicated.\n"
     "• Confirm alignment of radiocapitellar joint on appropriate views.\n"
     "• CT may be needed for complex fractures or uncertain joint alignment.\n"
     "• Repeat neurovascular examination after splinting or reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Reduction[/color]\n"
     "• Provide age- and weight-appropriate analgesia. Procedural sedation or anesthesia may be required for reduction, particularly in children.\n"
     "• Immobilize forearm and arrange prompt orthopedic reduction/stabilization. Reassess radial nerve function, distal perfusion, sensation after any intervention. Obtain post-reduction imaging to confirm restoration of radial head alignment.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• In adults, operative stabilization of ulna commonly required to restore radial head alignment.\n"
     "• In children, management depends on fracture pattern, displacement, stability; many require reduction and close specialist follow-up.\n"
     "• Persistent radial head dislocation requires urgent reassessment."),
    ("05 — WARNINGS", "danger", 
     "• Failure to recognize radial head dislocation can lead to chronic disability.\n"
     "• Do not repeatedly attempt reduction without appropriate expertise and imaging."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic referral or admission generally required.\n"
     "• Transfer to center with pediatric or upper-limb expertise if appropriate treatment unavailable locally."),
    ("REFERENCES", "info", "AO Surgery Reference; BOAST Fractures in Children; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Galeazzi Fracture-Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Fracture of radial shaft, typically distal third, associated with disruption of distal radioulnar joint (DRUJ).\n"
     "• Forearm pain, wrist pain, swelling, restricted pronation/supination. DRUJ instability may be subtle.\n"
     "• Check for ulnar nerve symptoms and distal neurovascular compromise.\n"
     "• In children, related injury may involve distal radial fracture with distal ulnar physeal injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and immobilize forearm. Document distal pulses, capillary refill, sensation, finger movement.\n"
     "• Obtain radiographs of entire forearm, including wrist and elbow.\n"
     "• Seek urgent orthopedic assessment, especially for deformity, open injury, or neurovascular abnormalities.\n"
     "• Cover open wounds with sterile dressing and initiate open-fracture care."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral forearm radiographs including wrist and elbow.\n"
     "• Assess DRUJ alignment and compare with opposite side when necessary.\n"
     "• CT may help evaluate complex DRUJ injury or uncertain alignment.\n"
     "• Post-reduction or postoperative imaging should confirm restoration of alignment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Pain Control[/color]\n"
     "• Use appropriate analgesia based on age, weight, renal function, contraindications. Procedural sedation or anesthesia may be needed for selected reductions.\n"
     "• Immobilize limb and avoid forceful forearm rotation. Reassess distal perfusion, sensation, motor function after splinting. Arrange urgent orthopedic management.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Adult Galeazzi fractures commonly require operative fixation of radius and assessment of DRUJ stability. Additional stabilization may be needed if DRUJ remains unstable after fixation.\n"
     "• Pediatric management depends on specific fracture pattern and stability."),
    ("05 — WARNINGS", "danger", 
     "• A radial shaft fracture with DRUJ disruption can be missed if wrist not examined and imaged.\n"
     "• Do not assume injury is stable solely because radial fracture appears minimally displaced."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic referral and usually hospital-based definitive management.\n"
     "• Admit or transfer for open fracture, neurovascular compromise, unstable joint alignment, or need for surgery."),
    ("REFERENCES", "info", "AO Surgery Reference; NICE Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Hand Compartment Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe, progressive hand pain following crush injury, fracture, reperfusion, or tight circumferential dressing. Tense swelling of hand or individual compartments. Pain on passive stretch of fingers.\n"
     "• Paresthesia or progressive sensory/motor deficits may occur.\n"
     "• Pallor and absent pulses are late findings; normal pulses do not exclude compartment syndrome."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Obtain immediate orthopedic or hand-surgery consultation.\n"
     "• Remove or split constrictive dressings, casts, bandages promptly.\n"
     "• Keep hand approximately at heart level rather than excessively elevated when compartment syndrome suspected.\n"
     "• Document pain, swelling, sensation, motor function, perfusion.\n"
     "• Do not delay urgent surgical assessment for imaging when clinical diagnosis clear."),
    ("03 — INVESTIGATIONS", "info", 
     "• Diagnosis is primarily clinical.\n"
     "• Measure compartment pressures when examination unreliable or diagnosis remains uncertain.\n"
     "• Check for associated fractures, crush injury, vascular injury, rhabdomyolysis.\n"
     "• Obtain electrolytes, renal function, creatine kinase in significant crush injuries."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Emergency Decompression[/color]\n"
     "• Analgesia should be titrated to patient's condition. Definitive treatment is urgent surgical decompression when acute compartment syndrome diagnosed.\n"
     "• Arrange immediate hand-surgery or orthopedic assessment and prepare for operative fasciotomy. Obtain urgent anesthesia and operating-room support. Perform necessary laboratory testing without delaying decompression.\n"
     "• Maintain appropriate hemodynamic support and reassess hand frequently. Proceed to fasciotomy when indicated by surgical team. Reassess muscle viability, perfusion, neurological function after decompression.\n"
     "• Manage associated fractures, vascular injuries, rhabdomyolysis."),
    ("05 — WARNINGS", "danger", 
     "• Do not wait for pulselessness before acting.\n"
     "• Analgesia, elevation, or dressing release alone is not definitive treatment when compartment syndrome persists.\n"
     "• Delayed decompression can result in permanent nerve and muscle damage."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency admission and operative management.\n"
     "• Postoperative monitoring and repeat debridement may be required depending on muscle viability and wound condition."),
    ("REFERENCES", "info", "BOA Compartment Syndrome Guidance; AAOS Acute Compartment Syndrome Guidance; Local protocols.")
]


# ==================== BATCH 4 (TOPICS 31-40) ====================

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Humeral Shaft Fracture with Radial Nerve Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Upper-arm pain, swelling, bruising, deformity, and reduced arm function after trauma.\n"
     "• Radial nerve injury may cause wrist drop, weak finger extension, and sensory loss over the dorsum of the hand near the first web space.\n"
     "• Assess brachial artery perfusion, distal pulses, capillary refill, and hand temperature.\n"
     "• Open fracture, vascular injury, and progressive neurological deficits require urgent specialist assessment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow the trauma ABCDE approach when indicated.\n"
     "• Provide analgesia and support the arm in a suitable splint.\n"
     "• Document radial, median, and ulnar nerve function before and after immobilization.\n"
     "• Assess distal perfusion and document pulses.\n"
     "• Cover open wounds with a sterile dressing and initiate the open-fracture protocol.\n"
     "• Arrange orthopedic consultation for displaced fractures, open injuries, vascular compromise, or worsening neurological findings."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral radiographs of the humerus, including the shoulder and elbow as appropriate.\n"
     "• Vascular imaging if arterial injury is suspected.\n"
     "• CBC and blood group/crossmatch if significant bleeding or surgery is anticipated.\n"
     "• Repeat neurological examination and document the findings clearly."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Analgesia[/color]\n"
     "• Use paracetamol or other appropriate analgesia according to age, weight, renal and hepatic function, and local protocol. Titrated opioid analgesia may be required for severe pain.\n"
     "• Prepare a suitable coaptation splint or other immobilization device.\n"
     "• Immobilize the arm and support it in a sling when appropriate. Reassess skin condition, distal perfusion, sensation, and motor function after splinting.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Many closed humeral shaft fractures can be treated with functional bracing or other nonoperative methods.\n"
     "• Operative fixation may be required for open fractures, vascular injury, unstable fracture patterns, polytrauma, or selected cases of nonunion.\n"
     "• A primary radial nerve palsy associated with a closed fracture does not automatically require immediate nerve exploration; the decision depends on fracture pattern, associated injuries, and specialist assessment."),
    ("05 — WARNINGS", "danger", 
     "• Do not apply a tight circumferential cast to a markedly swollen arm.\n"
     "• New or progressive neurological deficits or impaired perfusion require urgent reassessment.\n"
     "• Open injury, suspected nerve transection, or new neurological deficit after manipulation or fixation requires urgent specialist review."),
    ("06 — DISPOSITION", "warning", 
     "• Refer to orthopedics for definitive fracture management.\n"
     "• Admit or transfer for open injury, vascular compromise, unstable polytrauma, or other urgent surgical indications."),
    ("REFERENCES", "info", "AO Surgery Reference; AAOS Humeral Shaft Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Clavicle Fracture with Skin or Neurovascular Compromise")] = [
    ("01 — RECOGNIZE", "info", 
     "Shoulder pain, swelling, bruising, and tenderness over the clavicle.\n"
     "• Displacement may cause skin tenting, blanching, or threatened skin breakdown.\n"
     "• Assess for associated rib fractures, pneumothorax, and chest injury.\n"
     "• Check distal perfusion and brachial plexus function.\n"
     "• Open fracture, skin compromise, or suspected subclavian vessel injury is an emergency."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, and circulation, especially after high-energy trauma.\n"
     "• Inspect the skin carefully over the fracture.\n"
     "• Provide analgesia and support the arm in a sling.\n"
     "• Document distal pulses, capillary refill, sensation, and motor function.\n"
     "• Obtain urgent orthopedic consultation for open fracture, threatened skin, vascular injury, or severe displacement.\n"
     "• Do not repeatedly manipulate the fracture in the emergency department."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clavicle radiographs.\n"
     "• Chest radiograph or CT according to trauma mechanism and suspected associated injury.\n"
     "• CT angiography when subclavian or other major vascular injury is suspected and the patient is sufficiently stable.\n"
     "• Additional imaging for suspected pneumothorax, rib fractures, or scapular injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia and Support[/color]\n"
     "• Use appropriate analgesia based on age, weight, renal and hepatic function, and contraindications.\n"
     "• Prepare a correctly fitted sling that supports the arm without excessive pressure.\n"
     "• Support the arm and reassess pain, skin condition, and distal neurovascular status.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Most uncomplicated clavicle fractures can be treated nonoperatively with a sling and gradual rehabilitation.\n"
     "• Surgery may be indicated for open fracture, threatened skin, neurovascular injury, selected markedly displaced fractures, or associated shoulder-girdle instability.\n"
     "• Associated chest injuries must be evaluated and treated independently."),
    ("05 — WARNINGS", "danger", 
     "• Skin blanching or severe tenting over a displaced fracture requires urgent orthopedic assessment.\n"
     "• A normal distal pulse does not exclude subclavian vascular injury."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic review for skin compromise, open injury, marked displacement, or neurovascular abnormality.\n"
     "• Admit or transfer for major associated trauma or suspected vascular injury.\n"
     "• Discharge is appropriate for selected uncomplicated fractures with adequate pain control and follow-up."),
    ("REFERENCES", "info", "AAOS Clavicle Fractures; NICE Non-Complex Fractures; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Perilunate Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "High-energy wrist injury, commonly following a fall on an outstretched hand.\n"
     "• Severe wrist pain, swelling, and reduced movement.\n"
     "• Median nerve compression may cause numbness or tingling in the thumb, index, middle, and radial half of the ring finger.\n"
     "• Carpal alignment may be abnormal on lateral radiographs.\n"
     "• Perilunate dislocation may be associated with scaphoid fracture, creating a perilunate fracture-dislocation."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess distal perfusion and document median, ulnar, and radial nerve function.\n"
     "• Provide analgesia and immobilize the wrist.\n"
     "• Obtain urgent radiographs and orthopedic or hand-surgery consultation.\n"
     "• If there is acute median nerve compression or threatened circulation, arrange immediate specialist-led reduction without unnecessary delay.\n"
     "• Avoid repeated forceful reduction attempts."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP, lateral, and appropriate additional wrist radiographs.\n"
     "• Carefully assess carpal alignment on the lateral view.\n"
     "• CT may be required to define associated carpal fractures.\n"
     "• Repeat neurovascular examination after reduction."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Urgent Reduction and Immobilization[/color]\n"
     "• Use appropriate analgesia, regional anesthesia, or procedural sedation according to patient condition and local protocol.\n"
     "• Prepare monitoring, oxygen, suction, airway equipment, and resuscitation supplies if procedural sedation is planned.\n"
     "• Reduction should be performed by a trained clinician with urgent specialist involvement. Immobilize the wrist after reduction.\n"
     "• Reassess median nerve function, distal perfusion, sensation, and movement. Obtain post-reduction radiographs and arrange CT if indicated.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Most perilunate dislocations and fracture-dislocations require urgent operative management.\n"
     "• Surgery may involve reduction, ligament repair, and fixation of associated fractures.\n"
     "• Monitor for acute carpal tunnel syndrome, avascular necrosis, stiffness, and post-traumatic arthritis."),
    ("05 — WARNINGS", "danger", 
     "• Perilunate dislocation is a time-sensitive injury because of the risk of median nerve injury and long-term carpal dysfunction.\n"
     "• Persistent median nerve symptoms, vascular compromise, or failed reduction requires immediate hand-surgery review."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent admission or transfer to a center with orthopedic or hand-surgery capability.\n"
     "• Do not discharge a patient with an unreduced perilunate dislocation."),
    ("REFERENCES", "info", "AO Surgery Reference; BSSH Wrist Injury Resources; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Knee Extensor Mechanism Rupture")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden anterior knee pain after jumping, falling, or forceful quadriceps contraction.\n"
     "• Inability to actively extend the knee or perform a straight-leg raise.\n"
     "• Patella alta may suggest patellar tendon rupture; patella baja may suggest quadriceps tendon rupture.\n"
     "• A palpable tendon defect may be present.\n"
     "• Risk factors include older age, diabetes, chronic kidney disease, and previous tendon disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Provide analgesia and immobilize the knee in extension when appropriate.\n"
     "• Document distal pulses, capillary refill, sensation, and motor function.\n"
     "• Assess skin integrity and associated fractures.\n"
     "• Obtain urgent orthopedic consultation when the extensor mechanism is disrupted.\n"
     "• Avoid unsupported weight-bearing."),
    ("03 — INVESTIGATIONS", "info", 
     "• AP and lateral knee radiographs to assess patellar position and associated fractures.\n"
     "• Ultrasound or MRI when the diagnosis is uncertain.\n"
     "• Check for associated patellar fracture or other traumatic injury.\n"
     "• Additional laboratory testing is guided by comorbidities and planned surgery."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Pain Control[/color]\n"
     "• Use appropriate analgesia according to age, weight, renal and hepatic function, and contraindications.\n"
     "• Prepare a well-fitted knee immobilizer or extension splint.\n"
     "• Immobilize the knee in extension when indicated. Reassess pain, swelling, skin condition, and distal neurovascular status. Arrange prompt orthopedic evaluation.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Complete quadriceps or patellar tendon ruptures usually require surgical repair.\n"
     "• Partial tears with preserved extensor function may be treated nonoperatively under specialist supervision.\n"
     "• Rehabilitation and progressive mobilization must follow the treating orthopedic team's protocol."),
    ("05 — WARNINGS", "danger", 
     "• Do not assume that inability to extend the knee is caused only by pain.\n"
     "• Delayed diagnosis of complete tendon rupture can impair functional recovery."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic assessment for suspected complete rupture.\n"
     "• Admit or arrange expedited specialist management when surgery is indicated or the patient cannot mobilize safely."),
    ("REFERENCES", "info", "AAOS Quadriceps Tendon Tear; AAOS Patellar Tendon Tear; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Septic Bursitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Localized swelling, warmth, tenderness, and erythema over a superficial bursa, commonly the olecranon or prepatellar bursa.\n"
     "• Fever may be absent, especially in older or immunocompromised patients.\n"
     "• Skin abrasions, penetrating injury, diabetes, and immunosuppression increase infection risk.\n"
     "• Differentiate from septic arthritis, cellulitis, gout, and traumatic bursitis.\n"
     "• Severe pain with passive joint movement or a joint effusion should raise concern for septic arthritis."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs and screen for sepsis.\n"
     "• Examine the skin for wounds, fluctuance, spreading cellulitis, and drainage. Mark the extent of erythema when appropriate.\n"
     "• Obtain urgent specialist assessment if septic arthritis, deep infection, or systemic toxicity is suspected.\n"
     "• If sepsis is present, obtain blood cultures when feasible and start prompt empiric antimicrobial therapy."),
    ("03 — INVESTIGATIONS", "info", 
     "• CBC, CRP, and other tests according to clinical severity.\n"
     "• Aspirate bursal fluid for cell count, Gram stain, culture, and crystal analysis when indicated and safe.\n"
     "• Blood cultures for systemic illness, fever, or suspected bacteremia.\n"
     "• Ultrasound may help identify a fluid collection.\n"
     "• Imaging is indicated if foreign body, osteomyelitis, or another deep process is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Empiric Antimicrobial Therapy[/color]\n"
     "• Select empiric antibiotics to cover likely Staphylococcus aureus and streptococci. Include MRSA coverage when severity, local prevalence, prior colonization, or other risk factors warrant it.\n"
     "• Start IV therapy for severe infection, systemic toxicity, or circumstances requiring inpatient management. Oral therapy may be suitable for selected stable patients after clinical assessment.\n"
     "• Review culture results and narrow therapy when appropriate.\n\n"
     "[color=#1E3A8A]Drainage and Supportive Care[/color]\n"
     "• Aspiration or incision and drainage may be needed for a significant infected collection or failure of medical treatment.\n"
     "• Elevate and protect the affected area. Provide analgesia and review tetanus status if there is an associated wound."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay antibiotics in an unstable or septic patient while waiting for aspiration.\n"
     "• Avoid aspirating through infected skin when an alternative safe approach is available."),
    ("06 — DISPOSITION", "warning", 
     "• Admit for sepsis, rapidly progressive infection, suspected septic arthritis, immunocompromise with severe infection, or need for operative drainage.\n"
     "• Outpatient treatment may be appropriate for selected stable patients with reliable follow-up."),
    ("REFERENCES", "info", "IDSA Skin and Soft Tissue Infection Guidelines; AFP Common Superficial Bursitis; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Cervical Spine Fracture and Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Neck pain or midline cervical tenderness after trauma. High-risk mechanisms include road traffic collisions, falls from height, diving injuries, and axial loading.\n"
     "• Neurological symptoms may include limb weakness, numbness, paresthesia, or respiratory difficulty.\n"
     "• Altered consciousness, intoxication, distracting injury, or inability to communicate reliably may prevent clinical clearance.\n"
     "• Absence of neck pain does not exclude cervical spine injury in an unreliable examination."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow the trauma ABCDE approach while maintaining spinal motion restriction.\n"
     "• Maintain the airway with appropriate cervical spine precautions.\n"
     "• Avoid unnecessary neck movement and manual manipulation.\n"
     "• Assess limb power, sensation, respiratory function, and sphincter-related symptoms when feasible.\n"
     "• Obtain urgent trauma and spinal specialist consultation for suspected unstable injury or neurological deficit.\n"
     "• Treat associated hypoxia and hypotension promptly."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT cervical spine is generally the first-line imaging test for significant suspected cervical spine trauma in adults.\n"
     "• MRI is indicated when spinal cord, ligamentous, or other soft-tissue injury is suspected, particularly with neurological abnormalities not explained by CT.\n"
     "• Additional spine imaging depends on the mechanism, examination, and local trauma protocol.\n"
     "• Document the neurological examination before and after transfers or interventions."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Spinal Motion Restriction and Stabilization[/color]\n"
     "• No medication reverses mechanical spinal instability. Analgesia should be individualized according to pain, hemodynamic status, and respiratory function.\n"
     "• Prepare an appropriately fitted cervical collar when indicated. Ensure trained personnel and suitable equipment are available for transfers and airway management.\n"
     "• Maintain spinal precautions until the injury is assessed and the spine is appropriately cleared. Reassess airway patency, breathing, circulation, and neurological status frequently.\n\n"
     "[color=#1E3A8A]Hemodynamic and Neurological Management[/color]\n"
     "• Treat hypoxia and hypotension promptly to reduce secondary spinal cord injury.\n"
     "• If neurogenic shock is suspected, assess for concurrent hemorrhage before attributing hypotension to spinal cord injury.\n"
     "• High-dose corticosteroids are not routinely recommended as standard treatment for acute traumatic spinal cord injury."),
    ("05 — WARNINGS", "danger", 
     "• Avoid routine prolonged rigid-collar use without reassessment; collars can cause pressure injury and other complications.\n"
     "• Do not perform unsupervised neck manipulation or traction."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or transfer urgently for suspected unstable fracture, neurological deficit, or spinal cord injury.\n"
     "• Do not discharge until the cervical spine has been appropriately assessed and cleared under an accepted protocol."),
    ("REFERENCES", "info", "NICE Spinal Injury; ACS Best Practices Spine Injury; AO Spine Cervical Injury Management.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Thoracolumbar Spine Fracture")] = [
    ("01 — RECOGNIZE", "info", 
     "Back pain and focal tenderness following high-energy trauma or a fall. Axial loading injuries may cause vertebral compression, burst fractures, or fracture-dislocation.\n"
     "• Neurological findings may include lower-limb weakness, sensory loss, saddle anesthesia, or bladder and bowel dysfunction.\n"
     "• Older adults and patients with osteoporosis may sustain fractures after relatively minor trauma.\n"
     "• Associated abdominal, pelvic, and chest injuries must be considered."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess ABCDE and treat life-threatening injuries first.\n"
     "• Maintain spinal motion restriction when an unstable injury is suspected.\n"
     "• Assess lower-limb power, sensation, and sphincter-related symptoms.\n"
     "• Provide analgesia and avoid unnecessary spinal manipulation.\n"
     "• Seek urgent spinal consultation for neurological deficit, suspected instability, or significant fracture."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT of the relevant spinal region is generally preferred for significant traumatic injury.\n"
     "• MRI is indicated when spinal cord, cauda equina, ligamentous injury, or neural compression is suspected.\n"
     "• Evaluate for associated abdominal, chest, and pelvic trauma.\n"
     "• Obtain laboratory testing based on associated injuries and planned intervention."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Stabilization and Analgesia[/color]\n"
     "• Use appropriate analgesia based on age, weight, renal function, respiratory status, and contraindications. Opioids may be required for severe pain but should be carefully titrated.\n"
     "• Maintain spinal precautions until stability is determined. Monitor vital signs, pain, limb power, sensation, and bladder function when relevant.\n"
     "• Reassess neurological status after transfers and interventions.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Stable fractures without neurological compromise may be treated nonoperatively with appropriate mobilization and follow-up.\n"
     "• Unstable fractures, progressive deformity, or neural compression may require surgical stabilization or decompression.\n"
     "• Bracing is selected according to fracture pattern and specialist advice rather than used automatically in every case."),
    ("05 — WARNINGS", "danger", 
     "• New weakness, saddle anesthesia, urinary retention, or bowel dysfunction requires immediate reassessment for neural compression.\n"
     "• Do not delay urgent specialist assessment while awaiting nonessential tests."),
    ("06 — DISPOSITION", "warning", 
     "• Admit or transfer for unstable fracture, neurological deficit, inability to mobilize safely, or associated major trauma.\n"
     "• Discharge only after appropriate imaging, stability assessment, pain control, and a documented follow-up plan."),
    ("REFERENCES", "info", "NICE Spinal Injury; ACR Acute Spinal Trauma Criteria; AO Spine Thoracolumbar Injury Management.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Cauda Equina Syndrome")] = [
    ("01 — RECOGNIZE", "info", 
     "Severe low-back pain with new urinary retention, altered urinary sensation, or overflow incontinence.\n"
     "• Saddle or perineal sensory loss.\n"
     "• New bowel dysfunction or sexual dysfunction.\n"
     "• Bilateral sciatica, progressive lower-limb weakness, or sensory changes may occur.\n"
     "• Symptoms can be incomplete or evolve over time; a normal single examination does not reliably exclude the syndrome."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat as a time-critical spinal emergency.\n"
     "• Obtain urgent spinal surgical consultation.\n"
     "• Perform and document a focused lower-limb neurological examination.\n"
     "• Ask specifically about urinary sensation, ability to initiate urination, saddle sensation, and bowel function.\n"
     "• Arrange emergency MRI as soon as possible according to the local pathway.\n"
     "• Assess bladder retention with a bladder scan when available, without delaying definitive assessment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Emergency MRI of the lumbar spine is the preferred investigation for suspected cauda equina compression.\n"
     "• Bladder scan and post-void residual measurement may provide useful supporting information but cannot independently exclude the diagnosis.\n"
     "• Additional investigations depend on suspected causes such as tumor, infection, hemorrhage, or fracture.\n"
     "• Check anticoagulant use and relevant infection or malignancy history."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Emergency Assessment and Supportive Care[/color]\n"
     "• Provide appropriate analgesia according to clinical status and local protocol. No analgesic regimen substitutes for urgent diagnosis and decompression when indicated.\n"
     "• Arrange MRI, specialist consultation, and transfer to a center capable of urgent spinal intervention if necessary.\n"
     "• Prepare a bladder catheter when retention is present and catheterization is clinically appropriate.\n"
     "• Record bladder symptoms, neurological findings, symptom onset, and progression.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• MRI-confirmed compressive pathology requires urgent spinal surgical assessment.\n"
     "• Emergency decompression may be required depending on the cause and neurological findings.\n"
     "• Treat the underlying cause, such as a large disc herniation, epidural hematoma, tumor, or infection."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay MRI or specialist referral because symptoms are incomplete or because a bladder scan appears reassuring.\n"
     "• Do not rely on digital rectal tone alone to exclude cauda equina syndrome."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency hospital assessment and specialist management are required.\n"
     "• Do not discharge a patient with suspected cauda equina syndrome without appropriate definitive assessment."),
    ("REFERENCES", "info", "NICE Suspected Neurological Conditions/Spinal Injury; BASS Cauda Equina Resources; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Achilles Tendon Avulsion or Insertional Rupture")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden posterior heel pain following forced dorsiflexion or powerful calf contraction.\n"
     "• Tenderness at the Achilles insertion or a palpable defect near the heel.\n"
     "• Weak plantarflexion and difficulty pushing off during walking.\n"
     "• Insertional avulsion may be associated with a calcaneal fracture.\n"
     "• Consider open injury, skin compromise, and associated neurovascular abnormalities."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess skin integrity and distal neurovascular status.\n"
     "• Provide analgesia and immobilize the ankle in plantarflexion.\n"
     "• Avoid stretching the tendon or forcing the ankle into dorsiflexion.\n"
     "• Keep the patient protected from unsupported weight-bearing.\n"
     "• Arrange prompt orthopedic assessment, especially when an avulsion fracture or open injury is suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• Lateral ankle and calcaneal radiographs if an avulsion fracture is suspected.\n"
     "• Ultrasound may help assess tendon continuity.\n"
     "• MRI may be useful in complex or uncertain injuries.\n"
     "• Additional imaging depends on the mechanism and suspected associated fractures."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Immobilization and Analgesia[/color]\n"
     "• Use appropriate analgesia based on age, weight, renal function, hepatic function, and contraindications.\n"
     "• Prepare a well-padded splint or boot that maintains plantarflexion.\n"
     "• Immobilize the ankle and avoid tendon stretch. Reassess skin pressure points, pain, sensation, and distal perfusion.\n"
     "• Arrange timely specialist assessment to determine the definitive treatment pathway.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Treatment may include functional rehabilitation or surgical repair, depending on rupture location, displacement, tissue condition, and patient factors.\n"
     "• Displaced calcaneal avulsion fractures may require urgent operative management.\n"
     "• Rehabilitation should follow a structured specialist protocol."),
    ("05 — WARNINGS", "danger", 
     "• Do not force the ankle into neutral position when acute Achilles rupture is suspected.\n"
     "• Open injuries or threatened skin require urgent surgical assessment."),
    ("06 — DISPOSITION", "warning", 
     "• Arrange prompt orthopedic review.\n"
     "• Admit or transfer for open injury, displaced avulsion fracture, threatened skin, or neurovascular compromise."),
    ("REFERENCES", "info", "AAOS Achilles Tendon Rupture; AO Surgery Reference; Local protocols.")
]

ORTHOPEDICS_TOPICS[("Orthopedic Emergencies", "Acute Rotator Cuff Tear After Trauma")] = [
    ("01 — RECOGNIZE", "info", 
     "Sudden shoulder pain and weakness following a fall, traction injury, or shoulder dislocation.\n"
     "• Inability to actively elevate the arm despite relatively preserved passive movement.\n"
     "• Weakness may be more prominent than pain after initial analgesia.\n"
     "• Consider associated proximal humerus fracture, dislocation, and axillary nerve injury.\n"
     "• Older adults may develop an acute tear after relatively minor trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess for fracture, dislocation, and neurovascular injury.\n"
     "• Provide analgesia and support the arm in a sling for comfort.\n"
     "• Document active and passive shoulder movement when safe.\n"
     "• Assess axillary nerve sensation over the lateral shoulder and distal upper-limb neurological function.\n"
     "• Arrange urgent orthopedic assessment if there is marked weakness, inability to elevate the arm, or suspected acute full-thickness tear."),
    ("03 — INVESTIGATIONS", "info", 
     "• Shoulder radiographs to exclude fracture or dislocation.\n"
     "• Ultrasound or MRI when a significant rotator cuff tear is suspected.\n"
     "• Additional imaging if nerve injury or other structural injury is suspected.\n"
     "• Document the degree of weakness and functional limitation."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]Analgesia and Support[/color]\n"
     "• Use appropriate analgesia according to age, comorbidities, renal function, and contraindications.\n"
     "• Prepare a sling that supports the arm without unnecessary prolonged immobilization.\n"
     "• Provide analgesia and reassess shoulder function. Encourage gentle movement of unaffected joints.\n"
     "• Avoid forceful shoulder exercises until fracture, dislocation, and major tendon injury have been assessed.\n\n"
     "[color=#1E3A8A]Definitive Management[/color]\n"
     "• Treatment depends on tear size, tendon involvement, functional requirements, and patient factors.\n"
     "• Early specialist assessment is important for suspected acute traumatic full-thickness tears because selected patients may benefit from timely repair.\n"
     "• Rehabilitation is guided by the final diagnosis and specialist plan."),
    ("05 — WARNINGS", "danger", 
     "• Persistent inability to actively elevate the arm after trauma warrants further evaluation even when radiographs are normal.\n"
     "• Do not attribute all weakness to pain without reassessment."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent orthopedic or shoulder-specialist follow-up for substantial weakness or suspected full-thickness tear.\n"
     "• Emergency referral is required for associated dislocation, fracture, vascular compromise, or progressive neurological deficit."),
    ("REFERENCES", "info", "AAOS Management of Rotator Cuff Injuries; NICE Non-Complex Fractures; Local protocols.")
]