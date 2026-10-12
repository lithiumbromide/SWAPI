---
title: "InsertMagneticLine Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "InsertMagneticLine"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~InsertMagneticLine.html"
---

# InsertMagneticLine Property (IAutoBalloonOptions)

Gets and sets whether to insert magnetic lines with balloons.

## Syntax

### Visual Basic (Declaration)

```vb
Property InsertMagneticLine As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Boolean

instance.InsertMagneticLine = value

value = instance.InsertMagneticLine
```

### C#

```csharp
System.bool InsertMagneticLine {get; set;}
```

### C++/CLI

```cpp
property System.bool InsertMagneticLine {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to insert magnetic lines, false to not; only valid when [IAutoBalloonOptons::Layout](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions~Layout.html) is not set to [swBalloonLayoutType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBalloonLayoutType_e.html).swDetailingBalloonLayout_Circle

## VBA Syntax

See [AutoBalloonOptions::InsertMagneticLine](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~InsertMagneticLine.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
