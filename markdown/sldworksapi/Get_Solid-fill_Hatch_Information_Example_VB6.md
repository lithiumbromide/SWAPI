---
title: "Get Solid-fill Hatch Information Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Solid-fill_Hatch_Information_Example_VB6.htm"
---

# Get Solid-fill Hatch Information Example (VBA)

This example shows how to get information about solid-fill hatches in a detail view in the current drawing sheet.

```
'-----------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\introsw\bolt-assembly.slddrw.
' 2. Verify that c:\temp exists.
' 3. Create a detail view of Section View A-A:
'    a. Click Insert > Drawing View > Detail.
'    b. Sketch the profile for the detail view of Section View A-A.
'    c. Move the pointer while dragging drawing view. When the view
'       is where you want it to be, click to place the view.
'    d. Click OK to close the Detail View PropertyManager page.
' 4. Right-click the detail view in the drawing to open the
'    Area Hatch/Fill PropertyManager page.
'    a. Clear the Material crosshatch check box.
'    b. Select Solid.
'    c. Click OK.
'
' Postconditions:
' 1. Traverses the drawing views.
' 2. Gets data about the solid-fill hatches in the detail view.
' 3. Open c:\temp\SolidFillData.txt in a text editor and examine the
'    contents of the file.
'
' NOTE: Because the drawing is used elsewhere, do not save changes.
'-----------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swDrawing As SldWorks.DrawingDoc
Dim swSheet As SldWorks.Sheet
Dim swView As SldWorks.View
Dim nbrSolidFillHatches As Long
Dim ArraySize As Long
Dim i As Long
Dim boundaryData As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDrawing = swModel
```

```
    ' Open output file for solid-fill data
    Open "c:\temp\SolidFillData.txt" For Output As #1
```

```
    ' Get drawing sheet
    Set swSheet = swDrawing.GetCurrentSheet
```

```
    ' Get name of drawing sheet
    Write #1, "  Number of drawing views on drawing sheet: " & swDrawing.GetViewCount
```

```
    ' First view is the current drawing sheet
    Set swView = swDrawing.GetFirstView
    Write #1, "    First drawing view is the current drawing sheet, so..."
```

```
    ' Get first drawing view on drawing sheet
    Set swView = swView.GetNextView
    nbrSolidFillHatches = 0
    ArraySize = 0
```

```
    While Not swView Is Nothing
        Write #1, "        Get next drawing view on drawing sheet..."
        Write #1, "            View name: " & swView.Name
        nbrSolidFillHatches = swView.GetSolidHatchCount(ArraySize)
        Write #1, "            Number of solid-fill hatches in this view: " & nbrSolidFillHatches
        Write #1, "            Size of array for the boundary data for the solid-fill hatches: " & ArraySize
        If ArraySize > 0 Then
            boundaryData = swView.GetSolidHatchInfo
            Write #1, "                          Is the loop an outer loop (first)? " & boundaryData(0)
            Write #1, "                          Number of polylines in loop: " & boundaryData(1)
            Write #1, "                          Type ( 0 = polyline; 1 = arc or circle): " & boundaryData(2)
            Write #1, "                          Size of geometric data array (will be 0 if Type = 0): " & boundaryData(3)
            Write #1, "                              See IView::GetSolidHatchInfo's API Help topic for descriptions of these array elements: "
            For i = 4 To ArraySize - 1
                Write #1, "                                            Boundary data, array element " & i & ": " & boundaryData(i)
            Next i
        End If
        ' Get next drawing view
        Set swView = swView.GetNextView
    Wend
```

```
    ' Close c:\temp\SolidFillData.txt
    Close #1
```

```
End Sub
```
