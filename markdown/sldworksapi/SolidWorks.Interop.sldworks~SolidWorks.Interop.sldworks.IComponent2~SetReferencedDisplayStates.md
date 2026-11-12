---
title: "SetReferencedDisplayStates Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SetReferencedDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates.html"
---

# SetReferencedDisplayStates Method (IComponent2)

Sets the specified display state of this component to be referenced by the specified assembly display state(s).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetReferencedDisplayStates( _
   ByVal ComponentDisplayStateName As System.String, _
   ByVal Option As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim ComponentDisplayStateName As System.String
Dim Option As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Boolean

value = instance.SetReferencedDisplayStates(ComponentDisplayStateName, Option, AssemblyDisplayStateNames)
```

### C#

```csharp
System.bool SetReferencedDisplayStates(
   System.string ComponentDisplayStateName,
   System.int Option,
   System.object AssemblyDisplayStateNames
)
```

### C++/CLI

```cpp
System.bool SetReferencedDisplayStates(
   System.String^ ComponentDisplayStateName,
   System.int Option,
   System.Object^ AssemblyDisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ComponentDisplayStateName`: Component display state name
- `Option`: Display state option as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)
- `AssemblyDisplayStateNames`: Array of assembly display state names; valid only if Option is set to swDisplayStateOpts_e.swSpecifyDisplayState

### Return Value

True if component display state referenced successfully, false if not

## VBA Syntax

See [Component2::SetReferencedDisplayStates](ms-its:sldworksapivb6.chm::/sldworks~Component2~SetReferencedDisplayStates.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::GetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetReferencedDisplayStates.html)
[IComponent2::SetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetVisibilityInAsmDisplayStates.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
