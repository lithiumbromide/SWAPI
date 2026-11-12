---
title: "IsSafe Property (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsSafe"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsSafe.html"
---

# IsSafe Property (IBody2)

Not implemented.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property IsSafe As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.IsSafe
```

### C#

```csharp
System.bool IsSafe {get;}
```

### C++/CLI

```cpp
property System.bool IsSafe {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the IBody2 object survived the rebuild, false if not

**NOTE:** This property is not implemented; thus, it will always return false.

## VBA Syntax

See [Body2::IsSafe](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsSafe.html).

## Remarks

This property is read-only and does not persist from session to session.

To make a body safe, use [IBody2::GetSafeBody](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~GetSafeBody.html) .

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
