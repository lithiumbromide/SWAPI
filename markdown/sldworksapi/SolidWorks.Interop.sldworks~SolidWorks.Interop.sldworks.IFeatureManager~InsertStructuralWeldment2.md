---
title: "InsertStructuralWeldment2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertStructuralWeldment2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment2.html"
---

# InsertStructuralWeldment2 Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertStructuralWeldment3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertStructuralWeldment2( _
   ByVal Path As System.String, _
   ByVal EndCond As System.Integer, _
   ByVal Angle As System.Double, _
   ByVal Merge As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Path As System.String
Dim EndCond As System.Integer
Dim Angle As System.Double
Dim Merge As System.Boolean
Dim value As Feature

value = instance.InsertStructuralWeldment2(Path, EndCond, Angle, Merge)
```

### C#

```csharp
Feature InsertStructuralWeldment2(
   System.string Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge
)
```

### C++/CLI

```cpp
Feature^ InsertStructuralWeldment2(
   System.String^ Path,
   System.int EndCond,
   System.double Angle,
   System.bool Merge
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Path`: Path, filename, and name of the type of structural member to insert
- `EndCond`: End condition as defined in [swSolidworksWeldmentEndCondOptions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSOLIDWORKSWeldmentEndCondOptions_e.html)
- `Angle`: Angle of rotation of the sketch about the sketch segment
- `Merge`: True to merge the bodies of the arc segments to the adjacent bodies, false to not

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::InsertStructuralWeldment2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertStructuralWeldment2.html).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IStructuralMemberFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructuralMemberFeatureData.html)
[IFeatureManager::InsertStructuralWeldment3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertStructuralWeldment3.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
