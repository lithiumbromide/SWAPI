---
title: "EditDeleteFace Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EditDeleteFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EditDeleteFace.html"
---

# EditDeleteFace Method (IFeatureManager)

Edits a DeleteFace feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function EditDeleteFace( _
   ByVal Refill As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Refill As System.Integer
Dim value As System.Boolean

value = instance.EditDeleteFace(Refill)
```

### C#

```csharp
System.bool EditDeleteFace(
   System.int Refill
)
```

### C++/CLI

```cpp
System.bool EditDeleteFace(
   System.int Refill
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Refill`: 1 refills the face after it is deleted

  0 does not

### Return Value

True if the operation succeeds, false if not

## VBA Syntax

See [FeatureManager::EditDeleteFace](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EditDeleteFace.html).

## Remarks

This method assumes that the new faces to delete and the [DeleteFace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDeleteFaceFeatureData.html) feature are selected.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IDeleteFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDeleteFaceFeatureData.html)
[IModelDocExtension::InsertDeleteFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~InsertDeleteFace.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
