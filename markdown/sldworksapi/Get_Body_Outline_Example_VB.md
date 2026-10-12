---
title: "Get Body Outline Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Body_Outline_Example_VB.htm"
---

# Get Body Outline Example (VBA)

This example shows how to get the outline of a solid body. This example also creates and inserts a sketch of that outline.

```vb
 '-----------------------------------------------------
 ' Preconditions: Open a part document that contains
 ' at least one solid body.
 '
 ' Postconditions: Processes the body outline curves
 ' to remove gaps before sketching the outline.
 '-----------------------------------------------------
Option Explicit
Dim swApp As SldWorks.SldWorks
 Dim swPart As SldWorks.PartDoc
 Dim swModel As SldWorks.ModelDoc2
 Dim swMathVector As SldWorks.MathVector
 Dim swMathUtility As SldWorks.MathUtility
 Dim swModeler As SldWorks.Modeler
 Dim dirVar As Variant
 Dim bVar As Variant
 Dim crvOut As Variant
 Dim topol As Variant
 Dim outline As Variant
 Dim sEva As Variant
 Dim eEva As Variant
 Dim sEvaPrev As Variant
 Dim eEvaPrev As Variant
Dim sEvaNext As Variant
 Dim eEvaNext As Variant
Dim dirArr(0 To 2) As Double
 Dim s As Double
 Dim e As Double
 Dim nCt As Long
 Dim i As Long
 Dim v As Long
Dim isClosed As Boolean
 Dim isPer As Boolean
Enum direction
     X = 1
     Y = 2
     Z = 3
     Xminus = 4
     Yminus = 5
     Zminus = 6
 End Enum
Sub main()
    Set swApp = Application.SldWorks
     Set swPart = swApp.ActiveDoc
     Set swModel = swPart

    'Get the bodies in this part
     bVar = swPart.GetBodies2(swSolidBody, False)
     Set swModeler = swApp.GetModeler
     Set swMathUtility = swApp.GetMathUtility

    'Create the direction vector
     dirArr(0) = 0
     dirArr(1) = 0
     dirArr(2) = 0

    Dim userDirection As direction
     userDirection = Y

    If userDirection = X Then
         dirArr(0) = 1
     ElseIf userDirection = Xminus Then
         dirArr(0) = -1
     ElseIf userDirection = Y Then
         dirArr(1) = 1
     ElseIf userDirection = Yminus Then
         dirArr(1) = -1
     ElseIf userDirection = Z Then
         dirArr(2) = 1
     ElseIf userDirection = Zminus Then
         dirArr(2) = -1
     End If

    dirVar = dirArr

    'Create a MathVector
     Set swMathVector = swMathUtility.CreateVector((dirArr))

    'Get the number of curves in the body outline
     nCt = swModeler.GetBodyOutline2((bVar), swMathVector, 0.00001, True, crvOut, topol, outline)

    'Open a 3D sketch in the part document
     swPart.Insert3DSketch

    'Using the end conditions of the curves, create a 2D sketch of each curve
     Dim vCurve() As Curve
     Dim newCt As Integer

    For i = 0 To nCt - 1
         crvOut(i).GetEndParams s, e, isClosed, isPer
         If crvOut(i).GetLength3(s, e) > 0.00001 Then
             ReDim Preserve vCurve(newCt)
             Set vCurve(newCt) = crvOut(i)

            newCt = newCt + 1
         End If
     Next

    Dim sPoints() As Double
     Dim ePoints() As Double

    ReDim sPoints((newCt * 3) - 1)
     ReDim ePoints((newCt * 3) - 1)

    For i = 0 To newCt - 1
         vCurve(i).GetEndParams s, e, isClosed, isPer
         sEva = vCurve(i).Evaluate(s)
         eEva = vCurve(i).Evaluate(e)

        If i > 0 Then
             v = i - 1
         Else
             v = newCt - 1
         End If

        vCurve(v).GetEndParams s, e, isClosed, isPer
         sEvaPrev = vCurve(v).Evaluate(s)
         eEvaPrev = vCurve(v).Evaluate(e)

        If i < newCt - 1 Then
             v = i + 1
         Else
             v = 0
         End If

        vCurve(v).GetEndParams s, e, isClosed, isPer
         sEvaNext = vCurve(v).Evaluate(s)
         eEvaNext = vCurve(v).Evaluate(e)

        sPoints(i * 3) = sEva(0) + 0.5 * (eEvaPrev(0) - sEva(0))
         sPoints(i * 3 + 1) = sEva(1) + 0.5 * (eEvaPrev(1) - sEva(1))
         sPoints(i * 3 + 2) = sEva(2) + 0.5 * (eEvaPrev(2) - sEva(2))

        ePoints(i * 3) = eEva(0) + 0.5 * (sEvaNext(0) - eEva(0))
         ePoints(i * 3 + 1) = eEva(1) + 0.5 * (sEvaNext(1) - eEva(1))
         ePoints(i * 3 + 2) = eEva(2) + 0.5 * (sEvaNext(2) - eEva(2))

        If userDirection = X Or userDirection = Xminus Then
             sPoints(i * 3) = 0
             ePoints(i * 3) = 0
         ElseIf userDirection = Y Or userDirection = Yminus Then
             sPoints(i * 3 + 1) = 0
             ePoints(i * 3 + 1) = 0
         ElseIf userDirection = Z Or userDirection = Zminus Then
             sPoints(i * 3 + 2) = 0
             ePoints(i * 3 + 2) = 0
         End If
     Next i

    For i = 0 To (newCt * 3) - 1 Step 3
         swModel.CreateLine2 sPoints(i), sPoints(i + 1), sPoints(i + 2), ePoints(i), ePoints(i + 1), ePoints(i + 2)
     Next

    'Insert the sketches
     swModel.InsertSketch2 True
     swModel.ClearSelection2 True
End Sub
```
