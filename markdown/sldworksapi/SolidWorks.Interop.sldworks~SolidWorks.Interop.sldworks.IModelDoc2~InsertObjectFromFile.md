---
title: "InsertObjectFromFile Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertObjectFromFile"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertObjectFromFile.html"
---

# InsertObjectFromFile Method (IModelDoc2)

Obsolete. Superseded by [IModelDocExtension::InsertObjectFromFile](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~InsertObjectFromFile.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::InsertObjectFromFile](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertObjectFromFile.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
