---
title: "AllowDistributedCoupling Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "AllowDistributedCoupling"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AllowDistributedCoupling.html"
---

# AllowDistributedCoupling Property (ICWPinConnector)

Obsolete. Superseded by [ICWPinConnector::AllowDistributedCoupling2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AllowDistributedCoupling2.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

See [CWPinConnector::AllowDistributedCoupling](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWPinConnector~AllowDistributedCoupling.html).

## Remarks

If this property is true, you can set [ICWPinConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ConnectionType.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS Simulation API 2020 SP0
