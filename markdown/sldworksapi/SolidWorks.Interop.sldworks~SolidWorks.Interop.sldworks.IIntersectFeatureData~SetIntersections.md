---
title: "SetIntersections Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "SetIntersections"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersections.html"
---

# SetIntersections Method (IIntersectFeatureData)

Specifies which of the intersect regions to exclude from this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIntersections( _
   ByVal Intersections As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim Intersections As System.Object

instance.SetIntersections(Intersections)
```

### C#

```csharp
void SetIntersections(
   System.object Intersections
)
```

### C++/CLI

```cpp
void SetIntersections(
   System.Object^ Intersections
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Intersections`: Array of booleans; true indicates to exclude the corresponding intersect region in the array of intersect regions returned by [IIntersectFeatureData::GetIntersections](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IIntersectFeatureData~GetIntersections.html)

## VBA Syntax

See [IntersectFeatureData::SetIntersections](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~SetIntersections.html).

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
