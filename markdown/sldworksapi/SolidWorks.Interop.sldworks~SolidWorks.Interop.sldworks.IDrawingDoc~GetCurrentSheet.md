---
title: "GetCurrentSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetCurrentSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html"
---

# GetCurrentSheet Method (IDrawingDoc)

Gets the currently active drawing sheet.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentSheet() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim value As System.Object

value = instance.GetCurrentSheet()
```

### C#

```csharp
System.object GetCurrentSheet()
```

### C++/CLI

```cpp
System.Object^ GetCurrentSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Sheet

## VBA Syntax

See [DrawingDoc::GetCurrentSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetCurrentSheet.html).

## Examples

[Copy and Paste Drawing Sheet (C#)](Copy_and_Paste_Drawing_Sheet_Example_CSharp.htm)
[Copy and Paste Drawing Sheet (VB.NET)](Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm)
[Copy and Paste Drawing Sheet (VBA)](Copy_and_Paste_Drawing_Sheet_Example_VB.htm)
[Delete OLE Objects from Drawing Sheet and Template (VBA)](Delete_OLE_Objects_from_Drawing_Sheet_and_Template_Example_VB.htm)
[Get and Set Sheet Properties (VBA)](Get_and_Set_Sheet_Properties_Example_VB.htm)
[Get Drawing View Names and Types (VBA)](Get_Drawing_View_Names_and_Types_Example_VB.htm)
[Get Name and Properties of Drawing Sheet Template (VBA)](Get_Name_and_Properties_of_Drawing_Sheet_Template_Example_VB.htm)
[Get Revision Table (VBA)](Get_Revision_Table_Example_VB.htm)
[Get Sheet Numbers and Names (VBA)](Get_Sheet_Numbers_and_Names_Example_VB.htm)
[Rebuild All Configurations (VBA)](Rebuild_All_Configurations_Example_VB.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

## Remarks

The returned [ISheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISheet.html) object includes methods that you can use to access the [IBomTable](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html) object.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::ActivateSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~ActivateSheet.html)
[IDrawingDoc::GetSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetCount.html)
[IDrawingDoc::GetSheetNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetSheetNames.html)
[IDrawingDoc::SheetNext Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetNext.html)
[IDrawingDoc::SheetPrevious Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SheetPrevious.html)
[IDrawingDoc::IGetCurrentSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)
