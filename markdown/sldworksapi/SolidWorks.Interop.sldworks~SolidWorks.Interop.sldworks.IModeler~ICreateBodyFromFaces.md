---
title: "ICreateBodyFromFaces Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICreateBodyFromFaces"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICreateBodyFromFaces.html"
---

# ICreateBodyFromFaces Method (IModeler)

Obsolete. Superseded by [IModeler::ICreateBodyFromFace3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICreateBodyFromFaces3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBodyFromFaces( _
   ByVal NumOfFaces As System.Integer, _
   ByRef Faces As Face, _
   ByVal DoLocalCheck As System.Boolean, _
   ByRef LocalCheckResult As System.Boolean _
) As Body
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim NumOfFaces As System.Integer
Dim Faces As Face
Dim DoLocalCheck As System.Boolean
Dim LocalCheckResult As System.Boolean
Dim value As Body

value = instance.ICreateBodyFromFaces(NumOfFaces, Faces, DoLocalCheck, LocalCheckResult)
```

### C#

```csharp
Body ICreateBodyFromFaces(
   System.int NumOfFaces,
   ref Face Faces,
   System.bool DoLocalCheck,
   ref System.bool LocalCheckResult
)
```

### C++/CLI

```cpp
Body^ ICreateBodyFromFaces(
   System.int NumOfFaces,
   Face^% Faces,
   System.bool DoLocalCheck,
   System.bool% LocalCheckResult
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumOfFaces`:
- `Faces`:
- `DoLocalCheck`:
- `LocalCheckResult`:

## VBA Syntax

See [Modeler::ICreateBodyFromFaces](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICreateBodyFromFaces.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
