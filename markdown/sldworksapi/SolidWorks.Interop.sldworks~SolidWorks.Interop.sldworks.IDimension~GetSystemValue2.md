---
title: "GetSystemValue2 Method (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "GetSystemValue2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue2.html"
---

# GetSystemValue2 Method (IDimension)

Obsolete. See [IDimension::GetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetSystemValue3.html) and [IDimension::IGetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetSystemValue3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSystemValue2( _
   ByVal ConfigName As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim ConfigName As System.String
Dim value As System.Double

value = instance.GetSystemValue2(ConfigName)
```

### C#

```csharp
System.double GetSystemValue2(
   System.string ConfigName
)
```

### C++/CLI

```cpp
System.double GetSystemValue2(
   System.String^ ConfigName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ConfigName`: Name of configuration

### Return Value

Value in system units

## VBA Syntax

See [Dimension::GetSystemValue2](ms-its:sldworksapivb6.chm::/sldworks~Dimension~GetSystemValue2.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
