---
title: "CoordSystemType Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "CoordSystemType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~CoordSystemType.html"
---

# CoordSystemType Property (ICWPressure)

Gets or sets the type of coordinate system used to define this nonuniform pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Property CoordSystemType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

instance.CoordSystemType = value

value = instance.CoordSystemType
```

### C#

```csharp
System.int CoordSystemType {get; set;}
```

### C++/CLI

```cpp
property System.int CoordSystemType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of coordinate system as defined in [swsCoordinateType_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCoordinateType_e.html)

## VBA Syntax

See [CWPressure::CoordSystemType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~CoordSystemType.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## Remarks

This method is valid only if [ICWPressure::IncludeNonUniformDistribution](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~IncludeNonUniformDistribution.html) is set to true.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::GetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~GetCoordinateSystem.html)
[ICWPressure::SetCoordinateSystem Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetCoordinateSystem.html)
[ICWPressure::Equation Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Equation.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
