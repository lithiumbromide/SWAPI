---
title: "SetFavLibraryMaterialToSelectedEntities Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "SetFavLibraryMaterialToSelectedEntities"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToSelectedEntities.html"
---

# SetFavLibraryMaterialToSelectedEntities Method (ICWSolidManager)

Applies the specified favorite library material to selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavLibraryMaterialToSelectedEntities( _
   ByVal SFavLibName As System.String, _
   ByVal SFavMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim SFavLibName As System.String
Dim SFavMaterialName As System.String
Dim value As System.Integer

value = instance.SetFavLibraryMaterialToSelectedEntities(SFavLibName, SFavMaterialName)
```

### C#

```csharp
System.int SetFavLibraryMaterialToSelectedEntities(
   System.string SFavLibName,
   System.string SFavMaterialName
)
```

### C++/CLI

```cpp
System.int SetFavLibraryMaterialToSelectedEntities(
   System.String^ SFavLibName,
   System.String^ SFavMaterialName
)
```

### Parameters

- `SFavLibName`: Name of favorite material library
- `SFavMaterialName`: Name of material in SFavLibName

### Return Value

0 if material library and material name are set, 1 if not

## VBA Syntax

See [CWSolidManager::SetFavLibraryMaterialToSelectedEntities](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~SetFavLibraryMaterialToSelectedEntities.html).

## Remarks

Before calling this method, select one or more components to which to apply the specified favorite library material.

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)
[ICWSolidManager::SetLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToSelectedEntities.html)
[ICWSolidManager::SetFavLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToAllBodiesByCompName.html)
[ICWSolidManager::SetLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToAllBodiesByCompName.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
