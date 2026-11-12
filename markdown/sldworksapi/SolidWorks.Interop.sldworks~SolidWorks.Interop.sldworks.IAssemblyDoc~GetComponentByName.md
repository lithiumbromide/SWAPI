---
title: "GetComponentByName Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "GetComponentByName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.html"
---

# GetComponentByName Method (IAssemblyDoc)

Gets the specified top-level assembly component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentByName( _
   ByVal CompName As System.String _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim value As Component2

value = instance.GetComponentByName(CompName)
```

### C#

```csharp
Component2 GetComponentByName(
   System.string CompName
)
```

### C++/CLI

```cpp
Component2^ GetComponentByName(
   System.String^ CompName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Name of the top-level assembly component to get

### Return Value

[Component](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::GetComponentByName](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~GetComponentByName.html).

## Examples

[Get Component by Name (C#)](Get_Component_by_Name_Example_CSharp.htm)
[Get Component by Name (VB.NET)](Get_Component_by_Name_Example_VBNET.htm)
[Get Component by Name (VBA)](Get_Component_by_Name_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::GetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponents.html)
[IAssemblyDoc::IGetComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IGetComponents.html)
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html)
[IComponent2::GetSelectByIDString Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSelectByIDString.html)
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.html)
[IAssemblyDoc::GetComponentByID Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByID.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
