---
title: "RemoveFacesFromSheet Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "RemoveFacesFromSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~RemoveFacesFromSheet.html"
---

# RemoveFacesFromSheet Method (IBody)

Obsolete. Superseded by [IBody2::RemoveFacesFromSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~RemoveFacesFromSheet.html).

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
Dim instance As IBody
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

- `NumOfFaces`:
- `FacesToRemove`:

## VBA Syntax

See [Body::RemoveFacesFromSheet](ms-its:sldworksapivb6.chm::/sldworks~Body~RemoveFacesFromSheet.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
