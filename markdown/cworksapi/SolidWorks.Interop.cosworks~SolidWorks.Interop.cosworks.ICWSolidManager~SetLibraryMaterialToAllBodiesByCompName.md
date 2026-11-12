---
title: "SetLibraryMaterialToAllBodiesByCompName Method (ICWSolidManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidManager"
member: "SetLibraryMaterialToAllBodiesByCompName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToAllBodiesByCompName.html"
---

# SetLibraryMaterialToAllBodiesByCompName Method (ICWSolidManager)

Applies the specified library material to all bodies in the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetLibraryMaterialToAllBodiesByCompName( _
   ByVal SCompName As System.String, _
   ByVal SLibName As System.String, _
   ByVal SMaterialName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidManager
Dim SCompName As System.String
Dim SLibName As System.String
Dim SMaterialName As System.String
Dim value As System.Integer

value = instance.SetLibraryMaterialToAllBodiesByCompName(SCompName, SLibName, SMaterialName)
```

### C#

```csharp
System.int SetLibraryMaterialToAllBodiesByCompName(
   System.string SCompName,
   System.string SLibName,
   System.string SMaterialName
)
```

### C++/CLI

```cpp
System.int SetLibraryMaterialToAllBodiesByCompName(
   System.String^ SCompName,
   System.String^ SLibName,
   System.String^ SMaterialName
)
```

### Parameters

- `SCompName`: Name of component
- `SLibName`: Name of material library
- `SMaterialName`: Name of material in SLibName

### Return Value

0 if material library and material name are set, 1 if not

## VBA Syntax

See [CWSolidManager::SetLibraryMaterialToAllBodiesByCompName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidManager~SetLibraryMaterialToAllBodiesByCompName.html).

## See Also

[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
[ICWSolidManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager_members.html)
[ICWSolidManager::SetFavLibraryMaterialToAllBodiesByCompName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToAllBodiesByCompName.html)
[ICWSolidManager::SetFavLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetFavLibraryMaterialToSelectedEntities.html)
[ICWSolidManager::SetLibraryMaterialToSelectedEntities Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~SetLibraryMaterialToSelectedEntities.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
