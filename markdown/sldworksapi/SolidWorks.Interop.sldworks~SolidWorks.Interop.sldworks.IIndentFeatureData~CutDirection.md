---
title: "CutDirection Property (IIndentFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IIndentFeatureData"
member: "CutDirection"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~CutDirection.html"
---

# CutDirection Property (IIndentFeatureData)

Gets or sets whether to flip the side of the cut for this indent feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property CutDirection As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IIndentFeatureData
Dim value As System.Boolean

instance.CutDirection = value

value = instance.CutDirection
```

### C#

```csharp
System.bool CutDirection {get; set;}
```

### C++/CLI

```cpp
property System.bool CutDirection {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to flip the side of the cut, false to not

## VBA Syntax

See [IndentFeatureData::CutDirection](ms-its:sldworksapivb6.chm::/sldworks~IndentFeatureData~CutDirection.html).

## See Also

[IIndentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData.html)
[IIndentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData_members.html)
[IIndentFeatureData::IsCut Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IIndentFeatureData~IsCut.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
