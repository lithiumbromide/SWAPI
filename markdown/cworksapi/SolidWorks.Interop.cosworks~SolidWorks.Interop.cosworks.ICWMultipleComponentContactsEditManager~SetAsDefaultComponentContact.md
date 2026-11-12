---
title: "SetAsDefaultComponentContact Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "SetAsDefaultComponentContact"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~SetAsDefaultComponentContact.html"
---

# SetAsDefaultComponentContact Method (ICWMultipleComponentContactsEditManager)

Applies the properties of the specified component contact to the set of all component contacts to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetAsDefaultComponentContact( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.SetAsDefaultComponentContact(SName)
```

### C#

```csharp
System.int SetAsDefaultComponentContact(
   System.string SName
)
```

### C++/CLI

```cpp
System.int SetAsDefaultComponentContact(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the default component contact

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::SetAsDefaultComponentContact](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~SetAsDefaultComponentContact.html).

## Examples

See the [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html) examples.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
