---
title: "ContactComponentCount Property (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "ContactComponentCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~ContactComponentCount.html"
---

# ContactComponentCount Property (ICWContactManager)

Gets the number of component contacts in the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ContactComponentCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim value As System.Integer

value = instance.ContactComponentCount
```

### C#

```csharp
System.int ContactComponentCount {get;}
```

### C++/CLI

```cpp
property System.int ContactComponentCount {
   System.int get();
}
```

### Property Value

Number of component contacts

## VBA Syntax

See [CWContactManager::ContactComponentCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~ContactComponentCount.html).

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::GetContactComponentAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetContactComponentAt.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
