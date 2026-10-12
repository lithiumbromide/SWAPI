---
title: "UseSoftSpring2 Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "UseSoftSpring2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~UseSoftSpring2.html"
---

# UseSoftSpring2 Property (ICWFrequencyStudyOptions)

Gets or sets whether to use soft springs to stabilize the model in this frequency study.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseSoftSpring2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
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

- -1 or true = Use soft springs
- 0 or false = Do not use soft springs

## VBA Syntax

See [CWFrequencyStudyOptions::UseSoftSpring2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~UseSoftSpring2.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

Rigid body modes are calculated in addition to the specified number of modes.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
