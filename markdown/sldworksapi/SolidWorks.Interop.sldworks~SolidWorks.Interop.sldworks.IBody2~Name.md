---
title: "Name Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Name"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Name.html"
---

# Name Property (IBody2)

Gets or sets the name of the selected body.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of selected body

## VBA Syntax

See [Body2::Name](ms-its:sldworksapivb6.chm::/sldworks~Body2~Name.html).

## Examples

[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Get Bodies in Components (C#)](Get_Bodies_in_Components_Example_CSharp.htm)
[Get Bodies in Componets (VB.NET)](Get_Bodies_in_Components_Example_VBNET.htm)
[Get Bodies in Components (VBA)](Get_Bodies_in_Components_Example_VB.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

## Remarks

If changing the name of the body, then the name must be unique and cannot contain the at-sign character (@). Before changing the name of the body, call [IFeaturemanager::IsNameUsed](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~IsNameUsed.html) to find out if the name is unique and valid. To see the new name of the body in the FeatureManager design tree, call [IFeatureManager::UpdateFeatureTree](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~UpdateFeatureTree.html) to update it.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
