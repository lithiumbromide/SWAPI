---
title: "CheckRunAsLegacy Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckRunAsLegacy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckRunAsLegacy.html"
---

# CheckRunAsLegacy Property (ICWNonLinearStudyOptions)

Obsolete. Superseded by [ICWNonLinearStudyOptions::CheckRunAsLegacy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckRunAsLegacy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
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

See [CWNonLinearStudyOptions::CheckRunAsLegacy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckRunAsLegacy.html).

## Examples

See the [ICWNonLinearStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html) examples.

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWNonLinearStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowPressureFile.html) is set to a SOLIDWORKS Flow Simulation results file.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
