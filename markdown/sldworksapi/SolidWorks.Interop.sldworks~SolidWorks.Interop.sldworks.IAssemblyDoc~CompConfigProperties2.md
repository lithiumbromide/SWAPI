---
title: "CompConfigProperties2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "CompConfigProperties2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CompConfigProperties2.html"
---

# CompConfigProperties2 Method (IAssemblyDoc)

Obsolete. Superseded by [IAssemblyDoc::CompConfigProperties4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~CompConfigProperties4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CompConfigProperties2( _
   ByVal Suppression As System.Integer, _
   ByVal Visibility As System.Boolean, _
   ByVal FeatureDetails As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Suppression As System.Integer
Dim Visibility As System.Boolean
Dim FeatureDetails As System.Boolean
Dim value As System.Boolean

value = instance.CompConfigProperties2(Suppression, Visibility, FeatureDetails)
```

### C#

```csharp
System.bool CompConfigProperties2(
   System.int Suppression,
   System.bool Visibility,
   System.bool FeatureDetails
)
```

### C++/CLI

```cpp
System.bool CompConfigProperties2(
   System.int Suppression,
   System.bool Visibility,
   System.bool FeatureDetails
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Suppression`:
- `Visibility`:
- `FeatureDetails`:

## VBA Syntax

See [AssemblyDoc::CompConfigProperties2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~CompConfigProperties2.html).

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
