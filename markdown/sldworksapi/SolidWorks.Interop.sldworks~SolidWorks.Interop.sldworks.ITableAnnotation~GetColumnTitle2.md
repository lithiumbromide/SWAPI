---
title: "GetColumnTitle2 Method (ITableAnnotation)"
project: "SOLIDWORKS API Help"
interface: "ITableAnnotation"
member: "GetColumnTitle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~GetColumnTitle2.html"
---

# GetColumnTitle2 Method (ITableAnnotation)

Gets the title of the specified column.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColumnTitle2( _
   ByVal Index As System.Integer, _
   ByVal IncludeHidden As System.Boolean _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ITableAnnotation
Dim Index As System.Integer
Dim IncludeHidden As System.Boolean
Dim value As System.String

value = instance.GetColumnTitle2(Index, IncludeHidden)
```

### C#

```csharp
System.string GetColumnTitle2(
   System.int Index,
   System.bool IncludeHidden
)
```

### C++/CLI

```cpp
System.String^ GetColumnTitle2(
   System.int Index,
   System.bool IncludeHidden
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: 0-based index indicating the column
- `IncludeHidden`: True to get the title of the hidden column, false to not

### Return Value

Column title

## VBA Syntax

See [TableAnnotation::GetColumnTitle2](ms-its:sldworksapivb6.chm::/sldworks~TableAnnotation~GetColumnTitle2.html).

## Examples

[Export BOMs to XML (VBA)](Export_BOMs_to_XML_Example_VB.htm)
[Export BOMs to XML (VB.NET)](Export_BOMs_to_XML_Example_VBNET.htm)
[Export BOMs to XML (C#)](Export_BOMs_to_XML_Example_CSharp.htm)

## See Also

[ITableAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation.html)
[ITableAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation_members.html)
[ITableAnnotation::SetColumnTitle2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITableAnnotation~SetColumnTitle2.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
