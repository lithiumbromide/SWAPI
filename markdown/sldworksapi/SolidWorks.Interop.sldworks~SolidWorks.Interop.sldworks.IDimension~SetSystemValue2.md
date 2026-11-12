---
title: "SetSystemValue2 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SetSystemValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue2.html"
---

# SetSystemValue2 Method (IDimension)

Obsolete. Superseded by [IDimension::SetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~SetSystemValue3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetSystemValue2( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim value As System.Integer

value = instance.SetSystemValue2(NewValue, WhichConfigurations)
```

### C#

```csharp
System.int SetSystemValue2(
   System.double NewValue,
   System.int WhichConfigurations
)
```

### C++/CLI

```cpp
System.int SetSystemValue2(
   System.double NewValue,
   System.int WhichConfigurations
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NewValue`:
- `WhichConfigurations`:

## VBA Syntax

See [Dimension::SetSystemValue2](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SetSystemValue2.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
