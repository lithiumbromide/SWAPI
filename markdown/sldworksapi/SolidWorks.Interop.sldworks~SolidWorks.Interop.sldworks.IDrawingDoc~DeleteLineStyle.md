---
title: "DeleteLineStyle Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "DeleteLineStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.html"
---

# DeleteLineStyle Method (IDrawingDoc)

Deletes the specified line style from the current drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteLineStyle( _
   ByVal StyleName As System.String, _
   ByVal ReplaceName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim StyleName As System.String
Dim ReplaceName As System.String
Dim value As System.Boolean

value = instance.DeleteLineStyle(StyleName, ReplaceName)
```

### C#

```csharp
System.bool DeleteLineStyle(
   System.string StyleName,
   System.string ReplaceName
)
```

### C++/CLI

```cpp
System.bool DeleteLineStyle(
   System.String^ StyleName,
   System.String^ ReplaceName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of line style to delete
- `ReplaceName`: Name of line style to replace deleted StyleName

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::DeleteLineStyle](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~DeleteLineStyle.html).

## Examples

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## Remarks

The following line styles cannot be deleted:

- Solid
- Dashed
- Phantom
- Chain
- Center
- Stitch
- Thin/Thick Chain

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.html)
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.html)
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.html)
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.html)
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
