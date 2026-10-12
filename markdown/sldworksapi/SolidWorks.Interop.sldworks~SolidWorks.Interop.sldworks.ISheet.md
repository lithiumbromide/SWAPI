---
title: "ISheet Interface"
project: "SOLIDWORKS API Help"
interface: "ISheet"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet.html"
---

# ISheet Interface

Allows access to a sheet and objects on the sheet such as [BOM tables](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomTable.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISheet
```

### Visual Basic (Usage)

```vb
Dim instance As ISheet
```

### C#

```csharp
public interface ISheet
```

### C++/CLI

```cpp
public interface class ISheet
```

## VBA Syntax

See [Sheet](ms-its:sldworksapivb6.chm::/sldworks~Sheet.html).

## Examples

[Get Sheet Properties and Insert Object (C++)](Get_Sheet_Properties_and_Insert_Object_Example_CPlusPlus_COM.htm)
[Copy and Paste Drawing Sheet (C#)](Copy_and_Paste_Drawing_Sheet_Example_CSharp.htm)
[Copy and Paste Drawing Sheet (VB.NET)](Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm)
[Copy and Paste Drawing Sheet (VBA)](Copy_and_Paste_Drawing_Sheet_Example_VB.htm)
[Get and Set Sheet Properties (VBA)](Get_and_Set_Sheet_Properties_Example_VB.htm)
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)

## Remarks

A drawing document can consist of one or more sheets. Each sheet typically contains one or more [drawing views](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView.html). Each drawing view is an oriented snapshot of a particular SOLIDWORKS model and a particular [configuration](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) of the model.

## Accessors

[IDrawingDoc::GetCurrentSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetCurrentSheet.html) and [IDrawingDoc::IGetCurrentSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~IGetCurrentSheet.html)

[IDrawingDoc::Sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~Sheet.html)

[IFamilyTableAnnotation::GetSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableAnnotation~GetSheet.html)

[IRevisionTableAnnotation::GetSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevisionTableAnnotation~GetSheet.html)

[IView::Sheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IView~Sheet.html)

## Access Diagram

[Sheet](SWObjectModel.pdf#Sheet)

## See Also

[ISheet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheet_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
