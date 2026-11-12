---
title: "AllowDistributedCoupling2 Property (ICWPinConnector)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWPinConnector"
member: "AllowDistributedCoupling2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~AllowDistributedCoupling2.html"
---

# AllowDistributedCoupling2 Property (ICWPinConnector)

Gets whether distributed coupling is allowed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWPinConnector
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

This property returns a boolean value which can be cast to an integer. To set this property, you can specify either the boolean or the integer.

If this property is -1, you can set [ICWPinConnector::ConnectionType](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector~ConnectionType.html).

## See Also

[ICWPinConnector Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector.html)
[ICWPinConnector Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWPinConnector_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
