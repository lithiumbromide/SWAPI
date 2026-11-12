---
title: "IsThinFeature Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "IsThinFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.html"
---

# IsThinFeature Method (IRevolveFeatureData2)

Gets whether the revolution is a thin feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsThinFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
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

True if revolution is a thin feature, false if not

## VBA Syntax

See [RevolveFeatureData2::IsThinFeature](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~IsThinFeature.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::GetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.html)
[IRevolveFeatureData2::IsBossFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsBossFeature.html)
[IRevolveFeatureData2::SetWallThickness Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.html)
[IRevolveFeatureData2::ThinWallType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~ThinWallType.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
