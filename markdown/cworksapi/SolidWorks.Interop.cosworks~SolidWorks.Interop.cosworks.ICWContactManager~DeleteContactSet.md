---
title: "DeleteContactSet Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "DeleteContactSet"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactSet.html"
---

# DeleteContactSet Method (ICWContactManager)

Deletes the specified contact set.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteContactSet( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim SName As System.String

instance.DeleteContactSet(SName)
```

### C#

```csharp
void DeleteContactSet(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteContactSet(
   System.String^ SName
)
```

### Parameters

- `SName`: [Name](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet~ContactName.html) of contact set to delete

## VBA Syntax

See [CWContactManager::DeleteContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~DeleteContactSet.html).

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::CreateContactSet Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSet.html)
[ICWContactManager::CreateContactSetsFromPairList Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
