---
title: "InsertMoveCopyBody Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertMoveCopyBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoveCopyBody.html"
---

# InsertMoveCopyBody Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertMoveCopyBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMoveCopyBody2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertMoveCopyBody( _
   ByVal TransX As System.Double, _
   ByVal TransY As System.Double, _
   ByVal TransZ As System.Double, _
   ByVal TransDist As System.Double, _
   ByVal RotPointX As System.Double, _
   ByVal RotPointY As System.Double, _
   ByVal RotPointZ As System.Double, _
   ByVal RotAngleX As System.Double, _
   ByVal RotAngleY As System.Double, _
   ByVal RotAngleZ As System.Double, _
   ByVal BCopy As System.Boolean, _
   ByVal NumCopies As System.Integer _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim TransX As System.Double
Dim TransY As System.Double
Dim TransZ As System.Double
Dim TransDist As System.Double
Dim RotPointX As System.Double
Dim RotPointY As System.Double
Dim RotPointZ As System.Double
Dim RotAngleX As System.Double
Dim RotAngleY As System.Double
Dim RotAngleZ As System.Double
Dim BCopy As System.Boolean
Dim NumCopies As System.Integer
Dim value As Feature

value = instance.InsertMoveCopyBody(TransX, TransY, TransZ, TransDist, RotPointX, RotPointY, RotPointZ, RotAngleX, RotAngleY, RotAngleZ, BCopy, NumCopies)
```

### C#

```csharp
Feature InsertMoveCopyBody(
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
)
```

### C++/CLI

```cpp
Feature^ InsertMoveCopyBody(
   System.double TransX,
   System.double TransY,
   System.double TransZ,
   System.double TransDist,
   System.double RotPointX,
   System.double RotPointY,
   System.double RotPointZ,
   System.double RotAngleX,
   System.double RotAngleY,
   System.double RotAngleZ,
   System.bool BCopy,
   System.int NumCopies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TransX`:
- `TransY`:
- `TransZ`:
- `TransDist`:
- `RotPointX`:
- `RotPointY`:
- `RotPointZ`:
- `RotAngleX`:
- `RotAngleY`:
- `RotAngleZ`:
- `BCopy`:
- `NumCopies`:

## VBA Syntax

See [FeatureManager::InsertMoveCopyBody](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertMoveCopyBody.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
