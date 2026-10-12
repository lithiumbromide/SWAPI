---
title: "GetFeature Method (IGeneralTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IGeneralTableFeature"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature~GetFeature.html"
---

# GetFeature Method (IGeneralTableFeature)

Gets the general table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralTableFeature
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

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [GeneralTableFeature::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~GeneralTableFeature~GetFeature.html).

## Examples

[Get General Table Feature (C#)](Get_General_Table_Feature_Example_CSharp.htm)
[Get General Table Feature (VB.NET)](Get_General_Table_Feature_Example_VBNET.htm)
[Get General Table Feature (VBA)](Get_General_Table_Feature_Example_VB.htm)

## See Also

[IGeneralTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature.html)
[IGeneralTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralTableFeature_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
