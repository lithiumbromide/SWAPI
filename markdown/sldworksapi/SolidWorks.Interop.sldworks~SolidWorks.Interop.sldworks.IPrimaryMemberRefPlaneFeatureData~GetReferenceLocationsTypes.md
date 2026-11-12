---
title: "GetReferenceLocationsTypes Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "GetReferenceLocationsTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetReferenceLocationsTypes.html"
---

# GetReferenceLocationsTypes Method (IPrimaryMemberRefPlaneFeatureData)

Gets the types of location references for this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferenceLocationsTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim value As System.Object

value = instance.GetReferenceLocationsTypes()
```

### C#

```csharp
System.object GetReferenceLocationsTypes()
```

### C++/CLI

```cpp
System.Object^ GetReferenceLocationsTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of start and end reference types as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelDATUMPLANES
- swSelFACES

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::GetReferenceLocationsTypes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~GetReferenceLocationsTypes.html).

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
