---
title: "WeldmentCutListFeature Property (IWeldmentCutListAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentCutListAnnotation"
member: "WeldmentCutListFeature"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation~WeldmentCutListFeature.html"
---

# WeldmentCutListFeature Property (IWeldmentCutListAnnotation)

Gets the weldment cut list feature for this weldment cut list table annotation.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property WeldmentCutListFeature As WeldmentCutListFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentCutListAnnotation
Dim value As WeldmentCutListFeature

value = instance.WeldmentCutListFeature
```

### C#

```csharp
WeldmentCutListFeature WeldmentCutListFeature {get;}
```

### C++/CLI

```cpp
property WeldmentCutListFeature^ WeldmentCutListFeature {
   WeldmentCutListFeature^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Weldment cut list feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListFeature.html)

## VBA Syntax

See [WeldmentCutListAnnotation::WeldmentCutListFeature](ms-its:sldworksapivb6.chm::/sldworks~WeldmentCutListAnnotation~WeldmentCutListFeature.html).

## See Also

[IWeldmentCutListAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation.html)
[IWeldmentCutListAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentCutListAnnotation_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
