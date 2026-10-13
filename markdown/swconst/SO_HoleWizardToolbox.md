---
title: "System Options >Hole Wizard/Toolbox"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_HoleWizardToolbox.htm"
---

# System Options >Hole Wizard/Toolbox

## System Options > Hole Wizard/Toolbox

| Setting | Get/Set Methods | Return Value or < Value > | Comment |
| --- | --- | --- | --- |
| Hole Wizard and Toolbox folder | ISldWorks::GetUserPreferenceStringValue (swUserPreferenceStringValue_e.swHoleWizardToolBoxFolder) ISldWorks::SetUserPreferenceStringValue (swUserPreferenceStringValue_e.swHoleWizardToolBoxFolder, < Value >) | String value | Specifies the location of the Hole Wizard/Toolbox folder |
| Make this folder the default search location for Toolbox components | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swUseFolderAsDefaultSearchLocation) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swUseFolderAsDefaultSearchLocation, < Value >) | Boolean value | Specifies whether to make the specified Hole Wizard and Toolbox folder the default search location for Toolbox components |
| Toolbox Task Pane - Display Toolbox Favorites folder | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swShowToolboxFavoritesFolder) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swShowToolboxFavoritesFolder, < Value >) | Boolean value | Specifies whether to display the Toolbox Favorites folder |
| Toolbox Mates - Lock rotation of new concentric mates to Toolbox components | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swLockRotationConcentricMates) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swLockRotationConcentricMates, < Value >) | Boolean value |  |
| Hole Wizard settings | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swTransferHoleWizardSizeComboBoxSettings) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swTransferHoleWizardSizeComboBoxSettings, < Value >) | Boolean value | True to preserve settings for each Hole Wizard hole type, false to transfer settings when changing Hole Wizard hole type |
| Include data for DELMIA applications | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swIncludeDataForDelmia) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swIncludeDataForDelmia, < Value >) | Boolean value |  |
