---
title: "GetOwnerFeature Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "GetOwnerFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html"
---

# GetOwnerFeature Method (IFeature)

Gets the feature that owns this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetOwnerFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As Feature

value = instance.GetOwnerFeature()
```

### C#

```csharp
Feature GetOwnerFeature()
```

### C++/CLI

```cpp
Feature^ GetOwnerFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) that owns this feature

## VBA Syntax

See [Feature::GetOwnerFeature](ms-its:sldworksapivb6.chm::/sldworks~Feature~GetOwnerFeature.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetFirstSubFeature.html)
[IFeature::GetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetNextSubFeature.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)
[IFeature::IGetFirstSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetFirstSubFeature.html)
[IFeature::IGetNextSubFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetNextSubFeature.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
