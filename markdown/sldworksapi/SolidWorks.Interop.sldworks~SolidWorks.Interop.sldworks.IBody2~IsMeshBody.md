---
title: "IsMeshBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IsMeshBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsMeshBody.html"
---

# IsMeshBody Method (IBody2)

Gets whether this body is a mesh body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsMeshBody() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Boolean

value = instance.IsMeshBody()
```

### C#

```csharp
System.bool IsMeshBody()
```

### C++/CLI

```cpp
System.bool IsMeshBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if a mesh body, false if not

## VBA Syntax

See [Body2::IsMeshBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~IsMeshBody.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::GetMeshBody Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMeshBody.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
