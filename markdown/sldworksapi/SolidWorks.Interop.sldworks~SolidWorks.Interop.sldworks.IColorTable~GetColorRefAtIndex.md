---
title: "GetColorRefAtIndex Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetColorRefAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetColorRefAtIndex.html"
---

# GetColorRefAtIndex Method (IColorTable)

Gets the COLORREF at the specified index position of the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetColorRefAtIndex( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim Index As System.Integer
Dim value As System.Integer

value = instance.GetColorRefAtIndex(Index)
```

### C#

```csharp
System.int GetColorRefAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.int GetColorRefAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position of the desired color

### Return Value

COLORREF at the specified index position

## VBA Syntax

See [ColorTable::GetColorRefAtIndex](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetColorRefAtIndex.html).

## Examples

[Get COLORREF Values of Standard User-interface Elements (C#)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm)
[Get COLORREF Values of Standard User-interface Elements (VB.NET)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm)
[Get COLORREF Values of Standard User-interface Elements (VBA)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm)

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::SetColorRefAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetColorRefAtIndex.html)
