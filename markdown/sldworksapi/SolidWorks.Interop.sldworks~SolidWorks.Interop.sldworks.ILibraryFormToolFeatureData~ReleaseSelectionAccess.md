---
title: "ReleaseSelectionAccess Method (ILibraryFormToolFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILibraryFormToolFeatureData"
member: "ReleaseSelectionAccess"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~ReleaseSelectionAccess.html"
---

# ReleaseSelectionAccess Method (ILibraryFormToolFeatureData)

Releases access to the selections that created this library forming tool feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ReleaseSelectionAccess()
```

### Visual Basic (Usage)

```vb
Dim instance As ILibraryFormToolFeatureData

instance.ReleaseSelectionAccess()
```

### C#

```csharp
void ReleaseSelectionAccess()
```

### C++/CLI

```cpp
void ReleaseSelectionAccess();
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

## VBA Syntax

See

[LibraryFormToolFeatureData::ReleaseSelectionAccess](ms-its:sldworksapivb6.chm::/sldworks~LibraryFormToolFeatureData~ReleaseSelectionAccess.html)

.

## Remarks

[ILibraryFormToolFeatureData::AccessSelections](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~AccessSelections.html)puts the model into a rollback state to allow access to the selections that define this feature.

Use this method to restore the rollback state if you did not modify the feature or use[IFeature::ModifyDefinition](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~ModifyDefinition.html)if you did.

## See Also

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.html)

[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.html)

## Availability

SOLIDWORKS 2025 SP02, Revision Number 33.2
