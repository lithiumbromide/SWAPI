---
title: "SaveVirtualComponent Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "SaveVirtualComponent"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SaveVirtualComponent.html"
---

# SaveVirtualComponent Method (IComponent2)

Saves a virtual component to an external file.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveVirtualComponent( _
   ByVal CompPathName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim CompPathName As System.String
Dim value As System.Boolean

value = instance.SaveVirtualComponent(CompPathName)
```

### C#

```csharp
System.bool SaveVirtualComponent(
   System.string CompPathName
)
```

### C++/CLI

```cpp
System.bool SaveVirtualComponent(
   System.String^ CompPathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompPathName`: String containing full pathname of file to save component to

### Return Value

True if successful, false if not

## VBA Syntax

See [Component2::SaveVirtualComponent](ms-its:sldworksapivb6.chm::/sldworks~Component2~SaveVirtualComponent.html).

## Examples

[Insert New Virtual Component (C#)](Insert_New_Virtual_Component_Example_CSharp.htm)
[Insert New Virtual Component (VB.NET)](Insert_New_Virtual_Component_Example_VBNET.htm)
[Insert New Virtual Component (VBA)](Insert_New_Virtual_Component_Example_VB.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IComponent2::IsVirtual Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsVirtual.html)
[IModelDocExtension::IsVirtualComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsVirtualComponent3.html)
[IAssemblyDoc::InsertNewVirtualPart Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualPart.html)
[IAssemblyDoc::InsertNewAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewAssembly.html)
[IAssemblyDoc::InsertNewVirtualAssembly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertNewVirtualAssembly.html)
[IComponent2::MakeVirtual Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~MakeVirtual.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
