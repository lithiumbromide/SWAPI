---
title: "DefinedReferencePressure Property (ICWStaticStudyOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStaticStudyOptions"
member: "DefinedReferencePressure"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~DefinedReferencePressure.html"
---

# DefinedReferencePressure Property (ICWStaticStudyOptions)

Gets or sets the reference pressure offset to subtract from imported pressure values.

## Syntax

### Visual Basic (Declaration)

```vb
Property DefinedReferencePressure As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStaticStudyOptions
Dim value As System.Double

instance.DefinedReferencePressure = value

value = instance.DefinedReferencePressure
```

### C#

```csharp
System.double DefinedReferencePressure {get; set;}
```

### C++/CLI

```cpp
property System.double DefinedReferencePressure {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Reference pressure offset to subtract from imported pressure values

## VBA Syntax

See [CWStaticStudyOptions::DefinedReferencePressure](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStaticStudyOptions~DefinedReferencePressure.html).

## Examples

See the [ICWBearingLoad](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBearingLoad.html) examples.

## Remarks

This property is valid only if:

- [ICWStaticStudyOptions::CheckFlowPressure](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~CheckFlowPressure.html) is set to 1.
- [ICWStaticStudyOptions::ReferencePressureOption](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions~ReferencePressureOption.html) is set to 0.

## See Also

[ICWStaticStudyOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions.html)
[ICWStaticStudyOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStaticStudyOptions_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
