---
title: "IsGraphicsBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsGraphicsBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsGraphicsBody.html"
---

# IsGraphicsBody Method (IBody2)

Gets whether this body is a graphics body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsGraphicsBody() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.IsGraphicsBody()
```

### C#

```csharp
System.bool IsGraphicsBody()
```

### C++/CLI

```cpp
System.bool IsGraphicsBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a graphics body, false if not

## VBA Syntax

See [Body2::IsGraphicsBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsGraphicsBody.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetGraphicsBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetGraphicsBody.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
