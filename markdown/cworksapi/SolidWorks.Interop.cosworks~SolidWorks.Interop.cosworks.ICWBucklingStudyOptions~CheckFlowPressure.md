---
title: "CheckFlowPressure Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "CheckFlowPressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure.html"
---

# CheckFlowPressure Property (ICWBucklingStudyOptions)

Obsolete. Superseded by [ICWBucklingStudyOptions::CheckFlowPressure2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::CheckFlowPressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~CheckFlowPressure.html).

## Remarks

If this property is set to 1, use [ICWBucklingStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
