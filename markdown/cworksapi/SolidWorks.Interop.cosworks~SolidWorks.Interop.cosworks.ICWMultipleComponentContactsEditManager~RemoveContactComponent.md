---
title: "RemoveContactComponent Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "RemoveContactComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~RemoveContactComponent.html"
---

# RemoveContactComponent Method (ICWMultipleComponentContactsEditManager)

Removes the specified contact component from the set of contact components to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveContactComponent( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.RemoveContactComponent(SName)
```

### C#

```csharp
System.int RemoveContactComponent(
   System.string SName
)
```

### C++/CLI

```cpp
System.int RemoveContactComponent(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of contact component to remove from the set of contact components to edit

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::RemoveContactComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~RemoveContactComponent.html).

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::AddContactComponent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~AddContactComponent.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
