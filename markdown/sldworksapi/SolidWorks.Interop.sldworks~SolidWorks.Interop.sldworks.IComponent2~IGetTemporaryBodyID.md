---
title: "IGetTemporaryBodyID Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "IGetTemporaryBodyID"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetTemporaryBodyID.html"
---

# IGetTemporaryBodyID Method (IComponent2)

Gets the current body tag ID, which is not a permanent ID.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTemporaryBodyID() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.IGetTemporaryBodyID()
```

### C#

```csharp
System.int IGetTemporaryBodyID()
```

### C++/CLI

```cpp
System.int IGetTemporaryBodyID();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Body ID

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
