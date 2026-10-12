---
title: "FixtureNameInSelectedExcitation Property (ICWBaseExcitation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBaseExcitation"
member: "FixtureNameInSelectedExcitation"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation~FixtureNameInSelectedExcitation.html"
---

# FixtureNameInSelectedExcitation Property (ICWBaseExcitation)

Gets or sets the fixture name for this selected excitation.

## Syntax

### Visual Basic (Declaration)

```vb
Property FixtureNameInSelectedExcitation As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBaseExcitation
Dim value As System.String

instance.FixtureNameInSelectedExcitation = value

value = instance.FixtureNameInSelectedExcitation
```

### C#

```csharp
System.string FixtureNameInSelectedExcitation {get; set;}
```

### C++/CLI

```cpp
property System.String^ FixtureNameInSelectedExcitation {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Fixture name (see **Remarks**)

## VBA Syntax

See [CWBaseExcitation::FixtureNameInSelectedExcitation](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBaseExcitation~FixtureNameInSelectedExcitation.html).

## Remarks

This method applies only to selected base excitations that are created using [ICWLoadsAndRestraintsManager::AddSelectedBaseExcitation](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWLoadsAndRestraintsManager~AddSelectedBaseExcitation.html).

## See Also

[ICWBaseExcitation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation.html)
[ICWBaseExcitation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBaseExcitation_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
