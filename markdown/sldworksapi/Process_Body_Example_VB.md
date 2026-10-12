---
title: "Process Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Process_Body_Example_VB.htm"
---

# Process Body Example (VBA)

This example shows how create to a new part with an imported body from the processed body of the original part.

```
'------------------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open a part containing only one solid body.
' 3. Open the Immediate window.
' 4. Run the macro.
'
' Postconditions:
' 1. Creates a new part with an imported body
'    from the processed body of the original part.
' 2. Examine the Immediate window.
'
' NOTE: Differences are best seen in wireframe and with parts
' that contain curved, circular, or both types of faces.
'--------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    ' 1 radian = 180º/p = 57.295779513º or approximately 57.3º
    Const RadPerDeg                 As Double = 1# / 57.3
    Const MaxUAngle                 As Double = 1# * RadPerDeg
    Const MaxVAngle                 As Double = 1# * RadPerDeg
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swBody                      As SldWorks.Body2
    Dim swProcBody                  As SldWorks.Body2
    Dim swPart                      As SldWorks.PartDoc
    Dim swNewPart                   As SldWorks.PartDoc
    Dim swFeat                      As SldWorks.Feature
    Dim vBodies                     As Variant
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swPart = swModel
    vBodies = swPart.GetBodies2(swSolidBody, False)
    Set swBody = vBodies(0)
    Set swProcBody = swBody.GetProcessedBody2(MaxUAngle, MaxVAngle)
```

```
    Set swNewPart = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\part.prtdot", 0, 0, 0)
    Set swFeat = swNewPart.CreateFeatureFromBody3(swProcBody, False, swCreateFeatureBodyCheck)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Body faces            = " & swBody.GetFaceCount
    Debug.Print "  Processed body faces  = " & swProcBody.GetFaceCount
```

```
End Sub
```
