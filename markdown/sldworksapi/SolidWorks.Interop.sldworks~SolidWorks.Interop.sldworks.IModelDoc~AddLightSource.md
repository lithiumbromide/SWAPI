---
title: "AddLightSource Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "AddLightSource"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~AddLightSource.html"
---

# AddLightSource Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::AddLightSource](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~AddLightSource.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddLightSource( _
   ByVal IdName As System.String, _
   ByVal LTyp As System.Integer, _
   ByVal UserName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim IdName As System.String
Dim LTyp As System.Integer
Dim UserName As System.String
Dim value As System.Boolean

value = instance.AddLightSource(IdName, LTyp, UserName)
```

### C#

```csharp
System.bool AddLightSource(
   System.string IdName,
   System.int LTyp,
   System.string UserName
)
```

### C++/CLI

```cpp
System.bool AddLightSource(
   System.String^ IdName,
   System.int LTyp,
   System.String^ UserName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdName`:
- `LTyp`:
- `UserName`:

## VBA Syntax

See [ModelDoc::AddLightSource](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~AddLightSource.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
