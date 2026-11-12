---
title: "Get Mates and Mate Entities Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mates_and_Mate_Entities_Example_VB.htm"
---

# Get Mates and Mate Entities Example (VBA)

This example shows how to iterate through a FeatureManager design tree and get all of an assembly's mates and mate entities.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified assembly document.
' 2. Iterates through the FeatureManager design tree find
'    and print Mates feature to the Immediate window.
' 3. Iterates through the subfeatures of Mates and prints each mate
'    entity's information to the Immediate window.
' 4. Examine the Immediate window.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swFeat As SldWorks.Feature
Dim swMateFeat As SldWorks.Feature
Dim swSubFeat As SldWorks.Feature
Dim swMate As SldWorks.Mate2
Dim swComp As SldWorks.Component2
Dim swMateEnt(2) As SldWorks.MateEntity2
Dim fileName As String
Dim errors As Long
Dim warnings As Long
Dim i As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\simple-block.sldasm"
    Set swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocASSEMBLY, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
```

```
    'Get the first feature in the assembly
    Set swFeat = swModel.FirstFeature
```

```
    'Iterate over features in FeatureManager design tree
    Do While Not swFeat Is Nothing
        If "MateGroup" = swFeat.GetTypeName Then
            Set swMateFeat = swFeat
            Exit Do
        End If
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    Debug.Print "  " & swMateFeat.Name
    Debug.Print ""
```

```
    'Get first mate, which is a subfeature
    Set swSubFeat = swMateFeat.GetFirstSubFeature
    Do While Not swSubFeat Is Nothing
       Set swMate = swSubFeat.GetSpecificFeature2
        If Not swMate Is Nothing Then
            For i = 0 To 1
                Set swMateEnt(i) = swMate.MateEntity(i)
                Debug.Print "    " & swSubFeat.Name
                Debug.Print "      Type              = " & swMate.Type
                Debug.Print "      Alignment         = " & swMate.Alignment
                Debug.Print "      Can be flipped    = " & swMate.CanBeFlipped
                Debug.Print ""
                Set swComp = swMateEnt(i).ReferenceComponent
                Debug.Print "      Component         = " & swComp.Name2
                Debug.Print "      Mate entity type  = " & swMateEnt(i).ReferenceType
                Debug.Print "      (x,y,z)           = (" & swMateEnt(i).EntityParams(0) & ", " & swMateEnt(i).EntityParams(1) & ", " & swMateEnt(i).EntityParams(2) & ")"
                Debug.Print "      (i,j,k)           = (" & swMateEnt(i).EntityParams(3) & ", " & swMateEnt(i).EntityParams(4) & ", " & swMateEnt(i).EntityParams(5) & ")"
                Debug.Print "      Radius 1          = " & swMateEnt(i).EntityParams(6)
                Debug.Print "      Radius 2          = " & swMateEnt(i).EntityParams(7)
                Debug.Print ""
            Next i
            Debug.Print " "
        End If
        ' Get the next mate in MateGroup
        Set swSubFeat = swSubFeat.GetNextSubFeature
    Loop
```

```
End Sub
```
