---
title: "CutListFolderLocation Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "CutListFolderLocation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CutListFolderLocation.html"
---

# CutListFolderLocation Method (IFeatureManager)

Gets the parent folder of the specified solid body / cut list item / body folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function CutListFolderLocation( _
   ByVal QueryObj As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim QueryObj As System.Object
Dim value As System.Object

value = instance.CutListFolderLocation(QueryObj)
```

### C#

```csharp
System.object CutListFolderLocation(
   System.object QueryObj
)
```

### C++/CLI

```cpp
System.Object^ CutListFolderLocation(
   System.Object^ QueryObj
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `QueryObj`: Solid Body / cut list item / body folder / sub-weldment folder

[feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

### Return Value

Parent folder feature of QueryObj; null if QueryObj is not a Solid Body / cut list / body folder / sub-weldment folder

## VBA Syntax

See

[FeatureManager::CutListFolderLocation](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~CutListFolderLocation.html)

.

## Examples

See the

[IModelDocExtension::ReorderFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.html)

examples.

## Remarks

This method only works for:

- Solid Bodies / cut list items
- Feature / body folders
- Sub-weldment folders

Use[IFeatureManager::FeatureFolderLocation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureFolderLocation.html)to locate other FeatureManager design tree objects.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)

[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

[IModelDocExtension::ReorderFeature2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ReorderFeature2.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
