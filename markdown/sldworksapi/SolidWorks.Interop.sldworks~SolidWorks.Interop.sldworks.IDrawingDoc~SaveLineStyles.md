---
title: "SaveLineStyles Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SaveLineStyles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.html"
---

# SaveLineStyles Method (IDrawingDoc)

Exports to a file the specified line styles in the current drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveLineStyles( _
   ByVal StyleFiles As System.String, _
   ByVal StyleNameList As System.Object, _
   ByVal ReplaceExisting As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim StyleFiles As System.String
Dim StyleNameList As System.Object
Dim ReplaceExisting As System.Boolean
Dim value As System.Boolean

value = instance.SaveLineStyles(StyleFiles, StyleNameList, ReplaceExisting)
```

### C#

```csharp
System.bool SaveLineStyles(
   System.string StyleFiles,
   System.object StyleNameList,
   System.bool ReplaceExisting
)
```

### C++/CLI

```cpp
System.bool SaveLineStyles(
   System.String^ StyleFiles,
   System.Object^ StyleNameList,
   System.bool ReplaceExisting
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleFiles`: Full pathname of file to save line styles to
- `StyleNameList`: Array of strings containing line style names to save
- `ReplaceExisting`: True to replace existing styles in the file, false to not

### Return Value

True if successful, false if not

## VBA Syntax

See [DrawingDoc::SaveLineStyles](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SaveLineStyles.html).

## Examples

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.html)
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.html)
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.html)
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.html)
[ISldWorks::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
