---
title: "GetAxisType Method (IRevolveFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData2"
member: "GetAxisType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~GetAxisType.html"
---

# GetAxisType Method (IRevolveFeatureData2)

Gets the type of axis of revolution for this revolve feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAxisType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData2
Dim value As System.Integer

value = instance.GetAxisType()
```

### C#

```csharp
System.int GetAxisType()
```

### C++/CLI

```cpp
System.int GetAxisType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of axis as defined in [swSelectType_e:](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

- swSelDATUMAXES
- swSelEDGES
- swSelSKETCHSEGS

## VBA Syntax

See [RevolveFeatureData2::GetAxisType](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData2~GetAxisType.html).

## Examples

[Get Axis of Revolve Feature (VBA)](Get_Axis_of_Revolve_Feature_Example_VB.htm)

## See Also

[IRevolveFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2.html)
[IRevolveFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2_members.html)
[IRevolveFeatureData2::Axis Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData2~Axis.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
