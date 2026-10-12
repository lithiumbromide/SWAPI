---
title: "UseSoftSpring2 Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "UseSoftSpring2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~UseSoftSpring2.html"
---

# UseSoftSpring2 Property (ICWBucklingStudyOptions)

Gets or sets whether to use soft spring to stabilize the model.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
Dim value As System.Boolean

instance.UseSoftSpring2 = value

value = instance.UseSoftSpring2
```

### C#

```csharp
System.bool UseSoftSpring2 {get; set;}
```

### C++/CLI

```cpp
property System.bool UseSoftSpring2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

- -1 or true = Use soft spring to stabilize the model
- 0 or false = Do not use soft spring to stabilize the model

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

Use this property carefully. If you set this property to -1 for checking purposes, then set more [buckling modes](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWBucklingStudyOptions~BucklingModes.html) and check them. Apply proper restraints for final results.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
