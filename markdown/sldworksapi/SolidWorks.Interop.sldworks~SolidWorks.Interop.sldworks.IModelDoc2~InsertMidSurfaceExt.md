---
title: "InsertMidSurfaceExt Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertMidSurfaceExt"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.html"
---

# InsertMidSurfaceExt Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertMidSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMidSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMidSurfaceExt( _
   ByVal Placement As System.Double, _
   ByVal KnitFlag As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Placement As System.Double
Dim KnitFlag As System.Boolean
Dim value As System.Object

value = instance.InsertMidSurfaceExt(Placement, KnitFlag)
```

### C#

```csharp
System.object InsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

### C++/CLI

```cpp
System.Object^ InsertMidSurfaceExt(
   System.double Placement,
   System.bool KnitFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Placement`: Value from -1 to 1 that indicates the desired location of the midsurface relative to the face pair; a value of 0.0 places the midsurface equally between the face pair
- `KnitFlag`: True to sew all the reference surfaces (neutral sheets) into a single sheet(surface) body, false for the midsurface feature to contain individual reference surface geometry

### Return Value

[Mid-surface feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2.html)

## VBA Syntax

See [ModelDoc2::InsertMidSurfaceExt](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertMidSurfaceExt.html).

## Remarks

A midsurface feature is calculated from the solid body in your part document. This method first finds all parallel pairs of faces from the part solid. For each pair of parallel faces found, it creates a neutral reference surface between the two faces. The placement position of the reference surface is controlled by the placement parameter. This process repeats itself until all parallel body faces are processed. At the end of this process, all the reference surfaces are sewn into a single reference surface if knitFlag is set to True.

The hierarchy of a midsurface feature is:

A midsurface feature contains one or more reference surfaces. If sewn successfully using the knitFlag = True option, then the midsurface feature contains only one reference surface. Each reference surface is considered a sheet body. The sheet body has the normal topology that you would expect to find on a body object (for example, faces, edges, and so on). See the [IMidSurface2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2.html) object for methods that provide access to this topology.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IInsertMidSurfaceExt Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
