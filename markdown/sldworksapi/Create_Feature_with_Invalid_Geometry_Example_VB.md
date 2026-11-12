---
title: "Create Feature with Invalid Geometry Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Feature_with_Invalid_Geometry_Example_VB.htm"
---

# Create Feature with Invalid Geometry Example (VBA)

This example shows how to prompt the user whether to create a feature that has invalid geometry.

```vb
'-------------------------------------
'
' Preconditions: None
'
' Postconditions: If user clicks Yes, then create a feature that has invalid
'                 geometry; if No, then do not create a feature that has invalid
'                 geometry.
'
'-------------------------------------

Option Explicit
Sub main()
    Dim swApp                   As SldWorks.SldWorks
    Dim nResponse               As Integer
    Dim nStatus                 As Long
    Dim bRet                    As Boolean

    Set swApp = Application.SldWorks

    nResponse = MsgBox("Create feature that has invalid geometry?", vbYesNo)
    If nResponse = vbYes Then
        bRet = swApp.AllowFailedFeatureCreation(True)
    Else
        bRet = swApp.AllowFailedFeatureCreation(False)
    End If
End Sub
'-------------------------------------
```
