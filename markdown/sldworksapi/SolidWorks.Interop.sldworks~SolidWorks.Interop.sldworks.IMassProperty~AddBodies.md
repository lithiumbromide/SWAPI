---
title: "AddBodies Method (IMassProperty)"
project: "SOLIDWORKS API Help"
interface: "IMassProperty"
member: "AddBodies"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~AddBodies.html"
---

# AddBodies Method (IMassProperty)

Uses only the specified bodies when calculating the mass properties for this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddBodies( _
   ByVal BodyListIn As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IMassProperty
Dim BodyListIn As System.Object
Dim value As System.Boolean

value = instance.AddBodies(BodyListIn)
```

### C#

```csharp
System.bool AddBodies(
   System.object BodyListIn
)
```

### C++/CLI

```cpp
System.bool AddBodies(
   System.Object^ BodyListIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BodyListIn`: Array of [bodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in the model

### Return Value

True if the specified bodies are used for calculating mass properties, false if not

## VBA Syntax

See [MassProperty::AddBodies](ms-its:sldworksapivb6.chm::/sldworks~MassProperty~AddBodies.html).

## Examples

[Get Mass Properties of Multibody Assembly Component (C#)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_CSharp.htm)
[Get Mass Properties of Multibody Assembly Component (VB.NET)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VBNET.htm)
[Get Mass Properties of Multibody Assembly Component (VBA)](Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm)

## Remarks

This method lets you select which solid bodies to use when calculating mass properties, much like a end-user selecting the bodies via the user interface.

NOTE: If a sheet (surface) body is specified, it is ignored and false is returned.

The results of the mass property calculations vary based on whether or not this method is used.

| If this method is... | Then... |
| --- | --- |
| Called and bodies are specified | These bodies can either be from a subset of the documents body list or from temporary bodies. NOTE: Each specified body should either come from the owning document or be a temporary body. If the body does not satisfy either case, then it is not used when calculating the mass properties. |
| Not called | Mass properties' calculations include all available bodies in the document. Part . All of the solid bodies are included in the calculations. Assembly . All of the bodies in all of the components are used in the calculations. |

If the document from which the MassProperty object came is an assembly, then any body from any of the child components can be used. To obtain the body, call [IComponent2::GetBodies2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~GetBodies2.html). Your application does not need to make a copy of the body or apply a transform to the body.

## See Also

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.html)
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.html)
[IMassProperty::IAddBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~IAddBodies.html)

## Availability

SOLIDWORKS 2003 SP2, Revision Number 11.2
