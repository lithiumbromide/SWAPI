---
title: "DeleteSnapShot Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "DeleteSnapShot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.html"
---

# DeleteSnapShot Method (IModelViewManager)

Deletes the specified snapshot from an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteSnapShot( _
   ByVal SnapShotName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim SnapShotName As System.String
Dim value As System.Boolean

value = instance.DeleteSnapShot(SnapShotName)
```

### C#

```csharp
System.bool DeleteSnapShot(
   System.string SnapShotName
)
```

### C++/CLI

```cpp
System.bool DeleteSnapShot(
   System.String^ SnapShotName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SnapShotName`: Name of snapshot to delete

### Return Value

True if successful, false if not

## VBA Syntax

See [ModelViewManager::DeleteSnapShot](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~DeleteSnapShot.html).

## Remarks

This method is valid only for assemblies.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::AddSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.html)
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.html)
[IModelViewManager::GetSnapShots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
