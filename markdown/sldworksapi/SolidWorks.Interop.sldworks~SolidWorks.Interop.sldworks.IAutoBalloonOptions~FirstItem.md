---
title: "FirstItem Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "FirstItem"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~FirstItem.html"
---

# FirstItem Property (IAutoBalloonOptions)

Gets and sets the first balloon item.

## Syntax

### Visual Basic (Declaration)

```vb
Property FirstItem As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Object

instance.FirstItem = value

value = instance.FirstItem
```

### C#

```csharp
System.object FirstItem {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FirstItem {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AutoBalloonOptions::FirstItem](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~FirstItem.html).

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
