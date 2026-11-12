---
title: "IRemoveFacesFromSheet Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "IRemoveFacesFromSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~IRemoveFacesFromSheet.html"
---

# IRemoveFacesFromSheet Method (IBody)

Obsolete. Superseded by [IBody2::IRemoveFacesFromSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~IRemoveFacesFromSheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IRemoveFacesFromSheet( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FacesToRemove As System.IntPtr _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FacesToRemove As System.IntPtr

instance.IRemoveFacesFromSheet(NumOfFaces, FacesToRemove)
```

### C#

```csharp
void IRemoveFacesFromSheet(
   System.int NumOfFaces,
   System.IntPtr FacesToRemove
)
```

### C++/CLI

```cpp
void IRemoveFacesFromSheet(
   System.int NumOfFaces,
   System.IntPtr FacesToRemove
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FacesToRemove`:

## VBA Syntax

See [Body::IRemoveFacesFromSheet](ms-its:sldworksapivb6.chm::/sldworks~Body~IRemoveFacesFromSheet.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
