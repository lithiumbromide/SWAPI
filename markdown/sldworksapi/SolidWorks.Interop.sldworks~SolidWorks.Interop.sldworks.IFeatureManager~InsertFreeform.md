---
title: "InsertFreeform Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "InsertFreeform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFreeform.html"
---

# InsertFreeform Method (IFeatureManager)

Obsolete. Superseded by [IFeatureManager::InsertFreeform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertFreeform2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertFreeform( _
   ByVal Continuity0 As System.Short, _
   ByVal Continuity1 As System.Short, _
   ByVal Continuity2 As System.Short, _
   ByVal Continuity3 As System.Short, _
   ByVal Symmetric0 As System.Boolean, _
   ByVal Symmetric1 As System.Boolean _
) As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim Continuity0 As System.Short
Dim Continuity1 As System.Short
Dim Continuity2 As System.Short
Dim Continuity3 As System.Short
Dim Symmetric0 As System.Boolean
Dim Symmetric1 As System.Boolean
Dim value As Feature

value = instance.InsertFreeform(Continuity0, Continuity1, Continuity2, Continuity3, Symmetric0, Symmetric1)
```

### C#

```csharp
Feature InsertFreeform(
   System.short Continuity0,
   System.short Continuity1,
   System.short Continuity2,
   System.short Continuity3,
   System.bool Symmetric0,
   System.bool Symmetric1
)
```

### C++/CLI

```cpp
Feature^ InsertFreeform(
   System.short Continuity0,
   System.short Continuity1,
   System.short Continuity2,
   System.short Continuity3,
   System.bool Symmetric0,
   System.bool Symmetric1
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Continuity0`: Continuity of edge 1:

  - -1 = Movable
  - 0 = Contact
  - 2 = Tangent
  - 3 = Curvature
- `Continuity1`: Continuity of edge 2:

  - -1 = Movable
  - 0 = Contact
  - 2 = Tangent
  - 3 = Curvature
- `Continuity2`: Continuity of edge 3:

  - -1 = Movable
  - 0 = Contact
  - 2 = Tangent
  - 3 = Curvature
- `Continuity3`: Continuity of edge 4:

  - -1 = Movable
  - 0 = Contact
  - 2 = Tangent
  - 3 = Curvature
- `Symmetric0`: True if symmetry is on in Direction 0, false if not
- `Symmetric1`: True if symmetry is on in Direction 1, false if not

### Return Value

Pointer to the newly created freeform [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FeatureManager::InsertFreeform](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~InsertFreeform.html).

## Remarks

The SOLIDWORKS API Freeform-related methods are intended to journal the actions performed by an interactive user while creating the feature. Because user interaction is required to create a Freeform feature, fully automating the creation of it is not possible using the SOLIDWORKS API.

The typical steps performed by an interactive user to create a Freeform feature are:

1. Select the face to form.

  **NOTE**: The face must have four sides.
2. Add curves on the selected face. Corresponds to [IFeatureManager::SetFreeformCurveData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformCurveData.html).
3. Add points on the curves. Corresponds to [IFeatureManager::SetFreeformPointData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~SetFreeformPointData.html).

  Interactively pull or push the points to change the shape of the selected face.
4. Insert the Freeform feature. Corresponds to this method, IFeatureManager::InsertFreeform.

Record a macro while interactively creating a Freeform feature, then examine the macro to see the order in which the Freeform-related methods are recorded.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
