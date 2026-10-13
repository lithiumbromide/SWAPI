---
title: "AddLineStyle Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AddLineStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.html"
---

# AddLineStyle Method (IDrawingDoc)

Adds a line style to the current drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLineStyle( _
   ByVal StyleName As System.String, _
   ByVal StyleDefinition As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim StyleName As System.String
Dim StyleDefinition As System.String
Dim value As System.Boolean

value = instance.AddLineStyle(StyleName, StyleDefinition)
```

### C#

```csharp
System.bool AddLineStyle(
   System.string StyleName,
   System.string StyleDefinition
)
```

### C++/CLI

```cpp
System.bool AddLineStyle(
   System.String^ StyleName,
   System.String^ StyleDefinition
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of line style
- `StyleDefinition`: Comma-delimited string of line lengths and spacing values for the line style

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::AddLineStyle](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AddLineStyle.html).

## Examples

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## Remarks

Read about line style options in SOLIDWORKS Help.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.html)
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.html)
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.html)
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.html)
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
