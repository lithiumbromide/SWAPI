---
title: "LeaderAttachmentToFaces Property (IAutoBalloonOptions)"
project: "SOLIDWORKS API Help"
interface: "IAutoBalloonOptions"
member: "LeaderAttachmentToFaces"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions~LeaderAttachmentToFaces.html"
---

# LeaderAttachmentToFaces Property (IAutoBalloonOptions)

Gets and sets whether to attach balloons to faces.

## Syntax

### Visual Basic (Declaration)

```vb
Property LeaderAttachmentToFaces As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAutoBalloonOptions
Dim value As System.Boolean

instance.LeaderAttachmentToFaces = value

value = instance.LeaderAttachmentToFaces
```

### C#

```csharp
System.bool LeaderAttachmentToFaces {get; set;}
```

### C++/CLI

```cpp
property System.bool LeaderAttachmentToFaces {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to attach balloons to faces; false to attach balloons to edges

## VBA Syntax

See [AutoBalloonOptions::LeaderAttachmentToFaces](ms-its:sldworksapivb6.chm::/sldworks~AutoBalloonOptions~LeaderAttachmentToFaces.html).

## Examples

See [IAutoBalloonOptions](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAutoBalloonOptions.html) examples.

## Remarks

See the SOLIDWORKS Help for additional details about autoballoons.

## See Also

[IAutoBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions.html)
[IAutoBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAutoBalloonOptions_members.html)

## Availability

SOLIDWORKS 2012 FCS, Revision Number 20.0
