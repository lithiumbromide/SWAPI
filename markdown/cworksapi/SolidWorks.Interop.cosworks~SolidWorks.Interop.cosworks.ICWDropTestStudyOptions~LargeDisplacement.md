---
title: "LargeDisplacement Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "LargeDisplacement"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~LargeDisplacement.html"
---

# LargeDisplacement Property (ICWDropTestStudyOptions)

Obsolete. Superseded by [ICWDropTestStudyOptions::LargeDisplacement2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~LargeDisplacement2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDisplacement As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
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

0 to use a linear (small) displacement formulation, 1 to use a nonlinear (large) displacement formulation

## VBA Syntax

See [CWDropTestStudyOptions::LargeDisplacement](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDropTestStudyOptions~LargeDisplacement.html).

## Examples

See the Examples in [ICWDropTestStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestStudyOptions.html).

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
