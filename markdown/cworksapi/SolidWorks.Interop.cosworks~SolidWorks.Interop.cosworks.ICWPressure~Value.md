---
title: "Value Property (ICWPressure)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPressure"
member: "Value"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Value.html"
---

# Value Property (ICWPressure)

Gets or sets the pressure value.

## Syntax

### Visual Basic (Declaration)

```vb
Property Value As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPressure
Dim value As System.Double

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.double Value {get; set;}
```

### C++/CLI

```cpp
property System.double Value {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Pressure value

## VBA Syntax

See [CWPressure::Value](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPressure~Value.html).

## Examples

See the [ICWPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html) examples.

## See Also

[ICWPressure Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure.html)
[ICWPressure Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure_members.html)
[ICWPressure::Unit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~Unit.html)
[ICWPressure::ReverseDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPressure~ReverseDirection.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
