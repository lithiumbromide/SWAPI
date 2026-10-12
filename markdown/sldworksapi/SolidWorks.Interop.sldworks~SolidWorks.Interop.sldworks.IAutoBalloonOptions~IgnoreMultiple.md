---
title: "IgnoreMultiple Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "IgnoreMultiple"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~IgnoreMultiple.html"
---

# IgnoreMultiple Property (IAutoBalloonOptions)

Gets and sets whether to create balloons for multiple instances of an item.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreMultiple As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Boolean

instance.IgnoreMultiple = value

value = instance.IgnoreMultiple
```

### C#

```csharp
System.bool IgnoreMultiple {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreMultiple {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to create a balloon for only one instance of an item, false to create multiple balloons for multiple instances of an item

## VBA Syntax

See [AutoBalloonOptions::CustomSize](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~CustomSize.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
