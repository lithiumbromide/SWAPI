---
title: "GetEditSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetEditSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html"
---

# GetEditSheet Method (IDrawingDoc)

Gets whether the current drawing is in edit sheet mode or edit template mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEditSheet() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Boolean

value = instance.GetEditSheet()
```

### C#

```csharp
System.bool GetEditSheet()
```

### C++/CLI

```cpp
System.bool GetEditSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True for edit sheet mode, false for edit template mode

## VBA Syntax

See [DrawingDoc::GetEditSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetEditSheet.html).

## Remarks

Use:

- [IDrawingDoc::EditSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditSheet.html) to set the drawing to be editing the sheet.
- [IDrawingDoc::EditTemplate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EditTemplate.html) to set the drawing to be editing the template.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::EditSketch Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSketch.html)

## Availability

SOLIDWORKS 99, datecode 1999207
