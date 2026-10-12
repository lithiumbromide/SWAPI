---
title: "GetComponentsCount Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "GetComponentsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponentsCount.html"
---

# GetComponentsCount Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::GetComponentsCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetComponentsCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
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

See [HoleSeriesFeatureData::GetComponentsCount](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~GetComponentsCount.html).

## Remarks

Call this method before calling [IHoleSeriesFeatureData::IGetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData~IGetComponents.html) to get the size of the array for that method.

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponents.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
