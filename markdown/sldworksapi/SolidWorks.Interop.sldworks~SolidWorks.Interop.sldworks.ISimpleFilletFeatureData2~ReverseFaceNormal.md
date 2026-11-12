---
title: "ReverseFaceNormal Property (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "ReverseFaceNormal"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~ReverseFaceNormal.html"
---

# ReverseFaceNormal Property (ISimpleFilletFeatureData2)

Gets or sets the Reverse Face Normal option when creating a face fillet between surface bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property ReverseFaceNormal( _
   ByVal WhichFaceList As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2
Dim WhichFaceList As System.Integer
Dim value As System.Boolean

instance.ReverseFaceNormal(WhichFaceList) = value

value = instance.ReverseFaceNormal(WhichFaceList)
```

### C#

```csharp
System.bool ReverseFaceNormal(
   System.int WhichFaceList
) {get; set;}
```

### C++/CLI

```cpp
property System.bool ReverseFaceNormal {
   System.bool get(System.int WhichFaceList);
   void set (System.int WhichFaceList, System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichFaceList`: Face for Reverse Face Normal option as defined in [swSimpleFilletWhichFaces_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSimpleFilletWhichFaces_e.html)

### Property Value

True if the Reverse Face Normal option is enabled, false if not

## VBA Syntax

See [SimpleFilletFeatureData2::ReverseFaceNormal](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~ReverseFaceNormal.html).

## Examples

See [ISimpleFilletFeatureData2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleHoleFeatureData2.html) examples.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
