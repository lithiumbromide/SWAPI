---
title: "GetIntersectingObjectTypes Method (IPrimaryMemberFacePlaneIntersectionFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberFacePlaneIntersectionFeatureData"
member: "GetIntersectingObjectTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingObjectTypes.html"
---

# GetIntersectingObjectTypes Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Gets the types of entities that intersect with parameter faces of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectingObjectTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim value As System.Object

value = instance.GetIntersectingObjectTypes()
```

### C#

```csharp
System.object GetIntersectingObjectTypes()
```

### C++/CLI

```cpp
System.Object^ GetIntersectingObjectTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of intersecting object types as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelFACES
- swSelREFFACES
- swSelDATUMPLANES

## VBA Syntax

See [PrimaryMemberFacePlaneIntersectionFeatureData::GetIntersectingObjectTypes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberFacePlaneIntersectionFeatureData~GetIntersectingObjectTypes.html).

## See Also

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.html)
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
