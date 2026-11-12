---
title: "GetNameAtIndex Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetNameAtIndex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetNameAtIndex.html"
---

# GetNameAtIndex Method (IColorTable)

Gets the name of the color at the specified index position in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNameAtIndex( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim Index As System.Integer
Dim value As System.String

value = instance.GetNameAtIndex(Index)
```

### C#

```csharp
System.string GetNameAtIndex(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetNameAtIndex(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index position of the desired color

### Return Value

Name of the color at the specified index

## VBA Syntax

See [ColorTable::GetNameAtIndex](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetNameAtIndex.html).

## Examples

[Get COLORREF Values of Standard User-interface Elements (C#)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm)
[Get COLORREF Values of Standard User-interface Elements (VB.NET)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm)
[Get COLORREF Values of Standard User-interface Elements (VBA)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm)

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::SetColorRefAtIndex Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetColorRefAtIndex.html)
