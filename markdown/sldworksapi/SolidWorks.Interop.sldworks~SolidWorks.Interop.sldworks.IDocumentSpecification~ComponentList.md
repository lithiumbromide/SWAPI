---
title: "ComponentList Property (IDocumentSpecification)"
project: "SOLIDWORKS API Help"
interface: "IDocumentSpecification"
member: "ComponentList"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ComponentList.html"
---

# ComponentList Property (IDocumentSpecification)

Gets or sets the selected components to load when opening an assembly document.

## Syntax

### Visual Basic (Declaration)

```vb
Property ComponentList As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDocumentSpecification
Dim value As System.Object

instance.ComponentList = value

value = instance.ComponentList
```

### C#

```csharp
System.object ComponentList {get; set;}
```

### C++/CLI

```cpp
property System.Object^ ComponentList {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Selected components to open when opening an assembly document (see Remarks)

## VBA Syntax

See [DocumentSpecification::ComponentList](ms-its:sldworksapivb6.chm::/sldworks~DocumentSpecification~ComponentList.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

## Remarks

Use [IDocumentSpecification::Selective](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDocumentSpecification~Selective.html) to specify to load only selected components when opening an assembly document.

## See Also

[IDocumentSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html)
[IDocumentSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification_members.html)
[IDocumentSpecification::InteractiveComponentSelection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~InteractiveComponentSelection.html)

## Availability

SolildWorks 2008 FCS, Revision Number 16.0
