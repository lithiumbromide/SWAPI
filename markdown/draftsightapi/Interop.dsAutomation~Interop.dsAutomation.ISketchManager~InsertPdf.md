---
title: "InsertPdf Method (ISketchManager)"
project: ""
interface: "ISketchManager"
member: "InsertPdf"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISketchManager~InsertPdf.html"
---

# InsertPdf Method (ISketchManager)

Inserts page images from a PDF.

## Syntax

### Visual Basic

```vb
Function InsertPdf( _
   ByVal PathName As System.String, _
   ByVal InsertXDblArray As System.Object, _
   ByVal InsertYDblArray As System.Object, _
   ByVal InsertZDblArray As System.Object, _
   ByVal ScaleDblArray As System.Object, _
   ByVal RotationDblArray As System.Object, _
   ByVal PagesCountLongArray As System.Object _
) As System.Object
```

### C#

```csharp
System.object InsertPdf(
   System.string PathName,
   System.object InsertXDblArray,
   System.object InsertYDblArray,
   System.object InsertZDblArray,
   System.object ScaleDblArray,
   System.object RotationDblArray,
   System.object PagesCountLongArray
)
```

### JScript

```
function InsertPdf(
   PathName : System.String,
   InsertXDblArray : System.Object,
   InsertYDblArray : System.Object,
   InsertZDblArray : System.Object,
   ScaleDblArray : System.Object,
   RotationDblArray : System.Object,
   PagesCountLongArray : System.Object
) : System.Object;
```

### Managed Extensions for C++

```
System.Object* InsertPdf(
   System.string* PathName,
   System.Object* InsertXDblArray,
   System.Object* InsertYDblArray,
   System.Object* InsertZDblArray,
   System.Object* ScaleDblArray,
   System.Object* RotationDblArray,
   System.Object* PagesCountLongArray
)
```

### C++/CLI

```cpp
System.Object^ InsertPdf(
   System.String^ PathName,
   System.Object^ InsertXDblArray,
   System.Object^ InsertYDblArray,
   System.Object^ InsertZDblArray,
   System.Object^ ScaleDblArray,
   System.Object^ RotationDblArray,
   System.Object^ PagesCountLongArray
)
```

### Parameters

- `PathName`: Path and file name of the PDF
- `InsertXDblArray`: Array of x coordinates of pages
- `InsertYDblArray`: Array of y coordinates of pages
- `InsertZDblArray`: Array of z coordinates of pages
- `ScaleDblArray`: Array of scale factors of pages
- `RotationDblArray`: Array of rotation angles of pages
- `PagesCountLongArray`: Array of page numbers

### Return Value

Array of [IPdfReference](Interop.dsAutomation~Interop.dsAutomation.IPdfReference.html)s

## Examples

'VBA

'This example shows how to insert a PDF into a sketch.

'--------------------------------------------------------------
' Preconditions:
' 1. Create a VBA macro in a software product in which VBA is
' embedded.
' 2. Copy and paste this example into the Visual Basic IDE.
' 3. Add a reference to the DraftSight type library,
' `install_dir`**\bin\dsAutomation.dll**.
' 4. Change the path and file name of a PDF to insert.
' 5. Start DraftSight and open a drawing.
' 6. Run the macro.
'
' Postconditions: See the DraftSight Command Window for output
' messages and all of your drawing's immediate child references.
'--------------------------------------------------------------
Option Explicit

Sub main()

Dim dsApp As DraftSight.Application
Dim dsDoc As DraftSight.Document
Dim dsModel As DraftSight.Model
Dim dsSketchManager As DraftSight.SketchManager
Dim dsReference As DraftSight.ReferenceImage
Dim dsPdfReference As DraftSight.PdfReference
Dim dsDgnReference As DraftSight.DgnReference
Dim dsImageDefinition As DraftSight.ImageDefinition
Dim dsPdfDefinition As DraftSight.PdfDefinition
Dim dsDgnDefinition As DraftSight.DgnDefinition
Dim extDefTypeArray As Variant
Dim extDefArray As Variant
Dim commandline As DraftSight.CommandMessage

Dim imageFileName As String

'Connect to DraftSight
Set dsApp = GetObject(, "DraftSight.Application")

