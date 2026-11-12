---
title: "IRemoveFacesFromSheet Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "IRemoveFacesFromSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet.html"
---

# IRemoveFacesFromSheet Method (IBody2)

Removes the specified faces from a sheet (surface) body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub IRemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByRef FacesToRemove As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FacesToRemove As Face2

instance.IRemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

### C#

```csharp
void IRemoveFacesFromSheet(
   System.int NumOfFaces,
   ref Face2 FacesToRemove
)
```

### C++/CLI

```cpp
void IRemoveFacesFromSheet(
   System.int NumOfFaces,
   Face2^% FacesToRemove
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces generated when these two bodies intersect
- `FacesToRemove`: Pointer to an array of [faces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to remove

## VBA Syntax

See [Body2::IRemoveFacesFromSheet](ms-its:sldworksapivb6.chm::/sldworks~Body2~IRemoveFacesFromSheet.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::RemoveFacesFromSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
