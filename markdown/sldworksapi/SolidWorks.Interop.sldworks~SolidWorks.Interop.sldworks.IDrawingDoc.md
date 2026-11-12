---
title: "IDrawingDoc Interface"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html"
---

# IDrawingDoc Interface

Allows access to functions that perform drawing operations.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IDrawingDoc
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
```

### C#

```csharp
public interface IDrawingDoc
```

### C++/CLI

```cpp
public interface class IDrawingDoc
```

## VBA Syntax

See [DrawingDoc](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc.html).

## Examples

[Copy and Paste Drawing Sheet (C#)](Copy_and_Paste_Drawing_Sheet_Example_CSharp.htm)
[Copy and Paste Drawing Sheet (VB.NET)](Copy_and_Paste_Drawing_Sheet_Example_VBNET.htm)
[Copy and Paste Drawing Sheet (VBA)](Copy_and_Paste_Drawing_Sheet_Example_VB.htm)
[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)
[Activate Each View on Current Sheet (VBA)](Activate_Each_View_on_Current_Sheet_Example_VB.htm)
[Insert Spline in Drawing (C++)](Insert_Spline_in_Drawing_Example_CPlusPlus_COM.htm)
[Get Notes from New or Existing Title Block (C#)](Get_Notes_from_New_or_Existing_Title_Block_Example_CSharp.htm)
[Get Notes from New or Existing Title Block (VB.NET)](Get_Notes_from_New_or_Existing_Title_Block_Example_VBNET.htm)
[Get Notes from New or Existing Title Block (VBA)](Get_Notes_from_New_or_Existing_Title_Block_Example_VB.htm)
[Insert Revision Cloud into a Drawing (VBA)](Insert_Revision_Cloud_into_Drawing_Example_VB.htm)

## Remarks

Creating, aligning, and accessing drawing views are a few of the functions you find on the IDrawingDoc object.

The SOLIDWORKS API also includes functions that are common to all document types. For example, determining the file name associated with a document is a common operation. The SOLIDWORKS API uses the [IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) object to expose common document-level functions.

Events are implemented with delegates in the Microsoft .NET Framework. See the [Overview](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks_namespace.html) topic for a list of delegates for this interface.

## Access Diagram

[DrawingDoc](SWObjectModel.pdf#DrawingDoc)

## See Also

[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
