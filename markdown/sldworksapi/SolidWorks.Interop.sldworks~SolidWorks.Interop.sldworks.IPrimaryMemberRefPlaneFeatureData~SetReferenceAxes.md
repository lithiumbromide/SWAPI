---
title: "SetReferenceAxes Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "SetReferenceAxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetReferenceAxes.html"
---

# SetReferenceAxes Method (IPrimaryMemberRefPlaneFeatureData)

Sets the direction reference(s) for this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetReferenceAxes( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean

value = instance.SetReferenceAxes(RetEntities)
```

### C#

```csharp
System.bool SetReferenceAxes(
   System.object RetEntities
)
```

### C++/CLI

```cpp
System.bool SetReferenceAxes(
   System.Object^ RetEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RetEntities`: Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

### Return Value

True if reference axes successfully set, false if not

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::SetReferenceAxes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~SetReferenceAxes.html).

## Examples

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## Remarks

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.html) * [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.html))

During:

- creation, you can set any number of entities that are intersecting with the start and end reference ([IPrimaryMemberRefPlaneFeatureData::GetStartAndEndReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetStartAndEndReferences.html)).
- editing, you can set only one entity that intersects with the start and end reference.

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
