---
title: "GetSelectByIDString Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetSelectByIDString"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSelectByIDString.html"
---

# GetSelectByIDString Method (IComponent2)

Gets the name of the component for possible use with [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html), for selectively opening a document using [ISldWorks::OpenDoc7](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification.html), etc.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSelectByIDString() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.String

value = instance.GetSelectByIDString()
```

### C#

```csharp
System.string GetSelectByIDString()
```

### C++/CLI

```cpp
System.String^ GetSelectByIDString();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of component

## VBA Syntax

See [Component2::GetSelectByIDString](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetSelectByIDString.html).

## Examples

[Get Component Name from Selected Entity (VB.NET)](Get_Component_Name_From_Selected_Entity_Example_VBNET.htm)
[Get Component Name From Selected Entity (VBA)](Get_Component_Name_From_Selected_Entity_Example_VB.htm)
[Get Component Name from Selected Entity (C#)](Get_Component_Name_From_Selected_Entity_Example_CSharp.htm)

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)
[IAssemblyDoc::GetComponentByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetComponentByName.html)
[IComponent2::Name2 Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Name2.html)
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
