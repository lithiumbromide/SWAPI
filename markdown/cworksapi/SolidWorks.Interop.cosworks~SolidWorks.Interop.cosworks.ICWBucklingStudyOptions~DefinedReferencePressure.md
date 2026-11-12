---
title: "DefinedReferencePressure Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "DefinedReferencePressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~DefinedReferencePressure.html"
---

# DefinedReferencePressure Property (ICWBucklingStudyOptions)

Gets or sets the reference pressure offset to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefinedReferencePressure As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::DefinedReferencePressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~DefinedReferencePressure.html).

## Examples

See the [ICWBucklingStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html) examples.

## Remarks

This property is valid only if [ICWBucklingStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure.html) is set to 1, and [ICWBucklingStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~ReferencePressureOption.html) is set to 0.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
