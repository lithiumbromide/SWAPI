---
title: "GetStartAndEndReferences Method (IPrimaryMemberRefPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IPrimaryMemberRefPlaneFeatureData"
member: "GetStartAndEndReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData~GetStartAndEndReferences.html"
---

# GetStartAndEndReferences Method (IPrimaryMemberRefPlaneFeatureData)

Gets the start and end reference entities that are used to define the length of this structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStartAndEndReferences() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPrimaryMemberRefPlaneFeatureData
Dim value As System.Object

value = instance.GetStartAndEndReferences()
```

### C#

```csharp
System.object GetStartAndEndReferences()
```

### C++/CLI

```cpp
System.Object^ GetStartAndEndReferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of two parallel entities ([IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.html)s and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)s)

## VBA Syntax

See [PrimaryMemberRefPlaneFeatureData::GetStartAndEndReferences](ms-its:sldworksapivb6.chm::/sldworks~PrimaryMemberRefPlaneFeatureData~GetStartAndEndReferences.html).

## Remarks

The parallel entities returned by this method must be perpendicular and intersect the reference axes.

## See Also

[IPrimaryMemberRefPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData.html)
[IPrimaryMemberRefPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberRefPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
