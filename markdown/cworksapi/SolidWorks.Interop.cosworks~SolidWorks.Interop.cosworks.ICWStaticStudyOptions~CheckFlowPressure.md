---
title: "CheckFlowPressure Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "CheckFlowPressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure.html"
---

# CheckFlowPressure Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::CheckFlowPressure2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckFlowPressure As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::CheckFlowPressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~CheckFlowPressure.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

If this property is set to 1, use [ICWStaticStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FlowPressureFile.html) to set the SOLIDWORKS Flow Simulation results file.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)
[ICWStaticStudyOptions::DefinedReferencePressure Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~DefinedReferencePressure.html)
[ICWStaticStudyOptions::ReferencePressureOption Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ReferencePressureOption.html)
[ICWStaticStudyOptions::CheckRunAsLegacy Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckRunAsLegacy.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
