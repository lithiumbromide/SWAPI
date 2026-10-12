---
title: "EndCondition Property (ICoreFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ICoreFeatureData"
member: "EndCondition"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData~EndCondition.html"
---

# EndCondition Property (ICoreFeatureData)

Gets or sets the end condition in the specified direction for this core feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property EndCondition( _
   ByVal Index As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICoreFeatureData
Dim Index As System.Integer
Dim value As System.Integer

instance.EndCondition(Index) = value

value = instance.EndCondition(Index)
```

### C#

```csharp
System.int EndCondition(
   System.int Index
) {get; set;}
```

### C++/CLI

```cpp
property System.int EndCondition {
   System.int get(System.int Index);
   void set (System.int Index, System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Direction of end conditions as defined in [swCoreFeatureDirection_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCoreFeatureDirection_e.html)

### Property Value

Type of end conditions as defined in [swEndConditions_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEndConditions_e.html) (see **Remarks**)

## VBA Syntax

See [CoreFeatureData::EndCondition](ms-its:sldworksapivb6.chm::/sldworks~CoreFeatureData~EndCondition.html).

## Examples

[Get Core Feature Data (C#)](Get_Core_Feature_Example_CSharp.htm)
[Get Core Feature Data (VB.NET)](Get_Core_Feature_Example_VBNET.htm)
[Get Core Feature Data (VBA)](Get_Core_Feature_Example_VB.htm)

## Remarks

Valid end conditions are swEndConditions_e:

- swEndCondBlind
- swEndCondThroughAll
- swEndCondThroughNext

## See Also

[ICoreFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData.html)
[ICoreFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoreFeatureData_members.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
