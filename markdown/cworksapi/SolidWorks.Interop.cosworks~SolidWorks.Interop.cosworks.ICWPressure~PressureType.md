---
title: "PressureType Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "PressureType"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~PressureType.html"
---

# PressureType Property (ICWPressure)

Gets or sets the pressure direction type (normal or use reference geometry).

## Syntax

### Visual Basic (Declaration)

```vb
Property PressureType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

instance.PressureType = value

value = instance.PressureType
```

### C#

```csharp
System.int PressureType {get; set;}
```

### C++/CLI

```cpp
property System.int PressureType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Pressure direction type as defined in [swsPressureType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsPressureType_e.html)

## VBA Syntax

See [CWPressure::PressureType](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~PressureType.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::DirectionType Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~DirectionType.html)
[ICWPressure::SetReferenceGeometry Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~SetReferenceGeometry.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
