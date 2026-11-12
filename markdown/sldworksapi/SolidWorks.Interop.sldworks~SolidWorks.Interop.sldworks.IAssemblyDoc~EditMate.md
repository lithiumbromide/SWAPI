---
title: "EditMate Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EditMate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate.html"
---

# EditMate Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::EditMate2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~EditMate2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub EditMate( _
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

instance.EditMate(MateType, Align, Flip, Dist, Angle)
```

### C#

```csharp
void EditMate(
   System.int MateType,
   System.int Align,
   System.bool Flip,
   System.double Dist,
   System.double Angle
)
```

### C++/CLI

```cpp
void EditMate(
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

See [AssemblyDoc::EditMate](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EditMate.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
