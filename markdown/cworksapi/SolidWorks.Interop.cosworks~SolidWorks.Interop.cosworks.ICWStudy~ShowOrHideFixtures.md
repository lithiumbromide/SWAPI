---
title: "ShowOrHideFixtures Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "ShowOrHideFixtures"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ShowOrHideFixtures.html"
---

# ShowOrHideFixtures Property (ICWStudy)

Shows or hides fixture symbols in the graphics area.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ShowOrHideFixtures As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy

instance.ShowOrHideFixtures = value
```

### C#

```csharp
System.bool ShowOrHideFixtures {set;}
```

### C++/CLI

```cpp
property System.bool ShowOrHideFixtures {
   void set (    System.bool value);
}
```

### Property Value

True to show fixture symbols in the study, false to hide them

## VBA Syntax

See [CWStudy::ShowOrHideFixtures](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~ShowOrHideFixtures.html).

## Examples

[Analyze Part (C#)](Analyze_Part_Example_CSharp.htm)
[Analyze Part (VB.NET)](Analyze_Part_Example_VBNET.htm)
[Analyze Part (VBA)](Analyze_Part_Example_VB.htm)

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)
[ICWStudy::ShowOrHideForce Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~ShowOrHideForce.html)

## Availability

SOLIDWORKS Simulation API 2014 SP0
