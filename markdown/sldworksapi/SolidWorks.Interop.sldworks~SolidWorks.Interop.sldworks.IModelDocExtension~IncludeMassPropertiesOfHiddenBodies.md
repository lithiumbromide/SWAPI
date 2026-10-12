---
title: "IncludeMassPropertiesOfHiddenBodies Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IncludeMassPropertiesOfHiddenBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IncludeMassPropertiesOfHiddenBodies.html"
---

# IncludeMassPropertiesOfHiddenBodies Property (IModelDocExtension)

Gets or sets whether to include the mass properties of hidden components in the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeMassPropertiesOfHiddenBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

instance.IncludeMassPropertiesOfHiddenBodies = value

value = instance.IncludeMassPropertiesOfHiddenBodies
```

### C#

```csharp
System.bool IncludeMassPropertiesOfHiddenBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeMassPropertiesOfHiddenBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include the mass properties of hidden components in the assembly, false to not

## VBA Syntax

See [ModelDocExtension::IncludeMassPropertiesOfHiddenBodies](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IncludeMassPropertiesOfHiddenBodies.html).

## Examples

[Get Mass Properties of Visible and Hidden Components (C#)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_CSharp.htm)
[Get Mass Properties of Visible and Hidden Components (VB.NET)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_VBNET.htm)
[Get Mass Properties of Visible and Hidden Components (VBA)](Get_Mass_Properties_of_Visible_and_Hidden_Components_Example_VB.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IAssemblyDoc::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HasUnloadedComponents.html)
[IAssemblyDoc::HideComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~HideComponent.html)
[IAssemblyDoc::ISetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ISetComponentVisibility.html)
[IAssemblyDoc::SetComponentVisibility Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetComponentVisibility.html)
[IComponent2::HasUnloadedComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~HasUnloadedComponents.html)
[IComponent2::IsHidden Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsHidden.html)
[IModelDoc2::HideComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2.html)
[IModelDocExtension::CreateMassProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateMassProperty.html)

## Availability

SOLIDWORKS 2009 SP03, Revision Number 17.3
