---
title: "GetStandardCount Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetStandardCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.html"
---

# GetStandardCount Method (IColorTable)

Gets the number of basic or standard colors defined in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStandardCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim value As System.Integer

value = instance.GetStandardCount()
```

### C#

```csharp
System.int GetStandardCount()
```

### C++/CLI

```cpp
System.int GetStandardCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of basic or standard colors defined in the color table

## VBA Syntax

See [ColorTable::GetStandardCount](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetStandardCount.html).

## Examples

[Get COLORREF Values of Standard User-interface Elements (C#)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_CSharp.htm)
[Get COLORREF Values of Standard User-interface Elements (VB.NET)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VBNET.htm)
[Get COLORREF Values of Standard User-interface Elements (VBA)](Get_COLORREF_Values_of_Standard_User-interface_Elements_Example_VB.htm)

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetBasicColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.html)
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html)
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.html)
