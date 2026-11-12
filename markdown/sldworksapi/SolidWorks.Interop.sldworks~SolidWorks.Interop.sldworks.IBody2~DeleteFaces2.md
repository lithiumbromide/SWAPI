---
title: "DeleteFaces2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeleteFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces2.html"
---

# DeleteFaces2 Method (IBody2)

Obsolete. Superseded by [IBody2::DeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object, _
   ByVal Option As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim Option As System.Integer
Dim value As System.Integer

value = instance.DeleteFaces2(NumOfFaces, FaceList, Option)
```

### C#

```csharp
System.int DeleteFaces2(
   System.int NumOfFaces,
   System.object FaceList,
   System.int Option
)
```

### C++/CLI

```cpp
System.int DeleteFaces2(
   System.int NumOfFaces,
   System.Object^ FaceList,
   System.int Option
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:
- `Option`:

## VBA Syntax

See [Body2::DeleteFaces2](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeleteFaces2.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
