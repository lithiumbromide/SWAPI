---
title: "GetDampingRatios Method (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "GetDampingRatios"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetDampingRatios.html"
---

# GetDampingRatios Method (ICWDampingOptions)

Gets the damping ratios.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDampingRatios() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim value As System.Object

value = instance.GetDampingRatios()
```

### C#

```csharp
System.object GetDampingRatios()
```

### C++/CLI

```cpp
System.Object^ GetDampingRatios();
```

### Return Value

Array of modes and damping ratios (see **Remarks**)

## VBA Syntax

See [CWDampingOptions::GetDampingRatios](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~GetDampingRatios.html).

## Remarks

This method works only if [ICWDampingOptions::DampingType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~DampingType.html) is set to [swsDampingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDampingType_e.html).swsDampingType_Modal and [ICWDampingOptions::ComputeFromMaterialDamping](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping.html) is set to 0 (off).

This method returns a one-dimensional array of one or more data sets, each containing:

- Index of first mode
- Index of last mode
- Damping ratio

For more information about modal damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::SetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetDampingRatios.html)
[ICWDampingOptions::ClearAllDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ClearAllDampingRatios.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
