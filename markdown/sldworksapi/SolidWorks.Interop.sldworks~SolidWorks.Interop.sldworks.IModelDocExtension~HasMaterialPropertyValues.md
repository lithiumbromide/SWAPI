---
title: "HasMaterialPropertyValues Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HasMaterialPropertyValues"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasMaterialPropertyValues.html"
---

# HasMaterialPropertyValues Method (IModelDocExtension)

Gets whether this model has an appearance.

## Syntax

### Visual Basic (Declaration)

```vb
Function HasMaterialPropertyValues() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.HasMaterialPropertyValues()
```

### C#

```csharp
System.bool HasMaterialPropertyValues()
```

### C++/CLI

```cpp
System.bool HasMaterialPropertyValues();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this model has an appearance, false if not

## VBA Syntax

See [ModelDocExtension::HasMaterialPropertyValues](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~HasMaterialPropertyValues.html).

## Examples

[Add and Delete Appearances from Specific Display States (VBA)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VB.htm)
[Add and Delete Appearances from Specific Display States (VB.NET)](Add_and_Delete_Materials_from_Specific_Display_States_Example_VBNET.htm)
[Add and Delete Appearances from Specific Display States (C#)](Add_and_Delete_Materials_from_Specific_Display_States_Example_CSharp.htm)

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::SetMaterialPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetMaterialPropertyValues.html)
[IModelDocExtension::RemoveMaterialProperty Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveMaterialProperty.html)
[IModelDocExtension::GetMaterialPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
