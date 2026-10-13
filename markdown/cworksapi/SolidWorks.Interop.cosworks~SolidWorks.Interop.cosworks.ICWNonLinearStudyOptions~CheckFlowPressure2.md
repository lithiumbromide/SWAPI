---
title: "CheckFlowPressure2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckFlowPressure2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure2.html"
---

# CheckFlowPressure2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to import fluid pressure loads from a SOLIDWORKS Flow Simulation results file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

-1 or true to import fluid pressure loads, 0 or false to not (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::CheckFlowPressure2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckFlowPressure2.html).

## Remarks

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is set to -1 or true, use [ICWNonLinearStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
