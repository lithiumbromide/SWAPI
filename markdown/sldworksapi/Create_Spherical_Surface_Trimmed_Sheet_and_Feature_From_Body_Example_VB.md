---
title: "Create Spherical Surface, Trimmed Sheet, and Feature from Body Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Spherical_Surface_Trimmed_Sheet_and_Feature_From_Body_Example_VB.htm"
---

# Create Spherical Surface, Trimmed Sheet, and Feature from Body Example (VBA)

This example shows how to create a spherical surface, a trimmed sheet, and a feature from a body.

'===========================================

'Preconditions:

'1. Open a new part.

'2. Run the macro to the Stop.

'3. Press F5 to create the imported feature.

'

'Postconditions:

'1. Creates a temporary body and displays it.

'2. Uses the temporary body to create **Surface-Imported1**

' in the FeatureManager design tree.

'===========================================

Const RADIUS As Double = 0.01

Dim swApp As SldWorks.SldWorks

Dim swPart As SldWorks.PartDoc

Dim swSurf As SldWorks.Surface

Dim swBody As SldWorks.Body2

Dim swFeat As SldWorks.Feature

Dim swModeler As SldWorks.Modeler

Option Explicit

Sub main()

Set swApp = Application.SldWorks

Set swPart = swApp.**ActiveDoc**

Set swModeler = swApp.**GetModeler**

Dim dCenter(2) As Double

dCenter(0) = 0: dCenter(1) = 0: dCenter(2) = 0

Dim dAxis(2) As Double

dAxis(0) = 0: dAxis(1) = 0: dAxis(2) = 1

Dim dRef(2) As Double

dRef(0) = 1: dRef(1) = 0: dRef(2) = 0

Set swSurf = swModeler.**CreateSphericalSurface2**(dCenter, dAxis, dRef, RADIUS)

' No trimming curves are required, so pass one Nothing in the Curves parameter array

' of ISurface::CreateTrimmedSheet5

Dim ZeroTrimmingCurves(0 To 0) As SldWorks.Curve

Set ZeroTrimmingCurves(0) = Nothing

Set swBody = swSurf.**CreateTrimmedSheet5**(ZeroTrimmingCurves, True, 0.00001)

swBody.**Display3** swPart, RGB(255, 255, 0), swTempBodySelectOptions_e.swTempBodySelectable

Stop

Set swFeat = swPart.**CreateFeatureFromBody3**(swBody, False, swCreateFeatureBodyOpts_e.swCreateFeatureBodyCheck + swCreateFeatureBodyOpts_e.swCreateFeatureBodySimplify)

End Sub
