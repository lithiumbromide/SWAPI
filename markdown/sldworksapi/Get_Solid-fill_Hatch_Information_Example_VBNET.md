---
title: "Get Solid-fill Hatch Information Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Solid-fill_Hatch_Information_Example_VBNET.htm"
---

# Get Solid-fill Hatch Information Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDrawing As DrawingDoc
        Dim swSheet As Sheet
        Dim swView As View
        Dim nbrSolidFillHatches As Integer
        Dim ArraySize As Integer
        Dim i As Integer
        Dim boundaryData As Object
        Dim file As System.IO.StreamWriter

        swModel = swApp.ActiveDoc
        swDrawing = swModel

        ' Open output file for solid-fill data
        file = My.Computer.FileSystem.OpenTextFileWriter("c:\temp\SolidFillData.txt", False)

        ' Get drawing sheet
        swSheet = swDrawing.GetCurrentSheet

        ' Get name of drawing sheet
        file.WriteLine("  Number of drawing views on drawing sheet: " & swDrawing.GetViewCount)

        ' First view is the current drawing sheet
        swView = swDrawing.GetFirstView
        file.WriteLine("    First drawing view is the current drawing sheet, so...")

        ' Get first drawing view on drawing sheet
        swView = swView.GetNextView
        nbrSolidFillHatches = 0
        ArraySize = 0
        While Not swView Is Nothing
            file.WriteLine("        Get next drawing view on drawing sheet...")
            file.WriteLine("            View name: " & swView.Name)
            nbrSolidFillHatches = swView.GetSolidHatchCount(ArraySize)
            file.WriteLine("            Number of solid-fill hatches in this view: " & nbrSolidFillHatches)
            file.WriteLine("            Size of array for the boundary data for the solid-fill hatch(es): " & ArraySize)
            If ArraySize > 0 Then
                boundaryData = swView.GetSolidHatchInfo
                file.WriteLine("                          Is the loop an outer loop (first)? " & boundaryData(0))
                file.WriteLine("                          Number of polylines in loop: " & boundaryData(1))
                file.WriteLine("                          Type ( 0 = polyline; 1 = arc or circle): " & boundaryData(2))
                file.WriteLine("                          Size of geometric data array (will be 0 if Type = 0): " & boundaryData(3))
                file.WriteLine("                              See IView::GetSolidHatchInfo's API Help topic for descriptions of these array elements: ")
                For i = 4 To ArraySize - 1
                    file.WriteLine("                                            Boundary data, array element " & i & ": " & boundaryData(i))
                Next i
            End If
            ' Get next drawing view
            swView = swView.GetNextView
        End While

        file.Close()

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
