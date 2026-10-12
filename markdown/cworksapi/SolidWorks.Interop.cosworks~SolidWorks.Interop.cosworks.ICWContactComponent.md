---
title: "ICWContactComponent Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactComponent"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html"
---

# ICWContactComponent Interface

Allows access to component contacts.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWContactComponent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactComponent
```

### C#

```csharp
public interface ICWContactComponent
```

### C++/CLI

```cpp
public interface class ICWContactComponent
```

## VBA Syntax

See [CWContactComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactComponent.html).

## Examples

[Add Component Contacts (VBA)](Add_Component_Contacts_Example_VB.htm)
[Add Component Contacts (VB.NET)](Add_Component_Contacts_Example_VBNET.htm)
[Add Component Contacts (C#)](Add_Component_Contacts_Example_CSharp.htm)

## Remarks

Component contacts defined by [ICWContactManager::CreateContactComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactComponent.html) override global contact conditions defined by [ICWContactManager::SetGlobalContact](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~SetGlobalContact.html).

Contact sets defined by [ICWContactManager::CreateContactSet](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactSet.html) override both global and component contact definitions.

## Accessors

[ICWContactManager::CreateContactComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactComponent.html)

[ICWContactManager::GetContactComponentAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~GetContactComponentAt.html)

## See Also

[ICWContactComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
