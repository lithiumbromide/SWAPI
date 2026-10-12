---
title: "TrimOrder Property (ICornerMember)"
project: "SOLIDWORKS API Help"
interface: "ICornerMember"
member: "TrimOrder"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember~TrimOrder.html"
---

# TrimOrder Property (ICornerMember)

Gets and sets the trim order of this corner member.

## Syntax

### Visual Basic (Declaration)

```vb
Property TrimOrder As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerMember
Dim value As System.Integer

instance.TrimOrder = value

value = instance.TrimOrder
```

### C#

```csharp
System.int TrimOrder {get; set;}
```

### C++/CLI

```cpp
property System.int TrimOrder {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Trim order

## VBA Syntax

See [CornerMember::TrimOrder](ms-its:sldworksapivb6.chm::/sldworks~CornerMember~TrimOrder.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## See Also

[ICornerMember Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html)
[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
