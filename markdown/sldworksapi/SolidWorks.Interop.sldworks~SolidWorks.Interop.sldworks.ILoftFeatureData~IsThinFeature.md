---
title: "IsThinFeature Method (ILoftFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILoftFeatureData"
member: "IsThinFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsThinFeature.html"
---

# IsThinFeature Method (ILoftFeatureData)

Gets whether this loft feature is a thin feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsThinFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ILoftFeatureData
Dim value As System.Boolean

value = instance.IsThinFeature()
```

### C#

```csharp
System.bool IsThinFeature()
```

### C++/CLI

```cpp
System.bool IsThinFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if it is a thin feature, false if not

## VBA Syntax

See [LoftFeatureData::IsThinFeature](ms-its:sldworksapivb6.chm::/sldworks~LoftFeatureData~IsThinFeature.html).

## See Also

[ILoftFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData.html)
[ILoftFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData_members.html)
[ILoftFeatureData::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~GetWallThickness.html)
[ILoftFeatureData::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~SetWallThickness.html)
[ILoftFeatureData::IsBossFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~IsBossFeature.html)
[ILoftFeatureData::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoftFeatureData~ThinWallType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
