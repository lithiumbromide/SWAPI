---
title: "GetPathSegmentsTypes Method (IPrimaryMemberPathSegmentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberPathSegmentFeatureData"
member: "GetPathSegmentsTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData~GetPathSegmentsTypes.html"
---

# GetPathSegmentsTypes Method (IPrimaryMemberPathSegmentFeatureData)

Gets the types of path segments used to create the structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPathSegmentsTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberPathSegmentFeatureData
Dim value As System.Object

value = instance.GetPathSegmentsTypes()
```

### C#

```csharp
System.object GetPathSegmentsTypes()
```

### C++/CLI

```cpp
System.Object^ GetPathSegmentsTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of path segment types as defined by [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html):

- swSelSKETCHES
- swSelEDGES
- swSelREFCURVES

## VBA Syntax

See [PrimaryMemberPathSegmentFeatureData::GetPathSegmentsTypes](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberPathSegmentFeatureData~GetPathSegmentsTypes.html).

## See Also

[IPrimaryMemberPathSegmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData.html)
[IPrimaryMemberPathSegmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPathSegmentFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
