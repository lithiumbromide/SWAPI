---
title: "Rotate Move Face Feature Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rotate_MoveFace_Feature_Example_VB.htm"
---

# Rotate Move Face Feature Example (VBA)

This example shows how to rotate (draft) a Move Face feature by changing its XYZ location and rotation angles.

'----------------------------------------------------------------------------
' Preconditions:
' 1. Open a part document that contains a Move Face feature named **Move Face1**.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Rotates (drafts) the Move Face feature.
' 2. Examine the Immediate window.
'----------------------------------------------------------------------------

```vb
Option Explicit

Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeat As SldWorks.Feature
Dim swMoveFaceFeatData As SldWorks.MoveFaceFeatureData
Dim varPara As Variant
Dim newPara(5) As Double
Dim newVarPara As Variant
Dim boolstatus As Boolean
Dim PI As Double
Dim i As Long

Sub main()
```

```vb
' Set PI
PI = 4 * Atn(1)

Set swApp = Application.SldWorks
Set swModel = swApp.ActiveDoc
Set swSelMgr = swModel.SelectionManager
Set swModelDocExt = swModel.Extension

' Select, get, and access Move Face feature
boolstatus = swModelDocExt.SelectByID2("Move Face1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
Set swMoveFaceFeatData = swFeat.GetDefinition
swMoveFaceFeatData.AccessSelections swModel, Nothing

' Get current XYZ origin and rotation angles of Move Face feature
Debug.Print "Before rotating Move Face feature..."
' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
Debug.Print "  Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees"
Debug.Print "  XYZ origin (first 3) and rotation angles (last 3)"
varPara = swMoveFaceFeatData.TriadRotationParameters
For i = LBound(varPara) To UBound(varPara)
    Debug.Print "    " & (varPara(i))
Next i

' New XYZ location and rotation angles for Move Face feature
newPara(0) = 0#
newPara(1) = 0#
newPara(2) = 0#
newPara(3) = 2 * PI / 180 ' Convert radians to degrees
newPara(4) = 2 * PI / 180 ' Convert radians to degrees
newPara(5) = 0#
newVarPara = newPara

' Rotate the Move Face feature
swMoveFaceFeatData.TriadRotationParameters = newVarPara
Debug.Print " "
Debug.Print "After rotating Move Face feature..."
Debug.Print "  Draft angle of Move Face feature: " & swMoveFaceFeatData.Angle * 57.3 & " degrees"
Debug.Print "  XYZ origin (first 3) and rotation angles (last 3)"
newVarPara = swMoveFaceFeatData.TriadRotationParameters
For i = LBound(newVarPara) To UBound(newVarPara)
    Debug.Print "    " & (newVarPara(i))
Next i

' Modify the Move Face feature
swFeat.ModifyDefinition swMoveFaceFeatData, swModel, Nothing
```

```vb
End Sub
```
