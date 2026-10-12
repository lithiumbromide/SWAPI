---
title: "GetSafeBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetSafeBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetSafeBody.html"
---

# GetSafeBody Method (IBody2)

Not implemented.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSafeBody() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As Body2

value = instance.GetSafeBody()
```

### C#

```csharp
Body2 GetSafeBody()
```

### C++/CLI

```cpp
Body2^ GetSafeBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object

**NOTE:** This method is not yet implemented; thus, it will currently always return NULL.

## VBA Syntax

See [Body2::GetSafeBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetSafeBody.html).

## Remarks

To determine if a body is safe, use the [IBody2::IsSafe](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IsSafe.html) property. This property is read-only and does not persist from session to session.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
