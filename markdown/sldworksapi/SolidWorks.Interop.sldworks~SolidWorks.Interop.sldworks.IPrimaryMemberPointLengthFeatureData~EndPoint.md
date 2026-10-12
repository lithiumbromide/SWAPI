---
title: "EndPoint Property (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "EndPoint"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndPoint.html"
---

# EndPoint Property (IPrimaryMemberPointLengthFeatureData)

Gets and sets the end point of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndPoint As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Object

instance.EndPoint = value

value = instance.EndPoint
```

### C#

```csharp
System.object EndPoint {get; set;}
```

### C++/CLI

```cpp
property System.Object^ EndPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::EndPoint](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~EndPoint.html).

## Remarks

This property is valid only if [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.html) is [swPrimaryMemberPointLengthEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html).swPrimaryMemberPointLengthEndCondition_UpToPoint.

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
