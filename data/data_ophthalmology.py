# data_ophthalmology.py

OPHTHALMOLOGY_DATA = {
    "Ophthalmic Emergencies": {
        "Ocular Trauma & Foreign Bodies": [
            "Chemical Eye Injury",
            "Open Globe Injury",
            "Corneal and Intraocular Foreign Body",
            "Hyphema",
            "Orbital Fracture with Extraocular Muscle Entrapment",
            "Eyelid Laceration and Canalicular Injury",
            "Traumatic Lens Dislocation",
            "Traumatic Optic Neuropathy",
            "Orbital Compartment Syndrome"
        ],
        "Cornea & Anterior Segment": [
            "Corneal Abrasion",
            "Infectious Keratitis and Corneal Ulcer",
            "Acute Anterior Uveitis (Iritis)",
            "Acute Scleritis",
            "Corneal Graft Rejection",
            "Acute Hypopyon"
        ],
        "Retina & Vitreous": [
            "Central Retinal Artery Occlusion (CRAO)",
            "Central Retinal Vein Occlusion (CRVO)",
            "Retinal Detachment",
            "Acute Vitreous Hemorrhage"
        ],
        "Glaucoma & Neuro-Ophthalmology": [
            "Acute Angle-Closure Glaucoma",
            "Giant Cell Arteritis with Visual Symptoms",
            "Acute Optic Neuritis",
            "Acute Diplopia and Ocular Motor Cranial Nerve Palsy"
        ],
        "Orbit, Adnexa & Ocular Infections": [
            "Orbital Cellulitis",
            "Preseptal Cellulitis",
            "Acute Dacryocystitis",
            "Endophthalmitis",
            "Postoperative Eye Emergency and Suspected Endophthalmitis",
            "Herpes Zoster Ophthalmicus"
        ],
        "General Ophthalmic Emergencies": [
            "Acute Painful Red Eye — Emergency Differential Diagnosis"
        ]
    }
}

