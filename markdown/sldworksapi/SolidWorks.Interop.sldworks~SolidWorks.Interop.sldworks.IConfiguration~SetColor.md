---
title: "SetColor Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "SetColor"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~SetColor.html"
---

# SetColor Method (IConfiguration)

Sets the color for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetColor( _
   ByVal ColorIn As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim ColorIn As System.Integer
Dim value As System.Boolean

value = instance.SetColor(ColorIn)
```

### C#

```csharp
System.bool SetColor(
   System.int ColorIn
)
```

### C++/CLI

```cpp
System.bool SetColor(
   System.int ColorIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ColorIn`: COLORREF value of the color

### Return Value

True if the color is set, false if not

## VBA Syntax

See [Configuration::SetColor](ms-its:sldworksapivb6.chm::/sldworks~Configuration~SetColor.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
