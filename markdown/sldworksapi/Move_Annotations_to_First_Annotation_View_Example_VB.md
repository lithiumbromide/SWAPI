---
title: "Move Annotations to Notes Area Annotation View Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Move_Annotations_to_First_Annotation_View_Example_VB.htm"
---

# Move Annotations to Notes Area Annotation View Example (VBA)

```vb
This example shows how to move all annotations to the Notes Area annotation view.
```

```
'----------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\button.sldprt.
' 2. Add a note to the *Top annotation view by double-clicking
'    *Top in the Annotations folder in the FeatureManager design
'    tree and clicking Insert > Annotations > Note. If prompted
'    to turn on feature dimensions display, click No.
' 3. Repeat step 2 to add a note to the *Front annotation view.
' 4. Double-click the Unassigned Items annotation view in the
'    Annotations folder in the FeatureManager design tree.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Examine the Immediate window.
' 2. Double-click each annotation view in the FeatureManager
'    design tree to verify that all annotations were moved
'    from *Front and *Top to Notes Area only. If prompted
'    to turn on feature dimensions display, click No.
'
' NOTE: Because the part is used elsewhere,
' do not save changes when closing the document.
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
Dim annToMove(1) As SldWorks.Annotation
Dim swAnnView As SldWorks.AnnotationView
Dim swAnn As SldWorks.Annotation
Dim swFeat As SldWorks.Feature
Dim swMathTransform As SldWorks.MathTransform
Dim i As Long
Dim j As Long
Dim k As Long
Dim l as Long
Dim planeArray() As Double
Dim nbrPlaneArray as Long
Dim status As Boolean
Dim transformArray() As Double
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelExt = swModel.Extension
```

```
    'Get the annotation views, number of annotation views,
    'their names, and whether the annotation view is
    'hidden (i.e., not activated)
    swAnnViews = swModelExt.AnnotationViews
    Debug.Print "Number of annotation views: " & swModelExt.AnnotationViewCount
    Debug.Print "  Annotation view name: "
    For i = 0 To swModelExt.AnnotationViewCount - 1
        Set swAnnView = swAnnViews(i)
        Set swFeat = swAnnView
        Debug.Print "     " & swFeat.Name
        status = swAnnView.Hide
        'status dependent on whether the annotation view is activated
        'Only Unassigned Items is activated
        Debug.Print "        Hide: " & status
 	Debug.Print "        Flat-pattern view: " & swAnnView.FlatPatternView
    Next
```

```
    'Iterate through each annotation view and its annotations
    'Print each annotation name, its rotation matrix, whether it is
    'shown in the annotation view, and whether it is assigned to a
    '3D view
    'Add all annotations to an array to move them
    k = 0
    l = 0
    Debug.Print ""
    Debug.Print "  Name and number of annotations in annotation view: "
    For i = 0 To swModelExt.AnnotationViewCount - 1
        Set swAnnView = swAnnViews(i)
        swAnnView.Activate
        annotations = swAnnView.GetAnnotations2(False, False)
        Set swFeat = swAnnView
        Debug.Print ""
        Debug.Print "        " & swFeat.Name & " = " & swAnnView.AnnotationCount
        If Not IsEmpty(annotations) Then
            For j = 0 To swAnnView.AnnotationCount - 1
                Set swAnn = annotations(j)
                planeArray = swAnn.GetPlane
                nbrPlaneArray = UBound(planeArray)
                Debug.Print "          Rotation matrix of the annotation relative to the X-Y plane of the model: "
                Do While l < nbrPlaneArray
                    Debug.Print "           " & planeArray(l) & " " & planeArray(l + 1) & " " & planeArray(l + 2)
                    l = l + 3
                Loop
 		Set swMathTransform = swAnn.GetFlipPlaneTransform
		transformArray = swMathTransform.ArrayData()
		If Not IsEmpty(transformArray) Then
			Debug.Print "       Rotation matrix if annotation plane flipped:"
			Debug.Print "        " & transformArray(0) & " " & transformArray(1) & " " & transformArray(2)
			Debug.Print "        " & transformArray(3) & " " & transformArray(4) & " " & transformArray(5)
			Debug.Print "        " & transformArray(6) & " " & transformArray(7) & " " & transformArray(8)
			Debug.Print "       Translation component if annotation plane flipped:"
			Debug.Print "        " & transformArray(9) & " " & transformArray(10) & " " & transformArray(11)
			Debug.Print
		End If
                l = 0
                If k >= 0 Then
                    Set annToMove(k) = swAnn
                    k = k + 1
                End If
                Debug.Print "          Annotation names:"
                Debug.Print "            " & swAnn.GetName
                status = swAnnView.IsShown
                Debug.Print "               Shown in this annotation view: " & status
                status = swAnnView.UnassignedView
                Debug.Print "                  Assigned to a 3D View: " & status
            Next
        End If
    Next
```

```
    'Move all annotations to the Notes Area annotation view
    Debug.Print ""
    Debug.Print "Move all annotations to Notes Area annotation view:"
    For i = 0 To swModelExt.AnnotationViewCount - 1
        Set swAnnView = swAnnViews(i)
        swAnnView.Activate
        Set swFeat = swAnnView
        If swFeat.Name = "Notes Area" Then
            status = swAnnView.MoveAnnotations(annToMove)
            Debug.Print "  Annotations moved: " & status
            status = swAnnView.Show
            'status should be false because annotation was activated
            Debug.Print "    Show: " & status
        End If
    Next
```

```
End Sub
```
