---
title: "GetGridSettings Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetGridSettings"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetGridSettings.html"
---

# GetGridSettings Method (IModelDoc2)

Gets the current grid settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGridSettings() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Object

value = instance.GetGridSettings()
```

### C#

```csharp
System.object GetGridSettings()
```

### C++/CLI

```cpp
System.Object^ GetGridSettings();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current grid settings (see **Remarks**)

## VBA Syntax

See [ModelDoc2::GetGridSettings](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetGridSettings.html).

## Remarks

The return format is the following array of doubles:

[ dispGrid, gridSpacing, snap, dotStyle, nMajor, nMinor, angleSnap, angleUnit, minorAuto ]

where:

- dispGrid - can be interpreted as a BOOLEAN: True if grid displayed, false otherwise
- gridSpacing - snap distance
- snap - can be interpreted as a BOOLEAN: True if snap to grid is on, false otherwise
- dotStyle - can be interpreted as a BOOLEAN: True if dotted grids, false otherwise
- nMajor - number of minors in major
- nMinor - number of snaps in minor
- angleSnap - can be interpreted as a BOOLEAN: True if snap to angle is on, false otherwise
- angleUnit - value of angle to which to snap
- minorAuto - an be interpreted as a BOOLEAN: True if the minor grids are set automatically, false otherwise

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::GridOptions Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GridOptions.html)
[IModelDoc2::ToolsGrid Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ToolsGrid.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
