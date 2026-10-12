---
title: "FollowAssemblyOrder2 Property (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "FollowAssemblyOrder2"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.html"
---

# FollowAssemblyOrder2 Property (IBomFeature)

Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
Property FollowAssemblyOrder2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.Boolean

instance.FollowAssemblyOrder2 = value

value = instance.FollowAssemblyOrder2
```

### C#

```csharp
System.bool FollowAssemblyOrder2 {get; set;}
```

### C++/CLI

```cpp
property System.bool FollowAssemblyOrder2 {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for the item numbers in the BOM to follow the order in which the assembly appears in the FeatureManager design tree, false to not

## VBA Syntax

See [BomFeature::FollowAssemblyOrder2](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~FollowAssemblyOrder2.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)
[IBomFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepCurrentItemNumbers.html)

## Availability

SOLIDWORKS 2005 SP2, Revision Number 13
