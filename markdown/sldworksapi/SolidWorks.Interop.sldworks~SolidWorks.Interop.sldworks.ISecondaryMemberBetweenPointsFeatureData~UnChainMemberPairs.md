---
title: "UnChainMemberPairs Property (ISecondaryMemberBetweenPointsFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberBetweenPointsFeatureData"
member: "UnChainMemberPairs"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~UnChainMemberPairs.html"
---

# UnChainMemberPairs Property (ISecondaryMemberBetweenPointsFeatureData)

Gets and sets whether to chain member pairs to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnChainMemberPairs As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberBetweenPointsFeatureData
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

True to pair each member passed in [ISecondaryMemberBetweenPointsFeatureData::SetMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SetMemberPairs.html) to the previous member passed, false to pair consecutive members only

## VBA Syntax

See [SecondaryMemberBetweenPointsFeatureData::UnChainMemberPairs](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberBetweenPointsFeatureData~UnChainMemberPairs.html).

## Remarks

If this property is set to true, each primary member passed to ISecondaryMemberBetweenPointsFeatureData::SetMemberPairs pairs with the previous primary member to create a new member pair.

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

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.html)
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
