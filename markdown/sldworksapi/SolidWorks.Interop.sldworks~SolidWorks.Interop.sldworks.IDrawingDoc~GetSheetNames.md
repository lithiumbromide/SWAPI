---
title: "GetSheetNames Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetSheetNames"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html"
---

# GetSheetNames Method (IDrawingDoc)

Gets a list of the names of the drawing sheets in this drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSheetNames() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetSheetNames()
```

### C#

```csharp
System.object GetSheetNames()
```

### C++/CLI

```cpp
System.Object^ GetSheetNames();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the names of the drawing sheets in this drawing

## VBA Syntax

See [DrawingDoc::GetSheetNames](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetSheetNames.html).

## Examples

[Get Sheet Names (VBA)](Get_Sheet_Numbers_and_Names_Example_VB.htm)
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)
[Get Loaded Sheets (C#)](Get_Loaded_Sheets_Example_CSharp.htm)
[Get Loaded Sheets (VB.NET)](Get_Loaded_Sheets_Example_VBNET.htm)
[Modify and Reload Sheet Format Template (C#)](Modify_and_Reload_Sheet_Format_Template_Example_CSharp.htm)
[Modify and Reload Sheet Format Template (VB.NET)](Modify_and_Reload_Sheet_Format_Template_Example_VBNET.htm)
[Modify and Reload Sheet Format Template (VBA)](Modify_and_Reload_Sheet_Format_Template_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::EditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EditSheet.html)
[IDrawingDoc::GetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html)
[IDrawingDoc::GetEditSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetEditSheet.html)
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html)
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)
[IDrawingDoc::IGetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetSheetNames.html)
[IDrawingDoc::IReorderSheets Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IReorderSheets.html)
[IDrawingDoc::NewSheet3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet3.html)
[IDrawingDoc::SetupSheet4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet4.html)
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
[ISheet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html)
