---
title: "Options Property (ICWContactSet)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: "Options"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet~Options.html"
---

# Options Property (ICWContactSet)

Gets or sets the advanced options for this contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Property Options As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
Dim value As System.Integer

instance.Options = value

value = instance.Options
```

### C#

```csharp
System.int Options {get; set;}
```

### C++/CLI

```cpp
property System.int Options {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Option for

- no penetration ([static](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStaticStudyOptions.html) and [nonlinear](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWNonLinearStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsNoPenetrationOption_e.html)
- thermal resistance ([thermal](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWThermalStudyOptions.html) studies only) advanced options as defined in [swsNoPenetrationOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsNoPenetrationOption_e.html) (except swsNoPenetrationOptionNodeToNode)
- shrink fit (static and nonlinear studies only) advanced options as defined in [swsShrinkFitOption_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsShrinkFitOption_e.html)

## VBA Syntax

See [CWContactSet::Options](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet~Options.html).

## See Also

[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
