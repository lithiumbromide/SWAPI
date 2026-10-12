---
title: "SetAssembly Method (ICollisionDetectionManager)"
project: "SOLIDWORKS API Help"
interface: "ICollisionDetectionManager"
member: "SetAssembly"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~SetAssembly.html"
---

# SetAssembly Method (ICollisionDetectionManager)

Sets the active assembly for this collision detection manager.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAssembly( _
   ByVal OwnerAssem As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICollisionDetectionManager
Dim OwnerAssem As System.Object
Dim value As System.Integer

value = instance.SetAssembly(OwnerAssem)
```

### C#

```csharp
System.int SetAssembly(
   System.object OwnerAssem
)
```

### C++/CLI

```cpp
System.int SetAssembly(
   System.Object^ OwnerAssem
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `OwnerAssem`: [IAssemblyDoc](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)

### Return Value

Error code as defined in [swCollisionManagerSetAssemblyErrors_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCollisionManagerSetAssemblyErrors_e.html)

## VBA Syntax

See [CollisionDetectionManager::SetAssembly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~SetAssembly.html).

## Examples

See the [ICollisionDetectionManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html) examples.

## See Also

[ICollisionDetectionManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager.html)
[ICollisionDetectionManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager_members.html)
[ICollisionDetectionManager::GetAssembly Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICollisionDetectionManager~GetAssembly.html)

## Availability

SOLIDWORKS 2019 FCS Revision Number 27.0
