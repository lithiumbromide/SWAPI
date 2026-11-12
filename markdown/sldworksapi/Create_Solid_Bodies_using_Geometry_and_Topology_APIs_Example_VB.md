---
title: "Create Solid Bodies Using Geometry and Topology Methods Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Solid_Bodies_using_Geometry_and_Topology_APIs_Example_VB.htm"
---

# Create Solid Bodies Using Geometry and Topology Methods Example (VBA)

This example shows how to create a solid body using SOLIDWORKS geometry and topology methods.

```
'--------------------------------------------------
' Preconditions: Verify that the specified part
' document template exists.
'
' Postconditions:
' 1. Opens a new part document.
' 2. Creates a part containing a single solid
'    body feature that is the union of a box and
'    a cone.
' 3. Examine the graphics area and FeatureManager
'    design tree.
'--------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModeler As SldWorks.Modeler
    Dim swFeat As SldWorks.Feature
    Dim nConeParam(8) As Double
    Dim vConeArr As Variant
    Dim swConeBody As SldWorks.Body2
    Dim nBoxParam(8) As Double
    Dim vBoxArr As Variant
    Dim swBoxBody As SldWorks.Body2
    Dim vNewBodyArr As Variant
    Dim vNewBody As Variant
    Dim swNewPart As SldWorks.PartDoc
    Dim swNewBody As SldWorks.Body2
    Dim swFaultEnt As SldWorks.FaultEntity
    Dim nRetVal As Long
    Dim nCount As Long
```

```
    ' Form cone
    ' Face center
    nConeParam(0) = 0#
    nConeParam(1) = 0.1
    nConeParam(2) = 0#
    ' Axis
    nConeParam(3) = 0#
    nConeParam(4) = 0#
    nConeParam(5) = 1#
    ' Base radius
    nConeParam(6) = 0.2
    ' Top radius
    nConeParam(7) = 0.1
    ' Height
    nConeParam(8) = 0.3
    vConeArr = nConeParam
```

```
    ' Form box
    ' Face center
    nBoxParam(0) = 0#
    nBoxParam(1) = 0.1
    nBoxParam(2) = 0.2
    ' Axis
    nBoxParam(3) = 0#
    nBoxParam(4) = 0#
    nBoxParam(5) = 1#
    ' Width
    nBoxParam(6) = 0.3
    ' Length
    nBoxParam(7) = 0.25
    'Height
    nBoxParam(8) = 0.4
    vBoxArr = nBoxParam
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModeler = swApp.GetModeler
    Set swConeBody = swModeler.CreateBodyFromCone((vConeArr))
    Set swBoxBody = swModeler.CreateBodyFromBox((vBoxArr))
```

```
    Set swFaultEnt = swConeBody.Check3
    nCount = swFaultEnt.Count
    If nCount <> 0 Then
        Debug.Print "Faulty cone!"
        Exit Sub
    End If
```

```
    Set swFaultEnt = swBoxBody.Check3
    nCount = swFaultEnt.Count
    If nCount <> 0 Then
        Debug.Print "Faulty box!"
        Exit Sub
    End If
```

```
    vNewBodyArr = swConeBody.Operations2(swBodyOperationType_e.SWBODYADD, swBoxBody, nRetVal)
```

```
    Set swNewPart = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2015\templates\Part.prtdot", 0, 0, 0)
```

```
    For Each vNewBody In vNewBodyArr
        Set swNewBody = vNewBody
        ' Create solid body feature
        Set swFeat = swNewPart.CreateFeatureFromBody3(swNewBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify)
    Next
```

```
    Set swModel = swNewPart
    swModel.ViewZoomtofit2
```

```
End Sub
```
