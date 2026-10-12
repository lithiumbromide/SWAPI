---
title: "LargeDisplacement2 Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "LargeDisplacement2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~LargeDisplacement2.html"
---

# LargeDisplacement2 Property (ICWStaticStudyOptions)

Gets or sets whether loads are applied gradually and uniformly in steps up to their full values, performing contact iterations at every step.

## Syntax

### Visual Basic (Declaration)

```vb
Property LargeDisplacement2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

- -1 or true = Use large displacement formulation
- 0 or false = Do not use large displacement formulation

(see **Remarks**)

## VBA Syntax

See [CWStaticStudyOptions::LargeDisplacement2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~LargeDisplacement2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
