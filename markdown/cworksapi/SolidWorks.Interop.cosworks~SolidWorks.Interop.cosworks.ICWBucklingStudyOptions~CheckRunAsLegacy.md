---
title: "CheckRunAsLegacy Property (ICWBucklingStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBucklingStudyOptions"
member: "CheckRunAsLegacy"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckRunAsLegacy.html"
---

# CheckRunAsLegacy Property (ICWBucklingStudyOptions)

Obsolete. Superseded by [ICWBucklingStudyOptions::CheckRunAsLegacy2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckRunAsLegacy2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBucklingStudyOptions
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

See [CWBucklingStudyOptions::CheckRunAsLegacy](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBucklingStudyOptions~CheckRunAsLegacy.html).

## Remarks

This property is valid only if [ICWBucklingStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~CheckFlowPressure.html) is set to 1, and [ICWBucklingStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions~FlowPressureFile.html) is set to a SOLIDWORKS Flow Simulation results file.

## See Also

[ICWBucklingStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions.html)
[ICWBucklingStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBucklingStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
