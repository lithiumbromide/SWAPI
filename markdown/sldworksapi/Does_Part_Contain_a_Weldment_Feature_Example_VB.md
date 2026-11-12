---
title: "Does Part Contain a Weldment Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Does_Part_Contain_a_Weldment_Feature_Example_VB.htm"
---

# Does Part Contain a Weldment Feature Example (VBA)

This example shows how to query a part document to find out if it contains a weldment feature.

```vb
'------------------------------------------------------------
'
' Preconditions: A model document containing a part is open.
'
' Postconditions: None
'
'------------------------------------------------------------
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swPartDoc As SldWorks.PartDoc
Dim retVal As Boolean

Sub main()

Set swApp = Application.SldWorks
Set swPartDoc = swApp.ActiveDoc
retVal = swPartDoc.IsWeldment
Debug.Print "Does this part contain a weldment feature? " & retVal

End Sub
```
