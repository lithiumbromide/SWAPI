---
title: "InsertExtendSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertExtendSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertExtendSurface.html"
---

# InsertExtendSurface Method (IModelDoc2)

Extends a surface along the selected faces or edges.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertExtendSurface( _
   ByVal ExtendLinear As System.Boolean, _
   ByVal EndCondition As System.Integer, _
   ByVal Distance As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ExtendLinear As System.Boolean
Dim EndCondition As System.Integer
Dim Distance As System.Double

instance.InsertExtendSurface(ExtendLinear, EndCondition, Distance)
```

### C#

```csharp
void InsertExtendSurface(
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
)
```

### C++/CLI

```cpp
void InsertExtendSurface(
   System.bool ExtendLinear,
   System.int EndCondition,
   System.double Distance
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ExtendLinear`: True to extend surface linearly, false to extend along the same surface
- `EndCondition`: - 0 - Extend surface by given distance
  - 1 - Extend surface up to a selected point
  - 2 - Extend surface up to a selected surface
- `Distance`: Distance to extend surface along

## VBA Syntax

See [ModelDoc2::InsertExtendSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertExtendSurface.html).

## Remarks

The selection list can contain faces or edges from the surface. These selected entities will be extended away from the surface according to the input arguments.

The selected point or surface to which to extend should be in the selection list. If EndCondition is to a selected surface, then currently only faces from solids are supported through the API.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
