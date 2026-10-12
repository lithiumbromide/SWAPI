---
title: "SetTotalPlies Method (ICWCompositeShellOptions)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWCompositeShellOptions"
member: "SetTotalPlies"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetTotalPlies.html"
---

# SetTotalPlies Method (ICWCompositeShellOptions)

Sets the total number of plies in the composite laminate.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetTotalPlies( _
   ByVal NTotalPlies As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWCompositeShellOptions
Dim NTotalPlies As System.Integer
Dim value As System.Integer

value = instance.SetTotalPlies(NTotalPlies)
```

### C#

```csharp
System.int SetTotalPlies(
   System.int NTotalPlies
)
```

### C++/CLI

```cpp
System.int SetTotalPlies(
   System.int NTotalPlies
)
```

### Parameters

- `NTotalPlies`: Total number of plies

### Return Value

Error code as defined in [swsCompositeShellOptionsError_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsCompositeShellOptionsError_e.html)

## VBA Syntax

See [CWCompositeShellOptions::SetTotalPlies](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWCompositeShellOptions~SetTotalPlies.html).

## Remarks

This method is valid only if [ICWCompositeShellOptions::Sandwich](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~Sandwich.html) is set to 0.

## See Also

[ICWCompositeShellOptions Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html)
[ICWCompositeShellOptions Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions_members.html)
[ICWCompositeShellOptions::GetTotalPlies Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~GetTotalPlies.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
