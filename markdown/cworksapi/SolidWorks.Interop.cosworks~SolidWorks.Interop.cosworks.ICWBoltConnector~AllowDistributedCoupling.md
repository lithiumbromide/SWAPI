---
title: "AllowDistributedCoupling Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "AllowDistributedCoupling"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~AllowDistributedCoupling.html"
---

# AllowDistributedCoupling Property (ICWBoltConnector)

Obsolete. Superseded by [ICWBoltConnector::AllowDistributedCoupling2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~AllowDistributedCoupling2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
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

True if distributed coupling is allowed, false if not

## VBA Syntax

See [CWBoltConnector::AllowDistributedCoupling](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWBoltConnector~AllowDistributedCoupling.html).

## Remarks

If this property is true, you can set [ICWBoltConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ConnectionType.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
