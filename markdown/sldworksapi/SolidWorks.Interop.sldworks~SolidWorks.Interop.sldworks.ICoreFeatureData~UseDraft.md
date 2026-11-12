---
title: "UseDraft Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "UseDraft"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~UseDraft.html"
---

# UseDraft Property (ICoreFeatureData)

Gets or sets whether draft is applied to this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property UseDraft As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim value As System.Boolean

instance.UseDraft = value

value = instance.UseDraft
```

### C#

```csharp
System.bool UseDraft {get; set;}
```

### C++/CLI

```cpp
property System.bool UseDraft {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to apply draft, false to not

## VBA Syntax

See [CoreFeatureData::UseDraft](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~UseDraft.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)
[ICoreFeatureData::DraftAngle Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftAngle.html)
[ICoreFeatureData::DraftOutward Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~DraftOutward.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
