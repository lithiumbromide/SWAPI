---
title: "GetSheetCount Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetSheetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html"
---

# GetSheetCount Method (IDrawingDoc)

Gets the number of drawing sheets in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Integer

value = instance.GetSheetCount()
```

### C#

```csharp
System.int GetSheetCount()
```

### C++/CLI

```cpp
System.int GetSheetCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of drawing sheets in the drawing

## VBA Syntax

See [DrawingDoc::GetSheetCount](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetSheetCount.html).

## Examples

[Print Drawing Document to File (VBA)](Print_Drawing_Document_to_File_Example_VB.htm)

## Remarks

Call this method before call [IDrawingDoc::IGetSheetNames](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IGetSheetNames.html) to determine the size of that method's return array.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html)
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.html)
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html)
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)
[IDrawingDoc::IReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets.html)
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.html)
[IDrawingDoc::ReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.html)
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.html)
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
