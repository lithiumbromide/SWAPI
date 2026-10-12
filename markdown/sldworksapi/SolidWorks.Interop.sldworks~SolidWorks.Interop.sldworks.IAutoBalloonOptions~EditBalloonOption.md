---
title: "EditBalloonOption Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "EditBalloonOption"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloonOption.html"
---

# EditBalloonOption Property (IAutoBalloonOptions)

Gets and sets edit balloon options.

## Syntax

### Visual Basic (Declaration)

```vb
Property EditBalloonOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Integer

instance.EditBalloonOption = value

value = instance.EditBalloonOption
```

### C#

```csharp
System.int EditBalloonOption {get; set;}
```

### C++/CLI

```cpp
property System.int EditBalloonOption {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Edit balloon option as specified in [swEditBalloonOption_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEditBalloonOption_e.html); valid only if [IAutoBalloonOptions::EditBalloons](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions~EditBalloons.html) is true

## VBA Syntax

See [AutoBalloonOptions::EditBalloonOption](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~EditBalloonOption.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
