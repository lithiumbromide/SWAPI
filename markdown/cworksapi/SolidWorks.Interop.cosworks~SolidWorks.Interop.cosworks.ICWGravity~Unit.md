---
title: "Unit Property (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "Unit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~Unit.html"
---

# Unit Property (ICWGravity)

Gets or sets the units for gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Property Unit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
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

Unit system as defined in [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWGravity::Unit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~Unit.html).

## Examples

See the [ICWGravity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html) examples.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
