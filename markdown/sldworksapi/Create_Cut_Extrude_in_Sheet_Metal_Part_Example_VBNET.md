---
title: "Create Cut Extrude in Sheet Metal Part Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Cut_Extrude_in_Sheet_Metal_Part_Example_VBNET.htm"
---

# Create Cut Extrude in Sheet Metal Part Example (VB.NET)

This example shows how to create an optimized, normal, cut extrude in a sheet metal part.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Verify that the sheet metal part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the sheet metal part.
' 2. Selects a face.
' 3. Sketches a circle on the selected face.
' 4. Creates Cut-Extrude2, which is an optimized, normal, cut
'    extrude.
' 5. Examine the FeatureManager design tree, graphics area, and
'    Immediate window.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()
        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swFeatureManager As FeatureManager
        Dim swFeature As Feature
	Dim swExtrudeFeatureData As ExtrudeFeatureData2
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer

        swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\2012-sm.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        'Select a face
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByRay(-0.0287275955400048, 0.0301558252805876, 0.00509460972091347, 0.369531106281609, -0.495005022745071, -0.786394804756136, 0.00115698538052806, 2, False, 0, 0)

        'Sketch a circle
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.004122, -0.003029, 0.0#)

        'Create an optimized, normal, cut extrude
        swFeatureManager = swModel.FeatureManager
        swFeature = swFeatureManager.FeatureCut4(True, False, False, 1, 0, 0.01, 0.01, False, False, False, False, 0.0174532925199433, 0.0174532925199433, False, False, False, False, True, True, True, True, True, False, 0, 0, False, True)

        swModel.ClearSelection2(True)
```

```
 	swExtrudeFeatureData = swFeature.GetDefinition
        Debug.Print("Normal cut? " & swExtrudeFeatureData.NormalCut)
	Debug.Print("Geometry optimized? " & swExtrudeFeatureData.OptimizeGeometry)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
