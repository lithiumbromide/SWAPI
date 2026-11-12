---
title: "AddSnapShot Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "AddSnapShot"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.html"
---

# AddSnapShot Method (IModelViewManager)

Creates a snapshot with the specified name of an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddSnapShot( _
   ByVal SnapShotName As System.String _
) As SnapShot
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim SnapShotName As System.String
Dim value As SnapShot

value = instance.AddSnapShot(SnapShotName)
```

### C#

```csharp
SnapShot AddSnapShot(
   System.string SnapShotName
)
```

### C++/CLI

```cpp
SnapShot^ AddSnapShot(
   System.String^ SnapShotName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `SnapShotName`: - Name of the snapshot

  - or -

  - "" to give a default name of "Snap`n`"

  - or -

  - "?" to open the Name Snapshot dialog box

### Return Value

[ISnapShot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISnapShot.html)

## VBA Syntax

See [ModelViewManager::AddSnapShot](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~AddSnapShot.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

This method is valid only for assemblies.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::DeleteSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.html)
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.html)
[IModelViewManager::GetSnapShots Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
