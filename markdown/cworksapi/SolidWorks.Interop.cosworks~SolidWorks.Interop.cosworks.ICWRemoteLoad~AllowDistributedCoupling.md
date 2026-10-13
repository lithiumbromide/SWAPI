---
title: "AllowDistributedCoupling Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "AllowDistributedCoupling"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling.html"
---

# AllowDistributedCoupling Property (ICWRemoteLoad)

Obsolete. Superseded by [ICWRemoteLoad::AllowDistributedCoupling2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
Dim value As System.Integer

value = instance.AllowDistributedCoupling
```

### C#

```csharp
System.int AllowDistributedCoupling {get;}
```

### C++/CLI

```cpp
property System.int AllowDistributedCoupling {
   System.int get();
}
```

### Property Value

True if distributed coupling is allowed, false if it is not allowed

## VBA Syntax

See [CWRemoteLoad::AllowDistributedCoupling](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWRemoteLoad~AllowDistributedCoupling.html).

## Remarks

Distributed coupling is allowed only for linear static, topology, and nonlinear static studies.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)
[ICWRemoteLoad::ConnectionType Property ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~ConnectionType.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
