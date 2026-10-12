---
title: "GetIntersectionsTools Method (IIntersectFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIntersectFeatureData"
member: "GetIntersectionsTools"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsTools.html"
---

# GetIntersectionsTools Method (IIntersectFeatureData)

Gets the intersecting solids, surfaces, and planes in this intersect feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectionsTools() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IIntersectFeatureData
Dim value As System.Object

value = instance.GetIntersectionsTools()
```

### C#

```csharp
System.object GetIntersectionsTools()
```

### C++/CLI

```cpp
System.Object^ GetIntersectionsTools();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of intersecting [solids](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), [surfaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISurface.html), and [planes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) in this intersect feature

## VBA Syntax

See [IntersectFeatureData::GetIntersectionsTools](ms-its:sldworksapivb6.chm::/sldworks~IntersectFeatureData~GetIntersectionsTools.html).

## See Also

[IIntersectFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData.html)
[IIntersectFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData_members.html)
[IIntersectFeatureData::GetIntersectionsToolsCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~GetIntersectionsToolsCount.html)
[IIntersectFeatureData::SetIntersectionsTools Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIntersectFeatureData~SetIntersectionsTools.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
