---
title: "ISetUserValueIn2 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "ISetUserValueIn2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn2.html"
---

# ISetUserValueIn2 Method (IDimension)

Obsolete. Superseded by [IDimension::ISetUserValueIn3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ISetUserValueIn3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ISetUserValueIn2( _
   ByVal Doc As ModelDoc, _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim Doc As ModelDoc
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer

value = instance.ISetUserValueIn2(Doc, NewValue, WhichConfigurations)
```

### C#

```csharp
System.int ISetUserValueIn2(
   ModelDoc Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

### C++/CLI

```cpp
System.int ISetUserValueIn2(
   ModelDoc^ Doc,
   System.double NewValue,
   System.int WhichConfigurations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Doc`:
- `NewValue`:
- `WhichConfigurations`:

## VBA Syntax

See [Dimension::ISetUserValueIn2](ms-its:sldworksapivb6.chm::/sldworks~Dimension~ISetUserValueIn2.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
