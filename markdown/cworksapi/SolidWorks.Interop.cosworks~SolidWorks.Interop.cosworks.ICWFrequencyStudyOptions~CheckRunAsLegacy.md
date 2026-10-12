---
title: "CheckRunAsLegacy Property (ICWFrequencyStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWFrequencyStudyOptions"
member: "CheckRunAsLegacy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckRunAsLegacy.html"
---

# CheckRunAsLegacy Property (ICWFrequencyStudyOptions)

Obsolete. Superseded by [ICWFrequencyStudyOptions::CheckRunAsLegacy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckRunAsLegacy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWFrequencyStudyOptions
Dim value As System.Integer

instance.CheckRunAsLegacy = value

value = instance.CheckRunAsLegacy
```

### C#

```csharp
System.int CheckRunAsLegacy {get; set;}
```

### C++/CLI

```cpp
property System.int CheckRunAsLegacy {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

1 to run as legacy and import only the normal component of the pressure load, 0 to import all components including shear stress

## VBA Syntax

See [CWFrequencyStudyOptions::CheckRunAsLegacy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWFrequencyStudyOptions~CheckRunAsLegacy.html).

## Remarks

This property is valid only if:

- [ICWFrequencyStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWFrequencyStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions~FlowPressureFile.html) is set to a SOLIDWORKS Flow Simulation results file.

## See Also

[ICWFrequencyStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions.html)
[ICWFrequencyStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWFrequencyStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
