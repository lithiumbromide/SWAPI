---
title: "CriticalDampingRatio Property (ICWDropTestSetup)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestSetup"
member: "CriticalDampingRatio"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup~CriticalDampingRatio.html"
---

# CriticalDampingRatio Property (ICWDropTestSetup)

Gets or sets the critical damping ratio for the drop test study.

## Syntax

### Visual Basic (Declaration)

```vb
Property CriticalDampingRatio As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestSetup
Dim value As System.Double

instance.CriticalDampingRatio = value

value = instance.CriticalDampingRatio
```

### C#

```csharp
System.double CriticalDampingRatio {get; set;}
```

### C++/CLI

```cpp
property System.double CriticalDampingRatio {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

0.0 <= Critical damping ratio <= 1.0

## VBA Syntax

See [CWDropTestSetup::CriticalDampingRatio](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestSetup~CriticalDampingRatiohtml).

## Examples

See the [ICWDropTestSetup](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestSetup.html) examples.

## Remarks

See the Drop Test Setup PropertyManager topic in the SOLIDWORKS Simulation Help for more information about contact damping in drop test studies.

## See Also

[ICWDropTestSetup Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup.html)
[ICWDropTestSetup Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestSetup_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
