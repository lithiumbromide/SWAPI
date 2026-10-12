---
title: "TangentPropagation Property (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "TangentPropagation"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~TangentPropagation.html"
---

# TangentPropagation Property (IWeldmentBeadFeatureData)

Gets or sets whether to propagate the weld bead along the tangent.

## Syntax

### Visual Basic (Declaration)

```vb
Property TangentPropagation As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim value As System.Boolean

instance.TangentPropagation = value

value = instance.TangentPropagation
```

### C#

```csharp
System.bool TangentPropagation {get; set;}
```

### C++/CLI

```cpp
property System.bool TangentPropagation {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to propagate the weld bead along the tangent, false to not

## VBA Syntax

See [WeldmentBeadFeatureData::TangentPropagation](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~TangentPropagation.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::BeadLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadLength.html)
[IWeldmentBeadFeatureData::BeadPitch Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~BeadPitch.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
