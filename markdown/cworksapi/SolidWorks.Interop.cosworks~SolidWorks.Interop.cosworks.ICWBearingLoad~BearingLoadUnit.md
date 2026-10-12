---
title: "BearingLoadUnit Property (ICWBearingLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBearingLoad"
member: "BearingLoadUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad~BearingLoadUnit.html"
---

# BearingLoadUnit Property (ICWBearingLoad)

Gets or sets the unit system for this bearing load.

## Syntax

### Visual Basic (Declaration)

```vb
Property BearingLoadUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBearingLoad
Dim value As System.Integer

instance.BearingLoadUnit = value

value = instance.BearingLoadUnit
```

### C#

```csharp
System.int BearingLoadUnit {get; set;}
```

### C++/CLI

```cpp
property System.int BearingLoadUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Unit system as defined in [swsUnit_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnit_e.html)

## VBA Syntax

See [CWBearingLoad::BearingLoadUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBearingLoad~BearingLoadUnit.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## See Also

[ICWBearingLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html)
[ICWBearingLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad_members.html)

## Availability

SOLIDWORKS Simulation API 2009 SP0
