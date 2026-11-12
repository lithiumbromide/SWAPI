---
title: "InsertDeleteBody2 Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertDeleteBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertDeleteBody2.html"
---

# InsertDeleteBody2 Method (IFeatureManager)

Inserts a Body-Delete/Keep feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDeleteBody2( _
   ByVal KeepBodies As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim KeepBodies As System.Boolean
Dim value As Feature

value = instance.InsertDeleteBody2(KeepBodies)
```

### C#

```csharp
Feature InsertDeleteBody2(
   System.bool KeepBodies
)
```

### C++/CLI

```cpp
Feature^ InsertDeleteBody2(
   System.bool KeepBodies
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `KeepBodies`: True to keep bodies, false to delete bodies

### Return Value

[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertDeleteBody2](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertDeleteBody2.html).

## Examples

[Insert Body-Delete/Keep Feature (VBA)](Insert_Delete_Body_Feature_Example_VB.htm)
[Insert Body-Delete/Keep Feature (VB.NET)](Insert_Delete_Body_Feature_Example_VBNET.htm)
[Insert Body-Delete/Keep Feature (C#)](Insert_Delete_Body_Feature_Example_CSharp.htm)

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IDeleteBodyFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteBodyFeatureData.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
