---
title: "CheckRunAsLegacy2 Property (ICWNonLinearStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWNonLinearStudyOptions"
member: "CheckRunAsLegacy2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckRunAsLegacy2.html"
---

# CheckRunAsLegacy2 Property (ICWNonLinearStudyOptions)

Gets or sets whether to run as legacy and import only the normal component of the pressure load from a SOLIDWORKS Flow Simulation results file.

## Syntax

### Visual Basic (Declaration)

```vb
Property CheckRunAsLegacy2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWNonLinearStudyOptions
Dim value As System.Boolean

instance.CheckRunAsLegacy2 = value

value = instance.CheckRunAsLegacy2
```

### C#

```csharp
System.bool CheckRunAsLegacy2 {get; set;}
```

### C++/CLI

```cpp
property System.bool CheckRunAsLegacy2 {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

-1 or true to run as legacy and import only the normal component of the pressure load, 0 or false to import all components including shear stress (see **Remarks**)

## VBA Syntax

See [CWNonLinearStudyOptions::CheckRunAsLegacy2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWNonLinearStudyOptions~CheckRunAsLegacy2.html).

## Remarks

This property is valid only if:

- [ICWNonLinearStudyOptions::CheckFlowPressure2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~CheckFlowPressure2.html) is set to -1.
- [ICWNonLinearStudyOptions::FlowPressureFile](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions~FlowPressureFile.html) is set to a SOLIDWORKS Flow Simulation results file.

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

## See Also

[ICWNonLinearStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions.html)
[ICWNonLinearStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWNonLinearStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2021 SP04
