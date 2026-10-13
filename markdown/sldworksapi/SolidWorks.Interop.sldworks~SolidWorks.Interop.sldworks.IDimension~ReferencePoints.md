---
title: "ReferencePoints Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ReferencePoints"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ReferencePoints.html"
---

# ReferencePoints Property (IDimension)

Gets or sets the reference points for this dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReferencePoints As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Object

instance.ReferencePoints = value

value = instance.ReferencePoints
```

### C#

```csharp
System.object ReferencePoints {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ReferencePoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Reference points (see **Remarks**)

## VBA Syntax

See [Dimension::ReferencePoints](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ReferencePoints.html).

## Remarks

The returned objects, the reference points, are actually [IMathPoint](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathPoint.html) objects.

Reference point 1 and reference point 2 are valid for linear dimensions. Reference point 3 is the vertex for angular dimensions. This property does not distinguish between linear or angular dimensions or other types of dimensions. Three reference points are always returned.

NOTE: When regenerating a [macro feature](sldworksapiprogguide.chm::/macro_features/Overview_of_Macro_Features.htm), this property gets and sets the reference points of a display dimension ([IDisplayDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDisplayDimension.html) object). In all other cases, this property gets and sets the reference points of a dimension ([IDimension](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension.html) object).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
[IDimension::IGetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetReferencePoints.html)
[IDimension::ISetReferencePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetReferencePoints.html)
[IDimension::GetReferencePointsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetReferencePointsCount.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
