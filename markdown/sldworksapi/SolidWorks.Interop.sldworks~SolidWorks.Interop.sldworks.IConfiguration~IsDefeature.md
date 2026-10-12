---
title: "IsDefeature Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IsDefeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDefeature.html"
---

# IsDefeature Method (IConfiguration)

Gets whether this configuration is a defeature configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsDefeature() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

value = instance.IsDefeature()
```

### C#

```csharp
System.bool IsDefeature()
```

### C++/CLI

```cpp
System.bool IsDefeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if this configuration is a defeature configuration, false if not

## VBA Syntax

See [Configuration::IsDefeature](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IsDefeature.html).

## Remarks

A defeature configuration is a type of derived configuration. After using the Defeature tool to remove details from assemblies, multibody parts, and single-body parts, you can save the less-detailed model as a configuration and maintain references to the original part or assembly.

For more information see the **SOLIDWORKS Design user-interface help > Assemblies > Other Assembly Techniques > Defeature** topic.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IConfiguration::IsDerived Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsDerived.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
