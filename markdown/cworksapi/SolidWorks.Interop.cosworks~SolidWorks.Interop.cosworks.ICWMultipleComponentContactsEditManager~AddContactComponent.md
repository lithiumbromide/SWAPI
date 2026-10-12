---
title: "AddContactComponent Method (ICWMultipleComponentContactsEditManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMultipleComponentContactsEditManager"
member: "AddContactComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~AddContactComponent.html"
---

# AddContactComponent Method (ICWMultipleComponentContactsEditManager)

Adds the specified contact component to the set of contact components to edit.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddContactComponent( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMultipleComponentContactsEditManager
Dim SName As System.String
Dim value As System.Integer

value = instance.AddContactComponent(SName)
```

### C#

```csharp
System.int AddContactComponent(
   System.string SName
)
```

### C++/CLI

```cpp
System.int AddContactComponent(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of contact component to add

### Return Value

Error code as defined in [swsMultipleContactsEditErrorCode_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMultipleContactsEditErrorCode_e.html)

## VBA Syntax

See [CWMultipleComponentContactsEditManager::AddContactComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWMultipleComponentContactsEditManager~AddContactComponent.html).

## Examples

See the [ICWMultipleComponentContactsEditManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html) examples.

## See Also

[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleComponentContactsEditManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager_members.html)
[ICWMultipleComponentContactsEditManager::RemoveContactComponent Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager~RemoveContactComponent.html)

## Availability

SOLIDWORKS Simulation API 2017 SP0
