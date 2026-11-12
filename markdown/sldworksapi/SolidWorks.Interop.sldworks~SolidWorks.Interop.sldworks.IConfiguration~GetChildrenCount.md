---
title: "GetChildrenCount Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetChildrenCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildrenCount.html"
---

# GetChildrenCount Method (IConfiguration)

Gets the number of children for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetChildrenCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Integer

value = instance.GetChildrenCount()
```

### C#

```csharp
System.int GetChildrenCount()
```

### C++/CLI

```cpp
System.int GetChildrenCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of children in this configuration

## VBA Syntax

See [Configuration::GetChildrenCount](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetChildrenCount.html).

## Examples

[Work with Configurations (VBA)](Work_with_Configurations_Example_VB.htm)

## Remarks

Call this method before calling [IConfiguration::IGetChildren](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IGetChildren.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