OPHTHALMOLOGY_TOPICS = {}

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Chemical Eye Injury")] = [
    ("01 — DEFINITION", "info", "Ocular injury caused by acids, alkalis, or other chemicals. Alkali injuries can penetrate deeply and cause severe ocular damage."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Severe pain, redness, tearing, and photophobia.\n"
     "• Blurred vision.\n"
     "• Conjunctival swelling and corneal opacity.\n"
     "• Severe cases may show limbal ischemia or extensive tissue damage."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Start copious irrigation immediately with clean water, normal saline, or Ringer's lactate.\n"
     "• Do not delay irrigation to obtain history, measure visual acuity, or contact ophthalmology.\n"
     "• Remove contact lenses and accessible particulate material when safe.\n"
     "• Check ocular surface pH when available; continue irrigation until physiologic pH is achieved.\n"
     "• Recheck pH after a short pause to detect rebound acidity or alkalinity.\n"
     "• Arrange urgent ophthalmology assessment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IRRIGATION[/color]\n"
     "• Irrigate continuously and abundantly; several liters may be required.\n"
     "• Evert the eyelids and remove retained particles from the conjunctival fornices when trained and when globe rupture has been excluded.\n"
     "• Document the chemical, exposure time, irrigation performed, pH, and visual acuity when safely obtainable.\n\n"
     "[color=#1E3A8A]B. ADDITIONAL TREATMENT[/color]\n"
     "• Topical anesthetic may be used by a clinician to facilitate irrigation.\n"
     "• Ophthalmology may prescribe topical antibiotics, cycloplegics, corticosteroids, or other agents depending on injury severity.\n"
     "• Severe burns may require admission and surgical treatment."),
    ("05 — WARNINGS", "danger", 
     "• Do not attempt chemical neutralization with another acid or alkali.\n"
     "• If open globe injury is suspected, avoid pressure and obtain immediate specialist guidance regarding decontamination."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate ophthalmology referral for significant chemical burns, corneal opacity, reduced vision, persistent abnormal pH, or suspected limbal injury."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Irrigation is the priority; do not wait for a preferred solution.\n"
     "• Alkali burns can progress despite initially modest symptoms.\n"
     "• Avoid topical corticosteroids unless directed by ophthalmology."),
    ("REFERENCES", "info", "AAO EyeWiki: Chemical Eye Injury.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Open Globe Injury")] = [
    ("01 — DEFINITION", "info", "A full-thickness wound of the cornea or sclera caused by penetrating trauma or blunt trauma resulting in globe rupture."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Severe pain and reduced vision.\n"
     "• Irregular or peaked pupil.\n"
     "• Visible wound or protruding intraocular tissue.\n"
     "• Hyphema or abnormal anterior chamber depth.\n"
     "• Positive Seidel sign when tested appropriately."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess general trauma and stabilize airway, breathing, and circulation.\n"
     "• Place a rigid eye shield without pressure on the globe.\n"
     "• Keep the patient NPO.\n"
     "• Provide systemic analgesia and antiemetics as required.\n"
     "• Obtain immediate ophthalmology consultation.\n"
     "• Check tetanus immunization status."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. PROTECTION AND PREPARATION[/color]\n"
     "• Prevent rubbing, compression, and further trauma. Avoid manipulation of the eye.\n"
     "• Obtain urgent surgical assessment.\n"
     "• CT orbits may be indicated to assess the injury or identify an intraocular foreign body.\n\n"
     "[color=#1E3A8A]B. ANTIBIOTICS[/color]\n"
     "• Systemic broad-spectrum IV antibiotics are generally indicated (e.g., IV vancomycin plus a 3rd/4th-gen cephalosporin).\n"
     "• Select exact agents according to local protocols."),
    ("05 — WARNINGS", "danger", 
     "• Do not perform tonometry, ocular ultrasound, pressure patching, or forced eyelid examination.\n"
     "• Do not remove an embedded object.\n"
     "• Avoid MRI if a metallic foreign body is suspected.\n"
     "• Do not delay urgent surgical repair to complete investigations or antibiotic administration."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate transfer/admission for ophthalmic surgical management."),
    ("07 — CLINICAL PEARLS", "info", 
     "• A seemingly small wound may conceal a serious globe injury.\n"
     "• The shield must not exert pressure.\n"
     "• Definitive repair is time-critical."),
    ("REFERENCES", "info", "AAO EyeWiki: Pre-Ophthalmologist Management of Eye Trauma.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Angle-Closure Glaucoma")] = [
    ("01 — DEFINITION", "info", "Sudden obstruction of aqueous humor outflow causing a rapid rise in intraocular pressure (IOP), potentially resulting in permanent optic nerve damage."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Severe unilateral eye pain and redness.\n"
     "• Blurred vision or colored halos around lights.\n"
     "• Headache, nausea, and vomiting.\n"
     "• Hazy cornea and a mid-dilated, poorly reactive pupil.\n"
     "• Markedly elevated IOP."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Arrange immediate ophthalmology consultation.\n"
     "• Assess visual acuity, pupils, and IOP if safe and appropriately equipped.\n"
     "• Begin pressure-lowering treatment according to local protocol.\n"
     "• Check for contraindications to beta-blockers and systemic carbonic anhydrase inhibitors."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. ACETAZOLAMIDE[/color]\n"
     "• 500 mg IV or orally as an initial dose, if appropriate.\n"
     "• Monitor renal function, electrolytes, and clinical response.\n\n"
     "[color=#1E3A8A]B. TOPICAL PRESSURE-LOWERING AGENTS[/color]\n"
     "• Timolol 0.5%: 1 drop in affected eye.\n"
     "• Brimonidine 0.2%: 1 drop in affected eye.\n"
     "• Topical carbonic anhydrase inhibitor may be used.\n\n"
     "[color=#1E3A8A]C. DEFINITIVE TREATMENT[/color]\n"
     "• Laser peripheral iridotomy is commonly the definitive treatment.\n"
     "• Pilocarpine may be considered after IOP begins to fall."),
    ("05 — WARNINGS", "danger", 
     "• Avoid Acetazolamide in significant renal disease or severe electrolyte abnormalities.\n"
     "• Check for asthma, bradycardia, heart block, or decompensated heart failure before timolol."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency ophthalmology management and usually hospital-based treatment until IOP is controlled."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Painful red eye with blurred vision, halos, and vomiting is highly concerning.\n"
     "• Treatment must not be delayed.\n"
     "• Definitive treatment is usually procedural."),
    ("REFERENCES", "info", "AAO: Acute Angle Closure.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Orbital Compartment Syndrome")] = [
    ("01 — DEFINITION", "info", "A rapid increase in orbital pressure, commonly caused by retrobulbar hemorrhage after trauma or surgery, compromising optic nerve and retinal perfusion."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Acute proptosis and tense eyelids.\n"
     "• Severe orbital pain.\n"
     "• Reduced vision or color vision.\n"
     "• Restricted eye movements.\n"
     "• Relative afferent pupillary defect (RAPD).\n"
     "• Elevated IOP when safely measured."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Recognize the condition clinically.\n"
     "• Call ophthalmology and experienced emergency/trauma clinicians immediately.\n"
     "• Assess visual acuity, pupils, eye movements, and IOP if safe.\n"
     "• Prepare for immediate orbital decompression when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. EMERGENCY DECOMPRESSION[/color]\n"
     "• Lateral canthotomy with inferior cantholysis is the emergency decompression procedure.\n"
     "• It must be performed immediately by a trained clinician when indicated.\n"
     "• Do not wait for CT or ophthalmology arrival if the diagnosis is clear and vision is threatened.\n\n"
     "[color=#1E3A8A]B. ADDITIONAL MANAGEMENT[/color]\n"
     "• Urgent ophthalmology assessment after decompression.\n"
     "• Treat the cause, such as retrobulbar hemorrhage.\n"
     "• Reassess vision, pupils, IOP, and orbital tension."),
    ("05 — WARNINGS", "danger", 
     "• Do not perform decompression when open globe injury is suspected without specialist direction.\n"
     "• Imaging must not delay indicated decompression."),
    ("06 — DISPOSITION", "warning", 
     "• Emergency transfer/admission for ophthalmology and surgical management."),
    ("07 — CLINICAL PEARLS", "info", 
     "• Proptosis, tight lids, visual decline, and restricted movements after trauma strongly suggest this syndrome.\n"
     "• Time to intervention is critical."),
    ("REFERENCES", "info", "AAO EyeWiki: Orbital Compartment Syndrome.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Central Retinal Artery Occlusion (CRAO)")] = [
    ("01 — DEFINITION", "info", "Acute obstruction of the central retinal artery causing sudden retinal ischemia and usually painless monocular visual loss. It is an ocular and systemic vascular emergency."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Sudden, painless loss of vision in one eye.\n"
     "• Marked reduction in visual acuity.\n"
     "• Relative afferent pupillary defect.\n"
     "• Retinal whitening and a cherry-red spot may be seen on fundus examination."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Activate an emergency stroke pathway and arrange immediate transfer to a stroke-capable center.\n"
     "• Establish exact symptom onset or last-known-well time.\n"
     "• Assess neurological status, vital signs, and blood glucose.\n"
     "• Obtain urgent ophthalmology and stroke-team consultation.\n"
     "• Evaluate for carotid, cardiac, and other embolic sources."),
    ("04 — INVESTIGATIONS", "info", 
     "• Urgent stroke-directed brain and vascular imaging.\n"
     "• ECG and cardiovascular assessment.\n"
     "• CBC, glucose, renal function.\n"
     "• Assess for giant cell arteritis (ESR, CRP, platelets) if age >50 and clinically suspected."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]A. STROKE-CENTER MANAGEMENT[/color]\n"
     "• Consider eligibility for acute reperfusion treatment under the current stroke protocol.\n"
     "• Address vascular risk factors and secondary stroke prevention.\n\n"
     "[color=#1E3A8A]B. SUSPECTED GIANT CELL ARTERITIS[/color]\n"
     "• Urgent systemic corticosteroid treatment is required to protect the fellow eye.\n"
     "• Do not delay treatment while waiting for biopsy."),
    ("06 — WARNINGS", "danger", 
     "• Do not delay transfer for outpatient ophthalmology review.\n"
     "• Routine ocular massage, anterior chamber paracentesis, and unproven pressure-lowering methods should not delay stroke evaluation."),
    ("07 — DISPOSITION", "warning", 
     "• Immediate stroke-center evaluation and urgent ophthalmology assessment."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Sudden painless monocular visual loss should be treated as a vascular emergency.\n"
     "• CRAO is associated with increased risk of cerebral and cardiovascular events."),
    ("REFERENCES", "info", "AAO: Retinal and Ophthalmic Artery Occlusions.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Retinal Detachment")] = [
    ("01 — DEFINITION", "info", "Separation of the neurosensory retina from the underlying retinal pigment epithelium. Delayed treatment may result in permanent visual loss."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Sudden onset of flashes of light.\n"
     "• New or increasing floaters.\n"
     "• A curtain or shadow across the visual field.\n"
     "• Blurred or reduced vision.\n"
     "• Usually painless.\n\n"
     "[color=#991B1B]RISK FACTORS: High myopia, previous cataract/retinal surgery, ocular trauma, previous retinal detachment.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess and document visual acuity in each eye.\n"
     "• Ask about flashes, floaters, field loss, and symptom onset.\n"
     "• Arrange immediate or same-day ophthalmology assessment.\n"
     "• Avoid delays for routine investigations when retinal detachment is suspected."),
    ("04 — INVESTIGATIONS", "info", 
     "• Dilated retinal examination by an appropriately trained clinician.\n"
     "• Ocular ultrasound may assist when the fundus cannot be visualized (provided open globe excluded).\n"
     "• OCT or other retinal imaging by ophthalmology."),
    ("05 — TREATMENT", "info", 
     "[color=#1E3A8A]DEFINITIVE MANAGEMENT[/color]\n"
     "• Retinal tears may be treated with laser photocoagulation or cryotherapy.\n"
     "• Retinal detachment may require pneumatic retinopexy, scleral buckling, or vitrectomy.\n"
     "• Choice of procedure depends on detachment characteristics and specialist assessment.\n\n"
     "• Arrange urgent retinal specialist review.\n"
     "• Provide clear instructions to return immediately if vision deteriorates."),
    ("06 — WARNINGS", "danger", 
     "• Do not reassure patients with a new curtain-like shadow or sudden increase in floaters without adequate retinal assessment."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent ophthalmology referral. Suspected acute retinal detachment requires same-day assessment."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Retinal detachment is usually painless.\n"
     "• New flashes and floaters may indicate a retinal tear before detachment occurs.\n"
     "• Early treatment can preserve vision."),
    ("REFERENCES", "info", "NHS: Detached Retina; Merck Manual: Retinal Detachment.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Endophthalmitis")] = [
    ("01 — DEFINITION", "info", "Severe intraocular infection involving the vitreous and/or aqueous, commonly following eye surgery, intravitreal injection, penetrating trauma, or hematogenous spread."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Severe eye pain and redness.\n"
     "• Rapidly declining vision.\n"
     "• Photophobia.\n"
     "• Hypopyon.\n"
     "• Marked intraocular inflammation.\n"
     "• Recent eye surgery, injection, or penetrating injury."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Obtain immediate ophthalmology consultation.\n"
     "• Assess visual acuity and recent ocular procedures or trauma.\n"
     "• Arrange urgent ophthalmic examination and intraocular sampling when indicated.\n"
     "• Do not delay definitive treatment for routine laboratory investigations."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. INTRAVITREAL ANTIBIOTICS[/color]\n"
     "• Vancomycin 1 mg/0.1 mL intravitreal.\n"
     "• Plus ceftazidime 2.25 mg/0.1 mL intravitreal.\n"
     "• Administered by an appropriately trained ophthalmologist.\n"
     "• Severe cases may require urgent vitrectomy.\n\n"
     "[color=#1E3A8A]B. SYSTEMIC TREATMENT[/color]\n"
     "• Consider systemic antibiotics when endogenous endophthalmitis is suspected."),
    ("05 — WARNINGS", "danger", 
     "• Intravitreal medications require exact preparation and specialist administration. Incorrect concentration may cause severe ocular injury."),
    ("06 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Severe postoperative inflammation.\n"
     "• Toxic anterior segment syndrome.\n"
     "• Acute uveitis.\n"
     "• Severe microbial keratitis."),
    ("07 — DISPOSITION", "warning", 
     "• Immediate ophthalmic surgical assessment; hospital admission is commonly required."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Pain and rapidly worsening vision after eye surgery or injection are major warning signs.\n"
     "• Treatment delay can cause irreversible blindness."),
    ("REFERENCES", "info", "WHO: AWaRe Antibiotic Book; AAO EyeWiki.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Orbital Cellulitis")] = [
    ("01 — DEFINITION", "info", "A potentially sight- and life-threatening infection of the orbital tissues posterior to the orbital septum, often associated with sinusitis."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Fever and eyelid swelling.\n"
     "• Proptosis.\n"
     "• Painful or restricted eye movements.\n"
     "• Reduced visual acuity or color vision.\n"
     "• Diplopia.\n"
     "• RAPD or neurological signs in severe cases.\n\n"
     "[color=#991B1B]IMPORTANT: Preseptal cellulitis usually does not cause proptosis, restricted eye movements, or visual impairment.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity, pupils, color vision, and eye movements.\n"
     "• Check vital signs and signs of sepsis.\n"
     "• Obtain urgent ophthalmology and ENT consultation.\n"
     "• Admit the patient and keep NPO until the need for surgery is clarified.\n"
     "• Arrange contrast-enhanced CT of the orbits and sinuses when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. IV ANTIBIOTICS[/color]\n"
     "• Ceftriaxone 50 mg/kg IV every 24 hours (Pediatrics).\n"
     "• Third-generation cephalosporin-based regimen (Adults).\n"
     "• Add MRSA coverage (e.g., vancomycin) if suspected.\n\n"
     "[color=#1E3A8A]B. SURGICAL MANAGEMENT[/color]\n"
     "• Drainage may be required for an orbital or subperiosteal abscess, visual compromise, or failure to respond to IV antibiotics."),
    ("05 — WARNINGS", "danger", 
     "• Do not use outpatient oral antibiotics alone for suspected orbital cellulitis.\n"
     "• Do not delay treatment in an unstable patient for imaging."),
    ("06 — INVESTIGATIONS", "info", 
     "• CBC, CRP, blood cultures when indicated.\n"
     "• Contrast-enhanced CT of the orbits and sinuses; MRI if intracranial involvement suspected."),
    ("07 — DISPOSITION", "warning", 
     "• Hospital admission is required. ICU care or tertiary transfer may be necessary for visual compromise or intracranial complications."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Painful or restricted eye movements and proptosis are important warning signs.\n"
     "• Orbital cellulitis can lead to blindness, cavernous sinus thrombosis, meningitis, or intracranial abscess."),
    ("REFERENCES", "info", "Royal Children's Hospital Melbourne: Periorbital and Orbital Cellulitis.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Infectious Keratitis and Corneal Ulcer")] = [
    ("01 — DEFINITION", "info", "Infection of the cornea caused by bacteria, fungi, viruses, or Acanthamoeba. Corneal ulceration can progress rapidly and cause scarring, perforation, and permanent visual loss."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Painful red eye.\n"
     "• Photophobia and tearing.\n"
     "• Reduced visual acuity.\n"
     "• Corneal opacity or infiltrate.\n"
     "• Fluorescein-positive epithelial defect.\n"
     "• Contact lens use, ocular trauma, or topical steroid use may be risk factors.\n\n"
     "[color=#991B1B]RED FLAGS: Central or large corneal ulcer, rapid progression, reduced vision, corneal thinning, contact lens use with painful red eye.[/color]"),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess and document visual acuity.\n"
     "• Examine the cornea and perform fluorescein staining when safe.\n"
     "• Arrange urgent ophthalmology assessment.\n"
     "• Stop contact lens use.\n"
     "• Obtain corneal scraping and cultures when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. TOPICAL ANTIBIOTICS[/color]\n"
     "• Moxifloxacin 0.5% may be used for selected bacterial ulcers.\n"
     "• Severe or vision-threatening ulcers may require intensive fortified preparations.\n"
     "• Adjust treatment according to culture results.\n\n"
     "[color=#1E3A8A]B. SPECIAL CONSIDERATIONS[/color]\n"
     "• Fungal keratitis requires specialist-directed antifungal therapy.\n"
     "• Herpetic keratitis requires appropriate antiviral management.\n"
     "• Acanthamoeba keratitis requires specialist treatment."),
    ("05 — WARNINGS", "danger", 
     "• Do not delay specialist assessment for a central ulcer or reduced vision.\n"
     "• Avoid topical corticosteroids unless prescribed by ophthalmology."),
    ("06 — DIFFERENTIAL DIAGNOSIS", "info", 
     "• Corneal abrasion.\n"
     "• Anterior uveitis.\n"
     "• Acute angle-closure glaucoma.\n"
     "• Conjunctivitis.\n"
     "• Scleritis."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent ophthalmology review. Admit for severe ulcers, corneal thinning, or suspected perforation."),
    ("08 — CLINICAL PEARLS", "info", 
     "• A corneal infiltrate with an epithelial defect suggests microbial keratitis.\n"
     "• Contact lens wear is an important risk factor.\n"
     "• A painful red eye with reduced vision is not simple conjunctivitis."),
    ("REFERENCES", "info", "AAO: Bacterial Keratitis Preferred Practice Pattern.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Hyphema")] = [
    ("01 — DEFINITION", "info", "Blood within the anterior chamber of the eye, usually following blunt trauma that damages iris or ciliary body vessels. It may increase intraocular pressure and threaten vision."),
    ("02 — CLINICAL PRESENTATION", "info", 
     "• Blurred or reduced vision after eye trauma.\n"
     "• Visible blood in the anterior chamber.\n"
     "• Eye pain and photophobia.\n"
     "• Elevated IOP in some cases.\n"
     "• Severe hyphema may obscure the pupil."),
    ("03 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity and associated ocular or head trauma.\n"
     "• Place a rigid eye shield without pressure.\n"
     "• Elevate the head approximately 30–45 degrees when medically appropriate.\n"
     "• Arrange urgent, same-day ophthalmology assessment.\n"
     "• Avoid strenuous activity and prevent further eye injury."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]A. SUPPORTIVE MANAGEMENT[/color]\n"
     "• Protective rigid eye shield.\n"
     "• Head elevation and restricted physical activity.\n"
     "• Paracetamol for pain when appropriate.\n"
     "• Antiemetics if nausea or vomiting could increase pressure.\n\n"
     "[color=#1E3A8A]B. OPHTHALMOLOGY-DIRECTED TREATMENT[/color]\n"
     "• Topical corticosteroids may be prescribed.\n"
     "• Cycloplegic drops may be used.\n"
     "• Elevated IOP may require topical pressure-lowering medications."),
    ("05 — WARNINGS", "danger", 
     "• Exclude open globe injury before measuring IOP.\n"
     "• Avoid aspirin and NSAIDs for routine analgesia.\n"
     "• Patients with sickle cell disease or trait require particular caution."),
    ("06 — INVESTIGATIONS", "info", 
     "• Visual acuity and pupil examination.\n"
     "• Slit-lamp examination when available.\n"
     "• IOP measurement only after open globe injury has been excluded."),
    ("07 — DISPOSITION", "warning", 
     "• Urgent ophthalmology assessment for all traumatic hyphema. Admission may be required for significant bleeding or unreliable follow-up."),
    ("08 — CLINICAL PEARLS", "info", 
     "• Rebleeding often occurs during the first several days.\n"
     "• A small hyphema can still cause elevated IOP.\n"
     "• Worsening vision or increasing pain requires immediate reassessment."),
    ("REFERENCES", "info", "AAO EyeWiki: Pre-Ophthalmologist Management of Eye Trauma.")
]


