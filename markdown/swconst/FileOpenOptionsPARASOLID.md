---
title: "System Options > Import > Parasolid"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/FileOpenOptionsPARASOLID.htm"
---

# System Options > Import > Parasolid

To display the dialog:

Select **Tools > Options > System Options > Import > File Format > Parasolid**.

- or -

1. Select **File > Open**.
2. In **Files of type**, select **Parasolid**.
3. Click **Options**.

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Apply templates during Parasolid import | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swImportPSEnableTemplates) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swImportPSEnableTemplates, < OnFlag >) | Boolean value |  |
