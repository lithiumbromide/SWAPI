---
title: "IPMIDimensionItem Interface"
project: "SOLIDWORKS API Help"
interface: "IPMIDimensionItem"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem.html"
---

# IPMIDimensionItem Interface

Allows access to a Product and Manufacturing Information (PMI) dimension item.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPMIDimensionItem
```

### Visual Basic (Usage)

```vb
Dim instance As IPMIDimensionItem
```

### C#

```csharp
public interface IPMIDimensionItem
```

### C++/CLI

```cpp
public interface class IPMIDimensionItem
```

## VBA Syntax

See [PMIDimensionItem](ms-its:sldworksapivb6.chm::/sldworks~PMIDimensionItem.html).

## Examples

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.html) example.

## Remarks

This API does not yet support the fit tolerance information typically associated with shafts in holes, such as classification, hole fit, and shaft fit.

If [IPMIDimensionItem::TolType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem~TolType.html) returns [swTolType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTolType_e.html):

- swTolFIT
- swTolFITTOLONLY
- swTolFITWITHTOL

then no classfication, hole fit, or shaft fit data is available through this API.

## Accessors

[IPMIDimensionData::GetDimensionItemAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionData~GetDimensionItemAtIndex.html)

## Access Diagram

[PMIDimensionItem](SWObjectModel.pdf#PMIDimensionItem)

## See Also

[IPMIDimensionItem Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDimensionItem_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
