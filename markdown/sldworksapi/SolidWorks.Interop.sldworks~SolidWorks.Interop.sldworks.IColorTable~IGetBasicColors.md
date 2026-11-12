---
title: "IGetBasicColors Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "IGetBasicColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetBasicColors.html"
---

# IGetBasicColors Method (IColorTable)

Gets the basic colors in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBasicColors( _
   ByVal ColorCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim ColorCount As System.Integer
Dim value As System.Integer

value = instance.IGetBasicColors(ColorCount)
```

### C#

```csharp
System.int IGetBasicColors(
   System.int ColorCount
)
```

### C++/CLI

```cpp
System.int IGetBasicColors(
   System.int ColorCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColorCount`: Number of basic colors

### Return Value

- in-process, unmanaged C++: Pointer to an array of basic colors of size ColorCount

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IColorTable::GetBasicColorCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable~GetBasicColorCount.html) to determine the size of the array.

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColors.html)
[IColorTable::IGetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
