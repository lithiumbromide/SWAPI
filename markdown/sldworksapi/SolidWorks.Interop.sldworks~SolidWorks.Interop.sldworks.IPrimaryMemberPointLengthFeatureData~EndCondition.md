---
title: "EndCondition Property (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.html"
---

# EndCondition Property (IPrimaryMemberPointLengthFeatureData)

Gets and sets the end condition for the member length.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Integer

instance.EndCondition = value

value = instance.EndCondition
```

### C#

```csharp
System.int EndCondition {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

End condition for member length as defined by [swPrimaryMemberPointLengthEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html)

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~EndCondition.html).

## Examples

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
