---
title: "GetLineStyles Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetLineStyles"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetLineStyles.html"
---

# GetLineStyles Method (ISldWorks)

Gets all of the line styles in the specified file.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineStyles( _
   ByVal StyleFile As System.String, _
   ByRef StyleNameList As System.Object, _
   ByRef StyleList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim StyleFile As System.String
Dim StyleNameList As System.Object
Dim StyleList As System.Object
Dim value As System.Boolean

value = instance.GetLineStyles(StyleFile, StyleNameList, StyleList)
```

### C#

```csharp
System.bool GetLineStyles(
   System.string StyleFile,
   out System.object StyleNameList,
   out System.object StyleList
)
```

### C++/CLI

```cpp
System.bool GetLineStyles(
   System.String^ StyleFile,
   [Out] System.Object^ StyleNameList,
   [Out] System.Object^ StyleList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleFile`: Full pathname of the file containing line styles to get
- `StyleNameList`: Array of strings containing line style names
- `StyleList`: Array of strings containing line style types

### Return Value

True if successful, false if not

## VBA Syntax

See [SldWorks::GetLineStyles](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetLineStyles.html).

## Examples

[Manage Drawing Document Line Styles (C#)](Manage_Drawing_Document_Line_Styles_Example_CSharp.htm)
[Manage Drawing Document Line Styles (VB.NET)](Manage_Drawing_Document_Line_Styles_Example_VBNET.htm)
[Manage Drawing Document Line Styles (VBA)](Manage_Drawing_Document_Line_Styles_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[IDrawingDoc::AddLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AddLineStyle.html)
[IDrawingDoc::DeleteLineStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~DeleteLineStyle.html)
[IDrawingDoc::GetLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineStyles.html)
[IDrawingDoc::LoadLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~LoadLineStyles.html)
[IDrawingDoc::SaveLineStyles Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SaveLineStyles.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
