*** Settings ***
Library             DataDriver    csvs/transripted_speech_579.csv
Test Template       Verify Transcription
Library             utils.py

*** Variables ***
${actual_text}      Please call Stella ask her to bring this thing with her from the store six spoons of fresh snow piece five thick slabs of blue cheese and maybe snacks for her brother bob. We also need a small plastic snake and a big toy frog for the kids. She could keep this things into three red bags and we will go meet her next Wednesday at the train station.

*** Test Cases ***
Transripted_speech for ${file_name}

*** Keywords ***
Verify Transcription
    [Arguments]   ${file_name}  ${transripted_speech}
    ${res} =  compare_strings  ${actual_text}  ${transripted_speech}
    Log       ${res}   console=True
    Should Be True     ${res}>=80