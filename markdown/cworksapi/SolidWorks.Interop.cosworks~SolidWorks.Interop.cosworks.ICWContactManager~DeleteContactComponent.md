---
title: "DeleteContactComponent Method (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "DeleteContactComponent"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~DeleteContactComponent.html"
---

# DeleteContactComponent Method (ICWContactManager)

Deletes the specified component contact.

## Syntax

### Visual Basic (Declaration)

```vb
Sub DeleteContactComponent( _
   ByVal SName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim SName As System.String

instance.DeleteContactComponent(SName)
```

### C#

```csharp
void DeleteContactComponent(
   System.string SName
)
```

### C++/CLI

```cpp
void DeleteContactComponent(
   System.String^ SName
)
```

### Parameters

- `SName`: [Name](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactComponent~ContactName.html) of the component contact to delete

## VBA Syntax

See [CWContactManager::DeleteContactComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~DeleteContactComponent.html).

## Examples

[Add Component Contacts (VBA)](Add_Component_Contacts_Example_VB.htm)
[Add Component Contacts (VB.NET)](Add_Component_Contacts_Example_VBNET.htm)
[Add Component Contacts (C#)](Add_Component_Contacts_Example_CSharp.htm)

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::CreateContactComponent Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactComponent.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
