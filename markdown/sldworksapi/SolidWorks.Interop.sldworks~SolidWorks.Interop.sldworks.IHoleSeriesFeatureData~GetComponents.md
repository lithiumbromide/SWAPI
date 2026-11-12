---
title: "GetComponents Method (IHoleSeriesFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IHoleSeriesFeatureData"
member: "GetComponents"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponents.html"
---

# GetComponents Method (IHoleSeriesFeatureData)

Obsolete. Superseded by [IHoleSeriesFeatureData2::GetComponents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IHoleSeriesFeatureData2~GetComponents.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponents() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IHoleSeriesFeatureData
Dim value As System.Object

value = instance.GetComponents()
```

### C#

```csharp
System.object GetComponents()
```

### C++/CLI

```cpp
System.Object^ GetComponents();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [components](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) in this hole series

## VBA Syntax

See [HoleSeriesFeatureData::GetComponents](ms-its:sldworksapivb6.chm::/sldworks~HoleSeriesFeatureData~GetComponents.html).

## See Also

[IHoleSeriesFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData.html)
[IHoleSeriesFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData_members.html)
[IHoleSeriesFeatureData::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~IGetComponents.html)
[IHoleSeriesFeatureData::GetComponentsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHoleSeriesFeatureData~GetComponentsCount.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
