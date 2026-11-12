---
title: "DeleteBlends Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "DeleteBlends"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DeleteBlends.html"
---

# DeleteBlends Method (IBody)

Obsolete. Superseded by [IBody2::DeleteBlends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteBlends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteBlends( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Boolean

value = instance.DeleteBlends(NumOfFaces, FaceList)
```

### C#

```csharp
System.bool DeleteBlends(
   System.int NumOfFaces,
   System.object FaceList
)
```

### C++/CLI

```cpp
System.bool DeleteBlends(
   System.int NumOfFaces,
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body::DeleteBlends](ms-its:sldworksapivb6.chm::/sldworks~Body~DeleteBlends.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
