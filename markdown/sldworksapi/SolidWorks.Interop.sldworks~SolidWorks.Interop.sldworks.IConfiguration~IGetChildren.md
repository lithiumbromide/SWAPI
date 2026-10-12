---
title: "IGetChildren Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IGetChildren"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IGetChildren.html"
---

# IGetChildren Method (IConfiguration)

Gets all of the children configurations of this derived configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetChildren( _
   ByVal NumChildren As System.Integer _
) As Configuration
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim NumChildren As System.Integer
Dim value As Configuration

value = instance.IGetChildren(NumChildren)
```

### C#

```csharp
Configuration IGetChildren(
   System.int NumChildren
)
```

### C++/CLI

```cpp
Configuration^ IGetChildren(
   System.int NumChildren
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `NumChildren`: Number of children configurations of this configuration

### Return Value

- in-process, unmanaged C++: Pointer to an array containing the children [configurations](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration.html) of this configuration

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

To determine if this configuration is derived, call [IConfiguration::IsDerived](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~IsDerived.html).

Before calling this method, call [IConfiguration::GetChildrenCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IConfiguration~GetChildrenCount.html).

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::GetChildren Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetChildren.html)
[IConfiguration::GetParent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetParent.html)
[IConfiguration::GetRootComponent3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetRootComponent3.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
