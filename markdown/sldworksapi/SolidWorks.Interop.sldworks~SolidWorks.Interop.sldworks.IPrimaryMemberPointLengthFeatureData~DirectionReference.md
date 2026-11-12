---
title: "DirectionReference Property (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "DirectionReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~DirectionReference.html"
---

# DirectionReference Property (IPrimaryMemberPointLengthFeatureData)

Gets and sets the reference indicating the direction of this member.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionReference As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Object

instance.DirectionReference = value

value = instance.DirectionReference
```

### C#

```csharp
System.object DirectionReference {get; set;}
```

### C++/CLI

```cpp
property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IEdge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html) or [ISketchSegment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSegment.html)

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::DirectionReference](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~DirectionReference.html).

## Remarks

This property is:

- required for 3D sketches.
- valid only when [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.html) is [swPrimaryMemberPointLengthEndCondition_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html):

  - swPrimaryMemberPointLengthEndCondition_UpToPlane
  - swPrimaryMemberPointLengthEndCondition_Length

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
