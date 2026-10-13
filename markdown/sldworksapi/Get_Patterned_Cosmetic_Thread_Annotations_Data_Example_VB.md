---
title: "Get Patterned Cosmetic Thread Annotations Data Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Patterned_Cosmetic_Thread_Annotations_Data_Example_VB.htm"
---

# Get Patterned Cosmetic Thread Annotations Data Example (VBA)

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
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swMathUtility As SldWorks.MathUtility
```

```
Sub main()
```

```
    Dim myModel As SldWorks.ModelDoc2
    Dim myDrawing As SldWorks.DrawingDoc
    Dim thisView As SldWorks.View
    Dim thisCThread As SldWorks.CThread
```

```
    Set swApp = Application.SldWorks
    Set swMathUtility = swApp.GetMathUtility()
    Set myModel = swApp.ActiveDoc
    Set myDrawing = myModel
    myModel.ClearSelection2 True
```

```
   'Traverse annotations of the drawing views in this drawing and look for cosmetic threads
    Set thisView = myDrawing.GetFirstView()
    While Not thisView Is Nothing
    If thisView.Name = "Sheet1" Then
        Debug.Print
    Else
            Debug.Print "View name = " & thisView.Name
            Set thisCThread = thisView.GetFirstCThread()
            While Not thisCThread Is Nothing
                Call processCosmeticThread(myModel, thisCThread)
                Set thisCThread = thisCThread.GetNext()
            Wend
    End If
        Set thisView = thisView.GetNextView()
    Wend
End Sub
```

```
Private Sub processCosmeticThread(myModel As SldWorks.ModelDoc2, aCThread As SldWorks.CThread)
    Dim cthreadAnno As SldWorks.Annotation
    Dim annoName As String, annoVis As String
    Dim patternedCount As Long
    Dim vPatternedXform As Variant
    Dim i As Integer
    Dim transform As SldWorks.MathTransform
    Dim vTransform As Variant
```

```
    Set cthreadAnno = aCThread.GetAnnotation()
    annoName = cthreadAnno.GetName()
    If (cthreadAnno.Visible = SwConst.swAnnotationHidden) Then
        annoVis = "Hidden"
    Else
        annoVis = "Visible"
    End If
```

```
    Debug.Print "  Processing CThread " & annoName & "(" & annoVis & ")"
```

```
    'Retrieve information about any patterns made from this cosmetic thread
    patternedCount = aCThread.GetPatternedTransformsCount()
    Debug.Print "   Pattern count = " & patternedCount
    vPatternedXform = aCThread.PatternedTransforms()
    If Not IsEmpty(vPatternedXform) Then
        For i = LBound(vPatternedXform) To UBound(vPatternedXform)
            Set transform = vPatternedXform(i)
            vTransform = transform.ArrayData()
            If Not IsEmpty(vTransform) Then
                Debug.Print "    Rotate (" & Format(vTransform(0), "###0.0#####") & " " & Format(vTransform(1), "###0.0#####") & " " & Format(vTransform(2), "###0.0#####")
                Debug.Print "            " & Format(vTransform(3), "###0.0#####") & " " & Format(vTransform(4), "###0.0#####") & " " & Format(vTransform(5), "###0.0#####")
                Debug.Print "            " & Format(vTransform(6), "###0.0#####") & " " & Format(vTransform(7), "###0.0#####") & " " & Format(vTransform(8), "###0.0#####") & ")"
                Debug.Print "    Translate " & Format(vTransform(9), "###0.0#####") & " " & Format(vTransform(10), "###0.0#####") & " " & Format(vTransform(11), "###0.0#####")
                Debug.Print
            End If
        Next i
    End If
End Sub
```
