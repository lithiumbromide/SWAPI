---
title: "GetFeature Method (ITitleBlockTableFeature)"
project: "SOLIDWORKS API Help"
interface: "ITitleBlockTableFeature"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature~GetFeature.html"
---

# GetFeature Method (ITitleBlockTableFeature)

Provides access to the feature associated with this title block table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As ITitleBlockTableFeature
Dim value As Feature

value = instance.GetFeature()
```

### C#

```csharp
Feature GetFeature()
```

### C++/CLI

```cpp
Feature^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[Feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [TitleBlockTableFeature::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~TitleBlockTableFeature~GetFeature.html).

## Examples

[Get Title Block Tables (VBA)](Get_Title_Block_Tables_Example_VB6.htm)
[Get Title Block Tables (VB.NET)](Get_Title_Block_Tables_Example_VBNET.htm)
[Get Title Block Tables (C#)](Get_Title_Block_Tables_Example_CSharp.htm)

## See Also

[ITitleBlockTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature.html)
[ITitleBlockTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITitleBlockTableFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
