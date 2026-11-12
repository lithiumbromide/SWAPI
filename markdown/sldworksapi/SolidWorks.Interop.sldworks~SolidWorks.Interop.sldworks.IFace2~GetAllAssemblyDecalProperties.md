---
title: "GetAllAssemblyDecalProperties Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetAllAssemblyDecalProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllAssemblyDecalProperties.html"
---

# GetAllAssemblyDecalProperties Method (IFace2)

Gets all of the decal properties applied to this face in an assembly component.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllAssemblyDecalProperties() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetAllAssemblyDecalProperties()
```

### C#

```csharp
System.object GetAllAssemblyDecalProperties()
```

### C++/CLI

```cpp
System.Object^ GetAllAssemblyDecalProperties();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFaceDecalProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceDecalProperties.html) objects

## VBA Syntax

See [Face2::GetAllAssemblyDecalProperties](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetAllAssemblyDecalProperties.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetAllDecalProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
