---
title: "GetComponentConfigName Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetComponentConfigName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetComponentConfigName.html"
---

# GetComponentConfigName Method (IConfiguration)

Gets the referenced configuration name of the specified component in this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentConfigName( _
   ByVal CompName As System.String _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim CompName As System.String
Dim value As System.String

value = instance.GetComponentConfigName(CompName)
```

### C#

```csharp
System.string GetComponentConfigName(
   System.string CompName
)
```

### C++/CLI

```cpp
System.String^ GetComponentConfigName(
   System.String^ CompName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Component name

### Return Value

Referenced configuration name

## VBA Syntax

See [Configuration::GetComponentConfigName](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetComponentConfigName.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2001Plus SP1, Revision Number 10.1
