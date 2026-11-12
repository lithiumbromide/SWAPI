---
title: "ShowOrHideForce Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ShowOrHideForce"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ShowOrHideForce.html"
---

# ShowOrHideForce Property (ICWStudy)

Shows or hides the force symbols in the graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ShowOrHideForce As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy

instance.ShowOrHideForce = value
```

### C#

```csharp
System.bool ShowOrHideForce {set;}
```

### C++/CLI

```cpp
property System.bool ShowOrHideForce {
   void set (    System.bool value);
}
```

### Property Value

True to show force symbols in the study, false to hide them

## VBA Syntax

See [CWStudy::ShowOrHideForces](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ShowOrHideForce.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ShowOrHideFixtures Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ShowOrHideFixtures.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
