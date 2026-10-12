---
title: "InsertStructuralWeldment Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertStructuralWeldment"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment.html"
---

# InsertStructuralWeldment Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertStructuralWeldment( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim value As Feature

value = instance.InsertStructuralWeldment(Path, EndCond, Angle)
```

### C#

```csharp
Feature InsertStructuralWeldment(
   System.string Path,
   System.int EndCond,
   System.double Angle
)
```

### C++/CLI

```cpp
Feature^ InsertStructuralWeldment(
   System.String^ Path,
   System.int EndCond,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`:
- `EndCond`:
- `Angle`:

## VBA Syntax

See [FeatureManager::InsertStructuralWeldment](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertStructuralWeldment.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
