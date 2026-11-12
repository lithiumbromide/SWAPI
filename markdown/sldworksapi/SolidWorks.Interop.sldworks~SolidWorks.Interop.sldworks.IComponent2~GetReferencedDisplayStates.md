---
title: "GetReferencedDisplayStates Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetReferencedDisplayStates"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetReferencedDisplayStates.html"
---

# GetReferencedDisplayStates Method (IComponent2)

Gets the display states of this component that are referenced by the specified assembly display state(s).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencedDisplayStates( _
   ByVal AssemblyDisplayStateOption As System.Integer, _
   ByVal AssemblyDisplayStateNames As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim AssemblyDisplayStateOption As System.Integer
Dim AssemblyDisplayStateNames As System.Object
Dim value As System.Object

value = instance.GetReferencedDisplayStates(AssemblyDisplayStateOption, AssemblyDisplayStateNames)
```

### C#

```csharp
System.object GetReferencedDisplayStates(
   System.int AssemblyDisplayStateOption,
   System.object AssemblyDisplayStateNames
)
```

### C++/CLI

```cpp
System.Object^ GetReferencedDisplayStates(
   System.int AssemblyDisplayStateOption,
   System.Object^ AssemblyDisplayStateNames
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AssemblyDisplayStateOption`: Display state option as defined in [swDisplayStateOpts_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayStateOpts_e.html)
- `AssemblyDisplayStateNames`: Array of assembly display state names; valid only if AssemblyDisplayStateOption is set to swDisplayStateOpts_e.swSpecifyDisplayState

### Return Value

Array of referenced display state names

## VBA Syntax

See [Component2::GetReferencedDisplayStates](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetReferencedDisplayStates.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::SetReferencedDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetReferencedDisplayStates.html)
[IComponent2::GetVisibilityInAsmDisplayStates Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetVisibilityInAsmDisplayStates.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
