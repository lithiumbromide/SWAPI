---
title: "GetCount Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.html"
---

# GetCount Method (IColorTable)

Gets the total number of colors in the color table, including standard and custom colors.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim value As System.Integer

value = instance.GetCount()
```

### C#

```csharp
System.int GetCount()
```

### C++/CLI

```cpp
System.int GetCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of colors defined in the color table

## VBA Syntax

See [ColorTable::GetCount](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetCount.html).

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetBasicColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.html)
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html)
[IColorTable:GetStandardCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.html)
