---
title: "GetSnapShot Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetSnapShot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.html"
---

# GetSnapShot Method (IModelViewManager)

Gets the specified snapshot of an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSnapShot( _
   ByVal SnapShotName As System.String _
) As SnapShot
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim SnapShotName As System.String
Dim value As SnapShot

value = instance.GetSnapShot(SnapShotName)
```

### C#

```csharp
SnapShot GetSnapShot(
   System.string SnapShotName
)
```

### C++/CLI

```cpp
SnapShot^ GetSnapShot(
   System.String^ SnapShotName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SnapShotName`: Name of snapshot to get

### Return Value

[ISnapShot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISnapShot.html)

## VBA Syntax

See [ModelViewManager::GetSnapShot](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetSnapShot.html).

## Remarks

This method is valid only for assemblies.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::AddSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.html)
[IModelViewManager::DeleteSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.html)
[IModelViewManager::GetSnapShots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
