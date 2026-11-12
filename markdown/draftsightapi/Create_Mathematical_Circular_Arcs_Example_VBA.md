---
title: "Create Mathematical Circular Arcs Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Create_Mathematical_Circular_Arcs_Example_VBA.htm"
---

# Create Mathematical Circular Arcs Example (VBA)

This example shows how to create mathematical circular Arcs.

```
'-------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
'    embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to:
'    install_dir\bin\dsAutomation.dll.
' 4. Start DraftSight.
' 5. Press F5.
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
Option Explicit
```

```
Sub main()
```

```
    Dim dsApp As DraftSight.Application
```

```
    'Connects to DraftSight application
    Set dsApp = GetObject(, "DraftSight.Application")
```

```
    'Aborts any command currently running in DraftSight
    'to avoid nested commands
    dsApp.AbortRunningCommand
```

```
    'Gets active document
    Dim dsDoc As DraftSight.Document
    Set dsDoc = dsApp.GetActiveDocument()
    If dsDoc Is Nothing Then
        MsgBox ("There are no open documents in DraftSight.")
        Return
    End If
```

```
    Dim dsMathUtility As DraftSight.MathUtility
    Set dsMathUtility = dsApp.GetMathUtility()
```

```
    'Creates mathematical circular Arc
    Dim dsCenter As DraftSight.MathPoint
    Set dsCenter = dsMathUtility.CreatePoint(3#, 7#, 0#)
    Dim dsNormal As DraftSight.MathVector
    Set dsNormal = dsMathUtility.CreateVector(1#, 0#, 0#)
    Dim dsRadius As Double
    dsRadius = 2
    Dim RefVector As DraftSight.MathVector
    Set RefVector = dsMathUtility.CreateVector(1#, 0#, 0#)
    Dim dsMathCircArc As DraftSight.MathCircArc
    Set dsMathCircArc = dsMathUtility.CreateCircArc(dsCenter, dsNormal, RefVector, dsRadius, 20, 45)
```

```
    'Gets point on mathematical circular Arc
    'closest to this point
    Dim point As DraftSight.MathPoint
    Set point = dsMathUtility.CreatePoint(3#, 7#, 0#)
    Dim closestPoint As DraftSight.MathPoint
    Set closestPoint = dsMathCircArc.GetClosestPointTo(point)
    Dim X As Double
    Dim Y As Double
    Dim Z As Double
    closestPoint.GetPosition X, Y, Z
    MsgBox ("Closest point of (3, 7, 0) is (" & X & ", " & Y & ", " & Z & ")")
    'Sets radius of mathematical circular Arc
    dsMathCircArc.radius = 6.4
```

```
    'Creates mathematical circular Arc defining a Circle
    'using the specified center, normal, and radius
    Dim center As DraftSight.MathPoint
    Set center = dsMathUtility.CreatePoint(2#, 3.1, 0#)
    Dim normal As DraftSight.MathVector
    Set normal = dsMathUtility.CreateVector(1#, 0#, 0#)
    Dim radius As Double
    radius = 3#
    Dim dsCircle As DraftSight.MathCircArc
    Set dsCircle = dsMathUtility.CreateCircle(center, normal, radius)
```

```
End Sub
```
