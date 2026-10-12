---
title: "DirectionType Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "DirectionType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~DirectionType.html"
---

# DirectionType Property (ICWPressure)

Gets or sets how this pressure is applied along the specified reference geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Property DirectionType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

instance.DirectionType = value

value = instance.DirectionType
```

### C#

```csharp
System.int DirectionType {get; set;}
```

### C++/CLI

```cpp
property System.int DirectionType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Pressure direction type (see **Remarks**)

## VBA Syntax

See [CWPressure::DirectionType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~DirectionType.html).

## Requirements

This property is valid only if [ICWPressure::PressureType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PressureType.html) is [swsPressureType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsPressureType_e.html).swsPressureTypeUseReferenceGeometry.

Pressure direction type depends on the reference geometry that is set using [ICWPressure::SetReferenceGeometry](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetReferenceGeometry.html).

| If direction reference is... | Then set this property to a direction as defined in... |
| --- | --- |
| Planar face or reference plane | swsPressureReferenceGeometryPlanarType_e |
| Cylindrical face | swsPressureReferenceGeometryCylindricalType_e |
| Reference axis | swsPressureReferenceGeometryReferenceAxisType_e |
| Edge | swsPressureReferenceGeometryEdgeType_e |

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
