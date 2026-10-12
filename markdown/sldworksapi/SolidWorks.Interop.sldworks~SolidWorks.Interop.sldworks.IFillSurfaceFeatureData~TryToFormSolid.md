---
title: "TryToFormSolid Property (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "TryToFormSolid"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~TryToFormSolid.html"
---

# TryToFormSolid Property (IFillSurfaceFeatureData)

Gets or sets whether to form a solid.

## Syntax

### Visual Basic (Declaration)

```vb
Property TryToFormSolid As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean

instance.TryToFormSolid = value

value = instance.TryToFormSolid
```

### C#

```csharp
System.bool TryToFormSolid {get; set;}
```

### C++/CLI

```cpp
property System.bool TryToFormSolid {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if trying to form solid, false if not

## VBA Syntax

See [FillSurfaceFeatureData::TryToFormSolid](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~TryToFormSolid.html).

## Remarks

The behavior for this option depends on the boundaries.

- When all the boundaries belong to the same solid body, you can use the surface fill to patch the solid.
- If at least one of the edges is an open sheet edge and you merge results, then the fill knits with the surfaces to which the edges belong. See [IFillSurfaceFeatureData::Merge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~Merge.html) for details about merging results.
- If all the boundary entities are open edges, then a solid may be created.

See [IFillSurfaceFeatureData::GetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~GetPatchBoundary.html) or [IFillSurfaceFeatureData::IGetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~IGetPatchBoundary.html) and [IFillSurfaceFeatureData::SetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~SetPatchBoundary.html) or [IFillSurfaceFeatureData::ISetPatchBoundary](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFillSurfaceFeatureData~ISetPatchBoundary.html) for details about boundary entities.

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
