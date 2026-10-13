---
title: "DraftOutward Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "DraftOutward"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftOutward.html"
---

# DraftOutward Property (ICoreFeatureData)

Gets or sets whether draft is applied outward on this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DraftOutward As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As System.Boolean

instance.DraftOutward = value

value = instance.DraftOutward
```

### C#

```csharp
System.bool DraftOutward {get; set;}
```

### C++/CLI

```cpp
property System.bool DraftOutward {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if draft is applied outward, false if not

## VBA Syntax

See [CoreFeatureData::DraftOutward](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~DraftOutward.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## Remarks

To set this property, [ICoreFeatureData::UseDraft](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoreFeatureData~UseDraft.html) must be true.

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)
[ICoreFeatureData::DraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftAngle.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
