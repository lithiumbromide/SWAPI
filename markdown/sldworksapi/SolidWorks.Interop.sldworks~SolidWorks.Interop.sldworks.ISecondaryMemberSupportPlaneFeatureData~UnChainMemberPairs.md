---
title: "UnChainMemberPairs Property (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "UnChainMemberPairs"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~UnChainMemberPairs.html"
---

# UnChainMemberPairs Property (ISecondaryMemberSupportPlaneFeatureData)

Gets and sets whether to chain member pairs to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnChainMemberPairs As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim value As System.Boolean

instance.UnChainMemberPairs = value

value = instance.UnChainMemberPairs
```

### C#

```csharp
System.bool UnChainMemberPairs {get; set;}
```

### C++/CLI

```cpp
property System.bool UnChainMemberPairs {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to pair each member passed in [ISecondaryMemberSupportPlaneFeatureData::SetMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~SetMemberPairs.html) to the previous member passed, false to pair consecutive members only

## VBA Syntax

See [SecondaryMemberSupportPlaneFeatureData::UnChainMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~UnChainMemberPairs.html).

## Remarks

If this property is set to true, each primary member passed to ISecondaryMemberSupportPlaneFeatureData::SetMemberPairs pairs with the previous primary member in the list to create a new member pair.

For the list of members A,B,C,D,E,F:

If this property is set to true, then 5 member pairs are created:

A -- B

B -- C

C -- D

D -- E

E -- F

If this property is set to false, then only 3 member pairs are created:

A -- B

C -- D

E -- F

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
