---
title: "RemoveFacesFromSheet Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "RemoveFacesFromSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~RemoveFacesFromSheet.html"
---

# RemoveFacesFromSheet Method (IBody2)

Removes the specified faces from a sheet (surface) body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FacesToRemove As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FacesToRemove As System.Object

instance.RemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

### C#

```csharp
void RemoveFacesFromSheet(
   System.int NumOfFaces,
   System.object FacesToRemove
)
```

### C++/CLI

```cpp
void RemoveFacesFromSheet(
   System.int NumOfFaces,
   System.Object^ FacesToRemove
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`: Number of faces generated when these two bodies intersect
- `FacesToRemove`: Array of faces to remove

## VBA Syntax

See [Body2::RemoveFacesFromSheet](ms-its:sldworksapivb6.chm::/sldworks~Body2~RemoveFacesFromSheet.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
[IBody2::IRemoveFacesFromSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IRemoveFacesFromSheet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
