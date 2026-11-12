---
title: "Visible Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "Visible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Visible.html"
---

# Visible Property (IFeature)

Gets the visibility state of this feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Visible As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.Visible
```

### C#

```csharp
System.int Visible {get;}
```

### C++/CLI

```cpp
property System.int Visible {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Visibility state as defined by [swVisibilityState_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swVisibilityState_e.html)

## VBA Syntax

See [Feature::Visible](ms-its:sldworksapivb6.chm::/sldworks~Feature~Visible.html).

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetUIState.html)
[IFeature::IIsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IIsSuppressed2.html)
[IFeature::ISetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ISetSuppression2.html)
[IFeature::IsSuppressed2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IsSuppressed2.html)
[IFeature::SetSuppression2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetSuppression2.html)
[IFeature::SetUIState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetUIState.html)

## Availability

SOLIDWORKS 2004 SP4, Revision Number 12.4
