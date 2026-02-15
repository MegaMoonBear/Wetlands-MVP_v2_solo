# README - Main/overall repo
- Retype Wetlands-prototype-MVP to review what AI produced
- Renamed as "Wetlands-MVP_v2_solo"

# Goals 
- Visitor (look only – no action)
    Inform about importance of water and wetlands (intro level) and encourage return visits and use of “Contact/Feedback” option.
- Actor / Uploaders
    Increase understanding of water issues and wetlands’ role while encouraging simple, informed actions through quick photo uploads and guided participation.
(SMART components removed - see documentation folder)

# MVP shows AI capability
1. Place images manually in /backend/images/
2. Hardcode the filename in FastAPI
3. FastAPI sends the image path to Ollama
4. Ollama (LLaVA) returns descript'n
5. FastAPI returns JSON
6. React displays it
No uploads. No database. No authentication… So which of these is next? 


