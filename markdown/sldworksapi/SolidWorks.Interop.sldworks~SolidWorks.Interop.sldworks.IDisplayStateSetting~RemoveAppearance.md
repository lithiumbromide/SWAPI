---
title: "RemoveAppearance Property (IDisplayStateSetting)"
project: "SOLIDWORKS API Help"
interface: "IDisplayStateSetting"
member: "RemoveAppearance"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~RemoveAppearance.html"
---

# RemoveAppearance Property (IDisplayStateSetting)

Gets or sets whether to remove appearances for this display state setting.

## Syntax

### Visual Basic (Declaration)

```vb
Property RemoveAppearance As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDisplayStateSetting
Dim value As System.Boolean

instance.RemoveAppearance = value

value = instance.RemoveAppearance
```

### C#

```csharp
System.bool RemoveAppearance {get; set;}
```

### C++/CLI

```cpp
property System.bool RemoveAppearance {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to remove appearances, false to not

## VBA Syntax

See [DisplayStateSetting::RemoveAppearance](ms-its:sldworksapivb6.chm::/sldworks~DisplayStateSetting~RemoveAppearance.html).

## See Also

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.html)
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
