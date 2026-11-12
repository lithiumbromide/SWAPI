---
title: "IGetCurrentSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "IGetCurrentSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html"
---

# IGetCurrentSheet Method (IDrawingDoc)

Gets the currently active drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCurrentSheet() As Sheet
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As Sheet

value = instance.IGetCurrentSheet()
```

### C#

```csharp
Sheet IGetCurrentSheet()
```

### C++/CLI

```cpp
Sheet^ IGetCurrentSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ISheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) object

## VBA Syntax

See [DrawingDoc::IGetCurrentSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~IGetCurrentSheet.html).

## Examples

[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)

## Remarks

The returned [ISheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) object includes methods that you can use to access the [IBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html) object.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html)
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html)
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.html)
[IDrawingDoc::IReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets.html)
[IDrawingDoc::ReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ReorderSheets.html)
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.html)
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
