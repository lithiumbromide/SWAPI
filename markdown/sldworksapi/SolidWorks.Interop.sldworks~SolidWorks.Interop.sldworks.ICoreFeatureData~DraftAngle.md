---
title: "DraftAngle Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "DraftAngle"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftAngle.html"
---

# DraftAngle Property (ICoreFeatureData)

Gets or sets the angle of the draft for this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftAngle As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As System.Double

instance.DraftAngle = value

value = instance.DraftAngle
```

### C#

```csharp
System.double DraftAngle {get; set;}
```

### C++/CLI

```cpp
property System.double DraftAngle {
   System.double get();
   void set (    System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Angle of draft

## VBA Syntax

See [CoreFeatureData::DraftAngle](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~DraftAngle.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## Remarks

To set this property, [ICoreFeatureData::UseDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoreFeatureData~UseDraft.html) must be true.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)
[ICoreFeatureData::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftOutward.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
