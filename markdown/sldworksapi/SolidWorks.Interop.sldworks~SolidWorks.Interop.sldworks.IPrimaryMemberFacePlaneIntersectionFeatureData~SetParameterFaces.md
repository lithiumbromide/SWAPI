---
title: "SetParameterFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberFacePlaneIntersectionFeatureData"
member: "SetParameterFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~SetParameterFaces.html"
---

# SetParameterFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Sets the parameter faces of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetParameterFaces( _
   ByVal Faces As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim Faces As System.Object
Dim value As System.Boolean

value = instance.SetParameterFaces(Faces)
```

### C#

```csharp
System.bool SetParameterFaces(
   System.object Faces
)
```

### C++/CLI

```cpp
System.bool SetParameterFaces(
   System.Object^ Faces
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Faces`: Array of [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

### Return Value

True if parameter faces successfully set, false if not

## VBA Syntax

See [PrimaryMemberFacePlaneIntersectionFeatureData::SetParameterFaces](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberFacePlaneIntersectionFeatureData~SetParameterFaces.html).

## Examples

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html) examples.

## Remarks

Only [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html).swSelFACES type entities can be set using this method.

At edit time you can set only one parameter face.

## See Also

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
