---
title: "SetFavLibraryMaterialToAllBodiesByCompName Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "SetFavLibraryMaterialToAllBodiesByCompName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToAllBodiesByCompName.html"
---

# SetFavLibraryMaterialToAllBodiesByCompName Method (ICWSolidManager)

Applies the specified favorite library material to all bodies in the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFavLibraryMaterialToAllBodiesByCompName( _
   ByVal SCompName As System.String, _
   ByVal SFavLibName As System.String, _
   ByVal SFavMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim SCompName As System.String
Dim SFavLibName As System.String
Dim SFavMaterialName As System.String
Dim value As System.Integer

value = instance.SetFavLibraryMaterialToAllBodiesByCompName(SCompName, SFavLibName, SFavMaterialName)
```

### C#

```csharp
System.int SetFavLibraryMaterialToAllBodiesByCompName(
   System.string SCompName,
   System.string SFavLibName,
   System.string SFavMaterialName
)
```

### C++/CLI

```cpp
System.int SetFavLibraryMaterialToAllBodiesByCompName(
   System.String^ SCompName,
   System.String^ SFavLibName,
   System.String^ SFavMaterialName
)
```

### Parameters

- `SCompName`: Name of component
- `SFavLibName`: Name of favorite material library
- `SFavMaterialName`: Name of material in SFavLibName

### Return Value

0 if material library and material name are set, 1 if not

## VBA Syntax

See [CWSolidManager::SetFavLibraryMaterialToAllBodiesByCompName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~SetFavLibraryMaterialToAllBodiesByCompName.html).

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)
[ICWSolidManager::SetLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToAllBodiesByCompName.html)
[ICWSolidManager::SetFavLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToSelectedEntities.html)
[ICWSolidManager::SetLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToSelectedEntities.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
