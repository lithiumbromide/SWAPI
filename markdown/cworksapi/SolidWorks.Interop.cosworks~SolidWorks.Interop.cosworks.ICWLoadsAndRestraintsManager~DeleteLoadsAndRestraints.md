---
title: "DeleteLoadsAndRestraints Method (ICWLoadsAndRestraintsManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWLoadsAndRestraintsManager"
member: "DeleteLoadsAndRestraints"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~DeleteLoadsAndRestraints.html"
---

# DeleteLoadsAndRestraints Method (ICWLoadsAndRestraintsManager)

Deletes a load or restraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteLoadsAndRestraints( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWLoadsAndRestraintsManager
Dim SName As System.String

instance.DeleteLoadsAndRestraints(SName)
```

### C#

```csharp
void DeleteLoadsAndRestraints(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteLoadsAndRestraints(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the restraint or load object to delete

## VBA Syntax

See [CWLoadsAndRestraintsManager::DeleteLoadsAndRestraints](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWLoadsAndRestraintsManager~DeleteLoadsAndRestraints.html).

## See Also

[ICWLoadsAndRestraintsManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager.html)
[ICWLoadsAndRestraintsManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager_members.html)
[ICWLoadsAndRestraintsManager::CopyLoadsAndRestraintsToStudy Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~CopyLoadsAndRestraintsToStudy.html)
[ICWLoadsAndRestraintsManager::GetLoadsAndRestraints Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWLoadsAndRestraintsManager~GetLoadsAndRestraints.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
