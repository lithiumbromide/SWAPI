---
title: "UnChainPointsAndLength Property (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "UnChainPointsAndLength"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~UnChainPointsAndLength.html"
---

# UnChainPointsAndLength Property (IPrimaryMemberPointLengthFeatureData)

Gets and sets whether to chain points to create this primary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property UnChainPointsAndLength As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Boolean

instance.UnChainPointsAndLength = value

value = instance.UnChainPointsAndLength
```

### C#

```csharp
System.bool UnChainPointsAndLength {get; set;}
```

### C++/CLI

```cpp
property System.bool UnChainPointsAndLength {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to pair each point passed in [IPrimaryMemberPointLengthFeatureData::SetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints.html) to the previous point in the list, false to pair consecutive points only

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::UnChainPointsAndLength](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~UnChainPointsAndLength.html).

## Remarks

This property is valid only if [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.html) is [swPrimaryMemberPointLengthEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html).swPrimaryMemberPointLengthEndCondition_Point.

If this property is set to true, each point passed to [IPrimaryMemberPointLengthFeatureData::SetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints.html) pairs with the previous point in the list to create a new member.

For the list of points A,B,C,D,E,F:

If this property is set to true, then 5 members are created:

A -- B

B -- C

C -- D

D -- E

E -- F

If this property is set to false, then only 3 members are created:

A -- B

C -- D

E -- F

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
