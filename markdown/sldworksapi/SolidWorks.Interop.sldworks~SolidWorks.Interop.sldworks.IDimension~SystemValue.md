---
title: "SystemValue Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "SystemValue"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SystemValue.html"
---

# SystemValue Property (IDimension)

Obsolete. Superseded by [IDimension::GetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetSystemValue3.html), [IDimension::IGetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetSystemValue3.html), [IDimension::SetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~SetSystemValue3.html), and [IDimension::ISetSystemValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ISetSystemValue3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property SystemValue As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Double

instance.SystemValue = value

value = instance.SystemValue
```

### C#

```csharp
System.double SystemValue {get; set;}
```

### C++/CLI

```cpp
property System.double SystemValue {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Dimension::SystemValue](ms-its:sldworksapivb6.chm::/sldworks~Dimension~SystemValue.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
