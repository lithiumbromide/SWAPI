---
title: "IGetParentCount Method (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "IGetParentCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetParentCount.html"
---

# IGetParentCount Method (IFeature)

Gets the number of parent features for this feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetParentCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As System.Integer

value = instance.IGetParentCount()
```

### C#

```csharp
System.int IGetParentCount()
```

### C++/CLI

```cpp
System.int IGetParentCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of direct parents for this feature

## VBA Syntax

See [Feature::IGetParentCount](ms-its:sldworksapivb6.chm::/sldworks~Feature~IGetParentCount.html).

## Examples

[Get Parent Features (C++)](Get_Parent_Features_Example_CPlusPlus_COM.htm)

## Remarks

Call this method before calling [IFeature::IGetParents](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetParents.html) to determine the size of the array.

This method gets the number of direct parents for this feature, not including parents of parents.

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IFeature::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetChildren.html)
[IFeature::GetOwnerFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetOwnerFeature.html)
[IFeature::GetParents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetParents.html)
[IFeature::IGetChildCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildCount.html)
[IFeature::IGetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~IGetChildren.html)

## Availability

SOLIDWORKS 99, datecode 1999207
