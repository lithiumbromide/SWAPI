---
title: "CompConfigProperties3 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CompConfigProperties3"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties3.html"
---

# CompConfigProperties3 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompConfigProperties3( _
   ByVal Suppression As System.Integer, _
   ByVal Solving As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal FeatureDetails As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Suppression As System.Integer
Dim Solving As System.Integer
Dim Visibility As System.Boolean
Dim FeatureDetails As System.Boolean
Dim value As System.Boolean

value = instance.CompConfigProperties3(Suppression, Solving, Visibility, FeatureDetails)
```

### C#

```csharp
System.bool CompConfigProperties3(
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool FeatureDetails
)
```

### C++/CLI

```cpp
System.bool CompConfigProperties3(
   System.int Suppression,
   System.int Solving,
   System.bool Visibility,
   System.bool FeatureDetails
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Suppression`:
- `Solving`:
- `Visibility`:
- `FeatureDetails`:

## VBA Syntax

See [AssemblyDoc::CompConfigProperties3](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CompConfigProperties3.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
