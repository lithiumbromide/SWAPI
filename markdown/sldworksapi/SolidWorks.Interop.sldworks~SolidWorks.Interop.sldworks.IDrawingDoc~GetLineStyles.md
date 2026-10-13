---
title: "GetLineStyles Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineStyles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.html"
---

# GetLineStyles Method (IDrawingDoc)

Gets all of the line styles used in the current document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineStyles( _
   ByRef StyleNameList As System.Object, _
   ByRef StyleList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim StyleNameList As System.Object
Dim StyleList As System.Object
Dim value As System.Boolean

value = instance.GetLineStyles(StyleNameList, StyleList)
```

### C#

```csharp
System.bool GetLineStyles(
   out System.object StyleNameList,
   out System.object StyleList
)
```

### C++/CLI

```cpp
System.bool GetLineStyles(
   [Out] System.Object^ StyleNameList,
   [Out] System.Object^ StyleList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleNameList`: Array of strings containing style names
- `StyleList`: Array of strings containing style types

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::GetLineStyles](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineStyles.html).

## Examples

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.html)
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.html)
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.html)
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.html)
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
