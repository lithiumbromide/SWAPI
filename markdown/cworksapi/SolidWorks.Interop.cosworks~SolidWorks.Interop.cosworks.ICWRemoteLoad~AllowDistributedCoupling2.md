---
title: "AllowDistributedCoupling2 Property (ICWRemoteLoad)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWRemoteLoad"
member: "AllowDistributedCoupling2"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad~AllowDistributedCoupling2.html"
---

# AllowDistributedCoupling2 Property (ICWRemoteLoad)

Gets whether distributed coupling is allowed for the current study.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property AllowDistributedCoupling2 As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWRemoteLoad
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

## Examples

[Add a Remote Load with Distributed Coupling (VBA)](Add_Remote_Load_with_Distributed_Connection_Example_VB.htm)

## Remarks

This property returns a boolean value which can be cast to an integer.

Distributed coupling is allowed only for linear static, topology, and nonlinear static studies.

## See Also

[ICWRemoteLoad Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad.html)
[ICWRemoteLoad Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWRemoteLoad_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
