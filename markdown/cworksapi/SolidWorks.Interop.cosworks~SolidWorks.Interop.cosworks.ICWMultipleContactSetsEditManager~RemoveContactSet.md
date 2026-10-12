---
title: "RemoveContactSet Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "RemoveContactSet"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~RemoveContactSet.html"
---

# RemoveContactSet Method (ICWMultipleContactSetsEditManager)

Removes the specified contact set from the set of contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveContactSet( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.RemoveContactSet(SName)
```

### C#

```csharp
System.int RemoveContactSet(
   System.string SName
)
```

### C++/CLI

```cpp
System.int RemoveContactSet(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of contact set to remove from the set of contact sets to edit

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::RemoveContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~RemoveContactSet.html).

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::AddContactSet Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~AddContactSet.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
