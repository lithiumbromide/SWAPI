---
title: "SetFavMaterial2 Method (ICWShell)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWShell"
member: "SetFavMaterial2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~SetFavMaterial2.html"
---

# SetFavMaterial2 Method (ICWShell)

Applies the specified material from the material favorites list.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavMaterial2( _
   ByVal NFav As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWShell
Dim NFav As System.Integer
Dim value As System.Boolean

value = instance.SetFavMaterial2(NFav)
```

### C#

```csharp
System.bool SetFavMaterial2(
   System.int NFav
)
```

### C++/CLI

```cpp
System.bool SetFavMaterial2(
   System.int NFav
)
```

### Parameters

- `NFav`: 1 <= index of material in favorites list <= 100 (see **Remarks**)

### Return Value

-1 or true if material applied successfully, 0 or false if not

## Remarks

The list of material favorites appears when you right-click a component in the Simulation study tree and click **Apply Favorite Material**.

This method is not valid if [ICWShell::Formulation](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~Formulation.html) is set to [swsShellFormulation_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsShellFormulation_e.html).swsShellFormulationComposite. To set the material of composite shell plies, you must:

1. Use [ICWShell::CompositeOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell~CompositeOptions.html) to get an instance of [ICWCompositeShellOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions.html).
2. Call [ICWCompositeShellOptions::SetPlyParameters](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWCompositeShellOptions~SetPlyParameters.html) to set a ply's material.

## See Also

[ICWShell Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell.html)
[ICWShell Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWShell_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
