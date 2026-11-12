---
title: "Component Property (IMateInPlace)"
project: "SOLIDWORKS API Help"
interface: "IMateInPlace"
member: "Component"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace~Component.html"
---

# Component Property (IMateInPlace)

Gets the component for this Inplace mate.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Component As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IMateInPlace
Dim value As Component2

value = instance.Component
```

### C#

```csharp
Component2 Component {get;}
```

### C++/CLI

```cpp
property Component2^ Component {
   Component2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MateInPlace::Component](ms-its:sldworksapivb6.chm::/sldworks~MateInPlace~Component.html).

## Examples

[Get Component Names and Types for Inplace Mate (VBA)](Get_Component_Names_and_Types_for_Inplace_Mate_Example_VB.htm)

## Remarks

The component instance tree of a subassembly is not loaded because a subassembly does not have a view of its own. Thus, this property returns NULL if the Inplace mate is in a subassembly.

## See Also

[IMateInPlace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace.html)
[IMateInPlace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateInPlace_members.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
