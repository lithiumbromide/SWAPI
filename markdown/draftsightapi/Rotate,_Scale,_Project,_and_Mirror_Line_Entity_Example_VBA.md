---
title: "Rotate, Scale, Project, and Mirror a Line Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate,_Scale,_Project,_and_Mirror_Line_Entity_Example_VBA.htm"
---

# Rotate, Scale, Project, and Mirror a Line Entity Example (VBA)

This example shows how to use a math transform to rotate, scale, project, and mirror a Line entity.

```vb
 '-----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VBA macro in a software product in which VBA is
 '    embedded.
 ' 2. Copy and paste this example into the Visual Basic IDE.
 ' 3. Add a reference to the DraftSight type library,
 '    install_dir\bin\dsAutomation.dll.
 ' 4. Add a reference to the Microsoft Scripting Runtime library.
 ' 5. Start DraftSight.
 ' 6. Run the macro.
 '
 ' Postconditions:
 ' 1. A Line is drawn, rotated, scaled, projected, and mirrored.
 ' 2. The transformation parameters are printed before
 '    each transformation.
 ' 3. The Line parameters are printed before and after each
 '    transformation.
 '----------------------------------------------------------------
Dim dsApp As DraftSight.Application
Sub Main()
     'Connect to DraftSight
     Set dsApp = GetObject(, "DraftSight.Application")
     'Abort any command currently running in DraftSight
     'to avoid nested commands
     dsApp.AbortRunningCommand
    'Get active document
     Dim dsDoc As DraftSight.Document
     Set dsDoc = dsApp.GetActiveDocument()
     If dsDoc Is Nothing Then
         MsgBox ("There are no open documents in DraftSight.")
         Return
     End If
    'Get math utility
     Dim dsMathUtility As DraftSight.MathUtility
     Set dsMathUtility = dsApp.GetMathUtility()

    'Draw a Line
     Dim dsLine As Line
     Set dsLine = DrawLine(dsDoc)
    'Create different transformations
     Dim transformations As New Scripting.Dictionary
    'Create translation transformation
     Dim dsTranslationVector As DraftSight.MathVector
     Set dsTranslationVector = dsMathUtility.CreateVector(2, 3, 0)
     Dim dsTranslationTransformation As DraftSight.MathTransform
     Set dsTranslationTransformation = dsMathUtility.CreateTransformTranslation(dsTranslationVector)
    transformations.Add "translation", dsTranslationTransformation
     Call TransformLine(dsLine, "translation", transformations)
    'Create scaling transformation
     Dim dsCenterPoint As DraftSight.MathPoint
     Set dsCenterPoint = dsMathUtility.CreatePoint(0, 0, 0)
     Dim scaleFactor As Double
     scaleFactor = 1.2
     Dim dsScalingTransformation As DraftSight.MathTransform
     Set dsScalingTransformation = dsMathUtility.CreateTransformScaling(dsCenterPoint, scaleFactor)
    transformations.Add "scaling", dsScalingTransformation
     Call TransformLine(dsLine, "scaling", transformations)
    'Create rotation transformation
     Dim dsRotationAxis As DraftSight.MathVector
     Set dsRotationAxis = dsMathUtility.CreateVector(0, 0, 1)
     Dim rotationAngle As Double
     rotationAngle = 0.7875
     '45 degrees in radians
     Dim dsRotationTransformation As DraftSight.MathTransform
     Set dsRotationTransformation = dsMathUtility.CreateTransformRotation(dsCenterPoint, dsRotationAxis, rotationAngle)
    transformations.Add "rotation", dsRotationTransformation
     Call TransformLine(dsLine, "rotation", transformations)
    'Create mirror transformation about point
     Dim dsMirrorPoint As DraftSight.MathPoint
     Set dsMirrorPoint = dsMathUtility.CreatePoint(0, 0, 0)
     Dim dsMirrorAboutPointTransformation As DraftSight.MathTransform
     Set dsMirrorAboutPointTransformation = dsMathUtility.CreateTransformMirroringAboutPoint(dsMirrorPoint)
    transformations.Add "mirror about point", dsMirrorAboutPointTransformation
     Call TransformLine(dsLine, "mirror about point", transformations)
    'Create mirror transformation about Line
     Dim dsMirrorLine As DraftSight.MathLine
     Set dsMirrorLine = dsMathUtility.CreateLine(0, 0, 0, 0, 20, 0, dsMathLineType_e.dsMathLineType_Bounded)
     Dim dsMirrorAboutLineTransformation As DraftSight.MathTransform
     Set dsMirrorAboutLineTransformation = dsMathUtility.CreateTransformMirroringAboutLine(dsMirrorLine)
    transformations.Add "mirror about Line", dsMirrorAboutLineTransformation
     Call TransformLine(dsLine, "mirror about Line", transformations)
    'Create mirror transformation about plane
     Dim dsMirrorPlane As DraftSight.MathPlane
     Set dsMirrorPlane = dsMathUtility.CreateZXPlane()
     Dim dsMirrorAboutPlaneTransformation As DraftSight.MathTransform
     Set dsMirrorAboutPlaneTransformation = dsMathUtility.CreateTransformMirroringAboutPlane(dsMirrorPlane)
    transformations.Add "mirror about plane", dsMirrorAboutPlaneTransformation
     Call TransformLine(dsLine, "mirror about plane", transformations)
    'Create projection transformation
     Dim dsProjectionPlane As DraftSight.MathPlane
     Set dsProjectionPlane = dsMathUtility.CreateYZPlane()
     Dim dsProjectionDirection As DraftSight.MathVector
     Set dsProjectionDirection = dsMathUtility.CreateVector(1, 0, 0)
     Dim dsProjectionTransformation As DraftSight.MathTransform
     Set dsProjectionTransformation = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection)
    transformations.Add "projection", dsProjectionTransformation
     Call TransformLine(dsLine, "projection", transformations)
 End Sub
Sub TransformLine(dsLine As DraftSight.Line, keyString As String, transformations As Scripting.Dictionary)

    'Get the transformation by key out of the dictionary
     Dim transform As DraftSight.MathTransform
     Set transform = transformations(keyString)

    'Get MathLine property of Line entity
     Dim dsMathLine As DraftSight.MathLine
     Set dsMathLine = dsLine.MathLine
    'Print mathematical line parameters
     Call PrintMathLineParameters(dsMathLine)
    'Print transformation parameters
     Call PrintMathTransformation(keyString, transform)

     'Transform mathematical line
     dsMathLine.TransformBy transform
    'Update Line
     dsLine.MathLine = dsMathLine
    MsgBox ("The transformation " & keyString & " has been applied to the Line.")
    'Zoom by window
     Dim lowerLeftCorner(0 To 2) As Double
     lowerLeftCorner(0) = -10
     lowerLeftCorner(1) = -10
     lowerLeftCorner(2) = 0
     Dim upperRightCorner(0 To 2) As Double
     upperRightCorner(0) = 10
     upperRightCorner(1) = 10
     upperRightCorner(2) = 0
     dsApp.Zoom dsZoomRange_e.dsZoomRange_Window, lowerLeftCorner, upperRightCorner
    'Print result mathematical line parameters
     Call PrintMathLineParameters(dsMathLine)

End Sub
Function DrawLine(dsDoc As DraftSight.Document) As DraftSight.Line
     'Get model space
     Dim dsModel As DraftSight.Model
     Set dsModel = dsDoc.GetModel()
    'Get sketch manager
     Dim dsSketchMgr As DraftSight.SketchManager
     Set dsSketchMgr = dsModel.GetSketchManager()
    'Draw a Line
     Dim startPoint(0 To 2) As Double
     startPoint(0) = 1
     startPoint(1) = 1
     startPoint(2) = 0
     Dim endPoint(0 To 2) As Double
     endPoint(0) = 5
     endPoint(1) = 1
     endPoint(2) = 0
    Set DrawLine = dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
 End Function
Sub PrintMathTransformation(transformationName As String, dsMathTransformation As DraftSight.MathTransform)
     Debug.Print ("The " & transformationName & " transformation:")
    Dim countOfRows As Long
     countOfRows = 4
     Dim countOfColumns As Long
     countOfColumns = 4

    Dim i As Long
     Dim j As Long
    For i = 0 To countOfRows - 1
         Dim rowInformation As String
         rowInformation = "("
        For j = 0 To countOfColumns - 1
             rowInformation = rowInformation & dsMathTransformation.GetElementAt(i, j)
            If j <> countOfColumns - 1 Then
                 rowInformation = rowInformation & "  ,  "
             End If
         Next
        rowInformation = rowInformation & ");"
        Debug.Print (rowInformation)
     Next
 End Sub
Sub PrintMathLineParameters(dsMathLine As DraftSight.MathLine)
     Debug.Print ("Mathematical line parameters: ")
    Debug.Print ("Type = " & dsMathLine.GetType)
    'Get start point
     Dim dsPoint As DraftSight.MathPoint
     Set dsPoint = dsMathLine.startPoint
    Dim x As Double, y As Double, z As Double
     dsPoint.GetPosition x, y, z
    Debug.Print ("StartPoint: " & x & ", " & y & ", " & z)
    'Get end point
     Set dsPoint = dsMathLine.endPoint
    dsPoint.GetPosition x, y, z
    Debug.Print ("EndPoint: " & x & ", " & y & ", " & z)
    'Get direction
     Dim dsVector As DraftSight.MathVector
     dsMathLine.GetDirection dsVector
    dsVector.GetCoordinates x, y, z
    Debug.Print ("Direction: " & x & ", " & y & ", " & z)
    Debug.Print ("Length = " & dsMathLine.GetLength())
 End Sub
```
