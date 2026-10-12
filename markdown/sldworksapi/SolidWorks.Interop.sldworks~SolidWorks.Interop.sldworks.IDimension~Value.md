---
title: "Value Property (IDimension)"
project: "SOLIDWORKS API Help"
interface: "IDimension"
member: "Value"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~Value.html"
---

# Value Property (IDimension)

Obsolete. Superseded by [IDimension::GetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~GetValue3.html), [IDimension::IGetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~IGetValue3.html), [IDimension::ISetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~ISetValue3.html), and [IDimension::SetValue3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDimension~SetValue3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property Value As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimension
Dim value As System.Double

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.double Value {get; set;}
```

### C++/CLI

```cpp
property System.double Value {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [Dimension::Value](ms-its:sldworksapivb6.chm::/sldworks~Dimension~Value.html).

## See Also

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.html)
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.html)
