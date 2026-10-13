---
title: "GetComponentSuppressionState Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetComponentSuppressionState"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentSuppressionState.html"
---

# GetComponentSuppressionState Method (IConfiguration)

Gets the suppression state of the specified component in this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentSuppressionState( _
   ByVal CompName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim CompName As System.String
Dim value As System.Boolean

value = instance.GetComponentSuppressionState(CompName)
```

### C#

```csharp
System.bool GetComponentSuppressionState(
   System.string CompName
)
```

### C++/CLI

```cpp
System.bool GetComponentSuppressionState(
   System.String^ CompName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Component name

### Return Value

True if the configuration is suppressed, false if not

## VBA Syntax

See [Configuration::GetComponentSuppressionState](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetComponentSuppressionState.html).

## Examples

[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)
[Get Whether Components Are Laoded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)

## Remarks

SOLIDWORKS 2001Plus SP1, Revision Number 10.1

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
