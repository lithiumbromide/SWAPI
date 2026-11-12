---
title: "GetDecalsCount Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetDecalsCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetDecalsCount.html"
---

# GetDecalsCount Method (IFace2)

Gets the number of decals applied to this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDecalsCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetDecalsCount()
```

### C#

```csharp
System.int GetDecalsCount()
```

### C++/CLI

```cpp
System.int GetDecalsCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of decals applied to this face

## VBA Syntax

See [Face2::GetDecalsCount](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetDecalsCount.html).

## Examples

[Add Decal (C#)](Add_Decal_Example_CSharp.htm)
[Add Decal (VB.NET)](Add_Decal_Example_VBNET.htm)
[Add Decal (VBA)](Add_Decal_Example_VB.htm)

## Remarks

Call this method before calling [IFace2::IGetAllDecalProperties](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetAllDecalProperties.html) to get the size of the array for that method.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFae2::GetAllDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetAllDecalProperties.html)
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.html)
[IFace2::IGetDecalProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetDecalProperties.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
