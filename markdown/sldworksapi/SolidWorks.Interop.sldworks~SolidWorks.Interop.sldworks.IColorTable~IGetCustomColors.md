---
title: "IGetCustomColors Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "IGetCustomColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.html"
---

# IGetCustomColors Method (IColorTable)

Gets the number of custom colors in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCustomColors( _
   ByVal ColorCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim ColorCount As System.Integer
Dim value As System.Integer

value = instance.IGetCustomColors(ColorCount)
```

### C#

```csharp
System.int IGetCustomColors(
   System.int ColorCount
)
```

### C++/CLI

```cpp
System.int IGetCustomColors(
   System.int ColorCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColorCount`: Number of custom colors

### Return Value

- in-process, unmanaged C++: Pointer to an array of custom colors of size ColorCount

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Before calling this method, call [IColorTable::GetCustomColorCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IColorTable~GetCustomColorCount.html) to determine the size of the array.

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.html)
[IColorTable::SetCustomColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetCustomColor.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
