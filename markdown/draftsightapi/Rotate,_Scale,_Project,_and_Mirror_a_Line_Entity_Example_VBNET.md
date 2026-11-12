---
title: "Rotate, Scale, Project, and Mirror a Line Entity Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "draftsightapi/Rotate,_Scale,_Project,_and_Mirror_a_Line_Entity_Example_VBNET.htm"
---

# Rotate, Scale, Project, and Mirror a Line Entity Example (VB.NET)

This example shows how to use a math transform to rotate, scale, project, and mirror a Line entity.

```vb
 '--------------------------------------------------------------
 ' Preconditions:
 ' 1. Create a VB.NET Windows console project.
 ' 2. Copy and paste this project into the VB.NET IDE.
 ' 3. Add a reference to:
 '    install_dir\APISDK\tlb\DraftSight.Interop.dsAutomation.
 ' 4. Add references to System and System.Windows.Forms.
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
 Imports System.Collections.Generic
 Imports System.Text
 Imports DraftSight.Interop.dsAutomation
 Imports System.Windows.Forms
 Imports System.Runtime.InteropServices
 Imports System.Diagnostics

 Module Module1
     Dim dsApp As DraftSight.Interop.dsAutomation.Application

     Sub Main(ByVal args As String())
         'Connect to DraftSight application
         dsApp = ConnectToDraftSight()
         If dsApp Is Nothing Then
             Return
         End If

         dsApp.AbortRunningCommand() ' abort any command currently running in DraftSight to avoid nested commands

         'Get active document
         Dim dsDoc As Document = dsApp.GetActiveDocument()
         If dsDoc Is Nothing Then
             MessageBox.Show("There are no open documents in DraftSight.")
             Return
         End If

         'Get math utility
         Dim dsMathUtility As MathUtility = dsApp.GetMathUtility()

         'Create different transformations
         Dim transformations As Dictionary(Of String, MathTransform) = CreateDifferentTransformations(dsMathUtility)

         'Draw a Line
         Dim dsLine As Line = DrawLine(dsDoc)

         TransformLine(dsLine, transformations)
     End Sub

     Function CreateDifferentTransformations(ByVal dsMathUtility As MathUtility) As Dictionary(Of String, MathTransform)
         Dim transformations As New Dictionary(Of String, MathTransform)()

         'Create translation transformation
         Dim dsTranslationVector As MathVector = dsMathUtility.CreateVector(2, 3, 0)
         Dim dsTranslationTransformation As MathTransform = dsMathUtility.CreateTransformTranslation(dsTranslationVector)

         transformations.Add("translation", dsTranslationTransformation)

         'Create scaling transformation
         Dim dsCenterPoint As MathPoint = dsMathUtility.CreatePoint(0, 0, 0)
         Dim scaleFactor As Double = 1.2
         Dim dsScalingTransformation As MathTransform = dsMathUtility.CreateTransformScaling(dsCenterPoint, scaleFactor)

         transformations.Add("scaling", dsScalingTransformation)

         'Create rotation transformation
         Dim dsRotationAxis As MathVector = dsMathUtility.CreateVector(0, 0, 1)
         Dim rotationAngle As Double = Math.PI / 4
         '45 degrees in radians
         Dim dsRotationTransformation As MathTransform = dsMathUtility.CreateTransformRotation(dsCenterPoint, dsRotationAxis, rotationAngle)

         transformations.Add("rotation", dsRotationTransformation)

         'Create mirror transformation about point
         Dim dsMirrorPoint As MathPoint = dsMathUtility.CreatePoint(0, 0, 0)
         Dim dsMirrorAboutPointTransformation As MathTransform = dsMathUtility.CreateTransformMirroringAboutPoint(dsMirrorPoint)

         transformations.Add("mirror about point", dsMirrorAboutPointTransformation)

         'Create mirror transformation about Line
         Dim dsMirrorLine As MathLine = dsMathUtility.CreateLine(0, 0, 0, 0, 20, 0, _
          dsMathLineType_e.dsMathLineType_Bounded)
         Dim dsMirrorAboutLineTransformation As MathTransform = dsMathUtility.CreateTransformMirroringAboutLine(dsMirrorLine)

         transformations.Add("mirror about Line", dsMirrorAboutLineTransformation)

         'Create mirror transformation about plane
         Dim dsMirrorPlane As MathPlane = dsMathUtility.CreateZXPlane()
         Dim dsMirrorAboutPlaneTransformation As MathTransform = dsMathUtility.CreateTransformMirroringAboutPlane(dsMirrorPlane)

         transformations.Add("mirror about plane", dsMirrorAboutPlaneTransformation)

         'Create projection transformation
         Dim dsProjectionPlane As MathPlane = dsMathUtility.CreateYZPlane()
         Dim dsProjectionDirection As MathVector = dsMathUtility.CreateVector(1, 0, 0)
         Dim dsProjectionTransformation As MathTransform = dsMathUtility.CreateTransformProjection(dsProjectionPlane, dsProjectionDirection)

         transformations.Add("projection", dsProjectionTransformation)

         Return transformations
     End Function

     Sub TransformLine(ByVal dsLine As Line, ByVal transformations As Dictionary(Of String, MathTransform))
         'Get MathLine property of Line entity
         Dim dsMathLine As MathLine = dsLine.MathLine

         'Print mathematical line parameters
         PrintMathLineParameters(dsMathLine)

         'Transform Line using the created transformations
         For Each transformationItem As KeyValuePair(Of String, MathTransform) In transformations
             'Print transformation parameters
             PrintMathTransformation(transformationItem.Key, transformationItem.Value)

             'Transform mathematical line
             dsMathLine.TransformBy(transformationItem.Value)

             'Update Line
             dsLine.MathLine = dsMathLine

             MessageBox.Show("The " & transformationItem.Key & " transformation has been applied to a Line.")

             'Zoom by window
             Dim lowerLeftCorner As Double() = {-10, -10, 0}
             Dim upperRightCorner As Double() = {10, 10, 0}
             dsApp.Zoom(dsZoomRange_e.dsZoomRange_Window, lowerLeftCorner, upperRightCorner)

             'Print result mathematical line parameters
             PrintMathLineParameters(dsMathLine)
         Next
     End Sub

     Function DrawLine(ByVal dsDoc As Document) As Line
         'Get model space
         Dim dsModel As Model = dsDoc.GetModel()

         'Get sketch manager
         Dim dsSketchMgr As SketchManager = dsModel.GetSketchManager()

         'Draw a Line
         Dim startPoint As Double() = {1, 1, 0}
         Dim endPoint As Double() = {5, 1, 0}

         Return dsSketchMgr.InsertLine(startPoint(0), startPoint(1), startPoint(2), endPoint(0), endPoint(1), endPoint(2))
     End Function

     Sub PrintMathTransformation(ByVal transformationName As String, ByVal dsMathTransformation As MathTransform)
         Debug.Print(Environment.NewLine   "The " & transformationName & " transformation:")

         Dim countOfRows As Integer = 4
         Dim countOfColumns As Integer = 4

         For i As  Integer = 0  To countOfRows - 1
             Dim rowInformation As String = "("

             For j As  Integer = 0  To countOfColumns - 1
                 rowInformation += dsMathTransformation.GetElementAt(i, j).ToString()

                 If j <> countOfColumns - 1 Then
                     rowInformation += "  ,  "
                 End If
             Next

             rowInformation +=  ");"

             Debug.Print(rowInformation)
         Next
     End Sub

     Sub PrintMathLineParameters(ByVal dsMathLine As MathLine)
         Debug.Print(Environment.NewLine   "Mathematical line parameters")

         Debug.Print(String.Format("Type = {0};", dsMathLine.[GetType]().ToString()))

         'Get start point
         Dim dsPoint As MathPoint = dsMathLine.StartPoint

         Dim x As  Double, y  As  Double, z  As  Double
         dsPoint.GetPosition(x, y, z)

         Debug.Print(String.Format("StartPoint ({0}, {1}, {2});", x, y, z))

         'Get end point
         dsPoint = dsMathLine.EndPoint

         dsPoint.GetPosition(x, y, z)

         Debug.Print(String.Format("EndPoint ({0}, {1}, {2});", x, y, z))

         'Get direction
         Dim dsVector As MathVector = Nothing
         dsMathLine.GetDirection(dsVector)

         dsVector.GetCoordinates(x, y, z)

         Debug.Print(String.Format("Direction ({0}, {1}, {2});", x, y, z))

         Debug.Print(String.Format("Length = {0};", dsMathLine.GetLength().ToString()))
     End Sub

     Function ConnectToDraftSight() As DraftSight.Interop.dsAutomation.Application
         Dim dsApp As DraftSight.Interop.dsAutomation.Application =  Nothing

         Try
             'Connect to DraftSight
             dsApp =  DirectCast(Marshal.GetActiveObject("DraftSight.Application"), DraftSight.Interop.dsAutomation.Application)
         Catch ex As Exception
             MessageBox.Show("Failed to connect to DraftSight. Cause: " & ex.Message)
             dsApp = Nothing
         End Try

         Return dsApp
     End Function
 End Module
```
