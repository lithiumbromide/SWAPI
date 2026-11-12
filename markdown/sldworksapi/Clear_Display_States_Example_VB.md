---
title: "Clear Display States Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Clear_Display_States_Example_VB.htm"
---

# Clear Display States Example (VBA)

This example shows how to clear the display states from a part. This example also shows how to remove appearances and show any hidden features.

```
'----------------------------------------------------------------------------
' Preconditions: Open a part document that has any of the following:
' * appearances
' * linked display states
' * hidden features
'
' Postconditions:
' 1. Removes appearances from all configurations of the part.
' 2. Clears display states from all configurations.
' 3. Shows hidden features.
' ---------------------------------------------------------------------------
Option Explicit
```

```vb
Dim swApp As SldWorks.SldWorks
 Dim modelDoc As SldWorks.ModelDoc2
 Dim partDoc As SldWorks.PartDoc
 Dim boolstatus As Boolean

 Sub main()
     Set swApp = Application.SldWorks
     Set modelDoc = swApp.ActiveDoc
     Set partDoc = modelDoc
     boolstatus = partDoc.RemoveAllDisplayStates
 End Sub
```
