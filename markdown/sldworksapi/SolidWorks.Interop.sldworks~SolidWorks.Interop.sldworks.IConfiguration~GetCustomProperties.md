---
title: "GetCustomProperties Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetCustomProperties.html"
---

# GetCustomProperties Method (IConfiguration)

Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomProperties( _
   ByRef PropNames As System.Object, _
   ByRef PropValues As System.Object, _
   ByRef PropTypes As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim PropNames As System.Object
Dim PropValues As System.Object
Dim PropTypes As System.Object
Dim value As System.Integer

value = instance.GetCustomProperties(PropNames, PropValues, PropTypes)
```

### C#

```csharp
System.int GetCustomProperties(
   out System.object PropNames,
   out System.object PropValues,
   out System.object PropTypes
)
```

### C++/CLI

```cpp
System.int GetCustomProperties(
   [Out] System.Object^ PropNames,
   [Out] System.Object^ PropValues,
   [Out] System.Object^ PropTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PropNames`:
- `PropValues`:
- `PropTypes`:

## VBA Syntax

See [Configuration::GetCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetCustomProperties.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
