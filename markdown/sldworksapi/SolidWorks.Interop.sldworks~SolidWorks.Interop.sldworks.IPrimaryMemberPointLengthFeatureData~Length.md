---
title: "Length Property (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "Length"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~Length.html"
---

# Length Property (IPrimaryMemberPointLengthFeatureData)

Gets and sets the length of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property Length As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Double

instance.Length = value

value = instance.Length
```

### C#

```csharp
System.double Length {get; set;}
```

### C++/CLI

```cpp
property System.double Length {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Length

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::Length](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~Length.html).

## Examples

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

## Remarks

This property is valid only if [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.html) is [swPrimaryMemberPointLengthEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html).swPrimaryMemberPointLengthEndCondition_Length.

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
