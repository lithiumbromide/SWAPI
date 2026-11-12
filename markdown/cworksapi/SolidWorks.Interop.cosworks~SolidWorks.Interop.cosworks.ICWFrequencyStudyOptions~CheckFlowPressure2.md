---
title: "CheckFlowPressure2 Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "CheckFlowPressure2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure2.html"
---

# CheckFlowPressure2 Property (ICWFrequencyStudyOptions)

Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Boolean

instance.CheckFlowPressure2 = value

value = instance.CheckFlowPressure2
```

### C#

```csharp
System.bool CheckFlowPressure2 {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckFlowPressure2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to import fluid pressure loads, 0 or false to not

## Examples

See the [ICWFrequencyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html) examples.

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1, use [ICWFrequencyStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
