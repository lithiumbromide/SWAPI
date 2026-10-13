---
title: "IGetCustomProperties Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetCustomProperties"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetCustomProperties.html"
---

# IGetCustomProperties Method (IConfiguration)

Obsolete. Superseded by [IConfiguration::CustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~CustomPropertyManager.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub IGetCustomProperties( _
   ByVal NumProps As System.Integer, _
   ByRef PropNames As System.String, _
   ByRef PropValues As System.String, _
   ByRef PropTypes As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim NumProps As System.Integer
Dim PropNames As System.String
Dim PropValues As System.String
Dim PropTypes As System.Integer

instance.IGetCustomProperties(NumProps, PropNames, PropValues, PropTypes)
```

### C#

```csharp
void IGetCustomProperties(
   System.int NumProps,
   out System.string PropNames,
   out System.string PropValues,
   out System.int PropTypes
)
```

### C++/CLI

```cpp
void IGetCustomProperties(
   System.int NumProps,
   [Out] System.String^ PropNames,
   [Out] System.String^ PropValues,
   [Out] System.int PropTypes
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumProps`:
- `PropNames`:
- `PropValues`:
- `PropTypes`:

## VBA Syntax

See [Configuration::IGetCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IGetCustomProperties.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
