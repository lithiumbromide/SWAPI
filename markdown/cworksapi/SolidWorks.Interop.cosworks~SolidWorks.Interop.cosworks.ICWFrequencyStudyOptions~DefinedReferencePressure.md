---
title: "DefinedReferencePressure Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "DefinedReferencePressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~DefinedReferencePressure.html"
---

# DefinedReferencePressure Property (ICWFrequencyStudyOptions)

Gets or sets the reference pressure offset to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefinedReferencePressure As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Double

instance.DefinedReferencePressure = value

value = instance.DefinedReferencePressure
```

### C#

```csharp
System.double DefinedReferencePressure {get; set;}
```

### C++/CLI

```cpp
property System.double DefinedReferencePressure {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Reference pressure offset to subtract from imported pressure values

## VBA Syntax

See [CWFrequencyStudyOptions::DefinedReferencePressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~DefinedReferencePressure.html).

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWFrequencyStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWFrequencyStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~ReferencePressureOption.html) is set to 0.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
