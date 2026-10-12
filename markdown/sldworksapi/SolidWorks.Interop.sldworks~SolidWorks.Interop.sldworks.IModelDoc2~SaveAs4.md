---
title: "SaveAs4 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SaveAs4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SaveAs4.html"
---

# SaveAs4 Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::SaveAs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SaveAs.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveAs4( _
   ByVal Name As System.String, _
   ByVal Version As System.Integer, _
   ByVal Options As System.Integer, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Name As System.String
Dim Version As System.Integer
Dim Options As System.Integer
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean

value = instance.SaveAs4(Name, Version, Options, Errors, Warnings)
```

### C#

```csharp
System.bool SaveAs4(
   System.string Name,
   System.int Version,
   System.int Options,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
System.bool SaveAs4(
   System.String^ Name,
   System.int Version,
   System.int Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `Version`:
- `Options`:
- `Errors`:
- `Warnings`:

## VBA Syntax

See [ModelDoc2::SaveAs4](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SaveAs4.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
