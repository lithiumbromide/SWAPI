---
title: "GetReferenceAxes Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "GetReferenceAxes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.html"
---

# GetReferenceAxes Method (IPrimaryMemberRefPlaneFeatureData)

Gets the direction reference(s) used to create this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceAxes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim value As System.Object

value = instance.GetReferenceAxes()
```

### C#

```csharp
System.object GetReferenceAxes()
```

### C++/CLI

```cpp
System.Object^ GetReferenceAxes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::GetReferenceAxes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~GetReferenceAxes.html).

## Remarks

The parallel entities returned by this method must be perpendicular to and intersect the start and end references.

The number of members created = (IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes * [IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.html))

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
