---
title: "OpenSystem Property (ICWRadiation)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRadiation"
member: "OpenSystem"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~OpenSystem.html"
---

# OpenSystem Property (ICWRadiation)

Obsolete. Superseded by [ICWRadiation::OpenSystem2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~OpenSystem2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property OpenSystem As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRadiation
Dim value As System.Integer

instance.OpenSystem = value

value = instance.OpenSystem
```

### C#

```csharp
System.int OpenSystem {get; set;}
```

### C++/CLI

```cpp
property System.int OpenSystem {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

System as defined in [swsRadiationOpenSystem_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsRadiationOpenSystem_e.html)

## VBA Syntax

See [CWRadiation::OpenSystem](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRadiation~OpenSystem.html).

## See Also

[ICWRadiation Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation.html)
[ICWRadiation Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation_members.html)
[ICWRadiaiton::AmbientTemperature Property](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRadiation~AmbientTemperature.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
