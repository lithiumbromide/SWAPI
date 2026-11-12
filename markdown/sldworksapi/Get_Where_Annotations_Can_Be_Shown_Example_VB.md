---
title: "Get Where Annotations Can be Shown Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Where_Annotations_Can_Be_Shown_Example_VB.htm"
---

# Get Where Annotations Can be Shown Example (VBA)

This example shows how to get the names of the annotation views where an annotation can be shown.

```
'----------------------------------------------
' Preconditions:
' 1. Open a part document with one or more annotations
'    in one or more annotation views.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the annotation views.
' 2. Iterates through the annotation views and annotations.
' 3. Prints the name of each annotation view and number of
'    annotations in that annotation view.
' 4. Prints whether each annotation in that annotation view
'    can be shown in the other annotation views and in
'    multiple annotation views.
' 5. Examine the Immediate window.
'----------------------------------------------
```

```
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelExt As SldWorks.ModelDocExtension
Dim swAnnViews As Variant
Dim annotations As Variant
Dim swAnnView As SldWorks.AnnotationView
Dim swAnn As SldWorks.Annotation
Dim swFeat As SldWorks.Feature
Dim i As Long
Dim j As Long
Dim k As Long
Dim nbrAnnotations As Long
```

```
Sub main()
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelExt = swModel.Extension
```

```
    'Get the annotation views
    swAnnViews = swModelExt.AnnotationViews
    For i = 0 To swModelExt.AnnotationViewCount - 1
        Set swAnnView = swAnnViews(i)
    Next
    Debug.Print "Number of annotation views = " & swModelExt.AnnotationViewCount
    Debug.Print ""
```

```
    'Iterate through the annotation views and annotations
    'Print the name of each annotation view and number of annotations
    'in that annotation view
    'Print whether each annotation in that annotation view
    'can be shown in the other annotation views and in
    'multiple annotation views
    Debug.Print "  Name of annotation view and number of annotations in the annotation view "
    Debug.Print ""
    For i = 0 To swModelExt.AnnotationViewCount - 1
        Set swAnnView = swAnnViews(i)
        swAnnView.Activate
        annotations = swAnnView.GetAnnotations2(False, False)
        Set swFeat = swAnnView
        nbrAnnotations = swAnnView.AnnotationCount
        If nbrAnnotations > 0 Then
          Debug.Print ""
        End If
        Debug.Print "        " & swFeat.Name & " = " & nbrAnnotations
                If Not IsEmpty(annotations) Then
                        j = 0
                        For j = 0 To nbrAnnotations - 1
                                Debug.Print "          Can show annotation " & j + 1 & " in these annotation views: "
                                Set swAnn = annotations(j)
                                For k = 0 To swModelExt.AnnotationViewCount - 1
                                    Set swAnnView = swAnnViews(k)
                                    Set swFeat = swAnnView
                                    Debug.Print "              " & swFeat.Name & " = " & swAnn.CanShowInAnnotationView(swFeat.Name)
                                Next k
                                Debug.Print "              multiple = " & swAnn.CanShowInMultipleAnnotationViews()
                                Debug.Print ""
                        Next j
                End If
    Next i
```

```
End Sub
```
