---
title: "GetBasicColorCount Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetBasicColorCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColorCount.html"
---

# GetBasicColorCount Method (IColorTable)

Gets the number of basic colors defined in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBasicColorCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim value As System.Integer

value = instance.GetBasicColorCount()
```

### C#

```csharp
System.int GetBasicColorCount()
```

### C++/CLI

```cpp
System.int GetBasicColorCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of basic colors

## VBA Syntax

See [ColorTable::GetBasicColorCount](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetBasicColorCount.html).

## Remarks

Call this method before calling [IColorTable::IGetBasicColors](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable~IGetBasicColors.html) to determine the size of the array for that method.

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::IGetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetBasicColors.html)
[IColorTable::GetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColors.html)
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.html)
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html)
[IColorTable:GetStandardCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetStandardCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
