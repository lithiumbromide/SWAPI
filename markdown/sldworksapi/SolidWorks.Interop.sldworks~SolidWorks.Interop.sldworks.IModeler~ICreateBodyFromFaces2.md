---
title: "ICreateBodyFromFaces2 Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromFaces2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces2.html"
---

# ICreateBodyFromFaces2 Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromFaces2( _
   ByVal NumOfFaces As System.Integer, _
   ByRef Faces As Face, _
   ByVal ActionType As System.Integer, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As Face
Dim ActionType As System.Integer
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As Body

value = instance.ICreateBodyFromFaces2(NumOfFaces, Faces, ActionType, DoLocalCheck, LocalCheckResult)
```

### C#

```csharp
Body ICreateBodyFromFaces2(
   System.int NumOfFaces,
   ref Face Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   out System.bool LocalCheckResult
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromFaces2(
   System.int NumOfFaces,
   Face^% Faces,
   System.int ActionType,
   System.bool DoLocalCheck,
   [Out] System.bool LocalCheckResult
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `Faces`:
- `ActionType`:
- `DoLocalCheck`:
- `LocalCheckResult`:

## VBA Syntax

See [Modeler::ICreateBodyFromFaces2](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromFaces2.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
