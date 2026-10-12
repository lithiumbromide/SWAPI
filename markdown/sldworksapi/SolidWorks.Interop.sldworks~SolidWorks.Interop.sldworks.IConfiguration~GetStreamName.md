---
title: "GetStreamName Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "GetStreamName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetStreamName.html"
---

# GetStreamName Method (IConfiguration)

Gets the name of the stream for the current configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStreamName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.String

value = instance.GetStreamName()
```

### C#

```csharp
System.string GetStreamName()
```

### C++/CLI

```cpp
System.String^ GetStreamName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the stream

## VBA Syntax

See [Configuration::GetStreamName](ms-its:sldworksapivb6.chm::/sldworks~Configuration~GetStreamName.html).

## Examples

[Traverse Hierarchy of Configurations (VBA)](Traverse_Hierarchy_of_Configurations_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
