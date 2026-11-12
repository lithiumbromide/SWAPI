---
title: "IsComponentFailed2 Method (ICWMesh)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWMesh"
member: "IsComponentFailed2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh~IsComponentFailed2.html"
---

# IsComponentFailed2 Method (ICWMesh)

Checks the status of the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsComponentFailed2( _
   ByVal SName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICWMesh
Dim SName As System.String
Dim value As System.Boolean

value = instance.IsComponentFailed2(SName)
```

### C#

```csharp
System.bool IsComponentFailed2(
   System.string SName
)
```

### C++/CLI

```cpp
System.bool IsComponentFailed2(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of component

### Return Value

-1 or true if failed, 0 or false if not

## See Also

[ICWMesh Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh.html)
[ICWMesh Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWMesh_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
