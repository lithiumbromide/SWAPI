---
title: "SetFavMaterial Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "SetFavMaterial"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetFavMaterial.html"
---

# SetFavMaterial Method (ICWShell)

Obsolete. Superseded by [ICWShell::SetFavMaterial2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetFavMaterial2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavMaterial( _
   ByVal NFav As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim NFav As System.Integer
Dim value As System.Integer

value = instance.SetFavMaterial(NFav)
```

### C#

```csharp
System.int SetFavMaterial(
   System.int NFav
)
```

### C++/CLI

```cpp
System.int SetFavMaterial(
   System.int NFav
)
```

### Parameters

- `NFav`: 1 <= index of material in favorites list <= 100 (see **Remarks**)

### Return Value

1 if material applied successfully, 0 if not

## VBA Syntax

See [CWShell::SetFavMaterial](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWShell~SetFavMaterial.html).

## Remarks

The list of material favorites appears when you right-click a component in the Simulation study tree and click **Apply Favorite Material**.

This method is not valid if [ICWShell::Formulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html) is set to [swsShellFormulation_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFormulation_e.html).swsShellFormulationComposite. To set the material of composite shell plies, you must:

1. Use [ICWShell::CompositeOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~CompositeOptions.html) to get an instance of [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html).
2. Call [ICWCompositeShellOptions::SetPlyParameters](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html) to set a ply's material.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)
[ICWShell::SetShellMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetShellMaterial.html)
[ICWShell::SetLibraryMaterial Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetLibraryMaterial.html)

## Availability

SOLIDWORKS Simulation API 2015 SP3
