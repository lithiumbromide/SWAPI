---
title: "Depth Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "Depth"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~Depth.html"
---

# Depth Property (ICoreFeatureData)

Gets or sets the depth in the specified direction of this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property Depth( _
   ByVal Index As System.Integer _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim Index As System.Integer
Dim value As System.Double

instance.Depth(Index) = value

value = instance.Depth(Index)
```

### C#

```csharp
System.double Depth(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.double Depth {
   System.double get(System.int Index);
   void set (System.int Index, System.double value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Direction to extract core as defined in [swCoreFeatureDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCoreFeatureDirection_e.html)

### Property Value

Depth

## VBA Syntax

See [CoreFeatureData::Depth](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~Depth.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
