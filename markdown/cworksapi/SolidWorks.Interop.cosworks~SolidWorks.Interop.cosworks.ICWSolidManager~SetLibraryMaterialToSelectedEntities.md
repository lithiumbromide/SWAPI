---
title: "SetLibraryMaterialToSelectedEntities Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "SetLibraryMaterialToSelectedEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToSelectedEntities.html"
---

# SetLibraryMaterialToSelectedEntities Method (ICWSolidManager)

Applies the specified library material to selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterialToSelectedEntities( _
   ByVal SLibName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim SLibName As System.String
Dim SMaterialName As System.String
Dim value As System.Integer

value = instance.SetLibraryMaterialToSelectedEntities(SLibName, SMaterialName)
```

### C#

```csharp
System.int SetLibraryMaterialToSelectedEntities(
   System.string SLibName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.int SetLibraryMaterialToSelectedEntities(
   System.String^ SLibName,
   System.String^ SMaterialName
)
```

### Parameters

- `SLibName`: Name of material library
- `SMaterialName`: Name of material in SLibName

### Return Value

0 if material library and material name are set, 1 if not

## VBA Syntax

See [CWSolidManager::SetLibraryMaterialToSelectedEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~SetLibraryMaterialToSelectedEntities.html).

## Examples

[Apply Material to Selected Entities (VBA)](Apply_Material_to_Selected_Entities_Example_VB.htm)
[Apply Material to Selected Entities (VB.NET)](Apply_Material_to_Selected_Entities_Example_VBNET.htm)
[Apply Material to Selected Entities (C#)](Apply_Material_to_Selected_Entities_Example_CSharp.htm)

## Remarks

Before calling this method, select one or more components to which to apply the specified library material.

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)
[ICWSolidManager::SetFavLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToSelectedEntities.html)
[ICWSolidManager::SetFavLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToAllBodiesByCompName.html)
[ICWSolidManager::SetLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToAllBodiesByCompName.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
