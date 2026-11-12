---
title: "CornerCount Property (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "CornerCount"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerCount.html"
---

# CornerCount Property (ICornerReliefFeatureData)

Gets the number of corner objects in this corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CornerCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim value As System.Integer

value = instance.CornerCount
```

### C#

```csharp
System.int CornerCount {get;}
```

### C++/CLI

```cpp
property System.int CornerCount {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Number of [ISMCornerReliefData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html) objects

## VBA Syntax

See [CornerReliefFeatureData::CornerCount](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~CornerCount.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
