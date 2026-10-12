---
title: "CheckRunAsLegacy Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "CheckRunAsLegacy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckRunAsLegacy.html"
---

# CheckRunAsLegacy Property (ICWStaticStudyOptions)

Obsolete. Superseded by [ICWStaticStudyOptions::CheckRunAsLegacy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckRunAsLegacy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
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

See [CWStaticStudyOptions::CheckRunAsLegacy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~CheckRunAsLegacy.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if:

- [ICWStaticStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWStaticStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~FlowPressureFile.html) is set to a SOLIDWORKS Flow Simulation results file.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
