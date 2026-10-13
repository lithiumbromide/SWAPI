---
title: "InsertObjectFromFile Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "InsertObjectFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~InsertObjectFromFile.html"
---

# InsertObjectFromFile Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::InsertObjectFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertObjectFromFile.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertObjectFromFile( _
   ByVal FilePath As System.String, _
   ByVal CreateLink As System.Boolean, _
   ByVal Xx As System.Double, _
   ByVal Yy As System.Double, _
   ByVal Zz As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim FilePath As System.String
Dim CreateLink As System.Boolean
Dim Xx As System.Double
Dim Yy As System.Double
Dim Zz As System.Double
Dim value As System.Boolean

value = instance.InsertObjectFromFile(FilePath, CreateLink, Xx, Yy, Zz)
```

### C#

```csharp
System.bool InsertObjectFromFile(
   System.string FilePath,
   System.bool CreateLink,
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

### C++/CLI

```cpp
System.bool InsertObjectFromFile(
   System.String^ FilePath,
   System.bool CreateLink,
   System.double Xx,
   System.double Yy,
   System.double Zz
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FilePath`:
- `CreateLink`:
- `Xx`:
- `Yy`:
- `Zz`:

## VBA Syntax

See [ModelDoc::InsertObjectFromFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~InsertObjectFromFile.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
