---
title: "MoveType Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "MoveType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.html"
---

# MoveType Property (IMoveFaceFeatureData)

Gets or sets the type of Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MoveType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Integer

instance.MoveType = value

value = instance.MoveType
```

### C#

```csharp
System.int MoveType {get; set;}
```

### C++/CLI

```cpp
property System.int MoveType {
   System.int get();
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type of move as defined in [swMoveFaceType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMoveFaceType_e.html)

## VBA Syntax

See [MoveFaceFeatureData::MoveType](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~MoveType.html).

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
