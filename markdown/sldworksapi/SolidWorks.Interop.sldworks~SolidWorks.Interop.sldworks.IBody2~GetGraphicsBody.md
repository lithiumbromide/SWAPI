---
title: "GetGraphicsBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetGraphicsBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetGraphicsBody.html"
---

# GetGraphicsBody Method (IBody2)

Gets the graphics body associated with this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetGraphicsBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetGraphicsBody()
```

### C#

```csharp
System.object GetGraphicsBody()
```

### C++/CLI

```cpp
System.Object^ GetGraphicsBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IGraphicsBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGraphicsBody.html)

## VBA Syntax

See [Body2::GetGraphicsBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetGraphicsBody.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## Remarks

This method is valid only if [IBody2::IsGraphicsBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsGraphicsBody.html) is true.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
