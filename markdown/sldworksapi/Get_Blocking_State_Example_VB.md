---
title: "Get Blocking State Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Blocking_State_Example_VB.htm"
---

# Get Blocking State Example (VBA)

This example shows how to get the blocking state for a model document.

```vb
'----------------------------------------------------
'
' Preconditions: Model document is open.
'
' Postconditions: None
'
'----------------------------------------------------
Option Explicit
Public Enum swBlockingStates_e
    swNoBlock = &H0
    swFullBlock = &H1
    swModifyBlock = &H2
    swPartialModifyBlock = &H3
    swEditorBlock = &H4
End Enum
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim swModel                 As SldWorks.ModelDoc2

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Debug.Print "BlockingState = " & swModel.GetBlockingState
End Sub
'----------------------------------------------------
```
