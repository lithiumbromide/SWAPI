---
title: "GetCustomColors Method (IColorTable)"
project: "SOLIDWORKS API Help"
interface: "IColorTable"
member: "GetCustomColors"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColors.html"
---

# GetCustomColors Method (IColorTable)

Gets the number of custom colors in the color table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomColors() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IColorTable
Dim value As System.Object

value = instance.GetCustomColors()
```

### C#

```csharp
System.object GetCustomColors()
```

### C++/CLI

```cpp
System.Object^ GetCustomColors();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array containing the custom colors

## VBA Syntax

See [ColorTable::GetCustomColors](ms-its:sldworksapivb6.chm::/sldworks~ColorTable~GetCustomColors.html).

## See Also

[IColorTable Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable.html)
[IColorTable Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable_members.html)
[IColorTable::GetCustomColorCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCustomColorCount.html)
[IColorTable::IGetCustomColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~IGetCustomColors.html)
[IColorTable::SetCustomColor Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~SetCustomColor.html)
[IColorTable::GetBasicColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetBasicColors.html)
[IColorTable::GetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IColorTable~GetCount.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
