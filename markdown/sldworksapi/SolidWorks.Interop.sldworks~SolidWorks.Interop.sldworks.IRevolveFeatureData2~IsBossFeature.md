---
title: "IsBossFeature Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "IsBossFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsBossFeature.html"
---

# IsBossFeature Method (IRevolveFeatureData2)

Gets whether the revolution is a boss feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsBossFeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Boolean

value = instance.IsBossFeature()
```

### C#

```csharp
System.bool IsBossFeature()
```

### C++/CLI

```cpp
System.bool IsBossFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if revolution is a boss feature, false if not

## VBA Syntax

See [RevolveFeatureData2::IsBossFeature](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~IsBossFeature.html).

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::IsThinFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~IsThinFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
