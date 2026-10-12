---
title: "MoveToFolder Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "MoveToFolder"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~MoveToFolder.html"
---

# MoveToFolder Method (IFeatureManager)

Moves the selected feature or folder in the Solid Bodies Feature Manager design tree structure to the specified folder in the Solid Bodies Feature Manager design tree structure.

## Syntax

### Visual Basic (Declaration)

```vb
Function MoveToFolder( _
   ByVal MoveToFeat As System.String, _
   ByVal MoveFromFeat As System.String, _
   ByVal IsFolder As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim MoveToFeat As System.String
Dim MoveFromFeat As System.String
Dim IsFolder As System.Boolean
Dim value As System.Boolean

value = instance.MoveToFolder(MoveToFeat, MoveFromFeat, IsFolder)
```

### C#

```csharp
System.bool MoveToFolder(
   System.string MoveToFeat,
   System.string MoveFromFeat,
   System.bool IsFolder
)
```

### C++/CLI

```cpp
System.bool MoveToFolder(
   System.String^ MoveToFeat,
   System.String^ MoveFromFeat,
   System.bool IsFolder
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MoveToFeat`: Folder to which to move feature
- `MoveFromFeat`: Folder from which to move feature
- `IsFolder`: True if feature is a folder, false if a feature

### Return Value

True if feature is moved, false if not

## VBA Syntax

See [FeatureManager::MoveToFolder](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~MoveToFolder.html).

## Remarks

This method is specific to the Solid Bodies folder only; it does not work for components.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
