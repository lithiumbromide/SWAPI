---
title: "Component Property (IMateLoadReference)"
project: "SOLIDWORKS API Help"
interface: "IMateLoadReference"
member: "Component"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~Component.html"
---

# Component Property (IMateLoadReference)

Gets the specified component associated with the mate that owns this load reference.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Component( _
   ByVal WhichOne As System.Integer _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As Component2

value = instance.Component(WhichOne)
```

### C#

```csharp
Component2 Component(
   System.int WhichOne
) {get;}
```

### C++/CLI

```cpp
property Component2^ Component {
   Component2^ get(System.int WhichOne);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: - 0 = Component1

  - 1 = Component2

### Property Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html) associated with the mate that owns this load reference

## VBA Syntax

See [MateLoadReference::Component](ms-its:sldworksapivb6.chm::/sldworks~MateLoadReference~Component.html).

## Examples

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

## See Also

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
