---
title: "AddContactSet Method (ICWMultipleContactSetsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleContactSetsEditManager"
member: "AddContactSet"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~AddContactSet.html"
---

# AddContactSet Method (ICWMultipleContactSetsEditManager)

Adds the specified contact set to the set of contact sets to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddContactSet( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleContactSetsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.AddContactSet(SName)
```

### C#

```csharp
System.int AddContactSet(
   System.string SName
)
```

### C++/CLI

```cpp
System.int AddContactSet(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of contact set to add

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleContactSetsEditManager::AddContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleContactSetsEditManager~AddContactSet.html).

## Examples

See the [ICWMultipleContactSetsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html) examples.

## See Also

[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
[ICWMultipleContactSetsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager_members.html)
[ICWMultipleContactSetsEditManager::RemoveContactSet Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager~RemoveContactSet.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
