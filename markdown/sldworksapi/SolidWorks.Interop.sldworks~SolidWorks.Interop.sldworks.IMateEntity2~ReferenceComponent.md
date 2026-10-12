---
title: "ReferenceComponent Property (IMateEntity2)"
project: "SOLIDWORKS API Help"
interface: "IMateEntity2"
member: "ReferenceComponent"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceComponent.html"
---

# ReferenceComponent Property (IMateEntity2)

Gets the reference component for this mate entity.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ReferenceComponent As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IMateEntity2
Dim value As Component2

value = instance.ReferenceComponent
```

### C#

```csharp
Component2 ReferenceComponent {get;}
```

### C++/CLI

```cpp
property Component2^ ReferenceComponent {
   Component2^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [MateEntity2::ReferenceComponent](ms-its:sldworksapivb6.chm::/sldworks~MateEntity2~ReferenceComponent.html).

## Examples

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)
[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)
[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)
[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## Remarks

The component instance tree of a subassembly is not loaded because a subassembly does not have a view of its own. Thus, this property returns Nothing or null if the Inplace mate is in a subassembly.

## See Also

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)
[IMateEntity2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2_members.html)
[IMateEntity2::Reference Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~Reference.html)
[IMateEntity2::ReferenceType2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2~ReferenceType2.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