# ==================== NEW OPHTHALMOLOGY TOPICS (11-20) ====================

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Corneal Abrasion")] = [
    ("01 — RECOGNIZE", "info", 
     "Corneal abrasion is a defect in the corneal epithelium, commonly caused by fingernails, dust, foreign bodies, contact lenses, or trauma.\n"
     "Typical symptoms: Sudden eye pain, foreign-body sensation, tearing, redness, photophobia. Pain may worsen with blinking. Blurred vision if central cornea involved.\n\n"
     "[color=#991B1B]Red flags:[/color] Reduced visual acuity. Contact lens use with pain or corneal opacity. White corneal infiltrate, hypopyon, or purulent discharge. Suspected penetrating injury, irregular pupil, or positive Seidel test. Severe pain, marked photophobia, or worsening despite treatment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess and document visual acuity in each eye separately before treatment, if safe.\n"
     "• Obtain mechanism of injury, time of onset, contact lens use, chemical exposure, previous ocular disease.\n"
     "• Examine pupils, eye movements, external eye.\n"
     "• Use fluorescein staining and blue light to identify epithelial defect, provided open-globe injury is not suspected.\n"
     "• Evert the upper eyelid when appropriate to look for retained foreign body.\n"
     "• [color=#991B1B]If open-globe injury suspected: stop manipulation, avoid tonometry and ocular ultrasound, place rigid eye shield without pressure, keep NPO, arrange immediate ophthalmology transfer.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Visual acuity, pupils, and relative afferent pupillary defect assessment.\n"
     "• Fluorescein staining to identify epithelial defect.\n"
     "• Slit-lamp examination, if available, to assess defect size, depth, infiltrates, anterior chamber.\n"
     "• Seidel testing only when clinically appropriate and open-globe injury is not strongly suspected.\n"
     "• Corneal scraping and microbiological studies are not routinely required for simple abrasion but may be needed if infection/ulceration suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed; max 3,000 mg/day for routine unsupervised adult use.\n"
     "• Alternatively, ibuprofen 200–400 mg orally every 6–8 hours with food, if no contraindications.\n"
     "• [color=#991B1B]Do NOT dispense topical anesthetic drops for unsupervised home use. Prolonged/inappropriate use can damage corneal epithelium and delay healing.[/color]\n\n"
     "[color=#1E3A8A]2. Topical Antibiotic Prophylaxis[/color]\n"
     "• Erythromycin ophthalmic ointment 0.5%: ~1 cm ribbon to affected eye four times daily for 3–5 days.\n"
     "• For contact lens-associated abrasions: use appropriate topical antipseudomonal agent (e.g., ciprofloxacin 0.3% or ofloxacin 0.3%) per local protocol.\n"
     "• [color=#991B1B]Antibiotic selection/duration depend on injury type and local guidance. A painful red eye with corneal infiltrate/opacity should be managed as possible microbial keratitis, not simple abrasion.[/color]\n\n"
     "[color=#1E3A8A]3. Lubrication[/color]\n"
     "• Preservative-free artificial tears: 1–2 drops as needed, often four to six times daily.\n"
     "• [color=#991B1B]Do NOT use steroid-containing eye drops unless specifically prescribed by an ophthalmologist.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Most uncomplicated abrasions heal within 24–72 hours.\n"
     "• Do NOT routinely patch the eye.\n"
     "• Cycloplegic drops may be considered by a clinician for significant photophobia/ciliary spasm after appropriate assessment.\n"
     "• Reassess if pain or vision does not improve within 24 hours.\n"
     "• Urgent ophthalmology assessment required for large/central defects, suspected infection, contact lens-associated defects, recurrent erosions, or any red flags."),
    ("06 — DISPOSITION", "warning", 
     "• Discharge may be appropriate when: Abrasion is uncomplicated. Visual acuity reassuring. No evidence of infection or penetrating injury. Patient can follow treatment and return for review.\n"
     "• Urgent referral: Reduced vision, corneal infiltrate, suspected ulcer, contact lens-associated painful red eye, persistent symptoms, or suspected open-globe injury."),
    ("REFERENCES", "info", "AAO Corneal and External Disease Guidance; College of Optometrists Corneal Abrasion Guideline; ACEP Consensus Guidance on Topical Anesthetic Use.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Corneal and Intraocular Foreign Body")] = [
    ("01 — RECOGNIZE", "info", 
     "A foreign body may remain on the conjunctiva or corneal surface, become embedded in the cornea, or penetrate the globe and enter the eye.\n\n"
     "[color=#1E3A8A]High-risk mechanisms:[/color] Hammering metal on metal, grinding, drilling, explosions, high-velocity projectiles. Sharp objects, glass, penetrating trauma. Organic material (increased infection risk).\n\n"
     "Symptoms: Foreign-body sensation, tearing, redness, photophobia, pain. Visible foreign material or corneal rust ring. Reduced vision, irregular pupil, shallow anterior chamber, or suspected entry wound in penetrating injury.\n\n"
     "[color=#991B1B]Red flags:[/color] High-velocity mechanism. Protruding or deeply embedded object. Reduced visual acuity, abnormal pupil, hyphema, or positive Seidel sign. Severe pain or signs of endophthalmitis after penetrating trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity without applying pressure to the globe.\n"
     "• Ask specifically about high-velocity metal work, sharp trauma, and protective eyewear.\n"
     "• [color=#991B1B]If intraocular foreign body or open-globe injury possible: Do NOT remove object. Do NOT press, patch, or manipulate eye. Do NOT perform tonometry or ocular ultrasound. Place rigid eye shield without pressure. Keep NPO and arrange immediate ophthalmology transfer.[/color]\n"
     "• Provide analgesia and antiemetic treatment when needed to reduce pain, vomiting, and Valsalva-related pressure.\n"
     "• Update tetanus prophylaxis when indicated by injury and immunization history."),
    ("03 — INVESTIGATIONS", "info", 
     "• Visual acuity, pupils, and external examination, provided this does not delay transfer or place pressure on eye.\n"
     "• Slit-lamp examination for superficial foreign body when penetrating injury has been excluded.\n"
     "• Non-contrast thin-cut CT of orbits when intraocular foreign body or open-globe injury is suspected.\n"
     "• [color=#991B1B]MRI is contraindicated until a potentially metallic foreign body has been excluded. Do NOT use ocular ultrasound when open-globe injury is suspected before specialist assessment.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Superficial Corneal Foreign Body[/color]\n"
     "• Removal may be performed by a trained clinician only after confirming injury is superficial and open-globe injury is not suspected.\n"
     "• Use appropriate magnification, topical anesthetic for examination/procedure, and sterile instruments per local protocol.\n"
     "• [color=#991B1B]Do NOT attempt removal of a deeply embedded object or one near the visual axis without appropriate expertise. Never use force or manipulate an object that may penetrate the globe.[/color]\n\n"
     "[color=#1E3A8A]2. Antibiotic Treatment After Superficial Removal[/color]\n"
     "• Erythromycin ophthalmic ointment 0.5% ~1 cm ribbon four times daily for 3–5 days, or alternative topical antibiotic per local guidance.\n"
     "• For contact lens-associated injury: select an antipseudomonal ophthalmic antibiotic (e.g., ciprofloxacin 0.3% or ofloxacin 0.3%).\n\n"
     "[color=#1E3A8A]3. Suspected Intraocular Foreign Body or Open Globe[/color]\n"
     "• Immediate ophthalmology consultation and transfer for surgical assessment.\n"
     "• Systemic broad-spectrum antibiotics generally initiated in hospital per open-globe/IOFB protocol.\n"
     "• Provide tetanus prophylaxis as indicated.\n"
     "• Maintain NPO status and avoid pressure on the eye.\n"
     "• Surgical closure and foreign-body management determined by ophthalmic surgeon."),
    ("05 — WARNINGS", "danger", 
     "• Do NOT prescribe a routine superficial-abrasion treatment plan for a suspected intraocular foreign body.\n"
     "• A normal-looking external eye or a negative initial scan does not completely exclude serious injury when mechanism and clinical findings remain concerning."),
    ("06 — DISPOSITION", "warning", 
     "• Superficial and uncomplicated: discharge may be appropriate after safe removal, reassuring vision, and clear follow-up instructions.\n"
     "• Deep, central, difficult-to-remove, or infected: urgent ophthalmology review.\n"
     "• Possible penetrating or intraocular injury: immediate transfer to an ophthalmic surgical service."),
    ("REFERENCES", "info", "AAO Management of Intraocular Foreign Bodies; AAO Open Globe Injury Assessment and Preoperative Management; Defence Medical Services Globe Injury Guideline.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Anterior Uveitis (Iritis)")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute anterior uveitis is inflammation of the iris and ciliary body. May be idiopathic or associated with autoimmune disease, infection, trauma, or other ocular pathology.\n"
     "• Painful red eye, often with ciliary flush.\n"
     "• Photophobia, including consensual photophobia when light directed at unaffected eye causes pain in affected eye.\n"
     "• Blurred vision. Small or irregular pupil may occur.\n\n"
     "[color=#991B1B]Red flags:[/color] Markedly reduced vision. Severe pain, corneal opacity, or elevated intraocular pressure. Hypopyon or suspected endophthalmitis. History of ocular surgery, injection, penetrating trauma, or possible herpetic eye disease."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity, pupils, and pattern of redness.\n"
     "• Obtain history of autoimmune disease, inflammatory back pain, previous episodes, trauma, infection, ocular surgery.\n"
     "• Arrange same-day ophthalmology assessment for suspected acute anterior uveitis.\n"
     "• Exclude acute angle-closure glaucoma, microbial keratitis, and endophthalmitis.\n"
     "• [color=#991B1B]Do NOT start topical corticosteroids without appropriate ophthalmology guidance, especially before excluding corneal infection.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Visual acuity and pupil examination.\n"
     "• Slit-lamp examination to identify anterior chamber cells and flare, keratic precipitates, posterior synechiae.\n"
     "• Intraocular pressure measurement only when open-globe injury is not suspected and examination is appropriate.\n"
     "• Additional laboratory tests/imaging guided by clinical history, recurrence, systemic symptoms, ophthalmologist assessment."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Topical Corticosteroid[/color]\n"
     "• Prednisolone acetate 1% ophthalmic drops may be prescribed by an ophthalmologist, with frequency determined by inflammatory severity.\n"
     "• [color=#991B1B]Topical steroids can worsen untreated herpetic or microbial keratitis and may increase intraocular pressure. Do NOT use as empirical treatment for undiagnosed red eye.[/color]\n\n"
     "[color=#1E3A8A]2. Cycloplegic or Mydriatic Drops[/color]\n"
     "• Cyclopentolate 1%: commonly 1 drop in affected eye, frequency determined by ophthalmologist.\n"
     "• May relieve ciliary spasm and reduce risk of posterior synechiae.\n"
     "• [color=#991B1B]Confirm clinical situation is appropriate before using pupil-dilating medication, especially if angle closure is a concern.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within appropriate daily maximum."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat underlying cause when identified, including infection or systemic inflammatory disease.\n"
     "• Ophthalmology-directed topical anti-inflammatory treatment and cycloplegia are common for noninfectious anterior uveitis.\n"
     "• Recurrent or bilateral disease may require systemic evaluation and specialist follow-up."),
    ("06 — DISPOSITION", "warning", 
     "• Same-day ophthalmology assessment generally recommended.\n"
     "• Immediate emergency referral required for severe visual loss, suspected endophthalmitis, marked pressure elevation, or rapidly progressive symptoms."),
    ("REFERENCES", "info", "AAO EyeWiki Acute Anterior Uveitis; AAO Guidance on Inflammatory Eye Disease and Topical Corticosteroid Safety.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Herpes Zoster Ophthalmicus")] = [
    ("01 — RECOGNIZE", "info", 
     "Herpes zoster ophthalmicus (HZO) occurs when varicella-zoster virus reactivates in the ophthalmic division of the trigeminal nerve (V1).\n"
     "• Unilateral painful vesicular rash involving forehead, scalp, or upper eyelid.\n"
     "• Burning, tingling, or neuropathic pain.\n"
     "• Red eye, tearing, photophobia, or blurred vision if ocular structures involved.\n"
     "• Vesicles on tip or side of nose (Hutchinson sign) increase concern for ocular involvement.\n\n"
     "[color=#991B1B]Red flags:[/color] Reduced vision, severe eye pain, photophobia, or corneal changes. Immunocompromised status or disseminated rash. Ophthalmoplegia, proptosis, severe headache, confusion, or other neurological signs. Suspected keratitis, uveitis, retinitis, or optic nerve involvement."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity, pupils, eye movements, and distribution of rash.\n"
     "• Begin systemic antiviral treatment promptly when HZO suspected; most effective when started within 72 hours of rash onset.\n"
     "• Arrange urgent ophthalmology assessment, especially if ocular symptoms or signs present.\n"
     "• Provide appropriate analgesia and advise against touching/scratching lesions.\n"
     "• Use standard infection-control precautions and cover lesions when feasible."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical diagnosis is often sufficient for typical cases.\n"
     "• Visual acuity and ocular examination are essential.\n"
     "• Slit-lamp examination and fluorescein staining indicated when ocular involvement suspected.\n"
     "• Renal function should be assessed when clinically indicated to guide antiviral dosing.\n"
     "• Atypical, disseminated, or immunocompromised cases may require additional investigations and specialist input."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Oral Antiviral Therapy — Adults[/color]\n"
     "• Valacyclovir 1,000 mg orally three times daily for 7 days.\n"
     "• Alternatives: Acyclovir 800 mg orally five times daily for 7–10 days or Famciclovir 500 mg orally three times daily for 7 days.\n"
     "• Start as early as possible, ideally within 72 hours of rash onset.\n"
     "• [color=#991B1B]Severe disease, disseminated infection, immunocompromise, or neurological involvement may require hospital admission and IV therapy.[/color]\n\n"
     "[color=#1E3A8A]2. Intravenous Antiviral Therapy for Severe Disease[/color]\n"
     "• IV acyclovir may be indicated for severe, disseminated, neurological, or selected immunocompromised cases. Common adult regimen: 10 mg/kg IV every 8 hours, adjusted for renal function.\n"
     "• [color=#991B1B]IV acyclovir can cause crystal-associated kidney injury and neurotoxicity, particularly when renal dosing or hydration is inadequate. Involve specialist for severe disease.[/color]\n\n"
     "[color=#1E3A8A]3. Ocular Treatment[/color]\n"
     "• Preservative-free lubricants may help surface discomfort.\n"
     "• Specific antiviral eye treatment, topical corticosteroids, and IOP-lowering medication depend on ocular complication and should be directed by ophthalmology.\n"
     "• [color=#991B1B]Do NOT initiate topical corticosteroids without ophthalmology supervision.[/color]\n\n"
     "[color=#1E3A8A]4. Pain Control[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, subject to patient-specific maximum limits.\n"
     "• Neuropathic pain treatment may be considered when indicated, according to local guidance."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Complete indicated systemic antiviral course.\n"
     "• Treat keratitis, uveitis, retinitis, or raised intraocular pressure under ophthalmology guidance.\n"
     "• Monitor for delayed ocular complications and postherpetic neuralgia.\n"
     "• Consider specialist input for immunocompromised patients or suspected neurological involvement."),
    ("06 — DISPOSITION", "warning", 
     "• Same-day ophthalmology review recommended when ocular involvement suspected.\n"
     "• Admit or arrange urgent specialist assessment for severe ocular disease, disseminated infection, neurological signs, or inability to take oral treatment."),
    ("REFERENCES", "info", "AAO Herpes Zoster Ophthalmicus; NIH Clinical Guidelines Varicella-Zoster Virus Disease; CMAJ Herpes Zoster Ophthalmicus.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Scleritis")] = [
    ("01 — RECOGNIZE", "info", 
     "Scleritis is a potentially sight-threatening inflammation of the sclera. May be associated with systemic autoimmune disease, vasculitis, infection, or previous ocular surgery.\n"
     "• Severe, deep, boring eye pain, sometimes radiating to face or head. Pain may worsen at night or with eye movement.\n"
     "• Deep redness with a violaceous hue.\n"
     "• Possible photophobia, tearing, and reduced vision.\n\n"
     "[color=#991B1B]Red flags:[/color] Reduced visual acuity. Severe/rapidly worsening pain. Corneal involvement, scleral thinning, or suspected necrotizing scleritis. Previous eye surgery, trauma, or possible infectious disease. Systemic features of vasculitis (skin lesions, joint symptoms, respiratory symptoms, renal abnormalities)."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity, pupils, eye movements, pain severity, appearance of sclera.\n"
     "• Arrange urgent same-day ophthalmology assessment.\n"
     "• Distinguish scleritis from episcleritis, microbial keratitis, acute angle-closure glaucoma, anterior uveitis.\n"
     "• Ask about rheumatoid arthritis, systemic vasculitis, autoimmune disease, infection, trauma, ocular surgery.\n"
     "• Do NOT delay referral while attempting empirical topical treatment."),
    ("03 — INVESTIGATIONS", "info", 
     "• Visual acuity and complete ophthalmic examination.\n"
     "• Slit-lamp examination to assess scleral inflammation and associated corneal or intraocular disease.\n"
     "• Additional lab investigations guided by clinical suspicion may include CBC, renal function, urinalysis, inflammatory markers, autoimmune testing.\n"
     "• Microbiological assessment may be needed when infectious scleritis suspected, particularly after surgery or trauma."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Analgesia and Initial Supportive Care[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within patient-specific daily limits.\n"
     "• [color=#991B1B]Severe pain may indicate deeper inflammation or complications. Do not allow symptom relief to delay assessment.[/color]\n\n"
     "[color=#1E3A8A]2. Systemic Anti-Inflammatory Treatment[/color]\n"
     "• Oral NSAIDs may be used for selected noninfectious cases under clinician/ophthalmologist direction, provided no contraindications.\n"
     "• More severe disease may require systemic corticosteroids or immunosuppressive therapy prescribed by relevant specialist.\n"
     "• [color=#991B1B]Do NOT start systemic corticosteroids before considering infectious scleritis and other important contraindications. Topical corticosteroids alone are often insufficient for significant scleritis and should not be started empirically in undiagnosed painful red eye.[/color]\n\n"
     "[color=#1E3A8A]3. Suspected Infectious Scleritis[/color]\n"
     "• Urgent ophthalmology assessment and microbiological investigation where indicated.\n"
     "• Antimicrobial therapy selected according to suspected organism, exposure history, cultures, specialist advice.\n"
     "• Surgical debridement may be required in selected cases."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Determine whether condition is infectious or noninfectious.\n"
     "• Treat associated autoimmune or systemic disease where identified.\n"
     "• Ophthalmology-directed anti-inflammatory or antimicrobial treatment depends on subtype and severity.\n"
     "• Monitor for corneal complications, scleral thinning, perforation, vision loss."),
    ("06 — DISPOSITION", "warning", 
     "• Same-day ophthalmology assessment required for suspected acute scleritis.\n"
     "• Emergency referral or admission may be necessary for reduced vision, necrotizing disease, suspected infection, posterior scleritis, or systemic vasculitis."),
    ("REFERENCES", "info", "AAO Scleritis Clinical Guidance; AAO EyeWiki Scleritis; Specialist Ophthalmology Guidance on Infectious/Noninfectious Scleritis.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Central Retinal Vein Occlusion (CRVO)")] = [
    ("01 — RECOGNIZE", "info", 
     "CRVO is an obstruction of the central retinal vein that causes retinal hemorrhage, venous congestion, and variable visual impairment.\n"
     "• Sudden, painless blurring or loss of vision in one eye.\n"
     "• Visual acuity may range from mildly reduced to profound loss.\n"
     "• Fundoscopy may show dilated tortuous retinal veins, widespread retinal hemorrhages, cotton-wool spots, optic disc swelling.\n"
     "• Risk factors: hypertension, diabetes, glaucoma, dyslipidemia, increasing age.\n\n"
     "[color=#991B1B]Red flags:[/color] Severe visual loss. Suspected associated retinal arterial occlusion or another acute vascular event. Ocular pain or red eye developing later (may indicate neovascular glaucoma). Young patients or atypical cases requiring evaluation for selected systemic or hematologic causes."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Record visual acuity in each eye separately.\n"
     "• Assess pupils, visual fields, and presence of relative afferent pupillary defect.\n"
     "• Arrange urgent ophthalmology assessment, preferably same day or within 24 hours depending on severity and local access.\n"
     "• Check blood pressure and review diabetes, vascular risk factors, glaucoma, medications, previous ocular disease.\n"
     "• [color=#991B1B]Do NOT attempt empiric ocular massage, pressure-lowering treatment, or anticoagulation solely to reverse CRVO.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Dilated fundus examination.\n"
     "• Optical coherence tomography (OCT) to assess macular edema.\n"
     "• Fluorescein angiography when required to assess retinal perfusion and ischemia.\n"
     "• Intraocular pressure measurement when appropriate.\n"
     "• Blood pressure, glucose or HbA1c, lipid profile as clinically indicated.\n"
     "• Further investigations in younger patients or atypical presentations guided by ophthalmology and suspected underlying cause."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Acute Management[/color]\n"
     "• There is no established emergency bedside medication that reliably reverses established CRVO.\n"
     "• Arrange prompt ophthalmology assessment to classify occlusion as ischemic or nonischemic and identify complications.\n"
     "• Optimize systemic vascular risk factors.\n"
     "• [color=#991B1B]Do NOT assume CRVO is harmless because it is painless. Do NOT initiate systemic anticoagulation or antiplatelet therapy solely for CRVO unless another indication exists.[/color]\n\n"
     "[color=#1E3A8A]2. Intravitreal Anti-VEGF Therapy[/color]\n"
     "• Common ophthalmology regimens include ranibizumab 0.5 mg intravitreally or aflibercept 2 mg intravitreally for CRVO-associated macular edema. Exact product, regimen, frequency are specialist-directed.\n"
     "• Administer only by trained ophthalmologist under sterile intravitreal injection protocols.\n"
     "• [color=#991B1B]These are NOT bedside or emergency-department injections. New severe pain, redness, photophobia, or worsening vision after injection requires urgent evaluation for endophthalmitis or another complication.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat macular edema with ophthalmologist-directed intravitreal therapy when indicated.\n"
     "• Monitor for retinal neovascularization and neovascular glaucoma.\n"
     "• Manage coexisting glaucoma and systemic vascular risk factors.\n"
     "• Ischemic CRVO generally carries a worse visual prognosis and requires close follow-up."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent ophthalmology referral for all suspected acute CRVO.\n"
     "• Immediate specialist assessment for profound visual loss, ocular pain, or suspected neovascular glaucoma.\n"
     "• Arrange ongoing retinal follow-up because complications may develop after initial presentation."),
    ("REFERENCES", "info", "AAO Retinal Vein Occlusions Preferred Practice Pattern; Royal College of Ophthalmologists Retinal Vein Occlusion Guidelines.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Vitreous Hemorrhage")] = [
    ("01 — RECOGNIZE", "info", 
     "Vitreous hemorrhage is bleeding into the vitreous cavity, often caused by retinal tears, proliferative diabetic retinopathy, retinal vascular disease, trauma, or posterior vitreous detachment.\n"
     "• Sudden painless floaters, cobwebs, haze, or reddish vision.\n"
     "• Blurred vision or substantial visual loss.\n"
     "• Fundus view may be obscured by blood.\n\n"
     "[color=#991B1B]Red flags:[/color] New flashes and floaters, curtain-like visual field defect, or sudden severe visual loss. Recent ocular or head trauma. Suspected retinal tear or detachment. Proliferative diabetic retinopathy or anticoagulant use with significant bleeding."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Document visual acuity in both eyes.\n"
     "• Ask about flashes, floaters, curtain-like shadow, trauma, diabetes, previous retinal disease, anticoagulants.\n"
     "• Perform pupil examination and assess for relative afferent pupillary defect.\n"
     "• Arrange urgent ophthalmology assessment to exclude retinal tear or detachment.\n"
     "• Avoid pressure on eye if trauma or open-globe injury possible."),
    ("03 — INVESTIGATIONS", "info", 
     "• Dilated retinal examination if fundus can be visualized.\n"
     "• B-scan ocular ultrasonography may be required when fundus obscured, provided open-globe injury excluded.\n"
     "• OCT when appropriate to evaluate associated macular pathology.\n"
     "• Glucose testing and assessment for diabetic retinopathy when indicated.\n"
     "• Further evaluation for retinal vascular disease, trauma, or systemic causes according to clinical findings."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Initial Management[/color]\n"
     "• There is no universal medication that clears vitreous blood immediately.\n"
     "• Arrange urgent ophthalmology review.\n"
     "• Advise avoiding strenuous activity until retinal pathology assessed; positioning advice individualized by ophthalmologist.\n"
     "• Review anticoagulant/antiplatelet therapy, but do NOT stop essential medication without assessing indication and bleeding severity.\n"
     "• [color=#991B1B]A vitreous hemorrhage may conceal a retinal tear or detachment. Do NOT discharge a patient with new unexplained vitreous hemorrhage without appropriate retinal assessment and follow-up plan.[/color]\n\n"
     "[color=#1E3A8A]2. Definitive Treatment[/color]\n"
     "• Observation may be appropriate for selected cases once retinal tear/detachment excluded and follow-up reliable.\n"
     "• Retinal tears may require laser photocoagulation or cryotherapy.\n"
     "• Retinal detachment may require urgent retinal surgery.\n"
     "• Persistent/recurrent hemorrhage may require vitrectomy.\n"
     "• Proliferative diabetic retinopathy may require retinal laser treatment, intravitreal anti-VEGF therapy, or surgery depending on findings."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat source of bleeding.\n"
     "• Monitor visual acuity and retinal status until hemorrhage resolves or definitive treatment completed.\n"
     "• Provide appropriate diabetic and vascular risk-factor management."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent same-day ophthalmology or retinal assessment appropriate for new unexplained vitreous hemorrhage.\n"
     "• Immediate assessment required if retinal detachment, open-globe injury, or major trauma suspected."),
    ("REFERENCES", "info", "AAO Posterior Vitreous Detachment, Retinal Breaks, and Lattice Degeneration Preferred Practice Pattern; AAO Guidance on Diabetic Retinopathy and Vitreoretinal Disease.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Traumatic Optic Neuropathy")] = [
    ("01 — RECOGNIZE", "info", 
     "Traumatic optic neuropathy is injury to the optic nerve following head or orbital trauma. May occur without obvious injury to external eye.\n"
     "• Reduced vision following blunt or penetrating trauma.\n"
     "• Impaired color vision or reduced brightness perception.\n"
     "• Relative afferent pupillary defect when unilateral or asymmetric.\n"
     "• Normal-appearing optic disc may be present initially in posterior traumatic optic neuropathy.\n\n"
     "[color=#991B1B]Red flags:[/color] Rapidly progressive visual loss. Associated severe head injury, orbital fracture, or intracranial hemorrhage. Proptosis, tense orbit, restricted eye movement, or severe pain suggesting orbital compartment syndrome. Signs of open-globe injury."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Stabilize airway, breathing, circulation; follow trauma protocols.\n"
     "• Record visual acuity, pupils, color vision if feasible, ocular movements without delaying resuscitation.\n"
     "• Assess for orbital compartment syndrome (separate time-critical emergency).\n"
     "• If open-globe injury possible, place rigid eye shield without pressure and avoid tonometry.\n"
     "• Obtain urgent ophthalmology and trauma/neurosurgical consultation as indicated."),
    ("03 — INVESTIGATIONS", "info", 
     "• CT of orbits and head when indicated to assess fractures, optic canal injury, foreign bodies, intracranial trauma.\n"
     "• MRI may be considered later for selected optic nerve or intracranial pathology, once metallic foreign bodies and other contraindications excluded.\n"
     "• Formal ophthalmic assessment and serial visual examinations.\n"
     "• Investigate associated head injury according to standard trauma protocols."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Initial Management[/color]\n"
     "• Treat life-threatening trauma first.\n"
     "• Maintain adequate oxygenation and perfusion; avoid hypotension, particularly in associated traumatic brain injury.\n"
     "• Manage orbital compartment syndrome immediately if present, according to its specific emergency protocol.\n"
     "• [color=#991B1B]Do NOT confuse traumatic optic neuropathy with orbital compartment syndrome. Orbital compartment syndrome may require immediate decompression without waiting for imaging.[/color]\n\n"
     "[color=#1E3A8A]2. Corticosteroids[/color]\n"
     "• High-dose systemic corticosteroids are NOT routinely recommended for traumatic optic neuropathy because convincing benefit has not been established and high-dose treatment may cause harm, especially in traumatic brain injury.\n"
     "• [color=#991B1B]Do NOT administer megadose methylprednisolone routinely for traumatic optic neuropathy. Decisions about selected interventions require specialist discussion and must consider associated head injury.[/color]\n\n"
     "[color=#1E3A8A]3. Surgical Intervention[/color]\n"
     "• Optic canal decompression is not routinely indicated for all cases; role is controversial and must be assessed by specialist teams.\n"
     "• Surgery may be required for other associated injuries (orbital compartment syndrome, compressive lesions, selected fractures)."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Coordinate ophthalmology, trauma, and neurosurgical care.\n"
     "• Monitor visual function and treat associated orbital or intracranial injuries.\n"
     "• Provide prognosis counseling and rehabilitation support when visual impairment persists."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent hospital assessment for all suspected traumatic optic neuropathy.\n"
     "• Admission generally required when significant head injury, progressive visual loss, orbital injury, or other serious trauma present."),
    ("REFERENCES", "info", "AAO Traumatic Optic Neuropathy Clinical Guidance; Brain Trauma Foundation Guidelines for Severe TBI; International Neuro-Ophthalmology Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Giant Cell Arteritis with Visual Symptoms")] = [
    ("01 — RECOGNIZE", "info", 
     "Giant cell arteritis (GCA) is a large-vessel vasculitis that can cause irreversible visual loss. Predominantly affects adults aged 50 years and older.\n"
     "• New headache, especially temporal. Scalp tenderness or jaw claudication.\n"
     "• Transient monocular visual loss, diplopia, or sudden permanent visual loss.\n"
     "• Constitutional symptoms, polymyalgia rheumatica symptoms, or unexplained fever.\n"
     "• Anterior ischemic optic neuropathy may be found on examination.\n\n"
     "[color=#991B1B]Red flags:[/color] Any new visual symptom in patient with suspected GCA. Transient visual loss (may precede permanent blindness). Bilateral or rapidly progressive visual impairment."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Treat suspected GCA with visual symptoms as medical emergency.\n"
     "• Obtain urgent ophthalmology and medical/rheumatology input.\n"
     "• Draw blood for ESR, CRP, full blood count, platelet count as soon as possible, but do NOT delay treatment while awaiting results.\n"
     "• Assess for jaw claudication, scalp tenderness, headache, constitutional symptoms, polymyalgia rheumatica symptoms.\n"
     "• Arrange urgent evaluation for other causes of acute visual loss when appropriate."),
    ("03 — INVESTIGATIONS", "info", 
     "• ESR and CRP. Full blood count and platelet count.\n"
     "• Temporal artery ultrasound and/or temporal artery biopsy according to local pathways.\n"
     "• Additional vascular imaging may be required to evaluate large-vessel involvement.\n"
     "• Ophthalmic assessment to document type and extent of visual impairment.\n"
     "• [color=#991B1B]Normal inflammatory markers reduce but do not completely eliminate possibility of GCA when clinical suspicion is high.[/color]"),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Immediate Glucocorticoid Therapy[/color]\n"
     "• For suspected GCA with acute or threatened visual loss, urgent specialist-directed treatment required.\n"
     "• Commonly used regimen for threatened or established visual loss: methylprednisolone 500–1,000 mg IV once daily for up to 3 days, followed by high-dose oral glucocorticoid therapy per specialist guidance.\n"
     "• If IV treatment not immediately available, oral prednisolone (commonly 40–60 mg daily or ~1 mg/kg/day up to locally recommended maximum) should be started promptly under appropriate emergency pathway.\n"
     "• [color=#991B1B]Do NOT delay initial glucocorticoid treatment for temporal artery biopsy or imaging. Suspected GCA with visual symptoms requires immediate treatment because visual loss may become irreversible.[/color]\n\n"
     "[color=#1E3A8A]2. Long-Term Disease Control[/color]\n"
     "• Rheumatology or specialist medical follow-up required.\n"
     "• Tocilizumab or other steroid-sparing strategies may be considered in selected patients.\n"
     "• Bone protection, glucose monitoring, blood pressure control, and infection-risk assessment may be needed during prolonged glucocorticoid treatment."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Confirm diagnosis through temporal artery ultrasound, biopsy, or other appropriate imaging without delaying treatment.\n"
     "• Assess for systemic and large-vessel involvement.\n"
     "• Monitor symptoms, inflammatory markers, glucocorticoid adverse effects, and recurrence.\n"
     "• Provide clear instructions to seek immediate care for new visual symptoms, headache, or jaw claudication."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate hospital assessment and specialist involvement for any suspected GCA with visual symptoms.\n"
     "• Admission often appropriate when acute visual loss or IV glucocorticoid therapy required."),
    ("REFERENCES", "info", "BSR Guideline on Diagnosis and Treatment of Giant Cell Arteritis; ACR/Vasculitis Foundation Guideline for Management of GCA; AAO Ischemic Optic Neuropathy and GCA Clinical Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Optic Neuritis")] = [
    ("01 — RECOGNIZE", "info", 
     "Optic neuritis is inflammation of the optic nerve that commonly causes acute or subacute visual loss. May be associated with multiple sclerosis, MOG-antibody-associated disease, neuromyelitis optica spectrum disorder, infection, or other inflammatory conditions.\n"
     "• Subacute reduction in vision, usually developing over hours to days.\n"
     "• Pain with eye movement.\n"
     "• Impaired color vision, especially red desaturation.\n"
     "• Relative afferent pupillary defect in unilateral or asymmetric disease.\n"
     "• Optic disc may appear normal in retrobulbar optic neuritis.\n\n"
     "[color=#991B1B]Red flags:[/color] Severe bilateral visual loss. Profound or rapidly progressive visual impairment. Marked optic disc swelling, retinal hemorrhage, or atypical fundus findings. Fever, meningism, immunocompromise, or suspected infection. Older age, painless visual loss, or atypical clinical course. Neurological deficits suggesting another CNS disorder."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Document visual acuity, pupils, color vision, and visual fields when feasible.\n"
     "• Assess for neurological symptoms, pain with eye movement, recent infection, autoimmune disease, previous demyelinating episodes.\n"
     "• Arrange urgent ophthalmology or neuro-ophthalmology assessment.\n"
     "• Refer to emergency neurology when severe, atypical, bilateral, or rapidly progressive disease present.\n"
     "• [color=#991B1B]Do NOT assume that all acute visual loss with pain is optic neuritis; exclude retinal, vascular, infectious, and compressive causes.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• MRI of brain and orbits with appropriate contrast sequences when indicated.\n"
     "• Formal ophthalmic examination, including fundus assessment and visual fields.\n"
     "• OCT may help document retinal nerve fiber and ganglion cell changes.\n"
     "• Blood testing for MOG-IgG, aquaporin-4 IgG, infectious causes, or systemic inflammatory disorders may be indicated in atypical or severe presentations.\n"
     "• Further neurological evaluation may be required if multiple sclerosis or another demyelinating disorder suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Corticosteroid Treatment[/color]\n"
     "• For selected typical acute optic neuritis, IV methylprednisolone 1,000 mg daily for 3 days is a commonly used regimen when accelerated recovery is clinically indicated.\n"
     "• Other specialist-directed regimens may be used according to severity, underlying cause, and local protocol.\n"
     "• [color=#991B1B]Corticosteroids may accelerate visual recovery in typical demyelinating optic neuritis but do not necessarily improve long-term visual outcome. Oral prednisone alone at conventional doses should not be used as a substitute for evidence-based specialist-directed treatment of typical optic neuritis because some regimens have been associated with increased recurrence. Suspected infectious optic neuropathy requires cause-specific management.[/color]\n\n"
     "[color=#1E3A8A]2. Severe or Atypical Optic Neuritis[/color]\n"
     "• Severe disease, bilateral involvement, or poor response to corticosteroids may require specialist-directed plasma exchange or other immunotherapy.\n"
     "• Treatment for MOG-associated disease, neuromyelitis optica spectrum disorder, or infectious causes differs from routine typical optic neuritis.\n"
     "• [color=#991B1B]Do NOT delay escalation in severe bilateral or rapidly progressive visual loss.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify underlying cause and assess risk of future neurological disease.\n"
     "• Coordinate ophthalmology and neurology follow-up.\n"
     "• Monitor visual acuity, color vision, visual fields, and OCT where appropriate.\n"
     "• Provide disease-specific counseling and treatment if demyelinating or systemic inflammatory disorder diagnosed."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent specialist assessment for suspected acute optic neuritis.\n"
     "• Hospital evaluation appropriate for severe visual loss, atypical features, bilateral disease, suspected infection, or need for IV treatment."),
    ("REFERENCES", "info", "AAO Optic Neuritis Clinical Guidance; Optic Neuritis Treatment Trial (ONTT); AAN Evidence-Based Guidance on Optic Neuritis and Demyelinating Disease.")
]


