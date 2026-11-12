---
title: "ReverseSurface Property (IFillSurfaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IFillSurfaceFeatureData"
member: "ReverseSurface"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~ReverseSurface.html"
---

# ReverseSurface Property (IFillSurfaceFeatureData)

Gets or sets direction of the surface patch.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseSurface As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFillSurfaceFeatureData
Dim value As System.Boolean

instance.ReverseSurface = value

value = instance.ReverseSurface
```

### C#

```csharp
System.bool ReverseSurface {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseSurface {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True reverses the direction of the surface patch, false does not

## VBA Syntax

See [FillSurfaceFeatureData::ReverseSurface](ms-its:sldworksapivb6.chm::/sldworks~FillSurfaceFeatureData~ReverseSurface.html).

## Remarks

This property is dynamic and is only available when:

- All boundary curves are coplanar
- No constraint points exist
- No interior constraints
- Fill surface is nonplanar

## See Also

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.html)
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
