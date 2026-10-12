---
title: "DefinedReferencePressure Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "DefinedReferencePressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~DefinedReferencePressure.html"
---

# DefinedReferencePressure Property (ICWNonLinearStudyOptions)

Gets or sets the reference pressure offset to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefinedReferencePressure As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::DefinedReferencePressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~DefinedReferencePressure.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWNonLinearStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ReferencePressureOption.html) is set to 0.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
