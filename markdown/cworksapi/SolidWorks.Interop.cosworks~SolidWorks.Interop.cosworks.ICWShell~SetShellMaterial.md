---
title: "SetShellMaterial Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "SetShellMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetShellMaterial.html"
---

# SetShellMaterial Method (ICWShell)

Sets the material to apply to the shell for analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetShellMaterial( _
   ByVal MaterialDisp As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim MaterialDisp As System.Object
Dim value As System.Integer

value = instance.SetShellMaterial(MaterialDisp)
```

### C#

```csharp
System.int SetShellMaterial(
   System.object MaterialDisp
)
```

### C++/CLI

```cpp
System.int SetShellMaterial(
   System.Object^ MaterialDisp
)
```

### Parameters

- `MaterialDisp`: [Material](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWMaterial.html)

### Return Value

Error or warning as defined in [swsMaterialErrorWarning_e](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.swsMaterialErrorWarning_e.html)

## VBA Syntax

See [CWShell::SetShellMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~SetShellMaterial.html).

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::GetDefaultMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetDefaultMaterial.html)
[ICWShell::GetShellMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~GetShellMaterial.html)
[ICWShell::SetLibraryMaterial Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html)
[ICWShell::SetFavMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetFavMaterial.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
