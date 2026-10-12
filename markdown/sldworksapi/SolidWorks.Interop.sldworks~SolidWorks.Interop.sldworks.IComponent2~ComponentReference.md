---
title: "ComponentReference Property (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "ComponentReference"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~ComponentReference.html"
---

# ComponentReference Property (IComponent2)

Gets or sets a component reference for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentReference As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

instance.ComponentReference = value

value = instance.ComponentReference
```

### C#

```csharp
System.string ComponentReference {get; set;}
```

### C++/CLI

```cpp
property System.String^ ComponentReference {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Component reference string

## VBA Syntax

See [Component2::ComponentReference](ms-its:sldworksapivb6.chm::/sldworks~Component2~ComponentReference.html).

## Examples

[Get Component Name from Selected Entity (VB.NET)](Get_Component_Name_From_Selected_Entity_Example_VBNET.htm)
[Get Component Name from Selected Entity (VBA)](Get_Component_Name_From_Selected_Entity_Example_VB.htm)
[Get Component Name from Selected Entity (C#)](Get_Component_Name_From_Selected_Entity_Example_CSharp.htm)

## Remarks

Call [IModelDoc2::ForceRebuild3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ForceRebuild3.html) after setting a component reference.

To remove a component reference, set the component reference string to "".

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
