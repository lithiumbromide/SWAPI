---
title: "Gravity Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "Gravity"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~Gravity.html"
---

# Gravity Property (ICWDropTestSetup)

Gets or sets the magnitude of gravity.

## Syntax

### Visual Basic (Declaration)

```vb
Property Gravity As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.Gravity = value

value = instance.Gravity
```

### C#

```csharp
System.double Gravity {get; set;}
```

### C++/CLI

```cpp
property System.double Gravity {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Magnitude of gravity

## VBA Syntax

See [CWDropTestSetup::Gravity](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~Gravity.html).

## Examples

See the examples in [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html).

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)
[ICWDropTestSetup::SetEntityForGravityDirection Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~SetEntityForGravityDirection.html)
[ICWDropTestSetup::FlipGravityDirection Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~FlipGravityDirection.html)
[ICWDropTestSetup::GravityUnit Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~GravityUnit.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
