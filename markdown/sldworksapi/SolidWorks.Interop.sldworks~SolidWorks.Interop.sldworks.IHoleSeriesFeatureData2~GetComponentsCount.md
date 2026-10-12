---
title: "GetComponentsCount Method (IHoleSeriesFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData2"
member: "GetComponentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetComponentsCount.html"
---

# GetComponentsCount Method (IHoleSeriesFeatureData2)

Gets the number of components in this hole series.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData2
Dim value As System.Integer

value = instance.GetComponentsCount()
```

### C#

```csharp
System.int GetComponentsCount()
```

### C++/CLI

```cpp
System.int GetComponentsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of components in this hole series

## VBA Syntax

See [HoleSeriesFeatureData2::GetComponentsCount](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData2~GetComponentsCount.html).

## Examples

See the examples in [IHoleSeriesFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2.html).

## Remarks

Call this method before calling [IHoleSeriesFeatureData2::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~IGetComponents.html) to get the size of the array for that method.

## See Also

[IHoleSeriesFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2.html)
[IHoleSeriesFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2_members.html)
[IHoleSeriesFeatureData2::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData2~GetComponents.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
