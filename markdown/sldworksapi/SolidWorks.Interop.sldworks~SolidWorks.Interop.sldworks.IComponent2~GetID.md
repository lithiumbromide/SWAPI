---
title: "GetID Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetID.html"
---

# GetID Method (IComponent2)

Gets the component ID for this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetID()
```

### C#

```csharp
System.int GetID()
```

### C++/CLI

```cpp
System.int GetID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ID for this component

## VBA Syntax

See [Component2::GetID](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetID.html).

## Examples

[Get Component State (C#)](Get_Component_State_Example_CSharp.htm)
[Get Component State (VB.NET)](Get_Component_State_Example_VBNET.htm)
[Get Component State (VBA)](Get_Component_State_Example_VB.htm)
[Get Component IDs (C#)](Get_Component_IDs_Example_CSharp.htm)
[Get Component IDs (VB.NET)](Get_Component_IDs_Example_VBNET.htm)
[Get Component IDs (VBA)](Get_Component_IDs_Example_VB.htm)
[Get Top-level Components Using Component IDs (C#)](Get_Top-level_Component_Using_Component_IDs_Example_CSharp.htm)
[Get Top-level Components Using Component IDs (VB.NET)](Get_Top-level_Component_Using_Component_IDs_Example_VBNET.htm)
[Get Top-level Components Using Component IDs (VBA)](Get_Top-level_Component_Using_Component_IDs_Example_VB.htm)

## Remarks

A component ID:

- is unique within the context of the assembly to which it belongs.
  **NOTE:** A component ID might not be unique across subassemblies within the assembly. For example, a component in subassembly A might have a component ID of 1, and a component in subassembly B might also have a component ID of 1.
- is persistent across SOLIDWORKS Design sessions and never changes, even if you [change the name of the component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.html).
- can be used to identify a specific component in an assembly. Use the component ID returned by this method with [IAssemblyDoc::GetComponentByID](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html) to get a top-level assembly component.
- cannot be assigned by applications or users.
- is not the same as a [persistent reference ID](sldworksapiprogguide.chm::/overview/Persistent_Reference_IDs.htm). You can get any component using its persistent reference ID.

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
