---
title: "IsLoaded Method (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "IsLoaded"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~IsLoaded.html"
---

# IsLoaded Method (IConfiguration)

Gets whether a configuration is loaded.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsLoaded() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

value = instance.IsLoaded()
```

### C#

```csharp
System.bool IsLoaded()
```

### C++/CLI

```cpp
System.bool IsLoaded();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the configuration is loaded, false if not

## VBA Syntax

See [Configuration::IsLoaded](ms-its:sldworksapivb6.chm::/sldworks~Configuration~IsLoaded.html).

## Examples

[Are the Assembly Configurations Loaded (VB.NET)](Are_the_Assembly_Configurations_Loaded_Example_VBNET.htm)
[Are the Assembly Configurations Loaded (VBA)](Are_the_Assembly_Configurations_Loaded_Example_VB.htm)
[Are the Assembly Configurations Loaded (C#)](Are_the_Assembly_Configurations_Loaded_Example_CSharp.htm)

## Remarks

When a configuration is activated, SOLIDWORKS loads it. For example, if a part or assembly document has three configurations named DC1, DC2, and DC3, and DC1 is the active configuration when you open the document, then this method will return true for DC1 and false for DC2 and DC3.

If you activate the configuration named DC2, then this method will return true for DC1 and DC2 because DC1 was previously loaded. If you activate the configuration named DC3, then this method will return true for DC1, DC2, and DC3 because DC1 and DC2 were previously loaded and DC3 is now loaded.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2009 SP03, Revision Number 17.3
