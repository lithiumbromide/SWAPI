---
title: "SetReferenceLocations Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "SetReferenceLocations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetReferenceLocations.html"
---

# SetReferenceLocations Method (IPrimaryMemberRefPlaneFeatureData)

Gets the location reference(s) used to create this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetReferenceLocations( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean

value = instance.SetReferenceLocations(RetEntities)
```

### C#

```csharp
System.bool SetReferenceLocations(
   System.object RetEntities
)
```

### C++/CLI

```cpp
System.bool SetReferenceLocations(
   System.Object^ RetEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RetEntities`: Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

### Return Value

True if location references successfully set, false if not

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::SetReferenceLocations](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~SetReferenceLocations.html).

## Examples

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## Remarks

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.html) * [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.html))

During:

- creation, you can set any number of entities that are intersecting with the start and end references and at least one reference axis entity.
- editing, you can set only one entity that is intersecting with the start and end refereces and one reference axis entity.

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