# ==================== NEW OPHTHALMOLOGY TOPICS (21-30) ====================

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Dacryocystitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute dacryocystitis is an infection of the lacrimal sac, usually caused by obstruction of the nasolacrimal duct.\n"
     "• Painful, red swelling near the medial canthus, usually below the medial canthal tendon.\n"
     "• Tearing and tenderness over the lacrimal sac.\n"
     "• Purulent discharge may be expressed through the puncta.\n"
     "• Fever or malaise may occur.\n\n"
     "[color=#991B1B]Red flags:[/color] Proptosis, painful or restricted eye movements, or reduced vision. Rapidly spreading erythema, severe systemic illness, or immunocompromise. Suspected orbital cellulitis, abscess, or sepsis. Neonatal infection or suspected congenital lacrimal obstruction with systemic illness."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess vital signs and screen for sepsis.\n"
     "• Document visual acuity, pupils, eye movements, and extent of periocular swelling.\n"
     "• Determine whether infection is confined to lacrimal sac or has spread into orbit.\n"
     "• Avoid forceful pressure or repeated manipulation of a severely inflamed lacrimal sac.\n"
     "• Arrange urgent ophthalmology assessment for severe infection, systemic symptoms, abscess, or suspected orbital involvement."),
    ("03 — INVESTIGATIONS", "info", 
     "• Clinical diagnosis is often sufficient in uncomplicated cases.\n"
     "• CBC, CRP, renal function, and blood cultures may be indicated in systemic illness or hospitalized patients.\n"
     "• Culture purulent material when feasible in severe, recurrent, atypical, or treatment-resistant infection.\n"
     "• Contrast-enhanced CT of orbits and sinuses when orbital cellulitis, abscess, or another deep infection is suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Oral Antibiotics for Selected Uncomplicated Cases[/color]\n"
     "• Amoxicillin-clavulanate 875/125 mg orally every 12 hours, or 500/125 mg every 8 hours, for a commonly used 5–7-day course, adjusted to clinical response and local guidance.\n"
     "• Assess response within 24–48 hours. Review allergy history, renal function, and risk factors for resistant organisms.\n"
     "• [color=#991B1B]This regimen is for selected adults with uncomplicated disease who can take oral medication and have no orbital or systemic complications.[/color]\n\n"
     "[color=#1E3A8A]2. IV Antibiotics for Severe Infection[/color]\n"
     "• IV ampicillin-sulbactam 3 g every 6 hours is a commonly used adult regimen when broader treatment is required.\n"
     "• Alternative regimens should follow local orbital/facial infection protocol, with additional MRSA coverage when indicated.\n"
     "• [color=#991B1B]Suspected orbital cellulitis, sepsis, or abscess requires hospital management and urgent specialist assessment.[/color]\n\n"
     "[color=#1E3A8A]3. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within patient-specific daily limits."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat acute infection and identify underlying lacrimal drainage obstruction.\n"
     "• Drain an abscess when indicated by ophthalmology.\n"
     "• Definitive dacryocystorhinostomy may be considered after acute inflammation has settled, depending on cause and recurrence.\n"
     "• Recurrent or atypical swelling may require investigation for other lacrimal sac pathology."),
    ("06 — DISPOSITION", "warning", 
     "• Outpatient treatment may be appropriate for carefully selected uncomplicated cases with reliable follow-up.\n"
     "• Admit or arrange urgent specialist evaluation for systemic illness, abscess, rapid progression, immunocompromise, or suspected orbital involvement.\n"
     "• Any visual impairment or painful/restricted eye movement warrants emergency reassessment."),
    ("REFERENCES", "info", "AAO Lacrimal Drainage System Disease; Merck Manual Professional Edition Dacryocystitis; Local Antimicrobial Guidelines.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Preseptal Cellulitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Preseptal cellulitis is an infection of the eyelid and periocular tissues anterior to the orbital septum. It must be distinguished from orbital cellulitis, which can threaten vision and life.\n"
     "• Eyelid erythema, swelling, warmth, and tenderness.\n"
     "• Visual acuity usually remains normal.\n"
     "• Extraocular movements are full and generally painless.\n"
     "• No proptosis or relative afferent pupillary defect attributable to orbital involvement.\n\n"
     "[color=#991B1B]Red flags suggesting orbital cellulitis:[/color] Pain with eye movement or restricted ocular motility. Proptosis or diplopia. Reduced vision or abnormal pupillary response. Severe headache, neurological signs, or systemic toxicity."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Document visual acuity, pupils, ocular motility, and proptosis.\n"
     "• Check vital signs and assess for fever or sepsis.\n"
     "• Identify potential sources (skin trauma, insect bites, sinusitis, eyelid infection).\n"
     "• If eye cannot be adequately examined because of swelling, or orbital involvement cannot be excluded, arrange urgent hospital assessment and imaging as appropriate.\n"
     "• Do NOT delay treatment while waiting for imaging when orbital cellulitis or sepsis is strongly suspected."),
    ("03 — INVESTIGATIONS", "info", 
     "• No routine imaging is required for clearly uncomplicated preseptal cellulitis with a reliable examination.\n"
     "• CBC, CRP, and blood cultures may be indicated in severe illness or hospitalized patients.\n"
     "• Contrast-enhanced CT of orbits and sinuses is appropriate when orbital cellulitis, abscess, sinus complications, or inadequate examination is a concern.\n"
     "• Culture any drainable collection when feasible."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Oral Antibiotics for Selected Adults[/color]\n"
     "• Amoxicillin-clavulanate 875/125 mg orally every 12 hours, or 500/125 mg every 8 hours, according to local guidelines and patient factors.\n"
     "• Review within 24–48 hours to ensure improvement. Adjust therapy for allergy history, renal impairment, likely source, local resistance.\n"
     "• [color=#991B1B]The correct regimen depends on whether infection is related to sinusitis, skin trauma, animal/human bite, or another source. Suspected MRSA infection may require additional or alternative coverage per local guidelines.[/color]\n\n"
     "[color=#1E3A8A]2. IV Antibiotics for Severe Disease[/color]\n"
     "• IV ampicillin-sulbactam 3 g every 6 hours is one commonly used adult regimen when admission or IV treatment is required.\n"
     "• Broader therapy may be necessary in severe infection, immunocompromise, or suspected orbital involvement.\n"
     "• [color=#991B1B]If orbital cellulitis cannot be excluded, manage the patient through an orbital infection pathway rather than as uncomplicated preseptal cellulitis.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat infection and its source.\n"
     "• Drain a skin or eyelid abscess when clinically indicated.\n"
     "• Manage associated sinusitis or other underlying infection.\n"
     "• Reassess promptly for progression to orbital cellulitis."),
    ("06 — DISPOSITION", "warning", 
     "• Outpatient treatment may be appropriate for mild disease when eye can be examined reliably, patient is systemically well, and follow-up is assured.\n"
     "• Admit children with significant systemic illness, very young infants, immunocompromised patients, or those unable to take oral medication, per local pediatric guidance.\n"
     "• Immediate escalation required for any orbital red flag, worsening vision, or deterioration despite treatment."),
    ("REFERENCES", "info", "AAO Preseptal and Orbital Cellulitis; Royal Children's Hospital Melbourne Periorbital/Orbital Cellulitis Guideline; Local Antimicrobial Guidelines.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Orbital Fracture with Extraocular Muscle Entrapment")] = [
    ("01 — RECOGNIZE", "info", 
     "Orbital fractures may trap extraocular muscles or orbital soft tissue, particularly in pediatric 'trapdoor' fractures. Entrapment can cause ischemia and oculocardiac reflexes.\n"
     "• Periorbital bruising and swelling after facial trauma.\n"
     "• Diplopia or restricted gaze. Pain on eye movement.\n"
     "• Nausea or vomiting, particularly with attempted upward gaze.\n"
     "• Infraorbital numbness may occur with orbital floor fractures.\n\n"
     "[color=#991B1B]Red flags:[/color] Bradycardia, nausea, vomiting, or syncope triggered by eye movement. Marked restriction of ocular movement. Reduced vision, relative afferent pupillary defect, or suspected globe injury. Proptosis, tense orbit, or rapidly increasing pain suggesting orbital compartment syndrome."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Follow trauma assessment priorities and stabilize life-threatening injuries.\n"
     "• Document visual acuity, pupils, ocular movements, diplopia, and facial sensation.\n"
     "• Avoid nose blowing and advise patient to sneeze with mouth open.\n"
     "• Provide analgesia and antiemetic when indicated.\n"
     "• Obtain urgent ophthalmology and maxillofacial consultation if entrapment suspected.\n"
     "• Treat suspected orbital compartment syndrome immediately according to its dedicated emergency protocol."),
    ("03 — INVESTIGATIONS", "info", 
     "• Thin-cut CT of orbits and facial bones.\n"
     "• CT assessment for muscle or soft-tissue entrapment, fracture displacement, orbital hemorrhage, and associated injuries.\n"
     "• Formal ophthalmic examination.\n"
     "• Additional head and cervical spine imaging according to trauma indications."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Initial Supportive Management[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within patient-specific limits. Antiemetic may be used when clinically indicated.\n"
     "• Monitor pain, nausea, heart rate, visual acuity, and ocular movement. Keep patient fasting if urgent surgery likely.\n"
     "• [color=#991B1B]Avoid nose blowing (can introduce air into orbit and worsen orbital emphysema). Do NOT press on globe or attempt to manipulate trapped tissue.[/color]\n\n"
     "[color=#1E3A8A]2. Surgical Management[/color]\n"
     "• Indications: Suspected muscle entrapment (especially with oculocardiac reflex), significant persistent diplopia with mechanical restriction, pediatric trapdoor fracture with entrapment, selected large fractures or progressive enophthalmos.\n"
     "• Urgent surgical evaluation and release of entrapped tissue when indicated. Timing depends on clinical findings; true entrapment with oculocardiac reflex requires emergency specialist management.\n"
     "• [color=#991B1B]Do NOT delay surgical consultation in a child with restricted eye movement, nausea/vomiting, and bradycardia after orbital trauma.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Manage fracture and any entrapped muscle or soft tissue.\n"
     "• Monitor ocular motility, diplopia, visual acuity, and orbital position.\n"
     "• Provide specialist follow-up for persistent diplopia, enophthalmos, or sensory deficits.\n"
     "• Antibiotics are not automatically required for every closed orbital fracture; use according to injury, sinus involvement, surgical plan, and local guidance."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate specialist assessment for suspected entrapment or oculocardiac reflex.\n"
     "• Admit when urgent surgery, significant associated trauma, or serious ocular injury is present.\n"
     "• Outpatient management only after serious ocular injury and entrapment excluded and follow-up assured."),
    ("REFERENCES", "info", "AAO Orbital Floor Fractures; AO Surgery Reference Orbital Trauma; Pediatric Orbital Fracture and Oculocardiac Reflex Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Eyelid Laceration and Canalicular Injury")] = [
    ("01 — RECOGNIZE", "info", 
     "Eyelid lacerations may involve the eyelid margin, levator muscle, canthal tendons, lacrimal drainage system, or globe. Injuries near the medial canthus may damage the canaliculi.\n\n"
     "[color=#1E3A8A]High-risk features:[/color] Laceration through eyelid margin. Wound involving medial canthus or punctum. Visible orbital fat (suggesting septal penetration). Ptosis after trauma (suggesting levator injury). Tissue loss, contaminated wounds, animal bites, or high-velocity trauma.\n\n"
     "[color=#991B1B]Red flags:[/color] Suspected open-globe injury. Reduced vision, abnormal pupil, or significant ocular pain. Proptosis or tense orbit. Deep penetrating wound, retained foreign body, or associated facial fracture."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess and document visual acuity, pupils, and ocular motility.\n"
     "• Exclude open-globe injury before manipulating eyelid.\n"
     "• Control external bleeding with gentle pressure applied to surrounding soft tissue only when open-globe injury not suspected.\n"
     "• Cover suspected open globe with a rigid shield without pressure.\n"
     "• Assess tetanus status and mechanism of injury.\n"
     "• Arrange urgent ophthalmology or oculoplastic consultation for complex wounds."),
    ("03 — INVESTIGATIONS", "info", 
     "• Detailed ocular examination.\n"
     "• CT of orbits when penetrating injury, foreign body, fracture, or deep orbital involvement suspected.\n"
     "• Imaging should not delay urgent surgical assessment when open-globe injury evident.\n"
     "• Consider wound cultures only in selected infected or heavily contaminated cases."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Wound Care[/color]\n"
     "• Clean superficial wounds according to local wound-care protocols.\n"
     "• Avoid probing a deep wound or blindly exploring a laceration near the globe. Do NOT remove a deeply embedded object before specialist assessment.\n"
     "• [color=#991B1B]Visible orbital fat, medial canthal injury, eyelid-margin disruption, ptosis, or tissue loss requires specialist repair rather than routine skin closure.[/color]\n\n"
     "[color=#1E3A8A]2. Antibiotics when Indicated[/color]\n"
     "• Antibiotic choice depends on wound mechanism, contamination, bite exposure, local protocols. For selected contaminated wounds or bites, amoxicillin-clavulanate may be used when appropriate.\n"
     "• [color=#991B1B]Antibiotics are NOT a substitute for surgical repair of canalicular injury or open-globe trauma. Do NOT prescribe prophylactic antibiotics indiscriminately for every simple, clean eyelid laceration.[/color]\n\n"
     "[color=#1E3A8A]3. Definitive Wound Repair[/color]\n"
     "• Simple superficial skin wounds may be repaired by a suitably trained clinician after globe injury excluded.\n"
     "• Injuries involving eyelid margin, canaliculus, levator, canthal tendon, or orbital septum require appropriate specialist repair.\n"
     "• Canalicular injury may require microsurgical repair and temporary stenting.\n"
     "• [color=#991B1B]Poor alignment of eyelid margin can cause notching, exposure, and chronic irritation. Delayed recognition of canalicular injury may lead to persistent tearing.[/color]"),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Restore eyelid anatomy and function.\n"
     "• Repair canalicular and deeper structural injuries as indicated.\n"
     "• Provide wound care, tetanus prophylaxis, and antibiotics when clinically indicated.\n"
     "• Arrange follow-up to assess healing, eyelid position, tear drainage, and infection."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate referral for suspected open-globe injury or penetrating trauma.\n"
     "• Urgent specialist repair for canalicular injury, eyelid-margin involvement, levator injury, or tissue loss.\n"
     "• Discharge only for uncomplicated superficial wounds after appropriate assessment and follow-up arrangements."),
    ("REFERENCES", "info", "AAO Eyelid Laceration Repair; Merck Manual Professional Edition Eyelid Lacerations; Oculoplastic Trauma Management Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Traumatic Lens Dislocation")] = [
    ("01 — RECOGNIZE", "info", 
     "Traumatic lens dislocation or subluxation occurs when lens is displaced due to disruption of supporting zonular fibers. May cause acute visual impairment, inflammation, or secondary glaucoma.\n"
     "• Blurred vision or monocular diplopia after blunt trauma.\n"
     "• Visible lens displacement or abnormal anterior chamber.\n"
     "• Irregular or distorted red reflex. Phacodonesis or iridodonesis may be present.\n"
     "• Intraocular pressure may be elevated if lens obstructs aqueous outflow.\n\n"
     "[color=#991B1B]Red flags:[/color] Sudden severe visual loss. Lens displaced into anterior chamber. Markedly elevated intraocular pressure. Associated hyphema, open-globe injury, retinal injury, or severe inflammation. History suggesting penetrating trauma."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity, pupils, and mechanism of injury.\n"
     "• Exclude open-globe injury before performing tonometry or detailed ocular manipulation.\n"
     "• If open-globe injury suspected, place rigid eye shield without pressure and arrange immediate ophthalmology transfer.\n"
     "• Obtain urgent ophthalmology assessment for suspected traumatic lens displacement.\n"
     "• Control pain and vomiting and avoid pressure on globe."),
    ("03 — INVESTIGATIONS", "info", 
     "• Slit-lamp examination by a trained clinician.\n"
     "• Intraocular pressure measurement only when open-globe injury excluded.\n"
     "• Dilated retinal examination when safe and appropriate.\n"
     "• CT of orbits when associated fracture, foreign body, or significant trauma suspected.\n"
     "• Ultrasound or other imaging only when appropriate and after open-globe injury excluded."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Initial Stabilization[/color]\n"
     "• Protect eye from further trauma. Provide analgesia and antiemetic when indicated. Keep patient fasting if urgent surgery likely. Arrange urgent ophthalmology consultation.\n"
     "• [color=#991B1B]Do NOT attempt to reposition lens manually. Do NOT use routine glaucoma drops before specialist assessment if open-globe injury remains possible.[/color]\n\n"
     "[color=#1E3A8A]2. Elevated Intraocular Pressure[/color]\n"
     "• If lens-related secondary glaucoma suspected, obtain urgent ophthalmology guidance.\n"
     "• Pressure-lowering therapy may be needed, but drug selection depends on mechanism, lens position, inflammation, associated injuries.\n"
     "• [color=#991B1B]Avoid delaying treatment of acute pressure elevation. Do NOT use miotics or other ocular medication empirically without considering lens position and underlying mechanism.[/color]\n\n"
     "[color=#1E3A8A]3. Definitive Ophthalmic Management[/color]\n"
     "• Observation may be appropriate for selected stable subluxations with acceptable vision and no complications.\n"
     "• Surgical intervention may be required for anterior lens dislocation, uncontrolled pressure, severe inflammation, or significant visual impairment."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Determine extent of zonular damage and lens displacement.\n"
     "• Monitor intraocular pressure, inflammation, corneal health, and retinal status.\n"
     "• Select observation, lens removal, or other surgery according to ophthalmology assessment.\n"
     "• Plan visual rehabilitation after acute injury stabilized."),
    ("06 — DISPOSITION", "warning", 
     "• Urgent same-day ophthalmology assessment for suspected traumatic lens displacement.\n"
     "• Immediate emergency management for anterior chamber lens dislocation, acute glaucoma, open-globe injury, or severe visual loss.\n"
     "• Admission may be necessary if urgent surgery or intensive monitoring required."),
    ("REFERENCES", "info", "AAO Lens Dislocation and Ocular Trauma; AAO Guidance on Traumatic Cataract and Secondary Glaucoma; Ophthalmic Trauma Management Guidelines.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Hypopyon")] = [
    ("01 — RECOGNIZE", "info", 
     "Hypopyon is the accumulation of inflammatory cells in the anterior chamber. It is a clinical sign rather than a diagnosis and may occur in severe microbial keratitis, endophthalmitis, or severe intraocular inflammation.\n"
     "• Visible white or yellow fluid level in inferior anterior chamber.\n"
     "• Redness, photophobia, pain, and blurred vision.\n"
     "• Corneal ulceration or infiltrate may be present.\n"
     "• Recent ocular surgery, intravitreal injection, or penetrating trauma increases concern for endophthalmitis.\n\n"
     "[color=#991B1B]Red flags:[/color] Rapid visual deterioration. Severe pain, marked redness, or recent ocular surgery/injection. Corneal ulcer with stromal thinning or suspected perforation. Fever, systemic illness, or suspected endogenous infection."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess visual acuity in both eyes and document onset/progression of symptoms.\n"
     "• Ask about recent eye surgery, injections, trauma, contact lens use, and systemic infection.\n"
     "• Arrange immediate ophthalmology assessment if endophthalmitis possible.\n"
     "• Avoid pressure on eye if open-globe injury or corneal perforation suspected.\n"
     "• [color=#991B1B]Do NOT start topical corticosteroids empirically before infection has been assessed.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Slit-lamp examination to identify source of hypopyon.\n"
     "• Assessment of corneal integrity, anterior chamber inflammation, and IOP when appropriate.\n"
     "• Dilated fundus examination if visualization possible.\n"
     "• B-scan ultrasonography may be considered by ophthalmology team when fundus obscured, provided open-globe injury excluded.\n"
     "• Corneal scraping and cultures for suspected microbial keratitis.\n"
     "• Aqueous or vitreous sampling and systemic investigations may be indicated when endophthalmitis suspected."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Suspected Microbial Keratitis[/color]\n"
     "• Immediate ophthalmology assessment. Corneal scraping and microbiological sampling when indicated, without unnecessarily delaying treatment.\n"
     "• Intensive topical antimicrobial therapy selected by ophthalmology team according to ulcer severity and suspected organism.\n"
     "• [color=#991B1B]A hypopyon with corneal infiltrate may represent a sight-threatening corneal ulcer. Do NOT treat suspected infectious keratitis with topical corticosteroids alone.[/color]\n\n"
     "[color=#1E3A8A]2. Suspected Endophthalmitis[/color]\n"
     "• Treat as ophthalmic emergency. Immediate retinal/ophthalmic specialist assessment required. Intravitreal antibiotics and possible vitreoretinal surgery determined by ophthalmologist.\n"
     "• [color=#991B1B]Topical antibiotics alone are inadequate for suspected endophthalmitis. Do NOT delay specialist treatment while waiting for culture results.[/color]\n\n"
     "[color=#1E3A8A]3. Pain Control[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within patient-specific daily limits."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify and treat underlying cause.\n"
     "• Microbial keratitis requires organism-appropriate antimicrobial treatment and monitoring for corneal thinning/perforation.\n"
     "• Endophthalmitis may require intravitreal antimicrobial therapy and surgery.\n"
     "• Noninfectious uveitis requires specialist-directed anti-inflammatory treatment only after infection appropriately considered."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate ophthalmology assessment for unexplained hypopyon.\n"
     "• Emergency hospital transfer for suspected endophthalmitis, corneal perforation, or rapidly declining vision."),
    ("REFERENCES", "info", "AAO Bacterial Keratitis Preferred Practice Pattern; AAO Endophthalmitis Guidance; ESCRS Postoperative Infection Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Postoperative Eye Emergency and Suspected Endophthalmitis")] = [
    ("01 — RECOGNIZE", "info", 
     "Postoperative eye emergencies may include endophthalmitis, wound leak, raised intraocular pressure, retinal detachment, hemorrhage, or corneal complications. Acute endophthalmitis is a severe intraocular infection that may occur after surgery or intravitreal injection.\n"
     "• Increasing eye pain, redness, or blurred vision after ocular procedure.\n"
     "• Photophobia and reduced visual acuity.\n"
     "• Hypopyon or marked intraocular inflammation may be present.\n"
     "• Some patients with endophthalmitis have relatively little pain.\n\n"
     "[color=#991B1B]Red flags:[/color] Rapid visual deterioration after surgery or injection. Hypopyon, severe inflammation, or suspected wound leak. Proptosis, severe pain, or neurological symptoms. Recent penetrating trauma or signs of open globe."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Record visual acuity and exact procedure and date.\n"
     "• Contact operating ophthalmologist or emergency ophthalmology service immediately.\n"
     "• Do NOT delay assessment for routine outpatient follow-up.\n"
     "• Avoid pressure on eye if wound leak or open-globe injury suspected.\n"
     "• [color=#991B1B]Do NOT patch tightly, manipulate surgical wound, or start steroid drops without specialist advice.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Urgent slit-lamp examination.\n"
     "• Assessment of surgical wound, anterior chamber, IOP when safe, and posterior segment.\n"
     "• Dilated fundus examination when visualization permits.\n"
     "• B-scan ultrasound when posterior visualization limited and open-globe injury excluded.\n"
     "• Aqueous or vitreous sampling for microbiology when indicated by ophthalmologist."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Suspected Acute Postoperative Endophthalmitis[/color]\n"
     "• Immediate ophthalmology/vitreoretinal consultation. Intraocular sampling and intravitreal antibiotics commonly required. Decision between intravitreal treatment alone and urgent vitrectomy depends on visual acuity, clinical severity, and specialist assessment.\n\n"
     "[color=#1E3A8A]Common Intravitreal Regimens (Ophthalmologist-Administered):[/color]\n"
     "• Vancomycin 1 mg/0.1 mL intravitreally.\n"
     "• Ceftazidime 2.25 mg/0.1 mL intravitreally.\n"
     "• [color=#991B1B]These are specialist intravitreal preparations requiring strict aseptic technique, correct dilution, and verification of final concentration by trained ophthalmic personnel. Intravitreal dosing is NOT interchangeable with systemic dosing. Preparation errors can cause severe retinal toxicity. Do NOT attempt preparation or injection in an unequipped emergency department.[/color]\n\n"
     "[color=#1E3A8A]2. Other Postoperative Complications[/color]\n"
     "• Raised IOP, wound leak, retinal detachment, and suprachoroidal hemorrhage require diagnosis-specific urgent ophthalmic treatment.\n"
     "• Do NOT assume all postoperative pain or reduced vision represents infection."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat identified complication promptly.\n"
     "• Arrange repeated examinations and microbiological follow-up when endophthalmitis suspected.\n"
     "• Review postoperative medications with operating ophthalmologist.\n"
     "• Document visual acuity and all changes carefully."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate transfer or direct assessment by ophthalmic surgical team.\n"
     "• Do NOT discharge a patient with suspected postoperative endophthalmitis without specialist evaluation."),
    ("REFERENCES", "info", "AAO Endophthalmitis Clinical Guidance; Endophthalmitis Vitrectomy Study; ESCRS Prevention and Management of Postoperative Endophthalmitis.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Corneal Graft Rejection")] = [
    ("01 — RECOGNIZE", "info", 
     "Corneal graft rejection is an immune response against a transplanted cornea. Early recognition and treatment are important to preserve graft clarity.\n"
     "• New redness, photophobia, blurred vision, or discomfort in an eye with previous corneal transplant.\n"
     "• Corneal edema or graft haze.\n"
     "• An endothelial rejection line may be visible in some cases.\n"
     "• Symptoms can resemble infection or other postoperative complications.\n\n"
     "[color=#991B1B]Red flags:[/color] Rapid reduction in vision. Severe pain, discharge, corneal ulceration, or suspected graft infection. Recent interruption of prescribed topical corticosteroids. Previous graft rejection or high-risk corneal transplant."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Establish date and type of corneal transplant.\n"
     "• Ask about medication adherence, recent steroid changes, trauma, and contact lens use.\n"
     "• Document visual acuity and examine cornea if equipment and expertise available.\n"
     "• Arrange same-day ophthalmology assessment for suspected rejection.\n"
     "• [color=#991B1B]Do NOT independently increase or restart intensive steroid treatment without assessment, particularly if infection is possible.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Slit-lamp examination to assess graft clarity, epithelial integrity, edema, and inflammation.\n"
     "• Intraocular pressure measurement when appropriate.\n"
     "• Corneal scraping or microbiological tests when infection suspected.\n"
     "• Additional tests directed by ophthalmologist according to graft type and clinical findings."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Topical Corticosteroids[/color]\n"
     "• Intensive topical prednisolone acetate 1% may be used for acute rejection, with frequency determined by ophthalmologist and severity of inflammation.\n"
     "• Initiate or adjust therapy under urgent ophthalmology supervision. Monitor graft clarity, visual acuity, IOP, and signs of infection. Treatment often requires carefully supervised taper.\n"
     "• [color=#991B1B]Topical steroids may worsen microbial keratitis or other corneal infections. Do NOT delay specialist assessment while attempting empirical treatment.[/color]\n\n"
     "[color=#1E3A8A]2. Additional Treatment[/color]\n"
     "• Severe endothelial rejection may require additional specialist-directed treatment, including systemic corticosteroids in selected cases.\n"
     "• Treat associated infection or raised IOP when present."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Confirm diagnosis and exclude infection.\n"
     "• Begin appropriate anti-rejection treatment promptly.\n"
     "• Monitor graft clarity and visual function closely.\n"
     "• Reinforce adherence to prescribed maintenance drops and long-term corneal follow-up."),
    ("06 — DISPOSITION", "warning", 
     "• Same-day ophthalmology assessment recommended for suspected graft rejection.\n"
     "• Immediate referral required for rapid visual decline, severe pain, suspected infection, or graft failure."),
    ("REFERENCES", "info", "AAO Corneal Transplantation and Corneal Graft Rejection; AAO EyeWiki Corneal Graft Rejection; Cornea Specialist Clinical Guidance.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Painful Red Eye — Emergency Differential Diagnosis")] = [
    ("01 — RECOGNIZE", "info", 
     "A painful red eye may be caused by minor surface disease or a vision-threatening emergency. Priority is to identify conditions requiring immediate treatment.\n\n"
     "[color=#1E3A8A]Important differential diagnoses:[/color] Acute angle-closure glaucoma. Microbial keratitis and corneal ulcer. Anterior uveitis. Scleritis. Endophthalmitis. Chemical injury. Open-globe injury. Severe conjunctivitis or episcleritis.\n\n"
     "[color=#991B1B]Red flags:[/color] Reduced visual acuity. Severe pain or marked photophobia. Corneal opacity or infiltrate. Fixed or mid-dilated pupil. Halos around lights, headache, nausea, or vomiting. Hypopyon, proptosis, or restricted eye movements. Recent ocular surgery, injection, trauma, or chemical exposure."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Assess airway, breathing, circulation, and systemic illness when indicated.\n"
     "• Measure visual acuity in each eye separately if safe.\n"
     "• Examine pupils, ocular movements, cornea, and pattern of redness.\n"
     "• Ask about contact lenses, trauma, chemical exposure, previous glaucoma, recent procedures, and medication use.\n"
     "• Suspected chemical injury requires immediate copious irrigation before detailed examination.\n"
     "• Suspected open-globe injury requires rigid shield without pressure and immediate ophthalmology transfer.\n"
     "• Arrange urgent specialist assessment for any red flag or uncertain diagnosis."),
    ("03 — INVESTIGATIONS", "info", 
     "• Visual acuity and pupil examination.\n"
     "• Fluorescein staining when appropriate and open-globe injury not suspected.\n"
     "• Slit-lamp examination when available.\n"
     "• Intraocular pressure measurement only when open-globe injury excluded and measurement appropriate.\n"
     "• Additional tests depend on suspected diagnosis."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Acute Angle-Closure Glaucoma[/color]\n"
     "• Immediate emergency ophthalmology consultation. Initiate pressure-lowering therapy per dedicated acute angle-closure glaucoma protocol. Definitive treatment usually involves laser peripheral iridotomy.\n"
     "• [color=#991B1B]Do NOT delay treatment for severe ocular pain, reduced vision, halos, headache, nausea, and a mid-dilated pupil.[/color]\n\n"
     "[color=#1E3A8A]2. Microbial Keratitis[/color]\n"
     "• Urgent ophthalmology assessment. Corneal scraping when indicated. Intensive topical antimicrobial therapy directed by severity and likely organism.\n"
     "• [color=#991B1B]Contact lens-associated painful red eye is particularly concerning for microbial keratitis.[/color]\n\n"
     "[color=#1E3A8A]3. Anterior Uveitis or Scleritis[/color]\n"
     "• Urgent ophthalmology assessment. Cycloplegic and anti-inflammatory therapy may be required after diagnosis. Suspected infectious causes must be considered before initiating corticosteroids.\n\n"
     "[color=#1E3A8A]4. Suspected Endophthalmitis[/color]\n"
     "• Immediate ophthalmology/vitreoretinal assessment. Intraocular antimicrobial therapy may be required urgently.\n\n"
     "[color=#1E3A8A]5. Analgesia[/color]\n"
     "• Paracetamol 500–1,000 mg orally every 6–8 hours as needed, within patient-specific limits."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Identify underlying cause and follow relevant disease-specific protocol.\n"
     "• Reassess visual acuity and clinical findings after initial treatment.\n"
     "• Provide explicit return precautions and arrange specialist follow-up."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate emergency ophthalmology assessment: Reduced vision, severe pain, corneal opacity, abnormal pupil, hypopyon, recent eye surgery or injection, suspected open-globe injury, or suspected acute angle closure.\n"
     "• Possible outpatient management: Only when a benign diagnosis is established, visual acuity is reassuring, dangerous causes excluded, and follow-up is reliable."),
    ("REFERENCES", "info", "AAO Red Eye and Emergency Ophthalmology Guidance; Merck Manual Professional Edition Red Eye; Emergency Ophthalmology Clinical Assessment Guidelines.")
]

