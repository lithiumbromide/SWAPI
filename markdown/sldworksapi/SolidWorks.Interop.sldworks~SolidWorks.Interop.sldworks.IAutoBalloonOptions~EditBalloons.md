---
title: "EditBalloons Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "EditBalloons"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~EditBalloons.html"
---

# EditBalloons Property (IAutoBalloonOptions)

Gets and sets whether to use edit balloon options when creating the auto balloon.

## Syntax

### Visual Basic (Declaration)

```vb
Property EditBalloons As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Boolean

instance.EditBalloons = value

value = instance.EditBalloons
```

### C#

```csharp
System.bool EditBalloons {get; set;}
```

### C++/CLI

```cpp
property System.bool EditBalloons {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to use edit balloon option as specified in [IAutoBalloonOption::EditBalloonOption](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions~EditBalloonOption.html), false to not

## VBA Syntax

See [AutoBalloonOptions::EditBalloons](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~EditBalloons.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2013 FCS, Revision Number 21.0
