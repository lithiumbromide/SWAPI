---
title: "FeatureManager Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "FeatureManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManager.html"
---

# FeatureManager Property (IModelDoc2)

Gets the [IFeatureManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager.html) object, which allows access to the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property FeatureManager As FeatureManager
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As FeatureManager

value = instance.FeatureManager
```

### C#

```csharp
FeatureManager FeatureManager {get;}
```

### C++/CLI

```cpp
property FeatureManager^ FeatureManager {
   FeatureManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IFeatureManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager.html) object

## VBA Syntax

See [ModelDoc2::FeatureManager](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~FeatureManager.html).

## Examples

[Insert Macro Feature (C++)](Insert_Macro_Feature_Example_CPlusPlus_COM.htm)
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)
[Insert Folder in FeatureManager Design Tree (VBA)](Insert_Folder_in_FeatureManager_Design_Tree_Example_VB.htm)
[Insert Reference POints (VBA)](Insert_Reference_Points_Example_VB.htm)
[Update FeatureManager Design Tree (VBA)](Update_FeatureManager_Design_Tree_Example_VB.htm)
[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
