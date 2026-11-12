---
title: "Get Patterned Cosmetic Thread Annotations Data Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VBNET.htm"
---

# Get Patterned Cosmetic Thread Annotations Data Example (VB.NET)

This example shows how to get data for patterned cosmetic thread annotations in a drawing.

```
'--------------------------------------------------------------------------
' Preconditions:
' 1. Open a drawing that contains at least one
'    drawing view with patterned cosmetic thread annotations.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Iterates through the drawing views and prints
'    to the Immediate window the patterned cosmetic
'    thread annotations data in each drawing view.
' 2. Examine the Immediate window.
'--------------------------------------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swMathUtility As MathUtility
        Dim myModel As ModelDoc2
        Dim myDrawing As DrawingDoc
        Dim thisView As View
        Dim thisCThread As CThread

        swMathUtility = swApp.GetMathUtility()
        myModel = swApp.ActiveDoc
        myDrawing = myModel
        myModel.ClearSelection2(True)

        'Traverse annotations of the drawing views in this drawing and look for cosmetic threads
        thisView = myDrawing.GetFirstView()
        While Not thisView Is Nothing
            If thisView.Name = "Sheet1" Then
                Debug.Print("")
            Else
                Debug.Print("View name = " & thisView.Name)
                thisCThread = thisView.GetFirstCThread()
                While Not thisCThread Is Nothing
                    Call processCosmeticThread(myModel, thisCThread)
                    thisCThread = thisCThread.GetNext()
                End While
            End If
            thisView = thisView.GetNextView()
        End While
    End Sub

    Private Sub processCosmeticThread(ByVal myModel As ModelDoc2, ByVal aCThread As CThread)
        Dim cthreadAnno As Annotation
        Dim annoName As String, annoVis As String
        Dim patternedCount As Integer
        Dim vPatternedXform As Object
        Dim i As Integer
        Dim transform As MathTransform
        Dim vTransform As Object
        cthreadAnno = aCThread.GetAnnotation()
        annoName = cthreadAnno.GetName()
        If (cthreadAnno.Visible = swAnnotationVisibilityState_e.swAnnotationHidden) Then
            annoVis = "Hidden"
        Else
            annoVis = "Visible"
        End If
        Debug.Print("  Processing CThread " & annoName & "(" & annoVis & ")")

        'Retrieve information about any patterns made from this cosmetic thread
        patternedCount = aCThread.GetPatternedTransformsCount()
        Debug.Print("   Pattern count = " & patternedCount)
        vPatternedXform = aCThread.PatternedTransforms()
        If Not vPatternedXform Is Nothing Then
            For i = LBound(vPatternedXform) To UBound(vPatternedXform)
                transform = vPatternedXform(i)
                vTransform = transform.ArrayData()
                If Not vTransform Is Nothing Then
                    Debug.Print("    Rotate (" & Format(vTransform(0), "###0.0#####") & " " & Format(vTransform(1), "###0.0#####") & " " & Format(vTransform(2), "###0.0#####"))
                    Debug.Print("            " & Format(vTransform(3), "###0.0#####") & " " & Format(vTransform(4), "###0.0#####") & " " & Format(vTransform(5), "###0.0#####"))
                    Debug.Print("            " & Format(vTransform(6), "###0.0#####") & " " & Format(vTransform(7), "###0.0#####") & " " & Format(vTransform(8), "###0.0#####") & ")")
                    Debug.Print("    Translate " & Format(vTransform(9), "###0.0#####") & " " & Format(vTransform(10), "###0.0#####") & " " & Format(vTransform(11), "###0.0#####"))
                    Debug.Print("")
                End If
            Next i
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
