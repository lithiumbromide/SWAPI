---
title: "LargeDisplacement Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "LargeDisplacement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~LargeDisplacement.html"
---

# LargeDisplacement Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::LargeDisplacement2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~LargeDisplacement2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDisplacement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Integer

instance.LargeDisplacement = value

value = instance.LargeDisplacement
```

### C#

```csharp
System.int LargeDisplacement {get; set;}
```

### C++/CLI

```cpp
property System.int LargeDisplacement {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

- 1 = Use large displacement formulation
- 0 = Do not use large displacement formulation

## VBA Syntax

See [CWStaticStudyOptions::LargeDisplacement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~LargeDisplacement.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

The number of steps is internally decided by the software.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
