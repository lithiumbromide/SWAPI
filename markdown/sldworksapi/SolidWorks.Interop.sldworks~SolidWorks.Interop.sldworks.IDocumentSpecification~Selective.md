---
title: "Selective Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "Selective"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~Selective.html"
---

# Selective Property (IDocumentSpecification)

Gets or sets whether to open a document in Quick view (parts and drawings) or Quick view / Selective (assemblies) mode.

## Syntax

### Visual Basic (Declaration)

```vb
Property Selective As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Boolean

instance.Selective = value

value = instance.Selective
```

### C#

```csharp
System.bool Selective {get; set;}
```

### C++/CLI

```cpp
property System.bool Selective {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to open the document in Quick view / Selective open mode, false to not

## VBA Syntax

See [DocumentSpecification::Selective](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~Selective.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

Use [IDocumentSpecification::ComponentList](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~ComponentList.html) to specify the selected components to load when opening the assembly document.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IAssemblyDoc::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~GetUnloadedComponentNames.html)
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html)
[IComponent2::GetHiddenUnloadedChildrenCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetHiddenUnloadedChildrenCount.html)
[IComponent2::GetUnloadedComponentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetUnloadedComponentNames.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)
[IDocumentSpecification::InteractiveComponentSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
