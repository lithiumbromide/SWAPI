---
title: "Select2 Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Select2.html"
---

# Select2 Method (IConfiguration)

Selects the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal AppendFlag As System.Boolean, _
   ByVal SelectData As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim AppendFlag As System.Boolean
Dim SelectData As SelectData
Dim value As System.Boolean

value = instance.Select2(AppendFlag, SelectData)
```

### C#

```csharp
System.bool Select2(
   System.bool AppendFlag,
   SelectData SelectData
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool AppendFlag,
   SelectData^ SelectData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `AppendFlag`: True appends the configuration to the selection list, false replaces the selection
  list with the configuration
- `SelectData`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the configuration is selected, false if not

## VBA Syntax

See [Configuration::Select2](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Select2.html).

## Examples

[Add Derived Configurations (VBA)](Add_Derived_Configurations_Example_VB.htm)
[Add Derived Configurations (VB.NET)](Add_Derived_Configurations_Example_VBNET.htm)
[Add Derived Configurations (C#)](Add_Derived_Configurations_Example_CSharp.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
