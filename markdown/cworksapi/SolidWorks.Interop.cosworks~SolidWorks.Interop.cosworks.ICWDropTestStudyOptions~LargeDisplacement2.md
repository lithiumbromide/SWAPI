---
title: "LargeDisplacement2 Property (ICWDropTestStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDropTestStudyOptions"
member: "LargeDisplacement2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions~LargeDisplacement2.html"
---

# LargeDisplacement2 Property (ICWDropTestStudyOptions)

Gets or sets whether to use a large displacement formulation to solve the problem.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDisplacement2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDropTestStudyOptions
Dim value As System.Boolean

instance.LargeDisplacement2 = value

value = instance.LargeDisplacement2
```

### C#

```csharp
System.bool LargeDisplacement2 {get; set;}
```

### C++/CLI

```cpp
property System.bool LargeDisplacement2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

0 or false to use a linear (small) displacement formulation, -1 or true to use a nonlinear (large) displacement formulation

## Examples

See the Examples in [ICWDropTestStudyOptions](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDropTestStudyOptions.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWDropTestStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions.html)
[ICWDropTestStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDropTestStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
