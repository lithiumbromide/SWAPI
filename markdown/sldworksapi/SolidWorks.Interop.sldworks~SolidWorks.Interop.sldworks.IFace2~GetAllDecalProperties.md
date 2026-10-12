---
title: "GetAllDecalProperties Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetAllDecalProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.html"
---

# GetAllDecalProperties Method (IFace2)

Gets all of the decal properties applied to this face in a part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAllDecalProperties() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetAllDecalProperties()
```

### C#

```csharp
System.object GetAllDecalProperties()
```

### C++/CLI

```cpp
System.Object^ GetAllDecalProperties();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [decal properties applied to this face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFaceDecalProperties.html)

## VBA Syntax

See [Face2::GetAllDecalProperties](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetAllDecalProperties.html).

## Examples

[Add Decal (C#)](Add_Decal_Example_CSharp.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)
[Add Decal (VBA)](Add_Decal_Example_VB.htm)

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetDecalsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.html)
[IFace2::GetAllAssemblyDecalProperties Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllAssemblyDecalProperties.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
