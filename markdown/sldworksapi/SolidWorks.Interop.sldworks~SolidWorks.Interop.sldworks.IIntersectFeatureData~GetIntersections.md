---
title: "GetIntersections Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "GetIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersections.html"
---

# GetIntersections Method (IIntersectFeatureData)

Gets the intersect regions in this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersections( _
   ByRef Excluded As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim Excluded As System.Object
Dim value As System.Object

value = instance.GetIntersections(Excluded)
```

### C#

```csharp
System.object GetIntersections(
   out System.object Excluded
)
```

### C++/CLI

```cpp
System.Object^ GetIntersections(
   [Out] System.Object^ Excluded
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Excluded`: Array of booleans; true indicates that the corresponding intersect region in the array of returned intersect regions is excluded from this intersect feature

### Return Value

Array of [intersect regions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html)

## VBA Syntax

See [IntersectFeatureData::GetIntersections](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~GetIntersections.html).

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)
[IIntersectFeatureData::SetIntersections Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersections.html)
[IIntersectFeatureData::GetIntersectionsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsCount.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
