---
title: "DeleteFaces Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "DeleteFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~DeleteFaces.html"
---

# DeleteFaces Method (IBody2)

Obsolete. Superseded by [IBody2::DeleteFaces3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~DeleteFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByVal FaceList As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim NumOfFaces As System.Integer
Dim FaceList As System.Object
Dim value As System.Boolean

value = instance.DeleteFaces(NumOfFaces, FaceList)
```

### C#

```csharp
System.bool DeleteFaces(
   System.int NumOfFaces,
   System.object FaceList
)
```

### C++/CLI

```cpp
System.bool DeleteFaces(
   System.int NumOfFaces,
   System.Object^ FaceList
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `FaceList`:

## VBA Syntax

See [Body2::DeleteFaces](ms-its:sldworksapivb6.chm::/sldworks~Body2~DeleteFaces.html).

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)
