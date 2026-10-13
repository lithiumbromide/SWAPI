---
title: "IsVirtualComponent3 Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IsVirtualComponent3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html"
---

# IsVirtualComponent3 Method (IModelDocExtension)

Gets the paths to parent assembly components, up to and including the first non-virtual parent, if the model is a virtual component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsVirtualComponent3( _
   ByRef PathChain As System.Object, _
   ByRef TitleChain As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim PathChain As System.Object
Dim TitleChain As System.Object
Dim value As System.Boolean

value = instance.IsVirtualComponent3(PathChain, TitleChain)
```

### C#

```csharp
System.bool IsVirtualComponent3(
   out System.object PathChain,
   out System.object TitleChain
)
```

### C++/CLI

```cpp
System.bool IsVirtualComponent3(
   [Out] System.Object^ PathChain,
   [Out] System.Object^ TitleChain
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PathChain`: Array of fully qualified paths to parent assembly components, up to and including the first non-virtual parent assembly component, if the model is a virtual component
- `TitleChain`: Array of document titles; each document title corresponds to a fully qualified path in PathChain

### Return Value

True if the component is virtual, false if not

## VBA Syntax

See [ModelDocExtension::IsVirtualComponent3](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IsVirtualComponent3.html).

## Examples

[Get Paths and Titles of Parent of Virtual Component (C#)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_CSharp.htm)
[Get Paths and Titles of Parent of Virutal Component (VB.NET)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VBNET.htm)
[Get Paths and Titles of Parent of Virtual Component (VBA)](Get_Paths_and_Titles_of_Parents_of_Virtual_Component_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html)
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html)

## Availability

SOLIDWORKS 2008 SP4, Revision Number 16.4