OPHTHALMOLOGY_TOPICS[("Ophthalmic Emergencies", "Acute Diplopia and Ocular Motor Cranial Nerve Palsy")] = [
    ("01 — RECOGNIZE", "info", 
     "Acute diplopia is double vision that develops suddenly. May result from ocular misalignment, cranial nerve III/IV/VI palsy, neuromuscular disease, orbital pathology, or brainstem lesion.\n"
     "• Binocular diplopia that resolves when either eye is covered.\n"
     "• Abnormal eye alignment or restricted movement.\n"
     "• Ptosis may occur with third cranial nerve palsy.\n"
     "• Sixth nerve palsy commonly causes impaired abduction.\n"
     "• Fourth nerve palsy may cause vertical or torsional diplopia.\n\n"
     "[color=#991B1B]Red flags:[/color] Third cranial nerve palsy with dilated or poorly reactive pupil. Sudden severe headache or neck pain. Focal neurological deficits, ataxia, dysarthria, or altered consciousness. Proptosis, fever, painful eye movements, or orbital trauma. New diplopia with visual loss or other evidence of stroke."),
    ("02 — IMMEDIATE ACTIONS", "success", 
     "• Determine whether diplopia is monocular or binocular.\n"
     "• Document visual acuity, pupils, ptosis, ocular alignment, and extraocular movements.\n"
     "• Perform focused neurological examination.\n"
     "• Assess for severe headache, neck pain, vascular risk factors, trauma, and symptoms of myasthenia gravis.\n"
     "• Activate local stroke/emergency neurovascular pathway when stroke or aneurysm suspected.\n"
     "• [color=#991B1B]Do NOT assume an isolated cranial nerve palsy is benign until urgent causes have been considered.[/color]"),
    ("03 — INVESTIGATIONS", "info", 
     "• Neurological and ophthalmic examination.\n"
     "• Urgent CT angiography or MR angiography when aneurysm or other vascular lesion suspected.\n"
     "• Brain MRI when brainstem lesion, inflammation, demyelination, or other intracranial pathology suspected.\n"
     "• Glucose, blood pressure, and other lab tests according to clinical context.\n"
     "• Further evaluation for myasthenia gravis or systemic inflammatory disease when indicated."),
    ("04 — TREATMENT", "info", 
     "[color=#1E3A8A]1. Suspected Aneurysmal Third Nerve Palsy or Stroke[/color]\n"
     "• Immediate emergency department evaluation and neurovascular imaging. Obtain urgent neurology, neurosurgery, or stroke-team consultation as indicated.\n"
     "• [color=#991B1B]A painful third nerve palsy, particularly with pupillary involvement, is an emergency because of the risk of an intracranial aneurysm. A normal initial non-specialist examination does not reliably exclude a dangerous vascular cause.[/color]\n\n"
     "[color=#1E3A8A]2. Symptomatic Diplopia Management[/color]\n"
     "• Temporary occlusion of one lens may reduce diplopia while evaluation underway, if appropriate. Avoid driving or hazardous activities while diplopia persists.\n"
     "• [color=#991B1B]Symptom relief must NOT delay urgent investigation.[/color]\n\n"
     "[color=#1E3A8A]3. Suspected Myasthenia Gravis[/color]\n"
     "• Assess for fluctuating ptosis, fatigable weakness, dysphagia, dysarthria, and respiratory symptoms.\n"
     "• Respiratory or bulbar weakness requires emergency assessment for myasthenic crisis.\n"
     "• Arrange neurology review and disease-specific testing."),
    ("05 — DEFINITIVE MANAGEMENT", "info", 
     "• Treat underlying vascular, neurological, neuromuscular, orbital, or systemic condition.\n"
     "• Monitor ocular alignment, visual function, and neurological progression.\n"
     "• Arrange specialist follow-up even when isolated palsy initially thought to be microvascular."),
    ("06 — DISPOSITION", "warning", 
     "• Immediate emergency evaluation for pupil-involving third nerve palsy, severe headache, focal neurological deficits, orbital infection, trauma, or respiratory/bulbar weakness.\n"
     "• Urgent specialist assessment for all new unexplained binocular diplopia.\n"
     "• Outpatient follow-up only after dangerous causes excluded and safe plan documented."),
    ("REFERENCES", "info", "AAO Diplopia and Ocular Motility Disorders; AHA/ASA Acute Stroke Guidance; Neuro-Ophthalmology Clinical Guidance on Ocular Motor Cranial Nerve Palsies.")
]