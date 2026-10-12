---
title: "DeleteBlends2 Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "DeleteBlends2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~DeleteBlends2.html"
---

# DeleteBlends2 Method (IBody)

Obsolete. Superseded by [IBody2::CreateBlends2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteBlends2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteBlends2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal DoLocalCheck As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim DoLocalCheck As System.Boolean
Dim value As System.Boolean

value = instance.DeleteBlends2(NumOfFaces, FaceList, DoLocalCheck)
```

### C#

```csharp
System.bool DeleteBlends2(
   System.int NumOfFaces,
   System.object FaceList,
   System.bool DoLocalCheck
)
```

### C++/CLI

```cpp
System.bool DeleteBlends2(
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.bool DoLocalCheck
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `DoLocalCheck`:

## VBA Syntax

See [Body::DeleteBlends2](ms-its:sldworksapivb6.chm::/sldworks~Body~DeleteBlends2.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
