---
title: "GetCustomColorCount Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetCustomColorCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html"
---

# GetCustomColorCount Method (IColorTable)

Gets the number of custom colors in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomColorCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim value As System.Integer

value = instance.GetCustomColorCount()
```

### C#

```csharp
System.int GetCustomColorCount()
```

### C++/CLI

```cpp
System.int GetCustomColorCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of custom colors

## VBA Syntax

See [ColorTable::GetCustomColorCount](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetCustomColorCount.html).

## Remarks

Call this method before calling [IColorTable::IGetCustomColors](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable~IGetCustomColors.html) to determine the size of the array for that method.

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetBasicColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.html)
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.html)
[IColorTable::GetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.html)
[IColorTable:GetStandardCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
