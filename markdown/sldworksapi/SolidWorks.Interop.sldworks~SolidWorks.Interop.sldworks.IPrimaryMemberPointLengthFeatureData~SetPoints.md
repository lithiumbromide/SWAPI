---
title: "SetPoints Method (IPrimaryMemberPointLengthFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPointLengthFeatureData"
member: "SetPoints"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints.html"
---

# SetPoints Method (IPrimaryMemberPointLengthFeatureData)

Sets the vertexes, sketch points, and reference points.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetPoints( _
   ByVal Points As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPointLengthFeatureData
Dim Points As System.Object
Dim value As System.Boolean

value = instance.SetPoints(Points)
```

### C#

```csharp
System.bool SetPoints(
   System.object Points
)
```

### C++/CLI

```cpp
System.bool SetPoints(
   System.Object^ Points
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Points`: Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.html)es, [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.html)s, and/or [IRefPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.html)s

### Return Value

True if points successfully set, false if not

## VBA Syntax

See [PrimaryMemberPointLengthFeatureData::SetPoints](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPointLengthFeatureData~SetPoints.html).

## Examples

See the [IPrimaryMemberPointLengthFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html) examples.

## Remarks

Use [IPrimaryMemberPointLengthFeatureData::UnChainPointsAndLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~UnChainPointsAndLength.html) to specify whether to chain link members along a chain of points.

## See Also

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.html)
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
