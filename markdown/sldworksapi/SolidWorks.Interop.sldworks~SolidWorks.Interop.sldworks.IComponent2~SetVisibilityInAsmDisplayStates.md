---
title: "SetVisibilityInAsmDisplayStates Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetVisibilityInAsmDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibilityInAsmDisplayStates.html"
---

# SetVisibilityInAsmDisplayStates Method (IComponent2)

Sets the visibility of this component in the specified assembly display state(s).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetVisibilityInAsmDisplayStates( _
   ByVal HideComponent As System.Integer, _
   ByVal Option As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim HideComponent As System.Integer
Dim Option As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Boolean

value = instance.SetVisibilityInAsmDisplayStates(HideComponent, Option, AssemblyDisplayStateNames)
```

### C#

```csharp
System.bool SetVisibilityInAsmDisplayStates(
   System.int HideComponent,
   System.int Option,
   System.object AssemblyDisplayStateNames
)
```

### C++/CLI

```cpp
System.bool SetVisibilityInAsmDisplayStates(
   System.int HideComponent,
   System.int Option,
   System.Object^ AssemblyDisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `HideComponent`: Visibility as defined in [swComponentVisibilityState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentVisibilityState_e.html)
- `Option`: Display state option as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)
- `AssemblyDisplayStateNames`: Array of assembly display state names; valid only if Option is set to swDisplayStateOpts_e.swSpecifyDisplayState

### Return Value

True if visibility successfully set, false if not

## VBA Syntax

See [Component2::SetVisibilityInAsmDisplayStates](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetVisibilityInAsmDisplayStates.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::SetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates.html)
[IComponent2::GetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibilityInAsmDisplayStates.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
