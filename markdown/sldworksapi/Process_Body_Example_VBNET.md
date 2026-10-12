---
title: "Process Body Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Process_Body_Example_VBNET.htm"
---

# Process Body Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        ' 1 radian = 180º/p = 57.295779513º or approximately 57.3
        Const RadPerDeg As Double = 1.0# / 57.3
        Const MaxUAngle As Double = 1.0# * RadPerDeg
        Const MaxVAngle As Double = 1.0# * RadPerDeg

        Dim swModel As ModelDoc2
        Dim swBody As Body2
        Dim swProcBody As Body2
        Dim swPart As PartDoc
        Dim swNewPart As PartDoc
        Dim swFeat As Feature
        Dim vBodies As Object

        swModel = swApp.ActiveDoc
        swPart = swModel
        vBodies = swPart.GetBodies2(swBodyType_e.swSolidBody, False)
        swBody = vBodies(0)
        swProcBody = swBody.GetProcessedBody2(MaxUAngle, MaxVAngle)
        swNewPart = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2013\templates\part.prtdot", 0, 0, 0)
        swFeat = swNewPart.CreateFeatureFromBody3(swProcBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck)
        Debug.Print("File = " & swModel.GetPathName)
        Debug.Print("  Body faces            = " & swBody.GetFaceCount)
        Debug.Print("  Processed body faces  = " & swProcBody.GetFaceCount)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
