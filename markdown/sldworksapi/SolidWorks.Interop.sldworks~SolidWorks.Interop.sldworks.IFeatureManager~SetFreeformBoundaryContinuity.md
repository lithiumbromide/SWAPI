---
title: "SetFreeformBoundaryContinuity Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "SetFreeformBoundaryContinuity"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetFreeformBoundaryContinuity.html"
---

# SetFreeformBoundaryContinuity Method (IFeatureManager)

Sets the boundary continuity for this Freeform feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFreeformBoundaryContinuity( _
   ByVal BoundaryIndex As System.Short, _
   ByVal Continuity As System.Short _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim BoundaryIndex As System.Short
Dim Continuity As System.Short

instance.SetFreeformBoundaryContinuity(BoundaryIndex, Continuity)
```

### C#

```csharp
void SetFreeformBoundaryContinuity(
   System.short BoundaryIndex,
   System.short Continuity
)
```

### C++/CLI

```cpp
void SetFreeformBoundaryContinuity(
   System.short BoundaryIndex,
   System.short Continuity
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `BoundaryIndex`: 0-based index of the boundary to modify (i.e., a value ranging from 0 to (Number of face boundaries-1))
- `Continuity`: - -1 = Movaeable
  - 0 = Contact
  - 1 = Tangenet
  - 2= Curvature

## VBA Syntax

See [FeatureManager::SetFreeformBoundaryContinuity](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~SetFreeformBoundaryContinuity.html).

## Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.
2. Add curves on the selected face. Corresponds to [IFeatureManager::SetFreeformCurveData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformCurveData.html).
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformPointData.html).
4. Specify boundary continuity. Corresponds to IFeatureManager::SetFreeformBoundaryContinuity.

  Interactively pull or push the points to change the shape of the selected face.
5. Insert the Freeform feature. Corresponds to this method, [IFeatureManager::InsertFreeform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFreeform2.html).

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
