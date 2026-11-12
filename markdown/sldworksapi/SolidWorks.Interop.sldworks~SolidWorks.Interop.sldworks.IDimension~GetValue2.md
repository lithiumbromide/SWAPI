---
title: "GetValue2 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue2.html"
---

# GetValue2 Method (IDimension)

Obsolete. Superseded by [IDimension::GetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetValue3.html) and [IDimension::IGetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetValue3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetValue2( _
   ByVal ConfigName As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim ConfigName As System.String
Dim value As System.Double

value = instance.GetValue2(ConfigName)
```

### C#

```csharp
System.double GetValue2(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.double GetValue2(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`:

## VBA Syntax

See [Dimension::GetValue2](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetValue2.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