'Abort any command currently running in DraftSight
'to avoid nested commands
dsApp.AbortRunningCommand

Set commandline = dsApp.GetCommandMessage()

'Get active document
Set dsDoc = dsApp.GetActiveDocument()
If Not dsDoc Is Nothing Then

'Get model space
Set dsModel = dsDoc.GetModel()

'Get Sketch Manager
Set dsSketchManager = dsModel.GetSketchManager()

'Specify PDF (*.pdf) to insert into the sketch
imageFileName = "c:\Users\J4M\Desktop\INT-SWCheckinPolicyGuide-260718-1510-2.pdf"

'Insert PDF reference

Dim xcoords(4) As Double
xcoords(0) = 0#
xcoords(1) = 1#
xcoords(2) = 2#
xcoords(3) = 3#
xcoords(4) = 4#
Dim ycoords(4) As Double
ycoords(0) = 0#
ycoords(1) = 1#
ycoords(2) = 2#
ycoords(3) = 3#
ycoords(4) = 4#
Dim zcoords(4) As Double
zcoords(0) = 0#
zcoords(1) = 0#
zcoords(2) = 0#
zcoords(3) = 0#
zcoords(4) = 0#
Dim pagesArray(4) As Long
pagesArray(0) = 1
pagesArray(1) = 2
pagesArray(2) = 3
pagesArray(3) = 4
pagesArray(4) = 5
Dim scaleFactor(4) As Double
scaleFactor(0) = 1#
scaleFactor(1) = 1#
scaleFactor(2) = 1#
scaleFactor(3) = 1#
scaleFactor(4) = 1#
Dim Rotation(4) As Double
Rotation(0) = 0#
Rotation(1) = 0#
Rotation(2) = 0#
Rotation(3) = 0#
Rotation(4) = 0#

Dim refArray As Variant
refArray = dsSketchManager.**InsertPdf**(imageFileName, xcoords, ycoords, zcoords, scaleFactor, Rotation, pagesArray)

If IsEmpty(refArray) Then
commandline.PrintLine imageFileName & " PDF not inserted."
Else
commandline.PrintLine "A PDF was inserted in the drawing."
End If
Else
commandline.PrintLine "There are no open documents in DraftSight."
End If

'Get definition of the inserted PDF
Set dsPdfDefinition = refArray(0).**GetDefinition**()
commandline.PrintLine "PDF is loaded? " & dsPdfDefinition.**IsLoaded**

'Get all immediate child references of the active document
'In addition to the just inserted PDF, your drawing may
'contain other immediate child references of various image types
dsDoc.**GetImmediateChildReferences** extDefTypeArray, extDefArray

Dim objecttype As dsObjectType_e
Dim objectdefinition As Object
Dim i As Long

For i = 0 To UBound(extDefTypeArray)

objecttype = extDefTypeArray(i)
Set objectdefinition = extDefArray(i)

If (objecttype = dsObjectType_e.dsImageDefinitionType) Then
Set dsImageDefinition = objectdefinition
commandline.PrintLine "Raster image page " & (i + 1) & " Path: " & dsImageDefinition.**GetPath**()
commandline.PrintLine "Found In Path: " & dsImageDefinition.**GetFoundInPath**()
ElseIf (objecttype = dsObjectType_e.dsPdfDefinitionType) Then
Set dsPdfDefinition = objectdefinition
commandline.PrintLine "PDF page " & (i + 1) & " Path: " & dsPdfDefinition.**GetPath**()
commandline.PrintLine "Found In Path: " & dsPdfDefinition.**GetFoundInPath**()
ElseIf (objecttype = dsObjectType_e.dsDgnDefinitionType) Then
Set dsDgnDefinition = objectdefinition
commandline.PrintLine "DGN page " & (i + 1) & " Path: " & dsDgnDefinition.**GetPath**()
commandline.PrintLine "Found In Path: " & dsDgnDefinition.**GetFoundInPath**()
End If
Next

End Sub

## Remarks

All of the parameter arrays are the save size and map one to one.

## See Also

[ISketchManager Interface](Interop.dsAutomation~Interop.dsAutomation.ISketchManager.html)
[ISketchManager Members](Interop.dsAutomation~Interop.dsAutomation.ISketchManager_members.html)

## Availability

DraftSight 2020 SP0
