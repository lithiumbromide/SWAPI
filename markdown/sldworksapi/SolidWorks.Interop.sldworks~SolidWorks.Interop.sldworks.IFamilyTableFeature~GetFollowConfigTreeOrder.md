---
title: "GetFollowConfigTreeOrder Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetFollowConfigTreeOrder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetFollowConfigTreeOrder.html"
---

# GetFollowConfigTreeOrder Method (IFamilyTableFeature)

Gets whether the configuration tree order is used in this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFollowConfigTreeOrder() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.Boolean

value = instance.GetFollowConfigTreeOrder()
```

### C#

```csharp
System.bool GetFollowConfigTreeOrder()
```

### C++/CLI

```cpp
System.bool GetFollowConfigTreeOrder();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if uses the configuration tree order, false if not

## VBA Syntax

See [FamilyTableFeature::GetFollowConfigTreeOrder](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetFollowConfigTreeOrder.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
