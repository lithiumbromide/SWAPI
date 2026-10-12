---
title: "ICWContactManager Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html"
---

# ICWContactManager Interface

Allows managing of global contacts, [component contacts](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html), and [contact sets](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactSet.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWContactManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
```

### C#

```csharp
public interface ICWContactManager
```

### C++/CLI

```cpp
public interface class ICWContactManager
```

## VBA Syntax

See [CWContactManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

Component contacts defined by [ICWContactManager::CreateContactComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactComponent.html) override global contact conditions defined by [ICWContactManager::SetGlobalContact](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~SetGlobalContact.html).

Contact sets defined by [ICWContactManager::CreateContactSet](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactSet.html) override both global and component contact definitions.

## Accessors

[ICWStudy::ContactManager](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWStudy~ContactManager.html)

## See Also

[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactSet Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html)
[ICWMultipleComponentContactsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleComponentContactsEditManager.html)
[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
