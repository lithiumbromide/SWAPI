---
title: "SetStartAndEndReferences Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "SetStartAndEndReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~SetStartAndEndReferences.html"
---

# SetStartAndEndReferences Method (IPrimaryMemberRefPlaneFeatureData)

Sets the start and end reference entities that are used to define the length of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStartAndEndReferences( _
   ByVal RetEntities As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim RetEntities As System.Object
Dim value As System.Boolean

value = instance.SetStartAndEndReferences(RetEntities)
```

### C#

```csharp
System.bool SetStartAndEndReferences(
   System.object RetEntities
)
```

### C++/CLI

```cpp
System.bool SetStartAndEndReferences(
   System.Object^ RetEntities
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RetEntities`: Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

### Return Value

True if start and end references successfully set, false if not

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::SetStartAndEndReferences](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~SetStartAndEndReferences.html).

## Examples

See the [IPrimaryMemberRefPlaneFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html) examples.

## Remarks

The array set by this method should have only two entities: start and end references.

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
