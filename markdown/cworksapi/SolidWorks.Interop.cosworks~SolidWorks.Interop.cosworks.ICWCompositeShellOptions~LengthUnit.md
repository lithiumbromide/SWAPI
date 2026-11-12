---
title: "LengthUnit Property (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "LengthUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~LengthUnit.html"
---

# LengthUnit Property (ICWCompositeShellOptions)

Gets or sets the units of length.

## Syntax

### Visual Basic (Declaration)

```vb
Property LengthUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim value As System.Integer

instance.LengthUnit = value

value = instance.LengthUnit
```

### C#

```csharp
System.int LengthUnit {get; set;}
```

### C++/CLI

```cpp
property System.int LengthUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Units of length as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWCompositeShellOptions::LengthUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~LengthUnit.html).

## Examples

See the [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html) examples.

## Remarks

This property supports only the following options in swsLinearUnit_e:

- swsLinearUnitMillimeters
- swsLinearUnitCentimeters
- swsLinearUnitMeters
- swsLinearUnitInches
- swsLinearUnitFeet

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
