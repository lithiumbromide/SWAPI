---
title: "DeSelect Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeSelect"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeSelect.html"
---

# DeSelect Method (IBody2)

Deselects this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeSelect() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.DeSelect()
```

### C#

```csharp
System.bool DeSelect()
```

### C++/CLI

```cpp
System.bool DeSelect();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the body was deselected, false if it was not

## VBA Syntax

See [Body2::DeSelect](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeSelect.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Numbe 10
