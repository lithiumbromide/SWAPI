---
title: "Lock Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "Lock"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~Lock.html"
---

# Lock Property (IConfiguration)

Gets or sets whether the configuration is locked.

## Syntax

### Visual Basic (Declaration)

```vb
Property Lock As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
Dim value As System.Boolean

instance.Lock = value

value = instance.Lock
```

### C#

```csharp
System.bool Lock {get; set;}
```

### C++/CLI

```cpp
property System.bool Lock {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True for locked configuration, false for unlocked configuration

## VBA Syntax

See [Configuration::Lock](ms-its:sldworksapivb6.chm::/sldworks~Configuration~Lock.html).

## Examples

[Change Configuration Properties (VBA)](Change_Configuration_Properties_Example_VB.htm)

## Remarks

The names of configurations should not contain any of the special characters reserved
by SOLIDWORKS.

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
