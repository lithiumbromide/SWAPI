---
title: "GetSnapShots Method (IModelViewManager)"
project: "SOLIDWORKS API Help"
interface: "IModelViewManager"
member: "GetSnapShots"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShots.html"
---

# GetSnapShots Method (IModelViewManager)

Gets the snapshots of an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSnapShots() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelViewManager
Dim value As System.Object

value = instance.GetSnapShots()
```

### C#

```csharp
System.object GetSnapShots()
```

### C++/CLI

```cpp
System.Object^ GetSnapShots();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [ISnapShot](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISnapShot.html)s

## VBA Syntax

See [ModelViewManager::GetSnapShots](ms-its:sldworksapivb6.chm::/sldworks~ModelViewManager~GetSnapShots.html).

## Examples

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

## Remarks

This method is valid only for assemblies.

## See Also

[IModelViewManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager.html)
[IModelViewManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager_members.html)
[IModelViewManager::AddSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~AddSnapShot.html)
[IModelViewManager::DeleteSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~DeleteSnapShot.html)
[IModelViewManager::GetSnapShot Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelViewManager~GetSnapShot.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
