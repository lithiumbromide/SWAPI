---
title: "GetReferenceLocations Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "GetReferenceLocations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocations.html"
---

# GetReferenceLocations Method (IPrimaryMemberRefPlaneFeatureData)

Gets the position reference(s) used to create this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceLocations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim value As System.Object

value = instance.GetReferenceLocations()
```

### C#

```csharp
System.object GetReferenceLocations()
```

### C++/CLI

```cpp
System.Object^ GetReferenceLocations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of parallel [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::GetReferenceLocations](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~GetReferenceLocations.html).

## Remarks

The parallel entities returned by this method can be parallel or non-parallel to the start and end reference entities.

The number of members created = ([IPrimaryMemberRefPlaneFeatureData::GetReferenceAxes](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceAxes.html) * IPrimaryMemberRefPlaneFeatureData::GetReferenceLocations)

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
