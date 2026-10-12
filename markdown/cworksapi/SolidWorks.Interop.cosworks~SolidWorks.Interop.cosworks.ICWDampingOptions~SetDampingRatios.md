---
title: "SetDampingRatios Method (ICWDampingOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDampingOptions"
member: "SetDampingRatios"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~SetDampingRatios.html"
---

# SetDampingRatios Method (ICWDampingOptions)

Sets the damping ratios.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetDampingRatios( _
   ByVal NRows As System.Integer, _
   ByVal Values As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDampingOptions
Dim NRows As System.Integer
Dim Values As System.Object
Dim value As System.Integer

value = instance.SetDampingRatios(NRows, Values)
```

### C#

```csharp
System.int SetDampingRatios(
   System.int NRows,
   System.object Values
)
```

### C++/CLI

```cpp
System.int SetDampingRatios(
   System.int NRows,
   System.Object^ Values
)
```

### Parameters

- `NRows`: Number of rows in Values
- `Values`: Array of modes and damping ratios (see **Remarks**)

### Return Value

Error code as defined in [swsSetDampingRatiosError_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsSetDampingRatiosError_e.html)

## VBA Syntax

See [CWDampingOptions::SetDampingRatios](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDampingOptions~SetDampingRatios.html).

## Examples

See the [ICWDampingOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html) examples.

## Remarks

This method works only if [ICWDampingOptions::DampingType](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~DampingType.html) is set to [swsDampingType_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsDampingType_e.html).swsDampingType_Modal and [ICWDampingOptions::ComputeFromMaterialDamping](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDampingOptions~ComputeFromMaterialDamping.html) is set to 0 (off).

The Values parameter takes a one-dimensional array of one or more data sets, each containing:

- Index of first mode
- Index of last mode
- Damping ratio

For more information about modal damping, see the SOLIDWORKS Simulation Help.

## See Also

[ICWDampingOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions.html)
[ICWDampingOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions_members.html)
[ICWDampingOptions::GetDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~GetDampingRatios.html)
[ICWDampingOptions::ClearAllDampingRatios Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDampingOptions~ClearAllDampingRatios.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
