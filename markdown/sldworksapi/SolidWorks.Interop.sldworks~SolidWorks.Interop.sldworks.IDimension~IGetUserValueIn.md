---
title: "IGetUserValueIn Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "IGetUserValueIn"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn.html"
---

# IGetUserValueIn Method (IDimension)

Obsolete. Superseded by [IDimension::IGetUserValueIn2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetUserValueIn2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetUserValueIn( _
   ByVal Doc As ModelDoc _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As ModelDoc
Dim value As System.Double

value = instance.IGetUserValueIn(Doc)
```

### C#

```csharp
System.double IGetUserValueIn(
   ModelDoc Doc
)
```

### C++/CLI

```cpp
System.double IGetUserValueIn(
   ModelDoc^ Doc
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`:

## VBA Syntax

See [Dimension::IGetUserValueIn](ms-its:sldworksapivb6.chm::/sldworks~Dimension~IGetUserValueIn.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
