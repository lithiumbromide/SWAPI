---
title: "GetConstrainedStatus Method (IComponent2)"
project: "SOLIDWORKS API Help"
interface: "IComponent2"
member: "GetConstrainedStatus"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetConstrainedStatus.html"
---

# GetConstrainedStatus Method (IComponent2)

Gets the constrained status of this component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConstrainedStatus() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IComponent2
Dim value As System.Integer

value = instance.GetConstrainedStatus()
```

### C#

```csharp
System.int GetConstrainedStatus()
```

### C++/CLI

```cpp
System.int GetConstrainedStatus();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Constrained status as defined in [swConstrainedStatus_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swConstrainedStatus_e.html)

## VBA Syntax

See [Component2::GetConstrainedStatus](ms-its:sldworksapivb6.chm::/sldworks~Component2~GetConstrainedStatus.html).

## See Also

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
