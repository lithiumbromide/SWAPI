---
title: "ICWContactSet Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactSet"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet.html"
---

# ICWContactSet Interface

Allows access to a contact set.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWContactSet
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactSet
```

### C#

```csharp
public interface ICWContactSet
```

### C++/CLI

```cpp
public interface class ICWContactSet
```

## VBA Syntax

See [CWContactSet](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactSet.html).

## Examples

[Create Frequency Study with Mixed Mesh (C#)](Create_Frequency_Study_with_Mixed_Mesh_Example_CSharp.htm)
[Create Frequency Study with Mixed Mesh (VB.NET)](Create_Frequency_Study_with_Mixed_Mesh_Example_VBNET.htm)
[Create Frequency Study with Mixed Mesh (VBA)](Create_Frequency_Study_with_Mixed_Mesh_Example_VB.htm)

## Remarks

Component contacts defined by [ICWContactManager::CreateContactComponent](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactComponent.html) override global contact conditions defined by [ICWContactManager::SetGlobalContact](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~SetGlobalContact.html).

Contact sets defined by [ICWContactManager::CreateContactSet](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactSet.html) override both global and component contact definitions.

## Accessors

[ICWContactManager::CreateContactSet](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~CreateContactSet.html)

[ICWContactManager::CreateContactSetsFromPairList](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~CreateContactSetsFromPairList.html)

[ICWContactManager::GetContactSetAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWContactManager~GetContactSetAt.html)

## See Also

[ICWContactSet Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactSet_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWContactComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactComponent.html)
[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWMultipleContactSetsEditManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMultipleContactSetsEditManager.html)
