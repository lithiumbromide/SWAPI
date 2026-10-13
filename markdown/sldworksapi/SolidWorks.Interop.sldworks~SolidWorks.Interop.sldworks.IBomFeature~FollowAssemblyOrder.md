---
title: "FollowAssemblyOrder Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "FollowAssemblyOrder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder.html"
---

# FollowAssemblyOrder Method (IBomFeature)

Obsolete. Superseded by [IBomFeature::FollowAssemblyOrder2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function FollowAssemblyOrder() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

value = instance.FollowAssemblyOrder()
```

### C#

```csharp
System.bool FollowAssemblyOrder()
```

### C++/CLI

```cpp
System.bool FollowAssemblyOrder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True for the items numbers in the BOM to follow the order in which the assembly appears in the FeatureManager design tree, false to not

## VBA Syntax

See [BomFeature::FollowAssemblyOrder](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~FollowAssemblyOrder.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
