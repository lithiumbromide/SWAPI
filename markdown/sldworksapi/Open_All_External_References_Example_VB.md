---
title: "Open All External References Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_All_External_References_Example_VB.htm"
---

# Open All External References Example (VBA)

## Load All External References Example (VBA)

This example shows how to specify to open all external references.

```
'------------------------------------------------------------------
' Preconditions: Open the Immediate window.
'
' Postconditions:
' 1. Changes your SOLIDWORKS Design load all external references system
'    setting to 1 (swLoadExternalReferences_e.swLoadExternalReferences_All),
'    if not already set.
' 2. Examine the Immediate window.
'
' NOTE: This macro changes your SOLIDWORKS Design load external references
' setting.
'-------------------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
```

```
    'Get current external references setting
    Debug.Print "Load external references current setting = " & swApp.GetUserPreferenceIntegerValue(swLoadExternalReferences)
```

```
    ' Open all external references for part, document, and drawing documents
    bRet = swApp.SetUserPreferenceIntegerValue(swLoadExternalReferences, swLoadExternalReferences_e.swLoadExternalReferences_All)
```

```
    ' Get new external references setting
    Debug.Print "Load external references new setting = " & swApp.GetUserPreferenceIntegerValue(swLoadExternalReferences)
```

```
End Sub
```
