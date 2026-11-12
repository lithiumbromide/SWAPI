---
title: "AllowDistributedCoupling2 Property (ICWBoltConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWBoltConnector"
member: "AllowDistributedCoupling2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~AllowDistributedCoupling2.html"
---

# AllowDistributedCoupling2 Property (ICWBoltConnector)

Gets whether distributed coupling is allowed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWBoltConnector
Dim value As System.Boolean

value = instance.AllowDistributedCoupling2
```

### C#

```csharp
System.bool AllowDistributedCoupling2 {get;}
```

### C++/CLI

```cpp
property System.bool AllowDistributedCoupling2 {
   System.bool get();
}
```

### Property Value

-1 or true if distributed coupling is allowed, 0 or false if not

## Remarks

This property returns a boolean that can be cast to the integer.

If this property is true, you can set [ICWBoltConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector~ConnectionType.html).

## See Also

[ICWBoltConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector.html)
[ICWBoltConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWBoltConnector_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
