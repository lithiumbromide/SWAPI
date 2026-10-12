---
title: "SetFollowConfigTreeOrder Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "SetFollowConfigTreeOrder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~SetFollowConfigTreeOrder.html"
---

# SetFollowConfigTreeOrder Method (IFamilyTableFeature)

Sets whether the configuration tree order is used in this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFollowConfigTreeOrder( _
   ByVal Flag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim Flag As System.Boolean

instance.SetFollowConfigTreeOrder(Flag)
```

### C#

```csharp
void SetFollowConfigTreeOrder(
   System.bool Flag
)
```

### C++/CLI

```cpp
void SetFollowConfigTreeOrder(
   System.bool Flag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Flag`: True if the configuration tree order is used, false if not

## VBA Syntax

See [FamilyTableFeature::SetFollowConfigTreeOrder](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~SetFollowConfigTreeOrder.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
