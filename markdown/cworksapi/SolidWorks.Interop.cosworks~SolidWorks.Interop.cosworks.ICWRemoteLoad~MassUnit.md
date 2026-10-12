---
title: "MassUnit Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "MassUnit"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~MassUnit.html"
---

# MassUnit Property (ICWRemoteLoad)

Gets or sets the unit system for remote mass.

## Syntax

### Visual Basic (Declaration)

```vb
Property MassUnit As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

instance.MassUnit = value

value = instance.MassUnit
```

### C#

```csharp
System.int MassUnit {get; set;}
```

### C++/CLI

```cpp
property System.int MassUnit {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Unit of mass as defined by [swsUnitSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsUnitSystem_e.html)

## VBA Syntax

See [CWRemoteLoad::MassUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~MassUnit.html).

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::GetMassValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~GetMassValues.html)
[ICWRemoteLoad::SetMassValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~SetMassValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
