---
title: "CheckFlowPressure Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckFlowPressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure.html"
---

# CheckFlowPressure Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::CheckFlowPressure2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Integer

instance.CheckFlowPressure = value

value = instance.CheckFlowPressure
```

### C#

```csharp
System.int CheckFlowPressure {get; set;}
```

### C++/CLI

```cpp
property System.int CheckFlowPressure {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to import fluid pressure loads, 0 to not

## VBA Syntax

See [CWNonLinearStudyOptions::CheckFlowPressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckFlowPressure.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

If this property is set to 1, use [ICWNonLinearStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)
[ICWNonLinearStudyOptions::DefinedReferencePressure Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~DefinedReferencePressure.html)
[ICWNonLinearStudyOptions::ReferencePressureOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~ReferencePressureOption.html)
[ICWNonLinearStudyOptions::CheckRunAsLegacy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckRunAsLegacy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
