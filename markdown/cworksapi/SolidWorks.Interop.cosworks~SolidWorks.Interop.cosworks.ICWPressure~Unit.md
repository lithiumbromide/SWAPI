---
title: "Unit Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Unit.html"
---

# Unit Property (ICWPressure)

Gets or sets the units of pressure.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Integer

instance.Unit = value

value = instance.Unit
```

### C#

```csharp
System.int Unit {get; set;}
```

### C++/CLI

```cpp
property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units as defined in [swsStrengthUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsStrengthUnit_e.html)

## VBA Syntax

See [CWPressure::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~Unit.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::Value Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Value.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
