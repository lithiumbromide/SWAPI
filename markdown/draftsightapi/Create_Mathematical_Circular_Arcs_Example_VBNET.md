---
title: "Create Mathematical Circular Arcs Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Mathematical_Circular_Arcs_Example_VBNET.htm"
---

# Create Mathematical Circular Arcs Example (VB.NET)

This example shows how to create mathematical circular Arcs.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Create a VB.NET Windows console project.
' 2. Copy and paste this example into the VB.NET IDE.
' 3. Add a reference to:
'    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.dll.
' 4. Add a reference to System.Windows.Forms.
' 5. Start DraftSight.
' 6. Press F5.
'
' Postconditions:
' 1. Connects to DraftSight.
' 2. Gets the active document.
' 3. Creates a mathematical circular Arc.
' 4. Gets the point on the mathematical circular Arc
'    closest to a mathematical point. Click OK to close
'    the message box.
' 5. Sets the radius for the mathematical circular Arc.
' 6. Creates a mathematical circular Arc.
' 7. Sets the radius for the mathematical circular Arc.
'----------------------------------------------------------------

Imports System
Imports DraftSight.Interop.dsAutomation
Imports System.Runtime.InteropServices
Imports System.Windows.Forms

Module Module1

    Sub Main()
        Dim dsApp As DraftSight.Interop.dsAutomation.Application

        'Connects to DraftSight application
        dsApp = DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)

        If dsApp Is Nothing Then
            Return
        End If

        'Aborts any command currently running in DraftSight
        'to avoid nested commands
        dsApp.AbortRunningCommand()

        'Gets active document
        Dim dsDoc As Document = dsApp.GetActiveDocument()
        If dsDoc Is Nothing Then
            MessageBox.Show("There are no open documents in DraftSight.")
            Return
        End If

        Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()

        'Creates mathematical circular Arc
        Dim dsCenter As MathPoint = dsMathUtility.CreatePoint(3.0, 7.0, 0.0)
        Dim dsNormal As MathVector = dsMathUtility.CreateVector(1.0, 0.0, 0.0)
        Dim dsRadius As Double = 2
        Dim RefVector As MathVector = dsMathUtility.CreateVector(1.0, 0.0, 0.0)
        Dim dsMathCircArc As MathCircArc = dsMathUtility.CreateCircArc(dsCenter, dsNormal, RefVector, dsRadius, 20, 45)

        'Gets point on mathematical circular Arc
        'closest to this point
        Dim point As MathPoint = dsMathUtility.CreatePoint(3.0, 7.0, 0.0)
        Dim closestPoint As MathPoint = dsMathCircArc.GetClosestPointTo(point)
        Dim X As Double, Y As Double, Z As Double
        closestPoint.GetPosition(X, Y, Z)
        MessageBox.Show("Closest point of (3, 7, 0) is (" + CType(X, String) + ", " + CType(Y, String) + ", " + CType(Z, String) + ")")
        'Sets radius of mathematical circular Arc
        dsMathCircArc.Radius = 6.4

        'Creates mathematical circular Arc defining a Circle
        'using the specified center, normal, and radius
        Dim center As MathPoint = dsMathUtility.CreatePoint(2.0, 3.1, 0.0)
        Dim normal As MathVector = dsMathUtility.CreateVector(1.0, 0.0, 0.0)
        Dim radius As Double = 3.0
        Dim circle As MathCircArc = dsMathUtility.CreateCircle(center, normal, radius)

    End Sub
End Module
```
