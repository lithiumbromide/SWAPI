---
title: "AddMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "AddMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate.html"
---

# AddMate Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::AddMate3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddMate3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub AddMate( _
   ByVal MateType As System.Integer, _
   ByVal Align As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Dist As System.Double, _
   ByVal Angle As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim MateType As System.Integer
Dim Align As System.Integer
Dim Flip As System.Boolean
Dim Dist As System.Double
Dim Angle As System.Double

instance.AddMate(MateType, Align, Flip, Dist, Angle)
```

### C#

```csharp
void AddMate(
   System.int MateType,
   System.int Align,
   System.bool Flip,
   System.double Dist,
   System.double Angle
)
```

### C++/CLI

```cpp
void AddMate(
   System.int MateType,
   System.int Align,
   System.bool Flip,
   System.double Dist,
   System.double Angle
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `MateType`:
- `Align`:
- `Flip`:
- `Dist`:
- `Angle`:

## VBA Syntax

See [AssemblyDoc::AddMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~AddMate.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
