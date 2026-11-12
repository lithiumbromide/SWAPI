---
title: "TriadRotationParameters Property (IMoveFaceFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMoveFaceFeatureData"
member: "TriadRotationParameters"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadRotationParameters.html"
---

# TriadRotationParameters Property (IMoveFaceFeatureData)

Gets or sets the rotation parameters for this Move Face feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property TriadRotationParameters As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMoveFaceFeatureData
Dim value As System.Object

instance.TriadRotationParameters = value

value = instance.TriadRotationParameters
```

### C#

```csharp
System.object TriadRotationParameters {get; set;}
```

### C++/CLI

```cpp
property System.Object^ TriadRotationParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of six doubles (see **Remarks**)

## VBA Syntax

See [MoveFaceFeatureData::TriadRotationParameters](ms-its:sldworksapivb6.chm::/sldworks~MoveFaceFeatureData~TriadRotationParameters.html).

## Examples

[Rotate Move Face Feature (VB.NET)](Rotate_Move_Face_Feature_Example_VBNET.htm)
[Rotate Move Face Feature (VBA)](Rotate_MoveFace_Feature_Example_VB.htm)
[Rotate Move Face Feature (C#)](Rotate_Move_Face_Feature_Example_CSharp.htm)

## Remarks

The first three doubles are the X, Y, and Z rotation origin parameters. The remaining three doubles are the X, Y, and Z rotation angle parameters.

## See Also

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.html)
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.html)
[IMoveFaceFeatureData::IGetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadRotationParameters.html)
[IMoveFaceFeatureData::ISetTriadRotationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadRotationParameters.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
