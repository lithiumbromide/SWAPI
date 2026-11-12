---
title: "IGetChildCount Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetChildCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html"
---

# IGetChildCount Method (IFeature)

Gets the number of child features that belong to this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetChildCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.IGetChildCount()
```

### C#

```csharp
System.int IGetChildCount()
```

### C++/CLI

```cpp
System.int IGetChildCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of direct children belonging to this feature

## VBA Syntax

See [Feature::IGetChildCount](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetChildCount.html).

## Remarks

Call this method before calling [IFeature::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetChildren.html) to determine the size of the array.

This method gets the number of direct children belonging to this feature, not including children of children.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::IGetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParents.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetParentCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html)

## Availability

SOLIDWORKS 99, datecode 1999207
