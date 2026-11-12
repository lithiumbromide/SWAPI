---
title: "System Options > 3DEXPERIENCE Integration"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_3DEXP_Integration.htm"
---

# System Options > 3DEXPERIENCE Integration

This dialog is only available in SOLIDWORKS Design connected to the 3DEXPERIENCE platform.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Update SOLIDWORKS files for compatibility with the 3D EXPERIENCE platform | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnable3DEXPERIENCEFileCompatibilityUpdate) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnable3DEXPERIENCEFileCompatibilityUpdate, < OnFlag >) | Boolean value | This option is enabled only when no documents are open |
