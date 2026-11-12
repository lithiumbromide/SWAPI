---
title: "SetIntersectionsTools Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "SetIntersectionsTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersectionsTools.html"
---

# SetIntersectionsTools Method (IIntersectFeatureData)

Specifies the intersecting solids, surfaces, and planes for this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIntersectionsTools( _
   ByVal Tools As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim Tools As System.Object

instance.SetIntersectionsTools(Tools)
```

### C#

```csharp
void SetIntersectionsTools(
   System.object Tools
)
```

### C++/CLI

```cpp
void SetIntersectionsTools(
   System.Object^ Tools
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Tools`: Array of intersecting [solids](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html), and [planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) for this intersect feature

## VBA Syntax

See [IntersectFeatureData::SetIntersectionsTools](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~SetIntersectionsTools.html).

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)
[IIntersectFeatureData::GetIntersectionsTools Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
