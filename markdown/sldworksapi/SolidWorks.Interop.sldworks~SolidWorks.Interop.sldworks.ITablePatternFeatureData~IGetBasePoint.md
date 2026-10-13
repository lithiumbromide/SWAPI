---
title: "IGetBasePoint Method (ITablePatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ITablePatternFeatureData"
member: "IGetBasePoint"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetBasePoint.html"
---

# IGetBasePoint Method (ITablePatternFeatureData)

Gets the base point for this table-driven pattern feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetBasePoint() As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ITablePatternFeatureData
Dim value As System.Double

value = instance.IGetBasePoint()
```

### C#

```csharp
System.double IGetBasePoint()
```

### C++/CLI

```cpp
System.double IGetBasePoint();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of doubles that describe the table-driven pattern ( 3x number of points)

## See Also

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.html)
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.html)
[ITablePatternFeatureData::GetBasePoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetBasePoint.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
