---
title: "GetMeshBody Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "GetMeshBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetMeshBody.html"
---

# GetMeshBody Method (IBody2)

Gets the mesh body associated with this body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMeshBody() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim value As System.Object

value = instance.GetMeshBody()
```

### C#

```csharp
System.object GetMeshBody()
```

### C++/CLI

```cpp
System.Object^ GetMeshBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMeshBody.html)

## VBA Syntax

See [Body2::GetMeshBody](ms-its:sldworksapivb6.chm::/sldworks~Body2~GetMeshBody.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## Remarks

This method is valid only if [IBody2::IsMeshBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IsMeshBody.html) is true.

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
