---
title: "CornerType Property (ICornerReliefFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICornerReliefFeatureData"
member: "CornerType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~CornerType.html"
---

# CornerType Property (ICornerReliefFeatureData)

Gets the bend type of this corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CornerType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerReliefFeatureData
Dim value As System.Integer

value = instance.CornerType
```

### C#

```csharp
System.int CornerType {get;}
```

### C++/CLI

```cpp
property System.int CornerType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Corner relief bend type as defined by [swCornerReliefBendType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefBendType_e.html)

## VBA Syntax

See [CornerReliefFeatureData::CornerType](ms-its:sldworksapivb6.chm::/sldworks~CornerReliefFeatureData~CornerType.html).

## Remarks

This property cannot be changed after it is set by [ICornerReliefFeatureData::Intialize](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData~Initialize.html).

## See Also

[ICornerReliefFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html)
[ICornerReliefFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
