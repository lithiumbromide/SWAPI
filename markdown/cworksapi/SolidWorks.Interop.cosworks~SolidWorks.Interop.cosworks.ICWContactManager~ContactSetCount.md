---
title: "ContactSetCount Property (ICWContactManager)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWContactManager"
member: "ContactSetCount"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~ContactSetCount.html"
---

# ContactSetCount Property (ICWContactManager)

Gets the number of contact sets in the active study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ContactSetCount As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWContactManager
Dim value As System.Integer

value = instance.ContactSetCount
```

### C#

```csharp
System.int ContactSetCount {get;}
```

### C++/CLI

```cpp
property System.int ContactSetCount {
   System.int get();
}
```

### Property Value

Number of contact sets

## VBA Syntax

See [CWContactManager::ContactSetCount](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWContactManager~ContactSetCount.html).

## Examples

[Copy Items to Another Study (VBA)](Copy_Items_to_Another_Study_Example_VB.htm)
[Copy Items to Another Study (VB.NET)](Copy_Items_to_Another_Study_Example_VBNET.htm)
[Copy Items to Another Study (C#)](Copy_Items_to_Another_Study_Example_CSharp.htm)

## See Also

[ICWContactManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager.html)
[ICWContactManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager_members.html)
[ICWContactManager::GetContactSetAt Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWContactManager~GetContactSetAt.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
